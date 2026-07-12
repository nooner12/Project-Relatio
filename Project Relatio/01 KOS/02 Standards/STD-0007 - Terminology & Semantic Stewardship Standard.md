---
title: STD-0007 - Terminology & Semantic Stewardship Standard
document_type: Standards Document
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Operating System
  - Standards
  - Semantic Architecture
parent_documents:
  - KOS-0009 Knowledge Representation & Information Architecture Framework
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - STD-0003 Classification & Discovery Standard
related_documents:
  - STD-0004 Relationship & Linking Standard
  - STD-0005 Lifecycle & Revision Standard
tags:
  - ProjectRelatio
  - Standards
  - Terminology
  - Semantics
  - KnowledgeArchitecture
---

# STD-0007

# Project Relatio Terminology & Semantic Stewardship Standard

## Version 1.0

## Adopted Standards Document

---

# 1. Purpose

The Terminology & Semantic Stewardship Standard establishes how Project Relatio defines, maintains, and evolves the language used throughout the Relatio Knowledge Architecture.

The purpose of this standard is to ensure:

- conceptual precision,
- consistent communication,
- stable architectural meaning,
- interoperability between Knowledge Objects.

---

# 2. Standard Principle

Project Relatio adopts:

> Language is part of architecture. The words used to describe knowledge determine how knowledge can be organized, related, and understood.

Terminology is therefore treated as an architectural resource.

---

# 3. Scope

This standard governs:

- architectural terminology,
- Knowledge Object terminology,
- relationship vocabulary,
- metadata vocabulary,
- classification vocabulary.

This standard does not govern:

- scientific terminology,
- domain-specific research vocabulary,
- external disciplinary language.

---

# 4. Semantic Stewardship

Project Relatio uses the term **semantic stewardship** rather than strict vocabulary control.

Reason:

Knowledge systems must balance:

- consistency,
- exploration,
- evolution.

The objective is not to prevent new language.

The objective is to preserve meaning.

---

# 5. Knowledge Object

## Definition

A Knowledge Object is:

> A structured representation of knowledge that possesses identity, classification, relationships, and lifecycle.

Knowledge Objects are the primary conceptual units of the Relatio Knowledge Architecture.

---

# 6. Knowledge Object Categories

The following categories are recognized.

---

## Specification

A Knowledge Object that defines principles, rules, or architecture.

Examples:

- KOS documents
- Standards documents

---

## Registry

A Knowledge Object that provides authoritative inventory.

Examples:

- Indexes
- Catalogs
- Identifier Registry

---

## Map

A Knowledge Object that provides conceptual navigation.

Examples:

- Maps of Content
- Domain Maps

---

## Record

A Knowledge Object representing a specific instance.

Examples:

- ADRs
- Source Records
- Claim Records
- Entity Records

---

## Template

A Knowledge Object defining reusable structure.

---

## Procedure

A Knowledge Object defining repeatable action.

---

## Role

A Knowledge Object defining responsibility and authority.

---

# 7. Architectural Terms

The following terms have official meanings.

---

## Kernel

The foundational architectural layer defining first principles and conceptual foundations.

---

## Standard

A governing specification establishing required consistency.

---

## Framework

A conceptual structure organizing principles or relationships.

---

## Model

A representation of concepts, structures, or relationships.

---

## Schema

A formal description of allowed structure or properties.

---

## Architecture

The organized system of principles, components, relationships, and rules governing Project Relatio.

---

# 8. Deprecated Ambiguous Terms

The following terms should be avoided in architectural writing when precision is required.

---

## Note

Reason:

Implementation-specific.

Preferred:

Knowledge Object.

---

## File

Reason:

Storage-oriented.

Preferred:

Knowledge Object.

---

## Document

Reason:

Useful but incomplete.

Preferred:

Knowledge Object when discussing architecture.

"Document" remains acceptable when referring to a specific implementation artifact.

---

# 9. Vocabulary Governance

New architectural terms follow:

```
Proposed

↓

Reviewed

↓

Adopted

↓

Active
```

Only adopted terminology should be used in formal standards.

---

# 10. Relationship Vocabulary Foundation

The following terms are approved as preliminary relationship language.

Formal definitions will be established in STD-0004.

---

## defines

A Knowledge Object establishes the meaning or structure of another.

---

## implements

A Knowledge Object applies another Knowledge Object.

---

## extends

A Knowledge Object expands another while preserving compatibility.

---

## depends_on

A Knowledge Object requires another for operation or interpretation.

---

## supports

A Knowledge Object contributes to another.

---

## derived_from

A Knowledge Object originates from another.

---

## contrasts_with

A Knowledge Object differs meaningfully from another.

---

## related_to

A general relationship used only when a more precise relationship is not available.

---

# 11. Semantic Stability Principle

Project Relatio adopts:

> Concepts may evolve, but changes in meaning must be deliberate.

Changing terminology without considering existing relationships creates semantic drift.

---

# 12. Terminology Change Process

Changes to adopted terminology require:

1. Identify the proposed change.
2. Document rationale.
3. Assess affected Knowledge Objects.
4. Approve or reject the change.
5. Update standards and indexes if required.

---

# 13. Implementation Independence

Terminology should remain independent of implementation.

Preferred:

> Knowledge Object

Not:

> Obsidian note

Preferred:

> Relationship

Not:

> backlink

Preferred:

> Metadata field

Not:

> YAML property

Implementation terminology may be used in implementation documentation.

---

# 14. Semantic Debt

Project Relatio recognizes semantic debt as a form of architectural debt.

Examples:

- conflicting terminology,
- unclear definitions,
- duplicate concepts,
- outdated language.

Semantic debt should be tracked and resolved deliberately.

---

# 15. Relationship to Future Standards

STD-0007 provides the semantic foundation for:

## STD-0004 — Relationship & Linking Standard

which will define:

- relationship types,
- relationship rules,
- knowledge graph principles.

---

# 16. Governance

This standard is governed by:

KOS-0011 — Governance, Stewardship & Evolution Framework.

Changes require:

- documented rationale,
- review,
- version update.

---

# 17. Closing Principle

Project Relatio adopts:

> A knowledge architecture is only as precise as the language used to describe it.

Semantic stewardship preserves the ability of knowledge to remain understandable as the system grows.

---

# 18. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial semantic stewardship standard|

---

# End STD-0007