---
title: CLM-0021 - Maintenance Depends on Different Determinants Than Initiation
document_type: Claim Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-07-11
category:
  - Knowledge Base
  - Claim
  - Behaviour Change Maintenance
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0006 Wellness Intervention Adherence and Maintenance
related_documents:
  - SRC-0024 Kwasnicka 2016 Maintenance of Behaviour Change Theories Review
  - ENT-0004 Intention-Behaviour Gap
  - FND-0006 What Best Supports Sustained Wellness Behaviour
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - Maintenance
  - BehaviourChange
relationships:
  - type: derived_from
    target: SRC-0024
  - type: depends_on
    target: ENT-0004
  - type: supports
    target: FND-0006
  - type: part_of
    target: INV-0006
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

# CLM-0021

# Maintenance Depends on Different Determinants Than Initiation

## Draft Claim Record

---

# Claim
> A major reason wellness interventions fail *over time* — even when successfully started — is that **maintenance is governed by different factors than initiation**. Sustained behaviour depends on **maintenance motives, self-regulation capacity, habit/automaticity, adequate psychological and physical resources, and a supportive social/physical environment**. When these are absent — motivation decays to its initial goal only, self-regulation is effortful and depletable, no habit forms, resources (time, energy, money, attention) are strained by competing demands, and the environment or a life disruption removes supports — the behaviour relapses. Initial success does **not** predict maintenance.

---

# Claim Type (KOS-0003 §3)
**Descriptive / explanatory** (a synthesis of the theorised determinants of maintenance) with a **causal** implication (absence of these determinants drives relapse).

---

# Evidence (KOS-0003 §4)
Type: **Theoretical synthesis of empirical theories** (systematic review of behaviour theories).
- **SRC-0024 (Kwasnicka et al. 2016):** systematic review of behaviour-change-**maintenance** theories. Behaviour-change interventions frequently produce only **temporary** change; **maintenance is rarely attained**. Maintenance is theorised to rest on **five interrelated domains**: (1) maintenance motives, (2) self-regulation, (3) habits, (4) psychological and physical resources, and (5) environmental and social influences.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 4** — high-quality systematic review in a leading methodology journal.
- **Relevance: 5** — directly and specifically about *maintenance* failure, the heart of part (a) of the RQ.
- **Independence: 3** — a single (authoritative) synthesis; the five domains recur across many theories but are here sourced to one review.
- **Quality: 3** — it synthesises *theories*, not intervention effect sizes; the domains are well-motivated but not quantified or causally weighted.
- **Limitations:** Establishes *which mechanisms are theorised* to govern maintenance and that maintenance is commonly not attained; it does **not** quantify how much each domain contributes, nor prove a specific relapse rate.

---

# Consensus (KOS-0003 §9)
- Evidence strength: **Moderate** (theory synthesis, not effect sizes).
- Consensus strength: **High** — that maintenance is distinct from and harder than initiation, and rests on habit/self-regulation/environment, is a mainstream position.
- Relationship: the *distinction* is strongly supported; the precise mechanism weighting is open.

---

# Source Evaluation
SRC-0024: high authority, transparent systematic review, non-commercial. Its five-domain framework and "maintenance rarely attained" premise were verified this session against journal and repository abstracts. It is a theory synthesis, so its claims are qualitative/structural, not numeric — no numeric verification gap, but also no effect-size backing.

---

# Assumptions (KOS-0003 §10)
- **Ontological:** the five domains name real, separable determinants (granted the framework).
- **Methodological:** theory-synthesis conclusions transfer to real intervention outcomes — reasonable but untested by effect size here.

---

# Reasoning (KOS-0003 §7)
**Abductive.** The recurrence of the same five domains across independent maintenance theories is best explained by their genuinely governing maintenance. **Risks checked:** *argument from theory rather than outcome* — named; the claim is graded down (Moderate) precisely because it rests on synthesised theory, not on quantified intervention effects. *Confirmation bias* — this claim cuts *against* any simple "just start and you'll keep going" wellness pitch, so it is not commercially convenient; that reduces (does not eliminate) motivated-reasoning risk.

---

# Confidence (KOS-0003 §8)
**Level 3 (Moderate).** The initiation/maintenance distinction and the five governing domains are well-established and directly on-point, but the evidence is a theory synthesis rather than quantified outcomes, so confidence is capped at Moderate.

---

# Limitations
- Domains are qualitative; their relative causal weight is unquantified.
- Does not itself supply the remedies (those are CLM-0023/0024/0025, which operationalise self-regulation and habit).

---

# Alternative Interpretations
1. **"Maintenance is just weaker initiation — same factors, less of them."** Contradicted by the review's core finding that distinct determinants (habit, environmental support) matter for maintenance specifically; rejected.
2. **"Relapse is mainly personal willpower failure."** Reframed and largely rejected — the framework locates failure in depletable self-regulation, absent habit, and unsupportive environments, not a character deficit.

---

# Relationships (STD-0004)
- `derived_from` SRC-0024.
- `depends_on` ENT-0004 (maintenance is where the intention-behaviour gap re-opens over time).
- `supports` FND-0006.
- `part_of` INV-0006.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-11|Draft|Created for RQ-0006. Five-domain maintenance framework verified via Kwasnicka 2016 abstract. Graded Moderate: theory synthesis, not quantified outcomes.|
|0.2|2026-07-20|Draft|epistemic-field backfill, Stage 3|
|0.3|2026-07-21|Draft|review-field initialization per ADR-GOV-0008|

# End CLM-0021
