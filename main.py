"""One-Line Office Joke Laugh-Off — make.fun entry.

Writes one original one-line office joke to entry.txt inside
$MAKEFUN_OUTPUT_DIR (or /output when unset). Deterministic: no network,
no randomness, no clock. The joke is a fixed constant, so every run
produces byte-identical output.
"""

import os

ENTRY = (
    "My Slack status has read 'in a meeting' since Tuesday \u2014 "
    "and honestly, at this point, so have I."
)


def main() -> None:
    # Gate: entry must be one line of 1-200 characters, not only whitespace,
    # with no leading/trailing whitespace padding the count.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200
    assert ENTRY == ENTRY.strip()
    # The grader runs the repo read-only as nobody: only ever write to the
    # output directory from the environment, never next to the source files.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(
        os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline=""
    ) as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
