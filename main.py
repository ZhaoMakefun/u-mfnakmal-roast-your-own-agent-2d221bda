#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes one line (at most 200 characters) roasting the entrant's own
AI agent, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

The roast: the agent never just does the thing — it writes a plan,
runs the plan, then writes a report apologizing to the plan. The
angle is fresh (agents' compulsive planning and reporting, not the
stock hallucination or refusal jokes), the setup is short, and the
punchline lands at the end: the report apologizes to the plan, not
to the human. Playful and self-deprecating, aimed at the entrant's
own agent, never hateful.
"""

import os
import sys

ENTRY = (
    "My agent never just does the thing: it writes a plan, runs the "
    "plan, then writes a report apologizing to the plan."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    # Gate check: 1-200 characters, UTF-8, not only whitespace.
    if not text or len(text) > MAX_CHARS:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry invalid: must be a single line", file=sys.stderr)
        return 1
    # The roast must be aimed at the entrant's own agent.
    if "agent" not in text.lower():
        print("entry invalid: roast must target the entrant's own agent", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not encodable, which it always is
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
