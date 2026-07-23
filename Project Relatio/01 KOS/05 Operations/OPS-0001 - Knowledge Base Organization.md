---
title: OPS-0001 - Knowledge Base Organization
document_type: Operations Document
version: 1.1
status: Adopted
operational_status: Active
created: 2026-07-09
parent_documents:
  - KOS-0012 Knowledge Object Model
  - STD-0003 Classification & Discovery Standard
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - OPS-0002 Relationship Integrity & Graph Maintenance
  - Identifier Registry
  - Third-Run Assessment - RQ-0003
tags:
  - ProjectRelatio
  - Operations
  - KnowledgeBase
  - Organization
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# OPS-0001

# Knowledge Base Organization

## Version 1.1
## Adopted Operations Document

---

# 1. Purpose

This document defines **where each kind of Knowledge Object lives** inside `06 Knowledge Base/`. It resolves the organization gap surfaced by the first three research workflows (Pressure Test Report F-7; Third-Run Assessment F-11): investigation-per-folder placement broke down as soon as objects (Entities, Sources) were shared across investigations.

Folders are classification only (CLAUDE.md non-negotiable #4); this convention aids discovery and does not define the knowledge graph, which lives in relationships (OPS-0002).

---

# 2. Principle

> An object lives with what **owns** it. Objects owned by a single investigation live in that investigation's folder; objects shared across investigations live in a shared folder.

Ownership test: *if this object were only meaningful inside one investigation, it is investigation-scoped; if it is (or could be) cited by others, it is shared.*

---

# 3. Placement Convention

```
06 Knowledge Base/
├── INV-NNNN - <Title>/          ← one folder per investigation
│   ├── INV-NNNN - <Title>.md         (the investigation record)
│   ├── CLM-NNNN - <…>.md             (claims made in it)
│   ├── FND-NNNN - <…>.md             (findings it produces)
│   └── <Assessment/Report>.md        (its review artifacts)
│
├── Sources/                      ← ALL Source records (shared reference library)
│   └── SRC-NNNN - <…>.md
│
└── Entities/                     ← ALL Entity records (concepts are cross-cutting)
    └── ENT-NNNN - <…>.md
```

**Rationale by type:**
- **INV, FND, and investigation review reports** are investigation-scoped — they belong to one inquiry.
- **CLM (Claims)** are investigation-scoped by default (a claim is made *within* an inquiry). A claim reused across investigations may be promoted to a shared location later; none yet require it.
- **SRC (Sources)** are **always shared.** A source is a reference; any future investigation may cite it. Placing sources in a common library prevents duplication (the reuse problem seen when INV-0003 reused SRC-0002).
- **ENT (Entities)** are **always shared.** A concept/entity (e.g. *wu wei*) is inherently cross-investigation.

---

# 4. Migration Applied (2026-07-09)

To bring the existing KB into line with this convention:
- `Entities/` was created for ENT-0001 (Wu Wei), ENT-0002 (Ziran).
- `Sources/` was created and **SRC-0001 … SRC-0005 were moved into it** from their original investigation folders. (Safe: all source references are name-based, not path-based — verified before moving.)

Investigation folders now contain only investigation-scoped objects (INV, CLM, FND, reports).

---

# 5. Naming

Object files follow STD-0001 (`IDENTIFIER - Title`). Folder names follow `INV-NNNN - <Title>`. The shared folders `Sources/` and `Entities/` are descriptive (like `00 Standards Index`) and carry no identifier.

---

# 6. Relationship to Standards & Registry

- Classification and discovery follow **STD-0003**.
- Identifiers follow **STD-0001** and are inventoried in the **Identifier Registry**.
- This convention is verified under **STD-0006** (a misplaced object is a non-conformance finding, not an error to fix reactively).

---

# 7. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial KB organization convention; resolves F-7/F-11; sources and entities moved to shared folders|
|1.1|2026-07-22|Adopted|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End OPS-0001
