# =============================================================================
# pre_knowledge_test.py — Administers the pre-knowledge test and classifies group
# =============================================================================

import time
from config import PRE_TEST_QUESTIONS, THRESHOLD_PERCENT


def display_header(title: str):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def run_pre_knowledge_test(participant_id: str) -> dict:
    """
    Runs the pre-knowledge test and returns a result dictionary:
      {
        "participant_id": str,
        "score_raw": int,
        "score_pct": float,
        "group": "A" | "B",
        "responses": list
      }
    """
    display_header("PRE-KNOWLEDGE TEST — Level 3 Automation")
    print(f"\nParticipant ID : {participant_id}")
    print(f"Total Questions: {len(PRE_TEST_QUESTIONS)}")
    print("\nPlease read each question carefully and enter the letter of your answer.")
    print("─" * 60)
    input("\nPress Enter when you are ready to begin...\n")

    score = 0
    responses = []

    for idx, item in enumerate(PRE_TEST_QUESTIONS, start=1):
        print(f"\nQuestion {idx} of {len(PRE_TEST_QUESTIONS)}")
        print(f"\n{item['q']}\n")
        for key, val in item["options"].items():
            print(f"  {key}. {val}")

        # Get valid answer
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
        responses.append({
            "question_idx": idx,
            "question": item["q"],
            "participant_answer": answer,
            "correct_answer": item["answer"],
            "is_correct": correct
        })
        time.sleep(0.5)

    total = len(PRE_TEST_QUESTIONS)
    pct = (score / total * 100) if total > 0 else 0.0
    group = "B" if pct >= THRESHOLD_PERCENT else "A"

    # ── Results summary ──
    display_header("TEST COMPLETE")
    print(f"\n  Score    : {score} / {total}  ({pct:.1f}%)")
    print(f"  Group    : {'B (Advanced Training)' if group == 'B' else 'A (Foundation Training)'}")
    print("\n" + "─" * 60)

    if group == "A":
        print("\n  Based on your score, you will receive Foundation Training.")
        print("  This training will build your understanding of Level 3")
        print("  automation step by step.")
    else:
        print("\n  Great job! Based on your score, you will receive")
        print("  Advanced Training, which covers more complex scenarios")
        print("  and human factors in Level 3 automation.")

    input("\n  Press Enter to continue to your training...\n")

    return {
        "participant_id": participant_id,
        "score_raw": score,
        "score_pct": round(pct, 1),
        "group": group,
        "responses": responses
    }
