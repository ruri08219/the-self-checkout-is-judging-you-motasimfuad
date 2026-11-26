"""make.fun entry: The Self-Checkout Is Judging You.

Writes exactly one funny line in the voice of a smug, judgmental
self-checkout machine to /output/entry.txt. Deterministic, no network,
no randomness, standard library only.
"""

LINE = (
    "Four frozen pizzas, one wilted salad, and you scanned the salad "
    "twice like it cancels the pizzas \u2014 nice try. I did the maths."
)


def validate_line(line: str) -> str:
    """Enforce the competition gate on the line before it is written."""
    # Competition gate: 1-200 Unicode code points, not only whitespace.
    # The judge reads entry.txt as text, so a NUL byte would corrupt the
    # line (and a truncated/empty file would fail the gate outright).
    assert "\x00" not in line, "line must not contain NUL bytes"
    assert 1 <= len(line) <= 200, f"line is {len(line)} code points"
    assert line.strip(), "line must not be only whitespace"
    return line


def write_entry(line: str) -> None:
    """Write the validated line verbatim to the competition output path."""
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(validate_line(line))


def main() -> None:
    write_entry(LINE)


if __name__ == "__main__":
    main()
