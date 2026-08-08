---
title: CLM-0109 - Typeface and Letterform Prescriptions
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
  - SRC-0180 Arditi and Cho 2005 Serifs and Font Legibility
  - SRC-0181 Lund 1999 Knowledge Construction in Typography
  - SRC-0189 Arditi Lighthouse Making Text Legible
  - SRC-0193 Apple Human Interface Guidelines Typography
  - SRC-0194 Butterick Practical Typography
  - FND-0021 Reading Performance Evidence Synthesis
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - ReadingPerformance
  - Typeface
relationships:
  - type: derived_from
    target: SRC-0179
  - type: derived_from
    target: SRC-0180
  - type: derived_from
    target: SRC-0181
  - type: derived_from
    target: SRC-0189
  - type: derived_from
    target: SRC-0193
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
    level: 3
    label: Moderate
  - component: c_measured_performance_evidence
    level: 3
    label: Moderate
  - component: c_documented_costs_failure_modes
    level: 2
    label: Low
reliance_tier: R0
reliance_note: "serif measurement at abstract level (interior paywalled, disclosed); Lund thesis at surface level; the read sources are the review, the guideline artifacts, and the practitioner pages; not cleared for external reliance"
review_cycle: 6
review_date: 2027-02-08
last_reviewed: 2026-08-08
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-08-08
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# CLM-0109

# Typeface and Letterform Prescriptions (CLM-A)

## Draft Claim Record

---

# Claim
> **The typeface and letterform prescriptions — serif-vs-sans-serif selection rules, letter-spacing and line-spacing values, size-and-spacing rules of professional custom — are stated in this base's read prescription artifacts at specific values, while their measured reading-performance support at the surfaces accessible this session is either near-null (the serif question: one parametric measurement whose reading speeds "showed no effect of serifs" in RSVP and continuous reading, alongside a small size-threshold legibility advantage for slight (5%) serifs that the study attributes to the letter-spacing increase serifs impose — smaller than spacing alone predicts — and a doctoral critique of the 72-study lineage finding no valid conclusion in either direction), indirect (x-height as the operative size variable and font effects on critical print size, from the read vision-science review), or absent (no measured reading-performance evidence for the specific letter-spacing and line-spacing values prescribed). A reported preference for the sans-serif variants — carried from the citing literature, not establishable from the abstract — dissociates from the null speed result if it stands.**

---

# Element (i) — The Prescriptive Approach (as stated in the practice literature)

- **Professional custom, live-read (SRC-0194):** body point size 10–12 points in print and 15–25 pixels on the web; line spacing 120–145% of point size; line length 45–90 characters — stated as key rules on the read summary page, without citations there.
- **Vendor guidance, live-read (SRC-0193):** prefer regular-to-bold weights and "avoid Ultralight, Thin, and Light font weights, which can be difficult to see, especially when text is small"; minimize typeface count; per-platform system-font prescriptions.
- **Partial-sight guidance, interior read (SRC-0189):** avoid complicated, decorative, or cursive fonts; "standard serif or sans-serif fonts, with familiar, easily recognizable characters are best"; wide letter spacing; roman over italics/oblique/condensed.
- The classical serif-for-print prescription itself is carried in this base through the literatures that dispute it (SRC-0180/0181 frame it as the practice under test); no in-base artifact prescribes serifs for reading performance **at the surfaces accessible this session** — the unread interiors (SRC-0181's thesis body) are the disclosed hole this absence claim does not cover.

# Element (ii) — The Stated Rationale

- SRC-0194 (read): rules presented as established professional principles; the summary page states no research basis — the rationale register is craft custom.
- SRC-0193 (read): legibility across viewing distances and conditions; thin strokes harder to see at small sizes. No cited measurement.
- SRC-0189 (read): mechanism-level rationale for partial sight — impaired vision reduces light, blurs the image, damages the central retina; familiar letterforms and wide spacing compensate. The artifact itself hedges the evidential status of typeface comparisons (see (iii)).

# Element (iii) — Measured Human-Performance Evidence (including explicit bounded absence)

- **The serif question, measured (SRC-0180, interior unread; abstract-establishable except where marked):** using lower-case fonts varying only in serif size (0%, 5%, 10% of cap height), the study assessed legibility by **size thresholds and reading speed**. Abstract-verbatim: "RSVP and continuous reading speeds showed no effect of serifs"; "Five percentage serif fonts were slightly more legible than sans serif" on size thresholds, "but the average inter-letter spacing increase that serifs themselves impose, predicts greater enhancement than we observed"; the study's own summary — "our data exhibited no difference in legibility between typefaces that differ only in the presence or absence of serifs." A **reported preference for the sans-serif variants** circulates in the citing literature but is **not establishable from the abstract** and is carried at that lower access level only. Single study; no replication record in this base.
- **The lineage's evidential status (SRC-0181, interior unread; surface-establishable):** the University of Reading doctoral examination of the serif/sans-serif legibility-research corpus is consistently described at the surfaces read as reviewing 72 comparison studies and finding **no valid conclusion in favour of either**. Carried at surface level only.
- **The read guideline's own statement (SRC-0189, interior read):** "there is little reliable information on the comparative legibility of typefaces," with "some evidence" for sans-serif at small character sizes relative to acuity and "some evidence" for roman over italic — the prescription artifact itself reports the measured base as thin.
- **Indirect size-variable evidence (SRC-0179, interior read):** x-height, not nominal point size, is the operative size measure in the psychophysics; critical print size varies with font (the review cites a measured font effect on CPS) — measured evidence that letterform proportion affects the size-speed relationship, without ranking any typeface.
- **EXPLICITLY ABSENT at the surfaces accessible this session:** measured reading-performance evidence for the specific line-spacing values (120–145%; 25–30% of point size), letter-spacing values, or line-length ranges prescribed. The unread interiors (SRC-0180, SRC-0181, and the practitioner book beyond its summary page) are the disclosed holes this absence claim does not cover.
- **Population sub-elements: EXPLICITLY ABSENT** for typeface prescriptions in this base — no developmental/young-reader typeface evidence at any accessible surface; the aging-adjacent evidence (sans-serif at small size relative to acuity) is carried in SRC-0189's hedged form.

# Element (iv) — Documented Costs and Failure Modes (from the sources; not inferred)

- **Preference-performance dissociation (SRC-0180, citing-literature level — NOT abstract-establishable, disclosed):** the reported sans-serif preference beside the null speed result would mean selection by preference does not track measured speed; carried at the access level it actually has. The one documented entry for the territory, and a weak one.
- **EXPLICITLY EMPTY beyond that** at the surfaces read; unread interiors may document more (the grade reflects this).

---

# Claim Type (KOS-0003 §3)
**Descriptive** — what the practice prescribes, the rationale registers, what was measured and at what access level, and the documented dissociation. No element is normative.

# Evidence (KOS-0003 §4)
Type: **Empirical** (SRC-0180; SRC-0179 for the size-variable frame) and **Documentary** (SRC-0181, SRC-0189, SRC-0193, SRC-0194).
- SRC-0179, SRC-0189, SRC-0193, SRC-0194 — read this session (mirror PDF full text; guideline PDF; two live pages).
- SRC-0180 — abstract-level (paywalled); SRC-0181 — surface-level (thesis not held by an open repository located this session).

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: **3** — the read artifacts are read; the serif measurement is peer-reviewed but abstract-level.
- Relevance: **5** — exactly the territory's prescription and measurement literature.
- Independence: **3** — SRC-0180 and SRC-0189 share an author (recorded stake note); the practitioner artifacts are independent of the measurement program.
- Quality: **3** — one measurement study at abstract level; one surface-level critique; the strongest content is the read artifacts' own statements.
- Limitations: prescriptive values unmeasured in-base; population variation absent; two key interiors unread.

# Source Evaluation
The measurement study and thesis are academic; the three prescription artifacts carry recorded commercial/vendor stakes and contribute (i)/(ii) only; SRC-0189 spans both poles under its recorded shared-authorship note.

# Assumptions (KOS-0003 §10)
- **Absence claims bind accessible surfaces only** (all bounded in place above).
- **"No valid conclusion" (SRC-0181) is carried as the thesis's reported verdict on the lineage, not as this claim's own review of those 72 studies.**
- **Terminological bracket:** "legibility" (letter-level) and "readability" (continuous-text) usage differs across these sources; the record follows each source's own term at point of use.

# Reasoning (KOS-0003 §7)
**Descriptive reporting.** Risk checked: **debunking zeal** — the serif-null result invites "serifs are a myth" overclaim; controlled by recording the null as one parametric study plus a surface-level lineage critique, not a demonstrated equivalence. Risk: **shared-authorship non-independence** (SRC-0180/SRC-0189), named with the stake note.

# Confidence (KOS-0003 §8)
- **c_prescriptive_approach — Level 3 (Moderate):** the prescriptions' existence and specific values are documented from three read artifacts.
- **c_stated_rationale — Level 3 (Moderate):** read directly from the artifacts; the craft-custom register is explicit.
- **c_measured_performance_evidence — Level 3 (Moderate):** a real measured null plus a real lineage critique plus read indirect evidence — but single-study at abstract level, surface-level thesis, and the prescribed values themselves unmeasured in-base. A **read-but-evidence-capped** Moderate (recorded for the reflexive section's GB-2026-058 taxonomy).
- **c_documented_costs_failure_modes — Level 2 (Low):** one abstract-level entry.
- **No Level 4 or 5. Everything R0.**

# Limitations
- Asserts nothing about the interiors of SRC-0180/0181; nothing about typefaces this base does not cover; no equivalence claim among typefaces; no application decision.
- **May not be cited outside Relatio or for any external reliance (R0), regardless of INV-0021's closure state.**

# Alternative Interpretations
1. **"The null result vindicates sans-serif prescriptions."** Rejected — the speed null supports neither pole's prescription; and the abstract's small size-threshold advantage for slight serifs (attributed by the study to spacing) cuts against a sans-serif vindication reading rather than for it.
2. **"Professional custom encodes accumulated implicit measurement."** Not established and not refuted — the custom's values (10–12 pt, 120–145%) fall inside the read psychophysical fluent range (SRC-0179), which is consistent with the custom tracking real constraints; but consistency is not derivation, and the sources claim no derivation.
3. **"The absence of spacing-value evidence is a search failure."** Possible — bounded in place: the absence binds surfaces accessible this session, with the unread interiors named.

# Relationships (STD-0004)
- `derived_from` SRC-0179, SRC-0180, SRC-0181, SRC-0189, SRC-0193, SRC-0194.
- `supports` FND-0021.
- `part_of` INV-0021.

# Verification (STD-0006 §7.5 — Specialist disclosure)
**Mixed access for this claim, disclosed per source:** SRC-0179 read (mirror PDF full text); SRC-0189 read (guideline PDF full text); SRC-0193/0194 live-read; SRC-0180 abstract-level (paywalled, no open copy located); SRC-0181 surface-level (no open thesis copy located). Everything **R0; not cleared for external reliance regardless of closure.**

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.2|2026-08-08|Draft|**Critical Review – RQ-0021 remediation (F2). No grade changed.** The serif-measurement content aligned to the primary's abstract, retrieved verbatim during the review: reading speeds "showed no effect of serifs" in **RSVP and continuous reading** (the "paper" misstatement removed); the abstract's **5%-serif size-threshold advantage** (attributed by the study to inter-letter spacing, smaller than spacing predicts) added to element (iii), which scopes thresholds; the **sans-serif preference relabeled to its true access level** (citing-literature, not abstract-establishable) in the claim statement, element (iii), and element (iv), with the dissociation carried conditionally. Alternative 1 adjusted for the size-threshold nuance. All four components reviewer-confirmed and unchanged.|
|0.1|2026-08-08|Draft|Created for RQ-0021 (Specialist pass), CLM-A of six. Four separable elements: (i) the read prescription artifacts' typeface/spacing rules (Moderate); (ii) craft-custom and mechanism rationales, read (Moderate); (iii) the serif null at abstract level + the Lund lineage critique at surface + read indirect size-variable evidence + bounded absences for spacing values and populations (Moderate); (iv) the preference-performance dissociation, explicitly empty beyond (Low). Absences bounded to accessible surfaces from first draft. No Level 4/5; R0. Pending Critical Review and structural validation.|

# End CLM-0109
