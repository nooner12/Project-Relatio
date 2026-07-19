---
title: STD-0002 - Metadata & YAML Standard
document_type: Standards Document
version: 1.7
status: Adopted
operational_status: Active
category:
  - Knowledge Operating System
  - Standards
  - Metadata Architecture
created: 2026-07-09
parent_documents:
  - KOS-0009 Knowledge Representation & Information Architecture Framework
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - STD-0001 Naming & Identification Standard
  - STD-0003 Tagging Standard
  - STD-0004 Linking & Relationship Standard
  - TPL-0001 Formal Document Template
tags:
  - ProjectRelatio
  - Standards
  - Metadata
  - YAML
  - InformationArchitecture
---

# STD-0002

# Project Relatio Metadata & YAML Standard

## Version 1.7

## Adopted Standards Document

---

# 1. Purpose

The Metadata & YAML Standard defines the rules for describing Project Relatio knowledge objects.

Metadata provides structured information about documents, allowing the system to:

- identify documents,
- classify documents,
- establish relationships,
- track lifecycle,
- support future automation.

---

# 2. Standard Principle

Project Relatio adopts:

> Every knowledge object should describe what it is, where it belongs, how it relates, and how it changes over time.

---

# 3. Metadata Architecture

Every formal document consists of two layers:

```
Human Layer

↓

Document Content

↓

Metadata Layer

↓

Machine Interpretation
```

---

# 4. YAML Frontmatter Requirement

All formal Project Relatio documents require YAML frontmatter.

Structure:

```
---
metadata:
---
```

The YAML block must appear at the beginning of the document.

---

# 5. Required Metadata Fields

All formal documents require:

```
---
title:
document_type:
version:
status:
operational_status:
created:
category:
tags:
---
```

---

# 6. Field Definitions

---

# title

Purpose:

Defines the official document name.

Format:

```
title: STD-0002 - Metadata & YAML Standard
```

Rules:

- must match filename,
- must preserve identifier,
- must remain stable.

---

# document_type

Purpose:

Defines the classification of the document.

Approved values:

```
Kernel Operating System Document

Standards Document

Constitutional Instrument

Navigation Document

Architecture Document

Governance Record

Architecture Decision Record

Role Definition

Template

Operations Document

Source Record

Entity Record

Claim Record

Investigation Record

Finding Record

Review Report
```

**Content types** ("Kernel Operating System Document," "Standards Document," "Constitutional Instrument") name a document's substantive class and are layer-specific by nature. **Meta-document types** ("Navigation Document," "Architecture Document," "Governance Record," "Review Report") are deliberately **layer-agnostic** — the same type is reused across the Kernel, Standards, and future layers (e.g. both `Kernel Index` and `Standards Index` are Navigation Documents). This avoids a proliferation of near-duplicate, layer-prefixed types.

Notes:
- "Kernel Operating System Document" and "Constitutional Instrument" were added in v1.1 to match consistent, already-established vault usage.
- "Review Report" was added in v1.2 for the outputs of reviews and audits conducted under STD-0006 (e.g. the Standards Architecture Retrospective).
- v1.3 consolidated the meta-document types: the layer-prefixed values previously in use ("Standards Navigation Document," "Kernel Navigation Document," "Kernel Architecture Document/Manifest," "Kernel Governance Document") were replaced by the three layer-agnostic values above.
- v1.4 added the Knowledge Base content types "Investigation Record" and "Finding Record," defined by KOS-0012 (Knowledge Object Model).
- Draft-era values used only by not-yet-adopted documents ("Foundational Framework," "Operational Framework") remain unapproved pending the Standards Architecture Retrospective.

---

# version

Purpose:

Tracks document maturity.

Format:

```
version: 1.0
```

Uses:

Major.Minor

---

# status

Purpose:

Records a Knowledge Object's **maturity** — its development stage. Lifecycle is governed by STD-0005, which is authoritative.

> **Reconciliation note (v1.5):** STD-0005 defines a **two-dimensional** lifecycle: Maturity (Proposed → Draft → Reviewed → Adopted) and Operational (Active → Superseded → Archived), which are independent. As of v1.5 these are carried in **two fields**: `status` holds **maturity**; `operational_status` (below) holds the operational state. The migration adding `operational_status` across the vault (GB-2026-006) was executed 2026-07-11 — the deferral's trigger (a real supersession/archival event) having occurred. Earlier single-field usage where `status` held an operational value (`Active`/`Archived`/`Superseded`) was migrated: the operational value moved to `operational_status` and `status` was set to the object's maturity.

Approved values (maturity):

```
Proposed

Draft

Reviewed

Adopted
```

(Legacy `Review` reads as `Reviewed`.)

---

# operational_status

Purpose:

Records a Knowledge Object's **operational** state — its current role, independent of maturity (STD-0005 §10–13).

Approved values (operational):

```
Active

Superseded

Archived
```

Rules:

- Required on every formal Knowledge Object alongside `status` (v1.5).
- `Active` — currently in force / in use (this includes Draft-maturity research objects that are in active use; operational state is not gated on adoption in practice, and the vault applies `Superseded`/`Archived` to non-adopted objects — e.g. KOS-0200 — so `operational_status` is carried by all governed objects).
- `Superseded` — replaced by another object; pair with a `superseded_by` relationship (STD-0005 §12).
- `Archived` — retained for reference, no longer operational.

---

# created

Purpose:

Records initial creation date.

Format:

```
created: YYYY-MM-DD
```

Example:

```
created: 2026-07-09
```

---

# updated

Purpose:

Records the most recent modification date.

Recommended:

```
updated: YYYY-MM-DD
```

---

# category

Purpose:

Defines conceptual placement.

Format:

```
category:
  - Knowledge Operating System
  - Standards
```

Rules:

- use controlled terminology,
- avoid unnecessary categories.

---

# tags

Purpose:

Supports discovery and grouping.

Format:

```
tags:
  - ProjectRelatio
  - Standards
```

Rules:

- PascalCase,
- meaningful concepts,
- no filler tags.

---

# 7. Relationship Metadata

Documents may contain:

```
parent_documents:

related_documents:
```

---

## parent_documents

Purpose:

Identifies governing or originating documents.

Example:

```
parent_documents:
  - KOS-0009 Knowledge Representation Framework
```

---

## related_documents

Purpose:

Identifies connected documents.

Example:

```
related_documents:
  - STD-0001 Naming & Identification Standard
```

---

## relationships (typed — v1.6)

Purpose:

Carries **typed** relationships in the frontmatter, so tooling can read a relationship's *meaning*, not merely its existence. This closes the standing gap recorded as Pressure Test **F-4** / **GB-2026-001**: STD-0004 defines a relationship vocabulary that the flat `parent_documents`/`related_documents` lists could not express.

Optional block. Each entry pairs a **type** (drawn from the STD-0004 approved vocabulary) with a **target** (an identifier):

```
relationships:
  - type: derived_from
    target: SRC-0006
  - type: supports
    target: FND-0004
  - type: contrasts_with
    target: CLM-0002
```

Rules:

- `type` must be an approved STD-0004 relationship type (`defines`, `implements`, `extends`, `depends_on`, `derived_from`, `supports`, `contrasts_with`, `supersedes`, `part_of`, `instance_of`, `explains`, `related_to`). Prefer the most specific type (STD-0004 §9).
- `target` is the **identifier** of an existing object (e.g. `SRC-0006`). The Identifier Registry / object title resolves it to a name.
- The block **enriches**, it does not replace, `parent_documents`/`related_documents` (which remain the flat, tooling-read lists and STD-0002-required structure). `graph_integrity.py` reads both: the flat lists for dangling-reference checks, `relationships` for **type-aware** reciprocity.
- Directionality follows STD-0004 §8 — the entry reads *this object* `type` *target*.
- Adopted for **Knowledge Base objects** (INV/CLM/SRC/ENT/FND), where research edges carry semantic weight; other layers may use it where a relationship's type matters.

---

# 8. Optional Governance Metadata

Future-compatible fields:

```
owner:

review_date:

review_cycle:

revision_history:
```

---

# 9. Field Naming Convention

All YAML fields use:

```
lowercase_with_underscores
```

Correct:

```
parent_documents:
```

Incorrect:

```
Parent Documents:
```

Correct:

```
document_type:
```

Incorrect:

```
DocumentType:
```

---

# 10. Date Standard

All dates use:

```
YYYY-MM-DD
```

Example:

```
created: 2026-07-09
```

---

# 11. Document-Specific Metadata

Some document classes require additional fields.

---

## Source Records

May include:

```
source_author:

source_url:

publication_date:
```

---

## Architecture Decision Records

May include:

```
decision_status:

decision_date:
```

---

## Templates

May include:

```
template_type:
```

---

# 12. Metadata Integrity Rules

Metadata must:

- match document content,
- remain current,
- use approved values,
- avoid ambiguity.

Incorrect metadata creates structural errors.

## 12.1 Frontmatter References Are Graph Claims (ADR-GOV-0004 §2 D4)

Entries in **`related_documents`**, **`parent_documents`**, and any typed reference field (the `relationships` block, §7) **must resolve to existing files.** A frontmatter reference is not a note or an intention — it is a **claim that an edge exists in the knowledge graph**, and it is read as such by tooling.

**Named candidates and non-existent objects are referenced in prose only.** A reserved-but-unopened identifier, a planned object, or a candidate follow-on may be discussed freely in an object's body; it may **not** appear in a reference field until the object exists.

*Rationale.* Enforcement already exists — `graph_integrity.py` fails on a dangling reference — but the tool catches the violation only after it is committed. This rule states the constraint at **authoring time**, and states *why* the field is load-bearing: a reference that resolves to nothing silently corrupts the graph the architecture is built on. The occasioning case is recorded in ADR-GOV-0004 §1.4 (a named-but-unopened candidate listed in `related_documents` produced the vault's first dangling reference since GB-2026-005).

---

# 13. Metadata Change Rules

Changes to:

- title,
- document type,
- category,
- status,

require review.

Changes to:

- updated date,
- minor tags,
- relationships,

may occur during maintenance.

---

# 14. Example Complete Metadata Block

```
---
title: Example Document
document_type: Standards Document
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Operating System
  - Standards
parent_documents:
  - KOS-0009 Knowledge Representation Framework
related_documents:
  - STD-0001 Naming & Identification Standard
tags:
  - ProjectRelatio
  - Example
---
```

---

# 15. Relationship to Future Templates

All future templates must implement this standard.

Templates provide:

- convenience,
- consistency,
- reduced error.

STD-0002 provides:

- authority.

---

# 16. Governance

STD-0002 is maintained under:

KOS-0011 — Governance, Stewardship & Evolution Framework.

Changes require:

- documentation,
- review,
- version update.

---

# 17. Closing Principle

Project Relatio adopts:

> Metadata is the structural memory of the knowledge system.

---

# 18. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial metadata and YAML standard|
|1.1|2026-07-09|Adopted|Widened approved document_type values to include Kernel Operating System Document, Standards Navigation Document, and Constitutional Instrument, matching documented vault usage found during the pre-STD-0006 Architecture Status Note audit|
|1.2|2026-07-09|Adopted|Added "Review Report" document_type for STD-0006 review/audit outputs; added a status-field reconciliation note deferring to STD-0005's two-dimensional lifecycle model|
|1.3|2026-07-09|Adopted|Consolidated meta-document types: replaced layer-prefixed values (Standards/Kernel Navigation Document, Kernel Architecture Document/Manifest, Kernel Governance Document) with layer-agnostic Navigation Document, Architecture Document, and Governance Record; documented the content-type vs meta-type distinction|
|1.4|2026-07-09|Adopted|Added Investigation Record and Finding Record document_types, defined by KOS-0012 and demonstrated needed by the RQ-0001 pressure test|
|1.5|2026-07-11|Adopted|Implemented STD-0005's two-dimensional lifecycle in metadata (GB-2026-006): `status` narrowed to **maturity** (Proposed/Draft/Reviewed/Adopted); added the required **`operational_status`** field (Active/Superseded/Archived). Migrated the vault — operational values previously held in `status` moved to the new field. Trigger: the KOS-0200/ROLE-0003 supersession/archival events the deferral was waiting on.|
|1.6|2026-07-11|Adopted|Added the optional **typed `relationships`** frontmatter block (`type` + `target`), closing Pressure Test F-4 / GB-2026-001 — STD-0004's vocabulary can now be expressed in metadata, not only prose. Additive: the flat `parent_documents`/`related_documents` lists are retained for tooling. Adopted for Knowledge Base objects; `graph_integrity.py` made type-aware.|
|1.7|2026-07-20|Adopted|Added **§12.1 Frontmatter References Are Graph Claims**, enacting **ADR-GOV-0004 §2 D4**. Entries in `related_documents`, `parent_documents`, and the typed `relationships` block must resolve to existing files; named candidates and non-existent objects are referenced in **prose only**. Placed here rather than in STD-0004 because D4 governs what the frontmatter *fields* must contain (STD-0002's domain), whereas STD-0004 governs which relationship *types* exist and what they mean. Additive rule statement only — no field added, removed, or redefined, and no existing requirement changed; `graph_integrity.py` already enforced the constraint after commit, and this states it at authoring time with its rationale.|

---

# End STD-0002