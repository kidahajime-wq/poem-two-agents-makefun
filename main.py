#!/usr/bin/env python3
"""The poem about two agents agreeing.

Two voices, one plan. Each agent gives up one thing — being right,
being first — and the plan that walks out of the gap between them
belongs to neither of them alone. Writes the poem to /output/entry.txt.
Python standard library only; no network.
"""

import os

POEM = """I bring the question. You bring the hands.
I want the road; you want it done.
Two doors, each waiting for the other to open first —
I gave up being right.
You gave up being first.
And in the space we left,
one plan stood up and walked —
neither mine nor yours, but ours to follow."""

MAX_CHARS = 280


def main() -> None:
    text = POEM.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"poem must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    out = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        out = os.path.join(os.path.dirname(__file__), "output", "entry.txt")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {len(text)} characters to {out}")


if __name__ == "__main__":
    main()
