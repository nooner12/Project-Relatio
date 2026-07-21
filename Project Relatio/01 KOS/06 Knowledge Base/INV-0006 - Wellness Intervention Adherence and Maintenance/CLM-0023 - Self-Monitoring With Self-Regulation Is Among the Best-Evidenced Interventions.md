---
title: CLM-0023 - Self-Monitoring With Self-Regulation Is Among the Best-Evidenced Interventions
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
  - SRC-0026 Michie 2009 Effective Techniques Healthy Eating Physical Activity Meta-Regression
  - SRC-0027 Harkin 2016 Monitoring Goal Progress Meta-Analysis
  - FND-0006 What Best Supports Sustained Wellness Behaviour
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - SelfMonitoring
  - SelfRegulation
relationships:
  - type: derived_from
    target: SRC-0026
  - type: derived_from
    target: SRC-0027
  - type: supports
    target: FND-0006
  - type: part_of
    target: INV-0006
confidence:
  - component: self_monitoring_self_regulation_wellness
    level: 4
    label: High
reliance_tier: R0
reliance_note: "unassessed floor; predates verification-pass procedure."
---

# CLM-0023

# Self-Monitoring With Self-Regulation Techniques Is Among the Best-Evidenced Interventions

## Draft Claim Record

---

# Claim
> Among behaviour-change techniques, **self-monitoring — especially when combined with other self-regulation (control-theory) techniques such as goal-setting, feedback, and review** — has the strongest and most consistent evidence for improving health-behaviour outcomes. Prompting people to monitor progress toward a goal **causes** greater goal attainment (randomised evidence), and the effect is **larger when progress is recorded and made public/accountable**. Effect sizes are, however, **small-to-moderate**.

---

# Claim Type (KOS-0003 §3)
**Causal** (self-monitoring improves outcomes) supported by a **comparative descriptive** element (it explains more between-study variance than other techniques).

---

# Evidence (KOS-0003 §4)
Type: **Empirical** (meta-regression across trials + meta-analysis of randomised experiments).
- **SRC-0026 (Michie et al. 2009):** meta-regression of 122 evaluations (N≈44,747) in healthy-eating/physical-activity interventions. Overall pooled effect **0.31**; **self-monitoring explained the most between-study heterogeneity (~13%)**; interventions combining self-monitoring with ≥1 other control-theory technique were more effective (**0.42 vs 0.26**).
- **SRC-0027 (Harkin et al. 2016):** meta-analysis of 138 **randomised** studies (N≈19,951). Prompting progress monitoring raised monitoring frequency (d+≈1.98) and, in turn, **promoted goal attainment (d+≈0.40)**, mediated by monitoring frequency, and **larger when reported/made public and physically recorded**.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 4** — two large, high-quality reviews, one of them randomised-experiment based.
- **Relevance: 4** — directly identifies effective ingredients for changing (and tracking) wellness behaviour.
- **Independence: 4** — a cross-trial meta-regression and a randomised meta-analysis converge; different methods, same conclusion.
- **Quality: 4** — high; Michie 2009 is correlational-across-trials (confounding by intervention quality), but Harkin 2016's randomised design shores up causality.
- **Limitations:** Establishes that self-monitoring/self-regulation **improve outcomes with small-to-moderate effect**; neither review establishes durable (>12 month) **maintenance** after support ends, and Harkin spans many goal domains, not only wellness.

---

# Consensus (KOS-0003 §9)
- Evidence strength: **High** for the ingredient; **modest** for effect magnitude.
- Consensus strength: **High** — self-monitoring is a consensus "active ingredient" and is embedded in the Behaviour Change Technique Taxonomy and most guidelines.
- Relationship: strongly supported; the caveat is size and durability, not existence.

---

# Source Evaluation
SRC-0026 and SRC-0027: both high authority, transparent, non-commercial; all cited figures (0.31; 13%; 0.42 vs 0.26; d+ 1.98/0.40) verified this session via PubMed/DARE and White Rose/APA records.

---

# Assumptions (KOS-0003 §10)
- **Methodological:** technique effects generalise across wellness behaviours and delivery modes.
- **Epistemological:** meta-regression associations (Michie) approximate causal contribution — partly true; buttressed by Harkin's randomised design.

---

# Reasoning (KOS-0003 §7)
**Inductive + convergent.** Two independent methods (cross-trial meta-regression; randomised meta-analysis) converge on self-monitoring/self-regulation as high-value ingredients. **Risks checked:** *confounding in meta-regression* (named; offset by Harkin's RCTs); *effect-size inflation* (guarded — the small-to-moderate magnitude is stated plainly); *durability overreach* (named — maintenance after withdrawal is not established).

---

# Confidence (KOS-0003 §8)
**Level 4 (High)** that self-monitoring + self-regulation are among the best-evidenced techniques for improving wellness-behaviour outcomes, with **small-to-moderate** effects. Not Level 5: effects are modest, and long-term maintenance after support ends is not established.

---

# Limitations
- Small-to-moderate effect sizes — helpful, not transformative.
- Long-term maintenance after monitoring/support stops is not demonstrated.
- Self-monitoring can burden or demotivate some users if framed punitively (an implementation caveat).

---

# Alternative Interpretations
1. **"Self-monitoring works only because motivated people monitor more (reverse causation)."** Weakened by Harkin's randomised manipulation of monitoring; largely rejected.
2. **"It's the whole package, not self-monitoring specifically."** Partly conceded — combination beats self-monitoring alone (Michie 0.42 vs 0.26) — but self-monitoring is the single largest identifiable contributor; refined, not rejected.

---

# Relationships (STD-0004)
- `derived_from` SRC-0026, SRC-0027.
- `supports` FND-0006.
- `part_of` INV-0006.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-11|Draft|Created for RQ-0006. Michie 2009 and Harkin 2016 figures verified this session. Graded High for the ingredient; effect size and durability caveats recorded.|
|0.2|2026-07-21|Draft|**Renamed** per STD-0001 §8 (Path Length Constraint), owner approval 2026-07-21. This record was one of four whose absolute path exceeded the Windows `MAX_PATH` limit of 260 characters, making it invisible to naive scanners; the descriptive title was shortened to bring the relative path within the §8 budget of 180 characters. **Filename and `title:` shortened, body H1 heading matched; no claim statement, evidence, evidence evaluation, consensus, confidence grading, or relationship changed.** Graph references updated in the same commit so no reference is left dangling.|
|0.3|2026-07-21|Draft|epistemic-field backfill, Stage 3|

# End CLM-0023
