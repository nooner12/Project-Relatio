---
title: CLM-0026 - Financial Incentives Improve Behaviour While in Place But Effects Fade on Removal
document_type: Claim Record
version: 0.4
status: Draft
operational_status: Active
created: 2026-07-11
category:
  - Knowledge Base
  - Claim
  - Incentives
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0006 Wellness Intervention Adherence and Maintenance
related_documents:
  - SRC-0031 Mantzari 2015 Personal Financial Incentives Meta-Analysis
  - FND-0006 What Best Supports Sustained Wellness Behaviour
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - FinancialIncentives
  - Maintenance
relationships:
  - type: derived_from
    target: SRC-0031
  - type: supports
    target: FND-0006
  - type: contrasts_with
    target: CLM-0020
  - type: part_of
    target: INV-0006
confidence:
  - component: overall
    level: 4
    label: High
reliance_tier: R0
reliance_note: "unassessed floor; predates verification-pass procedure."
review_cycle: 12
review_date: 2027-07-20
last_reviewed: 2026-07-20
---

# CLM-0026

# Financial Incentives Improve Behaviour While in Place But Effects Fade on Removal

## Draft Claim Record

---

# Claim
> **Personal financial incentives** reliably improve habitual health behaviours **while the incentive is in place** and briefly afterward, but the effect **is generally not sustained beyond a few months after the incentive is withdrawn** — "new habits do not appear to be formed." Incentives are therefore a genuine tool for *initiating* or *boosting* a behaviour, but a **weak tool for durable maintenance** on their own. This makes them an instructive contrast: an intervention that works through *controlled/external* motivation buys behaviour temporarily without building the internal or habitual structures that sustain it.

---

# Claim Type (KOS-0003 §3)
**Causal** (incentives change behaviour) with a bounded **predictive/descriptive** element (the effect does not persist post-removal).

---

# Evidence (KOS-0003 §4)
Type: **Empirical** (systematic review and meta-analysis).
- **SRC-0031 (Mantzari et al. 2015):** meta-analysis of personal financial incentives across health behaviours. Incentives increased behaviour change during/shortly after the incentive period — e.g. **OR ≈ 1.53 (95% CI 1.05–2.23)** to 18 months from baseline and **OR ≈ 2.11 (95% CI 1.21–3.67)** at 2–3 months post-removal — but **effects were not sustained beyond ~3 months after removal**; authors concluded **"new habits do not appear to be formed."** A larger, time-limited effect appeared among highly-deprived recipients (OR ≈ 2.17).

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 4** — high-quality meta-analysis from a leading group, timepoint-stratified.
- **Relevance: 4** — directly addresses *durability* of an intervention that many wellness/employer programmes rely on.
- **Independence: 3** — a single (strong) meta-analysis; consistent with the broader incentives literature not individually catalogued.
- **Quality: 4** — pooled ORs with CIs across behaviours; heterogeneity across behaviour types is the main caveat.
- **Limitations:** Establishes that incentive effects **do not persist at the timepoints studied** after removal; it does **not** rule out that incentives *combined with* habit/self-regulation support could be more durable, nor that some behaviours (e.g. smoking cessation) persist somewhat longer.

---

# Consensus (KOS-0003 §9)
- Evidence strength: **High** for the "works during, fades after" pattern.
- Consensus strength: **High** — the non-durability of standalone incentives is a mainstream finding.
- Relationship: strongly supported; the open question is whether incentives + habit-support can do better.

---

# Source Evaluation
SRC-0031: high authority, transparent, public-health oriented; all cited ORs (1.53; 2.11; 2.17) and the "not sustained beyond ~3 months / no new habits" conclusion verified this session via PMC-4728181 full text.

---

# Assumptions (KOS-0003 §10)
- **Methodological:** pooling across heterogeneous behaviours yields a valid general pattern — reasonable, with behaviour-specific exceptions.
- **Epistemological:** absence of sustained effect at studied timepoints indicates genuine non-durability (rather than merely unmeasured later effect).

---

# Reasoning (KOS-0003 §7)
**Inductive.** Consistent decay of effect across behaviours after removal supports the non-durability conclusion and the "controlled motivation doesn't build maintenance" reading. **Risks checked:** *overgeneralisation* (named — some behaviours persist longer; incentives + support untested); *motivated reasoning* — this claim is *inconvenient* for incentive-based wellness/employer programmes, so it is not a self-serving conclusion; it is retained because the evidence supports it.

---

# Confidence (KOS-0003 §8)
**Level 4 (High)** that standalone financial incentives improve behaviour during the incentive period but generally do not sustain it after removal. Not Level 5: behaviour-type heterogeneity and the untested incentives-plus-habit-support combination leave room for exceptions.

---

# Limitations
- Non-durability is demonstrated for *standalone* incentives; combinations with habit/self-regulation support are untested here.
- Some behaviours (e.g. smoking cessation) may persist somewhat longer.
- Says nothing against short-term use of incentives to *initiate* a behaviour.

---

# Alternative Interpretations
1. **"Incentives are useless."** Overstated — they reliably work *during* the incentive period and may help initiation/equity; rejected as too strong.
2. **"Bigger/longer incentives would sustain it."** Possible but unproven here; the mechanism concern (external motivation crowding out internal) argues against it; left open, not endorsed.

---

# Relationships (STD-0004)
- `derived_from` SRC-0031.
- `supports` FND-0006.
- `contrasts_with` CLM-0020 (autonomous vs controlled motivation — incentives are the controlled-motivation case that fails to endure).
- `part_of` INV-0006.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-11|Draft|Created for RQ-0006. ORs and "not sustained / no new habits" conclusion verified via PMC-4728181 full text. Framed as an instructive non-durability contrast to autonomous motivation.|
|0.2|2026-07-21|Draft|**Renamed** per STD-0001 §8 (Path Length Constraint), owner approval 2026-07-21. This record was one of four whose absolute path exceeded the Windows `MAX_PATH` limit of 260 characters, making it invisible to naive scanners; the descriptive title was shortened to bring the relative path within the §8 budget of 180 characters. **Filename and `title:` shortened, body H1 heading matched; no claim statement, evidence, evidence evaluation, consensus, confidence grading, or relationship changed.** Graph references updated in the same commit so no reference is left dangling.|
|0.3|2026-07-20|Draft|epistemic-field backfill, Stage 3|
|0.4|2026-07-21|Draft|review-field initialization per ADR-GOV-0008|

# End CLM-0026
