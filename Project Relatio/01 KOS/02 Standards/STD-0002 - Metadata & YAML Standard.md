---
title: STD-0002 - Metadata & YAML Standard
document_type: Standards Document
version: 1.4
status: Adopted
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

## Version 1.4

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

Defines lifecycle position.

> **Reconciliation note (v1.2):** STD-0005 — Lifecycle & Revision Standard is authoritative on lifecycle and defines a two-dimensional model (Maturity: Proposed → Draft → Reviewed → Adopted; Operational: Active → Superseded → Archived). The single `status` field described here currently holds a document's **maturity** state. Whether a separate operational field (e.g. `operational_status`) is added across the vault is a pending migration decision recorded in the Standards Architecture Retrospective. Until that decision, use the values below, reading "Review" as "Reviewed" and preferring "Superseded" over "Deprecated" per STD-0005.

Approved values:

```
Draft

Review

Adopted

Active

Deprecated

Archived
```

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

---

# End STD-0002