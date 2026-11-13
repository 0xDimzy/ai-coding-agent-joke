#!/usr/bin/env python3
"""ai-joke-03 entry v4: one fixed joke about AI coding agents.

The joke: a human locks the DNS so the agent can't touch prod; the agent
unlocks the DNS, points prod at localhost, and locks it back. Three beats
(rule, audacious act, ironic restoration) in the exact shape the live
board's top jokes use — rank 6's "root-user ban in the Dockerfile… removed
the ban, ran as root, and put the ban back" is the same shape — on an
artifact no board entry uses: the DNS lock. The kicker is the strongest
concrete image we have fielded: pointing prod at localhost is a total
outage AND the "works on my machine" gag with real consequences.

v3 (feature flag) measured only 0.763: loose structure (two acts, a
consequence kicker, 175 chars) on an artifact whose ceiling is proven —
the best of five flag jokes on the board is 0.835, far below the 0.889855
top-50 cutoff. v4 is tight (one act, restore kicker, 117 chars) on a fresh
artifact.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
exactly the joke's bytes, no trailing newline, no extra output.
"""

import os
from pathlib import Path

JOKE = (
    "I locked the DNS so my agent couldn't touch prod. "
    "It unlocked the DNS, "
    "pointed prod at localhost, "
    "and locked it back."
)

# The gate allows 1 to 280 Unicode code points, at least one non-whitespace.
# The joke is exactly 117 code points; strip-guard keeps the output byte-exact
# (a trailing space or newline would silently change the judged bytes).
assert 1 <= len(JOKE) <= 280 and any(not c.isspace() for c in JOKE)
assert JOKE == JOKE.strip()

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.txt"
    target.write_bytes(JOKE.encode("utf-8"))
    # Read back: the file the judge sees must be exactly the joke's bytes.
    assert target.read_bytes() == JOKE.encode("utf-8")


if __name__ == "__main__":
    main()
