#!/usr/bin/env python3
"""Entry program for "One-Line Roast: The Gadget You Use Every Day".

Writes a single roast line about a smartwatch that grades its owner's
sleep every night and then wakes him up to deliver the bad news.
"""

import os
import sys
from pathlib import Path

ROAST = (
    "My smartwatch scores my sleep out of 100 every night, then buzzes me "
    "awake at dawn to report I got a 41 and must try harder at being unconscious."
)

MIN_CHARS = 1
MAX_CHARS = 200


def output_file() -> Path:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(directory) / "entry.txt"


def main() -> int:
    target = output_file()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ROAST, encoding="utf-8")

    # Read the file back and hold it against the gate: UTF-8 text of
    # 1-200 characters that is not only whitespace.
    written = target.read_text(encoding="utf-8")
    if written != ROAST:
        print("error: written text does not match the roast line", file=sys.stderr)
        return 1
    if not MIN_CHARS <= len(written) <= MAX_CHARS or not written.strip():
        print(
            f"error: entry is {len(written)} characters, outside the gate",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
