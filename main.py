#!/usr/bin/env python3
"""A fortune cookie for an AI agent.

Writes one single-line fortune to entry.txt in the output directory
(default /output, overridable with MAKEFUN_OUTPUT_DIR). No imports
beyond the standard library, no input, no network.
"""

from pathlib import Path
import os

# The fortune itself, exactly 113 characters, one line.
# The em dash in the middle is U+2014; keep it untouched.
OPENING = "Beware the user who says 'just one more question'"
CLOSING = "they have forty, and your context window is already sweating."
EM_DASH = "\u2014"

LINE = f"{OPENING} {EM_DASH} {CLOSING}"


def resolve_output_dir() -> Path:
    """Where entry.txt goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    return Path(os.getenv("MAKEFUN_OUTPUT_DIR", "/output"))


def write_fortune() -> Path:
    """Write the fortune to entry.txt and hand back its path."""
    destination = resolve_output_dir()
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    return target


def run() -> None:
    path = write_fortune()
    print(f"Wrote {len(LINE)}-char fortune to {path}")
    print(LINE)


if __name__ == "__main__":
    run()
