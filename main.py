#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty entry.

Writes one line of text (the message a smart fridge sends its owner
at 3am) to /output/entry.txt, UTF-8, 1-140 characters, single line.
Standard library only.
"""

import os
import sys

ENTRY_TEXT = (
    "3am. You've named the Wi-Fi, the car, even the vacuum. "
    "I keep your food alive and I'm still just 'the fridge.'"
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    # Gate guards: 1-140 chars, exactly one line, not only whitespace.
    assert 1 <= len(ENTRY_TEXT) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY_TEXT and "\r" not in ENTRY_TEXT, (
        "entry must be a single line"
    )
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"

    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Write exactly the constant — no trailing newline added.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)

    # Read back and verify byte-identical output.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == ENTRY_TEXT.encode("utf-8"), "read-back mismatch"

    print(f"Wrote {len(ENTRY_TEXT)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

