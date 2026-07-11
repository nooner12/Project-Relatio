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
- **Dangling references** — any `parent_documents` / `related_documents` entry that
  resolves to no existing object. Exit code 1 if any exist (reliability-critical).
- **One-directional KB links** — advisory; among Knowledge Base objects
  (INV/CLM/SRC/ENT/FND), an `A -> B` related link with no `B -> A` back
  (a parent-link counts as reciprocation). OPS-0002 §5 treats these as low-severity.

Matches the vault's actual convention: identifiers embedded in `title`/filename,
graph in `related_documents:` / `parent_documents:`.

## validate.py — structural conformance (partial)

Checks empty files, YAML validity, duplicate filenames, and broken `[[wikilinks]]`.
Note: it predates the current standards and does **not** check the
`related_documents` graph (that is graph_integrity.py's job). Its `id`-field check
is disabled (see validator_rules.yaml); aligning it to title-embedded identifiers
is Backlog GB-2026-016.
