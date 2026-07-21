---
title: CLM-0044 - Depression Onset-Timing Divergence
document_type: Claim Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-07-15
category:
  - Knowledge Base
  - Claim
  - Developmental Psychopathology
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0010 Psychosocial Stressor Onset Divergence
related_documents:
  - SRC-0059 Salk Hyde Abramson 2017 Depression Meta-Analysis
  - CLM-0045 Depression Emergence Tracks Pubertal Status
  - CLM-0046 Anxiety Early Divergence
  - FND-0010 Psychosocial Stressor Onset Divergence Map
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - Depression
  - SexGenderConstructs
relationships:
  - type: derived_from
    target: SRC-0059
  - type: related_to
    target: CLM-0045
  - type: contrasts_with
    target: CLM-0046
  - type: supports
    target: FND-0010
  - type: part_of
    target: INV-0010
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

# CLM-0044

# Within Ages 5–17, the Female-Preponderant Divergence in Depression Emerges in Early Adolescence (~Ages 12–13), Near the Pubertal Transition — as a Divergence by Recorded Sex/Gender Category, Not Established Here as a Biological-Sex Effect

## Draft Claim Record

---

# Claim
> In representative samples, rates of depression are approximately equal between girls and boys before adolescence and **diverge into a roughly 2:1 (up to ~3:1 for diagnoses) female preponderance emerging around ages 12–13**, stabilizing across mid-adolescence. This is a claim about **the timing of a divergence in a recorded female/male category**; it is **not**, on this source, a claim that the divergence is *caused by* biological sex.

---

# Claim Type (KOS-0003 §3)
**Descriptive / epidemiological** (developmental timing of a category difference). The timing pattern is well-established; the *attribution* of the divergence to a construct (sex vs gender) is deliberately withheld here and handled — partially — by CLM-0045.

---

# Evidence (KOS-0003 §4)
Type: **Empirical** — large meta-analysis of representative national samples.
- **SRC-0059 (Salk, Hyde & Abramson 2017, *Psychological Bulletin*):** diagnosis OR = 2.37 at age 12, peaking OR = 3.02 at 13–15; symptom d ≈ .02 (ages 8–11) → .14 (12) → .26 (13) → .38 (14). ~1.7–1.9M people, 90+ nations.

**Construct-provenance code (governing this claim): `CONFLATED`.** SRC-0059 compares a recorded female/male demographic category on prevalence data and assesses no biological mechanism and no gender-socialization variable. **Operative rule (INV-0010 §3.1): a CONFLATED source cannot support a sex-attributed claim at any confidence level.** This claim therefore asserts only the *timing of a category divergence*, not its cause, and explicitly disclaims biological-sex attribution.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 5** — one of the most replicated findings in developmental psychopathology; enormous pooled sample; convergent diagnosis and symptom analyses.
- **Relevance: 5** — directly answers the primary onset-timing question for depression.
- **Independence: 5** — aggregates many independent national datasets.
- **Quality: 4** — high; bounded by cross-national aggregation and the interview-vs-scale instrument split.
- **Limitations:** establishes **when the category ratio diverges**; establishes **nothing about mechanism** and cannot license a sex-attributed causal reading.

---

# Consensus (KOS-0003 §9)
- Evidence strength: **High** that the ratio diverges in early adolescence.
- Consensus strength: **High** across developmental psychopathology for the timing; the *explanation* is actively contested (biological, gendered-socialization, differential-exposure, and reporting accounts all live).

---

# Source Evaluation
SRC-0059 is a flagship, high-authority, high-independence meta-analysis. Its one binding limitation for this investigation: it is `CONFLATED` — a sex label on epidemiological data — so it anchors timing, not causation.

---

# Assumptions (KOS-0003 §10)
- **Methodological:** period/cross-sectional prevalence ratios by age are a valid proxy for onset-timing divergence — largely warranted at population scale, imperfect for individual incident dating.
- **Ontological:** "depression" is a coherent measured outcome across the pooled instruments — reasonably supported.

---

# Reasoning (KOS-0003 §7)
**Inductive from convergent large-sample meta-analysis.** **Risks checked:** *construct conflation* (named and enforced — the claim is capped at category-timing, not sex-causation, per the operative rule); *magnitude creep* (named — no superlative or "biggest divergence" claim is made; the effect sizes are reported as reported, not ranked against other stressors); *reification of the sex label* (named — "female/male" is treated as a recorded category, not a validated construct).

---

# Confidence (KOS-0003 §8)
- **Level 4 (High)** — that the depression category ratio diverges to female-preponderant around ages 12–13 and consolidates across mid-adolescence. Held at High rather than Very High because population prevalence ratios are a proxy for onset dating and instrument classes differ. **Not Level 5:** Level 5 is reserved, and even this well-replicated pattern rests on a category proxy. **The attribution of the divergence to biological sex is NOT claimed at any level here** (CONFLATED source).

---

# Limitations
- About **timing of a recorded category divergence**, not its cause.
- Prevalence-ratio proxy, not incident-onset dating.
- Does not rank depression against other stressors on any magnitude metric.

---

# Alternative Interpretations
1. **"The divergence is a reporting/measurement artifact (girls more willing to report, instruments gender-biased)."** Steelmanned: plausible in part; some gap could be reporting. It does not erase the age-graded emergence, but it is one reason attribution is withheld — it is exactly why a CONFLATED source cannot settle cause.
2. **"It is biologically driven by puberty."** A serious hypothesis — but it requires a source that *measured* a maturational variable; SRC-0059 did not. That reading is taken up, and bounded, by CLM-0045 via SRC-0060.
3. **"It reflects gendered social exposure (peer stress, sexualization, role strain) intensifying at puberty."** Equally live and unmeasured here; also a reason attribution is withheld.

---

# Relationships (STD-0004)
- `derived_from` SRC-0059.
- `related_to` CLM-0045 (which supplies the bounded pubertal-status attribution).
- `contrasts_with` CLM-0046 (anxiety's earlier / pre-pubertal onset-timing signature — the reciprocal of the contrast CLM-0046 declares).
- `supports` FND-0010.
- `part_of` INV-0010.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-15|Draft|Created for RQ-0010. Level 4 (High) that the depression category ratio diverges to female-preponderant ~ages 12–13 (SRC-0059). Construct-provenance `CONFLATED`: timing claim only, biological-sex attribution explicitly withheld per operative rule. Magnitude/superlative and reporting-artifact risks named.|
|0.2|2026-07-20|Draft|epistemic-field backfill, Stage 3|
|0.1a|2026-07-15|Draft|Structural validation (ROLE-0001): added the reciprocal `contrasts_with` CLM-0046 edge (frontmatter + related_documents + §Relationships). CLM-0046 already declared `contrasts_with` CLM-0044; graph_integrity flagged the missing side. No claim content, confidence level, or construct-provenance code changed.|
|0.3|2026-07-21|Draft|review-field initialization per ADR-GOV-0008|

# End CLM-0044
