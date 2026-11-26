"""make.fun entry: The Self-Checkout Is Judging You.

Writes exactly one funny line in the voice of a smug, judgmental
self-checkout machine to /output/entry.txt. Deterministic, no network,
no randomness, standard library only.
"""

LINE = (
    "Four frozen pizzas, one wilted salad, and you scanned the salad "
    "twice like it cancels the pizzas \u2014 nice try. I did the maths."
)


def main() -> None:
    # Competition gate: 1-200 Unicode code points, not only whitespace.
    # The judge reads entry.txt as text, so a NUL byte would corrupt the
    # line (and a truncated/empty file would fail the gate outright).
    assert "\x00" not in LINE, "line must not contain NUL bytes"
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} code points"
    assert LINE.strip(), "line must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
