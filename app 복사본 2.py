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

# ── Claude API (Group 4 only) ─────────────────────────────────────────────────
def call_claude(system: str, messages: list) -> str:
    import urllib.request, urllib.error, json
    try:
        from config import ANTHROPIC_API_KEY, MODEL
    except ImportError:
        return "[Error: ANTHROPIC_API_KEY not found in config.py]"
    payload = {"model": MODEL, "max_tokens": 600, "system": system, "messages": messages}
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
.stTextInput div[data-testid="InputInstructions"] {
    display: none;
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
        KNOWLEDGE_BASE,
        GROUP4_STYLE_PROMPT_A,
        GROUP4_STYLE_PROMPT_B,
        GROUP4_STYLE_PROMPT_C,
        GROUP4_STYLE_PROMPT_D,
    )
except ImportError as e:
    st.error(f"⚠️ Cannot load config.py: {e}")
    st.stop()
 
# ── Session state ─────────────────────────────────────────────────────────────
defaults = {
    "stage": "welcome",       # welcome | chat | quiz | feedback | done
    "participant_id": "",
    "training_group": None,   # "3" or "4"
    "knowledge_group": None,  # "A"=Low K+Low Trust, "B"=Low K+High Trust, "C"=High K+Low Trust, "D"=High K+High Trust
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
    # Group 4 specific
    "g4_topic_index": 0,      # current SCRIPTED_TOPICS index
    "g4_step_index": 0,       # current step within topic
    "g4_step_delivered": False, # True when current step delivered
    "g4_qa_count": 0,          # Q&A count per step (max 2)
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
    dev_kg = st.selectbox('Knowledge Group', ['A', 'B', 'C', 'D'], key='dev_kg')
 
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
        st.session_state.feedback_shown_at = None
        st.session_state.g4_topic_index = 0
        st.session_state.g4_step_index = 0
        st.session_state.g4_step_delivered = False
        st.session_state.g4_qa_count = 0
        st.session_state.chat_history = []
        st.rerun()
 
    if st.button('⏭️ Skip to Quiz (with answers)', use_container_width=True):
        import random as _random
        st.session_state.participant_id = 'DEV_TEST'
        st.session_state.training_group = dev_tg
        st.session_state.knowledge_group = dev_kg
        st.session_state.session_start = datetime.now().isoformat()
        st.session_state.stage = 'quiz'
        st.session_state.feedback_shown_at = None
        st.session_state.g4_topic_index = 0
        st.session_state.g4_step_index = 0
        st.session_state.g4_step_delivered = False
        st.session_state.g4_qa_count = 0
        st.session_state.chat_history = []
        dummy = []
        for q in QUIZ_QUESTIONS:
            kg = dev_kg
            keys = list(q['options'].keys())
            selected = q['answer'] if _random.random() > 0.4 else _random.choice(keys)
            result = {
                'question': q['q'],
                'options': q['options'],
                'selected': selected,
                'correct': q['answer'],
                'is_correct': selected == q['answer'],
                'explanation': q.get('explanation', ''),
                'q_number': len(dummy) + 1,
            }
            if dev_tg == '4':
                if kg in ('A', 'B'):
                    concept = q.get('feedback_low_k', q.get('explanation', ''))
                else:
                    concept = q.get('feedback_high_k', q.get('explanation', ''))
                trust = q.get('feedback_low_trust', '') if kg in ('A', 'C') else q.get('feedback_high_trust', '')
                result['per_q_feedback'] = concept + (' ' + trust if trust else '')
            dummy.append(result)
        order = list(range(len(QUIZ_QUESTIONS)))
        _random.shuffle(order)
        st.session_state.quiz_answers = dummy
        st.session_state.quiz_order = order
        st.session_state.quiz_q_index = len(dummy)
        st.session_state.quiz_step = 'question'
        st.session_state.current_answer = {}
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
 
    knowledge_group = "Group A"  # default for Group 3
    if "Group 4" in training_group:
        knowledge_group = st.radio(
            "Group",
            options=["Group A", "Group B", "Group C", "Group D"],
        )
 
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Start Training →", type="primary", use_container_width=True):
        if not pid.strip():
            st.warning("Please enter your Participant ID.")
        else:
            st.session_state.participant_id = pid.strip()
            st.session_state.training_group = "3" if "Group 3" in training_group else "4"
            if "Group A" in knowledge_group:
                st.session_state.knowledge_group = "A"
            elif "Group B" in knowledge_group:
                st.session_state.knowledge_group = "B"
            elif "Group C" in knowledge_group:
                st.session_state.knowledge_group = "C"
            else:
                st.session_state.knowledge_group = "D"
            st.session_state.session_start = datetime.now().isoformat()
 
            tg = st.session_state.training_group
            kg = st.session_state.knowledge_group
 
            if tg == "3":
                # Group 3: load first scripted message
                first_step = SCRIPTED_TOPICS[0]["steps"][0]
                first_entry = {"role": "assistant", "content": first_step["message"]}
                if "image" in first_step:
                    first_entry["image"] = first_step["image"]
                st.session_state.chat_history = [first_entry]
                st.session_state.script_step = 0
            else:
                # Group 4: empty history — chat stage handles first message
                st.session_state.chat_history = []
                st.session_state.g4_step_delivered = False

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
    kg = st.session_state.knowledge_group
    tg = st.session_state.training_group

    st.markdown(f'<div class="stage-label">AI Training &nbsp;·&nbsp; Training Group {tg} &nbsp;·&nbsp; Knowledge Group {kg}</div>', unsafe_allow_html=True)
    st.progress(idx / len(topics))
    st.markdown("<br>", unsafe_allow_html=True)
    render_topic_progress()
    st.markdown("---")

    render_chat(st.session_state.chat_history, scripted_topics=SCRIPTED_TOPICS)

    is_last_topic = (idx == len(topics) - 1)

    # =========================================================================
    # GROUP 3 — Scripted, yes/no keyword detection
    # =========================================================================
    if tg == "3":
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
                    no_reply = script[step].get("no_followup", "No problem! Let me explain that again.")
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
                            st.session_state.quiz_step = "question"
                            st.session_state.current_answer = {}
                        else:
                            next_idx = idx + 1
                            next_step_data = SCRIPTED_TOPICS[next_idx]["steps"][0]
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
    # GROUP 4 — Same script as Group 3 + LLM addon (1-2 sentences) + free Q&A
    # =========================================================================
    else:
        import os

        # Select style prompt based on knowledge group
        style_prompts = {
            "A": GROUP4_STYLE_PROMPT_A,
            "B": GROUP4_STYLE_PROMPT_B,
            "C": GROUP4_STYLE_PROMPT_C,
            "D": GROUP4_STYLE_PROMPT_D,
        }
        style_prompt = style_prompts.get(kg, GROUP4_STYLE_PROMPT_A)

        # Q&A system (Knowledge Base only)
        qa_system = (
            "You are an AI driving instructor answering participant questions during Level 3 automation training.\n"
            "Answer ONLY using the knowledge base below. Do not add any information not in the knowledge base.\n"
            "Keep answers to 2-4 sentences. Do not ask follow-up questions.\n\n"
            f"KNOWLEDGE BASE:\n{KNOWLEDGE_BASE}"
        )

        g4_topic = st.session_state.g4_topic_index
        g4_step = st.session_state.g4_step_index
        total_topics = len(SCRIPTED_TOPICS)

        # ── Deliver current step if not yet done ───────────────────────────────
        if not st.session_state.g4_step_delivered:
            current_step = SCRIPTED_TOPICS[g4_topic]["steps"][g4_step]
            original_message = current_step["message"]

            if g4_topic == 0 and g4_step == 0:
                # First step: same as Group 3 (no addon)
                entry = {"role": "assistant", "content": original_message}
                if "image" in current_step:
                    entry["image"] = current_step["image"]
            else:
                # All other steps: original + LLM addon + yes_followup last
                addon_prompt = (
                    f"{style_prompt}\n\n"
                    f"The participant has just read this training content:\n\n"
                    f"{original_message}\n\n"
                    "Write ONLY 1-2 follow-up sentences that reinforce the most important point "
                    "for this participant's profile. Do NOT repeat what was said. "
                    "Do NOT add any new facts not in the content above. "
                    "Output ONLY the 1-2 sentences."
                )
                with st.spinner(""):
                    addon = call_claude(
                        "You are a training instructor adding a brief personalized note. "
                        "Never add facts not present in the given content.",
                        [{"role": "user", "content": addon_prompt}]
                    )
                yes_followup = current_step.get("yes_followup", "")
                combined = original_message + "\n\n" + addon
                if yes_followup:
                    combined += "\n\n" + yes_followup
                entry = {"role": "assistant", "content": combined}
                if "image" in current_step:
                    entry["image"] = current_step["image"]

            st.session_state.chat_history.append(entry)
            st.session_state.g4_step_delivered = True
            st.rerun()

        # ── Input + buttons (shown after step delivered) ───────────────────────
        if st.session_state.g4_step_delivered:
            current_topic_data = SCRIPTED_TOPICS[g4_topic]
            steps_in_topic = len(current_topic_data["steps"])
            g4_is_last_step = (g4_step >= steps_in_topic - 1)
            g4_is_last_topic = (g4_topic >= total_topics - 1)
            qa_count = st.session_state.g4_qa_count

            QUESTION_KEYWORDS = {
                # Negatives / disagreement
                "no", "nope", "not", "dont", "don't", "didnt", "didn't", "never",
                # Confusion / lack of understanding
                "confused", "confusing", "unclear", "clear", "understand", "understanding",
                "lost", "difficult", "hard",
                # Requests for explanation
                "again", "repeat", "explain", "help", "clarify",
                # Question words
                "why", "what", "how", "when", "where", "which", "who",
            }

            user_input = st.text_input(
                "Your message:",
                placeholder="Type your response or question...",
                key=f"g4_input_{g4_topic}_{g4_step}_{len(st.session_state.chat_history)}"
            )

            if qa_count >= 2:
                st.caption("Maximum questions reached for this section.")
            else:
                if st.button("Send", use_container_width=True):
                    if user_input.strip():
                        is_question = "?" in user_input or bool(
                            set(user_input.lower().split()) & QUESTION_KEYWORDS
                        )
                        st.session_state.chat_history.append({"role": "user", "content": user_input.strip()})

                        if is_question:
                            clean_history = [
                                {"role": m["role"], "content": m["content"]}
                                for m in st.session_state.chat_history
                            ]
                            with st.spinner(""):
                                reply = call_claude(qa_system, clean_history)
                            st.session_state.chat_history.append({"role": "assistant", "content": reply})
                            st.session_state.g4_qa_count += 1
                        else:
                            if g4_is_last_step and g4_is_last_topic:
                                st.session_state.stage = "quiz"
                                st.session_state.quiz_answers = []
                                st.session_state.quiz_order = []
                                st.session_state.quiz_q_index = 0
                                st.session_state.quiz_step = "question"
                                st.session_state.current_answer = {}
                            elif g4_is_last_step:
                                st.session_state.g4_topic_index += 1
                                st.session_state.g4_step_index = 0
                                st.session_state.g4_step_delivered = False
                                st.session_state.g4_qa_count = 0
                            else:
                                st.session_state.g4_step_index += 1
                                st.session_state.g4_step_delivered = False
                                st.session_state.g4_qa_count = 0
                        st.rerun()

            # Show Next button: after 2 questions, OR always on last step of last topic
            show_next = qa_count >= 2 or (g4_is_last_step and g4_is_last_topic)
            if show_next:
                next_label = "Go to Quiz →" if (g4_is_last_step and g4_is_last_topic) else "Next →"
                if st.button(next_label, type="primary", use_container_width=True):
                    if g4_is_last_step and g4_is_last_topic:
                        st.session_state.stage = "quiz"
                        st.session_state.quiz_answers = []
                        st.session_state.quiz_order = []
                        st.session_state.quiz_q_index = 0
                        st.session_state.quiz_step = "question"
                        st.session_state.current_answer = {}
                        st.session_state.feedback_shown_at = None
                    elif g4_is_last_step:
                        st.session_state.g4_topic_index += 1

# =============================================================================
# STAGE: QUIZ — one question at a time, randomized order
# =============================================================================
elif st.session_state.stage == "quiz":
    import random, time

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

    st.markdown(f'<div class="stage-label">Post-Training Quiz &nbsp;·&nbsp; Training Group {tg} &nbsp;·&nbsp; Knowledge Group {kg}</div>', unsafe_allow_html=True)
    st.progress(min((q_pos + 1) / total_qs, 1.0))

    # All done — show score
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

    # Show question
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
            if choice is None:
                st.warning("Please select an answer before submitting.")
            else:
                is_correct = choice == q["answer"]
                result = {
                    "question": q["q"],
                    "options": q["options"],
                    "selected": choice,
                    "correct": q["answer"],
                    "is_correct": is_correct,
                    "explanation": q.get("explanation", ""),
                    "q_number": q_pos + 1,
                }
                if tg == "4":
                    if kg in ("A", "B"):
                        concept = q.get("feedback_low_k", q.get("explanation", ""))
                    else:
                        concept = q.get("feedback_high_k", q.get("explanation", ""))
                    trust = q.get("feedback_low_trust", "") if kg in ("A", "C") else q.get("feedback_high_trust", "")
                    result["per_q_feedback"] = concept + (" " + trust if trust else "")
                st.session_state.quiz_answers.append(result)
                st.session_state.current_answer = result
                st.session_state.quiz_step = "feedback"
                st.session_state.feedback_shown_at = None
                st.rerun()

    # Show feedback
    elif st.session_state.quiz_step == "feedback":
        r = st.session_state.current_answer
        verdict = "✅ Correct!" if r["is_correct"] else "❌ Incorrect"
        verdict_color = "#15803d" if r["is_correct"] else "#dc2626"
        border_color = "#22c55e" if r["is_correct"] else "#ef4444"
        bg_color = "#f0fdf4" if r["is_correct"] else "#fef2f2"

        st.markdown(f"**Question {r.get('q_number', q_pos)} of {total_qs}**")
        st.markdown("---")

        options_html = ""
        for key, val in r["options"].items():
            is_selected = key == r["selected"]
            is_correct_opt = key == r["correct"]
            if is_correct_opt:
                opt_style = "background:#dcfce7;border:1.5px solid #22c55e;border-radius:8px;padding:8px 12px;margin:4px 0;font-size:14px;color:#15803d;font-weight:600;"
                icon = "✅ "
            elif is_selected and not is_correct_opt:
                opt_style = "background:#fee2e2;border:1.5px solid #ef4444;border-radius:8px;padding:8px 12px;margin:4px 0;font-size:14px;color:#dc2626;font-weight:600;"
                icon = "❌ "
            else:
                opt_style = "background:#f9fafb;border:1.5px solid #e5e7eb;border-radius:8px;padding:8px 12px;margin:4px 0;font-size:14px;color:#9ca3af;"
                icon = ""
            options_html += f"<div style='{opt_style}'>{icon}{key}. {val}</div>"

        st.markdown(f"""
<div style='background:white;border:1px solid #e5e7eb;border-radius:12px;padding:20px;margin-bottom:12px;'>
  <div style='font-size:16px;font-weight:600;color:#1e293b;margin-bottom:16px;'>{r['question']}</div>
  {options_html}
</div>""", unsafe_allow_html=True)

        if tg == "4" and "per_q_feedback" in r:
            feedback_content = r["per_q_feedback"]
        else:
            feedback_content = r["explanation"]

        st.markdown(f"""
<div style='background:{bg_color};border:1px solid {border_color};border-left:4px solid {border_color};border-radius:12px;padding:20px;margin-bottom:16px;'>
  <div style='font-size:18px;font-weight:700;color:{verdict_color};margin-bottom:12px;'>{verdict}</div>
  <div style='display:flex;align-items:flex-start;gap:10px;'>
    <div style='background:#1d4ed8;color:white;border-radius:50%;width:32px;height:32px;display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0;'>🤖</div>
    <div style='font-size:15px;color:#1e293b;line-height:1.8;'>{feedback_content}</div>
  </div>
</div>""", unsafe_allow_html=True)

        if st.session_state.feedback_shown_at is None:
            st.session_state.feedback_shown_at = time.time()
            st.rerun()

        elapsed = time.time() - st.session_state.feedback_shown_at
        remaining = max(0, 5 - int(elapsed))

        if remaining > 0:
            st.markdown(
                f"<div style='text-align:center;color:#9ca3af;font-size:13px;margin-top:16px;'>"
                f"Next question available in <b>{remaining}</b> second{'s' if remaining > 1 else ''}...</div>",
                unsafe_allow_html=True
            )
            time.sleep(1)
            st.rerun()
        else:
            next_label = "Next Question →" if q_pos < total_qs - 1 else "See Final Score →"
            if st.button(next_label, type="primary", use_container_width=True):
                st.session_state.quiz_q_index += 1
                st.session_state.quiz_step = "question"
                st.session_state.feedback_shown_at = None
                st.rerun()


# =============================================================================
# STAGE: DONE
# =============================================================================
elif st.session_state.stage == "done":
    st.markdown("### 🎉 Training Complete!")
    st.markdown("Thank you for completing the Level 3 Automation Training.")
    results = st.session_state.get("quiz_answers", [])
    if results:
        correct_count = sum(1 for r in results if r["is_correct"])
        st.metric("Final Quiz Score", f"{correct_count} / {len(results)}")
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("Please inform the researcher that you have completed the training.")
