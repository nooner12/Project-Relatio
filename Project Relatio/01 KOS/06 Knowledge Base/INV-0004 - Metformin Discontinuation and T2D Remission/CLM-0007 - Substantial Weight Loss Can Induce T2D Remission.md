---
title: CLM-0007 - Substantial Weight Loss Can Induce T2D Remission
document_type: Claim Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-10
category:
  - Knowledge Base
  - Claim
  - Type 2 Diabetes
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0004 Metformin Discontinuation and T2D Remission
related_documents:
  - SRC-0006 DiRECT Trial Programme
  - SRC-0009 STAMPEDE Metabolic Surgery Trial
  - SRC-0010 ADA-EASD Consensus on Remission Definition
  - CLM-0008 Ectopic-Fat Removal Restores Insulin Sensitivity and Beta-Cell Function
  - CLM-0009 Remission Likelihood Declines with Duration and Beta-Cell Loss
  - CLM-0010 Carbohydrate Restriction Improves Control and Reduces Medication
  - CLM-0011 Discontinuation Must Be Supervised and Remission Can Relapse
  - CLM-0012 Exercise and Mediterranean Diet Improve Control but Rarely Alone Remit
  - FND-0004 Evidence-Based Pathways to T2D Remission and Safe De-prescribing
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - Type2Diabetes
  - Remission
  - WeightLoss
relationships:
  - type: derived_from
    target: SRC-0006
  - type: derived_from
    target: SRC-0009
  - type: depends_on
    target: CLM-0008
  - type: supports
    target: FND-0004
  - type: part_of
    target: INV-0004
confidence:
  - component: overall
    level: 4
    label: High
reliance_tier: R0
reliance_note: "unassessed floor; predates verification-pass procedure."
---

# CLM-0007

# Substantial Weight Loss Can Induce T2D Remission

## Draft Claim Record

---

# Claim
> Substantial, sustained weight loss (on the order of **10–15 kg**) can induce **remission of type 2 diabetes** — HbA1c <6.5% off all glucose-lowering medication — in a meaningful proportion of people, with the probability rising steeply with the amount of weight lost.

---

# Claim Type (KOS-0003 §3)
**Causal** (primary) — weight loss produces remission — with a **descriptive** component (remission occurs at measurable rates). Causal claims require mechanism, evidence, alternatives, and confounding analysis; the mechanism is carried by CLM-0008.

---

# Evidence (KOS-0003 §4)
Type: **Empirical** (randomised controlled trials).
- **SRC-0006 (DiRECT RCT):** remission at 12 months **46% (68/149) intervention vs 4% (6/149) control**; strong **dose–response by weight lost** — ≥15 kg: **86%**; 10–15 kg: 57%; 5–10 kg: 34%; 0–5 kg: 7%; weight gain: 0%.
- **SRC-0009 (STAMPEDE RCT):** metabolic surgery (a high-intensity weight-loss route) produced superior, more durable glycaemic control than medical therapy over 5 years.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 5** — a cluster RCT with a large between-arm difference (OR ≈19.7), reinforced by a surgical RCT.
- **Relevance: 5** — directly measures the remission endpoint at issue.
- **Independence: 4** — dietary (DiRECT) and surgical (STAMPEDE) routes converge on the weight-loss→remission link; both, however, share the confound that weight loss co-varies with many metabolic changes.
- **Quality: 4** — high; open-label behavioural intervention and (for STAMPEDE) single-centre/partial-industry funding are the caveats.
- **Limitations:** Establishes that remission *can* be induced and is *dose-dependent on weight loss* in **early-disease** populations; it does **not** establish permanence, nor rates in long-duration/insulin-treated patients.

---

# Consensus (KOS-0003 §9)
- Evidence strength: **High.**
- Consensus strength: **High** — that substantial weight loss can remit early T2D is now mainstream (basis of the NHS remission programme).
- Relationship: strongly supported; debate is about durability and who benefits, not whether the effect exists.

---

# Source Evaluation
SRC-0006: very high authority, charity-funded, transparent, candid about relapse. SRC-0009: high authority RCT, partial industry funding (COI). Both score remission/control against the SRC-0010 consensus standard.

---

# Assumptions (KOS-0003 §10)
- **Methodological:** trial cohorts (≤6 years' duration, obese, non-insulin in DiRECT) generalise to the broader T2D population — only partly true.
- **Ontological:** "remission" is a real, measurable state (granted the consensus definition, SRC-0010).

---

# Reasoning (KOS-0003 §7)
**Inductive + abductive.** The randomised between-arm difference and the monotonic dose–response support a causal reading (inductive); weight-driven ectopic-fat reduction is the best mechanistic explanation (abductive, via CLM-0008). Risks checked: **confounding** (randomisation addresses baseline confounds; the dose–response strengthens causality); **confirmation bias / commercial motivation** (named in INV-0004 §6 — the claim is stated conditionally, not as "diabetes is curable").

---

# Confidence (KOS-0003 §8)
**Level 4 — High.** Randomised, dose-responsive, replicated across dietary and surgical routes, mainstream consensus. Not Level 5: durability is limited (see CLM-0011) and the effect is demonstrated mainly in early disease.

---

# Limitations
- Concerns *induction* of remission, not its *maintenance*.
- Demonstrated primarily in early-disease, obese cohorts; weaker evidence for long-duration or lean patients.

---

# Alternative Interpretations
1. **It is glycaemic control, not true remission.** (Addressed by scoring against the off-medication consensus definition, SRC-0010 — DiRECT remission required being off all drugs.)
2. **Only surgery works; diet is transient.** (Partly right on durability — surgery is more durable — but DiRECT shows diet-induced remission is real at 1–2 years; rejected as a blanket claim.)
3. **Selection/placebo effects explain it.** (Weakened by randomisation and the objective HbA1c endpoint.)

---

# Relationships (STD-0004)
- `derived_from` SRC-0006, SRC-0009.
- `depends_on` CLM-0008 (mechanism), and is bounded by CLM-0009 (who benefits) and CLM-0011 (durability/relapse).
- `supports` FND-0004.
- `part_of` INV-0004.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-10|Draft|Created for RQ-0004.|
|0.2|2026-07-20|Draft|epistemic-field backfill, Stage 3|

---

# End CLM-0007
