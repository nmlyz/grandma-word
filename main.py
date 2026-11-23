#!/usr/bin/env python3
"""grandma-word: write the one word a grandma would text about AI to /output/entry.txt.

The word is "contraption". It is the word grandmothers reach for when a new
machine appears in the house: warm, a little baffled, and aimed squarely at
the thing itself rather than at any explanation of it. It needs no caption,
fits no other subject as well as it fits a machine, and it is not the
obvious pick. A real word beats a typo here: a misspelling can read as a
mistake, while this word reads as her voice.

Standard library only, no network. Deterministic: the same bytes on every run.
"""

import os
import sys

WORD = "contraption"

MIN_LEN = 1
MAX_LEN = 30


def problems(text: str) -> list:
    """Return every gate violation for the entry text (empty means valid)."""
    found = []
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        found.append(f"entry is {len(text)} characters, must be {MIN_LEN}-{MAX_LEN}")
    stripped = text.strip()
    if not stripped:
        found.append("entry must not be only white space")
    if text != stripped:
        found.append("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        found.append("entry must be a single line")
    if len(text.split()) != 1:
        found.append(f"entry has {len(text.split())} words, must be exactly 1")
    return found


def main() -> int:
    text = WORD
    bad = problems(text)
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # directory, so a failed chmod must never fail the run.
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    written = open(path, "rb").read()
    if written != text.encode("utf-8"):
        print("wrote back bytes do not match entry", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
