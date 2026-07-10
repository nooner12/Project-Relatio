---
title: Standards Dependency Map
document_type: Architecture Document
version: 1.0
status: Adopted
created: 2026-07-09
parent_documents:
  - KOS Architecture Manifest
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - Standards Index
  - Standards Status
  - KOS Dependency Map
  - Standards Architecture Retrospective
tags:
  - ProjectRelatio
  - Standards
  - DependencyMap
  - Architecture
---

# Project Relatio Standards Dependency Map

## Version 1.0

## Adopted Architecture Document

---

# 1. Purpose

The Standards Dependency Map defines the structural relationships between the Standards-layer documents (STD-0001 through STD-0007). It is the Standards-layer counterpart to the KOS Dependency Map, which performs the same function for the Kernel.

Its purpose is to:

- identify which Standards depend on which,
- support change-impact analysis,
- prevent architectural inconsistency,
- keep the Standards layer coherent as it evolves.

The dependency data here is derived from the `parent_documents` declarations of each Standard and was validated in the Standards Architecture Retrospective (§4).

---

# 2. Dependency Philosophy

The Standards layer sits below the Kernel and above Roles/Templates/Operations.

Every Standard roots into the Kernel — chiefly KOS-0009 (Knowledge Representation) and/or KOS-0011 (Governance). A Standard should never depend on a Role, Template, or Operations document.

```
Kernel

supports

Standards

supports

Roles / Templates / Operations
```

---

# 3. Primary Dependency Chain

The Standards build on one another in the following practical order (this is *dependency* order, not numeric order — see §6):

```
STD-0001  Naming & Identification

        ↓

STD-0002  Metadata & YAML

        ↓

STD-0003  Classification & Discovery

        ↓

STD-0004  Relationship & Linking

        ↓

STD-0005  Lifecycle & Revision

        ↓

STD-0006  Review & Validation

        ↓

STD-0007  Terminology & Semantic Stewardship  (cross-cutting — see §4)
```

---

# 4. Individual Dependencies

Read "Depends on" as the Kernel/Standards documents each Standard declares as `parent_documents`.

---

# STD-0001 — Naming & Identification

Depends on:

- KOS-0001, KOS-0009, KOS-0011

Supports:

- STD-0003, STD-0005, and all identifier usage across the vault.

Role:

Defines identifiers, filenames, and classification names.

---

# STD-0002 — Metadata & YAML

Depends on:

- KOS-0009, KOS-0011

Supports:

- STD-0003, all templates, all machine-readable metadata.

Role:

Defines the frontmatter schema every formal document carries.

---

# STD-0003 — Classification & Discovery

Depends on:

- KOS-0009, STD-0001, STD-0002

Supports:

- STD-0004, STD-0007, discovery and navigation.

Role:

Defines category and tag usage and how objects are found.

---

# STD-0004 — Relationship & Linking

Depends on:

- KOS-0009, STD-0007, STD-0003

Supports:

- STD-0005, the knowledge graph.

Role:

Defines relationship vocabulary and linking practice.

---

# STD-0005 — Lifecycle & Revision

Depends on:

- KOS-0011, STD-0001, STD-0004

Supports:

- STD-0006, governance, versioning across the vault.

Role:

Defines maturity/operational states and versioning. Authoritative on lifecycle (STD-0001 §11–12 defer to it).

---

# STD-0006 — Review & Validation

Depends on:

- KOS-0011, KOS-0009, STD-0005

Supports:

- the integrity of every other Standard (it verifies them).

Role:

Defines how compliance with all other Standards is checked. Sits at the top of the practical chain and is depended upon by none.

---

# STD-0007 — Terminology & Semantic Stewardship

Depends on:

- KOS-0009, KOS-0011, STD-0003

Supports:

- STD-0004, STD-0005, and consistent terminology everywhere.

Role:

Cross-cutting. Although numbered last, it is depended upon by STD-0004; its terminology discipline applies across the whole layer.

---

# 5. Dependency Layers

The Standards layer viewed vertically:

```
LEVEL 0   Identity of objects
          STD-0001

LEVEL 1   Description of objects
          STD-0002

LEVEL 2   Organization & connection
          STD-0003
          STD-0004
          STD-0007

LEVEL 3   Change & assurance
          STD-0005
          STD-0006
```

---

# 6. Numeric Order vs Dependency Order

Identifiers are not sequence numbers (STD-0001 §6). Two places where numeric order and dependency order diverge:

- STD-0004 depends on STD-0007 (higher number).
- STD-0006 (Review) depends on STD-0005 and verifies the whole layer, so it is logically last-but-one while STD-0007 is cross-cutting.

No one should infer build order or precedence from the numbers alone.

---

# 7. Change Impact Rules

Before modifying a Standard, evaluate:

- **Direct dependents** — Standards that declare it as a parent.
- **Indirect dependents** — documents affected transitively.
- **Operational dependents** — templates, roles, and workflows that implement it (not yet built).

STD-0002, STD-0005, and STD-0007 have the widest blast radius; change them with the most care.

---

# 8. Current Assessment

Standards Dependency Status:

# Stable

- No circular dependencies (verified in the Retrospective §4).
- Every Standard roots into the Kernel.
- STD-0006 correctly terminates the chain (verifies all, depended on by none).

---

# 9. Maintenance Rule

Update this map whenever:

- a new Standard is added,
- a Standard's `parent_documents` change,
- a Standard is superseded,
- the layer's boundaries change.

---

# 10. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial Standards Dependency Map; Standards-layer sibling to the KOS Dependency Map, seeded from the Standards Architecture Retrospective §4|

---

# End Standards Dependency Map
