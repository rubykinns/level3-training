# =============================================================================
# chatbot.py — Claude API chatbot for interactive Q&A during training
# =============================================================================

import json
import urllib.request
import urllib.error
from config import ANTHROPIC_API_KEY, MODEL


def _call_claude(system_prompt: str, conversation_history: list) -> str:
    """
    Calls the Anthropic API and returns the assistant's reply as a string.
    conversation_history: list of {"role": "user"|"assistant", "content": str}
    """
    payload = {
        "model": MODEL,
        "max_tokens": 1000,
        "system": system_prompt,
        "messages": conversation_history
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=data,
        headers={
            "Content-Type": "application/json",
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            # Extract text from content blocks
            texts = [block["text"] for block in result.get("content", []) if block.get("type") == "text"]
            return " ".join(texts).strip()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        return f"[API Error {e.code}]: {body}"
    except Exception as e:
        return f"[Connection Error]: {str(e)}"


def run_chatbot_session(system_prompt: str, intro_message: str):
    """
    Runs an interactive chatbot Q&A session in the terminal.
    Type 'done', 'exit', or 'quit' to end the session.
    """
    print("\n" + "─" * 60)
    print("  💬  CHATBOT Q&A SESSION")
    print("─" * 60)
    print(f"\n  Assistant: {intro_message}")
    print("\n  (Type your question and press Enter. Type 'done' to finish.)\n")

    conversation_history = []

    while True:
        user_input = input("  You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in {"done", "exit", "quit"}:
            print("\n  Assistant: Great questions! Let's move on to the next part of your training.\n")
            break

        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})

        # Get response
        print("\n  Assistant: ", end="", flush=True)
        reply = _call_claude(system_prompt, conversation_history)
        print(reply + "\n")

        # Add assistant reply to history
        conversation_history.append({"role": "assistant", "content": reply})

    return conversation_history
