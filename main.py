#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes one word describing an ex (max 111 characters) to
/output/entry.txt. Stdlib only, no network, no dependencies.

Run: python3 main.py
"""

import os
import sys

ENTRY = "Extinct"
MAX_CHARS = 111


def validate_entry(word: str) -> str:
    """Check the entry against the competition gate.

    Returns the word unchanged when it passes; raises SystemExit
    with a clear reason instead of shipping an entry the gate
    would refuse: 1-111 UTF-8 characters, not whitespace-only,
    exactly one word.
    """
    if not word.strip():
        raise SystemExit("entry is empty or whitespace-only")
    if word.strip() != word or any(c.isspace() for c in word):
        raise SystemExit("entry must be exactly one word, no whitespace")
    if any(ord(c) < 32 or ord(c) == 127 for c in word):
        raise SystemExit("entry must not contain control characters")
    if not 1 <= len(word) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(word)} characters, must be 1-{MAX_CHARS}")
    return word


def write_entry(word: str, out_dir: str) -> str:
    """Write the validated entry to entry.txt; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    return path


def main() -> None:
    word = validate_entry(ENTRY)
    if "--check" in sys.argv:
        # Dry run: validate only, write nothing.
        print(f"OK: {len(word)} characters, one word")
        return
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(word, out_dir)
    print(f"Wrote {len(word)} characters to {path}")


if __name__ == "__main__":
    main()
