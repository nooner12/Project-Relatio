---
title: ENT-0003 - Allostatic Load
document_type: Entity Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-10
category:
  - Knowledge Base
  - Entity
  - Stress Physiology
parent_documents:
  - KOS-0004 Ontological Framework & Reality Modeling System
  - KOS-0012 Knowledge Object Model
related_documents:
  - INV-0005 Chronic Stress Interventions
  - SRC-0023 McEwen Allostatic Load Literature
  - CLM-0016 Social Connection Buffers Stress but Evidence Is Largely Observational
  - FND-0005 Durable Chronic-Stress Relief Requires Stressor Reduction Plus Response Regulation
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - AllostaticLoad
  - StressPhysiology
relationships:
  - type: derived_from
    target: SRC-0023
  - type: explains
    target: FND-0005
  - type: related_to
    target: CLM-0016
  - type: related_to
    target: CLM-0014
  - type: related_to
    target: CLM-0018
  - type: part_of
    target: INV-0005
---

# ENT-0003

# Allostatic Load

## Draft Entity Record

---

# 1. Identification
**Allostatic load** — the construct, coined by Bruce McEwen and Eliot Stellar (1993), naming the cumulative physiological "wear and tear" that results from repeated or prolonged activation of the body's stress-response systems.

# 2. Definition
The cumulative dysregulation across multiple physiological systems (neuroendocrine — e.g. cortisol; autonomic — e.g. reduced heart-rate variability; cardiovascular; metabolic; immune/inflammatory) produced when stress mediators are activated too often, for too long, or fail to shut off. **Allostasis** is the process of achieving stability through change; **allostatic load** is the price paid when that process is chronically over-used; **allostatic overload** is the pathological extreme.

# 3. Classification (per KOS-0004)
- **Category:** Abstract / theoretical construct (a scientific model), not a concrete object. It is an *explanatory and measurement* construct in stress physiology, typically operationalised as a composite index of biomarkers.
- **Ontological status (KOS-0004 humility):** Real as a pattern of measurable physiological change; **not** a single directly-measured quantity — its operationalisation (which biomarkers, what thresholds) varies between studies. Held as a well-supported model, not a settled measurement.

# 4. Why It Is Load-Bearing (relevance to INV-0005)
Allostatic load is why **durability is the right question** for RQ-0005. If chronic stress harms health by accumulating physiological load, then the target of *durable relief* is **reducing the accumulated load over time** — not merely producing a transient calm state. This grounds the investigation's central distinction:
- A technique that damps the **acute** response (a single slow-breathing session, a walk in nature) may not reduce **cumulative** load if the stressor persists and the load re-accumulates.
- Durable relief plausibly requires either removing/reducing the stressor (lowering the input) or sustainably raising the body's buffering capacity (sleep, fitness, social support) — the logic behind FND-0005.

# 5. Relationships (STD-0004)
- `derived_from` SRC-0023 (McEwen literature; SRC-0023 `defines` this entity).
- `explains` why FND-0005 frames durable relief as cumulative-load reduction.
- `related_to` CLM-0016 (social buffering of load), CLM-0014 (exercise and stress physiology), CLM-0018 (acute vs cumulative distinction).
- `part_of` INV-0005 conceptually (cross-investigation candidate: relevant to any future health-stress inquiry).

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-10|Draft|Created for RQ-0005. Grounds the durability framing; classified as a theoretical construct with operationalisation caveat.|

# End ENT-0003
