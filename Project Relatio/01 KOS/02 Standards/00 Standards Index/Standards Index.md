---
title: Standards Index
document_type: Navigation Document
version: 1.2
status: Adopted
operational_status: Active
category:
  - Knowledge Operating System
  - Standards
  - Navigation
created: 2026-07-09
parent_documents:
  - KOS Architecture Manifest
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - STD-0001 Naming & Identification Standard
  - STD-0002 Metadata & YAML Standard
  - STD-0003 Classification & Discovery Standard
  - STD-0004 Relationship & Linking Standard
  - STD-0005 Lifecycle & Revision Standard
  - STD-0006 Review & Validation Standard
  - STD-0007 Terminology & Semantic Stewardship Standard
tags:
  - ProjectRelatio
  - Standards
  - Index
  - Architecture
---

# Project Relatio Standards Index

## Version 1.2

## Adopted Navigation Document

---

# 1. Purpose

The Standards Index provides the primary navigation point for the Project Relatio Standards layer.

It defines:

- existing standards,
- planned standards,
- standards relationships,
- implementation guidance.

---

# 2. Standards Definition

Standards are the implementation layer of Project Relatio.

The Kernel defines:

> What the system is.

Standards define:

> How the system is consistently built and maintained.

---

# 3. Standards Architecture Position

```
id="h3x8pa"
Kernel

↓

Standards

↓

Roles

↓

Templates

↓

Operations

↓

Research Applications
```

Standards translate architectural principles into repeatable practices.

---

# 4. Standards Principles

Project Relatio Standards follow five principles:

---

## SP-001 — Consistency

Similar objects should follow similar structures.

---

## SP-002 — Traceability

Changes should preserve history and reasoning.

---

## SP-003 — Scalability

Standards should support future growth.

---

## SP-004 — Clarity

Rules should reduce ambiguity.

---

## SP-005 — Adaptability

Standards should evolve when experience demonstrates improvement.

---

# 5. Current Standards Registry

|ID|Title|Status|Purpose|
|---|---|---|---|
|STD-0001|Naming & Identification Standard|Adopted|Defines identifiers, naming, and classification|
|STD-0002|Metadata & YAML Standard (v1.1)|Adopted|Defines document metadata requirements|
|STD-0003|Classification & Discovery Standard|Adopted|Defines category/tag usage and discovery|
|STD-0004|Relationship & Linking Standard|Adopted|Defines relationship vocabulary and linking practice|
|STD-0005|Lifecycle & Revision Standard|Adopted|Defines maturity/operational states and versioning|
|STD-0006|Review & Validation Standard|Adopted|Defines how compliance with STD-0001–0005, 0007 is checked|
|STD-0007|Terminology & Semantic Stewardship Standard|Adopted|Defines preferred terminology and semantic consistency|

All seven Standards are now Adopted. This section previously described an earlier planned sequence (Section 6, below) that no longer matches what was actually built — retained for historical record, not as current guidance.

---

# 6. Originally Planned Standards (superseded by actual build order)

The sequence below was the original plan as of this Index's v1.0 authoring. It is preserved here for historical traceability; it does not reflect what STD-0003 through STD-0007 actually became. Notably: the planned "STD-0005 — Document Classification" became **STD-0003 — Classification & Discovery**; the planned "STD-0006 — Version & Revision" became **STD-0005 — Lifecycle & Revision**; the planned "STD-0007 — Review & Validation" became **STD-0006 — Review & Validation**; and **STD-0007** was built as **Terminology & Semantic Stewardship**, which was not in the original plan at all.

---

# STD-0002 — Metadata & YAML Standard

Purpose:

Define:

- required YAML fields,
- metadata structure,
- property naming,
- document descriptors.

Status:

Adopted (see Section 5).

---

# STD-0003 — Tagging Standard

Originally planned as a Tagging Standard; built instead as **Classification & Discovery Standard**, covering tags plus broader classification/discovery mechanics.

Status:

Adopted (see Section 5).

---

# STD-0004 — Linking & Relationship Standard

Built as **Relationship & Linking Standard**, matching the original intent.

Status:

Adopted (see Section 5).

---

# STD-0005 — Document Classification Standard

Originally planned as a Document Classification Standard; built instead as **Lifecycle & Revision Standard**. Document classification was absorbed into STD-0003 instead.

Status:

Adopted (see Section 5).

---

# STD-0006 — Version & Revision Standard

Originally planned as a Version & Revision Standard; built instead as **Review & Validation Standard**. Version and revision practice was absorbed into STD-0005 instead.

Status:

Adopted (see Section 5).

---

# STD-0007 — Review & Validation Standard

Originally planned as Review & Validation; that role was ultimately filled by **STD-0006**. STD-0007 was built instead as **Terminology & Semantic Stewardship Standard**, a need that emerged during the build that wasn't anticipated in this original plan.

Status:

Adopted (see Section 5).

---

# 7. Standards Relationship Model (as actually built)

Standards build upon one another.

```
STD-0001

Naming

↓

STD-0002

Metadata

↓

STD-0003

Classification & Discovery

↓

STD-0004

Relationships & Linking

↓

STD-0005

Lifecycle & Revision

↓

STD-0006

Review & Validation

↓

STD-0007

Terminology & Semantic Stewardship
```

---

# 8. Standards Governance

Standards are governed by:

KOS-0011 — Governance, Stewardship & Evolution Framework.

Changes require:

- documented rationale,
- review,
- version update.

---

# 9. Standards Lifecycle

All Standards follow:

```
Draft

↓

Review

↓

Adopted

↓

Active

↓

Deprecated

↓

Archived
```

---

# 10. Standards Creation Rule

A new Standard should only be created when:

- repeated behavior requires consistency,
- ambiguity creates risk,
- architecture requires enforcement.

Not every preference requires a Standard.

---

# 11. Current Standards Status

```
Standards Layer

Foundation Established

↓

Expansion Authorized

↓

Complete — STD-0001 through STD-0007 Adopted (2026-07-09)
```

The Standards layer is complete as of STD-0006's adoption. Remaining work moves to the Standards Architecture Retrospective (dependency structure, naming consistency, integration issues) and then to the Roles, Templates, and Operations layers — see CLAUDE.md's priority order.

---

# 12. Closing Principle

Project Relatio adopts:

> Standards exist to preserve coherence without preventing intelligent evolution.

---

# 13. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial Standards Index|
|1.1|2026-07-09|Adopted|Integration Update following STD-0006 adoption: refreshed registry to reflect all seven Standards as Adopted; reconciled the originally-planned sequence against what was actually built|
|1.1a|2026-07-09|Adopted|Correction: an earlier edit in this pass wrongly removed the `KOS Architecture Manifest` parent reference believing it non-existent; the Manifest does exist (`01 Kernel/`) and the reference has been restored|
|1.2|2026-07-09|Adopted|document_type consolidated from "Standards Navigation Document" to the layer-agnostic "Navigation Document" (STD-0002 v1.3)|

---

# End Standards Index