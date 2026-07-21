#!/usr/bin/env python3
"""Detection tests for build_view.py (the vault visualizer).

House convention: prove the positive. An expected-clean run against the live
vault cannot distinguish a working generator from a blind one, so this drives
deliberately-shaped fixtures through the real parse+render path and asserts on
the emitted HTML:

  * a split-confidence record renders ALL its components, separately, never
    merged or averaged;
  * a single-component record renders exactly one;
  * a record with a cross-edge renders it as a chip;
  * a past-due review_date gets the node-level due marker, and a future one
    does NOT;
  * the reliance badge appears on EVERY CLM/FND node (count == record count) —
    the load-bearing gate that no view path may strip;
  * the standing reliance banner is present;
  * the frontmatter version is rendered as literal text (1.10 stays 1.10, not
    the float 1.1);
  * output is deterministic across two runs (fixed hash/date);
  * §8 compliance: the live vault's deepest-path KB record is read and rendered
    (proves the extended-length read path includes long-path files).

Run: python tools/tests/test_build_view.py
"""

from datetime import date
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import (  # noqa: E402
    read_text, markdown_files, extract_identifier, find_vault_root,
)
from build_view import (  # noqa: E402
    object_from_text, build_html, collect_objects,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"

failures = []


def load(name):
    return object_from_text(read_text(FIXTURES / name))


# --- Parse the fixture mini-tree ------------------------------------------
nodes = [
    load("view_inv_root.md"),
    load("view_single_confidence.md"),
    load("view_split_confidence.md"),
    load("view_finding.md"),
    load("view_source.md"),
]
if any(n is None for n in nodes):
    failures.append(f"a fixture failed to parse to a KB node: "
                    f"{[i for i, n in enumerate(nodes) if n is None]}")

GEN = date(2026, 7, 21)
html = build_html(nodes, "abc1234", GEN)


def want(cond, msg):
    if not cond:
        failures.append(msg)


def card_segment(html_text, ident):
    """The HTML slice for one card id (up to the next card/details or end)."""
    i = html_text.find(f'id="{ident}"')
    if i == -1:
        return ""
    nxt = html_text.find('class="card ', i + 1)
    end = nxt if nxt != -1 else len(html_text)
    return html_text[i:end]


# --- Split vs single confidence -------------------------------------------
split = card_segment(html, "CLM-9002")
split_rows = split.count('class="conf-row"')
want(split_rows == 3,
     f"split-confidence CLM-9002 should render 3 components, got {split_rows}")
# The three distinct component names must all survive (not merged/averaged).
for comp in ("strand_a", "strand_b", "strand_c"):
    want(comp in split, f"split component {comp!r} missing from CLM-9002 render")
# No averaging: a level-3 (Moderate) and level-4 (High) badge must both appear;
# an averaged '3' single row would be one conf-row, already caught above.

single = card_segment(html, "CLM-9001")
single_rows = single.count('class="conf-row"')
want(single_rows == 1,
     f"single-confidence CLM-9001 should render 1 component, got {single_rows}")

# --- Cross-edge chip -------------------------------------------------------
want('contrasts_with → CLM-9002' in single,
     "cross-edge chip (contrasts_with → CLM-9002) missing from CLM-9001")
# derived_from chip present too
want('derived_from → SRC-9001' in single,
     "derived_from chip (→ SRC-9001) missing from CLM-9001")

# --- Past-due marker -------------------------------------------------------
want('title="review_date is in the past"' in split,
     "past-due CLM-9002 should carry the node-level due marker")
want('title="review_date is in the past"' not in single,
     "future-dated CLM-9001 must NOT carry the due marker")

# --- Reliance badge on every CLM/FND (count == record count) ---------------
leaf_ids = [n["id"] for n in nodes if n["type"] in ("CLM", "FND")]
badge_count = html.count('reliance-badge head-reliance"')
want(badge_count == len(leaf_ids),
     f"reliance badge count {badge_count} != CLM/FND count {len(leaf_ids)}")
for lid in leaf_ids:
    seg = card_segment(html, lid)
    want('head-reliance' in seg, f"{lid} is missing its reliance badge")
# The tier surfaces its meaning and its promotion detail. CLM-9001 is R1
# (already retrieval-verified), so its promotion path is the independent channel.
want("Retrieval-verified" in single,
     "R1 node should state its meaning (retrieval-verified)")
want("independent verification channel" in single,
     "R1 node should state its promotion path (independent channel)")

# --- Standing banner -------------------------------------------------------
want("Findings not cleared for external reliance" in html,
     "standing reliance banner missing")

# --- Version as literal text (not float) -----------------------------------
want("v1.10" in single,
     "version 1.10 must render literally, not as the float 1.1")
want("v1.1<" not in single and ">v1.1 " not in single,
     "version rendered as 1.1 — the yaml float trap regressed")

# --- Determinism -----------------------------------------------------------
html2 = build_html(nodes, "abc1234", GEN)
want(html == html2, "build_html is not deterministic across two runs")

# --- §8 compliance: deepest-path live record is read and rendered ----------
try:
    vault = find_vault_root(Path(__file__).resolve().parent.parent)
    kb_files = [f for f in markdown_files(vault)
                if extract_identifier(f.stem)
                and extract_identifier(f.stem).split("-")[0]
                in ("INV", "CLM", "SRC", "ENT", "FND")]
    if kb_files:
        deepest = max(kb_files, key=lambda p: len(str(p.resolve())))
        deep_id = extract_identifier(deepest.stem)
        live = collect_objects(vault)
        live_html = build_html(live, "live0000", GEN)
        want(f'id="{deep_id}"' in live_html,
             f"deepest-path record {deep_id} not rendered — long-path read failed "
             f"(path len {len(str(deepest.resolve()))})")
        print(f"  §8 deepest-path record: {deep_id} "
              f"(abs path {len(str(deepest.resolve()))} chars) — rendered")
    else:
        failures.append("no KB files found for the §8 deepest-path check")
except Exception as ex:  # pragma: no cover - environment guard
    failures.append(f"§8 deepest-path live check raised: {ex}")


print()
if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (split/single/cross-edge/past-due/reliance/banner/"
      "version/determinism/§8 all proven)")
sys.exit(0)
