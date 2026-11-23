# grandma-word

[![make.fun · u-0xkianno-one-word-from-grandma-f04bed16](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/nmlyz/grandma-word/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/nmlyz/grandma-word/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)

grandma-word writes the one word a grandma would text about AI to a file: **"contraption"** — the word grandmothers reach for when a new machine appears in the house, warm and a little baffled, aimed at the thing itself rather than at any explanation of it. One word, nothing else: no sentence, no caption, no punctuation tricks.

## Why this word

- **It sounds like her.** "Contraption" is what a grandma calls a gadget she did not ask for and does not quite trust yet — affectionate, not technical.
- **It fits the machine, not the idea.** It points at the thing on the table, not at a concept, a company, or a lecture about the future.
- **It is a real word.** A misspelling can read as a mistake; this reads as her voice, spelled the way she would expect to see it.
- **It is not the obvious pick.** It sidesteps the first words anyone reaches for and lands on the one she actually would.

## Run it

```sh
python3 main.py
```

It writes the word to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set). No network access needed; the same text, byte for byte, on every run.

## How it works

`main.py` is a single self-contained program using only the Python standard library:

- The word is held in one constant, `WORD`, so there is exactly one place to look.
- Before writing anything, the word is checked against the brief's rules — length, single line, no stray whitespace, exactly one word — and every violation is reported instead of silently writing a bad entry.
- The entry is written with no trailing newline, then read back and compared byte for byte with the expected text; the run fails if the file on disk does not match.
- The output directory comes from `MAKEFUN_OUTPUT_DIR` when set, and defaults to `/output` otherwise.

## Output

`/output/entry.txt` contains exactly 11 bytes:

```
contraption
```

No trailing newline, no extra whitespace. Running the program twice produces byte-identical files.

---

<sub>See the word on [make.fun](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16) · Entered via [my referral link](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)</sub>
