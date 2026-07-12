---
title: KOS-0012 - Knowledge Object Model
document_type: Kernel Operating System Document
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-09
parent_documents:
  - KOS-0009 Knowledge Representation & Information Architecture Framework
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - STD-0001 Naming & Identification Standard
  - STD-0002 Metadata & YAML Standard
  - STD-0004 Relationship & Linking Standard
  - KOS-0008 Research Methodology & Investigation Framework
  - Pressure Test Report - RQ-0001
tags:
  - ProjectRelatio
  - KOS
  - KnowledgeObject
  - ObjectModel
  - KnowledgeArchitecture
---

# KOS-0012

# Project Relatio Knowledge Object Model

## Version 1.0

## Adopted Kernel Document

---

# 1. Purpose

The Knowledge Object is the primary architectural abstraction of Project Relatio (per CON-0002 and the KOS Architecture Manifest). Until now it has been named but never formally modeled: STD-0001 §5 enumerates identifier *classes* in one line each, and KOS-0003 §12 specifies the *content* of a claim, but no document defines what a Knowledge Object **is**, what types exist, or what each type must contain.

This document supplies that model. It was authored on **demonstrated need**: the first real research workflow (the RQ-0001 pressure test) could not be represented conformantly — it required an investigation container and a finding object that no type covered, and it exposed that the metadata rules (STD-0002) and the epistemic content rules (KOS-0003 §12) were never reconciled. KOS-0012 closes those gaps.

This document defines the abstract model (RKA). Its Obsidian implementation — templates, plugins, query mechanics (RRI) — lives in the Templates and Operations layers.

---

# 2. Definition

> A **Knowledge Object** is a governed, individually identified unit of the knowledge architecture that carries both a description of itself (metadata) and a structured body of meaning (content), and that participates in the knowledge graph through explicit relationships.

Three properties are essential:

- **Identified** — it has a unique identifier (STD-0001).
- **Described** — it carries conformant metadata (STD-0002).
- **Related** — it connects to other objects through meaningful relationships (STD-0004).

A file without all three is not yet a Knowledge Object; it is a draft toward one.

---

# 3. The Two Layers

Every Knowledge Object consists of two layers. This is the reconciliation the pressure test showed was missing (F-6).

```
METADATA LAYER   (frontmatter)   → governed by STD-0002   → UNIVERSAL across all types
        +
CONTENT LAYER    (body)          → governed by KOS-0012    → TYPE-SPECIFIC structure
```

- The **Metadata Layer** is the same schema for every object: the STD-0002 required fields (`title`, `document_type`, `version`, `status`, `created`, `category`, `tags`) plus optional relationship and governance fields.
- The **Content Layer** differs by type. KOS-0012 §5 defines the required content structure for each research object type. Where an existing Kernel document already specifies a content structure (notably KOS-0003 §12 for Claims), KOS-0012 **delegates** to it rather than restating it.

**Rule:** A conformant Knowledge Object must satisfy *both* layers — the universal metadata schema and its type's content structure. Neither STD-0002 nor KOS-0003 alone is sufficient.

---

# 4. Object Typology

The complete set of Knowledge Object types. Identifiers are governed by STD-0001 §5; document_type values by STD-0002 §6. "Content authority" names the document that defines the type's required content structure.

| Class | document_type | Layer | Purpose | Content authority |
|---|---|---|---|---|
| KOS | Kernel Operating System Document | Kernel | Foundational architecture | the document itself |
| STD | Standards Document | Standards | Repeatable rules | the document itself |
| ADR | Architecture Decision Record | any | Significant decisions | STD-0002 §11 |
| ROLE | Role Definition | Roles | Responsibility & authority | KOS-0012 (future) |
| TPL | Template | Templates | Reusable structures | KOS-0012 §5 (mirrors target type) |
| OPS | Operations Document | Operations | Workflows | KOS-0012 (future) |
| **INV** | **Investigation Record** | Knowledge Base | A research question, its method, and synthesis | **KOS-0012 §5.1** |
| **FND** | **Finding Record** | Knowledge Base | A synthesized answer/conclusion | **KOS-0012 §5.2** |
| CLM | Claim Record | Knowledge Base | An evaluated assertion | KOS-0003 §12 |
| SRC | Source Record | Knowledge Base | A reference/origin and its evaluation | KOS-0012 §5.4 (uses KOS-0003 §6) |
| ENT | Entity Record | Knowledge Base | An identifiable entity/concept | KOS-0012 §5.5 (uses KOS-0004) |

**INV** and **FND** are introduced by this document (see §6). All other classes pre-existed in STD-0001 §5; KOS-0012 only supplies their content authority.

---

# 5. Research Object Content Structures

The required content (body) structure for each Knowledge Base object type. These are minimums; objects may add sections.

## 5.1 Investigation Record (INV)

1. Research Question (original + refined, with rationale)
2. Scope & Disambiguation
3. Method (which frameworks/pipeline)
4. Findings / Synthesis (or reference to FND records)
5. Confidence Summary (per KOS-0003 §8)
6. Assumptions & Bracketing (per KOS-0003 §10)
7. Relationships (per STD-0004)

## 5.2 Finding Record (FND)

1. Statement (the finding, as a single proposition)
2. Supporting Claims (references to CLM records)
3. Confidence (per KOS-0003 §8)
4. Scope & Limitations
5. Relationships (per STD-0004)

## 5.3 Claim Record (CLM)

Delegated in full to **KOS-0003 §12** (Knowledge Entry Requirements): Claim, Claim Type, Evidence, Source Evaluation, Assumptions, Reasoning, Confidence, Limitations, Alternative Interpretations, Relationships. KOS-0012 adds only that a Claim record must also carry the STD-0002 metadata layer.

## 5.4 Source Record (SRC)

1. Identification
2. Source Evaluation (per KOS-0003 §6: authority, transparency, independence, intent)
3. Limitations (what the source does not establish)
4. Key Content / Passages Used
5. Relationships (per STD-0004)

## 5.5 Entity Record (ENT)

1. Identification
2. Definition
3. Classification (per KOS-0004 entity categories)
4. Relationships (per STD-0004)

---

# 6. New Types Introduced

## 6.1 Investigation Record (INV)

Rationale: the pressure test (F-1) had no object to hold a research question, its scope/method, and its synthesis; the container was created provisionally as `INV-0001`. KOS-0012 formalizes **INV** as an identifier class and **Investigation Record** as a document_type. An Investigation is the *unit of inquiry* — it frames Claims and Sources and produces Findings.

## 6.2 Finding Record (FND)

Rationale: the pressure test (F-2) had to fold the synthesized answer into the Investigation record because no Finding object existed. KOS-0012 formalizes **FND** / **Finding Record** so a conclusion can be a first-class, individually-citable, confidence-rated object, distinct from both the Investigation that produced it and the Claims that support it.

Both additions are integrated into STD-0001 §5 and STD-0002 §6 (see Integration, §8).

---

# 7. Object Lifecycle & Relationships

- Knowledge Objects carry lifecycle state per **STD-0005** (Maturity + Operational). Research objects typically begin at `Draft` and mature as evidence and review accrue.
- Objects connect through the **STD-0004** relationship vocabulary. A typical investigation graph:

```
INV  ──derived_from──▶  SRC (sources)
 │
 ├──part_of◀── CLM (claims)   CLM ──contrasts_with/related_to──▶ CLM
 │
 └──produces──▶ FND (findings)   FND ──derived_from──▶ CLM
```

("produces" is used descriptively here; if a formal relation is wanted, `part_of`/`derived_from` from STD-0004 already cover it.)

---

# 8. Reconciliation with the Standards (resolves F-6)

- **STD-0001** governs the *identifier* of every object (this document adds INV, FND to §5).
- **STD-0002** governs the *metadata layer* of every object (this document adds Investigation Record, Finding Record to §6).
- **KOS-0003 §12** governs the *content* of Claim records; KOS-0012 §5 governs the content of the other research objects.
- **KOS-0012** is the document that states all of the above compose into a single conformant object requiring *both* layers.

Validation of the two-layer requirement is performed under **STD-0006** (Review & Validation).

---

# 9. What This Model Does Not Yet Define

Flagged, not resolved here (they require their own decisions):

- **Typed relationships in frontmatter (F-4).** STD-0004's vocabulary is currently expressed in object bodies, not frontmatter. Whether to extend STD-0002 to carry typed relations is an open STD-0002/STD-0004 decision.
- **Identifier Registry (F-9).** STD-0001 §18 promises a central registry to prevent collisions; it does not yet exist. KOS-0012 assumes but does not build it.
- **Role and Operations content structures.** Marked "future" in §4; to be specified when those layers are built.
- **Source metadata for non-modern sources (F-3).** A STD-0002 §11 refinement, tracked separately.

---

# 10. Governance

KOS-0012 is maintained under KOS-0011. It extends KOS-0009 (Knowledge Representation) and depends on KOS-0003 (for Claim content). Changes require documentation, review, and version update.

---

# 11. Closing Principle

Project Relatio adopts:

> A knowledge architecture is only as usable as its object model is explicit. Knowledge Objects are not files with metadata; they are identified, described, related units of meaning — and every type must say what it is made of.

---

# 12. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial Knowledge Object Model. Un-deferred and authored on demonstrated need from the RQ-0001 pressure test (findings F-1, F-2, F-6). Introduces Investigation (INV) and Finding (FND) types; reconciles the metadata layer (STD-0002) with the content layer (KOS-0003 §12).|

---

# End KOS-0012
