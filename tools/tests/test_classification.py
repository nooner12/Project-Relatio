#!/usr/bin/env python3
"""Detection test for validator_rules.yaml filename classification.

First test to touch classification at all; modelled on
test_version_coherence.py (the house standalone fixture-script pattern,
including its source-level guard technique).

Prove-the-positive rationale: before the 2026-07-25 change, a file named
"Knowledge Base Map of Content.md" or "Relatio-Transfer-Brief-Standard.md"
fell through to `defaults` and "passed" only because nothing is required of
an unclassified file. A vault-still-passes run cannot distinguish that
silence from recognition. This test FIRES on the new behaviour: each new
`filename_contains` fragment ("Map of Content", "Transfer-Brief") must route
a real on-disk fixture filename to the `infrastructure_documents` rule —
identity-checked, because `infrastructure_documents` and `defaults` have
equal field values and only rule *identity* proves the fragment matched.

It also guards the trap named in the transfer brief: the match is a literal
substring, so "Transfer Brief" with a space would NOT match
"Relatio-Transfer-Brief-Standard.md" and would fail silently. The fragment
is asserted to be a substring of the exact owner-placed filename.

The classify() under test is validate.py's own, extracted by AST so the test
exercises the real matching code without importing validate.py (which runs a
full vault scan at module level).

Run: python tools/tests/test_classification.py
"""

import ast
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import read_text  # noqa: E402

TOOLS = Path(__file__).resolve().parent.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures"

failures = []

RULES = yaml.safe_load(read_text(TOOLS / "validator_rules.yaml"))
INFRA = RULES["document_types"]["infrastructure_documents"]
IDENTIFIED = RULES["document_types"]["identified_documents"]
DEFAULTS = RULES["defaults"]


def load_real_classify():
    """Extract validate.py's classify() via AST — the real code, no scan."""
    tree = ast.parse(read_text(TOOLS / "validate.py"))
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "classify":
            module = ast.Module(body=[node], type_ignores=[])
            namespace = {"RULES": RULES}
            exec(compile(module, "validate.py:classify", "exec"), namespace)
            return namespace["classify"]
    raise AssertionError("classify() not found in validate.py")


classify = load_real_classify()


def check(filename, expected_rule, label):
    got = classify(filename)
    ok = got is expected_rule
    if not ok:
        failures.append(f"{filename!r}: expected {label}, got a different rule")
    print(f"  {filename}\n    -> {label if ok else 'WRONG RULE'}")


print("classification detection test (validator_rules.yaml filename_contains)")
print()

# Positive: each new fragment routes a real fixture filename to the
# infrastructure rule. The fixture files exist on disk so the names under
# test are real names, not typo-prone string literals.
for fixture_name in (
    "Knowledge Base Map of Content.md",
    "Relatio-Transfer-Brief-Standard.md",
):
    if not (FIXTURES / fixture_name).exists():
        failures.append(f"fixture missing on disk: {fixture_name}")
    check(fixture_name, INFRA, "infrastructure_documents")

# The silent-failure trap: the fragment must be a literal substring of the
# exact owner-placed filename ("Transfer Brief" with a space would not be).
if "Transfer-Brief" not in INFRA.get("filename_contains", []):
    failures.append("'Transfer-Brief' fragment missing from filename_contains")
if "Map of Content" not in INFRA.get("filename_contains", []):
    failures.append("'Map of Content' fragment missing from filename_contains")
if "Transfer-Brief" not in "Relatio-Transfer-Brief-Standard.md":
    failures.append("'Transfer-Brief' is not a substring of the real filename")

# Negative control: a name carrying no fragment still falls to defaults —
# identity-checked, proving the positives above matched on the fragment
# rather than on any accident of equal field values.
check("coherent_control.md", DEFAULTS, "defaults")

# Regression guards: existing classifications are unchanged.
check("Kernel Index.md", INFRA, "infrastructure_documents")
check("CLM-0001 - Non-Striving Convergence.md", IDENTIFIED, "identified_documents")

print()

if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (2 new fragments fire, defaults control silent, priors hold)")
sys.exit(0)
