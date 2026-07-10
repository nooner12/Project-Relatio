---
title: OPS-0002 - Relationship Integrity & Graph Maintenance
document_type: Operations Document
version: 1.0
status: Adopted
created: 2026-07-09
parent_documents:
  - STD-0004 Relationship & Linking Standard
  - STD-0006 Review & Validation Standard
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - OPS-0001 Knowledge Base Organization
  - Identifier Registry
  - Third-Run Assessment - RQ-0003
tags:
  - ProjectRelatio
  - Operations
  - Relationships
  - GraphIntegrity
---

# OPS-0002

# Relationship Integrity & Graph Maintenance

## Version 1.0

## Adopted Operations Document

---

# 1. Purpose

Project Relatio's defining claim is that knowledge is **a graph of meaningful relationships, not stored information** (CLAUDE.md non-negotiable #7). A graph is only trustworthy if it is **consistent**: relationships must be real, semantic, and agreed on by both ends. The third research workflow demonstrated that, maintained by hand, the graph silently drifts (Third-Run Assessment F-12). This document defines the practice that keeps the graph consistent, and the validation that detects when it isn't.

This is an operational practice (RRI). It implements STD-0004 (vocabulary) and is enforced under STD-0006 (validation).

---

# 2. Principles

1. **Relationships are bidirectional.** If A relates to B, both A and B must record it. A link recorded on only one end is a defect, not a relationship.
2. **Relationships are typed and semantic.** Use the STD-0004 vocabulary (`defines, implements, extends, depends_on, derived_from, supports, contrasts_with, supersedes, part_of, instance_of, explains, related_to`). Prefer a specific relation; use `related_to` sparingly.
3. **Every related object exists.** A relationship to a non-existent object is a dangling reference (see the Identifier Registry as the source of truth for what exists).
4. **The reciprocal relation is correct.** `supports` ↔ `derived_from`; `part_of` ↔ (contains); `contrasts_with` ↔ `contrasts_with`; `supersedes` ↔ `superseded_by`.

---

# 3. Practice — Creating a Relationship

When asserting that object A relates to object B:
1. Add B to A's `related_documents` (frontmatter — the machine-readable layer) **and** state the typed relation in A's body Relationships section.
2. Add the **reciprocal** on B (frontmatter + body), using the correct reverse relation.
3. Confirm B exists in the Identifier Registry.

> **Two-layer note:** frontmatter `related_documents` is what tooling (Dataview, graph view) reads; the body Relationships section carries the STD-0004 *type*. Both must agree. (A future STD-0002/STD-0004 enhancement may let frontmatter carry typed relations directly — Pressure Test F-4; until then, type lives in the body.)

---

# 4. Validation (under STD-0006)

Two checks, runnable now with Obsidian mechanics (RRI):

- **Dangling-reference check:** every `related_documents` entry resolves to an existing file. Obsidian's unresolved-links view and the Identifier Registry surface violations.
- **Reciprocity check:** for every A→B link, B→A exists. A Dataview query over `related_documents` (or the backlinks pane, one object at a time) surfaces one-directional links.

Obsidian's **graph view** visualizes the whole KB graph; isolated or thinly-connected nodes are candidates for missing relationships.

---

# 5. Validation Performed (2026-07-09)

A first reciprocity pass over the Knowledge Base found:

- **INV-0002's** finding↔claim links (FND-0002 ↔ CLM-0003/CLM-0004): **consistent** — authored forward in run 2.
- **INV-0001's** and **INV-0003's** finding↔claim links (FND-0001 ↔ CLM-0001/CLM-0002; FND-0003 ↔ CLM-0005/CLM-0006): **one-directional** — the findings referenced their claims, but the claims (written before the findings existed) did not reference back.

**Repair applied:** the four claims were updated to reference their findings; the finding↔claim subgraph is now bidirectionally consistent. **Exemplar of a well-formed node:** CLM-0001 now connects to its sources (SRC-0001/0002), its sibling claim (CLM-0002, `contrasts_with`), its entity (ENT-0001, `related_to`), and its finding (FND-0001, `supports`).

Remaining known gaps (tracked, not yet reconciled): source↔claim reciprocity (many SRC records do not list the CLMs that cite them). These are low-severity and are the natural target for automation (§6).

---

# 6. Toward Automation

Manual reciprocity maintenance is the current practice but does not scale (F-12's core point). The intended RRI enhancement: a **Dataview-generated integrity report** that lists dangling and one-directional links across the KB, run as a periodic STD-0006 audit. Building it is a future Operations task, justified once the KB is large enough that manual checks become unreliable — not before (demonstrated-need discipline).

---

# 7. Relationship to Other Documents

- Vocabulary: **STD-0004**. Validation authority: **STD-0006**. Object definitions: **KOS-0012**. Object existence: **Identifier Registry**. Placement: **OPS-0001**.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial relationship-integrity practice; resolves the practice-gap behind F-12. Included a first reciprocity pass and repair of the finding↔claim subgraph.|

---

# End OPS-0002
