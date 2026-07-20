---
title: STD-0001 - Naming & Identification Standard
document_type: Standards Document
version: 1.4
status: Adopted
operational_status: Active
category:
  - Knowledge Operating System
  - Standards
  - Naming Convention
created: 2026-07-09
parent_documents:
  - KOS-0001 Research Operating System Foundation & Charter
  - KOS-0009 Knowledge Representation & Information Architecture Framework
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - KOS Architecture Manifest
  - STD-0002 Metadata Standard
  - STD-0003 Tagging Standard
  - STD-0004 Linking Standard
tags:
  - ProjectRelatio
  - Standards
  - Naming
  - Identification
  - Architecture
---

# STD-0001

# Project Relatio Naming & Identification Standard

## Version 1.4

## Adopted Standards Document

---

# 1. Purpose

The Naming & Identification Standard establishes the rules used to identify and organize components of Project Relatio.

This standard ensures:

- consistency,
- discoverability,
- scalability,
- machine readability,
- architectural integrity.

---

# 2. Standard Principle

Project Relatio adopts:

> Every component should have a clear identity, predictable location, and understandable purpose.

Names are not cosmetic.

Names are structural metadata.

---

# 3. Naming Architecture

Project Relatio uses a combination of:

```
Identifier

+

Title

+

Classification

+

Location
```

Example:

```
KOS-0010 - Reasoning & Synthesis Framework
```

Contains:

- identifier → KOS-0010
- title → Reasoning & Synthesis Framework
- classification → KOS
- location → Kernel

---

# 4. Identifier Format

All formal Project Relatio documents use:

```
TYPE-NUMBER
```

Example:

```
KOS-0001
STD-0001
ADR-KOS-0010
TPL-0001
ROLE-0001
OPS-0001
```

---

# 5. Identifier Classes

## KOS

Knowledge Operating System documents.

Purpose:

Foundational architecture.

Examples:

```
KOS-0001
KOS-0011
```

---

## STD

Standards documents.

Purpose:

Define repeatable rules.

Examples:

```
STD-0001 Naming Standard
STD-0002 Metadata Standard
```

---

## ADR

Architectural Decision Records.

Purpose:

Capture significant decisions.

Format:

```
ADR-[CATEGORY]-NUMBER
```

Example:

```
ADR-KOS-0010
```

---

## ROLE

Role definitions.

Purpose:

Define responsibilities.

---

## TPL

Templates.

Purpose:

Provide reusable structures.

---

## OPS

Operations documents.

Purpose:

Define workflows.

---

## SRC

Source records.

Purpose:

Represent references and origins.

---

## ENT

Entity records.

Purpose:

Represent identifiable entities.

---

## CLM

Claim records.

Purpose:

Represent evaluated assertions.

---

## INV

Investigation records.

Purpose:

Represent a research question, its method, and its synthesis. (Added v1.2; defined by KOS-0012.)

---

## FND

Finding records.

Purpose:

Represent a synthesized answer or conclusion. (Added v1.2; defined by KOS-0012.)

---

# 6. Numeric Standard

All identifiers use four digits.

Correct:

```
KOS-0001

KOS-0010

KOS-0100
```

Incorrect:

```
KOS-1

KOS-10

KOS-100
```

Purpose:

- sorting,
- scalability,
- future expansion.

---

# 7. File Naming Standard

Formal documents follow:

```
[IDENTIFIER] - [TITLE]
```

Examples:

Correct:

```
KOS-0010 - Reasoning & Synthesis Framework

STD-0001 - Naming & Identification Standard
```

Incorrect:

```
Reasoning Framework

Naming Rules
```

---

# 8. Folder Naming Standard

System folders follow:

```
[number] [category]
```

Examples:

```
01 Kernel

02 Standards

03 Roles

04 Templates

05 Operations
```

---

## Path Length Constraint

*Added per **ADR-GOV-0005 §5**. Governs §7 file names and §8 folder nesting jointly, since a path length is the sum of both.*

**Hazard.** Vault files whose absolute Windows path exceeds the `MAX_PATH` limit of **260 characters** are **invisible to naive scanners**. Four such files existed as of 2026-07-20; one carried undetected version drift that a clean-reporting validator had passed. Accordingly:

> **Any tool that enumerates the vault MUST use extended-length path handling** (the `\\?\` prefix or equivalent). A scan performed without it is **non-conforming, and its results are invalid regardless of what it reports** — including a clean report.

**Preventive rule.** The vault root occupies ~78 absolute characters, leaving ~182 of headroom beneath the 260 ceiling. Therefore:

> **A file's path relative to the vault root shall not exceed 180 characters.**

The margin between 180 and the remaining headroom is deliberate buffer against drive-prefix variation and sync-client overhead.

Because a long path is produced jointly by folder nesting and descriptive file names, the practical lever is §10's title discipline: keep descriptive wording bounded (the FND-0006 precedent — shorten the title, preserve the identifier).

**Existing violators are grandfathered.** Renames rewrite graph references (STD-0004) and are therefore an **owner decision**, never an incidental correction. A conforming scan reports violations; it does not fix them.

---

# 9. Folder Governance Rule

New top-level folders should not be created without:

- architectural justification,
- impact assessment,
- ADR when significant.

Purpose:

Prevent uncontrolled expansion.

---

# 10. Document Titles

Official titles must:

- preserve identifier,
- use descriptive wording,
- remain stable over time.

Preferred:

```
KOS-0009 - Knowledge Representation & Information Architecture Framework
```

Avoid:

```
Knowledge Notes
Info System
```

---

# 11. Version Convention

> **Reconciliation note (v1.1):** STD-0005 — Lifecycle & Revision Standard is authoritative on versioning. STD-0005 §16–19 defines the full `Major.Minor.Patch` scheme (Patch for corrections and wording fixes). The `Major.Minor` form shown here is the common case; where a patch-level correction is needed, follow STD-0005. This section is retained for naming-context only and does not override STD-0005.

Formal documents use:

```
Major.Minor
```

Examples:

```
0.1
0.2
1.0
2.0
```

---

## Major Version Change

Represents:

- architectural change,
- replacement,
- fundamental revision.

Example:

```
1.0 → 2.0
```

---

## Minor Version Change

Represents:

- clarification,
- refinement,
- non-structural improvement.

Example:

```
1.0 → 1.1
```

---

# 12. Status Convention

> **Reconciliation note (v1.1):** STD-0005 — Lifecycle & Revision Standard is authoritative on lifecycle. STD-0005 defines a **two-dimensional** model — Maturity (Proposed → Draft → Reviewed → Adopted) and Operational (Active → Superseded → Archived) — which are independent and must not be collapsed into one field. The single linear chain below predates STD-0005 and is superseded by it. In particular, "Review" reconciles to "Reviewed," and "Deprecated" is retired in favor of "Superseded." The field-level implementation of the two dimensions across existing documents is a pending migration (see the Standards Architecture Retrospective).

Approved lifecycle states (superseded — see note above; retained for historical reference):

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

# 13. Status Definitions

## Draft

Created but incomplete.

---

## Review

Awaiting evaluation.

---

## Adopted

Approved for use.

---

## Active

Currently implemented.

---

## Deprecated

No longer recommended but preserved.

---

## Archived

Historical record only.

---

# 14. Required Metadata Fields

All formal documents require:

```
title:
document_type:
version:
status:
created:
tags:
```

Additional metadata depends on document class.

---

# 15. Tag Naming Standard

Tags use:

```
PascalCase
```

Examples:

Correct:

```
#ProjectRelatio

#KnowledgeArchitecture

#ResearchMethodology
```

Avoid:

```
#knowledge_architecture

#research-methodology
```

---

# 16. Relationship Naming Standard

Relationships should use meaningful terminology.

Preferred:

```
supports

derived_from

influences

contrasts_with

part_of

implements

extends
```

Avoid:

```
related

misc

see_also
```

---

# 17. Document Lifecycle Standard

All documents follow:

```
Creation

↓

Classification

↓

Review

↓

Adoption

↓

Maintenance

↓

Revision

↓

Deprecation

↓

Archive
```

---

# 18. Identifier Registry Requirement

All formal identifiers must be recorded in a central registry.

Purpose:

Prevent:

- duplicate IDs,
- naming collisions,
- unclear ownership.

Implementation:

```
Identifier Registry
```

The Identifier Registry now exists (`05 Operations/Identifier Registry.md`, adopted 2026-07-09); it inventories all assigned identifiers per class and gives the next free number. Consult it before assigning an identifier and update it after. Maintenance is governed by OPS-0002.

---

# 19. Naming Exceptions

Exceptions may exist for:

- imported historical documents,
- external sources,
- quotations,
- archived materials.

Exceptions should preserve:

- original identity,
- source information,
- relationship to Project Relatio.

---

# 20. Governance

STD-0001 is maintained under:

KOS-0011 — Governance, Stewardship & Evolution Framework.

Changes require:

- documentation,
- review,
- version update.

---

# 21. Closing Principle

Project Relatio adopts:

> A well-named system is easier to understand, maintain, extend, and trust.

---

# 22. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial naming and identification standard|
|1.1|2026-07-09|Adopted|Added reconciliation notes deferring to STD-0005 as authoritative on versioning (§11) and lifecycle states (§12), resolving conflicts found in the pre-STD-0006 audit; non-destructive (original text retained)|
|1.2|2026-07-09|Adopted|Added INV (Investigation) and FND (Finding) identifier classes to §5, defined by KOS-0012 and demonstrated needed by the RQ-0001 pressure test|
|1.3|2026-07-09|Adopted|§18 updated: the Identifier Registry now exists (05 Operations), fulfilling the standard's registry requirement|
|1.4|2026-07-20|Adopted|**Path Length Constraint added as a subsection of §8, per ADR-GOV-0005 §5(c)** (which directed the operative text be amended into the document owning file-naming/path conventions; STD-0001 §7/§8/§10 is that owner). Records **§5(a) the hazard** — paths over the 260-character Windows `MAX_PATH` are invisible to naive scanners (four such files as of 2026-07-20, one carrying drift a clean-reporting validator had passed), making extended-length path handling **mandatory for all vault tooling** and any scan without it non-conforming and invalid; and **§5(b) the preventive rule** — relative path from vault root **≤180 characters**, with existing violators **grandfathered** because renames rewrite graph references and are owner-reserved. Cross-referenced to §10 title discipline as the practical lever. Placed as a `##` subsection to avoid renumbering §9–§22; no existing rule altered.|

---

# End STD-0001