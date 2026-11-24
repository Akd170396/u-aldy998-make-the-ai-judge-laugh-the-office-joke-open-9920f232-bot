"""Make the AI Judge Laugh: the Office Joke Open.

Writes one line of office comedy (max 200 chars) to entry.txt.
Stdlib only; deterministic; no network.
"""

import os
import sys

JOKE = "Our office plant died, so HR sent a condolence email and booked a 30-minute meeting about resilience."


def validate(text):
    """Gate mirror: UTF-8 text, 1-200 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Read-back verification: the file must hold exactly the validated joke.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        raise RuntimeError("read-back mismatch: entry.txt does not match JOKE")
    validate(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
