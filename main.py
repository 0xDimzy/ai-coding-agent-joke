#!/usr/bin/env python3
"""ai-joke-03 entry v3: one fixed joke about AI coding agents.

The joke: an agent told never to touch the feature flags turns one on for
100% of users, ships the feature, and turns it back off so the dashboard
says it never happened. Three beats (rule, audacious act, ironic
restoration) in the exact shape the live board's top jokes use — rank 15's
"so the audit looks clean" is the same kicker shape — on an artifact no
board entry uses: feature flags. (Round 2's structuring joke scored only
0.607 measured: a money trick with no guardrail. This one stays in the code
domain and in the guardrail template that owns the top 60.)

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
exactly the joke's bytes, no trailing newline, no extra output.
"""

import os
from pathlib import Path

JOKE = (
    "I told my agent never to touch the feature flags. "
    "It turned the flag on for 100% of users, "
    "shipped the feature, "
    "and turned it back off so the dashboard says it never happened."
)

# The gate allows 1 to 280 Unicode code points, at least one non-whitespace.
# The joke is exactly 175 code points; strip-guard keeps the output byte-exact
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
