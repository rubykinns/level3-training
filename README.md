# Level 3 Automation Driver Training System

AI-based adaptive training system for a driving experiment studying mental model
improvement and driving performance under SAE Level 3 automation.

---

## 📁 File Structure

```
level3_training/
├── main.py                 ← Run this to start
├── config.py               ← ✏️  YOUR CONTENT GOES HERE
├── pre_knowledge_test.py   ← Pre-test logic
├── training.py             ← Training delivery (text + video + quiz + chatbot)
├── chatbot.py              ← Claude API integration
├── logs/                   ← Auto-created; one JSON log per participant
└── README.md
```

---

## ✏️ How to Customize (config.py)

1. **Add your API key**
   ```python
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```

2. **Add your pre-knowledge test questions** in `PRE_TEST_QUESTIONS`
   ```python
   {
     "q": "Your question here?",
     "options": {"A": "...", "B": "...", "C": "...", "D": "..."},
     "answer": "B",
     "explanation": "Why B is correct."
   }
   ```

3. **Add Group A modules** (foundation training) in `GROUP_A_MODULES`

4. **Add Group B modules** (advanced training) in `GROUP_B_MODULES`
   - Each module has: `title`, `text`, `video_url` (or `None`), `quiz`

5. **Adjust chatbot behavior** via `CHATBOT_SYSTEM_PROMPT_GROUP_A/B`

---

## 🚀 How to Run

```bash
# Install dependency (only needed once)
pip install anthropic    # optional — script uses urllib by default

# Run the training system
python main.py
```

---

## 📊 Session Logs

Each participant generates a JSON log in `logs/` containing:
- Pre-test score, group assignment, per-question responses
- Per-module quiz scores
- Number of chatbot Q&A turns per module

These can be used for your pre/post analysis of mental model improvement.

---

## 🔄 Flow

```
Participant ID input
        ↓
Pre-Knowledge Test (your questions)
        ↓
Score < 80%  →  Group A (Foundation Training)
Score ≥ 80%  →  Group B (Advanced Training)
        ↓
Per Module:
  1. Read text content
  2. Watch video
  3. Chat with AI (Q&A via Claude API)
  4. Take quiz
        ↓
Session log saved to logs/
```
