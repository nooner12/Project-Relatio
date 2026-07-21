---
title: CLM-0004 - Backward Stop-and-Go Waves
document_type: Claim Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Base
  - Claim
  - Traffic Flow
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0002 Phantom Traffic Jams
related_documents:
  - SRC-0003 Sugiyama 2008 Circular-Track Experiment
  - SRC-0004 Traffic-Flow Instability & Jamiton Modeling
  - CLM-0003 Endogenous Instability, Not Bottleneck
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - TrafficFlow
  - Waves
relationships:
  - type: derived_from
    target: SRC-0003
  - type: derived_from
    target: SRC-0004
  - type: related_to
    target: CLM-0003
  - type: supports
    target: FND-0002
  - type: part_of
    target: INV-0002
confidence:
  - component: direction
    level: 4
    label: High
  - component: near_constancy
    level: 4
    label: High
  - component: numeric_speed
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "unassessed floor; predates verification-pass procedure."
review_cycle: 9
review_date: 2027-04-21
last_reviewed: 2026-07-21
---

# CLM-0004

# Backward Stop-and-Go Waves

## Draft Claim Record

---

# Claim

> The congestion produced by this instability takes the form of **stop-and-go waves that propagate backward (upstream)** through traffic at a roughly constant characteristic speed (empirically on the order of 15–20 km/h), even as individual vehicles move forward.

---

# Claim Type (KOS-0003 §3)

**Descriptive** (the observed phenomenology) + **causal** (the wave is the propagating instability). 

---

# Evidence (KOS-0003 §4)

Type: **Empirical** (experiment + field observation) + **modeling**.

- SRC-0003: the jam cluster moved backward around the loop at a roughly constant speed.
- SRC-0004: continuum models produce backward-traveling "jamiton" solutions; the backward propagation speed is a robust output largely insensitive to fine detail.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)

- **Reliability: 5** — backward-propagating waves are among the most reproducible observations in traffic science.
- **Relevance: 5** — directly characterizes the jam's form.
- **Independence: 4** — experiment and models agree; field data (highway detector studies) also concur.
- **Quality: 4** — robust qualitatively; the exact ~15–20 km/h figure varies with conditions.
- **Limitations:** The numeric speed is approximate and condition-dependent; the *direction* (backward) and *near-constancy* are the robust facts.

---

# Consensus (KOS-0003 §9)

- Evidence strength: High. Consensus strength: High. The backward stop-and-go wave is textbook traffic-flow physics.

---

# Assumptions (KOS-0003 §10)

- That the ~15–20 km/h figure is reported as an order-of-magnitude, not a universal constant (linguistic/quantitative caution).

---

# Reasoning (KOS-0003 §7)

**Inductive** (generalizing a reproducible observation) + **deductive** (the wave direction follows from the models). Risk checked: false precision on the speed value — mitigated by stating it as approximate.

---

# Confidence (KOS-0003 §8)

**Level 4 — High** for direction and near-constancy; **Level 3** for any specific numeric speed.

---

# Limitations

- Numeric wave speed should not be quoted as exact.
- Applies to the congested-wave regime; free flow shows no such waves.

---

# Alternative Interpretations

1. **Waves move with traffic:** naive intuition. (Rejected — the *pattern* moves upstream while *cars* move downstream; a standard, well-documented distinction.)

---

# Relationships (STD-0004)

- `derived_from` SRC-0003, SRC-0004.
- `related_to` CLM-0003 (this wave is the visible form of that instability).
- `supports` FND-0002.
- `part_of` INV-0002.

---

# Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-09|Draft|Created for RQ-0002|
|0.2|2026-07-21|Draft|epistemic-field backfill, Stage 3|
|0.3|2026-07-21|Draft|review-field initialization per ADR-GOV-0008|

---

# End CLM-0004
