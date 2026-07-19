---
title: CLM-0029 - Codification Value and Tacit Tradeoff
document_type: Claim Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-12
category:
  - Knowledge Base
  - Claim
  - Knowledge Management
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0007 Formal Constraints in Knowledge Systems
related_documents:
  - SRC-0036 Hansen Nohria Tierney 1999 Strategy for Managing Knowledge
  - SRC-0044 Polanyi 1966 The Tacit Dimension
  - FND-0007 Value and Failure of Formal Constraints
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - Codification
  - TacitKnowledge
relationships:
  - type: derived_from
    target: SRC-0036
  - type: derived_from
    target: SRC-0044
  - type: supports
    target: FND-0007
  - type: part_of
    target: INV-0007
---

# CLM-0029

# Codifying Knowledge Into Formal Reusable Structures Has Real Value But Trades Off Against Tacit/Personalized Knowledge; the Right Degree Is Contingent

## Draft Claim Record

---

# Claim
> **Codification** — extracting knowledge from individuals into formal, person-independent, reusable structures (documents, databases, schemas) — delivers genuine value (reuse, scale, consistency) for **standardized, recurring** problems, but it **trades off against** the tacit, contextual, person-carried knowledge that **personalization** preserves for **novel, ambiguous** problems. The right *degree* of formal codification is **contingent** on the knowledge type and strategy, and over-codification can strip the context that made the knowledge useful.

---

# Claim Type (KOS-0003 §3)
**Interpretive / contingent-normative** (what strategy fits what knowledge), grounded in **descriptive** case observation.

---

# Evidence (KOS-0003 §4)
Type: **Empirical (case-based) + traditional/theoretical**.
- **SRC-0036 (Hansen, Nohria & Tierney 1999):** from professional-service-firm cases — codification (an "economics of reuse") vs personalization (person-to-person sharing); effective firms emphasised **one** strategy (~80/20) and used the other in support; "straddling" tended to fail. Codification fits standardized reuse; personalization fits novel expertise-intensive work.
- **SRC-0044 (Polanyi 1966, *The Tacit Dimension*):** the foundational tacit-knowledge source — "we can know more than we can tell." Much valuable knowledge is **tacit** and resists lossless codification, so over-codification can strip the context/tacit component. *(Catalogued in remediation; the managerial extension of this into codification strategy runs through the later Nonaka tradition, which remains invoked, not catalogued.)*

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 3** — HBR practitioner article (not peer-reviewed empirical), but by serious scholars and widely treated as canonical.
- **Relevance: 4** — directly about the value and limits of formalizing (codifying) knowledge.
- **Independence: 3** — two catalogued anchors (Hansen; Polanyi, catalogued in remediation), but they are **complementary, not corroborating**: Hansen anchors the codification-value/tradeoff half and Polanyi the tacit-loss half. They support different halves of one claim, so this is not independent confirmation of a single proposition — Level 3 holds.
- **Quality: 3** — case-derived framework, no measured outcomes or effect sizes; one author had a consulting affiliation.
- **Limitations:** Establishes a **contingency/tradeoff**, not a measured optimum; does not prove over-codification harms in a controlled sense; evidence base is consulting firms.

---

# Consensus (KOS-0003 §9)
- Evidence strength: **Moderate** (influential, case-based).
- Consensus strength: **Moderate-to-High** — codification/personalization and the tacit/explicit distinction are standard KM reference points; specifics are debated.
- Relationship: well-accepted framework; the tradeoff is more consensual than any precise optimum.

---

# Source Evaluation
SRC-0036: moderate-to-high authority (HBR, strong authors), moderate transparency (managerial essay, cases not to research standard), moderate independence (one consulting-firm author), inform/advise intent. Verified this session via HBR/HBS/PubMed records; exact pagination flagged as standard-but-not-re-verified.

---

# Assumptions (KOS-0003 §10)
- **Ontological:** a meaningful tacit/explicit distinction exists and not all knowledge codifies without loss — well supported in the tradition.
- **Methodological:** consulting-firm lessons generalise to other evolving knowledge systems — an analogical assumption, made explicit.

---

# Reasoning (KOS-0003 §7)
**Inductive.** From observed firm performance, codification pays where reuse dominates and hurts where novelty/tacitness dominates; hence "right degree is contingent." **Risks checked:** *false dichotomy* (named — codification/personalization is a mix, not a binary; effective firms did both, one dominant); *practitioner-source bias* (graded down accordingly); *over-generalisation* beyond consulting (flagged).

---

# Confidence (KOS-0003 §8)
**Level 3 (Moderate)** that codification has real but bounded value and trades off against tacit/personalized knowledge, with the right degree contingent. Not higher: the codification-strategy anchor is a case-based practitioner article with no effect sizes; the tacit-loss half now rests on a catalogued foundational source (Polanyi) but the *managerial* codification-loss extension still runs through the invoked Nonaka tradition; and the transfer to knowledge systems is analogical.

---

# Limitations
- No measured optimum; "right degree" is judged per context.
- Evidence base is professional-service firms; extension is analogical.
- Says little about *dynamic* over-codification (that risk is developed in CLM-0032).

---

# Alternative Interpretations
1. **"Modern tooling makes near-total codification cheap and better."** Steelmanned (search, LLMs, rich metadata lower codification cost). Partly conceded, but it does not dissolve the tacit residue or the context-stripping risk; refines the *degree*, not the tradeoff.
2. **"Personalization is just under-investment in codification."** Rejected on the evidence — straddling under-performed focus; the two are distinct strategies, not a maturity ladder.

---

# Relationships (STD-0004)
- `derived_from` SRC-0036, SRC-0044.
- `supports` FND-0007.
- `part_of` INV-0007.
- *(Conceptually adjacent to CLM-0032 on dynamic over-codification / ossification; left as prose only — not asserted as a typed `related_to` edge, per "use related_to sparingly," STD-0004.)*

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-12|Draft|Created for RQ-0007. Hansen et al. 1999 codification/personalization thesis verified this session. Level 3 — case-based practitioner anchor; tacit-knowledge grounding invoked not catalogued; contingency/tradeoff stated without a measured optimum.|
|0.2|2026-07-12|Draft|Post-review remediation (Critical Review - RQ-0007, #6): catalogued Polanyi 1966 (SRC-0044) for the tacit-loss half (previously an uncatalogued invocation); noted Hansen and Polanyi are complementary (different halves), not corroborating, so Independence 3 holds; the managerial Nonaka extension remains an explicit invocation. #9: de-asserted the prose-only `related_to CLM-0032` (now prose adjacency, not a typed edge). Title shortened (STD-0001 §10). No confidence change — remains Level 3.|

# End CLM-0029
