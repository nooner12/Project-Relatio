---
title: ADR-GOV-0007 - Reflexive Architecture Evolution
document_type: Architecture Decision Record
version: 1.1
status: Adopted
operational_status: Active
created: 2026-07-20
decision_status: Accepted
decision_date: 2026-07-20
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - STD-0005 Lifecycle & Revision Standard
  - ADR-GOV-0006 - Tiered External-Reliance Model and Live-Retrieval Verification Channel
  - Governance Backlog
tags:
  - ProjectRelatio
  - ADR
  - ReflexiveEvolution
  - Governance
  - ArchitectureEvolution
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-20
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ADR-GOV-0007

# Reflexive Architecture Evolution

## Adopted Architecture Decision Record

> Governs how Relatio's own findings may inform the evolution of its knowledge architecture: provisional-anchor doctrine for bootstrap structures; reflexive findings inform but do not self-execute; a deferred, maturity-gated self-execution capability with an evidenced threshold and a transferable ratification seat. Cites STD-0005 §27 as its root. Inline pointer: Governance Backlog.

---

# 1. Context

Project Relatio is intended to become **reflexive**: as cross-investigation structure and relationships accumulate, the system's own findings should inform decisions about how its knowledge architecture grows — new structures, new questions, revised schemas. STD-0005 §27 already commits the architecture to this in principle: a knowledge architecture that cannot evolve becomes obsolete, and one that cannot preserve history cannot be trusted.

This ADR governs _how_ that evolution happens, so that "the investigation suggested it" never becomes a licence for casual restructuring — the precise failure the Architecture Baseline exists to prevent.

**Graduation path (recorded intention).** When the deferred self-execution capability (§5) is activated, the operative rules of this decision are consolidated into KOS-0011 (or a successor governance-framework document) as standing operational structure, and this ADR becomes the origin record of the reflexive principle and its guardrails — the same ADR-then-framework pattern by which ADR-GOV-0004's rules were enacted into the standards. Choosing the ADR form now is the first step of that path, not an alternative to it.

---

# 2. The Bootstrap Problem and Its Resolution

Some structures cannot be derived from findings because they are the precondition for producing those findings. The occasioning case: the first cross-investigation thematic schema — one cannot investigate what connects findings _through_ a system that already encodes those connections.

**Resolution — provisional anchors.** Such structures are laid as _deliberately minimal, explicitly provisional_ scaffolding: chosen to be as theory-light and revisable as possible, marked as scaffolding rather than settled truth, and expected to be corrected by the investigations they enable. An anchor is not claimed correct; it is claimed _sufficient to bootstrap_.

**Anchor discipline.** A provisional anchor must: (a) be labelled provisional in its own record; (b) name what would revise it (the kind of finding that would inform its correction); (c) be maximally revisable — chosen for ease of change, not permanence.

---

# 3. Reflexive Findings Inform; They Do Not Self-Execute (current rule)

An investigation that produces conclusions about Relatio's own structure produces **recommendations**, not changes. These recommendations are **inputs to an owner governance decision**, never self-applying.

This preserves the same separation the research circuit already uses (Specialist proposes → Reviewer disputes → owner ratifies), lifted one level to apply to the architecture itself. The reason is conflict-of-interest: an investigation that could silently reshape the structure it runs inside is grading its own homework. The brake is that structural change routes through recorded governance regardless of how strongly a finding recommends it.

---

# 4. Alternatives Considered

1. **No reflexive mechanism (owner-decree only, always).** Rejected — it forecloses the project's stated aim and wastes the very cross-investigation structure the architecture is built to accumulate.
2. **Allow reflexive self-execution now.** Rejected — the system has neither the accumulated internal data nor the demonstrated reliability to warrant autonomy; self-execution now would be the casual-restructuring failure mode with no brake.
3. **Record the principle in KOS-0011 now (framework form).** Rejected for the present — the operational machinery is deferred (§5) and does not yet exist; placing it in a framework document would describe machinery that isn't built (the state-that-isn't-real defect the D3 rule guards against). The ADR form is correct now; graduation to KOS-0011 is the recorded later step (§1).

---

# 5. Deferred Capability: Maturity-Gated Self-Execution

The long-term aim is a system that can execute structural revision reflexively — continually adjusting toward best-informed practice without external decree. This capability is **deferred, gated on a maturity threshold, and NOT in force.**

## 5.1 The threshold must be an evidenced condition, not a judgment call

Before reflexive self-execution may be enabled, defined criteria must be met and recorded — e.g. a demonstrated track record of recommendation quality, a sufficient volume of cross-validated internal data, and a measured reliability of past structural suggestions under governance. The specific criteria are authored when the capability is next seriously considered; **this ADR requires only that such criteria exist and be met before the gate opens.** "It seems mature enough now" is explicitly insufficient — that is the casual judgment the architecture guards against, applied to autonomy.

## 5.2 The ratification seat is designed to be transferable

The governance pipeline is structured so that the current human-held ratification seat is a **role that could later be occupied by the system** under §5.1's conditions — not a permanently human-shaped mechanism requiring reconstruction to admit a non-human actor. Design the seat now; decide who occupies it later. The transition, when it comes, is "the system meets the threshold and assumes an existing seat," not "rebuild governance."

---

# 6. Consequences

**Does:** authorize provisional anchors under anchor discipline; require reflexive findings to route through governance as recommendations; record the deferred self-execution capability and its gating principle; require the ratification seat to be transferable in design.

**Does not:** enable self-execution now; define the specific maturity criteria (deferred to when the capability is considered); permit any anchor to be treated as settled; alter the Architecture Baseline (Baseline changes route through their own recorded governance).

---

# 7. Decision Authority

Architectural/governance decision reserved to the **Vision Steward** (CON-0003 §5.2). Proposed on the support surface and **ratified in full by Brian Noon.**

---

# 8. Relationship to Other Objects

- Root: **STD-0005 §27** (evolution-with-preservation principle).
- Interacts with: **KOS-0011** (governance framework; graduation target); the **Architecture Baseline** (frozen; changes only through its own process); the **Epistemic State Standard** (reflexive recommendations about structure are themselves graded work and carry confidence/reliance like any finding); **ADR-GOV-0006** (the reliance model those graded recommendations inherit).

---

# 9. Review Trigger

Revisit if (a) the deferred self-execution capability (§5) is seriously considered — at which point §5.1's criteria are authored and the graduation to KOS-0011 (§1) is executed; (b) a provisional anchor proves non-revisable in practice (anchor discipline failed); or (c) a reflexive finding is found to have influenced structure without routing through governance (the §3 brake failed).

---

# 10. Revision History

| Version | Date       | Status  | Description                                                                                                                                                                                                                                                                                                                                            |
| ------- | ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1.0     | 2026-07-20 | Adopted | Initial reflexive-evolution instrument: provisional-anchor doctrine with anchor discipline; reflexive-findings-inform-not-self-execute rule; deferred maturity-gated self-execution with evidenced-threshold requirement and transferable-ratification-seat design; graduation path to KOS-0011 recorded. Cites STD-0005 §27; relates to ADR-GOV-0006. |
|1.1|2026-07-22|Adopted|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End ADR-GOV-0007