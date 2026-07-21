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
- **Dangling references** — any `parent_documents` / `related_documents` entry, any
  typed `relationships:` target, or any `bounded_by` entry inside a `confidence`
  component (STD-0002 §11 v1.9 / STD-0009 §9), that resolves to no existing object.
  Exit code 1 if any exist (reliability-critical). `bounded_by` entries are graph
  claims like any other reference; zero exist at introduction (ADR-GOV-0008 D5, no
  retroactive backfill), and detection is proven by `tests/test_bounded_by.py`.
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

The validator also shape-checks two Claim/Finding field families at **error** level:
the **epistemic fields** (`confidence` list + `reliance_tier`; STD-0008 / STD-0002 §11,
GB-2026-038 migration complete) and the **review fields** (`review_cycle`, `review_date`,
`last_reviewed`; STD-0009 §8 / STD-0002 §11 v1.9). The review check enforces the
arithmetic `review_date == last_reviewed + review_cycle months`; a divergence means one
of the three is stale (the review-field analogue of version incoherence). Both check
*shape*, never whether a grade or cadence is *correct* — that is review-act judgment.

## review_queue.py — the Review & Revision queue (STD-0009 §10)

```
python review_queue.py
```

**Read-only.** Runs the STD-0009 §4 trigger detections against the vault and emits the
current review queue (also written to `output/review_queue.md`): one row per surfaced
item — **object · trigger · resolved scope · prescribed act**, exactly per the
STD-0009 §4/§5 tables. The queue **PROPOSES**; it never writes to any record
(ADR-GOV-0008 D6). Every act runs through a governed session, never the tool. **Do not
hand-audit records for staleness — run the queue.**

v1 detections: `time_decay` (review_date ≤ today → Light re-affirmation),
`source_superseded` (a Superseded object in a record's `derived_from` or a component's
`bounded_by` → Targeted re-grade), `upstream_grade_change` (a bounded object with a
confidence change in its history **dated after** the dependent's `last_reviewed` →
Targeted re-grade), and two recorded-flag triggers, `contradiction` (→ Full OPS-0003
circuit) and `field_prose_divergence` (→ Reconciliation).

**MARKER CONVENTION (recorded flags).** A contradiction or a field/prose divergence is
a *judgment*, not something the graph shows, so it enters the queue via an explicit flag
line in the **Governance Backlog**:

```
REVIEW-FLAG | trigger=<contradiction|field_prose_divergence> | object=<ID> | scope=<free text>
```

Leading Markdown list/quote punctuation and surrounding whitespace are ignored; one flag
per line. The marker is deliberately explicit so ordinary Backlog prose that merely
*mentions* a contradiction does **not** enter the queue — in particular the
CLM-0043/0046/0050 borderline-split Backlog item is **not** a flag and must not be written
as one. Reflexive structural recommendations (ADR-GOV-0007) will enter the same queue via
the same marker once the reflexive process graduates (STD-0009 §10); v1 ships only the two
flag triggers above, so no act type beyond the STD-0009 §5 table is invented.

Expected live output at introduction: **empty** — all `review_date`s were just
initialized months out, no source is Superseded, no upstream grade change postdates any
`last_reviewed`, and no flags are recorded. `tests/test_review_queue.py` drives synthetic
inputs through the pure `detect()` core to prove every trigger fires with its correct act
(and that the near-miss cases — a future review_date, an upstream change *predating*
last_reviewed — do not).

## build_view.py — the vault visualizer (regenerating snapshot)

```
python build_view.py        # regenerate ../views/relatio-view.html
```

**Read-only. Frontmatter-only.** Reads the YAML frontmatter of every Knowledge Base
object (INV/CLM/SRC/ENT/FND) and emits ONE self-contained interactive HTML file,
`views/relatio-view.html` (a new top-level directory beside `tools/`). It NEVER parses
body prose for a datum, NEVER writes to any record, and adds NO new fields. Where a
datum is absent from frontmatter the node says so ("not fielded") — it is never inferred.

The file is **self-contained** (all CSS/JS inline, no external/CDN dependencies — it
renders from a double-click, offline) and **committed**, so it is viewable/shareable
directly from the public repo. It carries a **generated-from header** (git short hash +
generation date) so a stale copy identifies itself. Output is **deterministic** (every
list id-sorted); only the header hash/date vary, so regeneration diffs are meaningful.

**The reliance gate is load-bearing and MUST NOT be removed from the generator.** A
standing banner ("Findings not cleared for external reliance — reliance tiers shown per
node") sits atop the artifact; an R0/R1/R2 badge is on **every** CLM/FND node; each
badge's detail carries the `reliance_note` and what promotion would require (R1:
retrieval verification per ADR-GOV-0006; R2: an independent channel); reference chips to
a CLM/FND carry a reliance mini-badge. No view, filter, or search path strips it. The
self-check in `main()` fails the run if the reliance-badge count ≠ the CLM/FND count.

Structure — the tree spine is INV → its `part_of` claims/findings/sources → each
claim/finding's `derived_from` targets (rendered as reference chips). Every object is a
canonical node **exactly once** (node count == KB object count); derivation and the
cross-edges (`contrasts_with` / `depends_on` / `supports` / `related_to`, beyond the
spine) are chips/badges pointing at those canonical nodes, never duplicate full nodes.
Sources attach to an INV by `part_of`, or by the sole INV in their relationships/
`related_documents` when exactly one is referenced (no cross-investigation ambiguity
exists in the vault); sources with no INV signal, and the KB-shared **entities**, render
in a "Shared & Cross-Investigation" group. A split-`confidence` record renders every
component separately (never merged or averaged); a past-due `review_date` gets a visual
marker, making the view a second review-queue surface. A search box filters by identifier
or title and expands matches.

**Closure state is NOT prose-parsed (a deliberate limitation).** An investigation's
closed/open state lives in its banner + history row (prose), not in frontmatter — and
closed INVs keep `status: Draft` by design. So INV nodes are labelled by their honest
frontmatter `status` / `operational_status` only; the view does not claim to show which
investigations are "closed."

`views/` sits **outside the KOS numbering and lifecycle** — it is a generated artifact,
same category as CLAUDE.md, not a Knowledge Object. **Never hand-edit the output;
regenerate it.** The validators ignore it (it lives outside the vault dir and holds no
markdown). `tests/test_build_view.py` drives fixtures through the real parse+render path
to prove split/single confidence, cross-edges, the past-due marker, the reliance badge on
every leaf, the banner, version-as-literal-text, determinism, and — against the live
vault — that the deepest-path record is read and rendered (the STD-0001 §8 check).

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
