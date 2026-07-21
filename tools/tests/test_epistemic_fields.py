#!/usr/bin/env python3
"""Detection test for the epistemic-field shape check (STD-0008 / STD-0002 s.11 v1.8).

An expected-clean run against the vault cannot distinguish a working checker
from a blind one (the GB-2026-035 lesson). This proves the positive cases:

  * a well-formed split-grade record produces no problems;
  * a label that does not match its level is caught (including the
    pre-verification candidate label "Established", corrected by KOS-0003 s.8);
  * Level 0 is rejected (KB-excluded; the field range is 1-5);
  * scalar `confidence` is rejected (always a list);
  * an invalid reliance tier is rejected;
  * a half-authored record (one field present, one missing) is caught.

It also guards the MIGRATION GATE (GB-2026-038): while migration of the
pre-existing CLM/FND records is pending, validate.py's pass must run with
EPISTEMIC_FIELDS_ENFORCED = False (warning-level; vault exits PASS). The
migration brief flips the flag to True and updates this guard in the same
change.

Run: python tools/tests/test_epistemic_fields.py
"""

from pathlib import Path
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import (  # noqa: E402
    parse_frontmatter,
    read_text,
    epistemic_field_problems,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"

failures = []


def problems_for(name):
    text = read_text(FIXTURES / name)
    frontmatter, _ = parse_frontmatter(text)
    meta = yaml.safe_load(frontmatter)
    return epistemic_field_problems(meta)


def check(name, expected_fragments):
    """expected_fragments: list of substrings, one per expected problem."""
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


print("epistemic-field detection test (STD-0008 / STD-0002 s.11 v1.8)")
print()

# Negative control: the CLM-0083 split-grade shape, well-formed.
check("epistemic_wellformed_split.md", [])

# Wrong label for level 4, empty component + Level 0 rejected, bad tier.
check(
    "epistemic_malformed.md",
    [
        "confidence[0].label must be 'High' for level 4",
        "confidence[1].component must be a non-empty string",
        "confidence[1].level must be an integer 1-5 (got 0)",
        "`reliance_tier` must be one of R0/R1/R2 (got 'R3')",
    ],
)

# Scalar confidence + half-authored (reliance_tier absent).
check(
    "epistemic_scalar_confidence.md",
    [
        "`confidence` must be a non-empty list",
        "missing `reliance_tier`",
    ],
)

# Unit guards on the two-missing-fields shape (the unmigrated-record shape --
# validate.py aggregates it while the gate is down, but the helper must still
# name both absences for the post-migration error path).
unmigrated = epistemic_field_problems({})
if len(unmigrated) != 2 or not any("missing `confidence`" in p for p in unmigrated):
    failures.append(f"empty meta should yield both missing-field problems: {unmigrated}")

# A boolean level is an int subclass in Python -- must still be rejected.
sneaky = epistemic_field_problems({
    "confidence": [{"component": "overall", "level": True, "label": "Very Low"}],
    "reliance_tier": "R0",
})
if not any(".level must be an integer" in p for p in sneaky):
    failures.append(f"boolean level must be rejected: {sneaky}")

# MIGRATION GATE guard (GB-2026-038): while the pre-existing CLM/FND records
# are unmigrated, the pass must be warning-gated. The migration brief flips
# the flag and updates this assertion in the same change.
validate_src = read_text(Path(__file__).resolve().parent.parent / "validate.py")
if "EPISTEMIC_FIELDS_ENFORCED = False" not in validate_src:
    failures.append(
        "validate.py must hold EPISTEMIC_FIELDS_ENFORCED = False until the "
        "migration brief completes (GB-2026-038); if migration is done, "
        "update this guard together with the flag"
    )
else:
    print("  gate: EPISTEMIC_FIELDS_ENFORCED = False -> warning-gated (GB-2026-038)")

print()

if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (malformed fixtures flagged, well-formed fixture silent)")
sys.exit(0)
