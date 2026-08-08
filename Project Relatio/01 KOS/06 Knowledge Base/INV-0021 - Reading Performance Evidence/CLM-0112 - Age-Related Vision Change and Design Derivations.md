---
title: CLM-0112 - Age-Related Vision Change and Design Derivations
document_type: Claim Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-08-08
category:
  - Knowledge Base
  - Claim
  - Design Psychology
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0021 Reading Performance Evidence
related_documents:
  - SRC-0179 Legge and Bigelow 2011 Does Print Size Matter for Reading
  - SRC-0183 Whittaker and Lovie-Kitchin 1993 Visual Requirements for Reading
  - SRC-0184 W3C 2018 WCAG 2.1 Recommendation
  - SRC-0188 Owsley 2011 Aging and Vision
  - SRC-0189 Arditi Lighthouse Making Text Legible
  - FND-0021 Reading Performance Evidence Synthesis
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - ReadingPerformance
  - AgingVision
relationships:
  - type: derived_from
    target: SRC-0179
  - type: derived_from
    target: SRC-0183
  - type: derived_from
    target: SRC-0184
  - type: derived_from
    target: SRC-0188
  - type: derived_from
    target: SRC-0189
  - type: supports
    target: FND-0021
  - type: part_of
    target: INV-0021
confidence:
  - component: c_prescriptive_approach
    level: 3
    label: Moderate
  - component: c_stated_rationale
    level: 3
    label: Moderate
  - component: c_measured_performance_evidence
    level: 4
    label: High
  - component: c_documented_costs_failure_modes
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "the calibration anchor: the Owsley review interior READ in full (PMC) and the prescription artifact READ in full; the lens-yellowing/blue-discrimination sub-territory absent from the base, bounded; not cleared for external reliance"
review_cycle: 9
review_date: 2027-05-08
last_reviewed: 2026-08-08
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-08-08
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# CLM-0112

# Age-Related Vision Change Bearing on Type and Color (CLM-D)

## Draft Claim Record

---

# Claim
> **The aging-vision territory is, as the brief anticipated, the strongest measured base in this set — and this session read it: the read review documents convergent, mechanism-attributed, multi-study declines in spatial contrast sensitivity (intermediate-to-high spatial frequencies, ~0.3 log units at 8 cycles/degree on average, optically dominated under photopic conditions), a roughly threefold contrast requirement under low luminance, rod-mediated dark-adaptation delays exceeding ten minutes by the eighth decade, and slowed visual processing speed with everyday-task consequences. The design prescriptions derived from this literature (read in full from the partial-sight guideline) match the measured direction — maximize contrast, enlarge type, increase leading, avoid glare — but their specific values (16–18 points; 25–30% leading) are stated without citation in the artifact, the artifact itself hedges its comparative-typeface and polarity claims as resting on limited evidence, and the sub-territory the brief names first (lens yellowing and short-wavelength discrimination decline) is absent from this base's read review entirely — so the derivations match what was measured in direction, while the prescribed values and the blue-region story outrun the base's accessible surfaces.**

---

# Element (i) — The Prescriptive Approach (as stated in the practice literature)

- **The derived-prescription artifact (SRC-0189, interior READ in full):** highest possible contrast, with a stated claim that light-on-dark is more readable "for many readers who are older or partially sighted"; point size "at least 16 to 18 points"; leading "at least 25 to 30 percent of the point size"; standard familiar fonts; wide letter spacing; monospaced fonts described as seeming more legible for central-field-defect readers; non-glossy paper.
- **The age-anchored normative derivation (SRC-0184, read):** the 4.5:1 threshold explicitly compensates for "the loss in contrast sensitivity usually experienced by users with vision loss equivalent to approximately 20/40 vision," with 20/40 "commonly reported as typical visual acuity of elders at roughly age 80" — an aging-population anchor inside the world's dominant contrast prescription.

# Element (ii) — The Stated Rationale

- SRC-0189 (read): impaired vision "reduc[es] the amount of light that enters the eye," blurs the retinal image, and damages the central retina; light reduction and blur "reduce the effective contrast of the text" — mechanism-level rationale matching the measured optical account.
- SRC-0184 (read): the Arditi-Faye acuity-to-contrast-sensitivity association as the quantitative bridge from aging acuity to a threshold value.

# Element (iii) — Measured Human-Performance Evidence (including explicit bounded absence)

- **Spatial contrast sensitivity decline (SRC-0188, interior READ — PMC full text):** older adults show impaired contrast sensitivity at intermediate and high spatial frequencies under photopic conditions (young-old differences around 0.2–0.57 log units at ~8 cycles/degree, averaging ~0.3), with low-spatial-frequency sensitivity largely spared in daylight; under photopic conditions the loss is predominantly **optical** — verbatim: "optical characteristics of the aged eye reduce spatial contrast sensitivity. These factors include reduced retinal illuminance (either from pupillary miosis, increased lens density, or both), increased intraocular light scatter, and increased aberrations."
- **Low-luminance vision (SRC-0188, read):** under scotopic conditions older adults require roughly **three times the contrast** of younger adults for equivalent discrimination; rod-mediated dark adaptation slows substantially — verbatim: "The time taken for 70-year-olds to reach pre-bleach light sensitivity is over 10 minutes longer than for those in their 20s" — with a mechanism account (retinal pigment epithelium–Bruch's membrane transport decline).
- **Processing speed (SRC-0188, read):** slowed visual processing speed with divided-attention and clutter sensitivity, consequential for everyday visual tasks including reading labels; trainable in part.
- **Reading-specific evidence (SRC-0188, read):** peripheral visual span shrinks and limits peripheral reading speed; perceptual training enlarges it in older adults with smaller gains than in the young. The review's reading content is real but narrower than its contrast-sensitivity core.
- **The reserve frame (SRC-0183, abstract level):** contrast and acuity reserves as the quantitative bridge from measured thresholds to functional reading levels — convergent, different group, unread interior disclosed.
- **EXPLICITLY ABSENT from the base's accessible surfaces — the blue-region sub-territory:** the read review contains **no treatment of lens yellowing as a chromatic filter, short-wavelength (blue-region) discrimination decline, or chromatic aging at all** — the sub-territory the brief's claim definition names first is not covered by this base's read anchor, and no other in-base source covers it. Presbyopia appears only implicitly (near-work distance adjacency in CLM-0114's territory); illumination needs appear as the low-luminance findings plus a compensatory-illumination remark. Bounded: unread interiors (SRC-0183) are the disclosed holes these absence statements do not cover.

# Element (iv) — Documented Costs and Failure Modes (from the sources; not inferred)

- **The aesthetic tension (SRC-0189, read):** "the traditional dark on light may be aesthetically preferable" — the artifact documents that its own light-on-dark recommendation trades against preference.
- **Oversizing (SRC-0179, read):** the fluent range's upper bound (~2° x-height) means enlargement beyond it slows reading — a measured cost bounding "bigger is better" derivations.
- **The artifact's own hedges (SRC-0189, read):** "there is little reliable information on the comparative legibility of typefaces"; monospaced advantage phrased as "seem to be more legible" — the prescription artifact documents the limits of its own evidence base in place.
- **Glare (SRC-0189, read):** glossy finishes lessen legibility for older and partially sighted readers — a documented material-choice failure mode.

---

# Claim Type (KOS-0003 §3)
**Descriptive** — the measured aging-vision base, the derived prescriptions, and where derivation matches measurement (direction) versus outruns it (specific values; the blue-region story). No element is normative.

# Evidence (KOS-0003 §4)
Type: **Empirical** (SRC-0188, SRC-0183, SRC-0179) and **Documentary** (SRC-0189, SRC-0184).
- SRC-0188 — interior READ this session (PMC full text, PMCID PMC3049199); the anchor the brief directed to prioritize, and it was readable.
- SRC-0189 — interior READ in full. SRC-0184 — derivation chain read. SRC-0179 — read. SRC-0183 — abstract level, disclosed.

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: **4** — the anchor review and the prescription artifact were both read in full; the load-bearing quantitative findings are extracted from the read text.
- Relevance: **5** — exactly the aging-vision measurement base and its derived prescriptions.
- Independence: **4** — the review (Owsley), the reserve model (Whittaker & Lovie-Kitchin), the guideline (Arditi), and the normative derivation (W3C) are four distinct provenances; the review surveys a multi-laboratory literature.
- Quality: **4** — a 25-year field review in the field's principal journal, read; capped by review-level (not primary) access and the reserve model's unread interior.
- Limitations: one review carries the (iii) core; the blue-region sub-territory is a base hole, not a field hole.

# Source Evaluation
The read review is a peer-reviewed field synthesis with no commercial stake; the guideline carries the recorded shared-authorship note (Arditi: measurement literature and prescription artifact); the normative artifact's role is its own stated derivation.

# Assumptions (KOS-0003 §10)
- **Review-level evidence is carried as review-level:** the (iii) findings are the read review's reported synthesis of a multi-study literature, not this record's independent verification of the underlying primaries.
- **The brief's sub-territory list is not treated as a coverage promise:** where the base lacks a named sub-territory (lens yellowing / blue discrimination), the absence is recorded as a base limit, bounded to accessible surfaces.
- **Direction-match ≠ value-derivation:** the claim keeps "the prescriptions point the way the measurements point" strictly separate from "the prescribed values descend from measurements."

# Reasoning (KOS-0003 §7)
**Descriptive reporting.** Risk checked: **anchor inflation** — the brief expected this territory to be strongest, which invites over-grading; controlled by scoping the High strictly to the read review's convergent core (contrast sensitivity, low luminance, dark adaptation, processing speed) and grading the derivation-match and costs elements Moderate on their actual support. Risk: **halo from reading the interior** — a read source is not automatically a strong source; the High rests on the review's multi-study convergence and independence structure, stated in the Evidence Evaluation, not on access alone.

# Confidence (KOS-0003 §8)
- **c_prescriptive_approach — Level 3 (Moderate):** the prescriptions read in full from one artifact plus the read normative derivation; specific values uncited in the artifact.
- **c_stated_rationale — Level 3 (Moderate):** mechanism-level rationale read directly; matches the measured optical account at the level stated.
- **c_measured_performance_evidence — Level 4 (High):** the anchor interior was READ; the core findings are convergent, mechanism-attributed, multi-study, multi-laboratory results reported by the field's principal review, with an independent convergent reserve frame and an independent clinical association (Arditi-Faye, via the read WCAG companion) — the strongest-evidenced element in this investigation. **Recorded for the reflexive section: with the interior actually read, the calibration anchor grades ABOVE the absence-dominated components — the GB-2026-058 access-flattening did not recur (data point (a): the anchor discriminated).** Not Level 5: review-level access, one review carrying the core, and the blue-region hole cap it.
- **c_documented_costs_failure_modes — Level 3 (Moderate):** four read entries, all from the artifacts' own statements.
- **No Level 5. Everything R0.**

# Limitations
- Asserts nothing about lens yellowing or short-wavelength discrimination (absent from this base's accessible surfaces — a base limit, not a field verdict); nothing about the primaries beneath the read review beyond what it reports; no clinical or individual guidance whatsoever; no application decision.
- **May not be cited outside Relatio or for any external reliance (R0), regardless of INV-0021's closure state.** The health-adjacent character of aging-vision content makes the R0 gate doubly binding (STD-0006 §7.5).

# Alternative Interpretations
1. **"A single read review cannot carry a High."** Considered and answered in place: the High is earned by the review's reported multi-study, multi-mechanism convergence plus three independent convergent provenances in-base — not by the singleness of the review; the reviewer is invited to test this grading explicitly.
2. **"The prescriptions are validated by the measurements."** Refused — direction-match is recorded; the specific values (16–18 pt, 25–30%, 4.5:1) variously rest on uncited artifact statements or clinical adaptation, and the value-level derivation is exactly what the base cannot establish.
3. **"The blue-region absence undermines the anchor."** Rejected as stated — it bounds the anchor's scope; within its covered core the evidence is as graded, and the absence is recorded as the base hole it is.

# Relationships (STD-0004)
- `derived_from` SRC-0179, SRC-0183, SRC-0184, SRC-0188, SRC-0189.
- `supports` FND-0021.
- `part_of` INV-0021.

# Verification (STD-0006 §7.5 — Specialist disclosure)
**The anchor was read, as the brief directed:** SRC-0188 interior READ (PMC full text); SRC-0189 interior READ in full; SRC-0184's derivation chain read live; SRC-0179 read. SRC-0183 abstract-level (paywalled), disclosed. Everything **R0; not cleared for external reliance regardless of closure** — doubly noted for this health-adjacent territory.

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-08-08|Draft|Created for RQ-0021 (Specialist pass), CLM-D of six — the calibration anchor, interiors READ per the brief's priority instruction. Four separable elements: (i) the read derived prescriptions incl. the read WCAG age-anchored derivation (Moderate); (ii) mechanism rationale, read (Moderate); (iii) the read aging-vision core — contrast-sensitivity decline with optical attribution, threefold low-luminance requirement, 10-minute dark-adaptation delay, processing-speed slowing, visual-span reading evidence — plus the bounded blue-region absence (High — the anchor discriminated; GB-2026-058 data point recorded); (iv) aesthetic tension, oversizing bound, the artifact's own hedges, glare (Moderate). Direction-match vs value-derivation kept separate throughout. No Level 5; R0. Pending Critical Review and structural validation.|

# End CLM-0112
