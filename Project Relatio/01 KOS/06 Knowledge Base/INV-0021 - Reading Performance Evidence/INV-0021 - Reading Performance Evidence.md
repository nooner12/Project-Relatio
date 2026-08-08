---
title: INV-0021 - Reading Performance Evidence
document_type: Investigation Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-08-08
category:
  - Knowledge Base
  - Design Psychology
  - Investigation
parent_documents:
  - KOS-0008 Research Methodology & Investigation Framework
  - KOS-0003 Epistemic Framework & Knowledge Validation System
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Investigation
  - ReadingPerformance
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-08-08
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# INV-0021

# Evidence Status of Visual-Communication Reading-Performance Prescriptions

## Draft Investigation Record

> ## ✅ CLOSED — 2026-08-08 (full OPS-0003 circuit complete)
> **This investigation is formally CLOSED per ADR-GOV-0004 D1, under the owner's authorization in the 2026-08-07 transfer brief REISSUE v2 (end-to-end execution directed; closure per the operations documents).** The full adversarial circuit ran: Research Specialist (ROLE-0002) → Critical Reviewer (ROLE-0004, verdict **Conformant with Flags**, [[Critical Review - RQ-0021]]) → Knowledge Architect (ROLE-0001, structural validation clean, §6b). All ten §7 acceptance criteria are met with in-record evidence (§7.1). Closure conditions verified: **(a)** all ten criteria genuinely met; **(b)** verdict Conformant with Flags with **both determinate flags (F1 quotation-figure fidelity in CLM-0111; F2 access-level mislabel and omitted size-threshold result in CLM-0109) remediated in-session** (five advisory items — A1/A2/A4/A5 adopted in-session, A3 resolved by the F2 rewrite); **(c)** **no confidence level raised — and none lowered** (all 32 components reviewer-confirmed); **(d)** both validators clean (`validate.py` 465 files, 0 errors / 0 warnings, exit 0; `graph_integrity.py` 0 dangling / 0 branch / 0 projects_to / 0 influenced_by errors; advisories 39 + 2 unchanged) and all 13 detection tests pass.
>
> **Created: CLM-0109…CLM-0114, FND-0021, Critical Review – RQ-0021 — and nothing else.** No entity, no timeline edge, no new relationship type; SRC-0195 and ENT-0019 unconsumed; the source base fixed at sixteen and byte-unmodified by the circuit. **THE RESULT:** the measured/asserted boundary runs between **directions and values** — the measured regions are real and several were read (size/contrast psychophysics, chromatic-contrast equivalence, the aging-vision core, the media meta-analysis), and the prescriptions' specific values still fail to trace to reading measurement in all six territories at the surfaces accessible this session; the WCAG thresholds descend from display standards plus clinical adjustment by their own read chain; the vendor small-screen table is uncited on its read page. **Two Level 4 (High) components on read-and-convergent elements; no Level 5; the calibration anchor DISCRIMINATED (GB-2026-058 third data point, appended, owner-reserved).**
>
> **"Closed" is NOT a maturity promotion** — frontmatter `status` stays **Draft** (ADR-GOV-0005 §1: closure state lives in this banner and the history row). **"Closed" is NOT a clearance for external reliance:** everything lands **R0** and the **findings are NOT cleared for external reliance regardless of closure** (STD-0006 §7.5-analog, declared at opening and re-affirmed here). **The reflexive section's output is additionally §7.6-reflexively-gated** — routed per ADR-GOV-0007 §3, never self-applied; this circuit was Claude-family throughout and supplies no independence of kind.
>
> *Provenance: opened 2026-08-08 as an unfilled scaffold (v0.1); filled by the Specialist pass (v0.2), reviewed and remediated, closed at v0.3 — all under the single three-phase brief REISSUE v2 of 2026-08-07, a recorded deviation from the two-brief pattern precedented by INV-0020. Authored using TPL-0003; twenty-first research workflow (RQ-0021).*

> **WHAT THIS INVESTIGATION IS.** A **domain-general** comparative evidence survey of visual-communication design for reading — typography, luminance/contrast, and hue selection — asking which prescriptive practices rest on **measured human-performance evidence**, which rest on stated rationale or professional consensus only, and what the measured literatures document about costs, failure modes, and variation across populations (aging vision, developing/young readers) and media (print, desktop screen, small handheld screen). **It is not a review of Relatio and it names no organization, brand, product, or application decision anywhere in the investigation record** — application happens outside Relatio through the confidence-scale crosswalk.

> **EPISTEMIC POSTURE, STATED AT OPENING.** Unlike INV-0020's domain, parts of this literature (reading psychophysics, aging vision) are expected to carry a **real measured base**; the survey's value is **locating the boundary between the measured regions and the asserted ones**. A finding that the prescriptions outrun the measurements in fewer than six regions is as legitimate as one that they outrun them in all six — **if CLM-B/D come back genuinely measured, the located boundary is the finding.**

> **THE SOURCE BASE IS FIXED AT SIXTEEN — SRC-0179…SRC-0194 (Registry v1.52) — and is NOT extended by this investigation.** It does not represent these literatures; **under-coverage is DISCLOSED, never compensated for by reaching outside the base.** The three prescription artifacts (SRC-0184 WCAG 2.1, SRC-0193 Apple HIG Typography, SRC-0194 Butterick) are admitted **DELIBERATELY as the (i)/(ii) pole**; the APCA documentation (SRC-0185) is the critique pole carrying its recorded competing-model stake. No SRC identifier is consumed by this investigation (next-free stays **SRC-0195**).

> **CARRIED-FORWARD REVIEWER QUESTION (GB-2026-058, owner-reserved — binding on the reflexive section).** INV-0019 raised and INV-0020 confirmed that **Moderate may not discriminate when the content of a component is absence**, and that access limits can flatten even genuinely-measured calibration anchors to the grade of the absence claims around them. **Do not act on GB-2026-058.** DO record: **(a)** whether CLM-D grades above the absence-dominated claims **when interiors are actually read**, and **(b)** interior-reading actuals per source. If access constraints again flatten the anchor, the reflexive section says so explicitly **as a third data point for the GB item**.

> **STANDING DISCIPLINES (bind throughout the investigation).**
> - **Everything lands R0.** Findings are **NOT cleared for external reliance regardless of closure** (STD-0006 §7.5-analog). The **reserved reflexive section is additionally §7.6-gated**.
> - **ABSENCE CLAIMS ARE BOUNDED FROM BIRTH:** every within-base absence statement is written as "within surfaces accessible this session," with unread interiors disclosed per claim (INV-0020 F2, adopted here as a drafting instruction rather than a remediation).
> - **Native `Level N (Label)` is the only on-record confidence vocabulary** (KOS-0003 §8). No H-band and no ★-glyphs in any frontmatter or grading field. Split confidence is a **LIST, never averaged**.
> - **All new records at circuit are born conformant per the templates and `validate.py`** (the template and validator are authoritative; discrepancies are reported, not worked around).
> - **Actual execution dates on every row.** Extended-length path handling (STD-0001 §8) applies to any tooling touched.
> - **CI is live** and runs on every push. **A red CI run is a STOP-AND-REPORT**; no tool, validator, or test is edited to make a build pass.

---

# 1. Research Question

**Primary (recorded verbatim from the owner's transfer brief of 2026-08-07 REISSUE v2, which directs end-to-end execution — treated as the owner's authored question; executed as stated, not edited, narrowed, or broadened):**

> In visual-communication design for reading — typography, luminance/contrast, and hue selection — which prescriptive practices rest on measured human-performance evidence, which rest on stated rationale or professional consensus only, and what do the measured literatures document about (a) costs and failure modes of the prescriptions and (b) variation across populations (aging vision, developing/young readers) and media (print, desktop screen, small handheld screen)?

## 1.1 Claim decomposition mandate (recorded at scaffold; NO claim created at scaffold)

**The circuit will produce SIX claims, one per prescription territory.** Each claim carries **four SEPARABLE elements**, recorded as **discrete headed sections** and **separately graded** — the four-element structure precedented in INV-0019/INV-0020:

- **(i) THE PRESCRIPTIVE APPROACH** as stated in the design/practice literature. Descriptive; the (i)/(ii) pole may rest on the prescription artifacts.
- **(ii) THE STATED RATIONALE** — what the practice literature says the prescription is for. Recorded in that register only; never evidence.
- **(iii) MEASURED HUMAN-PERFORMANCE EVIDENCE — INCLUDING EXPLICIT ABSENCE where none exists.** Measured reading-performance outcomes (speed, comprehension, error rate, thresholds, preference dissociated from performance), never designer testimony. Replication/robustness information is stated where the base carries it and stated as absent where it does not.
- **(iv) DOCUMENTED COSTS AND FAILURE MODES** — what the sources record, not what the analyst infers. **Element (iv) entries resting on analyst inference rather than a source are REMOVED from the claim and re-routed to the reflexive section** (the INV-0019 reviewer check, carried forward).

> **SEPARABILITY TEST for (iii) vs (iv) — reviewer-checked.** (iii) is a measurement result; (iv) is what is documented about where and why the prescription breaks down or what it costs. A single source may populate both, but the two are recorded and graded separately and never merged.

**The six claims (identifiers assigned at execution, NOT here):**

- **CLM-A — TYPEFACE AND LETTERFORM PRESCRIPTIONS.** Serif vs sans-serif for reading; x-height; stroke-contrast; letter-spacing and line-spacing prescriptions. Element (iii) scoped to measured reading-performance outcomes (speed, comprehension, error rate, preference dissociated from performance), not designer testimony.
- **CLM-B — SIZE AND CONTRAST THRESHOLDS.** Minimum text-size prescriptions and the luminance-contrast thresholds embodied in WCAG 2.x (4.5:1 body / 3:1 large). **Interrogates the provenance of the WCAG 2.x contrast formula and thresholds**, and the measured critique base behind APCA / WCAG 3 candidate models (documented polarity mis-ranking, spatial-frequency ignorance, as claimed by the critique literature). The core question: whether the thresholds rest on **reading measurement** or on standards adapted from other domains.
- **CLM-C — HUE CHOICE AND READING PERFORMANCE.** Whether hue (as distinct from luminance contrast) has measured effects on reading performance — chromatic-contrast reading research, color coding for text. Scoped strictly to performance; **response/emotion claims belong to INV-0020**. If the measured base is thin, the thinness is catalogued.
- **CLM-D — AGE-RELATED VISION CHANGE BEARING ON TYPE AND COLOR.** Lens yellowing and short-wavelength discrimination decline; contrast-sensitivity loss; presbyopia; illumination needs. **Expected to be the strongest measured base in the set — the calibration anchor** (see the GB-2026-058 discipline above). Elements (i)/(ii) scoped to the design prescriptions derived from this literature; the test is whether the derivations match what was measured.
- **CLM-E — PRINT VS SCREEN READING DIVERGENCE.** Whether measured reading performance differs by medium and whether medium-specific prescriptions (sizes, faces, contrast) rest on that measurement or on carryover assumption.
- **CLM-F — SMALL-SCREEN / HANDHELD VS DESKTOP READING.** Viewing distance, effective visual angle, measured performance and scanning differences, and the prescriptions derived for small-screen typography. Distinguishes measured eye-tracking/performance work from **platform vendor guidelines asserted without cited measurement**.

**POPULATION SUB-ELEMENTS (aging, young readers) and MEDIUM SUB-ELEMENTS distribute across claims where the literature locates them; they are not separate claims. No seventh claim is created.**

**No claim is created, and no element is populated, at scaffold.** The four-element shape is the circuit's specification, not a result.

---

# 2. Scope & Disambiguation

All of the following disciplines bind the investigation and are recorded now:

- **DOMAIN-GENERAL ONLY.** No specific organization, brand, product, or application decision appears anywhere in the investigation record. If a drafted sentence names a specific organization's design decision, it is removed; application happens outside Relatio through the crosswalk. (Named platforms/organizations may appear only where a **source's own identity or content** is being described — e.g. a platform vendor's guideline as an artifact — and never as an application.)
- **THE INV-0020 BOUNDARY (binding).** INV-0020 (psychological/physiological response claims in brand visual design) owns persuasion, association, emotion, symbolism, and arousal territory. **Where a source here drifts into response-claims rather than reading performance, the boundary is noted and the material left — INV-0020's claims are not re-litigated.**
- **PRESCRIPTION ARTIFACTS ARE THE (i)/(ii) POLE ONLY.** SRC-0184/0193/0194 state prescriptions; nothing they assert populates element (iii) anywhere. SRC-0189 is a derived-prescription artifact: its prescriptions are (i)/(ii); whether they match the measurements is the CLM-D question.
- **DESIGN INTENT IS NOT EVIDENCE.** What the practice literature says a prescription achieves is element (ii), never element (iii).
- **CONSENSUS, ADOPTION, AND LEGISLATION ARE NOT EFFICACY.** A prescription's ubiquity — including WCAG's legal adoption — is recorded as ubiquity; it evidences nothing about reading performance.
- **PREFERENCE IS NOT PERFORMANCE.** Preference/readability ratings are recorded as preference, and a documented preference-performance dissociation is a legitimate (iii)/(iv) content class, never converted into performance evidence.
- **THRESHOLD ≠ OPTIMUM ≠ PRESCRIPTION.** A measured threshold (where reading fails), a measured optimum (where reading peaks), and a prescribed value are three different objects; the record says which one each cited number is.
- **ABSENCE IS A FINDING, AND IT IS BOUNDED FROM BIRTH.** "No measured evidence within surfaces accessible this session" is a legitimate, recordable, expected outcome, always with unread interiors disclosed per claim.
- **STAKES ARE RECORDED, NOT ADJUDICATED.** The APCA competing-model stake (SRC-0185), the vendor and practitioner commercial stakes, and the shared measurement/prescription authorship in the Lighthouse program are carried as recorded scope-notes wherever those sources are load-bearing.
- **TERMINOLOGICAL DRIFT (STD-0007).** "Legibility," "readability," "reading performance," "visibility," and "accessibility" are used in overlapping but non-identical senses across these literatures; where a source's usage differs from another's or from Relatio's, say so rather than silently translating.
- **BASE LIMITS.** Sixteen sources do not represent these literatures. Coverage limits are recorded as limits (§8), not silently absorbed.

## 2.1 Scale posture

Native **`Level N (Label)`** only in every frontmatter and grading field (KOS-0003 §8). No ★-glyphs anywhere in any Knowledge Object; no H-band in any grading field.

## 2.2 Reliance posture

**Everything lands R0.** Interiors are read where accessible and the achievable grade ceiling follows what was actually read — **verification strength is recorded per source, not averaged** — and **findings are NOT cleared for external reliance regardless of closure** (§7.5-analog, declared here at opening). The **reserved reflexive section is additionally §7.6-reflexively-gated.**

---

# 3. Method / Protocol

Execution follows the KOS-0003 pipeline (Question → Claims → Assumptions → Evidence → Confidence) through the **full OPS-0003 circuit** (Research Specialist → Critical Reviewer → Knowledge Architect; Vision Steward/owner closes — the brief's conditional pre-authorization governs closure). Claims are authored via **TPL-0001**; the synthesis via **TPL-0004**. **Sources are cited from the fixed base SRC-0179…SRC-0194**; no source is created and no SRC identifier consumed. All identifiers are registered in the Identifier Registry at execution.

## 3.1 Interior-reading posture

Interiors are read where accessible; **the CLM-D anchor sources' interiors are prioritized for actual reading** (the brief's instruction, serving the GB-2026-058 data point). Where an interior is inaccessible, that is DISCLOSED per source and the affected component grades down for the limit. Per-source verification strength is recorded, not averaged across the base.

## 3.2 Operative disciplines (bind at circuit)

> **NO PAGE-LEVEL CLAIM FROM AN UNREAD INTERIOR — and the discipline binds NEGATIVE page-level claims equally** (INV-0020 F2). A source whose interior was not read supports only what its abstract, metadata, or the citing literature actually establishes, and the record says which.

> **DESIGN RATIONALE MAY NEVER SATISFY ELEMENT (iii).** If the only support for a prescription is that its authors prescribe it, element (iii) is empty and is recorded as empty — bounded to accessible surfaces.

> **ELEMENT (iv) RECORDS DOCUMENTED COSTS AND FAILURE MODES — what the sources say, not what the analyst infers.** An analyst-visible weakness no source discusses is an observation: **REMOVED from the claim, recorded in the reserved reflexive section, and routed.** Element (iv) is not a speculation slot.

> **PRESCRIPTIONS ARE TESTED AT PRESCRIPTIVE STRENGTH.** The question is never merely "does any size/contrast/typeface effect exist?" but "does the measured evidence support the prescription as prescribed — at its stated values, for its stated populations and media?" A real measured phenomenon that does not reach the prescription's specificity is recorded as exactly that.

> **DERIVATION IS TESTED WHERE CLAIMED.** Where a prescription claims descent from measurement (SRC-0189; WCAG's cited lineage), the claim of descent is examined against what the measurement literature in this base actually reports — at the access level achieved, with the limit disclosed.

> **DISAGREEMENT IS RECORDED AS DISAGREEMENT, at the grade each side earns.** The WCAG/APCA tension in particular is recorded as a documented tension with its stake note; the circuit does not adjudicate the standards dispute.

---

# 4. Findings / Synthesis

**FILLED at circuit (Specialist pass, 2026-08-08).** The six mandated claims and the synthesis exist:

- **CLM-0109 — Typeface and Letterform Prescriptions (CLM-A).** Custom-stated values (10–12 pt / 15–25 px; 120–145%; 45–90 chars, live-read) against: the serif question's one in-base measurement (reading speeds unaffected by serifs in RSVP and continuous reading; a small 5%-serif size-threshold advantage the study attributes to letter spacing; the reported sans-serif preference at citing-literature level only — per Critical Review F2), the Lund lineage critique (72 studies, no valid conclusion, surface-level), the read guideline's own hedges, and bounded absences for the spacing values and populations. Elements: Moderate / Moderate / Moderate / Low.
- **CLM-0110 — Size and Contrast Thresholds (CLM-B).** The brief's provenance interrogation answered from the read chain: WCAG 4.5:1 = ISO/ANSI 3:1 ("standard text and vision") × 1.5 (Arditi-Faye 20/40 contrast-sensitivity association; age-80 framing) — display standards plus clinical adjustment, not reading measurement. Beside it, the READ psychophysics: ~350 wpm across 0.25°–2°, tenfold-contrast tolerance at 1°, no systematic polarity effect, the size-contrast interaction; fluent range 0.2°–2°, CPS 0.15°–0.3°; the abstract-level reserve model; the read APCA critique with its recorded stake and its own validation absence. Elements: Moderate / **High** / Moderate / Moderate.
- **CLM-0111 — Hue Choice and Reading Performance (CLM-C).** Two convergent chromatic-contrast programs (one READ: >300 wpm at high color contrast, threshold-multiple superimposition, no additive interaction; the read low-vision reversal verbatim) against a thin, bounded hue-for-reading prescription pole. The INV-0020 boundary honored. Elements: Low / Moderate / Moderate / Moderate.
- **CLM-0112 — Age-Related Vision Change (CLM-D, the calibration anchor — interiors READ).** The read anchor documents the convergent aging-vision core (contrast-sensitivity decline ~0.3 log units at 8 cpd, optically dominated photopic; ~3× contrast under low luminance; >10-minute dark-adaptation delay; processing-speed slowing; visual-span reading evidence); the read prescription artifact matches measured DIRECTION with uncited VALUES and self-hedged typeface/polarity claims; the blue-region sub-territory is a bounded base absence. Elements: Moderate / Moderate / **High** / Moderate. **The anchor discriminated — the GB-2026-058 access-flattening did not recur.**
- **CLM-0113 — Print vs Screen Reading Divergence (CLM-E).** The READ meta-analysis: paper advantage g = −.21 (54 studies; 171,055 participants; dual-design agreement), moderated by time frame and genre, increasing 2000–2017, NOT age-moderated; Dillon at abstract level (repository 403 disclosed); the medium-split size prescriptions connect to none of it at accessible surfaces. Elements: Moderate / Low / Moderate / Moderate.
- **CLM-0114 — Small-Screen / Handheld Prescriptions (CLM-F).** The live-read vendor table (17/11 pt iOS through 29/23 pt tvOS) with ZERO cited studies on the read page — the executed trace; the narrow measured leg (36.2/32.2 cm abstract-level distances; the read angular frame; the explicitly non-significant device contrast); the bounded absence of any direct small-screen performance measurement in-base. Elements: Moderate / Moderate / **Low** / Moderate.
- **FND-0021 — the synthesis:** the measured/asserted boundary runs between **directions and values** — the measured regions are real (several read) and the prescriptions' specific values still fail to trace to reading measurement in all six territories at accessible surfaces. Eight components; no Level 4 or 5 at finding level; weakest Low (small-screen picture).

---

# 5. Confidence Summary (KOS-0003 §8)

**FILLED at circuit.** Native `Level N (Label)`, per component, never averaged. Twenty-four claim components (four separable elements × six claims) plus eight finding components:

| Record | (i) prescriptive approach | (ii) stated rationale | (iii) measured performance evidence | (iv) documented costs |
|---|---|---|---|---|
| **CLM-0109** (A — typeface) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) | 2 (Low) |
| **CLM-0110** (B — size/contrast) | 3 (Moderate) | 4 (High) | 3 (Moderate) | 3 (Moderate) |
| **CLM-0111** (C — hue) | 2 (Low) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) |
| **CLM-0112** (D — aging, anchor) | 3 (Moderate) | 3 (Moderate) | 4 (High) | 3 (Moderate) |
| **CLM-0113** (E — medium) | 3 (Moderate) | 2 (Low) | 3 (Moderate) | 3 (Moderate) |
| **CLM-0114** (F — small screen) | 3 (Moderate) | 3 (Moderate) | 2 (Low) | 3 (Moderate) |

- **FND-0021:** five territory pictures 3 (Moderate) · small_screen_picture 2 (Low) · measured_asserted_boundary 3 (Moderate) · unread_interior_coverage 3 (Moderate — ten of sixteen interiors read).
- **Two Level 4 (High) components exist, both on read-and-convergent elements** (CLM-0110 (ii): the verbatim-read WCAG derivation chain; CLM-0112 (iii): the read multi-provenance aging-vision core). **No Level 5 anywhere.** The brief pre-authorized no-Level-4-anywhere as an acceptable outcome; it did not mandate it, and the read interiors earned two.
- **Everything R0** — not cleared for external reliance regardless of closure; the reflexive section is additionally §7.6-gated.

---

# 6. Assumptions & Bracketing (KOS-0003 §10)

Standing brackets, recorded at scaffold; circuit actuals are appended at execution:

- **Domain-general bracket (binding).** No organization, brand, product, or application decision is named anywhere as an application; application is out of scope.
- **The INV-0020 boundary (§2).** Response/emotion/association territory stays with INV-0020; boundary notes only.
- **Prescription-pole bracket.** SRC-0184/0193/0194 state prescriptions only; SRC-0189's prescriptions are (i)/(ii) with the derivation question live; nothing any of them asserts is evidence.
- **Preference ≠ performance; threshold ≠ optimum ≠ prescription (§2).**
- **Design intent ≠ evidence; adoption/legislation ≠ efficacy (§2).**
- **Absence is a finding, bounded from birth (§2, §3.2).**
- **Element (iv) is documented, not inferred (§3.2).** Analyst inferences are removed and routed.
- **Stakes recorded, not adjudicated (§2).**
- **The base is fixed at sixteen and does not represent the field (§2, §8).** Under-coverage is disclosed, never compensated for by reaching outside the base.
- **Everything R0; reflexive output additionally §7.6-gated (§2.2).**

**Circuit actuals (2026-08-08):**
- **Interior-reading actuals (§3.1): TEN of sixteen interiors READ this session** — SRC-0179 (mirror PDF full-text extraction), SRC-0182 (laboratory-hosted PDF full-text extraction), SRC-0184 (TR thresholds + the full Understanding SC 1.4.3 derivation chain, live), SRC-0185 (WhyAPCA and repository documentation pages, live), SRC-0186 (laboratory-hosted PDF; abstract and conclusions extracted verbatim), SRC-0188 (PMC full text, PMCID PMC3049199 — **the CLM-D anchor, read as the brief directed**), SRC-0189 (mirrored guideline PDF, full), SRC-0191 (author-hosted PDF full-text extraction), SRC-0193 (live page, prep and circuit), SRC-0194 (live page, prep). **Six interiors NOT read, disclosed and confined per claim:** SRC-0180 (paywalled; abstract), SRC-0181 (no open thesis copy located; surface), SRC-0183 (paywalled; abstract), SRC-0187 (paywalled; abstract), SRC-0190 (the catalogued open repository copy returned HTTP 403 this session; abstract), SRC-0192 (the catalogued LWW full-text URL now 301-redirects to the Wiley journal home after a platform migration; abstract). Per-source verification strength is recorded in each claim's Verification section, not averaged.
- **The domain discipline held:** no organization, brand, product, or application decision is named as an application anywhere; vendor and practitioner artifacts are described as sources under examination.
- **The INV-0020 boundary held:** no response/emotion/association claim made or re-litigated; boundary dispositions recorded in the reflexive section (d).
- **Two candidate (iv) inferences were withheld at write time** per §3.2 and are recorded in the reflexive section (a).
- **Date-stamp errata (disclosed):** the Phase 1/2 records were initially stamped 2026-08-07 (the brief's drafting date) instead of the actual execution date 2026-08-08; caught and corrected in-session before the circuit (errata commit), per the actual-execution-dates standing discipline.

---

# Reserved Reflexive Section (EMPTY at scaffold — filled and ROUTED at circuit, never applied)

**Governing rule (in force from scaffold):**

> **Observations about what this investigation implies for Relatio's own structure, grading vocabulary, or method are RECOMMENDATIONS.** They are **routed to the Governance Backlog per ADR-GOV-0007 §3**, are **§7.6-reflexively-gated**, and are **NEVER self-applied in session.** No refinement to Relatio follows from this investigation except through separately recorded governance after closure.

**Mandated contents at circuit (per the brief):** (a) any element-(iv) removals re-routed here; (b) the **CLM-D anchor-discrimination observation and the GB-2026-058 data point** — whether CLM-D grades above the absence-dominated claims when interiors are actually read, with interior-reading actuals per source, and an explicit statement if access constraints again flatten the anchor (the third data point); (c) any routed Governance Backlog candidates, with identifiers; (d) boundary notes toward INV-0020 where sources straddled.

## FILLED at circuit (2026-08-08) — ROUTED, NOT APPLIED

**Independence disclosure (ADR-GOV-0011, binding):** this circuit is Claude-family throughout — it supplies **no independence of kind** for any §7.6 purpose, and nothing below may count toward promoting any anchor or practice from provisional toward durable.

**Nothing below is enacted.** No standard, template, tool, field, or vocabulary was created or amended on account of anything in this section; no existing record was revised on account of it.

### (a) Element-(iv) dispositions — two candidate inferences withheld at write time

Per §3.2, an analyst-visible weakness no source discusses is an observation, not a claim element. Two candidate (iv) entries were identified during drafting and **withheld from the claims at write time** (the reviewer is asked to verify none remains):

1. *"The closer handheld viewing distances (SRC-0192) imply fixed-size small-screen prescriptions leave less acuity/contrast reserve than their print-derived rationale assumes"* — the distances are documented (abstract level) and the reserve frame is documented (SRC-0183 abstract), but no in-base source connects them; the connection is analyst inference. Recorded here only; CLM-0114 (iv) carries the distance fact with the inference explicitly not drawn.
2. *"The APCA documentation's own uncited thresholds imply a WCAG 3 adoption would repeat the WCAG 2.x provenance pattern"* — the validation absence is documented (read pages, bounded); the projection about future standards adoption is analyst inference. Recorded here only; CLM-0110 carries the symmetric absence without the projection.

### (b) The CLM-D anchor-discrimination observation and the GB-2026-058 data point (third data point — the anchor DISCRIMINATED)

**The access-flattening did not recur.** With interiors actually read (the brief's priority instruction executed — the Owsley anchor read in PMC full text; the derived-prescription artifact read in full), **CLM-0112's element (iii) graded Level 4 (High), above every absence-dominated component in the investigation** (CLM-0114 (iii) Low; CLM-0109 (iv) Low; CLM-0111 (i) Low; CLM-0113 (ii) Low), and a second read-and-convergent element (CLM-0110 (ii), the verbatim-read WCAG derivation chain) also graded High. This is the inverse of the INV-0019/INV-0020 pattern and supports GB-2026-058's diagnosis that the earlier flattening was **access-driven, not vocabulary-driven**: when access lifted, the grade separated.

**The vocabulary question does not disappear — it sharpens.** Moderate still carries distinguishable situations in this record: (1) **read-but-evidence-capped** positives (CLM-0110 (iii): interiors read, capped by small-n and same-laboratory structure; CLM-0113 (iii): a fully read large meta capped by single-source dependence); (2) **mixed access** composites (CLM-0109 (iii): one read leg, two capped legs); (3) **well-documented thin poles** (CLM-0111 (ii)). The discrimination between these is still done by prose and reliance_note, not by the grade — but this circuit shows the grade CAN separate when the evidence does, which localizes GB-2026-058's residual question to within-Moderate discrimination rather than anchor-flattening. **Routed as a third data point APPENDED to GB-2026-058 (owner-reserved; Backlog v1.55); nothing changed in-session; no scale change, field, or vocabulary proposed.**

### (c) Routed Governance Backlog candidates

- **None new.** No structural gap, entity warrant, or vocabulary strain arose that is not already carried by an open item. The GB-2026-058 append in (b) is a data-point contribution to an existing owner-reserved item, not a new candidate. (Two catalog-time access expectations failed at circuit — SRC-0190's 403, SRC-0192's platform migration — which is the GB-2026-051 phenomenon (reachability changes without firing a review trigger) appearing again; recorded here as an observation toward that existing open item, not as a new candidate and not appended to it, since the item already documents the class.)

### (d) Boundary notes toward INV-0020 (dispositions of its reflexive (d) notes, and straddle handling)

1. **SRC-0171 (eye-tracking monograph) was considered per INV-0020's note and NOT admitted:** its measured object is visual-marketing attention allocation, not reading performance; admitting it would have imported attention territory this investigation's RQ does not cover. The catalog pass took the reading-performance literatures directly instead.
2. **SRC-0172's F-pattern reading-efficiency implications were likewise left unabsorbed:** no claim here rests on scanning-pattern material; the F-pattern stays wholly with INV-0020's CLM-0107, and its comprehension/efficiency implications remain unowned by either investigation (a known unclaimed strip, recorded).
3. **The typeface straddle held in the anticipated direction:** SRC-0167/0168 (impression/congruence — INV-0020's measured objects) were not cited here; CLM-0109's territory is performance only. Arditi & Cho's preference finding is carried strictly as preference-performance dissociation, not as an impression claim.
4. **One new straddle arose and was boundary-noted in place:** SRC-0189's aesthetic-preference remark ("the traditional dark on light may be aesthetically preferable") is preference/response territory; CLM-0112 carries it only as the artifact's own documented trade-off, asserting nothing about aesthetic response.

### Analyst observations recorded here because they fail the element bar

1. **The read prescription artifacts vary sharply in evidential self-honesty:** the partial-sight guideline hedges its own claims in place ("some evidence," "little reliable information") while the vendor and practitioner artifacts state values without evidential register at all — a difference in artifact character the element structure has no slot for.
2. **Both catalog-time access expectations that failed did so between prep and circuit in the same session** (a 403 and a platform migration) — the reachability-decay window can be hours, not months.

---

# 6b. Structural Validation (ROLE-0001 — Knowledge Architect, 2026-08-08)

Recorded in-record per the OPS-0003 circuit:

- **`validate.py` at error level: PASS** — 465 files scanned, **0 errors / 0 warnings**, exit 0. Epistemic fields (`confidence` lists with matching STD-0008 labels — components at levels 2, 3, and 4, the two Level 4s intended; `reliance_tier: R0` throughout), review fields (arithmetic checked: Low-weakest records at 6 months → 2027-02-08; Moderate-weakest at 9 months → 2027-05-08), attribution (Stage-1 shape, `ai-delegated`/Claude), and version coherence all well-formed on all nine new/bumped records after remediation.
- **`graph_integrity.py`: clean** — 0 dangling references, 0 `branches_from` / 0 `projects_to` / 0 `influenced_by` edge errors; advisories unchanged (39 non-reciprocated symmetric + 2 legacy) — the circuit added no advisory.
- **Full detection suite: all 13 `tools/tests/test_*.py` PASS**, run as CI runs them.
- **Scale discipline grep-verified over the INV-0021 subtree:** no ★-glyph and no H-band token outside the two prohibition statements in this record; no `level: 5` in any frontmatter; `level: 4` exactly twice (CLM-0110 (ii), CLM-0112 (iii) — the intended Highs); every "Level 5" string is a no-Level-5 statement.
- **Subgraph confirmed against §8.2 programmatically:** the frontmatter `relationships` blocks of CLM-0109…0114 and FND-0021 were parsed and matched edge-for-edge against the §8.2 declaration (28 + 6 `derived_from`, 6 `supports`, 7 `part_of` = 47 edges). No edge exists that §8.2 does not declare; §8.2 declares no edge that does not exist; every one of the sixteen sources is cited by at least one claim.
- **Identifier discipline confirmed:** CLM-0109…CLM-0114 and FND-0021 consumed; **no ENT consumed; SRC-0195 unconsumed**; no relationship type minted; the sixteen catalogued source-base records byte-unmodified by the circuit (their only post-catalog change is the disclosed date-stamp errata, before the circuit).
- **Views regenerated (`build_view.py`): the timeline is byte-identical apart from the generation-metadata line (date + HEAD hash)** — 8 traditions, 5 `branches_from` edges, 8 tradition-reliance badges, unchanged. The stayed-in-lane proof the brief requires. The tree view gains the new INV/CLM/FND/SRC nodes as it should (368 objects; 135 reliance-graded with 135 badges — self-checks pass).

---

# 7. Acceptance Criteria for Closing

INV-0021 may close only when all ten of the following hold, each **independently checkable**:

1. **Six claims exist**, one per prescription territory (A–F), each with elements **(i)/(ii)/(iii)/(iv) as discrete headed sections, separately graded**, and **(iii) never merged with (iv)**.
2. **Every claim element cites the specific source(s) supporting it**; no element rests on a source whose interior was unread unless what it rests on is establishable without the interior, and this is stated.
3. **Every within-base absence statement is bounded to "surfaces accessible this session" from first draft**, with unread interiors disclosed per claim; interior-reading actuals are reported per source.
4. **Elements (iii) and (iv) are each populated or EXPLICITLY EMPTY for every prescription family discussed**; no element (iv) entry rests on analyst inference (removals routed to the reflexive section).
5. **The domain discipline held:** no organization, brand, product, or application decision is named anywhere in the investigation record; the INV-0020 boundary is honored with boundary notes in place of absorption.
6. **Population sub-elements (aging, young readers) and medium sub-elements (print, desktop, handheld) are recorded within claims as the base supports**, with absence stated where the base is silent; no seventh claim exists.
7. **Per-source verification strength is disclosed**, including which interiors were read and which were not; the CLM-D anchor sources' access outcomes are stated explicitly.
8. **A finding (FND) synthesizes the six claims at grades no stronger than their weakest necessary components, with no Level 5**; the finding states the located measured/asserted boundary, including any regions where the measurements genuinely support the prescriptions.
9. **The reserved reflexive section is completed and ROUTED, not applied** — carrying its four mandated contents ((iv) removals; the CLM-D anchor-discrimination observation and GB-2026-058 data point; routed GB candidates with identifiers; INV-0020 boundary notes).
10. **Base coverage limits are recorded as limits**, and the record contains no reach outside the fixed base.

## 7.1 Criteria assessment at closure (2026-08-08 — each ticked with in-record evidence)

1. ✅ **Met.** CLM-0109…0114 exist, one per territory, each with (i)/(ii)/(iii)/(iv) as discrete headed sections and per-element confidence components (§5 table); separability reviewer-verified (Critical Review – RQ-0021 check (a)).
2. ✅ **Met.** Every element cites its specific sources in place; unread-interior confinement stated per assertion (reviewer check (j)); the one access-level mislabel (F2 — the sans-serif preference carried as abstract-establishable when it is citing-literature level) remediated in-session in CLM-0109, FND-0021, and §4 here.
3. ✅ **Met.** Every within-base absence statement was bounded to accessible surfaces **from first draft** (the INV-0020 F2 rule as drafting instruction — reviewer check (b) found no flat absence claim); interior-reading actuals reported per source (§6 circuit actuals; per-claim Verification sections; reviewer check (i) confirmed consistency, with A5's partial-read clarification adopted).
4. ✅ **Met.** (iii)/(iv) populated or explicitly empty throughout; no (iv) entry rests on analyst inference — the two withheld inferences sit in the reflexive section (a), and the reviewer verified no third remains (check (c)).
5. ✅ **Met.** Domain discipline held (reviewer check (f)); the INV-0020 boundary honored with four dispositions recorded in the reflexive section (d) in place of absorption (reviewer check (k)).
6. ✅ **Met.** Population sub-elements recorded where the base supports them (low-vision reversal in CLM-0111; the aging core in CLM-0112; no-age-moderation in CLM-0113) and as explicit absences elsewhere (CLM-0109, CLM-0114); no seventh claim (reviewer check (h); Registry-consistent: CLM-0109…0114, FND-0021 only).
7. ✅ **Met.** Per-source verification strength disclosed per claim, not averaged; the CLM-D anchor access outcomes stated explicitly (both anchor interiors READ — §6, CLM-0112 Verification; reviewer check (i)).
8. ✅ **Met.** FND-0021 synthesizes at eight components capped at weakest necessary; **no Level 5 anywhere and no Level 4 at the finding level**; the located boundary — directions vs values, including the two genuinely measured-and-read regions — is the finding's §1 statement.
9. ✅ **Met.** The reflexive section is completed and ROUTED with all four mandated contents: two withheld (iv) inferences; the CLM-D anchor-discrimination observation and the GB-2026-058 third data point (the anchor DISCRIMINATED — reviewer-verified as honestly earned, and the Backlog append verified present, correctly gated, amending nothing); zero new GB candidates, stated with the GB-2026-051 observation left unappended; the INV-0020 boundary dispositions.
10. ✅ **Met.** Base limits recorded as limits (FND-0021 §4; §2/§8 here); no reach outside the fixed base (reviewer checks (d)/(o): no out-of-base source cited as evidence anywhere).

**Verification & reliance (§7.5 analog).** Per-source verification strength is disclosed and not averaged; ten of sixteen interiors were read this session (three partial, disclosed), and the Critical Review independently live-verified thirteen targets against primaries (its §1) — the review was NOT verification-light. **Everything lands R0 — findings are NOT cleared for external reliance regardless of closure.** The reflexive section's output is additionally **§7.6-reflexively-gated.**

---

# 8. Relationships (STD-0004)

- `part_of` the Knowledge Base — a **classification** statement, not a typed graph edge (no resolvable `part_of` target is declared in frontmatter, matching INV-0009…INV-0020).
- **Frontmatter edges at opening: NONE.** Per **ADR-GOV-0004 D4**, frontmatter references are graph claims and may name only existing objects; no claim or finding exists at scaffold. The catalogued sources attach to **child claims** created at circuit, not to INV-0021 itself. The planned subgraph is declared in **prose** here and edged at execution (existing STD-0004 types only; none invented): each CLM `derived_from` its sources, `supports` the FND, `part_of` INV-0021; the FND `derived_from` the CLMs, `part_of` INV-0021.

## 8.1 Expected source-to-claim bearing — PROSE, and EXPECTATION IS NOT FINDING

From the catalog surface only; a source may bear on other claims, or on none — the circuit reads each source and records what it actually supports:

| Source (catalog) | Expected primary bearing |
|---|---|
| SRC-0179 Legge & Bigelow 2011 (print size review) | **B**, **A**, **F** (visual-angle frame) |
| SRC-0180 Arditi & Cho 2005 (serif measurement) | **A** |
| SRC-0181 Lund 1999 (legibility-research critique) | **A** (the lineage's evidential status) |
| SRC-0182 Legge, Rubin & Luebker 1987 (contrast) | **B** |
| SRC-0183 Whittaker & Lovie-Kitchin 1993 (reserves) | **B**, **D** |
| SRC-0184 WCAG 2.1 (normative thresholds) | (i)/(ii) pole for **B**; the provenance question |
| SRC-0185 APCA documentation (critique; stake noted) | **B** (critique pole) |
| SRC-0186 Legge et al. 1990 (color contrast XI) | **C** |
| SRC-0187 Knoblauch, Arditi & Szlyk 1991 (chromatic reading) | **C** |
| SRC-0188 Owsley 2011 (aging vision) | **D** (anchor; interior prioritized) |
| SRC-0189 Arditi Lighthouse (derived prescriptions) | (i)/(ii) pole for **D**; the derivation test |
| SRC-0190 Dillon 1992 (paper vs screens review) | **E** |
| SRC-0191 Delgado et al. 2018 (media meta-analysis) | **E** (+ young-reader population sub-elements) |
| SRC-0192 Bababekova et al. 2011 (viewing distance) | **F** |
| SRC-0193 Apple HIG Typography (vendor guideline) | (i)/(ii) pole for **F** (and A/B as read) |
| SRC-0194 Butterick Practical Typography (practitioner) | (i)/(ii) pole for **A**, **B** |

- The prep-phase source-to-source edges (`contrasts_with` SRC-0184↔SRC-0185; `related_to` SRC-0179↔SRC-0182, SRC-0180↔SRC-0181, SRC-0186↔SRC-0187, SRC-0190↔SRC-0191) are existing catalogued edges recording documented literature relations; they are **not modified by this scaffold**.
- The timeline-program types (`branches_from` / `projects_to` / `influenced_by`) do not apply; **no ENT is created and no timeline edge is contemplated.** If an entity-warrant question genuinely arises, it is LOGGED as a backlog candidate and the circuit continues without minting.

## 8.2 Realized subgraph at circuit (2026-08-08)

The subgraph now exists, carried on the child records per the house pattern (this record itself declares no frontmatter edges; the children edge to it):

- **CLM-0109** `derived_from` SRC-0179, SRC-0180, SRC-0181, SRC-0189, SRC-0193, SRC-0194 · `supports` FND-0021 · `part_of` INV-0021.
- **CLM-0110** `derived_from` SRC-0179, SRC-0182, SRC-0183, SRC-0184, SRC-0185, SRC-0194 · `supports` FND-0021 · `part_of` INV-0021.
- **CLM-0111** `derived_from` SRC-0184, SRC-0186, SRC-0187, SRC-0189 · `supports` FND-0021 · `part_of` INV-0021.
- **CLM-0112** `derived_from` SRC-0179, SRC-0183, SRC-0184, SRC-0188, SRC-0189 · `supports` FND-0021 · `part_of` INV-0021.
- **CLM-0113** `derived_from` SRC-0190, SRC-0191, SRC-0194 · `supports` FND-0021 · `part_of` INV-0021.
- **CLM-0114** `derived_from` SRC-0179, SRC-0191, SRC-0192, SRC-0193 · `supports` FND-0021 · `part_of` INV-0021.
- **FND-0021** `derived_from` CLM-0109…CLM-0114 · `part_of` INV-0021.

**Totals: 28 `derived_from` (claims→sources) + 6 `derived_from` (finding→claims) + 6 `supports` + 7 `part_of` = 47 edges. Every one of the sixteen catalogued sources is cited by at least one claim; no source is cited outside its claims.** Actual bearing versus the §8.1 expectation table: expectations held with three refinements — SRC-0179 additionally bore on **D** (the fluent-range upper bound as a documented oversizing cost) and its CLM-A bearing is via the size-variable frame rather than serif content; SRC-0184 additionally bore on **C** (the hue-blind formula construction) and **D** (the age-anchored derivation); SRC-0191 additionally bore on **F** (the explicitly non-significant device contrast). **Identifiers consumed at circuit: CLM-0109…CLM-0114, FND-0021. No ENT consumed; SRC-0195 unconsumed; no new relationship type minted; the sixteen catalogued source-base records byte-unmodified by the circuit.**

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.3|2026-08-08|Draft|**Circuit completed and INVESTIGATION CLOSED per ADR-GOV-0004 D1, under the brief-directed authorization (REISSUE v2).** Critical Review – RQ-0021 (ROLE-0004): verdict **Conformant with Flags** — two determinate flags (F1 quotation-figure fidelity: "60'" → "6°" in CLM-0111's verbatim low-vision quote, a PDF-extraction artifact caught against the primary; F2 access-level mislabel and omitted result in CLM-0109: the sans-serif preference relabeled to citing-literature level, the RSVP/continuous phrasing corrected, the 5%-serif size-threshold result added, propagated to FND-0021 §1(1) and §4 here), **both remediated in-session** (affected records → v0.2 with per-flag history rows); five advisory items — A1 (APCA claim pinned to its carrying page, CLM-0110 v0.2), A2 (the CLM-0112 High's independence structure clarified, v0.2), A4 (tvOS observation softened, CLM-0114 v0.2), A5 (partial-read disclosure in FND-0021 v0.2 and §6 here) adopted in-session; A3 resolved by the F2 rewrite; **no confidence level raised, none lowered** (all 32 components confirmed); the review was NOT verification-light — thirteen targets live-verified against primaries, no fabrication found. Structural validation (ROLE-0001) recorded at **§6b**: validate.py 465/0/0 exit 0; graph_integrity 0/0/0/0, advisories 39+2 unchanged; all 13 detection tests pass; scale discipline grep-verified (the two `level: 4` entries are the intended Highs); subgraph parsed and matched edge-for-edge against §8.2 (47 edges); identifier discipline confirmed; **views regenerated with the timeline byte-identical apart from the generation line — the stayed-in-lane proof**. **All ten §7 criteria re-assessed and ticked with in-record evidence (§7.1).** Closure banner installed citing the four conditions (a)–(d), all verified. Frontmatter `status` untouched (Draft — ADR-GOV-0005 §1). **Findings NOT cleared for external reliance regardless of closure (everything R0); the reflexive output additionally §7.6-gated.** The directions-vs-values boundary is the located finding; the anchor discriminating is the GB-2026-058 third data point, appended and owner-reserved.|
|0.2|2026-08-08|Draft|**Specialist pass (ROLE-0002) executed under the owner's three-phase brief (REISSUE v2).** Created CLM-0109 (typeface/letterform), CLM-0110 (size/contrast incl. the WCAG-provenance answer), CLM-0111 (hue-reading), CLM-0112 (aging vision — the calibration anchor, interiors READ), CLM-0113 (print vs screen), CLM-0114 (small screen) — each with the four separable elements (i)–(iv) as discrete headed sections, separately graded, (iii) and (iv) never merged, every within-base absence bounded to accessible surfaces from first draft — and FND-0021 (eight components; the directions-vs-values boundary formulation; no Level 4/5 at finding level; weakest Low = small-screen picture). §4/§5 filled with actuals; §6 gains circuit actuals (interior-reading: TEN of sixteen READ — SRC-0179/0182/0184/0185/0186/0188/0189/0191/0193/0194; six unread disclosed per claim incl. two catalog-time access expectations that failed at circuit: SRC-0190 repository 403, SRC-0192 platform migration; the Phase 1/2 date-stamp errata disclosed). Reserved Reflexive Section FILLED and ROUTED: two withheld (iv) inferences; **the GB-2026-058 third data point — the anchor DISCRIMINATED (CLM-0112 (iii) High with interiors read; the earlier flattening localized as access-driven)**, appended to GB-2026-058; zero new GB candidates (the reachability observation recorded toward existing GB-2026-051 without amendment); four INV-0020 boundary dispositions incl. the SRC-0171 non-admission reasoning. §8.2 records the realized subgraph (28+6 `derived_from`, 6 `supports`, 7 `part_of` = 47 edges; all sixteen sources cited). Identifiers consumed: CLM-0109…0114, FND-0021 only; no ENT; SRC-0195 unconsumed. **Two Level 4 (High) components on read-and-convergent elements (CLM-0110 (ii), CLM-0112 (iii)); no Level 5 anywhere.** Everything R0. Pending Critical Review (ROLE-0004) and structural validation (ROLE-0001).|
|0.1|2026-08-08|Draft|**Opened as a scaffold (UNFILLED) — the scaffold commit creates no claim, entity, edge, or finding** (house pattern per INV-0016…INV-0020 and ADR-GOV-0004 D4; the executing brief — REISSUE v2, 2026-08-07, classified C+A+B combined three-phase per the Transfer Brief Standard §5 — directs prep, scaffold, and circuit in one session, a recorded deviation from the two-brief RQ-freeze pattern as precedented by INV-0020; the circuit fills this record under the same brief after this commit; no separate owner freeze checkpoint is scheduled between scaffold and circuit — reported in the execution report). Authored from **TPL-0003**. Records the §1 primary RQ **verbatim from the owner's brief**; the §1.1 **six-claim decomposition mandate** (CLM-A typeface/letterform / CLM-B size-contrast thresholds incl. WCAG provenance / CLM-C hue and reading / CLM-D aging vision, the calibration anchor / CLM-E print vs screen / CLM-F small-screen) with the four separable elements **(i) prescriptive approach / (ii) stated rationale / (iii) measured human-performance evidence incl. explicit bounded absence / (iv) documented costs and failure modes**, the (iii)-vs-(iv) separability test, and the (iv) analyst-inference removal rule; the §2 scope disciplines (domain-general; the INV-0020 boundary; prescription-pole brackets; preference ≠ performance; threshold ≠ optimum ≠ prescription; absence bounded from birth per INV-0020 F2; stakes recorded not adjudicated; base limits); the §3 method with operative blockquote rules incl. **prescriptive-strength testing and derivation testing**; §4/§5 reserved; §6 standing brackets; the **Reserved Reflexive Section** (named, empty, §7.6-gated, four mandated contents incl. the GB-2026-058 third-data-point discipline); the **ten §7 acceptance criteria**; §8 prose relationships (no frontmatter edges to non-existent objects). Source base **fixed at sixteen (SRC-0179…SRC-0194, Registry v1.52)**; no SRC/CLM/ENT/FND identifier consumed by this scaffold. Template-section mapping matches the INV-0019/INV-0020 precedent (template §7 Relationships → §8 here; template §8 Revision History → §9 here; §7 here is Acceptance Criteria).|

# End INV-0021
