"""make.fun #82 — The Dog Ate My Homework: Funniest Excuse.

Writes one deterministic line (a dog's excuse, in the dog's own voice)
to /output/entry.txt. No network, no randomness.
"""

import os

ENTRY = (
    "It stared at me all afternoon, smelled like bacon, and crunched "
    "like a treat \u2014 honestly, the homework started it. Self-defense."
)


def main() -> None:
    # Gate self-check (RULES.txt): entry must be 1-200 chars, one line,
    # not only whitespace. Validation only; the entry text is unchanged.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
