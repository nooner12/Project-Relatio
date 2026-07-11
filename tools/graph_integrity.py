#!/usr/bin/env python3
"""
graph_integrity.py — Relationship-graph integrity check for Project Relatio.

Implements the OPS-0002 (Relationship Integrity & Graph Maintenance) validation
as automation, so the Knowledge Architect no longer has to check the graph by hand.

It matches the vault's ACTUAL convention (STD-0001/STD-0002): identifiers are
embedded in the `title`/filename (e.g. "CLM-0007 - ..."), and the knowledge graph
lives in the `related_documents:` and `parent_documents:` YAML lists — NOT in an
`id` field or in [[wikilinks]] (which is what the older validate.py assumed).

Two checks:
  1. Dangling references — any `parent_documents` / `related_documents` entry that
     does not resolve to an existing object. (Both fields; references must resolve.)
  2. One-directional links — among Knowledge Base research objects
     (INV/CLM/SRC/ENT/FND), an A -> B `related_documents` link with no B -> A back.
     `parent_documents` is intentionally hierarchical (one-directional) and is NOT
     checked for reciprocity; references up to Kernel/Standards/Role docs are
     likewise not expected to reciprocate.

Exit code 0 = no dangling references (the reliability-critical failure).
One-directional links are reported as advisories, not failures (OPS-0002 §5 treats
them as low-severity maintenance).
"""

from pathlib import Path
import re
import sys
import yaml

from common import find_vault_root, markdown_files, parse_frontmatter

# ADR-GOV-0001 style OR TYPE-NNNN style (CON/KOS/STD/ROLE/TPL/OPS/INV/CLM/SRC/ENT/FND)
ID_RE = re.compile(r"^(ADR-[A-Z]{2,5}-\d{4}|[A-Z]{2,5}-\d{4})")
KB_TYPES = ("INV", "CLM", "SRC", "ENT", "FND")

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
    text = f.read_text(encoding="utf-8")
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
    is_kb = bool(ident) and ident.split("-")[0] in KB_TYPES

    objects[key] = {
        "file": f, "id": ident, "name": stem,
        "related": related, "parents": parents, "kb": is_kb,
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


# ---- Check 1: dangling references -----------------------------------------
dangling = []
for key, o in objects.items():
    for field in ("parents", "related"):
        for ref in o[field]:
            if resolve(ref) is None:
                fld = "parent_documents" if field == "parents" else "related_documents"
                dangling.append((o["name"], fld, ref))

# ---- Check 2: one-directional related_documents among KB objects ----------
one_way = []
for key, o in objects.items():
    if not o["kb"]:
        continue
    for ref in o["related"]:
        tgt = resolve(ref)
        if tgt is None:
            continue
        t = objects[tgt]
        if not t["kb"]:
            continue  # references up to Kernel/STD/ROLE are not expected to reciprocate
        # Reciprocation counts if B points back to A via EITHER related_documents
        # OR parent_documents (a child's parent-link is a valid reciprocal of the
        # parent's related-link — the relationship is bidirectional across two fields).
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
lines.append(f"One-directional KB links: {len(one_way)}")
lines.append("")

if dangling:
    lines.append("## Dangling references (FAIL - a reference resolves to nothing)")
    for name, fld, ref in sorted(dangling):
        lines.append(f"- `{name}` -> {fld}: `{ref}`")
    lines.append("")

if one_way:
    lines.append("## One-directional KB links (advisory - OPS-0002 sec.5)")
    lines.append("A lists B in related_documents, but B does not list A back:")
    for a, b in sorted(set(one_way)):
        lines.append(f"- {a} -> {b}  (no {b} -> {a})")
    lines.append("")

if not dangling and not one_way:
    lines.append("No dangling references and no one-directional KB links. Graph is clean.")

report = "\n".join(lines)
print(report)

out = ROOT / "output" / "graph_integrity_report.md"
out.parent.mkdir(exist_ok=True)
out.write_text(report + "\n", encoding="utf-8")

sys.exit(1 if dangling else 0)
