---
title: STD-0003 - Classification & Discovery Standard
document_type: Standards Document
version: 1.1
status: Adopted
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Operating System
  - Standards
  - Classification Architecture
parent_documents:
  - KOS-0009 Knowledge Representation & Information Architecture Framework
  - STD-0001 Naming & Identification Standard
  - STD-0002 Metadata & YAML Standard
related_documents:
  - STD-0004 Relationship & Linking Standard
  - STD-0007 Controlled Vocabulary & Terminology Standard
tags:
  - ProjectRelatio
  - Standards
  - Classification
  - Discovery
  - KnowledgeArchitecture
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# STD-0003

# Project Relatio Classification & Discovery Standard

## Version 1.1
## Adopted Standards Document

---

# 1. Purpose

The Classification & Discovery Standard defines how Knowledge Objects are organized, categorized, and discovered within the Relatio Knowledge Architecture.

This standard establishes the distinction between:

- classification,
- navigation,
- relationships,
- discovery.

The purpose of this separation is to preserve architectural clarity as Project Relatio scales.

---

# 2. Standard Principle

Project Relatio adopts:

> Every Knowledge Object shall have one primary classification, many relationships, and multiple possible discovery paths.

Classification provides structure.

Relationships provide meaning.

Discovery provides access.

---

# 3. Scope

This standard governs:

- Knowledge Object placement,
- document classification,
- category assignment,
- discovery mechanisms,
- taxonomy principles.

This standard does not define:

- semantic relationships,
- lifecycle management,
- implementation-specific tools.

Those are governed by other standards.

---

# 4. Classification Model

Classification answers:

> "What kind of thing is this?"

A Knowledge Object receives classification based on its architectural purpose.

Primary classification should remain stable.

---

# 5. Organizational Dimensions

Project Relatio recognizes four organizational dimensions.

```
Knowledge Object

        │

        ├── Identity
        │
        ├── Classification
        │
        ├── Relationships
        │
        └── Discovery
```

Each dimension serves a distinct function.

---

# 6. Identity

Identity defines the unique existence of a Knowledge Object.

Governed by:

- STD-0001 Naming & Identification Standard
- STD-0002 Metadata & YAML Standard

Identity includes:

- identifier,
- title,
- object type.

---

# 7. Classification

Classification determines architectural placement.

Examples:

```
Kernel

Standards

Roles

Templates

Operations

Research
```

Classification should answer:

> "Where does this belong within the architecture?"

---

# 8. Classification Rules

A Knowledge Object shall:

- have one primary classification,
- avoid duplicate classification,
- avoid classification based solely on topic,
- avoid classification based solely on discovery needs.

---

# 9. Folder Relationship

Folders are implementation expressions of classification.

Folders may represent:

- architecture layers,
- operational domains,
- organizational boundaries.

Folders shall not attempt to represent:

- every relationship,
- every topic,
- every possible discovery path.

---

# 10. Relationship Separation

Classification is not relationship.

Example:

A Standard may belong in:

```
02 Standards
```

while relating to:

```
KOS-0009 Knowledge Representation Framework

TPL-0001 Formal Document Template

STD-0004 Relationship & Linking Standard
```

The relationships do not change the classification.

---

# 11. Discovery Model

Discovery answers:

> "How can this Knowledge Object be found?"

Discovery mechanisms include:

- indexes,
- maps,
- search,
- tags,
- queries,
- graph visualization.

---

# 12. Indexes

Indexes are authoritative registries.

Purpose:

- inventory,
- navigation,
- canonical reference.

Examples:

- Kernel Index
- Standards Index

Indexes answer:

> "What exists?"

---

# 13. Maps of Content

Maps of Content (MOCs) are exploratory navigation structures.

Purpose:

- synthesis,
- exploration,
- conceptual navigation.

MOCs answer:

> "How should this domain be explored?"

---

# 14. Index vs MOC

The distinction:

|Object|Purpose|
|---|---|
|Index|Registry|
|MOC|Exploration Map|

An Index is authoritative.

A MOC is interpretive.

Both are valuable, but they serve different purposes.

---

# 15. Tagging Role

Tags are discovery mechanisms.

Tags are not:

- classifications,
- relationships,
- replacements for metadata.

Tags exist to create alternate discovery paths.

---

# 16. Tag Categories

Project Relatio recognizes two tag categories.

## Controlled Tags

Stable vocabulary.

Examples:

```
ProjectRelatio

Standards

Architecture

Research
```

---

## Emergent Tags

Context-specific concepts.

Examples:

```
BayesianInference

ClimateModeling

TacitKnowledge
```

---

# 17. Discovery Principle

Project Relatio adopts:

> Structure should remain intentional; discovery should remain flexible.

This principle prevents uncontrolled complexity.

---

# 18. Classification Integrity Rules

The following are prohibited:

## Topic-Based Classification

Example:

Incorrect:

```
Climate Research
```

when the object is actually a:

```
Research Record
```

---

## Duplicate Storage

A Knowledge Object should not exist in multiple locations solely for convenience.

Relationships and discovery mechanisms should provide access.

---

## Tag Replacement

Tags shall not replace classification.

---

# 19. Relationship to Future Standards

STD-0003 establishes the foundation for:

## STD-0004

Relationship & Linking Standard

which will define semantic connections.

---

## STD-0007

Controlled Vocabulary & Terminology Standard

which will define language consistency.

---

# 20. Governance

This standard is governed by:

KOS-0011 Governance, Stewardship & Evolution Framework.

Changes require:

- documented rationale,
- review,
- version update.

---

# 21. Closing Principle

Project Relatio adopts:

> Classification creates order. Relationships create meaning. Discovery creates accessibility.

A mature knowledge architecture requires all three.

---

# 22. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial classification and discovery standard|
|1.1|2026-07-22|Adopted|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End STD-0003