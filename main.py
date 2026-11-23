#!/usr/bin/env python3
"""Emit the competition entry: one six-word story.

The whole program does a single job — take a fixed sentence and
save it as ``entry.txt`` in the output folder. The sentence never
changes between runs, and nothing here touches the network, the
clock, or any random source, so repeated runs produce the same
file every time.

Where the file goes: the ``MAKEFUN_OUTPUT_DIR`` environment
variable, when set; otherwise the ``/output`` directory. The
folder is created on demand if it does not exist yet.
"""

from os import environ, makedirs
from os.path import join

STORY = "The letter arrived after the funeral."


def output_folder() -> str:
    """Return the directory the entry should land in."""
    return environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def save_entry(folder: str) -> str:
    """Write the story to entry.txt inside folder; return its path."""
    makedirs(folder, exist_ok=True)
    target = join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(STORY)
    return target


def run() -> None:
    save_entry(output_folder())


if __name__ == "__main__":
    run()
