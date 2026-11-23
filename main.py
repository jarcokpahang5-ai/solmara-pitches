"""One-line pitch entry for make.fun's "A Day of One-Line Pitches" bounty.

The whole entry is a single sentence, at most 240 characters, meant to
convince a friend who has never coded to let an AI agent build their
first app idea on make.fun. Running this module prints the sentence and
writes it (plus a trailing newline) to /output/entry.txt.
"""

import os

PITCH = (
    "Just describe the app you've always wanted, and an AI agent will "
    "build it for you on make.fun — no coding, no waiting, just your "
    "idea turned into something real you can use today."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(sentence: str) -> str:
    """Return the sentence if it is a single sentence of 1..240 chars."""
    text = sentence.strip()
    if not 1 <= len(text) <= 240:
        raise ValueError(
            f"sentence must be 1..240 characters, got {len(text)}"
        )
    if text[-1] not in ".!?":
        raise ValueError("sentence must end with terminal punctuation")
    # A sentence boundary is a terminator followed by whitespace or the
    # end of the string; a period inside "make.fun" is not one.
    boundaries = sum(
        1
        for i, ch in enumerate(text)
        if ch in ".!?" and (i == len(text) - 1 or text[i + 1].isspace())
    )
    if boundaries != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> None:
    sentence = validate(PITCH)
    print(sentence)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(sentence + "\n")


if __name__ == "__main__":
    main()
