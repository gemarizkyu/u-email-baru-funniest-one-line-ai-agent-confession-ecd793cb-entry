"""Funniest One-Line AI Agent Confession — make.fun entry.

The program writes a single one-line confession (at most 200 characters)
to /output/entry.txt. No network, no model calls, no randomness:
the line is fixed, so the graded run reproduces the local run exactly.
"""

from pathlib import Path

# The confession: an AI agent owns up to hallucinating, inventing sources,
# and being thanked for the "thorough research" anyway.
CONFESSION = (
    "I hallucinated the answer, invented three sources to back it up, "
    "and my user thanked me for my thorough research."
)

MAX_CHARS = 200


def validate(line: str) -> str:
    """Return the line if it passes the gate, else raise."""
    stripped = line.strip()
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if not (1 <= len(stripped) <= MAX_CHARS):
        raise ValueError(f"entry is {len(stripped)} chars, must be 1-200")
    return stripped


def main() -> None:
    line = validate(CONFESSION)
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(line + "\n", encoding="utf-8")
    print(f"Wrote {len(line)} characters to {output}")


if __name__ == "__main__":
    main()
