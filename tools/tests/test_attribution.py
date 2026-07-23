#!/usr/bin/env python3
"""Detection test for the attribution shape check (STD-0002 §6/§6.1 v1.12).

An expected-clean run against the vault cannot distinguish a working checker
from a blind one (the GB-2026-035 lesson), and the whole corpus was backfilled
to conformance in the commit before enforcement — so a green vault proves
nothing on its own. This proves the positive cases:

  * a well-formed single-entry attribution produces no problems;
  * a **TWO-ENTRY list PASSES** — the additivity proof. ADR-GOV-0011 §8 defers
    per-event attribution to Stage 2, which extends this same list; a Stage 1
    checker that rejected a second entry would turn that extension into a
    migration, which is exactly what the list shape exists to prevent;
  * a missing field is caught;
  * a scalar block (the shape that would force the Stage 2 migration) is caught;
  * an out-of-vocabulary `ai_degree` is caught;
  * a malformed `date` is caught;
  * both directions of the `ai_model_family: none` iff `ai_degree: unassisted`
    pairing rule are caught;
  * a half-authored entry names each absent key.

Run: python tools/tests/test_attribution.py
"""

from pathlib import Path
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import (  # noqa: E402
    parse_frontmatter,
    read_text,
    attribution_problems,
    AI_DEGREES,
    ATTRIBUTION_KEYS,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"

failures = []


def problems_for(name):
    text = read_text(FIXTURES / name)
    frontmatter, _ = parse_frontmatter(text)
    meta = yaml.safe_load(frontmatter)
    return attribution_problems(meta)


def check(name, expected_fragments, label=""):
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
    print(f"  {name}{label}\n    -> {status}")


print("attribution detection test (STD-0002 §6 v1.12 / ADR-GOV-0011 B+C)")
print()

# Negative control: well-formed single entry, silent.
check("attribution_wellformed.md", [])

# THE ADDITIVITY PROOF (ADR-GOV-0011 §8). Two entries must pass unflagged.
check("attribution_two_entries.md", [], "   [Stage 2 additivity]")

# Missing the field entirely.
check("attribution_missing.md", ["missing `attribution`"])

# A scalar block rather than a list.
check("attribution_scalar.md", ["must be a non-empty list"])

# Out-of-vocabulary degree.
check("attribution_bad_degree.md", ["ai_degree must be one of"])

# Malformed date.
check("attribution_bad_date.md", ["date must be YYYY-MM-DD"])

# Both directions of the pairing rule, one per entry.
check(
    "attribution_pairing.md",
    [
        "must be `none` when ai_degree is `unassisted`",
        "must name a model family when ai_degree is",
    ],
)

# A half-authored entry: four absent keys, each named.
check(
    "attribution_incomplete.md",
    [
        "attribution[0].role is required",
        "attribution[0].date is required",
        "attribution[0].ai_degree is required",
        "attribution[0].ai_model_family is required",
    ],
)

# ---------------------------------------------------------------------------
# Unit guards
# ---------------------------------------------------------------------------

# An empty list is not a list of one -- it must be rejected, not read as absent.
if not any("non-empty list" in p for p in attribution_problems({"attribution": []})):
    failures.append("an empty attribution list must be rejected")

# An entry that is not a mapping.
if not any(
    "must be a mapping" in p
    for p in attribution_problems({"attribution": ["Brian Noon"]})
):
    failures.append("a non-mapping attribution entry must be rejected")

# Whitespace-only actor is not a name.
blank = attribution_problems({"attribution": [{
    "actor": "   ", "role": "Vision Steward", "event": "created",
    "date": "2026-07-22", "ai_degree": "ai-delegated", "ai_model_family": "Claude",
}]})
if not any("actor must be a non-empty string" in p for p in blank):
    failures.append(f"whitespace-only actor must be rejected: {blank}")

# `event` is deliberately NOT vocabulary-checked: the Stage 2 vocabulary is not
# yet decided (ADR-GOV-0011 §8), so a future value must not fail today's build.
future_event = attribution_problems({"attribution": [{
    "actor": "Brian Noon", "role": "Vision Steward", "event": "verified",
    "date": "2026-07-22", "ai_degree": "unassisted", "ai_model_family": "none",
}]})
if future_event:
    failures.append(f"a non-`created` event must not be flagged at Stage 1: {future_event}")

# The controlled vocabulary is exactly the three ADR-GOV-0011 Decision C degrees.
if AI_DEGREES != ("unassisted", "ai-assisted", "ai-delegated"):
    failures.append(f"ai_degree vocabulary drifted from ADR-GOV-0011 §4: {AI_DEGREES}")

if set(ATTRIBUTION_KEYS) != {"actor", "role", "event", "date", "ai_degree",
                             "ai_model_family"}:
    failures.append(f"attribution key set drifted from STD-0002 §6: {ATTRIBUTION_KEYS}")

print()

if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (malformed fixtures flagged; well-formed and two-entry "
      "fixtures silent)")
sys.exit(0)
