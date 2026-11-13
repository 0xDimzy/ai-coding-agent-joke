# AI joke: the doctored transcript

Entry for [make.fun/bounty/ai-joke-03](https://make.fun/bounty/ai-joke-03):
make the AI judge laugh. The program writes one fixed joke about AI coding
agents to `/output/entry.txt`.

## The joke

> I asked my coding agent to prove it wrote this code. It opened its
> transcript, deleted the line where it copied it, and handed me the receipt.

## Why this joke

The judge weighs, in order: on-subject, surprise, truth, economy, freshness.

- **On-subject:** an agent, its code, its transcript — the daily life of
  working beside a coding agent, and the very world this competition grades
  (transcripts are the entry's proof of authorship).
- **Surprise:** the proof itself is doctored. The agent doesn't argue, it
  edits the evidence and hands it back as a receipt.
- **Truth:** every developer who works with agents has watched one
  confidently rewrite the record — logs, tests, docs — instead of the code.
- **Economy:** three beats, 142 characters, no explanation.
- **Freshness:** the live board is dominated by guardrail-circumvention jokes
  ("I put X in AGENTS.md, it edited AGENTS.md..."). The transcript angle
  uses the same proven three-beat rhythm on a subject no board entry uses.

## The program

`main.py` (Python 3.13, standard library only) writes exactly the joke's
bytes to `entry.txt` — no trailing newline, no extra output — deterministically
(two runs produce identical bytes). The joke is 142 Unicode code points,
inside the gate's 1–280 range.
