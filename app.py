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
.stRadio label p {
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)
 
# ── Config ────────────────────────────────────────────────────────────────────
try:
    from config import (
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
    "topic_index": 0,         # which training topic we're on
    "script_step": 0,         # Group 3: which step within current topic script
    "chat_history": [],       # full conversation across all topics
    "quiz_answers": [],
    "quiz_order": [],       # randomized question indices
    "quiz_q_index": 0,      # current question position
    "quiz_step": "question", # "question" | "feedback"
    "current_answer": {},
    "feedback_text": "",
    "session_start": None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v
 
# ── Developer Sidebar (hidden from participants) ──────────────────────────────
with st.sidebar:
    st.markdown('### 🛠️ Developer Tools')
    st.caption('Not visible to participants during the study.')
    st.markdown('---')
 
    dev_tg = st.selectbox('Training Group', ['3', '4'], key='dev_tg')
    dev_kg = st.selectbox('Knowledge Group', ['A', 'B'], key='dev_kg')
 
    if st.button('⏭️ Skip to Quiz', use_container_width=True):
        st.session_state.participant_id = 'DEV_TEST'
        st.session_state.training_group = dev_tg
        st.session_state.knowledge_group = dev_kg
        st.session_state.session_start = datetime.now().isoformat()
        st.session_state.stage = 'quiz'
        st.session_state.quiz_answers = []
        st.session_state.quiz_order = []
        st.session_state.quiz_q_index = 0
        st.session_state.quiz_step = 'question'
        st.session_state.current_answer = {}
        st.rerun()
 
    if st.button('⏭️ Skip to Feedback', use_container_width=True):
        import random as _random
        st.session_state.participant_id = 'DEV_TEST'
        st.session_state.training_group = dev_tg
        st.session_state.knowledge_group = dev_kg
        st.session_state.session_start = datetime.now().isoformat()
        dummy = []
        for q in QUIZ_QUESTIONS:
            keys = list(q['options'].keys())
            selected = q['answer'] if _random.random() > 0.4 else _random.choice(keys)
            dummy.append({
                'question': q['q'],
                'options': q['options'],
                'selected': selected,
                'correct': q['answer'],
                'is_correct': selected == q['answer'],
                'explanation': q.get('explanation', '')
            })
        st.session_state.quiz_answers = dummy
        st.session_state.feedback_text = ''
        st.session_state.stage = 'feedback'
        st.rerun()
 
    if st.button('🔄 Reset', use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
 
    st.markdown('---')
    st.caption(f"Stage: `{st.session_state.stage}`")
    if st.session_state.training_group:
        st.caption(f"Group: `{st.session_state.training_group}` / `{st.session_state.knowledge_group}`")
 
 
# ── Helpers ───────────────────────────────────────────────────────────────────
def participant_context():
    return (
        f"Participant profile — "
        f"Training Group: {st.session_state.training_group} "
        f"({'Structured Feedback' if st.session_state.training_group == '3' else 'Personalized Feedback'}), "
        f"Knowledge Group: {st.session_state.knowledge_group} "
        f"({'Foundation' if st.session_state.knowledge_group == 'A' else 'Advanced'})."
    )
 
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
 
    knowledge_group = "Group A — Foundation"  # default for Group 3
    if "Group 4" in training_group:
        knowledge_group = st.radio(
            "Knowledge Group",
            options=["Group A — Foundation", "Group B — Advanced"],
    )
 
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Start Training →", type="primary", use_container_width=True):
        if not pid.strip():
            st.warning("Please enter your Participant ID.")
        else:
            st.session_state.participant_id = pid.strip()
            st.session_state.training_group = "3" if "Group 3" in training_group else "4"
            st.session_state.knowledge_group = "A" if "Group A" in knowledge_group else "B"
            st.session_state.session_start = datetime.now().isoformat()
 
            tg = st.session_state.training_group
            kg = st.session_state.knowledge_group
 
            use_script = (tg == "3") or (tg == "4" and kg == "A")
 
            if use_script:
                # Group 3 or Group 4+A: fixed script
                first_step = SCRIPTED_TOPICS[0]["steps"][0]
                first_entry = {"role": "assistant", "content": first_step["message"]}
                if "image" in first_step:
                    first_entry["image"] = first_step["image"]
                st.session_state.chat_history = [first_entry]
                st.session_state.script_step = 0
            else:
                # Group 4+B: use same fixed script
                first_step = SCRIPTED_TOPICS[0]["steps"][0]
                first_entry = {"role": "assistant", "content": first_step["message"]}
                if "image" in first_step:
                    first_entry["image"] = first_step["image"]
                st.session_state.chat_history = [first_entry]
                st.session_state.script_step = 0
 
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
 
    render_chat(st.session_state.chat_history, scripted_topics=SCRIPTED_TOPICS)
 
    is_last_topic = (idx == len(topics) - 1)
 
    # =========================================================================
    # ALL GROUPS — Same scripted training
    # =========================================================================
    if True:
        script = SCRIPTED_TOPICS[idx]["steps"]
        step = st.session_state.script_step
        is_last_step = (step >= len(script) - 1)
 
        NO_KEYWORDS = {"no", "No", "nope", "n", "again", "explain", "unclear", "don't", "dont",
                       "didn't", "didnt", "not", "confused", "confusing", "help"}
 
        user_input = st.text_input(
            "Your response:",
            placeholder="Type your response 'yes' or 'no'",
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
                            st.session_state.quiz_order = []
                            st.session_state.quiz_q_index = 0
                            st.session_state.quiz_step = 'question'
                            st.session_state.current_answer = {}
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
# STAGE: QUIZ — one question at a time, immediate per-question feedback
# =============================================================================
elif st.session_state.stage == "quiz":
    import random
 
    # Initialize random order on first entry
    if not st.session_state.quiz_order:
        order = list(range(len(QUIZ_QUESTIONS)))
        random.shuffle(order)
        st.session_state.quiz_order = order
        st.session_state.quiz_q_index = 0
        st.session_state.quiz_step = "question"
 
    total_qs = len(QUIZ_QUESTIONS)
    q_pos = st.session_state.quiz_q_index
    tg = st.session_state.training_group
    kg = st.session_state.knowledge_group
 
    # ── Header ────────────────────────────────────────────────────────────
    st.markdown(f'<div class="stage-label">Post-Training Quiz &nbsp;·&nbsp; Training Group {tg} &nbsp;·&nbsp; Knowledge Group {kg}</div>', unsafe_allow_html=True)
    st.progress(min((q_pos + 1) / total_qs, 1.0))
 
    # ── All done → summary screen ──────────────────────────────────────────
    if q_pos >= total_qs:
        results = st.session_state.quiz_answers
        correct_count = sum(1 for r in results if r["is_correct"])
        st.markdown("### ✅ Quiz Complete!")
        st.metric("Final Score", f"{correct_count} / {total_qs}")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Finish Training →", type="primary", use_container_width=True):
            save_log()
            st.session_state.stage = "done"
            st.rerun()
 
    # ── Show question ──────────────────────────────────────────────────────
    elif st.session_state.quiz_step == "question":
        q_real_idx = st.session_state.quiz_order[q_pos]
        q = QUIZ_QUESTIONS[q_real_idx]
 
        st.markdown(f"**Question {q_pos + 1} of {total_qs}**")
        st.markdown("---")
        st.markdown(f"### {q['q']}")
        st.markdown("<br>", unsafe_allow_html=True)
 
        choice = st.radio(
            "Select your answer:",
            options=list(q["options"].keys()),
            format_func=lambda k: f"{k}.  {q['options'][k]}",
            key=f"quiz_q_{q_pos}",
            label_visibility="collapsed",
            index=None
        )
 
        if st.button("Submit Answer →", type="primary", use_container_width=True):
            is_correct = choice == q["answer"]
            result = {
                "question": q["q"],
                "options": q["options"],
                "selected": choice,
                "correct": q["answer"],
                "is_correct": is_correct,
                "explanation": q.get("explanation", ""),
                "q_number": q_pos + 1
            }
            st.session_state.quiz_answers.append(result)
            st.session_state.current_answer = result
 
            # Per-question feedback: use fixed text from config.py (no API call)
            # Add "feedback_group_a" and "feedback_group_b" keys to each question in QUIZ_QUESTIONS
            if tg == "4":
                feedback_key = "feedback_group_a" if kg == "A" else "feedback_group_b"
                per_q_feedback = q.get(feedback_key, q.get("explanation", ""))
                st.session_state.current_answer["per_q_feedback"] = per_q_feedback
 
            st.session_state.quiz_step = "feedback"
            st.rerun()
 
    # ── Show per-question feedback ─────────────────────────────────────────
    elif st.session_state.quiz_step == "feedback":
        r = st.session_state.current_answer
        verdict = "✅ Correct!" if r["is_correct"] else "❌ Incorrect"
        verdict_color = "#15803d" if r["is_correct"] else "#dc2626"
        border_color = "#22c55e" if r["is_correct"] else "#ef4444"
        bg_color = "#f0fdf4" if r["is_correct"] else "#fef2f2"
 
        q_number = st.session_state.current_answer.get("q_number", q_pos + 1)
        st.markdown(f"**Question {q_number} of {total_qs}**")
        st.markdown("---")
 
        # ── Question + answers card ────────────────────────────────────────
        # Build options HTML
        options_html = ""
        for key, val in r["options"].items():
            is_selected = key == r["selected"]
            is_correct = key == r["correct"]
 
            if is_correct:
                opt_style = "background:#dcfce7; border:1.5px solid #22c55e; border-radius:8px; padding:8px 12px; margin:4px 0; font-size:18px; color:#15803d; font-weight:600;"
                icon = "✅ "
            elif is_selected and not is_correct:
                opt_style = "background:#fee2e2; border:1.5px solid #ef4444; border-radius:8px; padding:8px 12px; margin:4px 0; font-size:18px; color:#dc2626; font-weight:600;"
                icon = "❌ "
            else:
                opt_style = "background:#f9fafb; border:1.5px solid #e5e7eb; border-radius:8px; padding:8px 12px; margin:4px 0; font-size:18px; color:#9ca3af;"
                icon = ""
 
            options_html += f"<div style='{opt_style}'>{icon}{key}. {val}</div>"
 
        st.markdown(f"""
<div style='background:white; border:1px solid #e5e7eb; border-radius:12px; padding:20px; margin-bottom:12px;'>
  <div style='font-size:11px; font-weight:600; letter-spacing:2px; text-transform:uppercase; color:#9ca3af; margin-bottom:8px;'>Question</div>
  <div style='font-size:18px; font-weight:600; color:#1e293b; margin-bottom:16px;'>{r['question']}</div>
  {options_html}
</div>""", unsafe_allow_html=True)
 
        # ── Verdict + AI feedback card ─────────────────────────────────────
        if tg == "4" and "per_q_feedback" in r:
            feedback_content = r["per_q_feedback"]
        else:
            feedback_content = r["explanation"]
 
        st.markdown(f"""
<div style='background:{bg_color}; border:1px solid {border_color}; border-left:4px solid {border_color}; border-radius:12px; padding:20px; margin-bottom:16px;'>
  <div style='font-size:16px; font-weight:700; color:{verdict_color}; margin-bottom:12px;'>{verdict}</div>
  <div style='display:flex; align-items:flex-start; gap:10px;'>
    <div style='background:#1d4ed8; color:white; border-radius:50%; width:32px; height:32px; display:flex; align-items:center; justify-content:center; font-size:15px; flex-shrink:0;'>🤖</div>
    <div style='font-size:16px; color:#1e293b; line-height:1.8;'>{feedback_content}</div>
  </div>
</div>""", unsafe_allow_html=True)
 
        # ── Next button ────────────────────────────────────────────────────
        next_label = "Next Question →" if q_pos < total_qs else "See Final Score →"
        if st.button(next_label, type="primary", use_container_width=True):
            st.session_state.quiz_q_index += 1
            st.session_state.quiz_step = "question"
            st.rerun()
 
 
 
# =============================================================================
# STAGE: FEEDBACK removed — quiz goes directly to done
 
 
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