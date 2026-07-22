#!/usr/bin/env python3
"""Detection tests for the timeline emitter of build_view.py (ADR-GOV-0009).

House convention: prove the positive. Deliberately-shaped fixtures are driven
through the real parse+render path (object_from_text -> build_timeline_html)
and the assertions target the emitted HTML:

  * a tradition renders its display_range VERBATIM (as authored — Path A);
  * a root (no branches_from) renders the root marker and NO inbound edge;
  * each of the five qualifier kinds renders its own distinct marking, and
    `disputed` carries the explicit uncertainty note;
  * a Low-confidence dating renders distinctly from a Moderate one (the
    weak-grade box — a non-colour-only marking);
  * the reliance badge appears on EVERY tradition node (count == tradition
    count) and the standing reliance banner is present — the load-bearing gate;
  * the Zurvanism / overturned-hypothesis curated note is present and flagged
    as curated, not field-derived;
  * an unresolvable dating_claims pointer is reported as a graph error;
  * output is deterministic across two runs (fixed hash/date);
  * TREE-VIEW REGRESSION: build_html output is byte-identical whether or not
    the tradition fields are present on the nodes (the tree emitter must not
    read them), and contains no timeline markup.

Run: python tools/tests/test_timeline_view.py
"""

from datetime import date
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import read_text  # noqa: E402
from build_view import (  # noqa: E402
    object_from_text, build_html, build_timeline_html, timeline_entries,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"

failures = []


def want(cond, msg):
    if not cond:
        failures.append(msg)


def load(name):
    return object_from_text(read_text(FIXTURES / name))


# --- Parse the fixture mini-family ----------------------------------------
nodes = [
    load("tl_root.md"),
    load("tl_branch_schism.md"),
    load("tl_branch_reform.md"),
    load("tl_branch_syncretic.md"),
    load("tl_branch_heterodox.md"),
    load("tl_branch_disputed.md"),
    load("tl_claim_moderate.md"),
    load("tl_claim_low.md"),
]
if any(n is None for n in nodes):
    failures.append(f"a fixture failed to parse to a KB node: "
                    f"{[i for i, n in enumerate(nodes) if n is None]}")

GEN = date(2026, 7, 22)
html = build_timeline_html(nodes, "abc1234", GEN)
TRADITIONS = ["ENT-9100", "ENT-9101", "ENT-9102", "ENT-9103",
              "ENT-9104", "ENT-9105"]


def card_segment(html_text, ident):
    """The HTML slice for one timeline card (up to the next card or end)."""
    i = html_text.find(f'id="tl-{ident}"')
    if i == -1:
        return ""
    nxt = html_text.find('class="tl-card"', i + 1)
    end = nxt if nxt != -1 else len(html_text)
    return html_text[i:end]


# --- Verbatim display_range (Path A) ---------------------------------------
root = card_segment(html, "ENT-9100")
want("2nd millennium BCE (fixture-contested)" in root,
     "root display_range must render VERBATIM, as authored")
want("12th c. CE crystallisation (fixture)" in card_segment(html, "ENT-9105"),
     "branch display_range must render VERBATIM, as authored")

# --- Root: marker present, no inbound edge ---------------------------------
want("family root" in root and "tl-root-marker" in root,
     "root must carry the family-root marker")
want("branches_from" not in root.replace("no \nbranches_from edge", "")
     .replace("no branches_from edge", ""),
     "root must render NO inbound branches_from edge")

# --- Each qualifier kind renders its distinct marking ----------------------
for ident, qual in (("ENT-9101", "schism"), ("ENT-9102", "reform"),
                    ("ENT-9103", "syncretic-descent"),
                    ("ENT-9104", "heterodox-offshoot"),
                    ("ENT-9105", "disputed")):
    seg = card_segment(html, ident)
    want(f"qual-{qual}" in seg,
         f"{ident} must carry the qualifier-specific class qual-{qual}")
    want(f">{qual}</span>" in seg,
         f"{ident} must print its qualifier label {qual!r}")
# The five qualifier classes must be mutually distinct in style: each class
# appears in exactly one card, and the style tuples differ (colour+border).
for qual in ("qual-schism", "qual-reform", "qual-syncretic-descent",
             "qual-heterodox-offshoot", "qual-disputed"):
    count = html.count(f'class="tl-edge {qual}"')
    want(count == 1, f"{qual} must appear on exactly one edge, got {count}")
from build_view import QUALIFIER_STYLE  # noqa: E402
styles = list(QUALIFIER_STYLE.values())
want(len({(c, b) for c, b, _ in styles}) == len(styles),
     "qualifier (colour, border-style) pairs must be pairwise distinct")

# --- disputed is marked uncertain ------------------------------------------
disputed = card_segment(html, "ENT-9105")
want("uncertainty is the finding" in disputed,
     "disputed edge must carry the explicit uncertainty note")

# --- Low renders distinctly from Moderate ----------------------------------
low = card_segment(html, "ENT-9104")       # dated by CLM-9102 (Low, level 2)
moderate = card_segment(html, "ENT-9101")  # dated by CLM-9101 (Moderate, 3)
want("conf-weak" in low,
     "Low-confidence dating must carry the weak-grade (non-colour) marking")
want("conf-weak" not in moderate,
     "Moderate-confidence dating must NOT carry the weak-grade marking")
want('title="confidence level 2"' in low and 'title="confidence level 3"' in moderate,
     "level badges must carry their distinct levels (2 vs 3)")

# --- Reliance badge on every tradition node + standing banner --------------
badge_count = html.count('trad-reliance"')
want(badge_count == len(TRADITIONS),
     f"reliance badge count {badge_count} != tradition count {len(TRADITIONS)}")
for ident in TRADITIONS:
    want("trad-reliance" in card_segment(html, ident),
         f"{ident} is missing its reliance badge")
want("Findings not cleared for external reliance" in html,
     "standing reliance banner missing from the timeline view")

# --- Zurvanism / overturned-hypothesis note --------------------------------
want("Zurvanism" in html and "curated note — not field-derived" in html,
     "the Zurvanism overturned-hypothesis note must be present and flagged curated")
want("INV-0016" in html,
     "the curated note must cite INV-0016")

# --- Unresolvable dating_claims pointer is a reported graph error ----------
bad = dict(nodes[0])
bad["id"] = "ENT-9199"
bad["title"] = "Fixture Unresolvable Dating"
bad["dating_claims"] = ["CLM-9999"]
_, errors = timeline_entries(nodes + [bad])
want(any("CLM-9999" in e and "ENT-9199" in e for e in errors),
     "an unresolvable dating_claims pointer must be reported as a graph error")
_, clean_errors = timeline_entries(nodes)
want(clean_errors == [],
     f"clean fixture set must produce no graph errors, got {clean_errors}")

# --- Determinism -----------------------------------------------------------
want(html == build_timeline_html(nodes, "abc1234", GEN),
     "build_timeline_html is not deterministic across two runs")

# --- TREE-VIEW REGRESSION: tree emitter ignores the tradition fields -------
tree_with = build_html(nodes, "abc1234", GEN)
stripped = []
for n in nodes:
    m = dict(n)
    if m["type"] == "ENT":
        m["tradition_type"] = None
        m["dating_claims"] = []
        m["display_range"] = None
    stripped.append(m)
tree_without = build_html(stripped, "abc1234", GEN)
want(tree_with == tree_without,
     "tree view output must be byte-identical with/without tradition fields "
     "(the tree emitter must not read them)")
want("tl-card" not in tree_with and "tl-lane" not in tree_with,
     "tree view must contain no timeline markup")


print()
if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (verbatim-range/root/qualifiers/disputed/low-vs-moderate/"
      "reliance/banner/zurvanism/graph-error/determinism/tree-regression all proven)")
sys.exit(0)
