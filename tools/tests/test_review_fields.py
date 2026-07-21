#!/usr/bin/env python3
"""Detection test for the review-field shape check (STD-0009 s.8 / STD-0002 s.11 v1.9).

An expected-clean run against the vault cannot distinguish a working checker from
a blind one (the GB-2026-035 lesson). This proves the positive cases:

  * a well-formed record produces no problems;
  * a non-positive review_cycle is caught;
  * a malformed last_reviewed date is caught;
  * the review_date == last_reviewed + review_cycle arithmetic is enforced when
    all three are otherwise well-formed (the drift case);
  * a half-authored record (fields missing) names each absence.

Run: python tools/tests/test_review_fields.py
"""

from pathlib import Path
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import (  # noqa: E402
    parse_frontmatter,
    read_text,
    review_field_problems,
    add_months,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"

failures = []


def problems_for(name):
    text = read_text(FIXTURES / name)
    frontmatter, _ = parse_frontmatter(text)
    meta = yaml.safe_load(frontmatter)
    return review_field_problems(meta)


def check(name, expected_fragments):
    problems = problems_for(name)
    if len(problems) != len(expected_fragments):
        failures.append(
            f"{name}: expected {len(expected_fragments)} problems, "
            f"got {len(problems)}: {problems}"
        )
    for fragment in expected_fragments:
        if not any(fragment in p for p in problems):
            failures.append(f"{name}: no problem mentions {fragment!r}: {problems}")
    status = f"{len(problems)} problem(s)" if problems else "clean"
    print(f"  {name}\n    -> {status}")


print("review-field detection test (STD-0009 s.8 / STD-0002 s.11 v1.9)")
print()

# Negative control: well-formed record, silent.
check("review_wellformed.md", [])

# review_cycle 0 (non-positive) and last_reviewed not a real date. The
# arithmetic check is skipped because last_reviewed is malformed -- exactly two
# problems surface, not three.
check(
    "review_malformed.md",
    [
        "`review_cycle` must be a positive integer",
        "`last_reviewed` must be YYYY-MM-DD",
    ],
)

# All three individually well-formed, but review_date != last_reviewed + cycle.
check(
    "review_arithmetic_drift.md",
    [
        "must equal last_reviewed + review_cycle months",
    ],
)

# Unit guards on the empty shape: all three absences named.
empty = review_field_problems({})
if len(empty) != 3:
    failures.append(f"empty meta should yield three missing-field problems: {empty}")
for fld in ("review_cycle", "last_reviewed", "review_date"):
    if not any(f"missing `{fld}`" in p for p in empty):
        failures.append(f"empty meta must name missing `{fld}`: {empty}")

# Unit guard: add_months clamps across a year boundary and month-length.
if add_months((2026, 7, 20), 9) != (2027, 4, 20):
    failures.append("add_months(2026-07-20, 9) must be 2027-04-20")
if add_months((2026, 12, 31), 2) != (2027, 2, 28):
    failures.append("add_months(2026-12-31, 2) must clamp to 2027-02-28")

# A boolean review_cycle is an int subclass -- must still be rejected.
sneaky = review_field_problems({
    "review_cycle": True, "review_date": "2027-04-20", "last_reviewed": "2026-07-20",
})
if not any("must be a positive integer" in p for p in sneaky):
    failures.append(f"boolean review_cycle must be rejected: {sneaky}")

print()

if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (malformed fixtures flagged, well-formed fixture silent)")
sys.exit(0)
