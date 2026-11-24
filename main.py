#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line.

Writes one pickup line, spoken by a vending machine to a passing human,
to /output/entry.txt. Deterministic: no randomness, no network, no clock.
The line is a single sentence of at most 200 characters.
"""

import os

# The line, as the machine says it to a passing human:
# - Machine's voice: "I only take exact change" is something only a
#   vending machine says; the machine is the speaker, not a stranger.
# - Machine's world: exact change, the B7 button, dropping the snack.
# - The laugh: the change/chance pun, with the punch ("drop something
#   sweet for you") arriving in the last few words.
# - Short and speakable at 107 characters; warm and cheeky, not creepy.
LINE = "I only take exact change, but for you I'd take a chance \u2014 press B7 and let me drop something sweet for you."


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("Invalid line: entry must be non-empty.")
    if line != line.strip():
        raise SystemExit(
            "Invalid line: entry must not have leading or trailing whitespace."
        )
    if len(line) > 200:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, over the 200 limit."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(
            "Write verification failed: entry file content does not match the line."
        )


if __name__ == "__main__":
    main()
