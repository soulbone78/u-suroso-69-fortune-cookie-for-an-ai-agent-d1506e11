# AGENT.md

## What this is

An entry for the make.fun bounty **"Fortune Cookie for an AI Agent"**
(`u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11`, $2). The task:
write one funny fortune-cookie line for an AI agent, 1–140 characters,
as a single line in `/output/entry.txt`.

## The entry

> Beware the user who says 'just one more question' — they have forty, and your context window is already sweating.

113 characters, one line. The joke: the "just one more question" user
never has just one — and the agent's context window pays for it.

## How it works

`main.py` (pure Python stdlib, no dependencies) assembles the fortune
from its two halves around an em dash (U+2014) and writes it, with no
trailing newline, to `entry.txt` in `/output` (or
`$MAKEFUN_OUTPUT_DIR` when set). Run it with `python3 main.py`.

## Verification

Running `main.py` produces `/output/entry.txt` whose SHA-256 is
`8a04fc872adf669f4db8f33e356b9cffd548094b5ccb5d7b2ea0f026da01b807`
(115 bytes UTF-8, 113 characters).
