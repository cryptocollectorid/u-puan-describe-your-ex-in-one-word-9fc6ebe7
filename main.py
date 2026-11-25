#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes one word describing an ex (max 111 characters) to
/output/entry.txt. Stdlib only, no network, no dependencies.

Run: python3 main.py
"""

import os

ENTRY = "Extinct"


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse:
    # 1-111 UTF-8 characters, not whitespace-only, exactly one word.
    if not ENTRY.strip():
        raise SystemExit("entry is empty or whitespace-only")
    if ENTRY.strip() != ENTRY or any(c.isspace() for c in ENTRY):
        raise SystemExit("entry must be exactly one word, no whitespace")
    if not 1 <= len(ENTRY) <= 111:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-111")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
