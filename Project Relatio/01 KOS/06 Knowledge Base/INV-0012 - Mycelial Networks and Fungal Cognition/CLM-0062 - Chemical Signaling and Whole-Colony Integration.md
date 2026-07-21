---
title: CLM-0062 - Chemical Signaling and Whole-Colony Integration
document_type: Claim Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-07-19
category:
  - Knowledge Base
  - Claim
  - Mycology
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0012 Mycelial Networks and Fungal Cognition
related_documents:
  - SRC-0078 Fricker et al 2017 The Mycelium as a Network
  - SRC-0085 Kiers et al 2011 Reciprocal Rewards Mycorrhizal Symbiosis
  - SRC-0082 Buffi et al 2025 Electrical Signaling in Fungi Review
  - FND-0012 Mycelial Network Signaling and the Bounds of Fungal Cognition
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - ChemicalSignaling
  - Integration
relationships:
  - type: derived_from
    target: SRC-0078
  - type: derived_from
    target: SRC-0085
  - type: derived_from
    target: SRC-0082
  - type: supports
    target: FND-0012
  - type: part_of
    target: INV-0012
confidence:
  - component: overall
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "unassessed floor; predates verification-pass procedure."
review_cycle: 9
review_date: 2027-04-20
last_reviewed: 2026-07-20
---

# CLM-0062

# The Mycelial Colony Behaves as a Physiologically Integrated Unit — Coordinating Transport and Development Across Distance via Chemical/Cytoplasmic (and Likely Ionic, e.g. Ca²⁺) Signaling Plus Mass Flow — Established at Moderate for Integration, With the Specific Non-Electrical Molecular Mechanisms Less Fully Pinned Down

## Draft Claim Record

---

# Claim
> A mycelial colony is not a bag of independent hyphae but a **physiologically integrated unit**: it coordinates resource allocation and developmental switching across the whole network through **cytoplasmic streaming, mass flow, diffusible chemical signals, and intracellular ionic signaling (calcium is the canonical eukaryotic second messenger, and is implicated in fungal signaling)** — non-electrical coordination that regulates "who gets what" and where growth/reproduction occurs. **Whole-colony integration is well-supported (Moderate); the specific molecular signaling pathways (e.g. exact Ca²⁺-wave roles) are less exhaustively established.**

---

# Claim Type (KOS-0003 §3)
**Descriptive** (the colony is integrated) **+ causal** (chemical/ionic signaling + mass flow *coordinate* whole-colony behavior).

---

# Evidence (KOS-0003 §4)
Type: **Empirical**.
- **SRC-0078 (Fricker et al. 2017):** structure–flow coupling integrates the network; local flow-driven reinforcement rules coordinate global transport **without a central controller.**
- **SRC-0085 (Kiers et al. 2011):** in the mycorrhizal symbiosis, reciprocal, discriminating resource exchange **regulates allocation** across the interface — a concrete mechanism by which distributed exchange is coordinated (biochemical/market, not cognitive).
- **SRC-0082 (Buffi et al. 2025):** situates electrical alongside chemical/ionic signaling in fungi; notes the field is real but under-characterized — supports "integration occurs" while cautioning against precise mechanistic overclaim.
- **General cell biology (parametric):** calcium signaling is a conserved intracellular second-messenger system across eukaryotes including fungi; invoked here as a plausible ionic channel, flagged as not independently re-verified with a fungal-Ca²⁺ primary this session.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: 3 — whole-colony integration is robustly evidenced (transport, reinforcement, coordinated development); the *specific* non-electrical signaling molecules are less pinned in this evidence set.
- Relevance: 4 — directly answers "signal internally" beyond electrical spiking.
- Independence: 4 — network biophysics (Fricker) and symbiosis biology (Kiers) converge on distributed coordination.
- Quality: 3 — strong on integration; the Ca²⁺-specific mechanism rests partly on general (non-fungal-specific, parametric) knowledge.
- Limitations: establishes integration and regulated exchange; does **not** pin the exact molecular signal set, and does **not** imply cognition.

---

# Source Evaluation
Kiers is especially valuable because it demonstrates coordinated, discriminating allocation in explicitly **non-cognitive, market-theoretic** terms — showing that "coordination" need not mean "decision-making." Fricker shows global order from local rules (no central integrator), which also constrains the neural analogy (CLM-0065).

---

# Assumptions (KOS-0003 §10)
- **Ontological:** the colony is a legitimate unit of physiological integration (well-supported for connected mycelium).
- **Methodological:** calcium's conserved second-messenger role in eukaryotes extends to fungal coordination — plausible but here parametric, flagged.

---

# Reasoning (KOS-0003 §7)
**Inductive/abductive.** **Risks checked:** *coordination→cognition slide* (named — integration is physiological, achieved by local rules + chemistry, not deliberation; Kiers demonstrates the non-cognitive route); *mechanism overclaim* (named — the specific Ca²⁺ pathway is not independently verified here, so the claim is capped at "integration, likely including ionic signaling," not a precise pathway).

---

# Confidence (KOS-0003 §8)
**Level 3 (Moderate)** — that the colony is a physiologically integrated unit coordinated by non-electrical (chemical/cytoplasmic/likely ionic) means plus mass flow. **Why not Level 4:** the *specific* molecular signaling mechanisms (especially the precise role of Ca²⁺) are not fully established in this evidence set and partly rest on general cell biology. **Why not lower:** integration itself (transport, reinforcement, coordinated development, regulated exchange) is well-evidenced and uncontested.

---

# Limitations
- Licenses "the colony is physiologically integrated and coordinates via chemistry/flow (and likely ions)," **not** a precise molecular signaling map, and **not** any cognitive/decisional reading.

---

# Alternative Interpretations
1. **No genuine integration (each hypha autonomous).** Rejected: transport, reinforcement, and coordinated fruiting demonstrate colony-level coordination.
2. **Cognitive coordination.** Deferred to CLM-0066; not required — local rules + chemistry (Fricker, Kiers) suffice, and are the more parsimonious account.
3. **Electrical signaling as the primary integrator.** Held open but not assumed — CLM-0061 shows the electrical datum is fragile; integration is better evidenced through chemistry/flow than through the contested spikes.

---

# Relationships (STD-0004)
- `derived_from` SRC-0078, SRC-0085, SRC-0082.
- `supports` FND-0012.
- `part_of` INV-0012.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-19|Draft|Created for RQ-0012. Level 3 (Moderate): whole-colony physiological integration via chemical/cytoplasmic/likely-ionic signaling + mass flow; integration well-evidenced (Fricker, Kiers), specific molecular mechanisms (Ca²⁺) less pinned and partly parametric (flagged). Coordination framed non-cognitively. Pending review/validation.|
|0.2|2026-07-20|Draft|epistemic-field backfill, Stage 3|
|0.3|2026-07-21|Draft|review-field initialization per ADR-GOV-0008|

# End CLM-0062
