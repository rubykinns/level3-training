# =============================================================================
# app.py — Level 3 Automation AI Training System
# Groups 3 & 4 only (Groups 1 & 2 use separate media)
#
# Flow:
#   Welcome → AI Conversation (all topics) → Quiz → Feedback → Done
#
# Group 3: AI chat + Structured feedback (pre-written, same for all)
# Group 4: AI chat + Personalized feedback (AI-generated, age/experience-based)
# Group A/B: within each group, based on Qualtrics pre-knowledge score
#
# Run with: streamlit run app.py
# =============================================================================

import streamlit as st
import json
import os
from datetime import datetime

# Streamlit Cloud Secrets에서 API 키 읽기
try:
    import config
    config.ANTHROPIC_API_KEY = st.secrets["ANTHROPIC_API_KEY"]
except Exception:
    pass 

st.set_page_config(
    page_title="L3 Automation Training",
    page_icon="🚗",
    layout="centered"
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.main { background-color: #f8f9fb; }

.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #1d4ed8, #3b82f6);
    border-radius: 99px;
}

/* ── Chat bubbles ── */
.bubble-ai {
    display: flex; align-items: flex-start; gap: 10px; margin: 10px 0;
}
.avatar {
    width: 36px; height: 36px; border-radius: 50%;
    background: #1d4ed8; color: white;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; flex-shrink: 0; margin-top: 2px;
}
.bubble-ai-text {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 4px 18px 18px 18px;
    padding: 12px 16px;
    max-width: 88%;
    line-height: 1.7;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.bubble-user {
    display: flex; justify-content: flex-end; margin: 10px 0;
}
.bubble-user-text {
    background: #1d4ed8; color: white;
    border-radius: 18px 4px 18px 18px;
    padding: 12px 16px; max-width: 80%; line-height: 1.7;
}

/* ── Stage label ── */
.stage-label {
    font-size: 11px; font-weight: 600;
    letter-spacing: 2px; text-transform: uppercase;
    color: #9ca3af; margin-bottom: 4px;
}

/* ── Feedback ── */
.feedback-structured {
    background: #f0fdf4; border: 1px solid #86efac;
    border-radius: 12px; padding: 20px 24px;
    line-height: 1.8; margin: 12px 0;
}
.feedback-personalized {
    background: #eff6ff; border: 1px solid #93c5fd;
    border-radius: 12px; padding: 20px 24px;
    line-height: 1.8; margin: 12px 0;
}

/* ── Topic pills ── */
.topic-done { 
    display: inline-block; padding: 4px 12px; border-radius: 99px;
    background: #dcfce7; color: #166534;
    font-size: 12px; font-weight: 600; margin: 3px;
}
.topic-active {
    display: inline-block; padding: 4px 12px; border-radius: 99px;
    background: #dbeafe; color: #1d4ed8;
    font-size: 12px; font-weight: 600; margin: 3px;
}
.topic-pending {
    display: inline-block; padding: 4px 12px; border-radius: 99px;
    background: #f3f4f6; color: #9ca3af;
    font-size: 12px; margin: 3px;
}
</style>
""", unsafe_allow_html=True)

# ── Config ────────────────────────────────────────────────────────────────────
try:
    from config import (
        ANTHROPIC_API_KEY, MODEL,
        TRAINING_TOPICS,
        SCRIPTED_TOPICS,
        QUIZ_QUESTIONS,
        STRUCTURED_FEEDBACK_GROUP_A,
        STRUCTURED_FEEDBACK_GROUP_B,
        CHATBOT_SYSTEM_PROMPT,
    )
except ImportError as e:
    st.error(f"⚠️ Cannot load config.py: {e}")
    st.stop()

# ── Session state ─────────────────────────────────────────────────────────────
defaults = {
    "stage": "welcome",       # welcome | chat | quiz | feedback | done
    "participant_id": "",
    "training_group": None,   # "3" or "4"
    "knowledge_group": None,  # "A" or "B"
    "age": None,              # Group 4 only
    "driving_years": None,    # Group 4 only
    "topic_index": 0,         # which training topic we're on
    "script_step": 0,         # Group 3: which step within current topic script
    "chat_history": [],       # full conversation across all topics
    "quiz_answers": [],
    "feedback_text": "",
    "session_start": None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Claude API ────────────────────────────────────────────────────────────────
def call_claude(system: str, messages: list) -> str:
    import urllib.request, urllib.error
    payload = {"model": MODEL, "max_tokens": 1000, "system": system, "messages": messages}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=data,
        headers={"Content-Type": "application/json",
                 "x-api-key": ANTHROPIC_API_KEY,
                 "anthropic-version": "2023-06-01"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return " ".join(b["text"] for b in result.get("content", []) if b.get("type") == "text")
    except urllib.error.HTTPError as e:
        return f"[API Error {e.code}]: {e.read().decode()}"
    except Exception as e:
        return f"[Error]: {str(e)}"

# ── Helpers ───────────────────────────────────────────────────────────────────
def participant_context():
    ctx = (f"Participant profile — "
           f"Training Group: {st.session_state.training_group} "
           f"({'Structured Feedback' if st.session_state.training_group == '3' else 'Personalized Feedback'}), "
           f"Knowledge Group: {st.session_state.knowledge_group} "
           f"({'Foundation' if st.session_state.knowledge_group == 'A' else 'Advanced'}).")
    if st.session_state.training_group == "4":
        ctx += (f" Age: {st.session_state.age}. "
                f"Driving experience: {st.session_state.driving_years} year(s).")
    return ctx

def render_chat(history, scripted_topics=None, topic_idx=0):
    """Render chat history. For Group 3, also show images attached to steps."""
    # Build a map of which assistant messages have images
    # assistant messages at positions 0, 2, 4... in the history correspond to script steps
    ai_msg_count = 0
    for msg in history:
        if msg["role"] == "assistant":
            st.markdown(f"""<div class="bubble-ai">
  <div class="avatar">🤖</div>
  <div class="bubble-ai-text">{msg["content"]}</div>
</div>""", unsafe_allow_html=True)
            # Check if this message has an associated image (Group 3 only)
            if scripted_topics and "image" in msg:
                img_path = msg["image"]
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
            ai_msg_count += 1
        else:
            st.markdown(f"""<div class="bubble-user">
  <div class="bubble-user-text">{msg["content"]}</div>
</div>""", unsafe_allow_html=True)

def render_topic_progress():
    topics = TRAINING_TOPICS
    idx = st.session_state.topic_index
    pills = ""
    for i, t in enumerate(topics):
        if i < idx:
            pills += f'<span class="topic-done">✓ {t["title"]}</span>'
        elif i == idx:
            pills += f'<span class="topic-active">▶ {t["title"]}</span>'
        else:
            pills += f'<span class="topic-pending">{t["title"]}</span>'
    st.markdown(pills, unsafe_allow_html=True)

def save_log():
    os.makedirs("logs", exist_ok=True)
    pid = st.session_state.participant_id
    log = {
        "participant_id": pid,
        "training_group": st.session_state.training_group,
        "knowledge_group": st.session_state.knowledge_group,
        "age": st.session_state.age,
        "driving_years": st.session_state.driving_years,
        "session_start": st.session_state.session_start,
        "session_end": datetime.now().isoformat(),
        "quiz_answers": st.session_state.quiz_answers,
        "feedback": st.session_state.feedback_text,
    }
    fname = f"logs/{pid}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)


# =============================================================================
# STAGE: WELCOME
# =============================================================================
if st.session_state.stage == "welcome":
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 🚗 Level 3 Automation\n### Driver Training System")
    st.markdown("<br>", unsafe_allow_html=True)

    pid = st.text_input("Participant ID", placeholder="e.g. P001")

    training_group = st.radio(
        "Training Group",
        options=["Group 3 — AI with Structured Feedback",
                 "Group 4 — AI with Personalized Feedback"],
    )

    knowledge_group = st.radio(
        "Knowledge Group (from Qualtrics pre-test)",
        options=["Group A — Foundation", "Group B — Advanced"],
    )

    # Group 4 only: collect age & driving experience
    age = None
    driving_years = None
    if "Group 4" in training_group:
        st.markdown("---")
        st.markdown("**Additional information for personalized feedback:**")
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=18, max_value=90, value=30, step=1)
        with col2:
            driving_years = st.number_input("Years of Driving Experience",
                                            min_value=0, max_value=70, value=5, step=1)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Start Training →", type="primary", use_container_width=True):
        if not pid.strip():
            st.warning("Please enter your Participant ID.")
        else:
            st.session_state.participant_id = pid.strip()
            st.session_state.training_group = "3" if "Group 3" in training_group else "4"
            st.session_state.knowledge_group = "A" if "Group A" in knowledge_group else "B"
            st.session_state.age = age
            st.session_state.driving_years = driving_years
            st.session_state.session_start = datetime.now().isoformat()

            tg = st.session_state.training_group
            kg = st.session_state.knowledge_group

            if tg == "3":
                # Group 3: single script — no A/B split
                first_step = SCRIPTED_TOPICS[0]["steps"][0]
                first_entry = {"role": "assistant", "content": first_step["message"]}
                if "image" in first_step:
                    first_entry["image"] = first_step["image"]
                st.session_state.chat_history = [first_entry]
                st.session_state.script_step = 0
            else:
                # Group 4: AI generates opening message
                topic = TRAINING_TOPICS[0]
                opening_prompt = (
                    f"{participant_context()}\n\n"
                    f"You are starting the training. The first topic is: '{topic['title']}'.\n"
                    f"Content to teach:\n{topic['content_group_' + kg.lower()]}\n\n"
                    f"Greet the participant warmly and begin teaching this topic conversationally. "
                    f"Be engaging and clear. End with a question to check understanding or invite discussion."
                )
                with st.spinner("Starting your training session..."):
                    opening = call_claude(CHATBOT_SYSTEM_PROMPT, [{"role": "user", "content": opening_prompt}])
                st.session_state.chat_history = [{"role": "assistant", "content": opening}]

            st.session_state.stage = "chat"
            st.rerun()


# =============================================================================
# STAGE: CHAT
# Group 3: pre-scripted messages + Yes/No buttons (identical for all participants)
# Group 4: AI-generated conversation + free text input
# =============================================================================
elif st.session_state.stage == "chat":
    topics = TRAINING_TOPICS
    idx = st.session_state.topic_index
    topic = topics[idx]
    kg = st.session_state.knowledge_group
    tg = st.session_state.training_group

    # ── Header ──
    st.markdown(f'<div class="stage-label">AI Training &nbsp;·&nbsp; Training Group {tg} &nbsp;·&nbsp; Knowledge Group {kg}</div>', unsafe_allow_html=True)
    st.progress(idx / len(topics))
    st.markdown("<br>", unsafe_allow_html=True)
    render_topic_progress()
    st.markdown("---")

    render_chat(st.session_state.chat_history, scripted_topics=SCRIPTED_TOPICS if tg == "3" else None)

    is_last_topic = (idx == len(topics) - 1)

    # =========================================================================
    # GROUP 3 — Scripted messages, free text input, NO A/B split
    # =========================================================================
    if tg == "3":
        script = SCRIPTED_TOPICS[idx]["steps"]
        step = st.session_state.script_step
        is_last_step = (step >= len(script) - 1)

        NO_KEYWORDS = {"no", "again", "explain", "unclear", "don't", "dont",
                       "didn't", "didnt", "not", "confused", "confusing", "help"}

        user_input = st.text_input(
            "Your response:",
            placeholder="Type your response...",
            key=f"g3_input_{idx}_{step}_{len(st.session_state.chat_history)}"
        )

        if st.button("Send", use_container_width=True):
            if user_input.strip():
                st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})

                words = set(user_input.lower().split())
                needs_reexplain = bool(words & NO_KEYWORDS)

                if needs_reexplain:
                    no_reply = script[step].get("no_followup",
                        "No problem! Let me explain that again in a different way.")
                    st.session_state.chat_history.append({"role": "assistant", "content": no_reply})
                else:
                    yes_reply = script[step].get("yes_followup")
                    if yes_reply:
                        st.session_state.chat_history.append({"role": "assistant", "content": yes_reply})

                    if is_last_step:
                        if is_last_topic:
                            st.session_state.stage = "quiz"
                            st.session_state.quiz_answers = []
                        else:
                            next_idx = idx + 1
                            next_script = SCRIPTED_TOPICS[next_idx]["steps"]
                            next_step_data = next_script[0]
                            next_entry = {"role": "assistant", "content": next_step_data["message"]}
                            if "image" in next_step_data:
                                next_entry["image"] = next_step_data["image"]
                            st.session_state.chat_history.append(next_entry)
                            st.session_state.topic_index = next_idx
                            st.session_state.script_step = 0
                    else:
                        next_step = step + 1
                        next_step_data = script[next_step]
                        next_entry = {"role": "assistant", "content": next_step_data["message"]}
                        if "image" in next_step_data:
                            next_entry["image"] = next_step_data["image"]
                        st.session_state.chat_history.append(next_entry)
                        st.session_state.script_step = next_step
                st.rerun()

    # =========================================================================
    # GROUP 4 — AI-generated, free text input
    # =========================================================================
    else:
        user_input = st.text_input(
            "Your response:",
            placeholder="Ask a question or respond to the instructor...",
            key=f"chat_in_{len(st.session_state.chat_history)}"
        )

        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("Send", use_container_width=True):
                if user_input.strip():
                    st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})
                    system = (
                        CHATBOT_SYSTEM_PROMPT + "\n\n"
                        + participant_context() + "\n\n"
                        f"Current topic: '{topic['title']}'. "
                        "Keep responses concise (3-5 sentences). Stay on topic. "
                        "Occasionally ask a follow-up question to maintain engagement."
                    )
                    with st.spinner(""):
                        reply = call_claude(system, st.session_state.chat_history)
                    st.session_state.chat_history.append({"role": "assistant", "content": reply})
                    st.rerun()

        with col2:
            next_label = "Go to Quiz →" if is_last_topic else "Next Topic →"
            if st.button(next_label, type="primary", use_container_width=True):
                if is_last_topic:
                    st.session_state.stage = "quiz"
                    st.session_state.quiz_answers = []
                    st.rerun()
                else:
                    next_idx = idx + 1
                    next_topic = topics[next_idx]
                    transition_prompt = (
                        f"{participant_context()}\n\n"
                        f"You just finished teaching '{topic['title']}'. "
                        f"Now transition smoothly to the next topic: '{next_topic['title']}'.\n"
                        f"Content to teach:\n{next_topic['content_group_' + kg.lower()]}\n\n"
                        f"Briefly wrap up the previous topic and begin the new one conversationally. "
                        f"End with a question."
                    )
                    with st.spinner("Moving to next topic..."):
                        transition = call_claude(CHATBOT_SYSTEM_PROMPT,
                                                [{"role": "user", "content": transition_prompt}])
                    st.session_state.chat_history.append({"role": "assistant", "content": transition})
                    st.session_state.topic_index = next_idx
                    st.rerun()


# =============================================================================
# STAGE: QUIZ — all questions at once, after all training
# =============================================================================
elif st.session_state.stage == "quiz":
    st.markdown(f'<div class="stage-label">Knowledge Check &nbsp;·&nbsp; Training Group {st.session_state.training_group} &nbsp;·&nbsp; Knowledge Group {st.session_state.knowledge_group}</div>', unsafe_allow_html=True)
    st.progress(1.0)
    st.markdown("### 📝 Post-Training Quiz")
    st.caption("Answer all questions below, then submit to receive your feedback.")
    st.markdown("---")

    with st.form("quiz_form"):
        answers = {}
        for i, q in enumerate(QUIZ_QUESTIONS):
            st.markdown(f"**Q{i+1}. {q['q']}**")
            answers[i] = st.radio(
                "",
                options=list(q["options"].keys()),
                format_func=lambda k, q=q: f"{k}.  {q['options'][k]}",
                key=f"qz_{i}",
                index=None,
                label_visibility="collapsed"
            )
            st.markdown("")

        submitted = st.form_submit_button(
            "Submit & Get Feedback →", type="primary", use_container_width=True
        )

    if submitted:
        results = []
        for i, q in enumerate(QUIZ_QUESTIONS):
            selected = answers[i]
            is_correct = selected == q["answer"]
            results.append({
                "question": q["q"],
                "options": q["options"],
                "selected": selected,
                "correct": q["answer"],
                "is_correct": is_correct,
                "explanation": q.get("explanation", "")
            })
        st.session_state.quiz_answers = results
        correct_count = sum(1 for r in results if r["is_correct"])

        # ── Generate feedback based on training group ──
        tg = st.session_state.training_group
        kg = st.session_state.knowledge_group

        if tg == "3":
            # Structured: pre-written feedback from config
            fb_key = f"STRUCTURED_FEEDBACK_GROUP_{kg}"
            feedback = STRUCTURED_FEEDBACK_GROUP_A if kg == "A" else STRUCTURED_FEEDBACK_GROUP_B

        else:
            # Personalized: AI-generated
            wrong_qs = [r for r in results if not r["is_correct"]]
            wrong_summary = "\n".join(
                f"- Q: {r['question']} | Selected: {r['selected']} | Correct: {r['correct']} | Explanation: {r['explanation']}"
                for r in wrong_qs
            ) if wrong_qs else "All answers were correct."

            feedback_prompt = (
                f"{participant_context()}\n\n"
                f"The participant scored {correct_count}/{len(results)} on the post-training quiz "
                f"about Level 3 automation.\n\n"
                f"Incorrect answers:\n{wrong_summary}\n\n"
                f"Write a warm, personalized feedback paragraph (5-7 sentences) that:\n"
                f"1. Acknowledges their score genuinely\n"
                f"2. Addresses specific misconceptions from wrong answers, "
                f"   tailored to Knowledge Group {kg} "
                f"   ({'Foundation level — use simple, relatable language' if kg == 'A' else 'Advanced level — use technical depth'})\n"
                f"3. Connects the feedback naturally to their driving profile "
                f"   ({st.session_state.driving_years} year(s) of experience, age {st.session_state.age})\n"
                f"4. Ends with an encouraging, forward-looking note\n"
                f"Write as one cohesive paragraph. Do not use bullet points."
            )
            with st.spinner("Generating your personalized feedback..."):
                feedback = call_claude(CHATBOT_SYSTEM_PROMPT, [{"role": "user", "content": feedback_prompt}])

        st.session_state.feedback_text = feedback
        st.session_state.stage = "feedback"
        st.rerun()


# =============================================================================
# STAGE: FEEDBACK
# =============================================================================
elif st.session_state.stage == "feedback":
    tg = st.session_state.training_group
    kg = st.session_state.knowledge_group
    results = st.session_state.quiz_answers
    correct_count = sum(1 for r in results if r["is_correct"])

    st.markdown(f'<div class="stage-label">Feedback &nbsp;·&nbsp; Training Group {tg} &nbsp;·&nbsp; Knowledge Group {kg}</div>', unsafe_allow_html=True)
    st.progress(1.0)
    st.markdown("### 🎯 Your Feedback")
    st.markdown("---")

    # Score
    col1, col2, col3 = st.columns(3)
    col1.metric("Quiz Score", f"{correct_count} / {len(results)}")
    col2.metric("Training Group", f"Group {tg}")
    col3.metric("Knowledge Group", f"Group {kg}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Feedback bubble
    feedback_class = "feedback-structured" if tg == "3" else "feedback-personalized"
    label = "📋 Structured Feedback" if tg == "3" else "✨ Personalized Feedback"
    st.markdown(f"**{label}**")
    st.markdown(f"""
<div class="bubble-ai">
  <div class="avatar">🤖</div>
  <div class="bubble-ai-text {feedback_class}">{st.session_state.feedback_text}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Answer review
    with st.expander("📖 Review all answers"):
        for r in results:
            icon = "✅" if r["is_correct"] else "❌"
            st.markdown(f"{icon} **{r['question']}**")
            if not r["is_correct"]:
                st.markdown(f"&nbsp;&nbsp;&nbsp;Your answer: `{r['selected']}` &nbsp;|&nbsp; Correct: `{r['correct']}`")
                if r["explanation"]:
                    st.markdown(f"&nbsp;&nbsp;&nbsp;💡 {r['explanation']}")
            st.markdown("")

    if st.button("Finish →", type="primary", use_container_width=True):
        save_log()
        st.session_state.stage = "done"
        st.rerun()


# =============================================================================
# STAGE: DONE
# =============================================================================
elif st.session_state.stage == "done":
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## ✅ Training Complete!")
    st.markdown(f"**Participant:** {st.session_state.participant_id}")
    st.markdown("<br>", unsafe_allow_html=True)

    results = st.session_state.quiz_answers
    correct_count = sum(1 for r in results if r["is_correct"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Quiz Score", f"{correct_count}/{len(results)}" if results else "—")
    col2.metric("Training Group", f"Group {st.session_state.training_group}")
    col3.metric("Knowledge Group", f"Group {st.session_state.knowledge_group}")

    st.success("✅ Session saved. Please let the experimenter know you are done.")

    if st.button("Start New Participant", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
