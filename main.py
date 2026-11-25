#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun entry.

Writes one line — the museum label a museum in the year 3000 puts beside
an ordinary object from today (a group chat) — to /output/entry.txt.
Pure Python standard library, no network, no input files: the line is
the entry.
"""

import os

LINE = (
    "Group chat, c. 2025. A nightly ritual in which 43 humans gathered "
    "to exchange frog pictures and never once agree on dinner."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read it back: the gate counts characters, so prove what landed on
    # disk is exactly the line we meant to enter, single line included.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt on disk differs from the entry"
    print(written, end="")


if __name__ == "__main__":
    main()
