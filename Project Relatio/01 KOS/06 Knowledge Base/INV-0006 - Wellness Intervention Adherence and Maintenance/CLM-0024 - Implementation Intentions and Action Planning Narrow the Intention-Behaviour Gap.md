---
title: CLM-0024 - Implementation Intentions and Action Planning Narrow the Intention-Behaviour Gap
document_type: Claim Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-07-11
category:
  - Knowledge Base
  - Claim
  - Behaviour Change Techniques
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0006 Wellness Intervention Adherence and Maintenance
related_documents:
  - SRC-0028 Gollwitzer Sheeran 2006 Implementation Intentions Meta-Analysis
  - ENT-0004 Intention-Behaviour Gap
  - FND-0006 What Best Supports Sustained Wellness Behaviour
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - ImplementationIntentions
  - Planning
relationships:
  - type: derived_from
    target: SRC-0028
  - type: depends_on
    target: ENT-0004
  - type: supports
    target: FND-0006
  - type: part_of
    target: INV-0006
confidence:
  - component: implementation_intentions_proximal_enactment
    level: 4
    label: High
reliance_tier: R0
reliance_note: "unassessed floor; predates verification-pass procedure."
review_cycle: 12
review_date: 2027-07-21
last_reviewed: 2026-07-21
---

# CLM-0024

# Implementation Intentions and Action Planning Narrow the Intention-Behaviour Gap

## Draft Claim Record

---

# Claim
> **Implementation intentions** — specific "if situation X, then I will do Y" if-then plans that pre-commit the *when, where, and how* of a behaviour — reliably improve goal attainment with a **medium-to-large effect (d ≈ 0.65)**. They work by directly attacking the **intention–behaviour gap** (CLM-0019/ENT-0004): they convert an abstract intention into a concrete, situation-triggered action. They are, however, a **translation** tool — they help people who already have an intention act on it; they do not manufacture motivation, and their long-term durability is less directly established.

---

# Claim Type (KOS-0003 §3)
**Causal** (forming implementation intentions increases goal attainment).

---

# Evidence (KOS-0003 §4)
Type: **Empirical** (meta-analysis).
- **SRC-0028 (Gollwitzer & Sheeran 2006):** meta-analysis of **94 independent tests**; implementation intentions had a **positive effect of medium-to-large magnitude (d ≈ 0.65)** on goal attainment, across many behavioural domains.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 4** — foundational, very heavily cited meta-analysis with a large replication base.
- **Relevance: 4** — directly targets the enactment failure identified as central (ENT-0004); applicable to exercise, diet, and other wellness behaviours.
- **Independence: 3** — lead author originated the construct (theoretical investment); the large independent replication base offsets this.
- **Quality: 3** — many primary studies are short-term, single-target, or laboratory; effect is heterogeneous and moderated by goal commitment.
- **Limitations:** Establishes that if-then planning **narrows the intention-behaviour gap** for committed goals; it does **not** establish durable long-term wellness maintenance, and effects shrink when commitment or self-efficacy is low.

---

# Consensus (KOS-0003 §9)
- Evidence strength: **High** for the proximal effect.
- Consensus strength: **High** — implementation intentions are a mainstream, well-replicated behaviour-change technique.
- Relationship: strongly supported for proximal enactment; durability and moderation by commitment are the caveats.

---

# Source Evaluation
SRC-0028: high authority; the 94-tests/d≈0.65 figure verified this session via multiple index records (Konstanz repository, SciRP, NCI-hosted PDF). Originator authorship noted as a theoretical-investment consideration.

---

# Assumptions (KOS-0003 §10)
- **Methodological:** cross-domain planning effects transfer to sustained wellness behaviours — plausible for enactment, less certain for maintenance.
- **Ontological:** the intention-behaviour gap is a real target the technique acts on (granted ENT-0004).

---

# Reasoning (KOS-0003 §7)
**Inductive.** A large meta-analytic effect across 94 tests supports a causal enactment benefit. **Risks checked:** *originator investment* (named; independence graded 3); *durability overreach* (named — claim is explicit that this is a translation tool, not a maintenance or motivation tool); *publication bias* (a general risk in a large meta-analysis; not separately quantified here — a limitation).

---

# Confidence (KOS-0003 §8)
**Level 4 (High)** that implementation intentions produce a medium-to-large *proximal* improvement in enacting intended behaviour. Not Level 5: durability for long-term wellness maintenance is not directly established, and effects depend on prior commitment.

---

# Limitations
- A translation tool for existing intentions — not a source of motivation.
- Long-term maintenance evidence is thinner than the proximal-effect evidence.
- Effectiveness declines with low goal commitment / self-efficacy.

---

# Alternative Interpretations
1. **"Planning helps only highly motivated people."** Partly true — commitment moderates the effect — but benefits appear across a broad range; refined, not rejected.
2. **"The effect is publication-bias inflation."** A legitimate general concern for large meta-analyses; conceded as a reason not to reach Level 5, but the effect is robust enough across 94 tests to retain High.

---

# Relationships (STD-0004)
- `derived_from` SRC-0028.
- `depends_on` ENT-0004 (it is the most direct gap-closer).
- `supports` FND-0006.
- `part_of` INV-0006.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-11|Draft|Created for RQ-0006. 94-tests/d≈0.65 verified this session. Framed explicitly as a translation (not motivation/maintenance) tool.|
|0.2|2026-07-21|Draft|epistemic-field backfill, Stage 3|
|0.3|2026-07-21|Draft|review-field initialization per ADR-GOV-0008|

# End CLM-0024
