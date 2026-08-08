---
title: CLM-0110 - Size and Contrast Thresholds
document_type: Claim Record
version: 0.2
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
  - SRC-0182 Legge Rubin Luebker 1987 Psychophysics of Reading V Contrast
  - SRC-0183 Whittaker and Lovie-Kitchin 1993 Visual Requirements for Reading
  - SRC-0184 W3C 2018 WCAG 2.1 Recommendation
  - SRC-0185 Somers APCA Documentation Why APCA
  - SRC-0194 Butterick Practical Typography
  - FND-0021 Reading Performance Evidence Synthesis
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - ReadingPerformance
  - ContrastThresholds
relationships:
  - type: derived_from
    target: SRC-0179
  - type: derived_from
    target: SRC-0182
  - type: derived_from
    target: SRC-0183
  - type: derived_from
    target: SRC-0184
  - type: derived_from
    target: SRC-0185
  - type: derived_from
    target: SRC-0194
  - type: supports
    target: FND-0021
  - type: part_of
    target: INV-0021
confidence:
  - component: c_prescriptive_approach
    level: 3
    label: Moderate
  - component: c_stated_rationale
    level: 4
    label: High
  - component: c_measured_performance_evidence
    level: 3
    label: Moderate
  - component: c_documented_costs_failure_modes
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "the WCAG provenance chain and two psychophysics interiors read this session; the reserve model at abstract level; small-n primary data disclosed; not cleared for external reliance"
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

# CLM-0110

# Size and Contrast Thresholds (CLM-B)

## Draft Claim Record

---

# Claim
> **The WCAG 2.x contrast thresholds (4.5:1 body / 3:1 large text) do not descend from reading measurement: by the normative document's own read provenance chain, the 3:1 floor is adopted from display-ergonomics standards (ISO 9241-3; ANSI/HFES 100-1988) "for standard text and vision," and the 4.5:1 figure is that floor multiplied by 1.5 for the contrast-sensitivity loss empirically associated with 20/40 acuity (the Arditi-Faye clinical relation), 20/40 being described as typical acuity at roughly age 80 — a derivation routed through display standards and clinical low-vision measurement, not through reading-performance studies. Meanwhile the reading psychophysics that does exist (read this session) reports normal fluent reading as strikingly tolerant of contrast reduction at fluent sizes — less than a factor-of-two speed loss over a tenfold contrast reduction for 1° characters — with the tolerance collapsing at small character sizes, exactly the size-contrast interaction a single blanket ratio cannot express; and the read critique documentation for the candidate successor model (APCA) asserts contrast mis-ranking against WCAG 2.x — most acutely for dark colors ("4.5:1 can be functionally unreadable when a color is near black," the polarity/dark-mode critique as documented on the read "Why APCA" page) — and spatial-frequency (size/weight) blindness, while itself citing no peer-reviewed validation of its own thresholds at the surfaces read. Minimum-size prescriptions in the base's practitioner artifact state values inside the psychophysically measured fluent range without claiming derivation from it.**

---

# Element (i) — The Prescriptive Approach (as stated in the practice literature)

- **WCAG 2.1 (SRC-0184, normative text read at the cited surfaces):** text and images of text at a contrast ratio of **at least 4.5:1**, with **3:1 for large-scale text** (at least 18 point, or 14 point bold, with a CJK-equivalence clause); SC 1.4.6 (enhanced) at 7:1. The world's most widely adopted and legislated contrast prescription.
- **Practitioner size rules (SRC-0194, live-read):** 10–12 points print body, 15–25 pixels web.
- **Large-print floor (context from the aging territory, read):** SRC-0189 prescribes 16–18 points for partial-sight readers (carried primarily in CLM-0112).

# Element (ii) — The Stated Rationale

- **The WCAG derivation chain, read this session from the Understanding SC 1.4.3 companion (SRC-0184):** (a) 3:1 adopted from ISO 9241-3 and ANSI/HFES 100-1988 as the minimum "for standard text and vision"; (b) "the empirical finding that in the population, visual acuity of 20/40 is associated with a contrast sensitivity loss of roughly 1.5" (the Arditi-Faye reference), so a 20/40 user "would thus require a contrast ratio of 3 * 1.5 = 4.5 to 1"; (c) 20/40 "commonly reported as typical visual acuity of elders at roughly age 80." The rationale is explicit, quantitative, and **routed through display-ergonomics standards and clinical acuity-contrast association — not through reading-performance measurement**. Graded High because the chain was read directly from the normative companion this session; what it shows about provenance is exactly what this claim asserts.
- **APCA rationale (SRC-0185, read):** perceptual uniformity, polarity awareness, and spatial-frequency (size/weight) sensitivity as requirements a readability-contrast model must meet.

# Element (iii) — Measured Human-Performance Evidence (including explicit bounded absence)

- **Contrast tolerance of fluent reading (SRC-0182, interior READ this session — full-text extraction):** five normal-vision subjects (20/20 corrected); drifting-text reading aloud; reading rates highest (~350 words/min) for letters from 0.25° to 2°; **"for 1° letters, reading rate decreased by less than a factor of two for a tenfold reduction in contrast"** (abstract, verbatim); at contrast 0.10 both plotted subjects still read near 200 words/min; **contrast polarity showed no systematic effect** ("These data do not provide evidence for a systematic advantage of either contrast polarity"). Small n (the central figure reports two subjects of the five), disclosed.
- **The size-contrast interaction (SRC-0182, read):** for 0.25° characters "contrast plays a much more critical role" — one subject's rate dropped fourfold for a one-log-unit contrast reduction and the other could not read at contrast 0.10 — the measured basis for size-dependent contrast requirements.
- **The fluent print size range (SRC-0179, interior READ — mirror full text):** the fluent range spans "a factor of 10 in angular print size (x-height) from approximately 0.2° to 2°" (abstract, verbatim); **critical print size** typically 0.15°–0.3° depending on individual, font, and method; at 40 cm the fluent range corresponds to x-heights of 1.4 mm (4 points) to 14 mm (40 points).
- **The reserve model (SRC-0183, interior unread; abstract/citing-surface level):** reading rate as a function of acuity reserve and contrast reserve, with a contrast reserve of roughly 10:1 associated with fluent-range reading and lower reserves with slower reading — a convergent threshold-distance frame from a different research group, carried at abstract level.
- **EXPLICITLY ABSENT at the surfaces accessible this session:** any reading-performance study validating the specific 4.5:1 / 3:1 values as reading thresholds, in the normative document, its read companion, or elsewhere in this base; and any peer-reviewed validation of APCA's own Lc thresholds in its read documentation (the critique documentation cites the Legge and Bailey-Lovie-Kitchin threshold literatures but no published validation study of its own cut-points at the surfaces read). Unread interiors (SRC-0183; the un-fetched remainder of the WCAG resource list; the APCA documentation corpus beyond the pages read) are the disclosed holes these absence claims do not cover.

# Element (iv) — Documented Costs and Failure Modes (from the sources; not inferred)

- **Small-size contrast collapse (SRC-0182, read):** the measured fourfold-to-total failure at 0.25° under reduced contrast — the documented failure mode of treating contrast adequacy as size-independent.
- **Fluent-range upper bound (SRC-0179, read):** reading rate declines for very large print (beyond ~2° x-height) — oversizing is a measured cost, not a free safety margin.
- **Documented mis-ranking claims against WCAG 2.x (SRC-0185 — specifically the "Why APCA as a New Contrast Method?" page, read; competing-model stake recorded):** that page asserts WCAG 2 "can pass colors that should fail as not readable" and can fail pairs that should pass, with dark-color/dark-mode over-statement ("4.5:1 can be functionally unreadable when a color is near black") — carried as the documented critique of the prescription, pinned to the page that carries it, at its recorded stake, not as an adjudicated verdict.
- **Reserve insufficiency (SRC-0183, abstract level):** contrast reserves near 3:1 are associated with spot reading rather than fluent reading — the documented cost of minimum-threshold compliance read as adequacy.

---

# Claim Type (KOS-0003 §3)
**Descriptive** — the prescription, its own stated derivation, what the measured literature reports, and the documented failure modes. No element is normative; the claim does not assert that the WCAG thresholds are wrong, only where they come from and what the reading literature measures.

# Evidence (KOS-0003 §4)
Type: **Empirical** (SRC-0182, SRC-0179, SRC-0183) and **Documentary** (SRC-0184, SRC-0185, SRC-0194).
- SRC-0182, SRC-0179 — interiors read this session (full-text extractions from the laboratory-hosted and mirror PDFs).
- SRC-0184 — normative thresholds and the Understanding SC 1.4.3 provenance chain read live this session.
- SRC-0185 — critique pages read live; stake recorded. SRC-0183 — abstract level. SRC-0194 — live-read.

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: **4** — the load-bearing provenance chain and two psychophysics interiors were read directly.
- Relevance: **5** — exactly the territory's prescription and measurement literature.
- Independence: **3** — SRC-0179 and SRC-0182 share the same laboratory and lead author; the reserve model is the one cross-group convergent leg, at abstract level; the critique carries its competing-model stake.
- Quality: **3** — small-n primary data (five subjects; two in the central figure); era-bound apparatus (1987 CRT); the reserve model unread.
- Limitations: the provenance finding binds the read companion's own citation chain; no claim is made about unlocated primary literature behind ISO 9241-3.

# Source Evaluation
The two psychophysics papers are peer-reviewed academic sources; the normative document is the prescription artifact under examination (read at its own surfaces); the APCA documentation carries the recorded competing-model stake and is used as the documented critique pole only.

# Assumptions (KOS-0003 §10)
- **The Understanding companion is treated as the authoritative statement of WCAG's own rationale** (it is the document the Recommendation designates for that purpose); the claim's provenance finding is about that stated rationale, not about unstated deliberations.
- **Absence claims bind accessible surfaces only** (bounded in place above).
- **Threshold ≠ optimum ≠ prescription** carried throughout: the psychophysical findings are tolerance curves and ranges, not alternative prescribed values.

# Reasoning (KOS-0003 §7)
**Descriptive reporting.** Risk checked: **critique adoption** — reading the APCA documentation could slide into adopting its verdict; controlled by carrying every mis-ranking claim as a documented, staked assertion and recording APCA's own validation absence symmetrically. Risk: **same-laboratory dependence** between the two read psychophysics sources, named. Risk: **provenance overreach** — the finding is about the stated derivation chain, not a claim that no reading evidence exists anywhere in the world; bounded accordingly.

# Confidence (KOS-0003 §8)
- **c_prescriptive_approach — Level 3 (Moderate):** thresholds read from the live normative text; the size-prescription pole read; one artifact each.
- **c_stated_rationale — Level 4 (High):** the derivation chain was read verbatim this session from the normative document's own companion — the element asserts what that chain says, and that is directly verified. The one High outside the calibration anchor; it rests on a read primary artifact stating its own rationale.
- **c_measured_performance_evidence — Level 3 (Moderate):** two interiors read at full text, but small-n primary data, same-laboratory dependence, one convergent leg at abstract level only. A **read-but-evidence-capped** Moderate (recorded for the reflexive section's GB-2026-058 taxonomy — the cap here is evidential shape, not access).
- **c_documented_costs_failure_modes — Level 3 (Moderate):** two read measured entries, one read staked critique, one abstract-level entry.
- **No Level 5. Everything R0.**

# Limitations
- Asserts nothing about ISO 9241-3's or ANSI/HFES 100-1988's own interior evidence bases (not in this base; not located this session); nothing about whether APCA's model is correct; no alternative threshold is proposed; no application decision.
- **May not be cited outside Relatio or for any external reliance (R0), regardless of INV-0021's closure state.**

# Alternative Interpretations
1. **"The display-standards lineage may itself rest on reading measurement, so the provenance finding is shallow."** Partly conceded and bounded: the finding binds the chain as stated in the read companion — the ISO/ANSI interiors are outside this base, and the claim says so rather than asserting their emptiness.
2. **"The psychophysical contrast tolerance shows the WCAG thresholds are too strict."** Refused — the tolerance data are normal-vision fluent-size findings; the WCAG derivation explicitly targets low-acuity users, a different population; the two are different objects, which is the point recorded, not a verdict either way.
3. **"APCA's critique being staked disqualifies it."** Rejected — the stake is recorded, not disqualifying; the documented critique stands as a documented critique, and its own validation absence is recorded with the same discipline.

# Relationships (STD-0004)
- `derived_from` SRC-0179, SRC-0182, SRC-0183, SRC-0184, SRC-0185, SRC-0194.
- `supports` FND-0021.
- `part_of` INV-0021.

# Verification (STD-0006 §7.5 — Specialist disclosure)
**The best-verified claim in this investigation:** SRC-0182 and SRC-0179 interiors read via full-text extraction (laboratory-hosted PDF; mirror PDF); SRC-0184's SC 1.4.3 thresholds and the entire Understanding-document derivation chain read live; SRC-0185's critique pages read live. SRC-0183 abstract-level (paywalled), disclosed. Everything **R0; not cleared for external reliance regardless of closure.**

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.2|2026-08-08|Draft|**Critical Review – RQ-0021 advisory adoption (A1). No grade changed.** The APCA "polarity mis-ranking" attribution pinned to its carrying surface: the claim statement now anchors the polarity/dark-mode critique on the read "Why APCA" page's own words, and element (iv) names that page as the carrier of the pass/fail mis-ranking assertions. All four components reviewer-confirmed and unchanged.|
|0.1|2026-08-08|Draft|Created for RQ-0021 (Specialist pass), CLM-B of six — the WCAG-provenance interrogation the brief mandates. Four separable elements: (i) the 4.5:1/3:1 thresholds and size rules, read from the live artifacts (Moderate); (ii) the read derivation chain — ISO/ANSI 3:1 for standard vision, ×1.5 Arditi-Faye clinical adjustment, age-80 20/40 framing — verbatim from Understanding SC 1.4.3 (High); (iii) read contrast-tolerance and fluent-range psychophysics with the size-contrast interaction, the abstract-level reserve model, and bounded absences for any reading-validation of the specific thresholds on either side of the WCAG/APCA dispute (Moderate); (iv) small-size collapse, oversize cost, staked mis-ranking claims, reserve insufficiency (Moderate). Provenance verdict: the thresholds rest on standards adapted from other domains plus clinical adjustment, not reading measurement — recorded descriptively. No Level 5; R0. Pending Critical Review and structural validation.|

# End CLM-0110
