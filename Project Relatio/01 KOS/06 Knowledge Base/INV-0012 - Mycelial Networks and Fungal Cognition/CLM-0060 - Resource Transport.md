---
title: CLM-0060 - Resource Transport
document_type: Claim Record
version: 0.4
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
  - SRC-0077 Boddy Mycelial Foraging Cord-Forming Fungi
  - SRC-0083 Simard et al 1997 Net Transfer of Carbon Between Trees
  - FND-0012 Mycelial Network Signaling and the Bounds of Fungal Cognition
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - Transport
  - Translocation
relationships:
  - type: derived_from
    target: SRC-0078
  - type: derived_from
    target: SRC-0077
  - type: derived_from
    target: SRC-0083
  - type: supports
    target: FND-0012
  - type: part_of
    target: INV-0012
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
    date: 2026-07-19
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# CLM-0060

# Mycelial Networks Translocate Nutrients, Carbon and Water Over Distance — Bidirectionally and Under Source–Sink Regulation — via Reinforced Transport Cords; a Well-Established Descriptive Fact (High) About Network Physiology That Says Nothing Yet About Cognition

## Draft Claim Record

---

# Claim
> Mycelial networks **actively translocate** nutrients, carbon and water over distance through their hyphae/cords, **bidirectionally** and under **source–sink regulation** (flux tracks demand gradients across the network), supported by cytoplasmic streaming and mass flow through reinforced transport conduits. This is a well-established descriptive fact of network **physiology**.

---

# Claim Type (KOS-0003 §3)
**Descriptive** (with an embedded, well-supported physiological mechanism: source–sink-regulated translocation).

---

# Evidence (KOS-0003 §4)
Type: **Empirical** (isotope tracing; quantitative flow imaging; network modelling).
- **SRC-0078 (Fricker et al. 2017):** network structure and resource flow are mutually coupled; major transport routes are selectively reinforced; flows modelled quantitatively across the mycelium.
- **SRC-0077 (Boddy):** biomass and nutrients are **reallocated** across cord systems toward new resources — directional, demand-linked translocation.
- **SRC-0083 (Simard et al. 1997):** field isotope labelling shows **bidirectional** carbon movement with a **net flux toward the sink** (shaded plant), i.e. source–sink regulation of translocation. *(Used here only for the transport datum; the contested inter-plant/network-mediation interpretation is CLM-0063.)*

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: 4 — translocation is directly measured (isotopes, imaging) across many systems; robust.
- Relevance: 5 — directly answers the "transport resources" part of the primary question.
- Independence: 4 — network biophysics (Fricker), ecology (Boddy), field isotope work (Simard) converge.
- Quality: 4 — strong methods; some flux magnitudes are system-specific.
- Limitations: establishes **that** networks translocate under source–sink control; does **not** establish that regulation is cognitive or that inter-*plant* transfer is ecologically significant (CLM-0063).

---

# Source Evaluation
The transport datum is agreed across poles — even Karst et al. (SRC-0084), the skeptics on the *wood-wide-web narrative*, do not dispute that carbon can move; they dispute significance and network-mediation. So the *intra-network* transport claim is on very firm ground.

---

# Assumptions (KOS-0003 §10)
- **Methodological:** isotope label recovered in a sink reflects genuine translocation (well-validated).
- **Ontological:** "source–sink regulation" is a physiological/physical control regime, not a deliberative one — stated to pre-empt the register slide.

---

# Reasoning (KOS-0003 §7)
**Inductive** from direct measurement. **Risks checked:** *conflating intra-network transport (firm) with inter-plant CMN transfer (contested)* — named and firewalled to CLM-0063; *reading "regulation" as decision* — named, capped at physiological control.

---

# Confidence (KOS-0003 §8)
**Level 4 (High)** — that networks translocate resources bidirectionally under source–sink regulation. **Why not Level 5:** reserved; some flux magnitudes/mechanistic details (e.g. relative roles of mass flow vs. active transport) remain system-specific and partly open. **Why not lower:** the core phenomenon is directly measured, independent, and uncontested.

---

# Limitations
- Licenses "networks translocate resources under source–sink control," **not** "networks decide how to allocate" (mechanism ≠ deliberation), and **not** any claim about ecologically significant tree-to-tree transfer (CLM-0063).

---

# Alternative Interpretations
1. **Passive diffusion only.** Rejected: directional, demand-linked, faster-than-diffusion transport through reinforced cords indicates active/regulated translocation, not mere diffusion.
2. **Cognitive allocation.** Deferred to CLM-0062/0066; not needed to explain the transport datum, which market-style/source–sink models (SRC-0085) already account for.

---

# Relationships (STD-0004)
- `derived_from` SRC-0078, SRC-0077, SRC-0083.
- `supports` FND-0012.
- `part_of` INV-0012.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-19|Draft|Created for RQ-0012. Level 4 (High): bidirectional, source–sink-regulated translocation through reinforced cords; datum agreed across poles. Firewalled from the contested inter-plant transfer (CLM-0063). Pending review/validation.|
|0.2|2026-07-20|Draft|epistemic-field backfill, Stage 3|
|0.3|2026-07-21|Draft|review-field initialization per ADR-GOV-0008|
|0.4|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

# End CLM-0060
