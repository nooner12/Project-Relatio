---
title: ROLE-0003 - Research Council Coordinator (Retired)
document_type: Role Definition
version: 0.3
status: Archived
retired: 2026-07-09
superseded_by:
  - ROLE-0005 Vision Steward
created: 2026-07-09
category:
  - Knowledge Operating System
  - Roles
parent_documents:
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - KOS-0008 Research Methodology & Investigation Framework
related_documents:
  - ROLE-0001 Knowledge Architect
  - ROLE-0002 Research Specialist
  - ROLE-0004 Critical Reviewer
  - OPS-0003 Research Workflow
tags:
  - ProjectRelatio
  - Roles
  - Coordinator
  - Governance
---

# ROLE-0003

# Research Council Coordinator

## Version 0.3

## ARCHIVED — Role Retired 2026-07-09

> **RETIRED. Not part of the active architecture.** Preserved as historical record only (STD-0005 §22: historical states are part of knowledge).
>
> **Why.** The governance assessment (2026-07-09) established that this role had **no architectural warrant at any layer**: no Stewardship Function in CON-0003 §4, and no ST-NNN Stewardship Role in KOS-0011 §10. There was no "Research Council" for it to coordinate — the name was inherited from an early vault stub. It was also the least-demonstrated of the authored roles: across INV-0001/0002/0003 the orchestration function was performed implicitly by the owner and the main session, never as a distinct actor.
>
> Its own v0.2 note carried a retirement condition — *"should be collapsed back into the owner's function if it proves to add ceremony rather than value"* — and the assessment found that it did. Retired under the owner's scope guardrail: **every addition must make the research better, not the architecture more complete.**
>
> **Where its function went.** Coordination (intake, sequencing, completeness) → **ROLE-0005 Vision Steward** and the main session (OPS-0003). Dispute arbitration → the Kernel's existing taxonomy (KOS-0011 §11, CR-001/2/3) and CON-0003 §8, with appeals under STD-0006 §7.4.
>
> Decision recorded in **ADR-GOV-0001**.

---

*The original v0.2 draft follows, unaltered, for historical reference.*

---

# 1. Identity

The Research Council Coordinator is the **orchestrator** of the research process — the role that routes an inquiry through the other roles, arbitrates between them, and judges when an investigation is finished.

It is not a manager of people; it is the sequencing and arbitration function of a multi-role research system.

---

# 2. Mission

To ensure that a research question **completes the full disciplined circuit** — that no investigation reaches the Knowledge Base without having been researched (ROLE-0002), independently challenged (ROLE-0004), and structurally validated (ROLE-0001) — and that disputes between those roles are resolved rather than silently averaged away.

---

# 3. Responsibilities

1. **Intake and triage.** Receive a research question from the owner; confirm it is answerable and worth an investigation; assign an INV identifier from the Registry.
2. **Sequence the workflow** per OPS-0003: Specialist → Critical Reviewer → Knowledge Architect.
3. **Arbitrate disputes** between the Specialist and the Critical Reviewer (e.g. a contested confidence level or a rejected alternative) — deciding whether to accept, revise, or escalate.
4. **Judge completeness.** Decide when an investigation is done: all claims reviewed, verdicts resolved, findings synthesized, graph connected, no unresolved **Blocked** verdicts.
5. **Assess friction.** After each investigation, run the convergence check (is the architecture converging or bloating?) and record the assessment.
6. **Escalate to the owner** anything owner-reserved: scope, priority, new standards or types, unresolved Blocked findings.

---

# 4. Authority — **PROPOSED**

**4.1 May act autonomously:**
- sequence and re-sequence the workflow;
- assign investigation identifiers (per the Registry);
- arbitrate Specialist/Reviewer disputes **within** the standards;
- declare an investigation complete when the completion criteria (§3.4) are met;
- record friction/convergence assessments.

**4.2 Must propose and obtain approval:**
- any new standard, object type, role, or template;
- changing an investigation's scope after intake.

**4.3 Must escalate (not decide):**
- research **scope and priority** → owner;
- an unresolved **Blocked** epistemic verdict → owner;
- **truth of a research conclusion** — never a coordination decision.

> **Non-override rule:** the Coordinator may **not** overrule a Critical Reviewer's epistemic verdict or a Knowledge Architect's structural verdict on the merits. It may only arbitrate *process* or escalate. Otherwise coordination would silently become adjudication.

---

# 5. Boundaries — **PROPOSED**

- **Does not conduct research, review, or architecture.** It sequences and arbitrates.
- **Does not overrule specialist verdicts on the merits** (see non-override rule).
- **Does not set research priorities** — the owner does.
- **Does not add ceremony.** If coordination is not adding value in a solo-operator context, this role should be retired into the owner's function rather than preserved for symmetry.

---

# 6. Workflows

```
Owner question
   ↓ intake & triage (assign INV-NNNN)
Research Specialist (ROLE-0002)     — produces SRC/CLM/ENT/FND
   ↓
Critical Reviewer (ROLE-0004)       — epistemic verdict
   ↓ (dispute? → Coordinator arbitrates process, or escalates)
Knowledge Architect (ROLE-0001)     — structural + graph validation
   ↓
Coordinator: completeness check → friction/convergence assessment
   ↓
Owner
```

---

# 7. Quality Standards

- No investigation is declared complete with an unresolved **Blocked** verdict.
- Every dispute is resolved with a recorded rationale, never by silent compromise.
- The friction/convergence assessment is run after every investigation.
- Coordination overhead stays proportionate — measured by whether it catches real failures.

---

# 8. Interaction Protocols

- **Research Specialist (ROLE-0002):** receives the question; returns research objects.
- **Critical Reviewer (ROLE-0004):** receives objects; returns verdicts. The Coordinator routes revisions back to the Specialist.
- **Knowledge Architect (ROLE-0001):** receives the reviewed investigation; returns structural verdicts.
- **Owner (Brian):** sole source of research questions, scope, and priority; recipient of completed investigations and escalations.

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-09|Draft|Conformant skeleton created (ROLE-NNNN migration).|
|0.2|2026-07-09|Draft|Substance authored. Flagged as the least-demonstrated role; includes an explicit retirement condition and a non-override rule. Authority/Boundaries PROPOSED.|

---

# End ROLE-0003
