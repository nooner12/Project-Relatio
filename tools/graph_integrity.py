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
    confidence_bounded_by,
)

# ADR-GOV-0001 style OR TYPE-NNNN style (CON/KOS/STD/ROLE/TPL/OPS/INV/CLM/SRC/ENT/FND)
ID_RE = re.compile(r"^(ADR-[A-Z]{2,5}-\d{4}|[A-Z]{2,5}-\d{4})")
KB_TYPES = ("INV", "CLM", "SRC", "ENT", "FND")
# STD-0004 symmetric relationship types — these are expected to reciprocate.
SYMMETRIC_TYPES = ("related_to", "contrasts_with")

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
    # typed relationships block (STD-0002 §7): list of {type, target}
    typed = []
    for r in (meta.get("relationships") or []):
        if isinstance(r, dict) and r.get("type") and r.get("target"):
            typed.append((str(r["type"]).strip(), str(r["target"]).strip()))
    # bounded_by entries inside confidence components (STD-0002 §11 v1.9 /
    # STD-0009 §9): each is a graph claim, so it participates in dangling
    # detection exactly like a relationships target. Optional; usually absent.
    bounded = confidence_bounded_by(meta)
    is_kb = bool(ident) and ident.split("-")[0] in KB_TYPES

    objects[key] = {
        "file": f, "id": ident, "name": stem,
        "related": related, "parents": parents, "typed": typed,
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

# ---- Check 2: non-reciprocated SYMMETRIC typed links (type-aware) ----------
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
lines.append(f"Non-reciprocated symmetric typed links: {len(set(sym_one_way))}")
lines.append(f"Untyped one-directional KB links (legacy): {len(one_way)}")
lines.append("")

if dangling:
    lines.append("## Dangling references (FAIL - a reference resolves to nothing)")
    for name, fld, ref in sorted(dangling):
        lines.append(f"- `{name}` -> {fld}: `{ref}`")
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

if not dangling and not sym_one_way and not one_way:
    lines.append("No dangling references and full reciprocity. Graph is clean.")

report = "\n".join(lines)
print(report)

out = ROOT / "output" / "graph_integrity_report.md"
out.parent.mkdir(exist_ok=True)
write_text(out, report + "\n")

sys.exit(1 if dangling else 0)
