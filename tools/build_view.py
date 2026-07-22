#!/usr/bin/env python3
"""
build_view.py — the Relatio vault visualizer (regenerating snapshot).

READ-ONLY. FRONTMATTER-ONLY. Reads the YAML frontmatter of every Knowledge Base
object (INV/CLM/SRC/ENT/FND) and emits TWO self-contained interactive HTML files
— no external network dependencies, no build step, both render from a
double-click. It NEVER parses body prose for data, NEVER writes to any record,
and adds NO new fields. Where a datum is absent from frontmatter the node says
so honestly ("not fielded"); it is never inferred from prose.

The two outputs share ONE parse (collect_objects / object_from_text) and have
separate emitters:

  * `views/relatio-view.html` — the whole-vault tree view (build_html).
  * `views/relatio-timeline.html` — the world-religions timeline view
    (build_timeline_html; ADR-GOV-0009). PATH A layout — honesty over false
    precision: `display_range` strings render AS-AUTHORED (verbatim), never
    parsed into numeric years; ordering is a best-effort coarse era reading
    used for SEQUENCE ONLY (root-first lineage layout, no pixel-proportional
    time axis — a proportional axis is a named future refinement requiring
    structured date fields and must not be approximated). Each tradition shows
    its `tradition_type`, its dating claims' confidence (components separate,
    visually weighted by level), and its reliance badge; `branches_from` edges
    render distinctly by qualifier (`disputed` explicitly marked uncertain);
    the Zurvanism overturned-hypothesis note renders as presence (curated,
    flagged as such — the outcome lives in prose, not frontmatter).

What is READ (frontmatter only):
  title, document_type, version (literal text, not yaml -- the 1.10-as-float
  trap), status, operational_status, the typed `relationships:` block
  (part_of / derived_from spine, plus contrasts_with / depends_on / supports /
  related_to cross-edges), parent_documents, and for CLM/FND the epistemic axis
  (`confidence` list, `reliance_tier`, `reliance_note`) and the review axis
  (`review_cycle`, `review_date`, `last_reviewed`). SRC also: source_author,
  publication_date.

The tree (spine): INV roots -> the CLM/FND/SRC that are `part_of` them ->
each claim/finding's `derived_from` targets rendered as reference chips. Every
object is a canonical node exactly once (so node count == KB object count);
derivation and cross-edges are chips/badges pointing at those canonical nodes,
never duplicate full nodes. Entities (KB-shared, no `part_of` INV) and any
object with no INV home render in a "Shared & Cross-Investigation" group.

Closure state is NOT prose-parsed. An investigation's closed/open state lives in
its banner + history row (prose), not in frontmatter -- and closed INVs keep
`status: Draft` deliberately. So INV nodes are labelled by their honest
frontmatter `status` / `operational_status`, and this limitation is documented
in tools/README.md. No closure inference is attempted.

The reliance gate is visually load-bearing (non-negotiable): a standing banner,
an R0/R1/R2 badge on EVERY claim/finding node, and each badge's detail carries
the `reliance_note` plus what promotion would require. No code path hides it.

Extended-length path handling per STD-0001 §8 (inherited from common.read_text).

Usage:
    python build_view.py            # regenerate views/relatio-view.html
    (importable: object_from_text / build_html are the pure core, exercised by
     tools/tests/test_build_view.py)
"""

from datetime import date
from pathlib import Path
import html
import subprocess
import sys

import yaml

from common import (
    find_vault_root, markdown_files, parse_frontmatter, read_text, write_text,
    extract_identifier, FRONTMATTER_VERSION_RE, _parse_date,
    EPISTEMIC_LEVEL_LABELS, relationship_entries,
)

KB_TYPES = ("INV", "CLM", "SRC", "ENT", "FND")
LEAF_TYPES = ("CLM", "FND")  # the graded, reliance-bearing records
SPINE_TYPES = ("part_of", "derived_from")

TYPE_LABEL = {
    "INV": "Investigation",
    "CLM": "Claim",
    "FND": "Finding",
    "SRC": "Source",
    "ENT": "Entity",
}

# Confidence level -> accessible colour (Okabe-Ito derived; distinct in the two
# common colour-vision deficiencies). Kept well away from the reliance palette so
# the two axes are never confused (STD-0008 §4 independence, rendered literally).
LEVEL_COLOR = {
    5: "#0b6e4f",  # Very High — deep green
    4: "#3d8f4e",  # High       — green
    3: "#b8860b",  # Moderate   — amber
    2: "#c65a11",  # Low        — orange
    1: "#a4243b",  # Very Low   — red
}

# Reliance tiers use a deliberately non-confidence palette (blue-greys), so a
# reliance badge is never mistaken for a confidence badge.
RELIANCE_COLOR = {
    "R0": "#5a6b8c",
    "R1": "#3a5a99",
    "R2": "#1f3a6e",
}
RELIANCE_MEANING = {
    "R0": "Parametric only — not externally verified.",
    "R1": "Retrieval-verified under edition-discipline (ADR-GOV-0006).",
    "R2": "Independently verified via a second channel.",
}
# What promotion would require, per tier (ADR-GOV-0006).
RELIANCE_PROMOTION = {
    "R0": "To promote: R1 requires retrieval verification (ADR-GOV-0006); "
          "R2 requires an independent verification channel.",
    "R1": "To promote: R2 requires an independent verification channel.",
    "R2": "Independently verified — top reliance tier.",
}


# ---------------------------------------------------------------------------
# Parsing — frontmatter only
# ---------------------------------------------------------------------------

def _short_title(ident, title):
    """The title with a leading 'IDENT - ' / 'IDENT — ' stripped, or the title."""
    if not isinstance(title, str):
        return ""
    t = title.strip()
    if ident and t.startswith(ident):
        rest = t[len(ident):].lstrip()
        for sep in ("-", "—", ":"):
            if rest.startswith(sep):
                return rest[len(sep):].strip()
        return rest
    return t


def _typed_relationships(meta):
    """List of (type, target_identifier) from the typed relationships block."""
    out = []
    for r in (meta.get("relationships") or []):
        if isinstance(r, dict) and r.get("type") and r.get("target"):
            rtype = str(r["type"]).strip()
            target = extract_identifier(str(r["target"]).strip()) \
                or str(r["target"]).strip()
            out.append((rtype, target))
    return out


def _rel_qualifiers(meta):
    """Map (type, target_identifier) -> qualifier for entries that carry one.

    Only branches_from entries carry a qualifier (STD-0004 §7.2). Keyed the same
    way _typed_relationships resolves targets so the view can look a qualifier up
    when rendering the cross-edge chip.
    """
    out = {}
    for e in relationship_entries(meta):
        if e["qualifier"] is not None:
            target = extract_identifier(e["target"]) or e["target"]
            out[(e["type"], target)] = e["qualifier"]
    return out


def _id_list(meta, field):
    """A frontmatter list field reduced to leading identifiers (drops non-ids)."""
    out = []
    for p in (meta.get(field) or []):
        ident = extract_identifier(str(p).strip())
        if ident:
            out.append(ident)
    return out


def _date_str(value):
    """A YYYY-MM-DD string for a date-ish frontmatter value, or None."""
    t = _parse_date(value)
    if t is None:
        return None
    return f"{t[0]:04d}-{t[1]:02d}-{t[2]:02d}"


def _confidence(meta):
    """The confidence list as [{component, level, label}], preserving order.

    Split components are kept SEPARATE — never merged, never averaged
    (STD-0008). A malformed component is passed through with what it has so the
    view can render it honestly rather than dropping it.
    """
    out = []
    for comp in (meta.get("confidence") or []):
        if isinstance(comp, dict):
            level = comp.get("level")
            label = comp.get("label")
            # Honest label: prefer the recorded one; if absent but the level is a
            # clean 1-5, fall back to the canonical label; else mark not-fielded.
            if not isinstance(label, str):
                if isinstance(level, int) and not isinstance(level, bool) \
                        and level in EPISTEMIC_LEVEL_LABELS:
                    label = EPISTEMIC_LEVEL_LABELS[level]
                else:
                    label = None
            out.append({
                "component": str(comp.get("component", "?")),
                "level": level if isinstance(level, int)
                and not isinstance(level, bool) else None,
                "label": label,
            })
    return out


def object_from_text(text):
    """Parse one KB object's frontmatter into a node dict, or None.

    Pure and fixture-testable: given a document's full text, returns None if the
    frontmatter carries no leading KB identifier, else a dict of exactly the
    frontmatter-derived fields the view renders. No body prose is read.
    """
    fm, _ = parse_frontmatter(text)
    if fm is None:
        return None
    try:
        meta = yaml.safe_load(fm)
    except Exception:
        return None
    if not isinstance(meta, dict):
        return None

    title = meta.get("title")
    ident = extract_identifier(title if isinstance(title, str) else "")
    if ident is None:
        return None
    prefix = ident.split("-")[0]
    if prefix not in KB_TYPES:
        return None

    # Version read as literal text, never yaml (unquoted `1.10` is the float 1.1).
    vmatch = FRONTMATTER_VERSION_RE.search(fm)
    version = vmatch.group(1).strip().strip("'\"") if vmatch else None

    return {
        "id": ident,
        "type": prefix,
        "type_label": TYPE_LABEL.get(prefix, prefix),
        "doc_type": meta.get("document_type"),
        "title": _short_title(ident, title),
        "version": version,
        "status": meta.get("status"),
        "operational_status": meta.get("operational_status"),
        "relationships": _typed_relationships(meta),
        "rel_qualifiers": _rel_qualifiers(meta),
        "parents": _id_list(meta, "parent_documents"),
        "related": _id_list(meta, "related_documents"),
        "confidence": _confidence(meta) if prefix in LEAF_TYPES else [],
        "reliance_tier": meta.get("reliance_tier") if prefix in LEAF_TYPES else None,
        "reliance_note": meta.get("reliance_note") if prefix in LEAF_TYPES else None,
        "review_cycle": meta.get("review_cycle") if prefix in LEAF_TYPES else None,
        "review_date": _date_str(meta.get("review_date")) if prefix in LEAF_TYPES else None,
        "last_reviewed": _date_str(meta.get("last_reviewed")) if prefix in LEAF_TYPES else None,
        "source_author": meta.get("source_author") if prefix == "SRC" else None,
        "publication_date": meta.get("publication_date") if prefix == "SRC" else None,
        # Tradition-class entity fields (ADR-GOV-0009 / STD-0002 §11 v1.10).
        # Read here so BOTH emitters share one parse; the tree emitter does not
        # render them (its output is unchanged by their presence — regression-
        # asserted in tests). display_range is verbatim text, render-only.
        "tradition_type": meta.get("tradition_type") if prefix == "ENT" else None,
        "dating_claims": _id_list(meta, "dating_claims") if prefix == "ENT" else [],
        "display_range": meta.get("display_range") if prefix == "ENT" else None,
    }


def collect_objects(vault):
    """All KB objects (INV/CLM/SRC/ENT/FND) as node dicts, sorted by identifier.

    Enumeration walks the whole vault via markdown_files (rglob) and keeps only
    objects whose title-embedded identifier is a KB type; every file is READ
    through common.read_text, i.e. with the STD-0001 §8 extended-length prefix.
    """
    objects = {}
    for f in markdown_files(vault):
        # Cheap pre-filter on the filename, but membership is decided by the
        # parsed title identifier inside object_from_text (the authoritative id).
        if extract_identifier(f.stem) is None:
            continue
        node = object_from_text(read_text(f))
        if node is None:
            continue
        objects[node["id"]] = node
    return [objects[k] for k in sorted(objects)]


# ---------------------------------------------------------------------------
# Tree assembly
# ---------------------------------------------------------------------------

def inv_of(node):
    """The INV identifier this object belongs to, or None.

    Frontmatter-only, deterministic, and honest about ambiguity:
      1. a `part_of` typed relationship pointing at an INV (authoritative);
      2. else the first parent_documents identifier that is an INV;
      3. else, for a SOURCE only, the sole INV appearing across its typed
         relationships + related_documents — used only when EXACTLY one distinct
         INV is referenced (no cross-investigation ambiguity). Entities are the
         deliberately KB-shared type and are never auto-placed this way; they
         stay in the Shared group by design.
    Returns None when no single INV home is derivable (Shared group).
    """
    for rtype, target in node["relationships"]:
        if rtype == "part_of" and target.startswith("INV-"):
            return target
    for p in node["parents"]:
        if p.startswith("INV-"):
            return p
    if node["type"] == "SRC":
        invs = {t for _, t in node["relationships"] if t.startswith("INV-")}
        invs |= {r for r in node["related"] if r.startswith("INV-")}
        if len(invs) == 1:
            return next(iter(invs))
    return None


def derived_targets(node):
    """The `derived_from` targets (spine children) of a node, in id order."""
    out = [t for rt, t in node["relationships"] if rt == "derived_from"]
    return sorted(set(out))


def cross_edges(node):
    """Non-spine typed edges as (type, target), sorted. These become badges.

    Everything typed that is not part of the tree spine (part_of / derived_from):
    contrasts_with, depends_on, supports, related_to, explains, extends, ...
    """
    out = [(rt, t) for rt, t in node["relationships"] if rt not in SPINE_TYPES]
    return sorted(set(out))


def build_tree(objects):
    """Group objects under their INV; return (inv_groups, shared).

    inv_groups: list of {inv, findings, claims, sources} in INV-id order.
    shared: objects with no INV home (entities, orphan sources), id-sorted.
    Every object appears exactly once across the whole structure.
    """
    by_id = {o["id"]: o for o in objects}
    invs = sorted((o for o in objects if o["type"] == "INV"),
                  key=lambda o: o["id"])

    members = {inv["id"]: {"FND": [], "CLM": [], "SRC": []} for inv in invs}
    shared = []

    for o in objects:
        if o["type"] == "INV":
            continue
        home = inv_of(o)
        if home in members and o["type"] in members[home]:
            members[home][o["type"]].append(o)
        else:
            shared.append(o)

    inv_groups = []
    for inv in invs:
        m = members[inv["id"]]
        inv_groups.append({
            "inv": inv,
            "findings": sorted(m["FND"], key=lambda o: o["id"]),
            "claims": sorted(m["CLM"], key=lambda o: o["id"]),
            "sources": sorted(m["SRC"], key=lambda o: o["id"]),
        })

    return by_id, inv_groups, sorted(shared, key=lambda o: o["id"])


# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------

def esc(value):
    return html.escape("" if value is None else str(value))


def _chip(target_id, by_id, kind):
    """A reference chip pointing at another object's canonical node.

    For CLM/FND targets the chip carries a reliance mini-badge so the reliance
    gate is present even on references (no view path strips it). `kind` labels
    the relation ('derived_from', or a cross-edge type).
    """
    tgt = by_id.get(target_id)
    label = target_id
    title = ""
    mini = ""
    if tgt is not None:
        title = tgt["title"]
        if tgt["type"] in LEAF_TYPES:
            tier = tgt["reliance_tier"] or "?"
            color = RELIANCE_COLOR.get(tier, "#888")
            mini = (f'<span class="mini-reliance" style="background:{color}" '
                    f'title="reliance tier {esc(tier)}">{esc(tier)}</span>')
    dangling = " chip-dangling" if tgt is None else ""
    return (f'<a class="chip{dangling}" href="#{esc(target_id)}" '
            f'data-kind="{esc(kind)}" title="{esc(kind)}: {esc(target_id)} '
            f'{esc(title)}">{esc(kind)} → {esc(target_id)}{mini}</a>')


def _confidence_block(node):
    """Every confidence component as its own level badge + name + label."""
    if not node["confidence"]:
        return '<div class="notfielded">confidence not fielded</div>'
    rows = []
    for comp in node["confidence"]:
        level = comp["level"]
        label = comp["label"]
        if level is None:
            badge = '<span class="level-badge level-na" title="level not fielded">?</span>'
            lbl = '<span class="notfielded">level not fielded</span>'
        else:
            color = LEVEL_COLOR.get(level, "#888")
            badge = (f'<span class="level-badge" style="background:{color}" '
                     f'title="confidence level {level}">{level}</span>')
            lbl = esc(label if label else EPISTEMIC_LEVEL_LABELS.get(level, "?"))
        rows.append(
            f'<div class="conf-row">{badge}'
            f'<span class="conf-name">{esc(comp["component"])}</span>'
            f'<span class="conf-label">{lbl}</span></div>'
        )
    return '<div class="conf-block">' + "".join(rows) + "</div>"


def _reliance_block(node):
    """The load-bearing reliance badge + note + promotion detail. Never omitted
    for a CLM/FND, even when the tier itself is unfielded (shown honestly)."""
    tier = node["reliance_tier"]
    if tier not in RELIANCE_COLOR:
        return ('<div class="reliance-block reliance-na">'
                '<span class="reliance-badge reliance-unf">reliance not fielded</span>'
                '</div>')
    color = RELIANCE_COLOR[tier]
    note = node["reliance_note"]
    note_html = (f'<div class="reliance-note">{esc(note)}</div>'
                 if note else '<div class="reliance-note reliance-note-empty">'
                 '(no reliance_note fielded)</div>')
    return (
        f'<div class="reliance-block">'
        f'<span class="reliance-badge" style="background:{color}" '
        f'title="{esc(RELIANCE_MEANING.get(tier, ""))}">{esc(tier)}</span>'
        f'<span class="reliance-meaning">{esc(RELIANCE_MEANING.get(tier, ""))}</span>'
        f'{note_html}'
        f'<div class="reliance-promotion">{esc(RELIANCE_PROMOTION.get(tier, ""))}</div>'
        f'</div>'
    )


def _review_block(node, gen_date):
    """Review cadence line; flags a past-due review_date visually."""
    cyc = node["review_cycle"]
    rd = node["review_date"]
    lr = node["last_reviewed"]
    if rd is None and cyc is None and lr is None:
        return '<div class="notfielded">review fields not fielded</div>'
    overdue = ""
    rd_tuple = _parse_date(rd)
    if rd_tuple is not None and tuple(rd_tuple) < (gen_date.year, gen_date.month, gen_date.day):
        overdue = ' <span class="pastdue" title="review_date is in the past">⚠ PAST DUE</span>'
    return (
        f'<div class="review-line">'
        f'<span class="review-item">cycle: {esc(cyc)} mo</span>'
        f'<span class="review-item">last reviewed: {esc(lr)}</span>'
        f'<span class="review-item">review due: {esc(rd)}{overdue}</span>'
        f'</div>'
    )


def _cross_edge_badges(node, by_id):
    edges = cross_edges(node)
    if not edges:
        return ""
    quals = node.get("rel_qualifiers", {})
    chips = []
    for rt, t in edges:
        # branches_from renders with its qualifier (STD-0004 §7.2) so the KIND of
        # branching is visible on the chip, e.g. "branches_from (schism) →".
        q = quals.get((rt, t))
        kind = f"{rt} ({q})" if (rt == "branches_from" and q) else rt
        chips.append(_chip(t, by_id, kind))
    return (f'<div class="cross-edges"><span class="cross-label">links:</span>'
            f'{"".join(chips)}</div>')


def _derived_chips(node, by_id):
    targets = derived_targets(node)
    if not targets:
        return ""
    chips = "".join(_chip(t, by_id, "derived_from") for t in targets)
    return f'<div class="derived"><span class="derived-label">derived from:</span>{chips}</div>'


def _leaf_card(node, by_id, gen_date):
    """A CLM/FND card — carries the reliance badge unconditionally."""
    search = esc((node["id"] + " " + node["title"]).lower())
    tier = node["reliance_tier"] or "unf"
    color = RELIANCE_COLOR.get(node["reliance_tier"], "#888")
    return (
        f'<div class="card card-{node["type"].lower()}" id="{esc(node["id"])}" '
        f'data-search="{search}" data-type="{node["type"]}">'
        f'<div class="card-head">'
        f'<span class="id-badge">{esc(node["id"])}</span>'
        f'<span class="type-badge type-{node["type"].lower()}">{esc(node["type_label"])}</span>'
        f'<span class="card-title">{esc(node["title"])}</span>'
        f'<span class="reliance-badge head-reliance" style="background:{color}" '
        f'title="reliance tier {esc(tier)}">{esc(node["reliance_tier"] or "R?")}</span>'
        f'<span class="version">v{esc(node["version"])}</span>'
        f'</div>'
        f'<div class="card-body">'
        f'{_confidence_block(node)}'
        f'{_reliance_block(node)}'
        f'{_review_block(node, gen_date)}'
        f'{_derived_chips(node, by_id)}'
        f'{_cross_edge_badges(node, by_id)}'
        f'</div></div>'
    )


def _plain_card(node, by_id, gen_date):
    """A SRC/ENT card (no epistemic/review/reliance axis on these types)."""
    search = esc((node["id"] + " " + node["title"]).lower())
    extra = ""
    if node["type"] == "SRC":
        bits = []
        if node["source_author"]:
            bits.append(f'<span class="src-meta">author: {esc(node["source_author"])}</span>')
        if node["publication_date"]:
            bits.append(f'<span class="src-meta">published: {esc(node["publication_date"])}</span>')
        if bits:
            extra = '<div class="src-meta-row">' + "".join(bits) + "</div>"
    return (
        f'<div class="card card-{node["type"].lower()}" id="{esc(node["id"])}" '
        f'data-search="{search}" data-type="{node["type"]}">'
        f'<div class="card-head">'
        f'<span class="id-badge">{esc(node["id"])}</span>'
        f'<span class="type-badge type-{node["type"].lower()}">{esc(node["type_label"])}</span>'
        f'<span class="card-title">{esc(node["title"])}</span>'
        f'<span class="version">v{esc(node["version"])}</span>'
        f'</div>'
        f'<div class="card-body">'
        f'{extra}'
        f'{_derived_chips(node, by_id)}'
        f'{_cross_edge_badges(node, by_id)}'
        f'</div></div>'
    )


def _subsection(title, nodes, render_fn, by_id, gen_date):
    if not nodes:
        return ""
    cards = "".join(render_fn(n, by_id, gen_date) for n in nodes)
    return (f'<div class="subsection"><h3 class="sub-title">{esc(title)} '
            f'<span class="count">({len(nodes)})</span></h3>{cards}</div>')


def _inv_group(group, by_id, gen_date):
    inv = group["inv"]
    n_f, n_c, n_s = len(group["findings"]), len(group["claims"]), len(group["sources"])
    status = esc(inv["status"])
    op = esc(inv["operational_status"])
    summary = (
        f'<summary class="inv-summary" data-search="'
        f'{esc((inv["id"] + " " + inv["title"]).lower())}">'
        f'<span class="id-badge inv-id">{esc(inv["id"])}</span>'
        f'<span class="inv-title">{esc(inv["title"])}</span>'
        f'<span class="status-chip">status: {status}</span>'
        f'<span class="status-chip">op: {op}</span>'
        f'<span class="version">v{esc(inv["version"])}</span>'
        f'<span class="inv-counts">{n_f} FND · {n_c} CLM · {n_s} SRC</span>'
        f'</summary>'
    )
    body = (
        _subsection("Findings", group["findings"], _leaf_card, by_id, gen_date)
        + _subsection("Claims", group["claims"], _leaf_card, by_id, gen_date)
        + _subsection("Sources", group["sources"], _plain_card, by_id, gen_date)
    )
    return f'<details class="inv-group" id="{esc(inv["id"])}">{summary}<div class="inv-body">{body}</div></details>'


CSS = """
:root{
  --bg:#f7f7f5; --fg:#1e1e1c; --muted:#6b6b66; --line:#e0e0da; --card:#ffffff;
  --banner:#7a1f2b; --banner-fg:#fff; --accent:#2b3a67;
}
*{box-sizing:border-box}
body{margin:0;font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  background:var(--bg);color:var(--fg)}
.reliance-banner{position:sticky;top:0;z-index:50;background:var(--banner);color:var(--banner-fg);
  padding:10px 18px;font-weight:600;font-size:14px;box-shadow:0 1px 4px rgba(0,0,0,.2)}
.reliance-banner small{display:block;font-weight:400;opacity:.92;margin-top:2px}
.wrap{max-width:1100px;margin:0 auto;padding:18px}
header.gen{display:flex;flex-wrap:wrap;gap:10px 20px;align-items:baseline;
  border-bottom:1px solid var(--line);padding-bottom:12px;margin-bottom:14px}
header.gen h1{font-size:20px;margin:0}
.genmeta{color:var(--muted);font-size:12.5px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.legend{display:flex;flex-wrap:wrap;gap:14px;background:var(--card);border:1px solid var(--line);
  border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:12.5px}
.legend .grp{display:flex;gap:6px;align-items:center}
.legend .swatch{width:16px;height:16px;border-radius:4px;display:inline-block}
.searchbar{margin-bottom:16px}
.searchbar input{width:100%;padding:9px 12px;border:1px solid var(--line);border-radius:8px;font-size:14px}
.inv-group{background:var(--card);border:1px solid var(--line);border-radius:8px;margin-bottom:10px;overflow:hidden}
.inv-summary{cursor:pointer;padding:12px 14px;display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center;
  list-style:none;user-select:none}
.inv-summary::-webkit-details-marker{display:none}
.inv-summary:hover{background:#fafaf8}
.inv-title{font-weight:600}
.inv-counts{color:var(--muted);font-size:12px;margin-left:auto}
.inv-body{padding:4px 14px 14px;border-top:1px solid var(--line)}
.subsection{margin-top:12px}
.sub-title{font-size:13px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin:14px 0 6px}
.count{color:var(--muted)}
.card{border:1px solid var(--line);border-radius:7px;margin:7px 0;background:#fff}
.card-head{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:8px 10px;border-bottom:1px solid var(--line)}
.card-body{padding:8px 10px;font-size:13.5px}
.id-badge{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-weight:700;font-size:12.5px}
.inv-id{font-size:13.5px}
.type-badge{font-size:11px;padding:1px 7px;border-radius:10px;border:1px solid var(--line);color:var(--muted)}
.type-clm{background:#eef3ff}.type-fnd{background:#eafaf0}.type-src{background:#fbf3e6}.type-ent{background:#f3eefb}
.card-title{flex:1;min-width:180px}
.version{color:var(--muted);font-size:12px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.status-chip{font-size:11.5px;color:var(--muted);background:#f0f0ec;border-radius:10px;padding:1px 8px}
.level-badge{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:5px;
  color:#fff;font-weight:700;font-size:12px;flex:none}
.level-na{background:#999}
.conf-block{display:flex;flex-direction:column;gap:3px;margin-bottom:8px}
.conf-row{display:flex;gap:8px;align-items:center}
.conf-name{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px}
.conf-label{color:var(--muted);font-size:12.5px}
.reliance-block{border-left:3px solid var(--accent);padding:5px 0 5px 10px;margin:6px 0}
.reliance-badge{display:inline-block;color:#fff;font-weight:700;font-size:12px;padding:2px 9px;border-radius:5px}
.head-reliance{margin-left:auto}
.reliance-unf{background:#999}
.reliance-meaning{margin-left:8px;font-size:12.5px;color:var(--fg)}
.reliance-note{font-size:12.5px;color:var(--muted);margin-top:3px;font-style:italic}
.reliance-note-empty{opacity:.7}
.reliance-promotion{font-size:12px;color:var(--accent);margin-top:3px}
.review-line{display:flex;flex-wrap:wrap;gap:6px 14px;margin:6px 0;font-size:12.5px;color:var(--muted)}
.pastdue{color:#a4243b;font-weight:700}
.mini-reliance{display:inline-block;color:#fff;font-size:10px;font-weight:700;padding:0 4px;border-radius:3px;margin-left:4px}
.derived,.cross-edges{margin-top:6px;display:flex;flex-wrap:wrap;gap:5px;align-items:center}
.derived-label,.cross-label{font-size:11.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
.chip{display:inline-flex;align-items:center;font-size:11.5px;text-decoration:none;color:var(--accent);
  background:#eef1f8;border:1px solid #dbe2f0;border-radius:12px;padding:1px 8px}
.chip:hover{background:#e2e8f6}
.chip-dangling{background:#fdecec;border-color:#f3c2c2;color:#a4243b}
.src-meta-row{display:flex;flex-wrap:wrap;gap:14px;margin-bottom:6px;font-size:12.5px;color:var(--muted)}
.notfielded{color:#a08a2a;font-size:12.5px;font-style:italic}
.shared-group{background:var(--card);border:1px solid var(--line);border-radius:8px;margin-bottom:10px;overflow:hidden}
.shared-group>summary{cursor:pointer;padding:12px 14px;font-weight:600;list-style:none}
.shared-group>summary::-webkit-details-marker{display:none}
.shared-body{padding:4px 14px 14px;border-top:1px solid var(--line)}
mark{background:#ffe58a;padding:0 1px}
.hidden{display:none !important}
footer{color:var(--muted);font-size:12px;margin:20px 0 40px;text-align:center}
"""

JS = """
(function(){
  var box = document.getElementById('search');
  var groups = Array.prototype.slice.call(document.querySelectorAll('.inv-group,.shared-group'));
  function run(){
    var q = box.value.trim().toLowerCase();
    groups.forEach(function(g){
      var cards = g.querySelectorAll('.card');
      var anyCard = false;
      cards.forEach(function(c){
        var hit = !q || (c.getAttribute('data-search')||'').indexOf(q) !== -1;
        c.classList.toggle('hidden', !hit);
        if(hit) anyCard = true;
      });
      var sum = g.querySelector('summary');
      var sumHit = sum && (sum.getAttribute('data-search')||'').indexOf(q) !== -1;
      var show = !q || anyCard || sumHit;
      g.classList.toggle('hidden', !show);
      if(q){ g.open = show; } // expand matches while searching
    });
  }
  box.addEventListener('input', run);
  // reveal a chip target on click (open its ancestor group, flash it)
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a.chip');
    if(!a) return;
    var id = a.getAttribute('href').slice(1);
    var t = document.getElementById(id);
    if(!t) return;
    var grp = t.closest('.inv-group,.shared-group');
    if(grp) grp.open = true;
    t.scrollIntoView({behavior:'smooth',block:'center'});
    t.style.transition='background .2s'; var old=t.style.background;
    t.style.background='#fff6cc'; setTimeout(function(){t.style.background=old;},900);
  });
})();
"""


def build_html(objects, git_hash, gen_date):
    """Render the whole-vault view as one self-contained HTML string.

    Deterministic for fixed (objects, git_hash, gen_date): every list is id-sorted,
    so regeneration diffs reflect real vault change, not ordering churn. Only the
    generated-from header carries the varying hash/date (so a stale copy identifies
    itself). No external resources are referenced.
    """
    by_id, inv_groups, shared = build_tree(objects)

    counts = {t: sum(1 for o in objects if o["type"] == t) for t in KB_TYPES}
    total = len(objects)
    leaf_total = counts["CLM"] + counts["FND"]

    inv_html = "".join(_inv_group(g, by_id, gen_date) for g in inv_groups)

    shared_html = ""
    if shared:
        cards = "".join(
            (_leaf_card(o, by_id, gen_date) if o["type"] in LEAF_TYPES
             else _plain_card(o, by_id, gen_date))
            for o in shared
        )
        shared_html = (
            '<details class="shared-group" open>'
            f'<summary>Shared &amp; Cross-Investigation ({len(shared)}) '
            '<span class="count">— entities and objects with no single INV home</span></summary>'
            f'<div class="shared-body">{cards}</div></details>'
        )

    legend = (
        '<div class="legend">'
        '<div class="grp"><strong>Confidence:</strong></div>'
        + "".join(
            f'<div class="grp"><span class="swatch" style="background:{LEVEL_COLOR[l]}"></span>'
            f'{l} {esc(EPISTEMIC_LEVEL_LABELS[l])}</div>' for l in (5, 4, 3, 2, 1))
        + '<div class="grp"><strong>Reliance:</strong></div>'
        + "".join(
            f'<div class="grp"><span class="swatch" style="background:{RELIANCE_COLOR[t]}"></span>'
            f'{t}</div>' for t in ("R0", "R1", "R2"))
        + '<div class="grp"><strong>Edges:</strong> derived_from = spine · '
        'contrasts_with / depends_on / supports = cross-links (chips)</div>'
        '<div class="grp"><span class="pastdue">⚠ PAST DUE</span> = review_date elapsed</div>'
        '</div>'
    )

    banner = (
        '<div class="reliance-banner">'
        'Findings not cleared for external reliance — reliance tiers shown per node.'
        '<small>The reliance tier travels with the data. R0 = parametric only; '
        'R1 = retrieval-verified (ADR-GOV-0006); R2 = independently verified. '
        'Promoting a tier is a contribution surface, not a disclaimer — see each node.</small>'
        '</div>'
    )

    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>Relatio Vault View</title>\n"
        f"<style>{CSS}</style>\n</head>\n<body>\n"
        + banner
        + '<div class="wrap">\n'
        + '<header class="gen">'
        + '<h1>Relatio Knowledge Base — Snapshot View</h1>'
        + f'<span class="genmeta">generated {esc(gen_date.isoformat())} · '
          f'HEAD {esc(git_hash)} · read-only · frontmatter-only</span>'
        + f'<span class="genmeta">{total} objects — {counts["INV"]} INV · '
          f'{counts["CLM"]} CLM · {counts["FND"]} FND · {counts["SRC"]} SRC · '
          f'{counts["ENT"]} ENT · {leaf_total} reliance-graded</span>'
        + '</header>\n'
        + legend
        + '<div class="searchbar"><input id="search" type="text" '
          'placeholder="Filter by identifier or title…" autocomplete="off"></div>\n'
        + inv_html
        + shared_html
        + '<footer>Generated by tools/build_view.py — regenerate after vault '
          'changes; never hand-edit. The reliance banner and per-node reliance '
          'badges are load-bearing and must not be removed.</footer>\n'
        + '</div>\n'
        + f"<script>{JS}</script>\n"
        + "</body>\n</html>\n"
    )


# ---------------------------------------------------------------------------
# Timeline emitter (ADR-GOV-0009 — Path A: honesty over false precision)
#
# SECOND OUTPUT of the same parse. Renders tradition-class entities (ENT with
# `tradition_type`) in a root-first lineage layout. display_range is VERBATIM —
# never parsed into numeric years for display or positioning. The only reading
# of the range text is a deliberately coarse era key used for SEQUENCE ONLY
# (which card comes before which); a proportional numeric axis is a NAMED
# FUTURE REFINEMENT requiring structured date fields, explicitly out of scope.
# ---------------------------------------------------------------------------

import re as _re

# Qualifier -> (colour, border-style, glyph). Distinct by colour AND border
# style AND printed label, so the distinction is never colour-only. Palette
# deliberately away from both the confidence colours (greens/ambers/reds) and
# the reliance blue-greys. `disputed` additionally carries the uncertainty
# marking (dashed border + "?" glyph + an explicit uncertainty line).
QUALIFIER_STYLE = {
    "schism":             ("#7a3b5e", "solid",  "∥"),   # ∥ split
    "reform":             ("#3b6e7a", "double", "↻"),   # ↻ renewal
    "syncretic-descent":  ("#5e3b7a", "dotted", "⊕"),   # ⊕ fusion
    "heterodox-offshoot": ("#7a5e3b", "dashed", "≠"),   # ≠ divergence
    "disputed":           ("#6b6b66", "dashed", "?"),
}

QUALIFIER_MEANING = {
    "schism": "a split within one tradition",
    "reform": "a reform movement become its own tradition",
    "syncretic-descent": "descent absorbing the parent among other sources",
    "heterodox-offshoot": "a heterodox movement diverging from the parent",
    "disputed": "descent itself contested — the uncertainty IS the finding",
}

# Curated notes (Path A honesty: an overturned hypothesis renders as PRESENCE,
# not silence). The dissolution outcome lives in INV-0016's prose, not in any
# frontmatter field, so this note is CURATED and flagged as such in the render;
# only the confidence/reliance appended from the cited claim is field-derived.
CURATED_NOTES = [
    {
        "heading": "Zurvanism — investigated, found NOT to warrant tradition status",
        "body": (
            "A hypothesized branch (Zurvanism) was investigated in INV-0016 and "
            "found not to clear the §2.3 distinctness threshold: no attested "
            "separate community, priesthood, or lineage. It is modelled as a "
            "heterodox CURRENT within Zoroastrianism (ENT-0008) — no tradition "
            "entity, no branches_from edge. The overturned hypothesis is a "
            "feature of the record, not an omission."
        ),
        "cites": ["INV-0016", "CLM-0088"],
        "field_claim": "CLM-0088",
    },
]

_MILLENNIUM_RE = _re.compile(r"(\d+)(?:st|nd|rd|th)?[^0-9]*millenni", _re.I)
_CENTURY_RE = _re.compile(r"(\d+)(?:st|nd|rd|th)?\s*c\b", _re.I)
_NUMBER_RE = _re.compile(r"(\d+)")


def _sequence_key(display_range):
    """A coarse comparable era value for SEQUENCE ORDERING ONLY, or None.

    Best-effort reading of an as-authored range string: era (BCE/CE) plus the
    first millennium/century/number mention, collapsed to an approximate year
    count. This value NEVER positions anything and NEVER renders — it only
    decides which card precedes which. Unreadable ranges return None and fall
    back to branch-structure grouping with a visible ambiguity note.
    """
    if not isinstance(display_range, str) or not display_range.strip():
        return None
    text = display_range
    bce = _re.search(r"\bBCE\b", text) is not None
    m = _MILLENNIUM_RE.search(text)
    if m:
        magnitude = int(m.group(1)) * 1000
    else:
        c = _CENTURY_RE.search(text)
        if c:
            magnitude = int(c.group(1)) * 100
        else:
            n = _NUMBER_RE.search(text)
            if n:
                magnitude = int(n.group(1))
            else:
                return None
    return -magnitude if bce else magnitude


def timeline_entries(objects):
    """Tradition entities joined to their dating claims; plus graph errors.

    Returns (entries, errors). Each entry: the ENT node, its branches_from
    (target, qualifier) pairs, its resolved dating-claim nodes (confidence is
    FOLLOWED to the claim, never re-derived), and its sequence key. A
    dating_claims pointer that does not resolve to a Claim Record is a graph
    error — reported, and rendered honestly as unresolved.
    """
    by_id = {o["id"]: o for o in objects}
    errors = []
    entries = []
    for o in objects:
        if o["type"] != "ENT" or not o.get("tradition_type"):
            continue
        claims = []
        for cid in o.get("dating_claims", []):
            c = by_id.get(cid)
            if c is None or c["type"] != "CLM":
                errors.append(
                    f"{o['id']}: dating_claims pointer {cid} does not resolve "
                    f"to a Claim Record (graph error)")
                claims.append({"id": cid, "node": None})
            else:
                claims.append({"id": cid, "node": c})
        branches = []
        for rt, tgt in o["relationships"]:
            if rt == "branches_from":
                q = o.get("rel_qualifiers", {}).get((rt, tgt))
                branches.append((tgt, q))
        entries.append({
            "node": o,
            "claims": claims,
            "branches": sorted(branches),
            "seq": _sequence_key(o.get("display_range")),
        })
    entries.sort(key=lambda e: e["node"]["id"])
    return entries, errors


def _lineage_order(entries):
    """Root-first lineage ordering; returns (ordered_entries, ambiguous_ids).

    Roots (no branches_from) come first, then non-roots, each ordered by
    sequence key (SEQUENCE ONLY) with the identifier as the deterministic
    tie-break. An entry whose key is None, or which ties another entry's key,
    is ordered by branch structure + identifier and flagged ambiguous (the
    view notes it rather than implying a settled sequence).
    """
    roots = [e for e in entries if not e["branches"]]
    branched = [e for e in entries if e["branches"]]

    def sort_key(e):
        seq = e["seq"]
        return (0 if seq is not None else 1,
                seq if seq is not None else 0,
                e["node"]["id"])

    roots.sort(key=sort_key)
    branched.sort(key=sort_key)

    ambiguous = set()
    for group in (roots, branched):
        seqs = {}
        for e in group:
            if e["seq"] is None:
                ambiguous.add(e["node"]["id"])
            else:
                seqs.setdefault(e["seq"], []).append(e["node"]["id"])
        for ids in seqs.values():
            if len(ids) > 1:
                ambiguous.update(ids)
    return roots + branched, ambiguous


def _tl_confidence(claim_entry):
    """One dating claim's confidence, followed to the claim node.

    Components render SEPARATELY (never merged/averaged); each level keeps its
    colour badge, and weak grades (level <= 2) additionally get a non-colour
    weight marking (`conf-weak`) so Low reads distinct from Moderate even in
    grayscale — the visual-weight rule the brief makes load-bearing.
    """
    cid = claim_entry["id"]
    c = claim_entry["node"]
    if c is None:
        return (f'<div class="tl-claim tl-claim-unresolved">dating claim '
                f'{esc(cid)} — <span class="notfielded">pointer does not '
                f'resolve (graph error)</span></div>')
    rows = []
    for comp in c["confidence"]:
        level, label = comp["level"], comp["label"]
        if level is None:
            badge = '<span class="level-badge level-na" title="level not fielded">?</span>'
            lbl = '<span class="notfielded">level not fielded</span>'
            weak = ""
        else:
            color = LEVEL_COLOR.get(level, "#888")
            badge = (f'<span class="level-badge" style="background:{color}" '
                     f'title="confidence level {level}">{level}</span>')
            lbl = esc(label if label else EPISTEMIC_LEVEL_LABELS.get(level, "?"))
            weak = " conf-weak" if level <= 2 else ""
        rows.append(
            f'<div class="conf-row{weak}">{badge}'
            f'<span class="conf-name">{esc(comp["component"])}</span>'
            f'<span class="conf-label">{lbl}</span></div>')
    conf = ("".join(rows) if rows
            else '<div class="notfielded">confidence not fielded</div>')
    return (f'<div class="tl-claim"><span class="tl-claim-id">dating: '
            f'{esc(cid)}</span> <span class="tl-claim-title">{esc(c["title"])}'
            f'</span><div class="conf-block">{conf}</div></div>')


def _tl_reliance_badge(entry):
    """The tradition node's load-bearing reliance badge (never omitted).

    The tier is the FLOOR (weakest) across the entity's resolved dating
    claims — the per-locus floor roll-up of STD-0008, followed to the claims,
    never re-derived. Unresolvable -> an honest "R?" badge, still rendered and
    still counted (the self-check counts `trad-reliance`, one per tradition).
    """
    tiers = [ce["node"]["reliance_tier"] for ce in entry["claims"]
             if ce["node"] is not None and ce["node"]["reliance_tier"] in RELIANCE_COLOR]
    if tiers:
        tier = max(tiers, key=lambda t: -RELIANCE_TIER_RANK[t])
        color = RELIANCE_COLOR[tier]
        title = RELIANCE_MEANING.get(tier, "")
        text = tier
    else:
        tier, color, title, text = None, "#888", "reliance tier not resolvable from dating claims", "R?"
    return (f'<span class="reliance-badge trad-reliance" style="background:{color}" '
            f'title="{esc(title)}">{esc(text)}</span>')


# Rank for the floor roll-up: R0 weakest.
RELIANCE_TIER_RANK = {"R0": 0, "R1": 1, "R2": 2}


def _tl_edge(entry, by_id):
    """The inbound branches_from edge(s), rendered distinctly by qualifier."""
    if not entry["branches"]:
        return ('<div class="tl-edge tl-root-marker">family root — no '
                'branches_from edge</div>')
    parts = []
    for tgt, qual in entry["branches"]:
        parent = by_id.get(tgt)
        pname = parent["title"] if parent else tgt
        color, border, glyph = QUALIFIER_STYLE.get(
            qual, ("#888", "solid", "→"))
        qual_txt = qual if qual else "qualifier missing"
        qcls = f" qual-{qual}" if qual in QUALIFIER_STYLE else " qual-unknown"
        uncertainty = ""
        if qual == "disputed":
            uncertainty = ('<div class="tl-disputed-note">descent disputed — '
                           'the uncertainty is the finding, not a rendering '
                           'artifact</div>')
        parts.append(
            f'<div class="tl-edge{qcls}" style="border-left:3px {border} {color}">'
            f'<span class="tl-edge-glyph" style="color:{color}">{glyph}</span> '
            f'branches_from <a class="tl-edge-target" href="#tl-{esc(tgt)}">'
            f'{esc(tgt)}</a> {esc(pname)} '
            f'<span class="tl-qual" style="background:{color}">{esc(qual_txt)}</span>'
            f'{uncertainty}</div>')
    return "".join(parts)


def _tl_card(entry, by_id, ambiguous):
    node = entry["node"]
    amb = ""
    if node["id"] in ambiguous:
        amb = ('<span class="tl-ambiguous" title="sequence not derivable from '
               'display_range — grouped by branch structure">sequence '
               'ambiguous</span>')
    claims_html = "".join(_tl_confidence(ce) for ce in entry["claims"]) or \
        '<div class="notfielded">no dating_claims fielded</div>'
    return (
        f'<div class="tl-card" id="tl-{esc(node["id"])}">'
        f'<div class="tl-head">'
        f'<span class="id-badge">{esc(node["id"])}</span>'
        f'<span class="tl-name">{esc(node["title"])}</span>'
        f'<span class="tl-type">{esc(node["tradition_type"])}</span>'
        f'{_tl_reliance_badge(entry)}'
        f'{amb}'
        f'</div>'
        f'<div class="tl-range" title="display_range — rendered as authored, '
        f'render-only, no evidential weight">{esc(node["display_range"])} '
        f'<span class="tl-range-tag">as authored</span></div>'
        f'{_tl_edge(entry, by_id)}'
        f'{claims_html}'
        f'</div>')


def _tl_curated_notes(by_id):
    """The curated-note cards (Zurvanism). Flagged curated, not field-derived;
    the cited claim's confidence/reliance, where it resolves, is appended and
    labelled as the field-derived part."""
    cards = []
    for note in CURATED_NOTES:
        cites = " · ".join(esc(c) for c in note["cites"])
        field_html = ""
        c = by_id.get(note["field_claim"])
        if c is not None and c["type"] == "CLM":
            field_html = (
                '<div class="tl-note-field"><span class="tl-note-field-tag">'
                'field-derived from ' + esc(note["field_claim"]) + ':</span>'
                + _tl_confidence({"id": note["field_claim"], "node": c})
                + '</div>')
        else:
            field_html = ('<div class="notfielded">cited claim '
                          + esc(note["field_claim"])
                          + ' not present in this build</div>')
        cards.append(
            f'<div class="tl-note">'
            f'<div class="tl-note-head">{esc(note["heading"])} '
            f'<span class="tl-note-tag">curated note — not field-derived</span></div>'
            f'<div class="tl-note-body">{esc(note["body"])}</div>'
            f'<div class="tl-note-cites">per {cites}</div>'
            f'{field_html}'
            f'</div>')
    return "".join(cards)


TL_CSS = """
:root{
  --bg:#f7f7f5; --fg:#1e1e1c; --muted:#6b6b66; --line:#e0e0da; --card:#ffffff;
  --banner:#7a1f2b; --banner-fg:#fff; --accent:#2b3a67;
}
*{box-sizing:border-box}
body{margin:0;font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  background:var(--bg);color:var(--fg)}
.reliance-banner{position:sticky;top:0;z-index:50;background:var(--banner);color:var(--banner-fg);
  padding:10px 18px;font-weight:600;font-size:14px;box-shadow:0 1px 4px rgba(0,0,0,.2)}
.reliance-banner small{display:block;font-weight:400;opacity:.92;margin-top:2px}
.wrap{max-width:900px;margin:0 auto;padding:18px}
header.gen{display:flex;flex-wrap:wrap;gap:10px 20px;align-items:baseline;
  border-bottom:1px solid var(--line);padding-bottom:12px;margin-bottom:14px}
header.gen h1{font-size:20px;margin:0}
.genmeta{color:var(--muted);font-size:12.5px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.pathnote{background:#fdf6e3;border:1px solid #e8dcb5;border-radius:8px;padding:10px 14px;
  margin-bottom:14px;font-size:13px}
.legend{display:flex;flex-wrap:wrap;gap:14px;background:var(--card);border:1px solid var(--line);
  border-radius:8px;padding:10px 14px;margin-bottom:14px;font-size:12.5px}
.legend .grp{display:flex;gap:6px;align-items:center}
.legend .swatch{width:16px;height:16px;border-radius:4px;display:inline-block}
.legend .edge-sample{display:inline-block;width:26px;border-bottom-width:3px;height:0}
.tl-lane{position:relative;padding-left:26px}
.tl-lane:before{content:"";position:absolute;left:9px;top:0;bottom:0;width:2px;background:var(--line)}
.tl-card{position:relative;background:var(--card);border:1px solid var(--line);border-radius:8px;
  padding:12px 14px;margin-bottom:14px}
.tl-card:before{content:"";position:absolute;left:-22px;top:18px;width:12px;height:12px;
  border-radius:50%;background:var(--accent);border:2px solid var(--bg)}
.tl-head{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.tl-name{font-weight:700;font-size:16px}
.tl-type{font-size:11.5px;color:var(--muted);background:#f3eefb;border:1px solid var(--line);
  border-radius:10px;padding:1px 8px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.tl-range{margin:8px 0 6px;font-size:15px;font-weight:600}
.tl-range-tag{font-size:11px;font-weight:400;color:var(--muted);font-style:italic;margin-left:6px}
.tl-ambiguous{font-size:11px;color:#8a6d1a;background:#fdf3d0;border:1px dashed #d8c27a;
  border-radius:10px;padding:1px 8px}
.tl-edge{margin:7px 0;padding:5px 0 5px 10px;font-size:13px}
.tl-root-marker{border-left:3px solid var(--accent);color:var(--muted);font-style:italic}
.tl-edge-glyph{font-weight:700}
.tl-edge-target{color:var(--accent);text-decoration:none;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.tl-qual{display:inline-block;color:#fff;font-size:11px;font-weight:700;border-radius:10px;
  padding:1px 8px;margin-left:6px}
.qual-disputed .tl-qual{font-style:italic}
.tl-disputed-note{font-size:12px;color:#6b6b66;font-style:italic;margin-top:3px}
.tl-claim{margin-top:8px;border-top:1px dashed var(--line);padding-top:7px;font-size:13px}
.tl-claim-id{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-weight:700;font-size:12px}
.tl-claim-title{color:var(--muted);font-size:12.5px}
.tl-claim-unresolved{color:#a4243b}
.conf-block{display:flex;flex-direction:column;gap:3px;margin-top:5px}
.conf-row{display:flex;gap:8px;align-items:center}
.conf-row.conf-weak{border:1px dashed #c65a11;border-radius:6px;padding:2px 6px;background:#fdf4ec}
.conf-row.conf-weak .conf-label{font-weight:700}
.conf-name{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px}
.conf-label{color:var(--muted);font-size:12.5px}
.level-badge{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;
  border-radius:5px;color:#fff;font-weight:700;font-size:12px;flex:none}
.level-na{background:#999}
.id-badge{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-weight:700;font-size:12.5px}
.reliance-badge{display:inline-block;color:#fff;font-weight:700;font-size:12px;padding:2px 9px;border-radius:5px}
.trad-reliance{margin-left:auto}
.notfielded{color:#a08a2a;font-size:12.5px;font-style:italic}
.tl-note{background:#f6f4ef;border:1px solid #ddd6c4;border-radius:8px;padding:12px 14px;margin:16px 0}
.tl-note-head{font-weight:700}
.tl-note-tag{font-size:11px;font-weight:400;color:#8a6d1a;background:#fdf3d0;border:1px dashed #d8c27a;
  border-radius:10px;padding:1px 8px;margin-left:8px}
.tl-note-body{font-size:13.5px;margin-top:6px}
.tl-note-cites{font-size:12px;color:var(--muted);margin-top:5px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.tl-note-field{margin-top:8px}
.tl-note-field-tag{font-size:11.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
footer{color:var(--muted);font-size:12px;margin:20px 0 40px;text-align:center}
"""


def build_timeline_html(objects, git_hash, gen_date):
    """Render the timeline view as one self-contained HTML string (Path A).

    Deterministic for fixed (objects, git_hash, gen_date). Verbatim ranges;
    sequence-only ordering; no proportional axis (named future refinement).
    """
    by_id = {o["id"]: o for o in objects}
    entries, errors = timeline_entries(objects)
    ordered, ambiguous = _lineage_order(entries)

    cards = "".join(_tl_card(e, by_id, ambiguous) for e in ordered)
    edge_count = sum(len(e["branches"]) for e in entries)

    legend = (
        '<div class="legend">'
        '<div class="grp"><strong>tradition_type:</strong> '
        'founded · emergent · reform · syncretic</div>'
        '<div class="grp"><strong>Qualifiers:</strong></div>'
        + "".join(
            f'<div class="grp"><span class="edge-sample" '
            f'style="border-bottom:3px {QUALIFIER_STYLE[q][1]} {QUALIFIER_STYLE[q][0]}"></span>'
            f'{QUALIFIER_STYLE[q][2]} {esc(q)} — {esc(QUALIFIER_MEANING[q])}</div>'
            for q in ("schism", "reform", "syncretic-descent",
                      "heterodox-offshoot", "disputed"))
        + '<div class="grp"><strong>Confidence:</strong></div>'
        + "".join(
            f'<div class="grp"><span class="swatch" style="background:{LEVEL_COLOR[l]}"></span>'
            f'{l} {esc(EPISTEMIC_LEVEL_LABELS[l])}</div>' for l in (5, 4, 3, 2, 1))
        + '<div class="grp">Low / Very Low components additionally render with '
        'a dashed weak-grade box (not colour-only)</div>'
        '<div class="grp"><strong>Reliance:</strong></div>'
        + "".join(
            f'<div class="grp"><span class="swatch" style="background:{RELIANCE_COLOR[t]}"></span>'
            f'{t}</div>' for t in ("R0", "R1", "R2"))
        + '<div class="grp"><span class="tl-ambiguous">sequence ambiguous</span> '
        '= order not derivable from display_range; grouped by branch structure</div>'
        '</div>'
    )

    banner = (
        '<div class="reliance-banner">'
        'Findings not cleared for external reliance — reliance tiers shown per node.'
        '<small>The reliance tier travels with the data. R0 = parametric only; '
        'R1 = retrieval-verified (ADR-GOV-0006); R2 = independently verified. '
        'Promoting a tier is a contribution surface, not a disclaimer — see each node.</small>'
        '</div>'
    )

    pathnote = (
        '<div class="pathnote"><strong>Path A — honesty over false precision.</strong> '
        'Every range below renders exactly as authored in its entity\'s '
        '<code>display_range</code> (render-only, no evidential weight; dates are '
        'claims — see each node\'s dating claim). Cards are ordered root-first, '
        'then by a coarse era reading used for <em>sequence only</em> — spacing '
        'and position are NOT proportional to time. A proportional numeric axis '
        'is a named future refinement requiring structured date fields; it is '
        'deliberately not approximated here.</div>'
    )

    errors_html = ""
    if errors:
        errors_html = ('<div class="pathnote" style="border-color:#a4243b">'
                       '<strong>Graph errors:</strong><br>'
                       + "<br>".join(esc(e) for e in errors) + '</div>')

    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>Relatio Timeline View</title>\n"
        f"<style>{TL_CSS}</style>\n</head>\n<body>\n"
        + banner
        + '<div class="wrap">\n'
        + '<header class="gen">'
        + '<h1>Relatio — World-Religions Timeline (ADR-GOV-0009)</h1>'
        + f'<span class="genmeta">generated {esc(gen_date.isoformat())} · '
          f'HEAD {esc(git_hash)} · read-only · frontmatter-only · Path A</span>'
        + f'<span class="genmeta">{len(entries)} traditions · {edge_count} '
          f'branches_from edges</span>'
        + '</header>\n'
        + pathnote
        + legend
        + errors_html
        + f'<div class="tl-lane">{cards}</div>\n'
        + _tl_curated_notes(by_id)
        + '<footer>Generated by tools/build_view.py — regenerate after vault '
          'changes; never hand-edit. The reliance banner, per-tradition reliance '
          'badges, and confidence markings are load-bearing and must not be '
          'removed. Ranges are verbatim; ordering is sequence-only (Path A).</footer>\n'
        + '</div>\n'
        + "</body>\n</html>\n"
    )


def _git_short_hash(vault):
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(vault), capture_output=True, text=True, timeout=15,
        )
        if out.returncode == 0:
            return out.stdout.strip() or "unknown"
    except Exception:
        pass
    return "unknown"


def main():
    tools = Path(__file__).parent
    vault = find_vault_root(tools)
    repo_root = vault.parent  # git root is the Research OS parent dir
    objects = collect_objects(vault)
    git_hash = _git_short_hash(repo_root)
    gen_date = date.today()

    html_out = build_html(objects, git_hash, gen_date)

    views = repo_root / "views"
    views.mkdir(exist_ok=True)
    out_path = views / "relatio-view.html"
    write_text(out_path, html_out)

    counts = {t: sum(1 for o in objects if o["type"] == t) for t in KB_TYPES}
    leaf = [o for o in objects if o["type"] in LEAF_TYPES]
    badge_count = html_out.count('reliance-badge head-reliance"')
    print(f"Wrote {out_path}")
    print(f"  objects: {len(objects)}  "
          + "  ".join(f"{t}={counts[t]}" for t in KB_TYPES))
    print(f"  reliance-graded (CLM/FND): {len(leaf)}  head-reliance badges: {badge_count}")
    failed = False
    if badge_count != len(leaf):
        print("  WARNING: reliance-badge count != CLM/FND count", file=sys.stderr)
        failed = True

    # Second output: the timeline view (ADR-GOV-0009, Path A). Same parse.
    tl_out = build_timeline_html(objects, git_hash, gen_date)
    tl_path = views / "relatio-timeline.html"
    write_text(tl_path, tl_out)

    entries, errors = timeline_entries(objects)
    edge_count = sum(len(e["branches"]) for e in entries)
    tl_badges = tl_out.count('trad-reliance"')
    print(f"Wrote {tl_path}")
    print(f"  traditions: {len(entries)}  branches_from edges: {edge_count}  "
          f"trad-reliance badges: {tl_badges}")
    for err in errors:
        print(f"  GRAPH ERROR: {err}", file=sys.stderr)
        failed = True
    # Load-bearing self-check (mirror of the tree view's): exactly one reliance
    # badge per tradition node — no view path may strip it.
    if tl_badges != len(entries):
        print("  WARNING: trad-reliance badge count != tradition count",
              file=sys.stderr)
        failed = True
    if "curated note — not field-derived" not in tl_out and CURATED_NOTES:
        print("  WARNING: curated overturned-hypothesis note missing",
              file=sys.stderr)
        failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
