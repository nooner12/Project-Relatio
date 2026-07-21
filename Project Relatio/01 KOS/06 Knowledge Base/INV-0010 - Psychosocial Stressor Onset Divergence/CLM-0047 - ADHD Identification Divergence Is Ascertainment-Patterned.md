---
title: CLM-0047 - ADHD Identification Divergence Is Ascertainment-Patterned
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
  - SRC-0062 Gaub Carlson 1997 ADHD Gender Meta-Analysis
  - SRC-0063 Ramtekkar et al 2010 ADHD Community Ratio
  - FND-0010 Psychosocial Stressor Onset Divergence Map
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - ADHD
  - ReferralBias
  - SexGenderConstructs
relationships:
  - type: derived_from
    target: SRC-0062
  - type: derived_from
    target: SRC-0063
  - type: supports
    target: FND-0010
  - type: part_of
    target: INV-0010
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

# CLM-0047

# The Apparent Sex Divergence in ADHD Identification During Childhood Is Substantially an Ascertainment/Referral Effect (Gender-Patterned), Not Established Here as a Biological-Sex Difference in Underlying Rate

## Draft Claim Record

---

# Claim
> The large male-preponderant sex ratio in *identified/referred* childhood ADHD is **substantially an artifact of ascertainment**: the male:female ratio is ~10:1 in clinic-referred samples but only ~2–3:1 in community samples, because boys' more externalizing presentation draws referral while girls' more inattentive presentation is under-detected. What diverges most clearly is **who gets identified and when**, which is **gender-patterned**; a biological-sex difference in underlying ADHD liability is **not** established by these sources (and the residual community gap is left unexplained by them).

---

# Claim Type (KOS-0003 §3)
**Descriptive / causal-leaning** about measurement and ascertainment. Strong for "ascertainment shapes the ratio"; agnostic on any residual biological component.

---

# Evidence (KOS-0003 §4)
Type: **Empirical** — meta-analysis + independent community study.
- **SRC-0062 (Gaub & Carlson 1997, *JAACAP*):** clinic-referred M:F ~10:1 vs community ~3:1; referred girls more severely/intellectually impaired and less hyperactive — a higher (gendered) referral threshold for girls.
- **SRC-0063 (Ramtekkar et al. 2010, *JAACAP*):** community M:F ~2.28:1, far below the ~4:1 clinical figure; explicit conclusion that **females are under-diagnosed** through clinical channels.
- Two **independent** designs converging on the same account.

**Construct-provenance code (governing this claim): `CONFLATED`.** Both sources apply sex labels to referral/rating data; neither measures a biological mechanism or a gender-socialization construct. **Operative rule (§3.1): gender/ascertainment-patterned claim only.** The claim is framed exactly this way — indeed the sources' own thesis is that the sex label mismeasures the construct.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 4** — the clinic-vs-community ratio gap is robust and independently replicated.
- **Relevance: 5** — the flagship demonstration of construct conflation the investigation was built to test.
- **Independence: 4** — a pooled meta-analysis and a separate large community sample.
- **Quality: 3** — older diagnostic criteria (Gaub & Carlson); single-informant parent ratings (Ramtekkar); neither dates neurobiological onset.
- **Limitations:** establishes **ascertainment shapes the identification ratio**; does **not** resolve whether any biological-sex difference in true rate exists beneath the artifact.

---

# Consensus (KOS-0003 §9)
- Evidence strength: **Moderate–High** that referral/ascertainment substantially inflates the apparent sex ratio.
- Consensus strength: **High** that clinic ratios overstate the community ratio; **ongoing debate** over how much of the residual community gap is "real."

---

# Source Evaluation
SRC-0062 and SRC-0063 are high-authority and mutually independent; their convergence is the strength. Both are `CONFLATED` by construction — sex labels on ascertainment-shaped data — which is precisely the point they make about the field.

---

# Assumptions (KOS-0003 §10)
- **Methodological:** the clinic-vs-community ratio difference validly indexes ascertainment bias — strongly warranted.
- **Inferential:** "ascertainment inflates the ratio" does **not** assume "there is no biological difference" — the residual is left open, not denied.

---

# Reasoning (KOS-0003 §7)
**Inductive from convergent independent designs.** **Risks checked:** *over-correction bias* (named — resisting the tidy "it's all referral bias, no real difference" reading; the residual community gap is explicitly left unexplained, not zeroed); *construct conflation* (named and enforced — gender/ascertainment-patterned only); *criteria-drift* (named — Gaub & Carlson use older DSM criteria); *single-informant bias* (named — Ramtekkar's parent ratings are themselves gender-influenced, which cuts both ways).

---

# Confidence (KOS-0003 §8)
- **Level 3 (Moderate)** — that the childhood ADHD identification divergence is substantially ascertainment/gender-patterned (clinic ratios overstate community ratios; girls under-identified). Held at Moderate because the sources cannot quantify how much residual difference survives ascertainment correction, and rest on older criteria / single-informant ratings. **Not higher:** the "substantially" is well-supported, the "how much is real" is unresolved. **Not sex-attributed** (CONFLATED).

---

# Limitations
- About **identification/ascertainment divergence**, not incident neurobiological onset.
- Does not establish, or exclude, a residual biological-sex difference in true rate.
- No magnitude ranking against other stressors.

---

# Alternative Interpretations
1. **"Boys genuinely have more ADHD; the clinic ratio is roughly right."** Steelmanned: a residual community gap (~2.28:1) does persist, so *some* real difference may exist. But the collapse from ~10:1 to ~2–3:1 across ascertainment methods shows the identified ratio is substantially inflated — the claim's core.
2. **"Girls have a categorically different disorder (pure inattentive)."** Steelmanned and partly undercut — inattentive presentation is most common in *both* sexes (SRC-0063); the difference is more of degree/detection than of kind.

---

# Relationships (STD-0004)
- `derived_from` SRC-0062, SRC-0063.
- `supports` FND-0010.
- `part_of` INV-0010.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-15|Draft|Created for RQ-0010. Level 3 (Moderate) that childhood ADHD identification divergence is substantially ascertainment/gender-patterned (clinic ~10:1 vs community ~2–3:1; girls under-identified) (SRC-0062, SRC-0063). Construct-provenance `CONFLATED` — flagship conflation case; gender/ascertainment-patterned only. Over-correction and criteria-drift risks named; residual community gap left open.|
|0.2|2026-07-20|Draft|epistemic-field backfill, Stage 3|
|0.3|2026-07-21|Draft|review-field initialization per ADR-GOV-0008|

# End CLM-0047
