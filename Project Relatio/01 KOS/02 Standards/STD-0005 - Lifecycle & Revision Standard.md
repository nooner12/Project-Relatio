---
title: STD-0005 - Lifecycle & Revision Standard
document_type: Standards Document
version: 1.0
status: Adopted
created: 2026-07-09
category:
  - Knowledge Operating System
  - Standards
  - Governance Architecture
parent_documents:
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - STD-0001 Naming & Identification Standard
  - STD-0004 Relationship & Linking Standard
related_documents:
  - STD-0006 Review & Validation Standard
  - STD-0007 Terminology & Semantic Stewardship Standard
tags:
  - ProjectRelatio
  - Standards
  - Lifecycle
  - Revision
  - Governance
---

# STD-0005

# Project Relatio Lifecycle & Revision Standard

## Version 1.0

## Adopted Standards Document

---

# 1. Purpose

The Lifecycle & Revision Standard defines how Knowledge Objects evolve throughout their existence within the Relatio Knowledge Architecture.

This standard establishes:

- lifecycle states,
- revision practices,
- versioning principles,
- historical preservation requirements.

---

# 2. Standard Principle

Project Relatio adopts:

> Knowledge Objects evolve over time, but their evolution must preserve continuity, context, and trust.

A mature knowledge architecture does not erase its past.

It maintains a relationship between past, present, and future states.

---

# 3. Scope

This standard governs:

- Knowledge Object maturity,
- operational status,
- revision practices,
- supersession,
- archival behavior.

This standard does not define:

- relationship vocabulary,
- classification,
- implementation workflows.

---

# 4. Lifecycle Model

Project Relatio recognizes two lifecycle dimensions.

A Knowledge Object possesses:

1. **Maturity State**
2. **Operational State**

These dimensions are independent.

---

# 5. Maturity State

Maturity describes the development progression of a Knowledge Object.

```
Proposed

↓

Draft

↓

Reviewed

↓

Adopted
```

---

# 6. Proposed

Definition:

A potential Knowledge Object identified for development.

Characteristics:

- concept exists,
- structure may be incomplete,
- no authority assigned.

---

# 7. Draft

Definition:

A Knowledge Object undergoing development.

Characteristics:

- content incomplete,
- subject to modification,
- not authoritative.

---

# 8. Reviewed

Definition:

A Knowledge Object evaluated for quality and architectural compatibility.

Review considers:

- clarity,
- dependencies,
- terminology,
- consistency.

---

# 9. Adopted

Definition:

A Knowledge Object accepted as part of the formal architecture.

Characteristics:

- authoritative,
- governed,
- available for operational use.

---

# 10. Operational State

Operational state describes the current role of a Knowledge Object after adoption.

```
Active

↓

Superseded

↓

Archived
```

---

# 11. Active

Definition:

A Knowledge Object currently recognized as valid and in use.

---

# 12. Superseded

Definition:

A Knowledge Object replaced by another Knowledge Object.

Superseded objects:

- remain preserved,
- retain historical value,
- identify replacement relationships.

A superseded object is not deleted.

---

# 13. Archived

Definition:

A Knowledge Object retained for historical reference but no longer considered operational.

---

# 14. Lifecycle Relationship

Lifecycle transitions create relationships.

Examples:

```
STD-0005

supersedes

STD-0005 v0.9
```

or:

```
New Model

derived_from

Previous Model
```

Lifecycle changes should preserve lineage.

---

# 15. Revision Principles

Every revision should answer:

1. What changed?
2. Why did it change?
3. What impact does it have?
4. What previous state does it replace or extend?

---

# 16. Versioning Standard

Project Relatio adopts semantic versioning principles.

Format:

```
Major.Minor.Patch
```

---

# 17. Major Revision

Example:

```
1.0 → 2.0
```

Used when:

- meaning changes substantially,
- compatibility breaks,
- architecture changes.

---

# 18. Minor Revision

Example:

```
1.0 → 1.1
```

Used when:

- functionality expands,
- concepts are extended,
- additional capability is introduced.

---

# 19. Patch Revision

Example:

```
1.0 → 1.0.1
```

Used when:

- corrections occur,
- errors are fixed,
- wording improves.

---

# 20. Revision History Requirement

Formal Knowledge Objects should maintain revision history.

Minimum fields:

- version,
- date,
- status,
- change description.

---

# 21. Supersession Rules

When replacing a Knowledge Object:

The successor should:

- identify the predecessor,
- explain the change,
- preserve continuity.

The predecessor should:

- remain accessible,
- indicate replacement status.

---

# 22. Preservation Principle

Project Relatio adopts:

> Historical states are part of knowledge.

Archived and superseded objects may contain valuable:

- reasoning,
- context,
- decisions,
- lessons.

---

# 23. Draft Governance

Drafts are permitted and encouraged.

However:

Draft status must communicate that the object is not authoritative.

Drafts must not be treated as standards or adopted architecture.

---

# 24. Lifecycle Metadata

Knowledge Objects may express lifecycle information through metadata including:

- status,
- version,
- created date,
- modified date,
- superseded_by,
- derived_from.

---

# 25. Relationship to Other Standards

STD-0005 depends on:

- STD-0004 Relationship & Linking Standard
- STD-0007 Terminology & Semantic Stewardship Standard

STD-0005 supports:

- governance,
- review,
- architectural evolution.

---

# 26. Governance

Lifecycle changes are governed through:

KOS-0011 Governance, Stewardship & Evolution Framework.

---

# 27. Closing Principle

Project Relatio adopts:

> A knowledge architecture that cannot evolve will eventually become obsolete. A knowledge architecture that cannot preserve history cannot be trusted.

Lifecycle governance enables both adaptation and continuity.

---

# 28. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial lifecycle and revision standard|

---

# End STD-0005