---
title: INV-0021 - Reading Performance Evidence
document_type: Investigation Record
version: 0.1
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

*Reserved. Filled at circuit; no content exists at scaffold.*

---

# 5. Confidence Summary (KOS-0003 §8)

*Reserved. Filled at circuit; native `Level N (Label)`, per component, never averaged.*

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

---

# Reserved Reflexive Section (EMPTY at scaffold — filled and ROUTED at circuit, never applied)

**Governing rule (in force from scaffold):**

> **Observations about what this investigation implies for Relatio's own structure, grading vocabulary, or method are RECOMMENDATIONS.** They are **routed to the Governance Backlog per ADR-GOV-0007 §3**, are **§7.6-reflexively-gated**, and are **NEVER self-applied in session.** No refinement to Relatio follows from this investigation except through separately recorded governance after closure.

**Mandated contents at circuit (per the brief):** (a) any element-(iv) removals re-routed here; (b) the **CLM-D anchor-discrimination observation and the GB-2026-058 data point** — whether CLM-D grades above the absence-dominated claims when interiors are actually read, with interior-reading actuals per source, and an explicit statement if access constraints again flatten the anchor (the third data point); (c) any routed Governance Backlog candidates, with identifiers; (d) boundary notes toward INV-0020 where sources straddled.

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

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-08-08|Draft|**Opened as a scaffold (UNFILLED) — the scaffold commit creates no claim, entity, edge, or finding** (house pattern per INV-0016…INV-0020 and ADR-GOV-0004 D4; the executing brief — REISSUE v2, 2026-08-07, classified C+A+B combined three-phase per the Transfer Brief Standard §5 — directs prep, scaffold, and circuit in one session, a recorded deviation from the two-brief RQ-freeze pattern as precedented by INV-0020; the circuit fills this record under the same brief after this commit; no separate owner freeze checkpoint is scheduled between scaffold and circuit — reported in the execution report). Authored from **TPL-0003**. Records the §1 primary RQ **verbatim from the owner's brief**; the §1.1 **six-claim decomposition mandate** (CLM-A typeface/letterform / CLM-B size-contrast thresholds incl. WCAG provenance / CLM-C hue and reading / CLM-D aging vision, the calibration anchor / CLM-E print vs screen / CLM-F small-screen) with the four separable elements **(i) prescriptive approach / (ii) stated rationale / (iii) measured human-performance evidence incl. explicit bounded absence / (iv) documented costs and failure modes**, the (iii)-vs-(iv) separability test, and the (iv) analyst-inference removal rule; the §2 scope disciplines (domain-general; the INV-0020 boundary; prescription-pole brackets; preference ≠ performance; threshold ≠ optimum ≠ prescription; absence bounded from birth per INV-0020 F2; stakes recorded not adjudicated; base limits); the §3 method with operative blockquote rules incl. **prescriptive-strength testing and derivation testing**; §4/§5 reserved; §6 standing brackets; the **Reserved Reflexive Section** (named, empty, §7.6-gated, four mandated contents incl. the GB-2026-058 third-data-point discipline); the **ten §7 acceptance criteria**; §8 prose relationships (no frontmatter edges to non-existent objects). Source base **fixed at sixteen (SRC-0179…SRC-0194, Registry v1.52)**; no SRC/CLM/ENT/FND identifier consumed by this scaffold. Template-section mapping matches the INV-0019/INV-0020 precedent (template §7 Relationships → §8 here; template §8 Revision History → §9 here; §7 here is Acceptance Criteria).|

# End INV-0021
