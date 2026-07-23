---
title: FND-0002 - Jams as Emergent Instability
document_type: Finding Record
version: 0.4
status: Draft
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Base
  - Finding
  - Traffic Flow
parent_documents:
  - INV-0002 Phantom Traffic Jams
  - KOS-0010 Reasoning & Synthesis Framework
  - KOS-0006 Systems Modeling & Complexity Framework
related_documents:
  - CLM-0003 Endogenous Instability, Not Bottleneck
  - CLM-0004 Backward Stop-and-Go Waves
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Finding
  - TrafficFlow
  - Emergence
relationships:
  - type: derived_from
    target: CLM-0003
  - type: derived_from
    target: CLM-0004
  - type: related_to
    target: KOS-0006
  - type: part_of
    target: INV-0002
confidence:
  - component: overall
    level: 4
    label: High
reliance_tier: R0
reliance_note: "unassessed floor; predates verification-pass procedure."
review_cycle: 12
review_date: 2027-07-20
last_reviewed: 2026-07-20
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# FND-0002

# Jams as Emergent Instability

## Draft Finding Record

---

# 1. Statement

> Highway traffic jams can form with no bottleneck, accident, or obstruction. Above a **critical density**, free-flowing traffic becomes **dynamically unstable**: ordinary driver reaction-time delays amplify small perturbations, which grow into **self-sustaining stop-and-go waves that propagate backward** through traffic. The jam is an **emergent, self-organized** property of the collective system (KOS-0006), not a consequence of any individual vehicle or external cause.

---

# 2. Supporting Claims

- **CLM-0003** — the jam arises endogenously from instability above critical density, not from a bottleneck.
- **CLM-0004** — the resulting congestion is a backward-propagating stop-and-go wave.

---

# 3. Confidence (KOS-0003 §8)

**Level 4 — High.** Both supporting claims are Level 4, corroborated by an independent controlled experiment (SRC-0003) and convergent modeling (SRC-0004), with high scientific consensus on the qualitative mechanism. Held below Level 5 due to model-choice openness and the idealization of controlled/closed-track conditions.

---

# 4. Scope & Limitations

- Concerns the *bottleneck-free* case; real congestion often combines this instability with genuine bottlenecks.
- Quantitative thresholds (critical density) and the ~15–20 km/h wave speed are approximate/condition-dependent.

---

# 5. Relationships (STD-0004)

- `derived_from` CLM-0003, CLM-0004.
- `related_to` KOS-0006 (a canonical example of emergence/self-organization).
- `part_of` INV-0002.

---

# 6. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-09|Draft|Created for RQ-0002|
|0.2|2026-07-20|Draft|epistemic-field backfill, Stage 3|
|0.3|2026-07-21|Draft|review-field initialization per ADR-GOV-0008|
|0.4|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End FND-0002
