---
title: CLM-0003 - Endogenous Instability, Not Bottleneck
document_type: Claim Record
version: 0.2
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
  - CLM-0004 Backward Stop-and-Go Waves
  - KOS-0006 Systems Modeling & Complexity Framework
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - TrafficFlow
  - Emergence
relationships:
  - type: derived_from
    target: SRC-0003
  - type: derived_from
    target: SRC-0004
  - type: related_to
    target: KOS-0006
  - type: supports
    target: FND-0002
  - type: part_of
    target: INV-0002
confidence:
  - component: overall
    level: 4
    label: High
reliance_tier: R0
reliance_note: "unassessed floor; predates verification-pass procedure."
---

# CLM-0003

# Endogenous Instability, Not Bottleneck

## Draft Claim Record

---

# Claim

> Phantom highway jams arise **endogenously**: above a critical traffic density, uniform flow is dynamically unstable, so ordinary driver reaction-time delays amplify small perturbations into congestion — **without any external bottleneck, accident, or obstruction**.

---

# Claim Type (KOS-0003 §3)

**Causal** (primary) — it asserts a generative mechanism (instability → jam). Causal claims require mechanism, evidence, alternatives, and confounding analysis (KOS-0003 §3.2).

---

# Evidence (KOS-0003 §4)

Type: **Empirical** (controlled experiment) + **modeling/analytical**.

- SRC-0003: in a bottleneck-free closed track, a jam emerged spontaneously above a critical density — direct empirical demonstration that no bottleneck is needed.
- SRC-0004: linear stability analysis of car-following and continuum models shows the uniform-flow state becomes unstable above a critical density; perturbations grow rather than damp.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)

- **Reliability: 5** — controlled experiment + independent theory converge.
- **Relevance: 5** — directly targets the "no bottleneck" claim.
- **Independence: 5** — empirical (SRC-0003) and theoretical (SRC-0004) streams are independent and agree (triangulation).
- **Quality: 4** — high; the closed-track idealization is the main caveat.
- **Limitations:** Establishes the mechanism *can* and *does* produce bottleneck-free jams; exact critical-density values are calibration-dependent.

> **Evidence-structure note (architecture):** KOS-0003 §5's 0–5 scale captures evidence *quality* but has no field for quantitative specifics (sample size, effect size, replication count, consensus level). For empirical claims this is a gap — flagged as F-10 in the Second-Run Friction Assessment. (KOS-0003 §9 "Consensus Evaluation" partly compensates; see below.)

---

# Consensus (KOS-0003 §9)

- Evidence strength: **High.**
- Consensus strength: **High** — the qualitative mechanism (density-driven instability producing phantom jams) is broadly accepted in traffic-flow physics.
- Relationship: strongly supported; disagreement is over model *choice* and parameters, not the mechanism.

---

# Assumptions (KOS-0003 §10)

- That closed-track dynamics generalize to open highways (methodological; supported by consistent field observations).
- That aggregate driver behavior is adequately captured by car-following models (methodological).

---

# Reasoning (KOS-0003 §7)

**Abductive + inductive.** Instability is the best explanation for bottleneck-free jams (abductive), and it generalizes from the controlled experiment and multiple model families (inductive). Reasoning risks checked: **confounding** (the closed-track design removes bottleneck confounds by construction); overgeneralization from one experiment (mitigated by independent modeling).

---

# Confidence (KOS-0003 §8)

**Level 4 — High.** Experimentally demonstrated, theoretically explained, and broadly accepted. Not Level 5 only because of idealization and model-choice openness.

---

# Limitations

- The *existence* and *mechanism* are settled; precise thresholds are context-dependent.
- Real jams often mix endogenous instability with genuine bottlenecks; this claim isolates the bottleneck-free case.

---

# Alternative Interpretations

1. **Hidden micro-bottleneck:** every jam has some tiny trigger. (Partly true as a *seed*, but SRC-0003 shows no *sustained* bottleneck is needed; instability, not the seed, produces the jam.)
2. **Pure driver error:** jams are just bad individual driving. (Rejected — the phenomenon is collective/emergent, arising even with cooperative uniform-speed instructions.)

---

# Relationships (STD-0004)

- `derived_from` SRC-0003, SRC-0004.
- `related_to` KOS-0006 (an instance of emergent, self-organized system behavior).
- `supports` FND-0002.
- `part_of` INV-0002.

---

# Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-09|Draft|Created for RQ-0002|
|0.2|2026-07-20|Draft|epistemic-field backfill, Stage 3|

---

# End CLM-0003
