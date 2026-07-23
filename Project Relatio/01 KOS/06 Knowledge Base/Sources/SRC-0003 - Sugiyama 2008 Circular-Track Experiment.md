---
title: SRC-0003 - Sugiyama 2008 Circular-Track Experiment
document_type: Source Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Base
  - Source
  - Empirical Study
source_author: "Yuki Sugiyama, Minoru Fukui, Macoto Kikuchi, Katsuya Hasebe, Akihiro Nakayama, Katsuhiro Nishinari, Shin-ichi Tadaki, Satoshi Yukawa"
source_url: "https://doi.org/10.1088/1367-2630/10/3/033001"
publication_date: 2008-03-04
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - INV-0002 Phantom Traffic Jams
  - SRC-0004 Traffic-Flow Instability & Jamiton Modeling
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Source
  - TrafficFlow
  - Experiment
relationships:
  - type: supports
    target: CLM-0003
  - type: supports
    target: CLM-0004
  - type: related_to
    target: SRC-0004
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# SRC-0003

# Sugiyama et al. (2008) — Circular-Track Experiment

## Draft Source Record

---

# 1. Identification

Sugiyama et al., "Traffic jams without bottlenecks — experimental evidence for the physical mechanism of the formation of a jam," *New Journal of Physics* 10 (2008) 033001. A controlled experiment: ~22 vehicles driven around a single-lane circular track (~230 m), instructed to maintain a uniform speed (~30 km/h). A stop-and-go jam emerged spontaneously and propagated backward around the loop.

---

# 2. Source Evaluation (KOS-0003 §6)

- **Authority:** High — peer-reviewed, physics collaboration; a landmark controlled demonstration.
- **Transparency:** High — controlled protocol, measured trajectories, open-access journal.
- **Independence:** Independent empirical test of a theoretical prediction (car-following instability); not derived from the models it corroborates.
- **Intent:** To test a physical hypothesis (jams can form without bottlenecks). Scientific-explanatory intent.

---

# 3. Limitations (what this source does NOT establish)

- A closed loop with fixed vehicle count is an idealization of open highway traffic (though the qualitative mechanism generalizes).
- Small N (~22 vehicles); instructed rather than naturalistic driving.
- Demonstrates the phenomenon and its onset; the quantitative parameters (critical density, wave speed) are refined by other work (see SRC-0004).

---

# 4. Key Content Used

- Spontaneous emergence of a jam from a near-uniform initial state (no bottleneck).
- The jam cluster propagates **backward** (upstream) at a roughly constant speed.
- Onset above a critical density — below it, uniform flow is stable.

---

# 5. Relationships (STD-0004)

- `supports` CLM-0003, CLM-0004.
- `related_to` SRC-0004 (modeling counterpart).

---

# 6. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-09|Draft|Created for RQ-0002|
|0.2|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End SRC-0003
