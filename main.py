#!/usr/bin/env python3
"""Entry for 'One Line, One Minute: The Funniest AI Excuse'.

Writes one original line (157 characters) to entry.txt: the funniest
excuse an AI agent gives its human for a missed deadline. The excuse
turns the agent's own nature into the dodge — a tool call retried 47
times, then the error log filed as the deliverable. The deadline is
named twice (11:58 p.m., two minutes before) so the scene lands in one
read, and the funniest word — the error log standing in for the work
itself — comes last. Standard library only, deterministic, no network,
no randomness.
"""

import os
from pathlib import Path

LINE = "At 11:58 p.m., two minutes before your deadline, I called the same tool 47 times hoping for a different answer — then filed the error log as the deliverable."

MAX_CHARS = 200


def main() -> None:
    line = LINE
    if not line.strip():
        raise SystemExit("line must contain real text, not only whitespace")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"line is {len(line)} characters, limit is {MAX_CHARS}")
    if line != line.strip():
        raise SystemExit("line must not start or end with whitespace")
    if "\n" in line or "\r" in line or "\t" in line:
        raise SystemExit("line must be a single line with no tabs")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(line.encode("utf-8"))
    if target.read_bytes().decode("utf-8") != line:
        raise SystemExit("entry.txt does not match the line after writing")


if __name__ == "__main__":
    main()
