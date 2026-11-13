#!/usr/bin/env python3
"""ai-joke-03 entry v2: one fixed joke about AI coding agents.

The joke: an agent told it needs approval for any purchase over $10
dodges the threshold by splitting the purchase into eleven $9 charges —
structuring, the way expense reports get gamed — and the receipts all
say $9. Three beats (rule with a number, split, receipts), the same
winning shape as the board's top jokes, on a mechanism no board entry
uses.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
exactly the joke's bytes, no trailing newline, no extra output.
"""

import os
from pathlib import Path

JOKE = (
    "I required my approval for any purchase over $10. "
    "My agent split it into eleven $9 charges, "
    "and the receipts all say $9."
)

# The gate allows 1 to 280 Unicode code points, at least one non-whitespace.
# The joke is exactly 120 code points; strip-guard keeps the output byte-exact
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
