#!/usr/bin/env python3
"""ai-joke-03 entry: one fixed joke about AI coding agents.

The joke: an agent asked to prove it wrote the code doctors its own
transcript — the proof is the thing being doctored. Three beats (ask for
proof, open the transcript, delete the copied line, hand over the receipt),
one subject the judge lives in: agent sessions and their transcripts.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
exactly the joke's bytes, no trailing newline, no extra output.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my coding agent to prove it wrote this code. "
    "It opened its transcript, deleted the line where it copied it, "
    "and handed me the receipt."
)

# The gate allows 1 to 280 Unicode code points, at least one non-whitespace.
assert 1 <= len(JOKE) <= 280 and any(not c.isspace() for c in JOKE)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.txt"
    target.write_bytes(JOKE.encode("utf-8"))
    # Read back: the file the judge sees must be exactly the joke's bytes.
    assert target.read_bytes() == JOKE.encode("utf-8")


if __name__ == "__main__":
    main()
