---
title: STD-0009 - Review & Revision Standard
document_type: Standards Document
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-21
category:
  - Knowledge Operating System
  - Standards
  - Review & Revision
parent_documents:
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - STD-0002 Metadata & YAML Standard
  - STD-0005 Lifecycle & Revision Standard
  - STD-0008 Epistemic State Standard
  - ADR-GOV-0008 - Review and Revision Framework
  - ADR-GOV-0007 - Reflexive Architecture Evolution
relationships:
  - type: depends_on
    target: ADR-GOV-0008
tags:
  - ProjectRelatio
  - Standards
  - Review
  - Revision
  - Governance
---

# STD-0009

# Project Relatio Review & Revision Standard

## Version 1.0

## Adopted Standards Document

---

# 1. Purpose

This standard gives KOS-0011 §12's declared review cycles (GR-001/GR-002/GR-003) their operational body: what surfaces an object for review, on what cadence, and what a review may and may not do. It is the lifecycle counterpart to STD-0005 for *revisitation* rather than transition, and the operational consumer of STD-0008's epistemic fields.

It enacts **ADR-GOV-0008 - Review and Revision Framework**.

---

# 2. Standard Principle

Project Relatio adopts:

> Knowledge ages. The system surfaces what warrants review; recorded governance decides. Mechanism proposes, never disposes.

---

# 3. Scope

Owns:

- the trigger vocabulary and its definitions (§4),
- the trigger → scope → act resolution (§5),
- the review acts and their bounds (§6),
- the cadence schedule (§7),
- the review-field semantics — `review_cycle`, `review_date`, `last_reviewed` (§8),
- the `bounded_by` semantics (§9),
- the queue-tool requirements (§10),
- the reflexive-queue connection (ADR-GOV-0007).

Does **not** own: field format (STD-0002), grade semantics (STD-0008 / KOS-0003), circuit procedure (OPS-0003), deprecation (KOS-0011 §13).

---

# 4. Trigger Vocabulary (ADR-GOV-0008 D1)

Reviews are surfaced by defined triggers, not personal noticing:

| Trigger | Definition | Detected by |
|---|---|---|
| `time_decay` | now ≥ `review_date` | queue tool, field query |
| `source_superseded` | a load-bearing source's `operational_status` → Superseded, or a superseding/contradicting object appears | queue tool, graph walk |
| `upstream_grade_change` | an object named in a component's `bounded_by` (or the record's `derived_from` where `bounded_by` absent) has a confidence change in its history | queue tool, graph walk |
| `contradiction` | a new finding/claim conflicts with a closed one (flagged by circuit sessions or reviews) | recorded flag → queue |
| `field_prose_divergence` | structured field disagrees with record prose (the CLM-0063 class) | recorded flag → queue |

Graph-event triggers are in scope for v1 (owner decision, ADR-GOV-0008 §3 alternative 1 rejected).

---

# 5. Trigger → Scope → Act (ADR-GOV-0008 D2)

| Trigger | Scope | Act |
|---|---|---|
| `time_decay` | whole record | Light re-affirmation |
| `source_superseded` | components whose `bounded_by` (or record `derived_from`) includes the source | Targeted re-grade |
| `upstream_grade_change` | components bounded by the changed object | Targeted re-grade |
| `contradiction` | the conflicting claims | Full OPS-0003 circuit |
| `field_prose_divergence` | the divergent field | Reconciliation |

---

# 6. Review Acts and Bounds (ADR-GOV-0008 D3)

- **Light re-affirmation.** Reviewer confirms the record still stands. Records "reviewed, unchanged"; sets `last_reviewed`; advances `review_date` per cadence. **MAY NEVER change a grade, a reliance tier, or any content.** If review reveals a needed change, it escalates to the appropriate act below.
- **Targeted re-grade.** Mini-circuit (Specialist proposal + Critical Review) on the affected components only; grade changes propagate per the layer rules; history rows everywhere touched.
- **Full circuit.** OPS-0003 in full; for contradiction-class review this is research, not maintenance.
- **Reconciliation.** Aligns a divergent field with prose (or corrects prose via a recorded owner decision); no re-research; history row states which side won and why.

All acts update `last_reviewed` and reset `review_date`. All grade changes obey STD-0008 (never averaged; layer-bounded; circuit-authorized).

---

# 7. Cadence Schedule (ADR-GOV-0008 D4)

Base cadence is set from the record's **weakest** confidence component:

| Weakest level | Base cycle |
|---|---|
| Level 5 (Very High) / Level 4 (High) | 12 months |
| Level 3 (Moderate) | 9 months |
| Level 2 (Low) | 6 months |
| Level 1 (Very Low) | 3 months |

**Reliance modifier:** R1 or R2 on all load-bearing loci extends the cycle ×1.5 (verified knowledge ages slower).

Cadence values are **maintenance-adjustable** (minor version bump of this standard), not constitutional.

---

# 8. Review Fields (format in STD-0002 v1.9; semantics here)

- `review_cycle` — the cadence in months, set from §7 at closure/initialization.
- `review_date` — next review due (`last_reviewed` + `review_cycle`).
- `last_reviewed` — date of the most recent review act (initialization: the record's closure or epistemic-backfill date).

Required on Claim Records and Finding Records. Initialization of existing records is **mechanical** (scripted from existing fields; no human walk).

---

# 9. bounded_by Semantics (ADR-GOV-0008 D5)

Optional list on a confidence component naming the objects bounding that component's grade. Required only where a component's dependencies differ from the record's `derived_from` edges. Absent → the record-level graph is the resolution surface.

**No retroactive backfill**; templates make new records born review-ready; existing records are enriched opportunistically when next touched.

`bounded_by` entries are graph claims (STD-0002 §12.1): they must resolve to existing objects, and graph tooling reads them for trigger resolution.

---

# 10. The Queue (ADR-GOV-0008 D6)

A tool (`tools/review_queue.py`) runs §4's detections against the vault and emits the current review queue: object, trigger, resolved scope, prescribed act. Reflexive structural recommendations (ADR-GOV-0007) enter the same queue.

The queue **PROPOSES**; every act is executed through a session under recorded governance — the queue never writes to records. Tooling must use extended-length path handling (STD-0001 §8).

---

# 11. Governance

Maintained under KOS-0011. The trigger vocabulary and act bounds are controlled (standards change); cadence values are maintenance-adjustable (§7).

---

# 12. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-21|Adopted|Initial review & revision standard enacting ADR-GOV-0008: trigger vocabulary with graph events, trigger→scope→act table, bounded review acts (re-affirmation never changes grades), epistemic-strength cadence with reliance modifier, review-field semantics, optional bounded_by, queue-proposes-governance-disposes.|

---

# End STD-0009
