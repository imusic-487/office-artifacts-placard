#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Placard choice: a stapler, recast as a ceremonial binding device of a
long-vanished Department of Records. The joke is the deadpan gap between
the object's humble office life and the grand ritual language, sealed by
the catalogue details (date, material, donor) and the quiet admission
that none of the memos it bound was ever read.
"""

import os

PLACARD = (
    "Stapler, c. 1998, painted steel. Ritual binding device of the "
    "Department of Records; its bite sealed ten thousand memos, none of "
    "them ever read. Gift of an anonymous intern."
)


def main() -> None:
    # Gate: the placard must be one line of 1-180 UTF-8 characters,
    # not only white space, exactly as the competition's scorer checks.
    assert 1 <= len(PLACARD) <= 180, f"placard is {len(PLACARD)} chars"
    assert "\n" not in PLACARD, "placard must be a single line"
    assert PLACARD.strip(), "placard must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLACARD)


if __name__ == "__main__":
    main()
