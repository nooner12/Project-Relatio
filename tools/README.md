# Project Relatio — Tools (RRI)

Implementation tooling that operates *on* the Project Relatio vault. This is
**RRI** (reference-implementation) tooling, not architecture (RKA): it enforces
the standards, it does not define them.

Requires: `pip install -r requirements.txt` (PyYAML).

## graph_integrity.py — relationship-graph integrity (OPS-0002 automation)

Automates the OPS-0002 (Relationship Integrity & Graph Maintenance) check so the
Knowledge Architect no longer validates the graph by hand.

```
python graph_integrity.py
```

Reports, and writes `output/graph_integrity_report.md`:
- **Dangling references** — any `parent_documents` / `related_documents` entry, or any
  typed `relationships:` target, that resolves to no existing object. Exit code 1 if
  any exist (reliability-critical).
- **Non-reciprocated symmetric typed links** — advisory; type-aware (GB-2026-001).
  Among KB objects, a *symmetric*-type edge (`related_to`, `contrasts_with`) with no
  reciprocal back. Directional types (`derived_from`, `supports`, `part_of`, …) are
  one-way by design and are NOT flagged — the typed block lets the tool tell them
  apart, which the old flat-list check could not. OPS-0002 §5 = low-severity.
- **Untyped one-directional KB links** — legacy advisory, only for KB objects that
  carry no typed `relationships:` block (so nothing goes unchecked).

Matches the vault's actual convention: identifiers embedded in `title`/filename,
flat graph in `related_documents:` / `parent_documents:`, typed edges in
`relationships:` (STD-0002 §7 / STD-0004).

## validate.py — structural conformance

```
python validate.py
```

Checks, per STD-0001/STD-0002:
- **Empty files** and **YAML validity** (frontmatter parses to a mapping).
- **Title-embedded identifier** — for identified objects (CON/KOS/STD/ROLE/TPL/OPS/
  ADR/ENT/SRC/INV/CLM/FND), the filename carries a valid identifier, the `title:`
  field carries the **same** one, and the identifier is **unique** across the vault.
  Identifier form: `TYPE-NNNN` (e.g. `KOS-0004`) or `ADR-CAT-NNNN` (e.g. `ADR-GOV-0001`).
- **Duplicate filenames** (advisory warning).

Exit code 1 if any errors. It does **not** check the `related_documents` graph — that
is graph_integrity.py's job. (Rebuilt from the old `id`/`[[wikilink]]` checks per
Backlog GB-2026-016; those predated the adopted standards.)
