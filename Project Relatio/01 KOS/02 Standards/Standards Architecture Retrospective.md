---
title: Standards Architecture Retrospective
document_type: Review Report
version: 1.4
status: Adopted
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Operating System
  - Standards
  - Review
parent_documents:
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - STD-0006 Review & Validation Standard
related_documents:
  - STD-0001 Naming & Identification Standard
  - STD-0002 Metadata & YAML Standard
  - STD-0003 Classification & Discovery Standard
  - STD-0004 Relationship & Linking Standard
  - STD-0005 Lifecycle & Revision Standard
  - STD-0007 Terminology & Semantic Stewardship Standard
  - Standards Index
tags:
  - ProjectRelatio
  - Standards
  - Review
  - Retrospective
  - Migration
---

# Standards Architecture Retrospective

## Version 1.4

## Adopted Review Report

---

# 1. Purpose

This Retrospective is the first periodic audit conducted under STD-0006 §4.4. It reviews the completed Standards layer (STD-0001 through STD-0007) as a whole: its dependency structure, internal consistency, integration state, and outstanding migration needs.

It is a **Review Report**, not a Standard. It does not create or change any rule. It records findings, states which were resolved during this pass, and registers the decisions that still require Brian's explicit approval before execution.

---

# 2. Scope

In scope:

- the seven adopted Standards and the Standards Index,
- their metadata, naming, and cross-references,
- consistency between Standards and the adopted decisions in CLAUDE.md and STD-0005.

Out of scope (noted, not resolved here):

- Kernel document content,
- the Roles, Templates, and Operations layers beyond their effect on the Standards layer,
- remediation of any specific document, which happens only under a governed migration Brian approves.

---

# 3. Standards Layer — As-Built State

All seven Standards are Adopted as of 2026-07-09.

|ID|Title|Version|Status|
|---|---|---|---|
|STD-0001|Naming & Identification Standard|1.1|Adopted|
|STD-0002|Metadata & YAML Standard|1.2|Adopted|
|STD-0003|Classification & Discovery Standard|1.0|Adopted|
|STD-0004|Relationship & Linking Standard|1.0|Adopted|
|STD-0005|Lifecycle & Revision Standard|1.0|Adopted|
|STD-0006|Review & Validation Standard|1.0|Adopted|
|STD-0007|Terminology & Semantic Stewardship Standard|1.0|Adopted|

---

# 4. Dependency Structure

Declared `parent_documents` / `related_documents` across the Standards layer resolve to this dependency picture (A → B means "A depends on / is governed by B"):

```
STD-0001  →  KOS-0001, KOS-0009, KOS-0011
STD-0002  →  KOS-0009, KOS-0011
STD-0003  →  KOS-0009, STD-0001, STD-0002
STD-0004  →  KOS-0009, STD-0007, STD-0003
STD-0005  →  KOS-0011, STD-0001, STD-0004
STD-0006  →  KOS-0011, KOS-0009, STD-0005
STD-0007  →  KOS-0009, KOS-0011, STD-0003
```

Observations:

- The layer is acyclic — no circular dependencies. Good.
- Every Standard roots into the Kernel (KOS-0009 Knowledge Representation and/or KOS-0011 Governance), as intended.
- STD-0006 sits correctly at the top of the practical chain: it depends on STD-0005 and verifies all the others without being depended upon by them.
- **Ordering vs. dependency mismatch (cosmetic):** STD-0004 depends on STD-0007, but STD-0007 has a higher number. Numeric order is not dependency order. This is acceptable under STD-0001 (numbers are identifiers, not sequence), but worth noting so no one assumes the numbering implies build order.

---

# 5. Consistency Findings

## 5.1 Resolved in this pass

| # | Finding | Resolution |
|---|---|---|
| C-1 | Versioning conflict: STD-0001 §11 declared `Major.Minor`; STD-0005 §16 declared `Major.Minor.Patch`. | STD-0001 → v1.1: added a non-destructive note making STD-0005 authoritative on versioning. |
| C-2 | Lifecycle vocabulary conflict: STD-0001/0002 used a single linear status chain (…Review…Deprecated…); STD-0005 + CLAUDE.md use a two-dimensional model (Maturity + Operational) with "Reviewed" and "Superseded". | STD-0001 → v1.1 and STD-0002 → v1.2: added notes deferring to STD-0005; "Review"→"Reviewed", "Deprecated" retired in favor of "Superseded". Field-level migration deferred (see M-1). |
| C-3 | `document_type` values in use vault-wide were absent from STD-0002's approved list. | STD-0002 → v1.1: widened the list to match consistent usage (Kernel Operating System Document, Constitutional Instrument, Standards Navigation Document); → v1.2 added Review Report. |
| C-4 | Standards Index registry was stale (listed STD-0002 as "Planned"; planned sequence didn't match the build). | Standards Index → v1.1: registry refreshed to all-Adopted; plan-vs-actual divergence documented; dangling "KOS Architecture Manifest" parent reference removed. |
| C-5 | Corrupted YAML in archived KOS-0002 (invalid `status`, duplicated block outside frontmatter). | Frontmatter rewritten to valid YAML. |
| C-6 | KOS-0011 filename typo ("Framewor"). | File renamed to match its `title`. |

## 5.2 Open — require decision (see Migration Register, Section 7)

| # | Finding |
|---|---|
| C-7 | The two-dimensional lifecycle model is declared but **not implemented**: no document carries both a maturity and an operational field. Every document has a single `status`. |
| C-8 | KOS-0003 (Epistemic Framework) is a v0.1 **Draft** dated 2026-07-08, carries pre-standard fields (`owner`, `architect`), yet is cited as a `parent_document`/`related_document` by KOS-0001 and most of the Kernel as though Adopted. It also cites a superseded KOS-0002 and mis-titles KOS-0001. |
| C-9 | **Phantom references:** ADR-KOS-0001 through ADR-KOS-0010 are cited (KOS-0003 dependencies; KOS-0011 related_documents) but the `01 Architectural Decisions` folder is empty — no ADR exists. |
| C-10 | ~~**Roles layer non-conformance:** no `ROLE-NNNN` identifiers exist (STD-0001 §5 defines the class). KOS-0100 uses a KOS prefix and has no frontmatter; 0101/0102 are empty files.~~ **RESOLVED (M-4):** ROLE-NNNN adopted; files migrated to ROLE-0001/0002/0003 with conformant Draft frontmatter and a shared skeleton. Substance authoring remains the step-4 build. |
| C-11 | Draft-era `document_type` values ("Foundational Framework", "Operational Framework") remain on KOS-0002/0003/0200 and are still not on STD-0002's approved list. |
| C-12 | **Audit-coverage gap (this report).** Four Adopted Kernel meta-documents — `KOS Architecture Manifest`, `Kernel Index`, `KOS Dependency Map`, `Kernel Status` — sit directly in `01 Kernel/` and were missed by the initial survey's file discovery. They use `document_type` values not on STD-0002's approved list (`Kernel Architecture Manifest`, `Kernel Navigation Document`, `Kernel Architecture Document`, `Kernel Governance Document`). Consequence: the priority step-3 integration documents (KOS Index, KOS Dependency Map, Architecture Status Note) **substantially already exist at Kernel scope** and should be extended/reconciled, not built from scratch. |
| C-13 | **VOID — correction.** This finding originally claimed `KOS Architecture Manifest` was a non-existent (phantom) reference. That was wrong: the Manifest exists at `01 Kernel/KOS Architecture Manifest.md` and is Adopted. The error was a consequence of the same incomplete file discovery as C-12. An earlier edit in this pass that removed the Manifest reference from the Standards Index has been reverted. No phantom manifest exists; the only confirmed phantom references are the ADRs (C-9). |

---

# 6. Integration State

- **CLAUDE.md** updated: KOS-0004 correction applied; STD-0006 marked Adopted; priority order updated with the open items above.
- **Standards Index** updated to v1.1 and now reflects reality.
- **STD cross-references** among the seven Standards all resolve to existing files (verified). No dangling references remain *within* the Standards layer.
- Dangling references remain **outside** the Standards layer (C-8, C-9) and are registered below.

---

# 7. Migration Register

Each item below is a batch migration. Per CLAUDE.md ("No spontaneous restructuring… Batch migrations; never rename incrementally" and "Propose, then execute"), none will be executed until Brian approves the specific plan.

---

## M-1 — Implement the two-dimensional lifecycle (addresses C-7)

**Problem:** CLAUDE.md and STD-0005 mandate independent Maturity and Operational states; documents carry only one `status`.

**Options:**
- **(a) Two fields** — add `operational_status` (Active/Superseded/Archived) alongside `status` (used for maturity). Most faithful to the adopted model; touches ~24 files.
- **(b) Single field, documented convention** — keep one `status`, define precedence rules (operational overrides maturity once Active). Less faithful; amends STD-0002/0005 instead of files.
- **(c) Defer** — leave as-is until real research content exercises the need (honors "formalize only on demonstrated need").

**Recommendation:** (c) defer, then (a) when first needed. No document currently needs an operational state distinct from its maturity; forcing the field now is over-architecture. Revisit at first supersession event.

**Scope if executed (a):** all formal documents in `00 Constitution`, `01 Kernel`, `02 Standards`.

---

## M-2 — Resolve KOS-0003's status (addresses C-8)

**Problem:** A load-bearing document is a stale Draft cited as if Adopted.

**Options:**
- **(a) Upgrade** KOS-0003 to Adopted: bring its frontmatter to current schema, fix its stale references (KOS-0002→KOS-0004; correct KOS-0001 title), drop non-existent ADR dependencies. Kernel content change → governed review.
- **(b) Downgrade the citations** — if KOS-0003 is genuinely not ready, mark the citing documents' references as "(Draft)" and stop treating it as authoritative.

**Recommendation:** (a). KOS-0003 is referenced as foundational by KOS-0001, 0005–0010; the architecture already leans on it. Formalize what is already true, under a governed review pass.

**Scope if executed (a):** KOS-0003 (frontmatter + reference fixes). No changes to citing documents required.

---

## M-3 — Resolve phantom ADR references (addresses C-9)

**Problem:** ADR-KOS-0001…0010 are cited but do not exist.

**Options:**
- **(a) Remove/reword** the dangling references in KOS-0003 and KOS-0011.
- **(b) Create** the ADRs. **Rejected** — creating 10 placeholder ADRs is textbook over-architecture (Risk 1); CLAUDE.md already defers the ADR/Architecture-Discovery work.

**Recommendation:** (a). Remove the phantom `dependencies`/`related_documents` entries; if a real decision needs recording later, create that one ADR then, on demonstrated need.

**Scope if executed (a):** KOS-0003 (frontmatter), KOS-0011 (frontmatter). Batch with M-2 since both touch KOS-0003.

---

## M-4 — Roles layer conformance (addresses C-10) — belongs to Priority Step 4

**Problem:** Roles use no `ROLE-` identifiers; role files are empty or frontmatter-less.

**Note:** This is not a cleanup migration but the actual **build** of the Roles layer (priority step 4). It requires a prior decision: do role definitions use the `ROLE-NNNN` class (STD-0001 §5) or the existing `KOS-01xx` numbering? Recommend deciding identifier scheme first, then authoring role definitions to standard. Deferred to step 4; flagged here for completeness.

---

## M-5 — Draft-era document_type cleanup (addresses C-11)

**Problem:** "Foundational Framework"/"Operational Framework" persist on KOS-0002 (Superseded), KOS-0003 (Draft), KOS-0200 (Draft).

**Recommendation:** Fold into M-2 for KOS-0003 (retype to "Kernel Operating System Document" on adoption). Leave KOS-0002 as-is (it is Superseded/archived — historical record, per STD-0005 §22). Decide KOS-0200's fate separately (it appears to duplicate the Standards Index's purpose — candidate for supersession).

---

# 7.6 Decision Log (Brian, 2026-07-09)

| Item | Decision | Execution |
|---|---|---|
| M-1 (two-dimensional lifecycle) | **Defer until first needed.** | No changes made. Revisit at first supersession event. |
| M-2 (KOS-0003 status) | **Upgrade to Adopted.** | Executed 2026-07-09: KOS-0003 brought to current schema, stale references fixed (KOS-0001 title; KOS-0002→KOS-0004), retyped, adopted as v1.0. C-8 resolved. |
| M-3 (phantom ADR references) | **Leave for later.** | Not executed. ADR-KOS-0001…0008 references retained in KOS-0003 `related_documents`; ADR-KOS-0010 retained in KOS-0011. C-9 remains open, to be handled in a future Kernel review pass. |
| M-4 (Roles layer) | **Adopt ROLE-NNNN** (per STD-0001 §5) as the identifier scheme — chosen for cleanest upstream layer development. | Executed 2026-07-09: KOS-0100→ROLE-0001, 0101→ROLE-0002, 0102→ROLE-0003; folder flattened; conformant Draft frontmatter + shared skeleton added; stale KOS-0100 reference in STD-0006 updated. C-10 resolved. Role *substance* authoring remains the step-4 build. |
| M-5 (draft-era document_type) | Partially addressed via M-2 (KOS-0003 retyped). | KOS-0002 left as Superseded/historical; **KOS-0200 superseded & archived 2026-07-11 (GB-2026-007)** — never adopted; superseded by STD-0001…0007. |

---

# 8. Recommended Next Actions

In priority order, matching CLAUDE.md:

1. **Brian's decisions** on M-1 (recommend defer), M-2 (recommend upgrade KOS-0003), M-3 (recommend remove phantom refs). M-2+M-3 can execute as one batch touching KOS-0003 and KOS-0011.
2. **Integration documents (priority step 3) — mostly already exist (see C-12).** `Kernel Index`, `KOS Dependency Map`, and `Kernel Status` are Adopted and cover the Kernel. Remaining work is *extension and reconciliation*, not fresh authoring: (a) decide whether these are renamed/rescoped from "Kernel …" to whole-KOS scope (they omit the Standards layer entirely); (b) resolve their non-approved `document_type` values (C-12). This Retrospective serves as the Architecture Status Note for the Standards layer; `Kernel Status` is its counterpart for the Kernel.
3. **Roles layer (step 4):** identifier scheme decided (ROLE-NNNN) and skeletons migrated; **author the role substance** (identity, mission, responsibilities, authority, boundaries) — ideally informed by real workflow experience rather than speculatively.
4. **Templates, then Operations (step 5).**
5. **Real research workflows (step 6)** — the true test of the architecture.

---

# 9. Closing Assessment

The Standards layer is structurally sound: acyclic dependencies, complete coverage, and — after this pass — internally consistent and honestly documented. The remaining issues are concentrated in the **Kernel's early drafts** (KOS-0003) and **phantom scaffolding** (ADRs, empty role stubs) left from the pre-standards period, not in the Standards themselves.

The single most important discipline going forward, per CLAUDE.md: **bias toward step 6.** The architecture has still never processed real research content. Further polishing of the scaffolding has sharply diminishing returns compared to running one real research workflow through it.

---

# 10. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial Standards Architecture Retrospective; first STD-0006 §4.4 periodic audit|
|1.1|2026-07-09|Adopted|Added §7.6 Decision Log recording Brian's M-1/M-2/M-3 decisions; M-2 executed (KOS-0003 adopted), C-8 resolved|
|1.2|2026-07-09|Adopted|Recorded audit-coverage gap: three Kernel meta-documents (Kernel Index, KOS Dependency Map, Kernel Status) were missed in the initial survey (C-12); added second phantom-reference finding for KOS Architecture Manifest (C-13); corrected step-3 next-actions to reflect that integration documents largely already exist|
|1.3|2026-07-09|Adopted|Correction: KOS Architecture Manifest was found to exist (a fourth missed meta-document, not a phantom); C-13 voided; C-12 updated to four documents; the erroneous removal of the Manifest reference from the Standards Index was reverted|
|1.4|2026-07-09|Adopted|Recorded Brian's decisions and their execution: document_type consolidation (STD-0002 v1.3); Standards-layer siblings created (Standards Dependency Map, Standards Status); M-4 ROLE-NNNN scheme adopted and Roles files migrated (C-10 resolved)|

---

# End Standards Architecture Retrospective
