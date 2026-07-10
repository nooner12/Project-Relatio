---
title: STD-0004 - Relationship & Linking Standard
document_type: Standards Document
version: 1.0
status: Adopted
created: 2026-07-09
category:
  - Knowledge Operating System
  - Standards
  - Relationship Architecture
parent_documents:
  - KOS-0009 Knowledge Representation & Information Architecture Framework
  - STD-0007 Terminology & Semantic Stewardship Standard
  - STD-0003 Classification & Discovery Standard
related_documents:
  - STD-0005 Lifecycle & Revision Standard
  - STD-0006 Review & Validation Standard
tags:
  - ProjectRelatio
  - Standards
  - Relationships
  - KnowledgeGraph
  - SemanticArchitecture
---

# STD-0004

# Project Relatio Relationship & Linking Standard

## Version 1.0

## Adopted Standards Document

---

# 1. Purpose

The Relationship & Linking Standard defines how Knowledge Objects connect within the Relatio Knowledge Architecture.

The purpose of this standard is to establish meaningful semantic connections between Knowledge Objects rather than merely increasing the number of links.

---

# 2. Standard Principle

Project Relatio adopts:

> Links connect objects. Relationships explain why objects connect.

The value of a knowledge architecture is determined not by the quantity of connections, but by the quality and meaning of those connections.

---

# 3. Scope

This standard governs:

- relationship principles,
- relationship categories,
- approved relationship vocabulary,
- semantic linking practices.

This standard does not govern:

- implementation-specific linking methods,
- database structures,
- Obsidian syntax,
- visualization systems.

---

# 4. Knowledge Relationship Model

A relationship consists of:

```
Subject

↓

Relationship Type

↓

Object
```

Example:

```
STD-0004

depends_on

STD-0007
```

The relationship itself carries architectural meaning.

---

# 5. Relationship Requirements

Every formal relationship should:

1. Have identifiable source and destination objects.
2. Use the most precise available relationship type.
3. Represent meaningful semantic connection.
4. Avoid unnecessary duplication.

---

# 6. Relationship Categories

Project Relatio recognizes five initial relationship categories.

---

# 6.1 Structural Relationships

Describe organization and composition.

Examples:

- part_of
- contains
- instance_of

---

# 6.2 Semantic Relationships

Describe conceptual meaning.

Examples:

- explains
- supports
- contrasts_with

---

# 6.3 Dependency Relationships

Describe requirements and implementation.

Examples:

- depends_on
- implements
- requires

---

# 6.4 Evolutionary Relationships

Describe change over time.

Examples:

- supersedes
- revises
- derived_from

---

# 6.5 Navigational Relationships

Describe exploration paths.

Examples:

- related_to
- see_also

---

# 7. Approved Relationship Vocabulary

Version 1.0 adopts the following foundational relationship types.

---

# defines

Meaning:

A Knowledge Object establishes the meaning, rules, or structure of another object.

Example:

```
STD-0003 defines classification principles.
```

---

# implements

Meaning:

A Knowledge Object applies another object's principles or requirements.

Example:

```
A template implements a standard.
```

---

# extends

Meaning:

A Knowledge Object expands another while maintaining compatibility.

---

# depends_on

Meaning:

A Knowledge Object requires another object for interpretation or operation.

---

# derived_from

Meaning:

A Knowledge Object originates from another.

---

# supports

Meaning:

A Knowledge Object contributes to the purpose or function of another.

---

# contrasts_with

Meaning:

Two Knowledge Objects represent meaningfully different perspectives, approaches, or conclusions.

---

# supersedes

Meaning:

A Knowledge Object replaces a previous version or approach.

---

# part_of

Meaning:

A Knowledge Object belongs to a larger structure.

---

# instance_of

Meaning:

A Knowledge Object represents a specific example of a broader class.

---

# explains

Meaning:

A Knowledge Object provides understanding or interpretation of another.

---

# related_to

Meaning:

A general relationship used only when a more precise relationship cannot yet be determined.

---

# 8. Relationship Directionality

Relationships may be directional.

Example:

Correct:

```
STD-0004

depends_on

STD-0007
```

Incorrect assumption:

```
STD-0007

depends_on

STD-0004
```

Direction is part of meaning.

---

# 9. Relationship Precision Principle

Project Relatio prefers:

```
specific relationship
```

over:

```
generic relationship
```

Example:

Preferred:

```
implements
```

instead of:

```
related_to
```

when implementation exists.

---

# 10. Linking Principle

Project Relatio adopts:

> Create relationships because they improve understanding, not because links are available.

---

# 11. Relationship Anti-Patterns

## Link Quantity Optimization

Creating links merely to increase graph density.

---

## Relationship Ambiguity

Using broad relationships when specific meaning exists.

---

## False Reciprocity

Assuming every relationship works in both directions.

---

## Structural Substitution

Using folders or tags as replacements for relationships.

---

# 12. Relationship Evolution

The relationship vocabulary will evolve through use.

New relationship types require:

- definition,
- purpose,
- examples,
- compatibility review.

---

# 13. Relationship to Other Standards

STD-0004 depends on:

- STD-0007 Terminology & Semantic Stewardship
- STD-0003 Classification & Discovery

STD-0004 supports:

- research modeling,
- knowledge graphs,
- future automation,
- advanced discovery.

---

# 14. Governance

Relationship vocabulary is governed through:

KOS-0011 Governance, Stewardship & Evolution Framework.

Changes require:

- rationale,
- review,
- version control.

---

# 15. Closing Principle

Project Relatio adopts:

> The purpose of linking is not connection. The purpose of linking is understanding.

Meaningful relationships transform stored information into structured knowledge.

---

# 16. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial relationship and linking standard|

---

# End STD-0004