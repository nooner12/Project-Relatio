#!/usr/bin/env python3
"""Detection tests for the SVG timeline emitter of build_view.py (ADR-GOV-0009).

The timeline was upgraded from the Path-A block layout to a proportional SVG
tree-on-a-time-axis (STD-0002 §11 v1.11 render-only positioning bounds). House
convention: prove the positive. Deliberately-shaped fixtures are driven through
the real parse+render path (object_from_text -> build_timeline_html) and the
assertions target the emitted SVG/HTML:

  * a bar renders at its NUMERIC bounds (x + width derived from year_to_x, not
    from parsing display_range prose);
  * a `present` end extends to the axis end (living-tradition cap), an integer
    end stops at that year, and an OMITTED end renders a terminus-undated stub
    (never extended to present, never a fabricated coordinate);
  * high uncertainty renders visibly weaker than low (dashed + most-faded);
  * each of the six qualifier connectors renders distinctly (colour + dash +
    glyph), `disputed` is marked uncertain, and `continuation` (ADR-GOV-0010 D1)
    renders its distinct heavier main-line-carry-forward stroke;
  * a bounds-less tradition renders in the undated/sequence-only fallback lane
    with its verbatim display_range, and is NOT placed on the axis;
  * the reliance badge appears on EVERY tradition (count == tradition count,
    on-axis + undated) and the standing banner is present — the load-bearing gate;
  * display_range renders verbatim on every bar (authoritative string visible);
  * the axis-compression note is present (honest about non-linearity);
  * the Zurvanism / overturned-hypothesis curated note is present and flagged;
  * an unresolvable dating_claims pointer is reported as a graph error;
  * output is deterministic across two runs;
  * TREE-VIEW REGRESSION: build_html is byte-identical with/without the tradition
    and range fields, and contains no timeline/SVG markup.

Run: python tools/tests/test_timeline_view.py
"""

from datetime import date
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import read_text  # noqa: E402
from build_view import (  # noqa: E402
    object_from_text, build_html, build_timeline_html, timeline_entries,
    QUALIFIER_STYLE, _make_year_to_x, _num,
    TIMELINE_RENDER_CLASSES, TIMELINE_EDGE_TYPES,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"

failures = []


def want(cond, msg):
    if not cond:
        failures.append(msg)


def load(name):
    return object_from_text(read_text(FIXTURES / name))


# --- Parse the fixture mini-family ----------------------------------------
FIX = [
    "tl_root.md",            # ENT-9100 root, -2000..present, moderate
    "tl_branch_schism.md",   # ENT-9101 schism, 300..800, low
    "tl_branch_reform.md",   # ENT-9102 reform, 500..present, moderate
    "tl_branch_syncretic.md",  # ENT-9103 syncretic-descent, 700.., low (OPEN)
    "tl_branch_heterodox.md",  # ENT-9104 heterodox-offshoot, 900..950, high
    "tl_branch_disputed.md",   # ENT-9105 disputed, 1100..present, moderate
    "tl_branch_continuation.md",  # ENT-9107 continuation, 200..1000, moderate (ADR-GOV-0010 D1)
    "tl_undated.md",         # ENT-9106 undated (no bounds) -> fallback lane
    "tl_community.md",       # ENT-9108 COMMUNITY class -> must NOT render (D7)
    "tl_influence.md",       # ENT-9109 influence-only tradition -> renders as a ROOT
    "tl_claim_moderate.md",  # CLM-9101 (Moderate)
    "tl_claim_low.md",       # CLM-9102 (Low)
]
nodes = [load(n) for n in FIX]
if any(n is None for n in nodes):
    failures.append(f"a fixture failed to parse: "
                    f"{[FIX[i] for i, n in enumerate(nodes) if n is None]}")

GEN = date(2026, 7, 22)
PRESENT = GEN.year
html = build_timeline_html(nodes, "abc1234", GEN)

anchors, y2x, plot_w = _make_year_to_x(PRESENT)
PLOT_RIGHT = 214 + plot_w   # _GUTTER + plot_w


def svg_of(text):
    """The MAIN plot SVG (inside .svg-scroll) — not the tiny legend samples,
    which each also open an <svg>."""
    m = text.find('class="svg-scroll"')
    if m == -1:
        return ""
    i = text.find("<svg", m)
    j = text.find("</svg>", i)
    return text[i:j] if i != -1 and j != -1 else ""


svg = svg_of(html)


# --- A bar renders at its numeric bounds -----------------------------------
# ENT-9101 schism: 300..800, low (no fuzz) -> a single bar rect at those coords.
x1 = _num(y2x(300))
w = _num(max(y2x(800) - y2x(300), 3))
want(f'x="{x1}"' in svg, f"schism bar not positioned at year_to_x(300)={x1}")
want(f'width="{w}"' in svg, f"schism bar width not year_to_x(800)-year_to_x(300)={w}")

# --- present extends to axis end; integer ends stop; omitted = undated stub -
# Three present-ended traditions (root, reform, disputed) -> three living caps.
want(html.count("▶") == 3,
     f"expected 3 living-tradition caps (present ends), got {html.count('▶')}")
# The open-terminus (ENT-9103 syncretic, no end) renders a terminus-undated stub.
want(html.count("terminus undated") == 1,
     f"expected exactly one terminus-undated stub, got {html.count('terminus undated')}")
# and it is NOT extended to present: its stub is short, so no living cap for it.

# --- high uncertainty renders visibly weaker than low ----------------------
want('fill-opacity="0.3"' in svg,
     "high-uncertainty bar must render most-faded (fill-opacity 0.3)")
want('fill-opacity="0.82"' in svg,
     "low-uncertainty bar must render strong (fill-opacity 0.82)")
want('stroke-dasharray="5 3"' in svg,
     "high-uncertainty bar must render dashed (the visibly-weakest encoding)")

# --- each qualifier connector renders distinctly ---------------------------
for q, (color, dash, glyph) in QUALIFIER_STYLE.items():
    want(f'stroke="{color}"' in svg,
         f"qualifier {q} colour {color} missing from a connector")
    want(glyph in svg, f"qualifier {q} glyph {glyph!r} missing")
# (colour, dash) pairs must be pairwise distinct (never colour-only).
pairs = {(c, d) for c, d, _ in QUALIFIER_STYLE.values()}
want(len(pairs) == len(QUALIFIER_STYLE),
     "qualifier (colour, dash) pairs must be pairwise distinct")
# disputed is marked uncertain.
want("descent disputed — uncertainty is the finding" in svg,
     "disputed connector must carry the explicit uncertainty note")
# continuation (ADR-GOV-0010 D1) renders its distinct HEAVIER main-line stroke.
want('stroke-width="3.2"' in svg,
     "continuation connector must render its heavier (3.2) main-line-carry-forward stroke")

# --- undated fallback lane: verbatim, not on the axis ----------------------
want("undated-lane" in html, "undated/sequence-only fallback lane missing")
want("ENT-9106" in html, "undated tradition ENT-9106 missing from the fallback lane")
want("date genuinely unknown (fixture)" in html,
     "undated tradition's verbatim display_range missing")
want("ENT-9106" not in svg,
     "undated tradition must NOT be placed on the axis (no invented coordinates)")

# --- reliance badge on every tradition (on-axis + undated) + banner --------
# Count the badge marker token, which matches BOTH the on-axis SVG <g
# class="trad-reliance"> and the undated lane's class="reliance-badge
# trad-reliance" (the same token main()'s self-check counts).
badge_count = html.count('trad-reliance"')
n_traditions = sum(1 for n in nodes if n and n["type"] == "ENT"
                   and n.get("tradition_type")
                   and n.get("rendering_class") in TIMELINE_RENDER_CLASSES)
want(badge_count == n_traditions,
     f"reliance badge count {badge_count} != tradition count {n_traditions}")
want("Findings not cleared for external reliance" in html,
     "standing reliance banner missing from the timeline view")

# --- display_range verbatim on every bar -----------------------------------
for dr in ("2nd millennium BCE (fixture-contested)", "3rd c. CE", "5th c. CE",
           "7th c. CE", "9th c. CE", "12th c. CE crystallisation (fixture)"):
    want(dr in svg, f"verbatim display_range {dr!r} missing from the SVG")

# --- axis compression is documented ----------------------------------------
want("compress" in html.lower(),
     "the axis-compression note (honest non-linearity) must be present")

# --- Zurvanism / overturned-hypothesis curated note ------------------------
want("Zurvanism" in html and "curated note — not field-derived" in html,
     "the Zurvanism overturned-hypothesis note must be present and flagged curated")
want("INV-0016" in html, "the curated note must cite INV-0016")

# --- ADR-GOV-0012 D7: THE TWO DEFAULT-TIMELINE FILTERS, PROVEN TO FIRE ------
# House convention is prove-the-positive, and these two filters are the ones
# that keep the default view VISUALLY UNCHANGED by this enactment. A live run
# proves nothing (the community entities and influence edges would simply be
# absent), so each is fired against a fixture built to be excluded.

entries_all, _ = timeline_entries(nodes)
rendered = {e["node"]["id"] for e in entries_all}

# (1) A community-class node does NOT render — not on the axis, not in the
#     undated fallback lane, not in the tradition count, nowhere in the output.
want("ENT-9108" not in rendered,
     "FILTER 1 FAILED: the community-class entity reached timeline_entries")
want("ENT-9108" not in html,
     "FILTER 1 FAILED: the community-class entity appears in the timeline HTML")
want("ENT-9108" not in svg,
     "FILTER 1 FAILED: the community-class entity was placed on the axis")
want("attestation" not in html.lower(),
     "FILTER 1 FAILED: a community attestation window leaked into the timeline")
# ...and it is excluded for the right REASON: it is not the tradition class.
# Same node re-declared `tradition` (with bounds) would render, so the filter is
# keyed on rendering_class, not on some incidental property of the fixture.
community_node = next(n for n in nodes if n and n["id"] == "ENT-9108")
promoted = dict(community_node)
promoted.update(tradition_type="founded", rendering_class="tradition",
                dating_claims=["CLM-9101"], display_range="fixture")
entries_promoted, _ = timeline_entries(
    [n for n in nodes if n and n["id"] != "ENT-9108"] + [promoted])
want("ENT-9108" in {e["node"]["id"] for e in entries_promoted},
     "the community filter must key on rendering_class — the same node declared "
     "`tradition` must render, or the exclusion proves nothing")
want(TIMELINE_RENDER_CLASSES == ("tradition",),
     f"the default timeline must render the tradition class ONLY (D7); "
     f"got {TIMELINE_RENDER_CLASSES}")
print()
print("  D7 filter 1: community-class node does NOT render — and the same node "
      "declared `tradition` does")

# (2) An influenced_by edge does NOT render as a connector, and the node whose
#     ONLY edges are influence edges still renders as a ROOT (the Islam case).
influence_entry = next(e for e in entries_all if e["node"]["id"] == "ENT-9109")
want(influence_entry["branches"] == [],
     f"FILTER 2 FAILED: an influenced_by edge became a timeline connector: "
     f"{influence_entry['branches']}")
want("influenced_by" not in html,
     "FILTER 2 FAILED: `influenced_by` appears in the timeline HTML")
want(TIMELINE_EDGE_TYPES == ("branches_from",),
     f"the default timeline must draw DESCENT connectors only (D7); "
     f"got {TIMELINE_EDGE_TYPES}")
# The node itself DOES render — the finding is "no descent," not "no node".
want("ENT-9109" in rendered and "ENT-9109" in svg,
     "the influence-only tradition must still render, as a ROOT — an "
     "unconnected node is an honest rendering of 'no descent'")
# And it is a root: no connector terminates on it. Every connector in the SVG is
# titled `branches_from (<qualifier>)`, and none of the fixture's branch edges
# targets ENT-9109, so its start node carries no inbound line.
want(all(t != "ENT-9109" for e in entries_all for t, _ in e["branches"]),
     "nothing may branch from the influence-only node in this fixture set")
print("  D7 filter 2: influenced_by does NOT render — and the influence-only "
      "node still renders as a ROOT")
print()

# --- unresolvable dating_claims pointer is a reported graph error -----------
bad = dict(nodes[0])
bad["id"] = "ENT-9199"
bad["title"] = "Unresolvable"
bad["dating_claims"] = ["CLM-9999"]
_, errors = timeline_entries(nodes + [bad])
want(any("CLM-9999" in e and "ENT-9199" in e for e in errors),
     "an unresolvable dating_claims pointer must be reported as a graph error")
_, clean = timeline_entries(nodes)
want(clean == [], f"clean fixture set must produce no graph errors, got {clean}")

# --- Determinism -----------------------------------------------------------
want(html == build_timeline_html(nodes, "abc1234", GEN),
     "build_timeline_html is not deterministic across two runs")

# --- TREE-VIEW REGRESSION: tree emitter ignores tradition + range fields ----
tree_with = build_html(nodes, "abc1234", GEN)
stripped = []
for n in nodes:
    m = dict(n)
    if m["type"] == "ENT":
        m["tradition_type"] = None
        m["dating_claims"] = []
        m["display_range"] = None
        m["range_start_year"] = None
        m["range_end_year"] = None
        m["range_uncertainty"] = None
        m["rendering_class"] = None
    stripped.append(m)
tree_without = build_html(stripped, "abc1234", GEN)
want(tree_with == tree_without,
     "tree view output must be byte-identical with/without tradition+range fields")
want("<svg" not in tree_with and "tl-lane" not in tree_with
     and "svg-scroll" not in tree_with,
     "tree view must contain no timeline/SVG markup")


print()
if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (numeric-bounds/present-extends/open-terminus/high-vs-low/"
      "qualifiers/disputed/undated-fallback/reliance/banner/verbatim/compression/"
      "zurvanism/graph-error/determinism/tree-regression all proven)")
sys.exit(0)
