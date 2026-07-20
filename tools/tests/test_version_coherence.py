#!/usr/bin/env python3
"""Detection test for the version-coherence check (GB-2026-035).

An expected-zero run against the vault cannot distinguish a working checker from
a blind one -- the MAX_PATH scanner failure recorded in GB-2026-028 is the
standing lesson: it reported clean while silently skipping four files. This test
proves the positive case, and guards the two traps named in the build notes:

  * newest history row by **parse-and-max, not by position** (GB-2026-029)
  * versions compared as **tuples, not floats** (1.23 > 1.9)

It also guards the **severity ruling**: the check reports at ERROR level (owner
decision 2026-07-21, promoted from the warning level it was built at). That is a
governance decision rather than a detection property, so it is asserted against
validate.py's source -- enough to catch a silent regression to warning.

Run: python tools/tests/test_version_coherence.py
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import (  # noqa: E402
    parse_frontmatter,
    read_text,
    version_elements,
    parse_version,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"

failures = []


def elements_for(path):
    text = read_text(path)
    frontmatter, body = parse_frontmatter(text)
    return version_elements(
        body if frontmatter is not None else text,
        frontmatter,
    )


def incoherent(found):
    present = {
        label: found[label]
        for label in ("frontmatter", "heading", "history")
        if found[label] is not None
    }
    if len(present) < 2:
        return False, present
    return len({parse_version(v) for v in present.values()}) > 1, present


def check(name, expect_flagged, expect_history=None):
    found = elements_for(FIXTURES / name)
    flagged, present = incoherent(found)

    if flagged != expect_flagged:
        failures.append(
            f"{name}: expected flagged={expect_flagged}, got {flagged} ({present})"
        )
    if expect_history is not None and found["history"] != expect_history:
        failures.append(
            f"{name}: expected newest history row {expect_history}, "
            f"got {found['history']} (rows in order: {found['rows']})"
        )

    status = "FLAGGED" if flagged else "clean"
    print(f"  {name}\n    -> {status}; elements: {present}")


print("version-coherence detection test (GB-2026-035)")
print()

# Positive: the dominant shape of the 2026-07-20 sweep.
check("drift_frontmatter_vs_history.md", expect_flagged=True, expect_history="0.2")

# Positive: newest row is neither last by position nor highest by float.
check("drift_out_of_order_rows.md", expect_flagged=True, expect_history="1.23")

# Negative control: coherent at 2.10, which a float comparator would misjudge.
check("coherent_control.md", expect_flagged=False, expect_history="2.10")

# Unit guard on the comparator itself.
if not parse_version("1.23") > parse_version("1.9"):
    failures.append("parse_version: 1.23 should sort above 1.9 (tuple, not float)")
if parse_version("not-a-version") is not None:
    failures.append("parse_version: non-numeric input should return None")

# Guard the YAML float-coercion trap directly: an unquoted `version: 2.10` is
# valid YAML for the float 2.1. Reading it through a YAML load would drop the
# trailing zero and manufacture drift against a 2.10 history row. The control
# fixture above covers this end-to-end; this asserts the literal read.
control = elements_for(FIXTURES / "coherent_control.md")
if control["frontmatter"] != "2.10":
    failures.append(
        "frontmatter version must be read literally, not via yaml: "
        f"expected '2.10', got {control['frontmatter']!r}"
    )

# Severity guard (owner ruling 2026-07-21): version incoherence is an ERROR.
# Asserted against source because severity is a policy choice, not a detection
# property -- this exists to catch a silent regression back to warning level.
validate_src = read_text(Path(__file__).resolve().parent.parent / "validate.py")
marker = 'f"Version incoherence: {file.name}\\n"'
before = validate_src.split(marker)[0]
appended_to = before.rstrip().rsplit("\n", 1)[-1].strip()

if not appended_to.startswith("errors.append"):
    failures.append(
        "version incoherence must report at ERROR level (owner ruling "
        f"2026-07-21); validate.py appends it to: {appended_to!r}"
    )
else:
    print("  severity: reports via errors.append -> ERROR level (owner ruling)")

print()

if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (2 drift fixtures flagged, 1 coherent fixture silent)")
sys.exit(0)
