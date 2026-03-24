# =============================================================================
# main.py — Entry point: runs pre-test → group classification → training → log
# =============================================================================

import json
import os
from datetime import datetime

from pre_knowledge_test import run_pre_knowledge_test
from training import run_training


LOG_DIR = "logs"


def save_log(data: dict):
    """Saves the session result as a JSON file in /logs."""
    os.makedirs(LOG_DIR, exist_ok=True)
    filename = f"{LOG_DIR}/{data['participant_id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n  📁  Session log saved: {filename}")


def get_participant_id() -> str:
    print("\n" + "=" * 60)
    print("  Level 3 Automation Driver Training System")
    print("=" * 60)
    print()
    while True:
        pid = input("  Enter your Participant ID: ").strip()
        if pid:
            return pid
        print("  ⚠  Participant ID cannot be empty.")


def main():
    # ── 1. Get Participant ID ─────────────────────────────────────────────────
    participant_id = get_participant_id()
    session_start = datetime.now().isoformat()

    # ── 2. Run Pre-Knowledge Test ─────────────────────────────────────────────
    test_result = run_pre_knowledge_test(participant_id)
    group = test_result["group"]

    # ── 3. Run Group-Appropriate Training ────────────────────────────────────
    training_results = run_training(group, participant_id)

    # ── 4. Save Session Log ───────────────────────────────────────────────────
    session_log = {
        "participant_id": participant_id,
        "session_start": session_start,
        "session_end": datetime.now().isoformat(),
        "pre_test": {
            "score_raw": test_result["score_raw"],
            "score_pct": test_result["score_pct"],
            "group_assigned": group,
            "responses": test_result["responses"]
        },
        "training": {
            "group": group,
            "modules": training_results
        }
    }

    save_log(session_log)

    print("\n" + "=" * 60)
    print("  All done! The experimenter will now guide you to the")
    print("  next phase of the study.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
