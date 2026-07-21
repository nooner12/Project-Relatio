#!/usr/bin/env python3
"""Detection test for the tradition-entity field shape check
(STD-0002 s.11 v1.10 / ADR-GOV-0009 D3).

Zero tradition-class entities exist in the vault at introduction (entities on
demand, ADR-GOV-0009 D2), so an expected-clean live run proves nothing about
whether the checker can see a bad one. The check GUARDS BIRTHS -- this proves
the positive cases against fixtures:

  * a well-formed tradition entity (all three fields, valid tradition_type)
    produces no problems;
  * a co-presence violation (one field missing) is caught;
  * an out-of-vocabulary tradition_type is caught;
  * a concept entity (none of the three fields) is left untouched -- the seven
    existing concept entities must never be flagged.

It also asserts the source wiring: validate.py imports the shared helper and
appends its problems to `errors` at ERROR level (the test_bounded_by convention).

Run: python tools/tests/test_tradition_entity.py
"""

from pathlib import Path
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import (  # noqa: E402
    parse_frontmatter,
    read_text,
    tradition_entity_problems,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"
TOOLS = Path(__file__).resolve().parent.parent

failures = []

print("tradition-entity field shape-detection test (STD-0002 s.11 v1.10)")
print()


def problems_for(name):
    text = read_text(FIXTURES / name)
    fm, _ = parse_frontmatter(text)
    meta = yaml.safe_load(fm)
    probs, dating = tradition_entity_problems(meta)
    return probs, dating


# 1. Well-formed -> no problems, dating_claims extracted.
probs, dating = problems_for("tradition_entity_wellformed.md")
if probs:
    failures.append(f"well-formed tradition entity flagged: {probs}")
if dating != ["CLM-9001"]:
    failures.append(f"expected dating_claims ['CLM-9001'], got {dating}")
print(f"  well-formed -> {len(probs)} problems; dating_claims={dating}")

# 2. Co-presence violation -> caught (mentions co-required + the missing field).
probs, _ = problems_for("tradition_entity_missing_field.md")
if not any("co-required" in p for p in probs):
    failures.append(f"co-presence violation not caught: {probs}")
if not any("dating_claims" in p for p in probs):
    failures.append(f"missing dating_claims not named: {probs}")
print(f"  co-presence violation -> {len(probs)} problems")

# 3. Bad tradition_type -> caught.
probs, _ = problems_for("tradition_entity_bad_type.md")
if not any("tradition_type" in p and "ancient" in p for p in probs):
    failures.append(f"bad tradition_type not caught: {probs}")
print(f"  bad tradition_type -> {len(probs)} problems")

# 4. Concept entity -> untouched.
probs, dating = problems_for("concept_entity.md")
if probs or dating:
    failures.append(f"concept entity must be untouched, got problems={probs} dating={dating}")
print(f"  concept entity -> {len(probs)} problems (must be 0)")

# 5. Wiring: validate.py uses the helper at error level.
src = read_text(TOOLS / "validate.py")
if "tradition_entity_problems" not in src:
    failures.append("validate.py must import/use tradition_entity_problems")
if "Tradition-entity fields malformed" not in src or "errors.append" not in src:
    failures.append("validate.py must append tradition-entity problems to `errors`")
print("  wiring -> validate.py enforces tradition-entity shape at error level")

print()

if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (tradition-entity shape violations detected; concept entities untouched)")
sys.exit(0)
