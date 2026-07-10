---
title: ADR-GOV-0001 - Governance and Role Reconciliation
document_type: Architecture Decision Record
version: 1.0
status: Adopted
created: 2026-07-09
decision_status: Accepted
decision_date: 2026-07-09
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - Roles Index
  - ROLE-0001 Knowledge Architect
  - ROLE-0004 Critical Reviewer
  - ROLE-0005 Vision Steward
  - Governance Backlog
  - Standing Authorizations
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - STD-0006 Review & Validation Standard
tags:
  - ProjectRelatio
  - ADR
  - Governance
  - Roles
---

# ADR-GOV-0001

# Governance and Role Reconciliation

## Adopted Architecture Decision Record

> **The first ADR in Project Relatio.** CON-0003 §7 has required ADRs since adoption; none existed. This record both *makes* a decision and *inaugurates the practice* (Governance Backlog GB-2026-010).

---

# 1. Context

On 2026-07-09 the Vision Steward commissioned a reflexive audit of authorities and guardrails — an exercise CON-0003 **GP-005** (*Governance Reflexivity*) mandates rather than merely permits.

The audit found that the Roles layer had been authored **without reading KOS-0011 §10**, producing a third vocabulary competing with two that already existed:

- **CON-0003 §4** defines Stewardship *Functions* (constitutional).
- **KOS-0011 §10** defines ST-NNN Stewardship *Roles* (kernel).
- **ROLE-NNNN** definitions duplicated both under new names.

Consequences discovered: ROLE-0004 was presented as a *new* role when it already existed as **ST-004 Review Function**; ROLE-0003 (Research Council Coordinator) had **no warrant at any layer**; the owner's own authority was undocumented; and the **anti-fabrication guardrail existed only in `.claude/agents/`** — the platform layer — meaning the single most important rule in a research system would vanish if the vault left Claude Code.

This is precisely the failure ROLE-0001 exists to prevent — *duplicated knowledge, inconsistent terminology* — committed by ROLE-0001.

---

# 2. Decision

> The three vocabularies **nest rather than compete**: CON-0003 Functions are primary; KOS-0011 ST-roles name them; ROLE-NNNN definitions implement them, and may not create a stewardship function without warrant in one of the two. The **Roles Index** is the canonical mapping. In consequence: ROLE-0004 is re-founded as ST-004's implementation, **ROLE-0003 is retired**, **ROLE-0005 (Vision Steward)** is created to document owner authority *and its constitutional limits*, and the **prohibition on fabricating evidence is elevated from the platform layer into KOS-0003 §12.1**.

---

# 3. Alternatives Considered

1. **Leave the vocabularies parallel, cross-referencing them.** Rejected — STD-0007 forbids exactly this drift, and three names for one function is the "duplicated knowledge" failure mode.
2. **Delete the ST-roles from KOS-0011 and let ROLE-NNNN stand alone.** Rejected — the Kernel and Constitution are higher governance levels; KOS-0011 §8 states lower levels *"may propose changes to higher levels but cannot override them."* The Roles layer cannot overwrite the Kernel to resolve its own error.
3. **Keep ROLE-0003 for symmetry.** Rejected — it had no warrant, no council to coordinate, and its own retirement condition had triggered. Retaining it would violate the owner's scope guardrail: *every addition must make the research better, not the architecture more complete.*
4. **Leave anti-fabrication in the agent files.** Rejected — an RKA/RRI leak placing the most critical epistemic guardrail in the most replaceable layer.

---

# 4. Reasoning

CON-0003 §4 settles the hierarchy directly: *"The function is primary. The person or system performing the function is secondary."* Functions therefore govern roles, not the reverse.

Retiring ROLE-0003 and documenting ROLE-0005 both serve **GP-006** (*the project shall not depend upon a single person*): the first removes ceremony, the second makes the owner's authority explicit, bounded, and **transferable**.

ROLE-0005 was deliberately written with **constitutional limits on the owner** (GP-002 evidence over preference; GP-003 no authority over truth; GP-004 preserve disagreement; GP-005 reflexivity; GP-007 governance/inquiry separation). Authority that cannot be cited against its holder is not governance.

Elevating anti-fabrication to KOS-0003 §12.1 reflects that Project Relatio's value rests entirely on claims remaining connected to evidence. Fabrication severs that connection *while preserving its appearance* — it is the one failure review cannot recover from, because it corrupts the record review depends on.

---

# 5. Consequences

**Accepted costs**
- Two Adopted Kernel documents (KOS-0003, KOS-0011) and one Adopted Standard (STD-0006) amended.
- A role retired within a day of authoring — visible churn, honestly recorded.
- ROLE-0002, ROLE-0004, ROLE-0005 remain Draft until their authority is ratified.

**Benefits**
- One canonical role vocabulary; drift closed and prevented by the Roles Index.
- The critical research guardrail is now platform-independent.
- Validation authority is split and bounded (STD-0006 §8); neither validator adjudicates truth.
- Dissent is preserved and Blocked verdicts are appealable — nobody, including the Reviewer and the owner, is unchecked.
- Open items consolidated into the long-mandated Governance Backlog.

**Affected objects**
- Amended: KOS-0003 (v1.1), KOS-0011 (v1.1), STD-0006 (v1.1), ROLE-0001 (v1.1), ROLE-0002, ROLE-0004.
- Created: ROLE-0005, Roles Index, Governance Backlog, Standing Authorizations, TPL-0005, this ADR.
- Retired: ROLE-0003 → `07 Archive/`.

---

# 6. Decision Authority

Architectural decision (CON-0003 §5.2), reserved to the **Vision Steward**. Proposed by the Knowledge Architect as a 13-item assessment; **approved in full by Brian Noon on 2026-07-09** with the instruction to execute all items.

---

# 7. Review Date

Revisit at the next STD-0006 §4.4 periodic audit, or immediately if a ROLE definition is proposed without a CON-0003 / KOS-0011 warrant.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|First ADR. Records the governance and role reconciliation, and inaugurates ADR practice under CON-0003 §7.|

---

# End ADR-GOV-0001
