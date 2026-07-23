---
title: SRC-0078 - Fricker et al 2017 The Mycelium as a Network
document_type: Source Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-19
source_author: "Fricker, M.D.; Heaton, L.L.M.; Jones, N.S.; Boddy, L. (2017)"
source_url: "'The Mycelium as a Network', Microbiology Spectrum 5(3): FUNK-0033-2017; doi:10.1128/microbiolspec.FUNK-0033-2017"
publication_date: "2017"
category:
  - Knowledge Base
  - Source
  - Secondary
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - INV-0012 Mycelial Networks and Fungal Cognition
  - CLM-0060 Resource Transport
  - CLM-0062 Chemical Signaling and Whole-Colony Integration
  - CLM-0065 The Neural-Network Analogy
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Source
  - Mycelium
  - NetworkTopology
relationships:
  - type: supports
    target: CLM-0060
  - type: supports
    target: CLM-0062
  - type: supports
    target: CLM-0065
  - type: part_of
    target: INV-0012
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-19
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# SRC-0078

# Fricker, Heaton, Jones & Boddy 2017 — "The Mycelium as a Network"

## Draft Source Record

---

# 1. Identification
Mark D. Fricker, Luke L. M. Heaton, Nick S. Jones & Lynne Boddy, "The Mycelium as a Network," *Microbiology Spectrum* 5(3): FUNK-0033-2017 (2017; also in *The Fungal Kingdom*, ASM/Wiley). A synthesis treating the mycelium as a **self-organized, adaptive transport network** analyzed with graph-theoretic and biophysical tools. **In this KB it is the anchor for network-level transport, whole-colony integration, and the structural side of the neural-network analogy** — authored by the same group that did the *Physarum* network-optimization work (SRC-0089), so it is well placed to draw the analogy carefully.

# 2. Source Evaluation (KOS-0003 §6)
- **Authority:** High. Fricker (Oxford) is a leading analyst of biological transport networks; co-authored with Boddy (fungal ecology) and Jones (applied mathematics/networks).
- **Transparency:** High. Quantitative network metrics, flow modelling, and imaging; methods explicit.
- **Independence:** Strong. Biophysical/mathematical framing, not a cognition-enthusiast source; treats "intelligence"-style language with restraint.
- **Intent:** To characterize how network structure governs resource flow and how flow reshapes structure (co-adaptation), and to place fungal networks among other adaptive biological networks.

# 3. Limitations (what this source does NOT establish)
- Establishes **network structure, transport, selective reinforcement, and topological optimization**; does **not** establish cognition, learning, or that structural analogy to neural nets extends to dynamics/function (those disanalogies are CLM-0065's content).
- Network optimization is explained by **local flow-driven reinforcement rules**, not central control — a point that constrains any "central integrator" reading.

# 4. Key Content / Passages Used
- The mycelium is a network that "explores new territory… while maintaining an effective internal transport system in the face of continuous attack or random damage," adapting by **selective reinforcement of major transport routes and recycling of redundant material.**
- Network structure and resource flow are **mutually coupled**: flows modify architecture, which in turn modifies flows.
- Provides the structural vocabulary (nodes/anastomoses, hubs, transport efficiency vs. resilience trade-offs) used to grade the structural axis of the neural analogy.

# 5. Relationships (STD-0004)
- `supports` CLM-0060 (transport), CLM-0062 (whole-colony integration), CLM-0065 (structural axis of the analogy).
- `part_of` INV-0012.

# 6. Verification (STD-0006 §5.7 / §7.5)
**Live-verified this session (strong).** Title, authorship (Fricker, Heaton, Jones, Boddy), venue (*Microbiology Spectrum*, 2017; reprinted in *The Fungal Kingdom*, Wiley) confirmed via ASM/Wiley catalogue listings and the markfricker.org publication list. The load-bearing paraphrases (self-organized adaptive network; selective reinforcement; structure–flow coupling) match the abstracts/summaries returned.

# 7. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-19|Draft|Created for RQ-0012. Network-transport and structural-analogy anchor (CLM-0060/0062/0065). Live-verified strong.|
|0.2|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

# End SRC-0078
