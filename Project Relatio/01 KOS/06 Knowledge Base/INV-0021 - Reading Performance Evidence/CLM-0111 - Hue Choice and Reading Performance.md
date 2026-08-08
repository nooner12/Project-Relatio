---
title: CLM-0111 - Hue Choice and Reading Performance
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
  - SRC-0184 W3C 2018 WCAG 2.1 Recommendation
  - SRC-0186 Legge Parish Luebker Wurm 1990 Psychophysics of Reading XI Color Contrast
  - SRC-0187 Knoblauch Arditi Szlyk 1991 Chromatic and Luminance Contrast Reading
  - SRC-0189 Arditi Lighthouse Making Text Legible
  - FND-0021 Reading Performance Evidence Synthesis
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - ReadingPerformance
  - ColorContrast
relationships:
  - type: derived_from
    target: SRC-0184
  - type: derived_from
    target: SRC-0186
  - type: derived_from
    target: SRC-0187
  - type: derived_from
    target: SRC-0189
  - type: supports
    target: FND-0021
  - type: part_of
    target: INV-0021
confidence:
  - component: c_prescriptive_approach
    level: 2
    label: Low
  - component: c_stated_rationale
    level: 3
    label: Moderate
  - component: c_measured_performance_evidence
    level: 3
    label: Moderate
  - component: c_documented_costs_failure_modes
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "one chromatic-reading interior read (abstract and conclusions extracted), the second at abstract level (paywalled); the hue-prescription pole thin at accessible surfaces, bounded; not cleared for external reliance"
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

# CLM-0111

# Hue Choice and Reading Performance (CLM-C)

## Draft Claim Record

---

# Claim
> **Hue as such is a measured near-non-factor for normal-vision reading performance in this base's chromatic-contrast literature: two measurement programs (one interior read, one at abstract level) converge on the finding that text defined by color contrast alone can be read about as fast as text defined by luminance contrast (~300 words/min at high contrast), with the curves superimposing when contrast is expressed in threshold multiples and no additive benefit from combining the two — while for low-vision readers the read source reports color contrast conferred no advantage and all low-vision subjects read large text better with luminance contrast. The hue-for-reading prescription pole is itself thin at the surfaces accessible this session: the read partial-sight guideline prescribes black-and-white as generally most readable and demotes color combinations to large or highlighted text, and the WCAG 2.x formula is hue-blind by construction (contrast computed from relative luminance alone). Hue-response and hue-emotion territory belongs to INV-0020 and is not re-litigated here.**

---

# Element (i) — The Prescriptive Approach (as stated in the practice literature)

- **The read partial-sight guideline (SRC-0189):** "Printed material, generally, is most readable in black and white"; color combinations reserved "only for larger or highlighted text, such as headlines and titles" — a restraint prescription about hue for text.
- **The hue-blind normative construction (SRC-0184, read at the cited surfaces):** WCAG 2.x computes contrast from relative luminance alone — hue does not enter the formula; the prescription pole's dominant artifact treats hue as performance-irrelevant by construction. (Recorded as a fact about the artifact's design, not as evidence it is right.)
- **BOUNDED THINNESS:** no in-base artifact prescribes specific hues *for reading performance* at the surfaces accessible this session (hue-emotion prescriptions exist in INV-0020's territory and stay there). The unread interiors are the disclosed holes this absence claim does not cover.

# Element (ii) — The Stated Rationale

- SRC-0189 (read): "Very high contrasts are difficult to achieve with color combinations other than black and white" — the stated reason for the restraint prescription.
- The two measurement papers' own framing (SRC-0186 read; SRC-0187 abstract): whether chromaticity differences can carry the letter-recognition signal as luminance differences do — the rationale register of the measurement question itself.

# Element (iii) — Measured Human-Performance Evidence (including explicit bounded absence)

- **Chromatic-contrast reading, program one (SRC-0186, interior READ — abstract and conclusions extracted):** eight normal and ten low-vision subjects; drifting text on a color monitor; luminance contrast, red/green color contrast, and combinations. Verbatim: "When color contrast is high, normal subjects can read as rapidly as with high luminance contrast (>300 words/min)"; curves "are superimposed when contrast is measured in multiples of a threshold value"; "there is no sign of additive interaction."
- **Chromatic-contrast reading, program two (SRC-0187, interior unread; abstract-establishable):** with moderate luminance contrast added, chromatic contrast neither helped nor hurt across a 30-fold character-size range; near the luminance-contrast reading threshold, chromatic contrast alone sustained reading rates near 300 words/min. Convergent with program one; different laboratory.
- **Population sub-element — low vision (SRC-0186, read, verbatim):** "We found no advantages of color contrast for low-vision reading. For text composed of 60' characters, all low-vision subjects read better with luminance contrast than with color contrast."
- **EXPLICITLY ABSENT at the surfaces accessible this session:** measured hue effects on reading performance beyond the chromatic-contrast paradigm (e.g., specific-hue text/background pairings at matched contrast; color coding of continuous text; aging-reader hue effects; child-reader hue effects). The unread interiors (SRC-0187 and the rest of the base) are the disclosed holes this absence claim does not cover.

# Element (iv) — Documented Costs and Failure Modes (from the sources; not inferred)

- **The low-vision reversal (SRC-0186, read):** relying on color contrast to carry text costs low-vision readers measured performance — the documented failure mode of hue-borne text.
- **The achievable-contrast cost (SRC-0189, read):** color combinations other than black-and-white make very high contrast difficult to achieve — the guideline's documented reason for restraint.
- **EXPLICITLY EMPTY beyond that** at the surfaces read; unread interiors may document more (the grade reflects this).

---

# Claim Type (KOS-0003 §3)
**Descriptive** — what was measured, what the prescriptions say, and where the boundary with INV-0020's territory lies. No element is normative.

# Evidence (KOS-0003 §4)
Type: **Empirical** (SRC-0186, SRC-0187) and **Documentary** (SRC-0184, SRC-0189).
- SRC-0186 — interior read this session (full-text extraction; abstract and conclusions verbatim). SRC-0189 — read. SRC-0184 — read at the cited surfaces.
- SRC-0187 — abstract level (paywalled), disclosed.

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: **4** — the load-bearing findings are verbatim from a read interior, convergent with an abstract-level second program.
- Relevance: **5** — exactly the hue-versus-performance measurement literature.
- Independence: **3** — two laboratories, but the second program is abstract-level; the guideline shares an author with the second program (Arditi — recorded stake note).
- Quality: **3** — 1990–1991 display apparatus; red/green mixtures only (chromatic axis coverage limited); n = 8 + 10 in the read study.
- Limitations: the chromatic-contrast paradigm does not exhaust "hue choice"; the absence beyond it is bounded above.

# Source Evaluation
Both measurement papers are peer-reviewed academic sources; the guideline and normative artifacts contribute the (i)/(ii) pole with their recorded provenance notes (Lighthouse program authorship spans SRC-0187/0189).

# Assumptions (KOS-0003 §10)
- **The INV-0020 boundary holds:** hue-emotion/response claims are neither cited nor re-litigated; this claim is performance-only.
- **Chromatic contrast ≠ hue identity:** the measured paradigm varies chromaticity difference, not named-hue selection; the record keeps the two distinct and does not convert "color contrast reads fine" into "any hue pairing reads fine."
- **Absence claims bind accessible surfaces only** (bounded in place above).

# Reasoning (KOS-0003 §7)
**Descriptive reporting.** Risk checked: **paradigm overextension** — sliding from red/green chromatic-contrast findings to all hue claims; controlled by the explicit chromatic-contrast ≠ hue-identity bracket and the bounded absence for everything beyond the paradigm. Risk: **Lighthouse shared authorship** across measurement and guideline records, named.

# Confidence (KOS-0003 §8)
- **c_prescriptive_approach — Level 2 (Low):** the hue-for-reading prescription pole is genuinely thin at accessible surfaces — one read restraint prescription and one hue-blind formula; bounded.
- **c_stated_rationale — Level 3 (Moderate):** read directly from the guideline; one artifact.
- **c_measured_performance_evidence — Level 3 (Moderate):** one read interior with verbatim findings plus one convergent abstract-level program; capped by the second interior being unread, the paradigm's chromatic-axis limits, and era-bound apparatus.
- **c_documented_costs_failure_modes — Level 3 (Moderate):** the low-vision reversal is read and verbatim; the achievable-contrast cost read.
- **No Level 4 or 5. Everything R0.**

# Limitations
- Asserts nothing about hue-emotion or hue-response territory (INV-0020's); nothing about specific-hue pairings at matched contrast; nothing about the unread SRC-0187 interior beyond its abstract; no application decision.
- **May not be cited outside Relatio or for any external reliance (R0), regardless of INV-0021's closure state.**

# Alternative Interpretations
1. **"Color contrast reads as well as luminance contrast, so hue pairings are performance-safe."** Refused — the measured equivalence is at *equated threshold multiples* in a controlled paradigm; real hue pairings vary enormously in achievable contrast (SRC-0189's documented point), and the low-vision reversal cuts the other way.
2. **"The thin prescription pole means nobody prescribes hue for reading."** Not asserted — the thinness binds this base's accessible surfaces; hue prescriptions circulate abundantly in INV-0020's response register, which is exactly the boundary recorded.
3. **"Two convergent programs make this High."** Rejected — one program is abstract-level; the convergence is real but not fully read; Moderate is the honest ceiling.

# Relationships (STD-0004)
- `derived_from` SRC-0184, SRC-0186, SRC-0187, SRC-0189.
- `supports` FND-0021.
- `part_of` INV-0021.

# Verification (STD-0006 §7.5 — Specialist disclosure)
**Mixed access, disclosed per source:** SRC-0186 read (laboratory-hosted PDF, abstract and conclusions extracted verbatim); SRC-0189 read; SRC-0184 read at the cited surfaces; SRC-0187 abstract-level (paywalled, no open copy located). Everything **R0; not cleared for external reliance regardless of closure.**

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-08-08|Draft|Created for RQ-0021 (Specialist pass), CLM-C of six. Four separable elements: (i) the thin hue-for-reading prescription pole — read restraint prescription + hue-blind normative formula, bounded (Low); (ii) the achievable-contrast rationale, read (Moderate); (iii) the two-program chromatic-contrast convergence — read verbatim equivalence findings + abstract-level second program + the read low-vision reversal + bounded absence beyond the paradigm (Moderate); (iv) the low-vision reversal and achievable-contrast costs, explicitly empty beyond (Moderate). The INV-0020 boundary honored; hue-response territory untouched. No Level 4/5; R0. Pending Critical Review and structural validation.|

# End CLM-0111
