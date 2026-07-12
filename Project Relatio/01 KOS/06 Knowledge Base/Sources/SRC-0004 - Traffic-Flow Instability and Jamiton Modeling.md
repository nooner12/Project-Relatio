---
title: SRC-0004 - Traffic-Flow Instability and Jamiton Modeling
document_type: Source Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Base
  - Source
  - Modeling Literature
source_author: "Multiple: Bando et al. (Optimal Velocity Model, 1995); Aw & Rascle (2000) / Zhang (2002) (second-order models); Flynn, Kasimov, Nave, Rosales & Seibold ('jamitons', 2009)"
source_url: "Representative: https://doi.org/10.1103/PhysRevE.79.056113 (Flynn et al. 2009, 'Self-sustained nonlinear waves in traffic flow')"
publication_date: "1995–2009 (body of work; no single date)"
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - KOS-0006 Systems Modeling & Complexity Framework
related_documents:
  - INV-0002 Phantom Traffic Jams
  - SRC-0003 Sugiyama 2008 Circular-Track Experiment
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Source
  - TrafficFlow
  - Modeling
relationships:
  - type: supports
    target: CLM-0003
  - type: supports
    target: CLM-0004
  - type: related_to
    target: SRC-0003
  - type: derived_from
    target: KOS-0006
---

# SRC-0004

# Traffic-Flow Instability & Jamiton Modeling

## Draft Source Record

---

# 1. Identification

The body of traffic-flow modeling that explains phantom jams as a dynamical instability. Microscopic car-following models (e.g. the Optimal Velocity Model, Bando et al. 1995) show that above a critical density the uniform-flow solution becomes linearly unstable. Macroscopic second-order continuum models (Payne–Whitham; Aw–Rascle–Zhang) admit traveling-wave solutions — termed **"jamitons"** by Flynn, Kasimov, Nave, Rosales & Seibold (2009) — that are the mathematical analogue of the observed stop-and-go waves.

This is a *composite source* (a literature, not one paper); one representative citation is given.

---

# 2. Source Evaluation (KOS-0003 §6)

- **Authority:** High — established, peer-reviewed applied-mathematics / physics literature.
- **Transparency:** High — explicit models, analytical and numerical derivations.
- **Independence:** Modeling stream is theoretically independent of, yet convergent with, the empirical result (SRC-0003) — a strong triangulation.
- **Intent:** Explanatory/predictive modeling.

---

# 3. Limitations (what this source does NOT establish)

- Models are idealizations; parameter values (critical density, reaction time) vary by calibration.
- Multiple model families reproduce the phenomenon; the *qualitative* mechanism is robust, but no single "correct" model is settled.
- Continuum "jamiton" solutions are a mathematical idealization of discrete traffic.

---

# 4. Key Content Used

- Above a **critical density**, uniform flow is dynamically unstable (linear stability analysis).
- Perturbations grow into self-sustaining traveling waves (stop-and-go / jamitons).
- The mechanism is a systems-level instability (KOS-0006: feedback, emergence), not a property of any individual vehicle.

---

# 5. Relationships (STD-0004)

- `supports` CLM-0003, CLM-0004.
- `related_to` SRC-0003 (empirical counterpart).
- `derived_from` KOS-0006 framing (systems/complexity).

---

# 6. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-09|Draft|Created for RQ-0002|

---

# End SRC-0004
