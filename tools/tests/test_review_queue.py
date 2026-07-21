#!/usr/bin/env python3
"""Detection test for review_queue.py (STD-0009 §4/§5).

The live queue is expected EMPTY at introduction (all review_dates future-dated;
no supersessions; no post-review upstream grade changes; no recorded flags), so
an expected-empty live run proves nothing. This drives synthetic inputs through
the pure detect() core and proves every trigger fires and resolves to the
STD-0009 §5 scope/act — plus that the near-miss cases do NOT fire.

Run: python tools/tests/test_review_queue.py
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from review_queue import detect, load_flags, FLAG_RE, GRADE_CHANGE_RE, GRADE_NOCHANGE_RE  # noqa: E402

failures = []


def has(items, object_, trigger, act):
    return any(i["object"] == object_ and i["trigger"] == trigger and i["act"] == act
              for i in items)


TODAY = (2026, 7, 21)

# --- Synthetic graph ------------------------------------------------------
objects = {
    "SRC-0500": {"operational_status": "Superseded", "grade_change_dates": []},
    "SRC-0501": {"operational_status": "Active", "grade_change_dates": [(2026, 8, 1)]},  # re-graded AFTER
    "SRC-0502": {"operational_status": "Active", "grade_change_dates": [(2026, 1, 1)]},  # re-graded BEFORE
    "SRC-0503": {"operational_status": "Active", "grade_change_dates": []},
}

records = [
    # time_decay: review_date in the past.
    {"id": "CLM-0500", "review_date": (2026, 6, 1), "last_reviewed": (2025, 9, 1),
     "derived_from": ["SRC-0503"], "components": [{"component": "overall", "bounded_by": []}]},
    # source_superseded: a component bounded by a Superseded source; not yet due.
    {"id": "CLM-0501", "review_date": (2027, 6, 1), "last_reviewed": (2026, 7, 20),
     "derived_from": ["SRC-0503"],
     "components": [{"component": "placement", "bounded_by": ["SRC-0500"]}]},
    # upstream_grade_change: bounded source re-graded after last_reviewed; not due.
    {"id": "CLM-0502", "review_date": (2027, 6, 1), "last_reviewed": (2026, 7, 20),
     "derived_from": ["SRC-0503"],
     "components": [{"component": "mechanics", "bounded_by": ["SRC-0501"]}]},
    # near-miss: bounded source re-graded BEFORE last_reviewed → must NOT fire.
    {"id": "CLM-0503", "review_date": (2027, 6, 1), "last_reviewed": (2026, 7, 20),
     "derived_from": ["SRC-0502"],
     "components": [{"component": "overall", "bounded_by": ["SRC-0502"]}]},
]

flags = [
    {"trigger": "contradiction", "object": "CLM-0504", "scope": "conflicts with CLM-0080"},
    {"trigger": "field_prose_divergence", "object": "CLM-0505", "scope": "confidence field vs prose"},
]

items = detect(records, objects, flags, TODAY)

print("review-queue detection test (STD-0009 §4/§5)")
print()
for it in items:
    print(f"  {it['object']:9} {it['trigger']:22} -> {it['act']}")
print()

# Each trigger fires with the correct act.
if not has(items, "CLM-0500", "time_decay", "Light re-affirmation"):
    failures.append("time_decay did not fire / wrong act")
if not has(items, "CLM-0501", "source_superseded", "Targeted re-grade"):
    failures.append("source_superseded did not fire / wrong act")
if not has(items, "CLM-0502", "upstream_grade_change", "Targeted re-grade"):
    failures.append("upstream_grade_change did not fire / wrong act")
if not has(items, "CLM-0504", "contradiction", "Full OPS-0003 circuit"):
    failures.append("contradiction flag did not fire / wrong act")
if not has(items, "CLM-0505", "field_prose_divergence", "Reconciliation"):
    failures.append("field_prose_divergence flag did not fire / wrong act")

# Near-miss must NOT fire: upstream change dated before last_reviewed.
if any(i["object"] == "CLM-0503" for i in items):
    failures.append("CLM-0503 must not fire (upstream change predates last_reviewed)")

# Near-miss: a future review_date must NOT produce time_decay.
if has(items, "CLM-0501", "time_decay", "Light re-affirmation"):
    failures.append("time_decay must not fire on a future review_date")

# Marker convention: a well-formed flag line parses; a plain mention does not.
good = "- REVIEW-FLAG | trigger=contradiction | object=CLM-0075 | scope=the conflicting claims"
if not FLAG_RE.search(good):
    failures.append("FLAG_RE must parse a well-formed REVIEW-FLAG line")
plain = "GB-2026-099: the CLM-0043/0046/0050 borderline split is a contradiction worth noting"
if FLAG_RE.search(plain):
    failures.append("FLAG_RE must NOT match ordinary Backlog prose (the not-a-flag case)")

# Grade-change row heuristic: real change matches; a 'no level changed' row does not.
if not GRADE_CHANGE_RE.search("Targeted re-grade: overall Level 2→Level 3"):
    failures.append("GRADE_CHANGE_RE must match a real level change")
nochange = "F-1 CLM-0064 carry-over sub-grade lowered Level 3→Level 2, no confidence level raised"
if GRADE_CHANGE_RE.search(nochange) and not GRADE_NOCHANGE_RE.search(nochange):
    failures.append("a 'no confidence level' row must be excluded by GRADE_NOCHANGE_RE")

print()
if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (all five triggers fire with correct acts; near-misses excluded)")
sys.exit(0)
