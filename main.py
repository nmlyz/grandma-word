#!/usr/bin/env python3
"""grandma-word: the one word a grandma would text about AI.

The entry is a single word, "contraption". It is the word grandmothers
reach for when a new machine appears in the house: warm, a little baffled,
and aimed squarely at the thing itself rather than at any explanation of
it. It needs no caption, fits no other subject as well as it fits a
machine, and it is not the obvious pick. A real word beats a typo here:
a misspelling can read as a mistake, while this word reads as her voice.

The program writes the word, and nothing else, to ``entry.txt`` inside
the output directory. By default that directory is ``/output``; setting
``MAKEFUN_OUTPUT_DIR`` overrides it. The output is exactly eleven bytes,
``contraption`` with no trailing newline, and running the program twice
produces byte-identical files.

Standard library only. No network, no arguments, no configuration files.
"""

import os
import sys

# The entry: the one word a grandma would text about AI.
WORD = "contraption"

# The brief allows a single word of one to thirty characters.
MIN_WORD_LENGTH = 1
MAX_WORD_LENGTH = 30

# Where the entry goes unless MAKEFUN_OUTPUT_DIR says otherwise.
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"

# File mode for the written entry.
ENTRY_MODE = 0o644


class EntryError(ValueError):
    """Raised when the entry text fails a rule of the brief."""


def word_is_single_word(text: str) -> bool:
    """True when *text* is exactly one whitespace-free word."""
    return len(text.split()) == 1 and text == text.strip()


def check_length(text: str) -> str | None:
    """Return an error message if *text* breaks the length rule, else None."""
    if len(text) < MIN_WORD_LENGTH:
        return f"entry is empty, must be at least {MIN_WORD_LENGTH} character"
    if len(text) > MAX_WORD_LENGTH:
        return (
            f"entry is {len(text)} characters, "
            f"must be at most {MAX_WORD_LENGTH}"
        )
    return None


def check_single_line(text: str) -> str | None:
    """Return an error message if *text* is not a single line, else None."""
    if "\n" in text or "\r" in text:
        return "entry must be a single line, no line breaks"
    return None


def check_whitespace(text: str) -> str | None:
    """Return an error message if *text* has stray whitespace, else None."""
    if not text.strip():
        return "entry must not be only white space"
    if text != text.strip():
        return "entry must not start or end with white space"
    return None


def check_word_count(text: str) -> str | None:
    """Return an error message if *text* is not exactly one word, else None."""
    words = text.split()
    if len(words) != 1:
        return f"entry has {len(words)} words, must be exactly 1"
    return None


# Every check, in the order it is reported. Keeping the checks in one
# table means adding a rule is a one-line change, and the report order
# never depends on the order the functions happen to be defined in.
CHECKS = (
    check_length,
    check_single_line,
    check_whitespace,
    check_word_count,
)


def validate(text: str) -> list:
    """Collect every brief violation for *text* (empty list means valid)."""
    problems = []
    for check in CHECKS:
        problem = check(text)
        if problem is not None:
            problems.append(problem)
    return problems


def resolve_output_dir() -> str:
    """Return the directory the entry is written into.

    ``MAKEFUN_OUTPUT_DIR`` wins when it is set to a non-empty value;
    an empty value falls back to the default, so an accidental empty
    export can never point the entry at the current directory.
    """
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return override
    return DEFAULT_OUTPUT_DIR


def entry_path(output_dir: str) -> str:
    """Return the full path of the entry file inside *output_dir*."""
    return os.path.join(output_dir, ENTRY_FILENAME)


def write_entry(text: str, path: str) -> None:
    """Write *text* to *path* exactly as given, no added newline."""
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # Best effort only: in the grading sandbox /output is a root-owned
    # directory, so a failed chmod must never fail the run.
    try:
        os.chmod(path, ENTRY_MODE)
    except OSError:
        pass


def read_back(path: str) -> bytes:
    """Read the entry file back as raw bytes for verification."""
    with open(path, "rb") as handle:
        return handle.read()


def verify(path: str, expected: bytes) -> bool:
    """True when the file at *path* holds exactly *expected* bytes."""
    return read_back(path) == expected


def run() -> int:
    """Validate the word, write it, and verify what was written."""
    text = WORD
    problems = validate(text)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1

    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    path = entry_path(output_dir)
    write_entry(text, path)

    expected = text.encode("utf-8")
    if not verify(path, expected):
        print("wrote back bytes do not match entry", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} characters to {path}")
    return 0


def main() -> int:
    """Entry point: exit 0 on success, 1 when the entry is invalid."""
    try:
        return run()
    except EntryError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
