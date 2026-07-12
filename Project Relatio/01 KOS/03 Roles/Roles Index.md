---
title: Roles Index
document_type: Navigation Document
version: 1.1
status: Adopted
operational_status: Active
created: 2026-07-09
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - ROLE-0001 Knowledge Architect
  - ROLE-0002 Research Specialist
  - ROLE-0004 Critical Reviewer
  - ROLE-0005 Vision Steward
  - Standing Authorizations
tags:
  - ProjectRelatio
  - Roles
  - Index
  - Governance
---

# Roles Index

## Version 1.1

## Adopted Navigation Document

---

# 1. Purpose

The **canonical mapping** between the three layers that describe stewardship in Project Relatio. It exists because these three vocabularies drifted apart: the ROLE layer was authored without reference to the Kernel's ST-roles, duplicating them under different names (governance assessment, 2026-07-09; ADR-GOV-0001).

This index is the single source of truth for that mapping. **A ROLE may not exist without a warrant in CON-0003 or KOS-0011.**

---

# 2. The Three Layers

```
CON-0003 §4   Stewardship FUNCTIONS   (constitutional — what must be done)
      ↓            "The function is primary. The person or system performing it is secondary."
KOS-0011 §10  ST-NNN Stewardship ROLES  (kernel — names the functions)
      ↓
ROLE-NNNN     Role DEFINITIONS          (roles layer — implements them: authority, boundaries, workflows)
      ↓
.claude/agents/  Agents                 (RRI — how a role is invoked on this platform)
```

Changing an agent does not change the architecture. Changing a role's **authority** requires Vision Steward ratification.

---

# 3. Canonical Mapping

| Function (CON-0003 §4) | Stewardship Role (KOS-0011 §10) | Role Definition | Status | Agent (RRI) |
|---|---|---|---|---|
| §4.1 Vision Stewardship | *(none — constitutional only)* | **ROLE-0005** Vision Steward | **Adopted v1.0** | *(main session / owner)* |
| §4.2 Systems Architecture + §4.4 Knowledge Management | **ST-001** Knowledge Architect | **ROLE-0001** Knowledge Architect | **Adopted v1.1** | `knowledge-architect` |
| *(research conduct)* | **ST-002** Research Specialist | **ROLE-0002** Research Specialist | **Adopted v1.0** | `research-specialist` |
| *(domain interpretation)* | **ST-003** Domain Specialist | *unimplemented* | — | — |
| §4.3 Research Integrity + §4.5 External Review | **ST-004** Review Function | **ROLE-0004** Critical Reviewer | **Adopted v1.0** | `critical-reviewer` |

All active roles are now **Adopted** (owner-ratified 2026-07-09). Two refinements were applied at ratification: ROLE-0002 §4.2a (scope boundary) and ROLE-0004 §5 (procedural-independence limit).

**Retired:** ROLE-0003 Research Council Coordinator — no warrant at any layer; retired 2026-07-09 (`07 Archive/`). Its coordination function was absorbed by ROLE-0005.

**Unimplemented:** ST-003 Domain Specialist — no demonstrated need across INV-0001/0002/0003. Tracked in the Governance Backlog; do not implement speculatively.

---

# 4. Validation Authority (STD-0006 §8)

| Scope | Role |
|---|---|
| **Structural** — naming, metadata, classification, relationships, lifecycle, terminology, graph integrity | ROLE-0001 |
| **Epistemic** — evidence, reasoning, confidence calibration, bias, source fidelity, fabrication | ROLE-0004 |

Neither rules in the other's scope. Neither adjudicates **truth** (CON-0003 GP-003).

---

# 5. Constitutional Limits Binding Every Role

Any role may cite these against any other, including the Vision Steward:

- **GP-002** Evidence over preference.
- **GP-003** No authority over truth.
- **GP-004** Preserve disagreement — dissent is recorded, never discarded for lack of agreement.
- **GP-005** Governance reflexivity — governance examines itself by the same standards.
- **GP-006** Stewardship continuity — the project shall not depend on a single person.
- **GP-007** Governance/inquiry separation — governance sets *how* research occurs, not *what* it concludes.

---

# 6. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Created by the governance assessment (R1) to close the three-vocabulary drift and serve as the canonical Function → ST-role → ROLE → Agent mapping.|
|1.1|2026-07-09|Adopted|All active roles ratified to Adopted; statuses updated. Recorded the two ratification refinements (ROLE-0002 §4.2a; ROLE-0004 §5).|

---

# End Roles Index
