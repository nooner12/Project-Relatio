# Project Relatio — Tools (RRI)

Implementation tooling that operates *on* the Project Relatio vault. This is
**RRI** (reference-implementation) tooling, not architecture (RKA): it enforces
the standards, it does not define them.

Requires: `pip install -r requirements.txt` (PyYAML).

**Windows long paths:** both tools read files through `common.read_text` / `write_text`,
which apply the `\\?\` extended-length prefix so deep vault folders plus long object
titles (absolute path > 260 chars) don't raise `FileNotFoundError`. This surfaced on
INV-0006, whose long finding title pushed the path past `MAX_PATH`.

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
- **Version coherence** (**error**; GB-2026-035) — a document's `version:` frontmatter,
  its `## Version` body heading, and the newest row of its own `# Revision History`
  table must agree.

  Built at warning level, on the reasoning that a drifted record's content is not
  wrong, only its summary field stale. **Promoted to error by owner ruling
  2026-07-21** on three grounds: a stale version field is a record lying about itself,
  which is the defect ADR-GOV-0004 §4's trust-without-re-derivation principle exists to
  prevent; the class produced 40 known instances, one of which manual sweeping
  structurally could not see; and a zero-warning baseline erodes, whereas an error
  cannot be deferred without a deliberate act. **A version bump that forgets its
  history row now fails validation.**

  Automates the countermeasure GB-2026-028 asked for. That entry's 2026-07-20 sweep
  found **39 drift instances** — spread across Claims, Findings, Sources, Entities,
  Investigations and two review reports — every one of which the validator had passed
  clean, because nothing compared the three elements. The sweep was remediation; this
  is the prevention.

  Two traps this check is built to avoid, both load-bearing:
  - **Newest history row by parse-and-max, never by position** (GB-2026-029). The
    Identifier Registry's rows are genuinely out of numeric order — its last row reads
    1.18 while the newest is 1.23.
  - **Versions compared as tuples, never as floats.** As floats 1.9 > 1.23; as
    versions the reverse. Relatedly, the frontmatter version is read as **literal text,
    not through `yaml.safe_load`** — unquoted `version: 1.10` is valid YAML for the
    float 1.1, which would silently drop the trailing zero and manufacture drift.

  Scope is **self-scoping and deliberately not gated by `validator_rules.yaml`**: the
  check runs wherever at least two of the three elements are present, and is silent
  where fewer are (a `version:` field alone has nothing to disagree with). Gating by
  document class would have blinded it — 17 versioned files, including the Architecture
  Baseline and every Critical Review report, match neither rule class, and the drift
  class had already reached two review reports.

Exit code 1 if any errors. It does **not** check the `related_documents` graph — that
is graph_integrity.py's job. (Rebuilt from the old `id`/`[[wikilink]]` checks per
Backlog GB-2026-016; those predated the adopted standards.)

## tests/ — detection tests

```
python tests/test_version_coherence.py
```

Proves the version-coherence check actually detects drift. An expected-zero run against
the vault cannot distinguish a working checker from a blind one — the `MAX_PATH` scanner
failure in GB-2026-028 is the standing lesson, having reported clean while silently
skipping four files. `tests/fixtures/` holds three deliberately-shaped documents (two
drifted, one coherent control) kept **outside the vault** so they are never scanned as
content. The control fixture is versioned `2.10` specifically to catch float comparison.
