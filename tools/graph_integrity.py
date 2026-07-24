#!/usr/bin/env python3
"""
graph_integrity.py — Relationship-graph integrity check for Project Relatio.

Implements the OPS-0002 (Relationship Integrity & Graph Maintenance) validation
as automation, so the Knowledge Architect no longer has to check the graph by hand.

It matches the vault's ACTUAL convention (STD-0001/STD-0002): identifiers are
embedded in the `title`/filename (e.g. "CLM-0007 - ..."), and the knowledge graph
lives in the `related_documents:` and `parent_documents:` YAML lists — NOT in an
`id` field or in [[wikilinks]] (which is what the older validate.py assumed).

Three checks:
  1. Dangling references — any `parent_documents` / `related_documents` entry, OR
     any typed `relationships:` target (STD-0002 §7 / STD-0004), OR any
     `bounded_by` entry inside a `confidence` component (STD-0002 §11 v1.9 /
     STD-0009 §9), that does not resolve to an existing object.
  2. Non-reciprocated symmetric typed links (type-aware, GB-2026-001) — among KB
     research objects, a *symmetric*-type edge (`related_to`, `contrasts_with`) with
     no reciprocal symmetric edge back. Directional types (`derived_from`, `supports`,
     `part_of`, `depends_on`, `explains`, `defines`, …) are legitimately one-way and
     are NOT flagged — the typed block lets us tell the difference, which the old
     flat-list check could not.
  3. Untyped one-directional `related_documents` (legacy advisory) — kept only for
     KB objects that carry NO typed `relationships:` block, so nothing goes unchecked.

Exit code 0 = no dangling references (the reliability-critical failure).
Reciprocity findings are advisories, not failures (OPS-0002 §5 = low-severity).
"""

from pathlib import Path
import re
import sys
import yaml

from common import (
    find_vault_root, markdown_files, parse_frontmatter, read_text, write_text,
    confidence_bounded_by, relationship_entries, relationship_raw,
    branches_from_problems, projects_to_problems, influenced_by_problems,
)

# ADR-GOV-0001 style OR TYPE-NNNN style (CON/KOS/STD/ROLE/TPL/OPS/INV/CLM/SRC/ENT/FND)
ID_RE = re.compile(r"^(ADR-[A-Z]{2,5}-\d{4}|[A-Z]{2,5}-\d{4})")
KB_TYPES = ("INV", "CLM", "SRC", "ENT", "FND")
# STD-0004 symmetric relationship types — these are expected to reciprocate.
SYMMETRIC_TYPES = ("related_to", "contrasts_with")
# STD-0004 v1.2 §7.2: the provisional lineage edge — directional (never a
# symmetric-advisory candidate), ENT → ENT only, qualifier REQUIRED.
BRANCHES_FROM = "branches_from"
# STD-0004 v1.5 §7.3 (ADR-GOV-0012 D5/D6). Both are directional by construction
# and neither is in SYMMETRIC_TYPES, so neither is ever a reciprocity candidate:
# mutual influence is TWO explicit influenced_by edges, never one symmetric edge.
PROJECTS_TO = "projects_to"
INFLUENCED_BY = "influenced_by"

ROOT = Path(__file__).parent
vault = find_vault_root(ROOT)
files = list(markdown_files(vault))


def ident_of(text: str):
    """Extract a leading TYPE-NNNN / ADR-CAT-NNNN identifier from a string, or None."""
    m = ID_RE.match(text.strip())
    return m.group(0) if m else None


# ---- Index every object: identifier -> file, and name -> file -------------
by_id = {}
by_name = {}
objects = {}  # key -> {"file", "id", "name", "related": [...], "parents": [...], "kb": bool}

for f in files:
    stem = f.stem
    text = read_text(f)
    fm, _ = parse_frontmatter(text)
    meta = {}
    if fm is not None:
        try:
            loaded = yaml.safe_load(fm)
            if isinstance(loaded, dict):
                meta = loaded
        except Exception:
            meta = {}

    ident = ident_of(stem)
    key = ident or stem
    related = [str(x) for x in (meta.get("related_documents") or [])]
    parents = [str(x) for x in (meta.get("parent_documents") or [])]
    # typed relationships block (STD-0002 §7): list of {type, target, qualifier}.
    # `typed` stays 2-tuples (type, target) for the reciprocity checks; branch
    # edges keep their qualifier separately for the branches_from integrity check.
    entries = relationship_entries(meta)
    typed = [(e["type"], e["target"]) for e in entries]
    branches = [(e["target"], e["qualifier"])
                for e in entries if e["type"] == BRANCHES_FROM]
    # projects_to / influenced_by are checked against their RAW entries, not the
    # normalized ones: `projects_to`'s rule is that certain keys must be ABSENT
    # (STD-0004 §7.3), and a normalizer that drops unknown keys would make a
    # forbidden `confidence` invisible to the very check that must reject it.
    raw = relationship_raw(meta)
    projections = [r for r in raw if str(r["type"]).strip() == PROJECTS_TO]
    influences = [r for r in raw if str(r["type"]).strip() == INFLUENCED_BY]
    # bounded_by entries inside confidence components (STD-0002 §11 v1.9 /
    # STD-0009 §9): each is a graph claim, so it participates in dangling
    # detection exactly like a relationships target. Optional; usually absent.
    bounded = confidence_bounded_by(meta)
    # dating_claims on tradition-class entities (STD-0002 §11 v1.10): graph-claim
    # pointers, so they participate in dangling detection like any reference.
    dating = [str(x).strip() for x in (meta.get("dating_claims") or [])]
    # attestation_claims on community-class entities (STD-0002 §11 v1.13): graph
    # claims, exactly like dating_claims, so they join the dangling pass.
    attesting = [str(x).strip() for x in (meta.get("attestation_claims") or [])]
    is_kb = bool(ident) and ident.split("-")[0] in KB_TYPES

    objects[key] = {
        "file": f, "id": ident, "name": stem,
        "related": related, "parents": parents, "typed": typed,
        "branches": branches, "dating": dating, "attesting": attesting,
        "projections": projections, "influences": influences,
        "rendering_class": meta.get("rendering_class"),
        "bounded": bounded, "kb": is_kb,
    }
    if ident:
        by_id[ident] = key
    by_name[stem] = key


def resolve(ref: str):
    """Resolve a reference string to an object key, or None if it dangles."""
    ident = ident_of(ref)
    if ident and ident in by_id:
        return by_id[ident]
    ref = ref.strip()
    # unnumbered meta-docs referenced by name (e.g. "Kernel Index")
    if ref in by_name:
        return by_name[ref]
    for name, key in by_name.items():
        if name.startswith(ref) or ref.startswith(name):
            return key
    return None


# ---- Check 1: dangling references (flat lists + typed targets) -------------
dangling = []
for key, o in objects.items():
    for field in ("parents", "related"):
        for ref in o[field]:
            if resolve(ref) is None:
                fld = "parent_documents" if field == "parents" else "related_documents"
                dangling.append((o["name"], fld, ref))
    for rtype, target in o["typed"]:
        if resolve(target) is None:
            dangling.append((o["name"], f"relationships[{rtype}]", target))
    for cname, target in o["bounded"]:
        if resolve(target) is None:
            dangling.append((o["name"], f"confidence[{cname}].bounded_by", target))
    for target in o["dating"]:
        if resolve(target) is None:
            dangling.append((o["name"], "dating_claims", target))
    for target in o["attesting"]:
        if resolve(target) is None:
            dangling.append((o["name"], "attestation_claims", target))

# ---- Check 1b: branches_from lineage-edge integrity (STD-0004 v1.2 §7.2) ----
# Errors (fail the build), not advisories: the provisional edge is ENT → ENT
# only and its qualifier is REQUIRED and drawn from a controlled list. The
# warrant rule (every edge backed by a graded claim) is NOT enforced here --
# see the report note and tools/README.md for why it is review-checked.
def _type_of(target):
    """The object type ('ENT', 'CLM', …) of a reference target, or None if it
    does not resolve. Used by branches_from's ENT-target check (shared helper)."""
    tgt = resolve(target)
    if tgt is None:
        return None
    tid = objects[tgt]["id"]
    return tid.split("-")[0] if tid else None


branch_errors = []
for key, o in objects.items():
    if not o["branches"]:
        continue
    for target, why in branches_from_problems(o["id"], o["branches"], _type_of):
        branch_errors.append((o["name"], target, why))


# ---- Check 1c: projects_to + influenced_by integrity (STD-0004 v1.5 §7.3) ----
# ADR-GOV-0012 D5/D6. Errors, not advisories, and for opposite reasons:
#
#   * `projects_to` is NON-EVIDENTIAL and must STAY non-evidential. It runs
#     non-tradition -> tradition, is machine-traversable (roll-up rendering will
#     traverse it, so a dangling target is an error via Check 1 above), and takes
#     NO qualifier, NO warrant, and NO confidence. Enforcing the absences is what
#     keeps a rendering convenience from quietly becoming a historical claim.
#
#   * `influenced_by` IS evidential, and its warrant rule is CONSTITUTIVE: a
#     graded warrant PLUS a recorded not-descent determination naming why
#     `branches_from` was refused. Both are structured resolvable pointers, so
#     unlike the branches_from warrant rule this one is TOOL-checked. Without it
#     the type becomes the soft option that empties the edge-restraint rule.
#
# `warrant` / `not_descent` resolvability is reported HERE rather than folded
# into Check 1's dangling list, so a broken warrant is named as the edge defect
# it is instead of appearing twice under two headings.
def _class_of(target):
    """(object type, rendering_class) of a reference target; (None, None) if it
    does not resolve. Used by the projects_to class-direction check."""
    tgt = resolve(target)
    if tgt is None:
        return None, None
    tid = objects[tgt]["id"]
    return (tid.split("-")[0] if tid else None), objects[tgt]["rendering_class"]


projection_errors = []
influence_errors = []
for key, o in objects.items():
    for target, why in projects_to_problems(o["id"], o["projections"], _class_of):
        projection_errors.append((o["name"], target, why))
    for target, why in influenced_by_problems(
            o["id"], o["influences"], _type_of,
            lambda ref: resolve(ref) is not None):
        influence_errors.append((o["name"], target, why))

# ---- Check 2: non-reciprocated SYMMETRIC typed links (type-aware) ----------
# branches_from is directional by construction and is NOT in SYMMETRIC_TYPES, so
# it is never a reciprocity candidate here (STD-0004 v1.2 §7.2).
# Only related_to / contrasts_with are expected to reciprocate. A reciprocal is
# any symmetric typed edge from B back to A. Directional types are never flagged.
sym_one_way = []
for key, o in objects.items():
    if not o["kb"]:
        continue
    for rtype, target in o["typed"]:
        if rtype not in SYMMETRIC_TYPES:
            continue
        tgt = resolve(target)
        if tgt is None or not objects[tgt]["kb"]:
            continue
        t = objects[tgt]
        back = any(rt in SYMMETRIC_TYPES and resolve(tg) == key
                   for rt, tg in t["typed"])
        if not back:
            sym_one_way.append((o["id"] or o["name"], rtype, t["id"] or t["name"]))

# ---- Check 3: legacy untyped one-directional related_documents ------------
# Only for KB objects with NO typed block (so nothing goes unchecked).
one_way = []
for key, o in objects.items():
    if not o["kb"] or o["typed"]:
        continue
    for ref in o["related"]:
        tgt = resolve(ref)
        if tgt is None:
            continue
        t = objects[tgt]
        if not t["kb"]:
            continue
        back = any(resolve(r) == key for r in t["related"]) or \
               any(resolve(p) == key for p in t["parents"])
        if not back:
            one_way.append((o["id"] or o["name"], t["id"] or t["name"]))


# ---- Report ---------------------------------------------------------------
lines = []
lines.append("# Graph Integrity Report - Project Relatio")
lines.append("")
lines.append(f"Objects scanned: {len(objects)}")
lines.append(f"Dangling references: {len(dangling)}")
lines.append(f"branches_from edge errors: {len(branch_errors)}")
lines.append(f"projects_to edge errors: {len(projection_errors)}")
lines.append(f"influenced_by edge errors: {len(influence_errors)}")
lines.append(f"Non-reciprocated symmetric typed links: {len(set(sym_one_way))}")
lines.append(f"Untyped one-directional KB links (legacy): {len(one_way)}")
lines.append("")

if dangling:
    lines.append("## Dangling references (FAIL - a reference resolves to nothing)")
    for name, fld, ref in sorted(dangling):
        lines.append(f"- `{name}` -> {fld}: `{ref}`")
    lines.append("")

if branch_errors:
    lines.append("## branches_from edge errors (FAIL - STD-0004 v1.2 §7.2)")
    lines.append("The provisional lineage edge is ENT -> ENT only, qualifier REQUIRED and controlled:")
    for name, target, why in sorted(branch_errors):
        lines.append(f"- `{name}` -[branches_from]-> `{target}`: {why}")
    lines.append("")

# The warrant rule (every branches_from edge backed by a graded claim) is
# review-checked, not tool-checked: a warrant is a claim ABOUT lineage, not a
# structured pointer on the edge, so confirming it needs prose reading. Per the
# ADR-GOV-0009 Task 4 fallback, qualifier + ENT->ENT are enforced here now; the
# warrant rule is recorded as review-checked (tools/README.md).
if projection_errors:
    lines.append("## projects_to edge errors (FAIL - STD-0004 v1.5 §7.3)")
    lines.append("NON-EVIDENTIAL: non-tradition -> tradition, and no qualifier / warrant / confidence:")
    for name, target, why in sorted(projection_errors):
        lines.append(f"- `{name}` -[projects_to]-> `{target}`: {why}")
    lines.append("")

if influence_errors:
    lines.append("## influenced_by edge errors (FAIL - STD-0004 v1.5 §7.3)")
    lines.append("ENT -> ENT, controlled qualifier, resolvable warrant, and a REQUIRED not-descent determination:")
    for name, target, why in sorted(influence_errors):
        lines.append(f"- `{name}` -[influenced_by]-> `{target}`: {why}")
    lines.append("")

lines.append("> Note: the branches_from **warrant rule** (every edge backed by a "
             "graded claim) is review-checked, not tool-checked (STD-0004 §7.2). "
             "The **influenced_by** warrant rule IS tool-checked (§7.3): its "
             "`warrant` and `not_descent` pointers are structured and resolvable, "
             "because ADR-GOV-0012 D6 makes the not-descent determination "
             "constitutive of the type.")
lines.append("")

if sym_one_way:
    lines.append("## Non-reciprocated symmetric typed links (advisory - GB-2026-001)")
    lines.append("A has a symmetric edge (related_to/contrasts_with) to B, but B has none back:")
    for a, rt, b in sorted(set(sym_one_way)):
        lines.append(f"- {a} -[{rt}]-> {b}  (no symmetric edge {b} -> {a})")
    lines.append("")

if one_way:
    lines.append("## Untyped one-directional KB links (legacy advisory - OPS-0002 sec.5)")
    lines.append("KB objects with no typed relationships block; A lists B but not vice-versa:")
    for a, b in sorted(set(one_way)):
        lines.append(f"- {a} -> {b}  (no {b} -> {a})")
    lines.append("")

if not dangling and not branch_errors and not projection_errors \
        and not influence_errors and not sym_one_way and not one_way:
    lines.append("No dangling references and full reciprocity. Graph is clean.")

report = "\n".join(lines)
print(report)

out = ROOT / "output" / "graph_integrity_report.md"
out.parent.mkdir(exist_ok=True)
write_text(out, report + "\n")

sys.exit(1 if (dangling or branch_errors or projection_errors
               or influence_errors) else 0)
