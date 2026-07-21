---
title: CLM-0045 - Depression Emergence Tracks Pubertal Status
document_type: Claim Record
version: 0.2
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
  - SRC-0060 Angold Costello Worthman 1998 Puberty Depression
  - CLM-0044 Depression Onset-Timing Divergence
  - FND-0010 Psychosocial Stressor Onset Divergence Map
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - Depression
  - Puberty
  - SexGenderConstructs
relationships:
  - type: derived_from
    target: SRC-0060
  - type: related_to
    target: CLM-0044
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
---

# CLM-0045

# The Timing of the Depression Divergence Tracks Physically Assessed Pubertal Status (Tanner III+), Not Chronological Age — a Bounded Biology-Linked Timing Claim Whose Downstream Mechanism (Hormonal vs Socially-Mediated) Remains Unresolved

## Draft Claim Record

---

# Claim
> The emergence of the female-preponderant depression ratio is **better predicted by physically assessed pubertal status (Tanner Stage III and above) than by chronological age**: girls exceed boys in depression only after mid-puberty, independent of the age at which mid-puberty is reached. This links the *timing* of the divergence to a **biological maturational variable that was actually measured** — but it does **not** establish that the underlying cause is hormonal rather than socially-mediated by the changes puberty brings.

---

# Claim Type (KOS-0003 §3)
**Causal-leaning descriptive** — a predictor-ranking finding (status > age) about the timing of divergence. The proximal predictor is biologically measured; the distal mechanism is not resolved.

---

# Evidence (KOS-0003 §4)
Type: **Empirical** — community-epidemiological study with physical pubertal staging.
- **SRC-0060 (Angold, Costello & Worthman 1998, *Psychological Medicine*):** girls exceed boys in depression only from Tanner Stage III+; **pubertal status outpredicted chronological age**; pubertal *timing* (early/late) had little effect.

**Construct-provenance code (governing this claim): `SEX-MEASURED`.** SRC-0060 physically assessed pubertal status (a biological maturational construct with a stated developmental mechanism) — it is the **one source in INV-0010 that can license a sex/biology-attributed claim** under the operative rule (§3.1). The license is **narrow**: it covers "the timing tracks a measured biological maturational variable," not "the cause is hormonal." **A further, decisive bound (per Critical Review – RQ-0010 F-2): puberty occurs in *both* sexes, so measuring pubertal stage does NOT establish that the *between-sex* divergence is biologically caused — the sex × puberty interaction is unmeasured.** What is licensed is only "the timing of the divergence co-varies with a measured maturational variable," not "the between-sex difference is a biological-sex effect." See Alternative Interpretations.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 4** — landmark, well-powered, widely cited; the status-over-age result has held up.
- **Relevance: 5** — directly addresses the construct question for depression's timing.
- **Independence: 4** — epidemiological cohort; not advocacy-linked; single-region.
- **Quality: 4** — strong design (physical staging), but the status–depression link is cross-sectional at the individual level and cannot separate the downstream pathway.
- **Limitations:** shows the timing tracks **pubertal status**; does **not** isolate a hormonal pathway from a socially-mediated one; single region.

---

# Consensus (KOS-0003 §9)
- Evidence strength: **Moderate–High** that pubertal status (not age) marks the transition.
- Consensus strength: **Moderate** — the status-over-age finding is broadly accepted, but the field increasingly holds that **peer/social stress mediates a substantial part** of the puberty–depression link (later mediation studies), so the pure-biology reading is *not* consensus.

---

# Source Evaluation
SRC-0060 is the investigation's strongest construct-provenance source precisely because it measured a biological variable rather than applying a bare sex label. That earns it `SEX-MEASURED`, but the same paper cannot tell us *why* pubertal status matters — which is where the claim is capped.

---

# Assumptions (KOS-0003 §10)
- **Methodological:** Tanner staging validly indexes maturational status — well supported.
- **Inferential:** "status predicts timing" ⇒ "a biological variable is in the causal path" — reasonable; but "biological variable in the path" ≠ "hormonal cause," which is the assumption explicitly *not* made.

---

# Reasoning (KOS-0003 §7)
**Inductive, predictor-ranking.** **Risks checked:** *construct over-attribution* (named and central — this is the one place a sex-linked claim is permitted, so the temptation to over-read it into "hormones cause female depression" is the main hazard; held down by capping at "measured maturational variable" and flagging social mediation); *perennial/convenient-biology bias* (named — a clean biological story is tidy and could flatter a "just puberty" reading; the peer-stress mediation literature is cited precisely to resist it); *single-cohort generalization* (named).

---

# Confidence (KOS-0003 §8)
- **Level 3 (Moderate)** — that the divergence timing tracks physically assessed pubertal status rather than chronological age. Held at Moderate (not higher) because the downstream mechanism is contested and substantially socially mediated, and the evidence is a single strong cohort. **Not Level 4/5:** the biologically *measured* predictor is solid, but its causal interpretation is unresolved, and INV-0010's discipline forbids letting a measured proximal variable masquerade as a settled distal mechanism.

---

# Limitations
- Licenses only "timing tracks a measured maturational variable," **not** "hormonally caused."
- Single-region cohort.
- Says nothing about magnitude relative to other stressors.

---

# Alternative Interpretations
1. **"Pubertal status matters because of hormonal/neuroendocrine change."** Steelmanned: biologically plausible; some hormonal correlates exist. But SRC-0060 did not measure hormones or isolate this pathway, so it remains a hypothesis, not this claim's content.
2. **"Pubertal status matters because a visibly maturing (esp. female) body changes social treatment, peer stress, and sexualization."** Steelmanned and *supported* by later mediation work showing peer stress carries much of the puberty–depression link. This is why the claim stops at "tracks measured pubertal status" and does not become a biology-cause claim.
3. **"It's really age/cohort, not puberty."** Rejected on the evidence — status outpredicted age in this design; this is the finding's core strength.

---

# Relationships (STD-0004)
- `derived_from` SRC-0060.
- `related_to` CLM-0044 (supplies the bounded attribution the timing claim withheld).
- `supports` FND-0010.
- `part_of` INV-0010.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-15|Draft|Created for RQ-0010. Level 3 (Moderate) that the depression divergence timing tracks physically assessed pubertal status (Tanner III+) over age (SRC-0060). Construct-provenance `SEX-MEASURED` — the only sex-attributed claim INV-0010 permits — but capped: downstream mechanism (hormonal vs socially-mediated) unresolved; peer-stress mediation named to resist convenient-biology bias.|
|0.2|2026-07-20|Draft|epistemic-field backfill, Stage 3|
|0.1a|2026-07-15|Draft|Added F-2 bound per Critical Review – RQ-0010: puberty occurs in both sexes, so pubertal-stage measurement does not establish biological-sex causation of the *between-sex* divergence (sex × puberty interaction unmeasured); the claim licenses only "timing co-varies with a measured maturational variable." **Confidence unchanged (Level 3).**|

# End CLM-0045
