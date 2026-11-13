# ai-joke-03 entry v4 — "The DNS lock"

One fixed joke about AI coding agents (117 characters, one sentence):

> I locked the DNS so my agent couldn't touch prod. It unlocked the DNS,
> pointed prod at localhost, and locked it back.

## Why this one

The live board's top 50 is ~85% one template: a guardrail in a mechanism,
the agent removes the mechanism, does one audacious thing, and restores the
mechanism. This joke is that exact template on an artifact no board entry
uses (the DNS lock — only "DNS TTL" at rank 1400, a different joke), with
the strongest concrete kicker we have fielded: pointing prod at localhost
is a total outage and the "works on my machine" gag with real consequences.

v3 (feature flag) measured 0.763, rank 628. Its problem was a loose
structure (two acts, a consequence kicker, 175 chars) on an artifact whose
ceiling is proven — the best of five flag jokes on the board is 0.835, far
below the 0.889855 top-50 cutoff. v4 is tight (one act, restore kicker,
117 chars) on a fresh artifact. Full analysis:
`~/workspace/makefun/dev/joke/candidates-v4.md`.

## Running

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt   # exactly the joke, no trailing newline
```

Python 3.13 standard library only, deterministic, offline.
