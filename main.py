#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a traveler
from 1800 to /output/entry.txt.

The sentence: The internet is a post office that never sleeps, where a
letter crosses the world in a blink and returns with whole libraries
before the ink is dry.

Why this sentence: one familiar 1800 institution (the post office)
carries the whole explanation, it is two-way (a letter goes out and
knowledge comes back), every word is one a person from 1800 knows, and
"before the ink is dry" is the image that sticks.
"""
import os

SENTENCE = (
    "The internet is a post office that never sleeps, where a letter "
    "crosses the world in a blink and returns with whole libraries "
    "before the ink is dry."
)


def main() -> None:
    # Enforce the gate ourselves: 1-200 chars, not only whitespace.
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("entry sentence fails the gate: %r" % SENTENCE)
    # The bounty wants exactly ONE sentence: a single terminal period
    # and no other sentence-ending mark anywhere in the text.
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("entry is not exactly one sentence: %r" % SENTENCE)
    if any(mark in text for mark in ("!", "?", "\n")):
        raise ValueError("entry carries extra sentence marks: %r" % SENTENCE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
