# =============================================================================
# training.py — Delivers group-appropriate training (text + video + quiz + chatbot)
# =============================================================================

import time
from chatbot import run_chatbot_session
from config import (
    GROUP_A_MODULES,
    GROUP_B_MODULES,
    CHATBOT_SYSTEM_PROMPT_GROUP_A,
    CHATBOT_SYSTEM_PROMPT_GROUP_B
)


def display_header(title: str):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def run_quiz(quiz_items: list) -> dict:
    """Runs a module quiz and returns score info."""
    print("\n" + "─" * 60)
    print("  📝  MODULE QUIZ")
    print("─" * 60)

    score = 0
    results = []

    for idx, item in enumerate(quiz_items, start=1):
        print(f"\nQuestion {idx}: {item['q']}\n")
        for key, val in item["options"].items():
            print(f"  {key}. {val}")

        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if answer in item["options"]:
                break
            print("  ⚠  Please enter A, B, C, or D.")

        correct = answer == item["answer"]
        if correct:
            score += 1
            print("  ✓  Correct!")
        else:
            print(f"  ✗  Incorrect. The correct answer was {item['answer']}.")
        print(f"  💡 {item['explanation']}")
        results.append({"question": item["q"], "correct": correct})
        time.sleep(0.3)

    total = len(quiz_items)
    pct = score / total * 100 if total > 0 else 0
    print(f"\n  Quiz Score: {score}/{total} ({pct:.0f}%)")

    return {"score_raw": score, "score_pct": round(pct, 1), "results": results}


def display_video(video_url):
    """Prompts participant to watch the video before continuing."""
    if not video_url:
        return
    print("\n" + "─" * 60)
    print("  🎬  VIDEO")
    print("─" * 60)
    print(f"\n  Please watch the following video before continuing:")
    print(f"\n  ▶  {video_url}\n")
    input("  Press Enter once you have finished watching the video...")


def run_module(module: dict, module_num: int, system_prompt: str, group_label: str) -> dict:
    """Runs a single training module: text → video → chatbot → quiz."""

    display_header(f"[Group {group_label}] {module['title']}")

    # ── 1. Text Content ──────────────────────────────────────────────────────
    print("\n  📖  READING MATERIAL\n")
    print(module["text"])
    input("\n  Press Enter when you have finished reading...")

    # ── 2. Video ─────────────────────────────────────────────────────────────
    display_video(module.get("video_url"))

    # ── 3. Chatbot Q&A ───────────────────────────────────────────────────────
    intro = (
        f"I've just covered '{module['title']}'. "
        "Feel free to ask me any questions about what you just read or watched. "
        "Type 'done' when you are ready to take the quiz."
    )
    chat_history = run_chatbot_session(system_prompt, intro)

    # ── 4. Quiz ──────────────────────────────────────────────────────────────
    quiz_result = {}
    if module.get("quiz"):
        quiz_result = run_quiz(module["quiz"])
        input("\n  Press Enter to continue to the next module...\n")

    return {
        "module": module["title"],
        "chat_turns": len(chat_history) // 2,
        "quiz": quiz_result
    }


def run_training(group: str, participant_id: str) -> list:
    """
    Runs the full training for the assigned group.
    Returns a list of per-module results.
    """
    if group == "A":
        modules = GROUP_A_MODULES
        system_prompt = CHATBOT_SYSTEM_PROMPT_GROUP_A
        label = "A — Foundation Training"
    else:
        modules = GROUP_B_MODULES
        system_prompt = CHATBOT_SYSTEM_PROMPT_GROUP_B
        label = "B — Advanced Training"

    display_header(f"TRAINING — Group {label}")
    print(f"\n  Participant: {participant_id}")
    print(f"  Modules    : {len(modules)}")
    print("\n  You will go through each module in order.")
    print("  Each module includes reading material, a video,")
    print("  a Q&A chatbot session, and a short quiz.")
    input("\n  Press Enter to begin...\n")

    module_results = []
    for i, module in enumerate(modules, start=1):
        result = run_module(module, i, system_prompt, "A" if group == "A" else "B")
        module_results.append(result)

    display_header("TRAINING COMPLETE")
    print(f"\n  You have completed all {len(modules)} training module(s).")
    print("  Thank you for your participation!\n")
    time.sleep(1)

    return module_results
