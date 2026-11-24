"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word describing home Wi-Fi to ``<OUTPUT_DIR>/entry.txt``.

The word: "cliffhanger" — home Wi-Fi that always freezes right at the
good part: the climax of the episode, the boss's verdict on the call,
the final seconds of the match. Full bars, then nothing, exactly when
it matters most. It is funny the instant you read it, true of every
household's Wi-Fi, and it makes a great network name.

Stdlib only (``os`` and ``sys``). Run with ``python3 main.py``.
Set ``OUTPUT_DIR`` to override the output folder (default ``/output``).
"""

import os
import sys

WORD = "cliffhanger"


def main() -> int:
    # Gate: 1-20 characters, a single word, not only whitespace.
    assert 1 <= len(WORD) <= 20, "word must be 1-20 characters"
    assert WORD.strip() == WORD and WORD, "word must not be only whitespace"
    assert not any(ch.isspace() for ch in WORD), "word must be a single word"
    assert all(ch.isprintable() for ch in WORD), "word must have no control chars"
    assert "\n" not in WORD and "\r" not in WORD, "word must have no newline"

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # No trailing newline: the file is exactly the word, nothing else.
    data = WORD.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read back and confirm byte-identical output.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "read-back mismatch: output is not byte-identical"
    assert written.decode("utf-8") == WORD, "output is not valid UTF-8 text"

    print(f"Wrote {len(WORD)}-character entry to {path}: {WORD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
