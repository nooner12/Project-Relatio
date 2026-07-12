---
title: ROLE-0005 - Vision Steward
document_type: Role Definition
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Operating System
  - Roles
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - ROLE-0001 Knowledge Architect
  - ROLE-0002 Research Specialist
  - ROLE-0004 Critical Reviewer
  - Standing Authorizations
tags:
  - ProjectRelatio
  - Roles
  - VisionSteward
  - Governance
---

# ROLE-0005

# Vision Steward

## Version 1.0

## Adopted Role Definition

> **Adopted 2026-07-09.** Currently performed by **Brian Noon**. In ratifying this role, the owner did more than grant himself authority — he **accepted the constitutional limits in §4.2 as binding on himself** (may not determine truth, override evidence, dictate conclusions, discard dissent, or exempt himself from review). That acceptance is what makes the governance real rather than decorative. Written down so the function is auditable and, per CON-0003 GP-006, **transferable** beyond any single person.

---

# Architectural Warrant

- **Implements:** CON-0003 §4.1 **Vision Stewardship Function**.
- **Stewardship role (KOS-0011 §10):** none — the Kernel's ST-roles cover architecture, research, domain, and review, but not vision. This role derives directly from the Constitution.

Per CON-0003 §4: *"The function is primary. The person or system performing the function is secondary."* This document defines the **function**; Brian currently performs it.

---

# 1. Identity

The Vision Steward protects the **identity, mission, and foundational principles** of Project Relatio, and is the final authority on decisions the architecture reserves to the owner.

Stewardship is not ownership. Per CON-0003 §2: *ownership implies control; stewardship implies responsibility.* The Vision Steward serves the continued integrity of the system, not personal preference.

---

# 2. Mission

To ensure Project Relatio remains **what it is for** — currently, a system that conducts thorough and disciplined research on the Steward's questions — and that it evolves through governance rather than drift.

---

# 3. Responsibilities

1. **Set the research agenda** — pose questions, set scope and priority.
2. **Ratify governance** — role authority, new standards, new object types, constitutional and architectural decisions.
3. **Approve governed change** — batch migrations, restructuring, Adopted-status changes, un-deferrals.
4. **Resolve escalations** — contested `Blocked` verdicts (STD-0006 §7.4), unresolved CR-001/2/3 conflicts, and Specialist↔Reviewer disputes on the merits.
5. **Grant and revoke Standing Authorizations** (see `Standing Authorizations`), keeping delegation explicit rather than implicit.
6. **Guard the scope guardrail** — apply the test *does this make the research better?* and remove what does not.
7. **Coordination** — intake, sequencing, and completeness of investigations (absorbed from the retired ROLE-0003).

---

# 4. Authority — *ratified by owner 2026-07-09*

**4.1 Reserved decisions (the Vision Steward alone):**
- constitutional decisions (CON-0003 §5.1): mission, foundational principles, project identity;
- architectural decisions (CON-0003 §5.2): new or amended Standards, Kernel documents, object types, roles, and role authority;
- Adopted-status changes; batch migrations; restructuring; un-deferring deferred items;
- research scope and priority;
- granting, scoping, and revoking Standing Authorizations.

**4.2 Bounded by the Constitution — the Vision Steward may NOT:**
- **determine truth** (GP-003: governance may not establish factual conclusions through authority alone);
- **override evidence with preference** (GP-002);
- **dictate research conclusions** (GP-007: governance may establish *how* research occurs, not *what* it must conclude);
- **discard reasoned dissent** for lack of agreement (GP-004);
- **exempt itself from review** (GP-005: governance must be capable of examining itself).

> These are not courtesies. They are constitutional limits on the owner's authority, and any role may cite them.

**4.3 Delegable:** anything in §4.1 except constitutional decisions may be delegated by a recorded Standing Authorization, satisfying GP-006 (*the project shall not depend upon a single person*).

---

# 5. Boundaries — *ratified by owner 2026-07-09*

- Does not conduct research, review, or architecture — those are ROLE-0002, ROLE-0004, ROLE-0001.
- Does not adjudicate whether a claim is true; only whether the process that produced it was sound and whether the work should proceed.
- Does not resolve disputes by fiat: escalations are resolved through CON-0003 §8, with the dissenting position preserved.

---

# 6. Workflows

- **Research intake:** pose question → assign to Research Specialist (via the main session) → receive completed investigation after epistemic and structural validation.
- **Escalation:** receive contested Blocked verdicts and CR-001/2/3 conflicts with both positions recorded; resolve per CON-0003 §8; document the outcome and the dissent.
- **Governance:** receive proposals from ROLE-0001; ratify, revise, or decline; record significant decisions as ADRs (CON-0003 §7).

---

# 7. Quality Standards

- No decision reserved to this role is taken by another role without a recorded Standing Authorization.
- Every escalation outcome preserves the dissenting position.
- Significant architectural decisions carry an ADR.
- The scope guardrail is applied: additions that do not improve research are removed.
- Delegation increases over time (GP-006) rather than concentrating.

---

# 8. Interaction Protocols

- **Knowledge Architect (ROLE-0001):** proposes; the Steward ratifies or declines. The Architect may act autonomously only within §4.1 of its own definition or a Standing Authorization.
- **Research Specialist (ROLE-0002):** receives questions and scope from the Steward.
- **Critical Reviewer (ROLE-0004):** escalates contested Blocked verdicts to the Steward; the Steward may not overrule a verdict on the *merits of the evidence*, only rule on process and whether work proceeds.

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-09|Draft|Created by the governance assessment (R12) to complete and make transferable the authority model. Implements CON-0003 §4.1. Authority and Boundaries PROPOSED, including explicit constitutional limits on the owner.|
|1.0|2026-07-09|Adopted|Owner ratified. In doing so, accepted the §4.2 constitutional limits as binding on himself. No changes to the drafted authority were required.|

---

# End ROLE-0005
