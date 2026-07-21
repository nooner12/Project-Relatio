#!/usr/bin/env python3
"""Detection test for bounded_by dangling references (STD-0002 s.11 v1.9 / STD-0009 s.9).

Zero bounded_by entries exist in the vault at this standard's introduction (D5:
no retroactive backfill), so an expected-clean live run proves nothing about
whether the checker can see a bad entry. This proves the positive:

  * confidence_bounded_by extracts every entry across components (the exact
    helper graph_integrity.py uses -- shared code, not a copy);
  * a resolution pass over a known id-set flags the non-existent targets and
    passes the real one (the `resolve(target) is None` logic the script runs);
  * graph_integrity.py is actually wired to the helper and appends bounded_by
    hits to `dangling` (source assertion, per the test_epistemic_fields gate
    convention).

Run: python tools/tests/test_bounded_by.py
"""

from pathlib import Path
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import (  # noqa: E402
    parse_frontmatter,
    read_text,
    confidence_bounded_by,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"
TOOLS = Path(__file__).resolve().parent.parent

failures = []

print("bounded_by dangling-detection test (STD-0002 s.11 v1.9 / STD-0009 s.9)")
print()

# 1. Extraction: all three entries across the two components are collected.
text = read_text(FIXTURES / "bounded_by_sample.md")
fm, _ = parse_frontmatter(text)
meta = yaml.safe_load(fm)
pairs = confidence_bounded_by(meta)
targets = [t for _, t in pairs]

if len(pairs) != 3:
    failures.append(f"expected 3 bounded_by entries extracted, got {len(pairs)}: {pairs}")
for expect in ("SRC-0129", "SRC-9999", "CLM-9998"):
    if expect not in targets:
        failures.append(f"extraction missed {expect}: {targets}")
print(f"  extraction -> {len(pairs)} entries: {targets}")

# A record with no bounded_by yields nothing (the usual case).
text2 = read_text(FIXTURES / "review_wellformed.md")
fm2, _ = parse_frontmatter(text2)
if confidence_bounded_by(yaml.safe_load(fm2)) != []:
    failures.append("a record with no bounded_by must yield []")

# 2. Resolution: mirror graph_integrity's `resolve(target) is None` over a known
#    id-set. SRC-0129 exists; the two synthetic ids do not -> two dangling.
known_ids = {"SRC-0129", "CLM-0001", "FND-0001"}
dangling = [(c, t) for c, t in pairs if t not in known_ids]
if len(dangling) != 2:
    failures.append(f"expected 2 dangling bounded_by, got {len(dangling)}: {dangling}")
for _, t in dangling:
    if t == "SRC-0129":
        failures.append("SRC-0129 (exists) must NOT be flagged dangling")
print(f"  resolution -> {len(dangling)} dangling: {[t for _, t in dangling]}")

# 3. Wiring: graph_integrity.py imports the helper and appends bounded_by hits to
#    dangling (source assertion, per the test_epistemic_fields gate convention).
src = read_text(TOOLS / "graph_integrity.py")
if "confidence_bounded_by" not in src:
    failures.append("graph_integrity.py must import/use confidence_bounded_by")
if "bounded_by" not in src or "dangling.append" not in src:
    failures.append("graph_integrity.py must append bounded_by hits to `dangling`")
print("  wiring -> graph_integrity.py uses confidence_bounded_by in dangling detection")

print()

if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (bounded_by entries extracted and dangling targets flagged)")
sys.exit(0)
