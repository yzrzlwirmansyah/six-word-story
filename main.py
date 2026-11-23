"""Six words, one story.

Writes a single six-word story (37 characters) to entry.txt.
Deterministic: fixed text, no randomness, no network, no time dependence.
"""

import os

TEXT = "The letter arrived after the funeral."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
