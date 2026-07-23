#!/usr/bin/env python3
"""Detection test for the branches_from lineage-edge integrity check
(STD-0004 v1.2 §7.2 / ADR-GOV-0009 D4).

Zero branches_from edges exist in the vault at introduction (INV-0016 populates
them, not this session), so an expected-clean live run proves nothing. This
proves the positive cases:

  * relationship_entries extracts branches_from edges WITH their qualifier (the
    exact helper graph_integrity.py and build_view.py both use -- shared code);
  * branches_from_problems flags a missing qualifier, an out-of-vocabulary
    qualifier, and a non-ENT target, and passes a valid ENT->ENT/qualified edge;
  * a non-ENT source is flagged (checked with a synthetic source id);
  * graph_integrity.py is wired to the helper and exits non-zero on branch
    errors; build_view.py renders the qualifier on the chip (source assertions).

Run: python tools/tests/test_branches_from.py
"""

from pathlib import Path
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import (  # noqa: E402
    parse_frontmatter,
    read_text,
    relationship_entries,
    branches_from_problems,
    BRANCH_QUALIFIERS,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"
TOOLS = Path(__file__).resolve().parent.parent

failures = []

print("branches_from lineage-edge integrity-detection test (STD-0004 v1.2 §7.2)")
print()

# 1. Extraction: qualifiers are read off the entries.
text = read_text(FIXTURES / "branches_from_edges.md")
fm, _ = parse_frontmatter(text)
meta = yaml.safe_load(fm)
entries = relationship_entries(meta)
branches = [(e["target"], e["qualifier"]) for e in entries if e["type"] == "branches_from"]

if len(branches) != 5:
    failures.append(f"expected 5 branches_from edges extracted, got {len(branches)}: {branches}")
by_target = dict(branches)
if by_target.get("ENT-9000") != "schism":
    failures.append(f"ENT-9000 qualifier should be 'schism', got {by_target.get('ENT-9000')!r}")
if by_target.get("ENT-9007") is not None:
    failures.append(f"ENT-9007 qualifier should be None (absent), got {by_target.get('ENT-9007')!r}")
if by_target.get("ENT-9008") != "continuation":
    failures.append(f"ENT-9008 qualifier should be 'continuation', got {by_target.get('ENT-9008')!r}")
print(f"  extraction -> {len(branches)} edges; qualifiers={[q for _, q in branches]}")

# 2. Integrity: type_of maps every ENT-* to 'ENT' and the CLM target to 'CLM'.
#    Source is an ENT (ENT-9010), so only per-edge problems should surface.
def type_of(target):
    return target.split("-")[0] if target.startswith(("ENT-", "CLM-", "SRC-")) else None

problems = branches_from_problems("ENT-9010", branches, type_of)
reasons = [why for _, why in problems]

def has(target, fragment):
    return any(t == target and fragment in why for t, why in problems)

if not has("ENT-9006", "invalid qualifier"):
    failures.append(f"invalid qualifier (ENT-9006) not caught: {problems}")
if not has("ENT-9007", "missing REQUIRED qualifier"):
    failures.append(f"missing qualifier (ENT-9007) not caught: {problems}")
if not has("CLM-9099", "target is not an ENT"):
    failures.append(f"non-ENT target (CLM-9099) not caught: {problems}")
if any(t == "ENT-9000" for t, _ in problems):
    failures.append(f"valid edge ENT-9000/schism must NOT be flagged: {problems}")
# prove the positive: the sixth qualifier `continuation` (ADR-GOV-0010 D1) is accepted.
if any(t == "ENT-9008" for t, _ in problems):
    failures.append(f"valid edge ENT-9008/continuation must NOT be flagged: {problems}")
print(f"  integrity (ENT source) -> {len(problems)} problems: {reasons}")

# 3. Non-ENT source is flagged for every edge.
src_problems = branches_from_problems("CLM-1234", [("ENT-9000", "schism")], type_of)
if not any("source is not an ENT" in why for _, why in src_problems):
    failures.append(f"non-ENT source not caught: {src_problems}")
print(f"  integrity (non-ENT source) -> {len(src_problems)} problems")

# 4. Vocabulary sanity: 'reform' is shared between tradition_type and qualifiers
#    but the two lists are independent; assert the qualifier list is exactly the
#    ADR-GOV-0009 D4 set + the ADR-GOV-0010 D1 addition (`continuation`).
if set(BRANCH_QUALIFIERS) != {"schism", "reform", "syncretic-descent",
                              "heterodox-offshoot", "disputed", "continuation"}:
    failures.append(f"BRANCH_QUALIFIERS drifted from ADR-GOV-0009 D4 + ADR-GOV-0010 D1: {BRANCH_QUALIFIERS}")

# 5. Wiring: graph_integrity uses the helper and exits on branch errors;
#    build_view renders the qualifier on the chip.
gi = read_text(TOOLS / "graph_integrity.py")
if "branches_from_problems" not in gi:
    failures.append("graph_integrity.py must import/use branches_from_problems")
if "branch_errors" not in gi or "dangling or branch_errors" not in gi:
    failures.append("graph_integrity.py must exit non-zero on branch_errors")
if 'dating_claims' not in gi:
    failures.append("graph_integrity.py must resolve dating_claims for dangling")

bv = read_text(TOOLS / "build_view.py")
if "rel_qualifiers" not in bv or "branches_from (" not in bv:
    failures.append("build_view.py must render the branches_from qualifier on the chip")
print("  wiring -> graph_integrity exits on branch errors; build_view renders the qualifier")

print()

if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (branches_from qualifier/ENT-restriction violations detected; valid edge passes)")
sys.exit(0)
