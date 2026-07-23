---
title: STD-0004 - Relationship & Linking Standard
document_type: Standards Document
version: 1.3
status: Adopted
operational_status: Active
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

## Version 1.3

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

# branches_from (PROVISIONAL — ADR-GOV-0009 D4)

Meaning:

Tradition B `branches_from` tradition A — the historical descent of one religious tradition from another. **Entity-to-entity ONLY (ENT → ENT).** Asymmetric; never reciprocated; not a symmetric-advisory candidate (it is directional by construction, like `derived_from`, and `graph_integrity.py` treats it as such).

**Required qualifier.** Every `branches_from` edge carries a `qualifier` naming the *kind* of branching, one of:

- `schism`
- `reform`
- `syncretic-descent`
- `heterodox-offshoot`
- `disputed`
- `continuation`

An edge without a qualifier is **malformed** (a graph-integrity error, not an advisory). Different kinds of branching render differently.

**`continuation` (added v1.3 — ADR-GOV-0010 D1).**

> `continuation` — B `branches_from` A where B carries forward A's principal or main line rather than departing from it: the least-departed descendant after a rupture or transformation. Distinguished from `reform` (reconstitution-with-change) by the absence of a departure connotation.

This value was added by the anchor-vocabulary review (ADR-GOV-0009 §7(a)) in response to INV-0017's demonstrated inability to name a main-line-continuation edge (Rabbinic Judaism carrying forward Second Temple Judaism after 70 CE): every prior value connoted departure. Adding it is **additive repair of a demonstrated gap, not a promotion of the list from provisional to durable** — the qualifier list stays provisional (ADR-GOV-0010 D5); it simply has one more tool in it.

**Warrant rule.** Every `branches_from` edge must be supported by a **graded claim** — the edge is the render; the claim is the warrant. An unwarranted edge is a graph-integrity error. (Because a warrant is a claim about lineage rather than a structured pointer on the edge, this rule is **review-checked, not tool-checked** — see §7.2 and `tools/README.md`.)

**Provisional status (ADR-GOV-0007 §2 anchor discipline).** This type and its qualifier list are *scaffolding*, expected to be revised by the first two family investigations of the world-religions timeline program (ADR-GOV-0009); their findings on edge semantics route to the review queue as recommendations (ADR-GOV-0007 §3). It is a vocabulary entry, not load-bearing architecture — maximally revisable. **Named revision trigger: ADR-GOV-0009 §7(a).**

---

# 7.1 Machine-Readable Encoding (v1.1)

The vocabulary above is expressed in metadata through the typed **`relationships`** block defined by STD-0002 §7 — each entry pairs a `type` from this vocabulary with a `target` identifier. This closes Pressure Test **F-4** / **GB-2026-001**, where these types could previously live only in an object's prose. The flat `parent_documents`/`related_documents` lists remain the tooling-read graph for dangling-reference checks; the typed block adds the *meaning* of each edge, which `graph_integrity.py` uses for type-aware reciprocity (§11 *False Reciprocity* — directional types such as `derived_from`, `supports`, `part_of` are not expected to reciprocate; symmetric types such as `related_to`, `contrasts_with` are).

---

# 7.2 The `qualifier` key (v1.2 — branches_from)

The typed `relationships` block gains an optional **`qualifier`** key, valid **only** on `branches_from` entries (an unqualified `branches_from` edge is malformed; a `qualifier` on any other type is meaningless and ignored):

```
relationships:
  - type: branches_from
    target: ENT-00XX
    qualifier: schism
```

`qualifier` takes one value from the controlled list in the `branches_from` entry above (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed` / `continuation`). `graph_integrity.py` enforces the qualifier-required rule, the vocabulary, and the ENT → ENT restriction as errors.

**Disambiguation note — the two `reform` vocabularies (D3, ADR-GOV-0010).** The `branches_from` **qualifier** `reform` (this field, STD-0004 §7.2 — a *kind of descent relationship*) and the STD-0002 §11 **`tradition_type`** value `reform` (a different field — *how a tradition came to be*) are **different vocabularies on different fields that coincidentally share a word.** They are never conflated: a tradition may carry `tradition_type: reform` while its lineage edge carries any qualifier (or vice versa), and the two are graded and reviewed independently. (Rabbinic Judaism is the case that exposed the collision: `tradition_type: reform` with a `branches_from` qualifier of `continuation`.)

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
|1.1|2026-07-11|Adopted|Added §7.1 Machine-Readable Encoding: the vocabulary is now carried in the typed `relationships` frontmatter block (STD-0002 §7 v1.6), closing F-4 / GB-2026-001. No vocabulary change — the twelve approved types are unchanged.|
|1.2|2026-07-21|Adopted|Added the **provisional `branches_from`** relationship type (ENT → ENT, asymmetric, REQUIRED qualifier from schism/reform/syncretic-descent/heterodox-offshoot/disputed, warrant-by-graded-claim) enacting ADR-GOV-0009 D4; added §7.2 defining the optional `qualifier` frontmatter key (valid only on branches_from). PROVISIONAL under ADR-GOV-0007 §2 anchor discipline; revision trigger ADR-GOV-0009 §7(a). Additive — the existing twelve types are unchanged.|
|1.3|2026-07-22|Adopted|**Anchor-vocabulary review (ADR-GOV-0009 §7(a)) enacting ADR-GOV-0010 D1/D3.** Added a sixth `branches_from` qualifier **`continuation`** (B carries forward A's principal/main line rather than departing — the least-departed descendant after a rupture; distinguished from `reform` by the absence of a departure connotation) in response to INV-0017's demonstrated inability to name a main-line-continuation edge (Rabbinic Judaism); list now schism/reform/syncretic-descent/heterodox-offshoot/disputed/continuation. Added §7.2 the two-`reform`-vocabularies disambiguation note (the `branches_from` qualifier `reform` and the STD-0002 `tradition_type` value `reform` are different fields sharing a word, never conflated). **Additive repair of a demonstrated gap — the qualifier list stays PROVISIONAL (ADR-GOV-0010 D5); NOT a promotion toward durable.** The `graph_integrity.py` enforced set was extended to match.|

---

# End STD-0004