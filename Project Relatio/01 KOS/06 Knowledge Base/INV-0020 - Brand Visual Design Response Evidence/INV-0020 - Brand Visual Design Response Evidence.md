---
title: INV-0020 - Brand Visual Design Response Evidence
document_type: Investigation Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-08-07
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
  - BrandVisualDesign
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-08-07
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# INV-0020

# Evidence Status of Psychological and Physiological Response Claims in Brand Visual Design

## Draft Investigation Record

> **WHAT THIS INVESTIGATION IS.** A **domain-general** examination of which prescriptive practices in brand visual design — hue selection, color combination, typeface character, mark shape and symbolism, spatial placement, and claimed physiological effects — rest on **measured psychological or physiological response evidence**, which rest on stated rationale, practitioner consensus, or uncited assertion, and what the measured literatures document about robustness (including replication status and context dependence), costs and failure modes, and variation across populations. **It is not a review of Relatio and it names no organization, brand, product, or application decision anywhere in the investigation record** — application happens outside Relatio through the confidence-scale crosswalk.

> **EPISTEMIC POSTURE, STATED AT OPENING.** This literature sits in the region of psychology most affected by the replication crisis; several of its most-cited effects have documented failed replications. **REPLICATION STATUS is therefore a mandatory component of element (iii) on every claim**: a single-study effect and a replicated effect are never graded as equivalent measured evidence, and **a documented failed replication is recorded inside (iii), not buried in (iv)**. The dominant rigorous framework in the hue literature (color-in-context theory) is itself anti-prescriptive; **if the measured base dissolves the prescriptions rather than grounding them, that dissolution is the finding.**

> **THE SOURCE BASE IS FIXED AT EIGHTEEN — SRC-0161…SRC-0178 (Registry v1.48) — and is NOT extended by this investigation.** It does not represent six literatures; **under-coverage is DISCLOSED, never compensated for by reaching outside the base.** The two practitioner records (SRC-0177, SRC-0178) are admitted **DELIBERATELY as the (i)/(ii) pole only** — they state prescriptions; they never evidence them. No SRC identifier is consumed by this investigation (next-free stays **SRC-0179**).

> **CARRIED-FORWARD REVIEWER QUESTION (from INV-0019's closure, binding on the reflexive section):** whether **Moderate discriminates adequately when the content of a component is absence** — a grade earned by a well-documented empty (iii) and a grade earned by a moderately evidenced positive result share a label. CLM-C and CLM-D exist partly as **calibration anchors** (expected stronger measured regions); **if they grade flat with the rest, the reflexive section says so.**

> **STANDING DISCIPLINES (bind throughout the investigation).**
> - **Everything lands R0.** Findings are **NOT cleared for external reliance regardless of closure** (STD-0006 §7.5-analog). The **reserved reflexive section is additionally §7.6-gated**.
> - **Native `Level N (Label)` is the only on-record confidence vocabulary** (KOS-0003 §8). No H-band and no ★-glyphs in any frontmatter or grading field. Split confidence is a **LIST, never averaged**.
> - **All new records at circuit are born conformant per the templates and `validate.py`** (the template and validator are authoritative; discrepancies are reported, not worked around).
> - **Actual execution dates on every row.** Extended-length path handling (STD-0001 §8) applies to any tooling touched.
> - **CI is live** and runs on every push. **A red CI run is a STOP-AND-REPORT**; no tool, validator, or test is edited to make a build pass.

---

# 1. Research Question

**Primary (recorded verbatim from the owner's transfer brief of 2026-08-06, which directs end-to-end execution — treated as the owner's authored question; executed as stated, not edited, narrowed, or broadened):**

> In brand visual design — hue selection, color combination, typeface character, mark shape and symbolism, spatial placement, and claimed physiological effects — which prescriptive practices rest on measured psychological or physiological response evidence, which rest on stated rationale, practitioner consensus, or uncited assertion, and what do the measured literatures document about (a) effect robustness including replication status and context dependence, (b) costs and failure modes of the prescriptions, and (c) variation across populations (age, developmental stage, culture)?

## 1.1 Claim decomposition mandate (recorded at scaffold; NO claim created at scaffold)

**The circuit will produce SIX claims, one per prescription territory.** Each claim carries **four SEPARABLE elements**, recorded as **discrete headed sections** and **separately graded** — the four-element structure precedented in INV-0019, adapted per the brief:

- **(i) THE PRESCRIPTIVE APPROACH** as stated in the practice literature. Descriptive; the (i)/(ii) pole may rest on the practitioner records.
- **(ii) THE STATED RATIONALE** — what the practice literature says the prescription is for. Recorded in that register only; never evidence.
- **(iii) MEASURED PSYCHOLOGICAL/PHYSIOLOGICAL RESPONSE EVIDENCE — INCLUDING REPLICATION STATUS, CONTEXT-DEPENDENCE FINDINGS, AND EXPLICIT ABSENCE where none exists.** A measurement result, never a design rationale. **Replication status is a mandatory component**; a documented failed replication is recorded here.
- **(iv) DOCUMENTED COSTS AND FAILURE MODES** — what the sources record, not what the analyst infers. **Element (iv) entries resting on analyst inference rather than a source are REMOVED from the claim and re-routed to the reflexive section** (the INV-0019 reviewer check, carried forward).

> **SEPARABILITY TEST for (iii) vs (iv) — reviewer-checked.** (iii) is a measurement result; (iv) is what is documented about where and why the prescription breaks down or what it costs. A single source may populate both, but the two are recorded and graded separately and never merged.

**The six claims (identifiers assigned at execution, NOT here):**

- **CLM-A — SINGLE-HUE RESPONSE PRESCRIPTIONS.** "Blue conveys trust, green conveys calm, red conveys urgency" and the color-emotion association family. Core question: **do hue effects survive at PRESCRIPTIVE strength, or only as context-dependent, small, or population-specific effects?** Cross-cultural color-meaning evidence and age/developmental-stage variation distribute here as sub-elements.
- **CLM-B — COLOR-COMBINATION AND HARMONY PRESCRIPTIONS.** Complementary/analogous scheme rules, proportion rules (e.g. 60-30-10), palette-structure response claims. **PRE-AUTHORIZED as a probable near-empty element (iii):** if the measured base is absent or limited to preference ratings dissociated from any response outcome, the absence is recorded explicitly and graded accordingly. **An empty (iii) here is the finding, not a failure.**
- **CLM-C — TYPEFACE CHARACTER AND CONGRUENCE.** Whether typefaces carry measured semantic/personality associations, and whether typeface-offering congruence measurably affects perception or response. Expected among the stronger measured regions; **a calibration anchor.** (iii) scoped to measured impression/congruence outcomes, not designer testimony. Age/developmental variation distributes here where the base supports it.
- **CLM-D — MARK SHAPE AND SYMBOLISM.** Roundness vs angularity, symmetry, elaborateness/naturalness, and symbolic-content claims. Tests how far the real logo-measurement literature's effects extend, at what effect sizes, and **whether symbolic-meaning claims beyond shape geometry have any measured base.** A calibration anchor; population variation distributes here where the base supports it.
- **CLM-E — PLACEMENT AND LAYOUT ATTENTION CLAIMS.** Eye-tracking-derived attention findings vs asserted layout rules. **Three strata distinguished explicitly: measured attention findings, plausible extrapolations from them, and folklore with no citation trail.** The golden-ratio family is expected to land in the third stratum — **verified against SRC-0173, not assumed.**
- **CLM-F — PHYSIOLOGICAL RESPONSE CLAIMS.** Autonomic and arousal effects attributed to color and visual design (heart rate, skin conductance, EEG, the red-effects family). (iii) must record **lab-vs-field setting, sample sizes, and the replication record**; core question: **does ANY physiological finding transfer to a branding prescription at documented strength, or is the transfer step uniformly asserted?**

**POPULATION AND CULTURAL VARIATION distributes as sub-elements** (age/developmental stage primarily within CLM-A/C/D; cross-cultural color-meaning within CLM-A); **no seventh claim is created.**

**No claim is created, and no element is populated, at scaffold.** The four-element shape is the circuit's specification, not a result.

---

# 2. Scope & Disambiguation

All of the following disciplines bind the investigation and are recorded now:

- **DOMAIN-GENERAL ONLY.** No specific organization, brand, product, or application decision appears anywhere in the investigation record. If a drafted sentence names one as an application, it is removed; application happens outside Relatio through the crosswalk. (Named brands may appear only where a **source's own content** is being described — e.g. an infographic built from brand logos — and never as an application.)
- **PRACTITIONER SOURCES ARE THE (i)/(ii) POLE ONLY.** SRC-0177 and SRC-0178 state prescriptions; nothing they assert populates element (iii) anywhere.
- **DESIGN INTENT IS NOT EVIDENCE.** What the practice literature says a prescription achieves is element (ii), never element (iii).
- **CONSENSUS, ADOPTION, AND CIRCULATION ARE NOT EFFICACY.** A prescription's ubiquity is recorded as ubiquity; it evidences nothing.
- **ASSOCIATION IS NOT RESPONSE.** Measured color-emotion **associations** (what people say a color term means, e.g. SRC-0162's survey object) are a distinct measured object from affective, behavioral, or physiological **response** to presented color. The distinction is carried explicitly wherever it matters.
- **PREFERENCE IS NOT RESPONSE OUTCOME.** Preference ratings (e.g. SRC-0165's object) are recorded as preference, never converted into response or effectiveness evidence.
- **REPLICATION STATUS IS MANDATORY IN (iii).** Single-study and replicated effects are never graded as equivalent; documented failed replications are recorded inside (iii), not buried in (iv); where the base carries no replication information for a cited effect, that is stated.
- **ABSENCE IS A FINDING.** "No measured evidence exists in this base," and "the trail terminates in assertion" are legitimate, recordable, expected outcomes. They are not filled.
- **THE LEGIBILITY BOUNDARY (sequencing note, binding).** A second investigation (reading-performance/legibility prescriptions: reading speed, comprehension, contrast thresholds, aging-vision psychophysics) is queued to run AFTER this one under its own brief. **Where this investigation's sources touch legibility or reading performance rather than psychological/physiological response, the boundary is noted and the material left for the queued INV rather than absorbed.**
- **TERMINOLOGICAL DRIFT (STD-0007).** "Emotion," "arousal," "preference," "attention," "association," and "response" are used in overlapping but non-identical senses across these literatures; where a source's usage differs from another's or from Relatio's, say so rather than silently translating.
- **BASE LIMITS.** Eighteen sources do not represent six literatures. Coverage limits are recorded as limits (§8), not silently absorbed.

## 2.1 Scale posture

Native **`Level N (Label)`** only in every frontmatter and grading field (KOS-0003 §8). No ★-glyphs anywhere in any Knowledge Object; no H-band in any grading field.

## 2.2 Reliance posture

**Everything lands R0.** Much of the base is paywalled; interiors are read where accessible and the achievable grade ceiling follows what was actually read — **verification strength is recorded per source, not averaged** — and **findings are NOT cleared for external reliance regardless of closure** (§7.5-analog, declared here at opening). The **reserved reflexive section is additionally §7.6-reflexively-gated.**

---

# 3. Method / Protocol

Execution follows the KOS-0003 pipeline (Question → Claims → Assumptions → Evidence → Confidence) through the **full OPS-0003 circuit** (Research Specialist → Critical Reviewer → Knowledge Architect; Vision Steward/owner closes — the brief's conditional pre-authorization governs closure). Claims are authored via **TPL-0001**; the synthesis via **TPL-0004**. **Sources are cited from the fixed base SRC-0161…SRC-0178**; no source is created and no SRC identifier consumed. All identifiers are registered in the Identifier Registry at execution.

## 3.1 Interior-reading posture

Interiors are read where accessible (several records are open-access or live pages); **where an interior is inaccessible, that is DISCLOSED per source and the affected component grades down for the limit.** Per-source verification strength is recorded, not averaged across the base.

## 3.2 Operative disciplines (bind at circuit)

> **NO PAGE-LEVEL CLAIM FROM AN UNREAD INTERIOR.** A source whose interior was not read supports only what its abstract, metadata, or the citing literature actually establishes, and the record says which.

> **DESIGN RATIONALE MAY NEVER SATISFY ELEMENT (iii).** If the only support for a prescription is that its authors prescribe it, element (iii) is empty and is recorded as empty.

> **ELEMENT (iv) RECORDS DOCUMENTED COSTS AND FAILURE MODES — what the sources say, not what the analyst infers.** An analyst-visible weakness no source discusses is an observation: **REMOVED from the claim, recorded in the reserved reflexive section, and routed.** Element (iv) is not a speculation slot.

> **PRESCRIPTIONS ARE TESTED AT PRESCRIPTIVE STRENGTH.** The question is never merely "does any hue effect exist?" but "does the measured evidence support the prescription as prescribed — context-general, effect-bearing, decision-guiding?" A real but small, context-bound, or population-specific effect does not ground a context-general prescription, and recording that dissolution is a valid measured finding, not a null result.

> **REPLICATION STATUS TRAVELS WITH EVERY (iii) ENTRY.** For every cited effect: replicated / single-study / documented failed replication / no replication information in this base — stated in place. Lab-vs-field setting and sample scale stated for physiological measurements.

> **DISAGREEMENT IS RECORDED AS DISAGREEMENT, at the grade each side earns.** Where sources in the base disagree (the documented replication tension among SRC-0161/0175/0176 in particular), the disagreement is recorded as a disagreement; the circuit does not adjudicate the field's dispute.

---

# 4. Findings / Synthesis

**FILLED at circuit (Specialist pass, 2026-08-07).** The six mandated claims and the synthesis exist:

- **CLM-0103 — Single-Hue Response Prescriptions (CLM-A).** The circulated hue code (live-read artifact, zero citations) against: universal-but-modulated color-emotion ASSOCIATIONS (30 nations, association-level, developmentally emergent preference), the field's own review stating application recommendations are not yet warranted (abstract verbatim), and the red-attraction replication record READ in full — pooled d = 0.26→0.19 / 0.13, I² 89%/53%, decline effect, preregistered subset d = −0.10, adversarial collaboration ending at odds. Explicit absence of any measured brand-asset hue-response transfer. Elements: Moderate ×4.
- **CLM-0104 — Color Combination and Harmony Prescriptions (CLM-B).** The pre-authorized near-empty (iii), found emptier: NO measured response evidence for combinations in base; the nearest measured work (READ) is single-color preference (r = .893, 80% variance, explicitly no combination content); the harmony family sourceable only via the critique literature ("contradictory and ambiguous"); the 60-30-10 rule unsourceable in base. Elements: Low / Low / Moderate / Low.
- **CLM-0105 — Typeface Character and Congruence (CLM-C, calibration anchor).** The base's most measured region — 210-typeface six-dimension impression measurement; font-product congruity on Osgood dimensions — at abstract-level access, single studies, no in-base replication, perception outcomes; population sub-elements explicitly absent. Elements: Moderate / Moderate / Moderate / Low.
- **CLM-0106 — Mark Shape and Symbolism (CLM-D, calibration anchor).** Measured geometry (foundational 1998 logo study; five-experiment circularity/angularity program, abstract-level) kept structurally separate from symbolic-content claims beyond geometry, which have NO measured base here. Elements: Low / Moderate / Moderate / Low.
- **CLM-0107 — Placement and Layout Attention Claims (CLM-E).** The three mandated strata: measured gaze allocation (232-user F-pattern, read live, with its own "rough, general shape" qualification); the visible-but-unmeasured extrapolation from gaze to effectiveness (located inside the origin artifact); the golden-ratio stratum verified to the accessible surface (peer-reviewed examination scoped to "false or seriously misleading" claims; interior scan-blocked, disclosed). Elements: Moderate / Moderate / Moderate / Low.
- **CLM-0108 — Physiological Response Claims (CLM-F).** The least sourceable family; room-scale EEG/EKG evidence with the abstract's own PARADOXICAL heart-rate slowing; lab-vs-field divergence documented in the read meta (waiter/waitress minimal-to-negative); and the central explicit absence — no measured physiological response to any brand asset in this base; the transfer step uniformly unmeasured. Elements: Low / Low / Moderate / Moderate.
- **FND-0020 — the synthesis:** prescriptions outrun measured response evidence in **all six regions within this base**, and the measured regions that exist are non-prescriptive in character (association-level, perception-level, small, context-dependent, adversely replicated, or setting-bound). Eight components; no Level 4, no Level 5; weakest Low (unread-interior coverage).

---

# 5. Confidence Summary (KOS-0003 §8)

**FILLED at circuit.** Native `Level N (Label)`, per component, never averaged. Twenty-four claim components (four separable elements × six claims) plus eight finding components:

| Record | (i) prescriptive approach | (ii) stated rationale | (iii) measured response evidence | (iv) documented costs |
|---|---|---|---|---|
| **CLM-0103** (A — hue) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) |
| **CLM-0104** (B — combination) | 2 (Low) | 2 (Low) | 3 (Moderate) | 2 (Low) |
| **CLM-0105** (C — typeface) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) | 2 (Low) |
| **CLM-0106** (D — mark shape) | 2 (Low) | 3 (Moderate) | 3 (Moderate) | 2 (Low) |
| **CLM-0107** (E — placement) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) | 2 (Low) |
| **CLM-0108** (F — physiological) | 2 (Low) | 2 (Low) | 3 (Moderate) | 3 (Moderate) |

- **FND-0020:** six region pictures 3 (Moderate) · replication_record_adversity 3 (Moderate) · **unread_interior_coverage 2 (Low)** — the binding weakest component.
- **No Level 5 anywhere; no Level 4 anywhere** — the pre-authorized outcome class realized. The absence of any Level 4 is driven jointly by genuine thinness and by access limits (fourteen of eighteen interiors unread) — the distinction is recorded per claim and in the reflexive section.
- **Everything R0** — not cleared for external reliance regardless of closure; the reflexive section is additionally §7.6-gated.

---

# 6. Assumptions & Bracketing (KOS-0003 §10)

Standing brackets, recorded at scaffold; circuit actuals are appended at execution:

- **Domain-general bracket (binding).** No organization, brand, product, or application decision is named anywhere; application is out of scope.
- **Practitioner (i)/(ii) pole bracket.** SRC-0177/SRC-0178 state prescriptions only; nothing they assert is evidence.
- **Association ≠ response; preference ≠ response outcome (§2).** Carried explicitly wherever either literature is cited.
- **Design intent ≠ evidence; circulation ≠ efficacy (§2).**
- **Absence is a finding (§2).** Empty (iii)/(iv) entries are explicit, expected outcomes.
- **Replication posture (§1.1, §3.2).** Single-study ≠ replicated; failed replications recorded inside (iii); the field's replication dispute recorded as a dispute.
- **The legibility boundary (§2).** Reading-performance material is noted and left for the queued investigation.
- **Element (iv) is documented, not inferred (§3.2).** Analyst inferences are removed and routed.
- **The base is fixed at eighteen and does not represent the field (§2, §8).** Under-coverage is disclosed, never compensated for by reaching outside the base.
- **Everything R0; reflexive output additionally §7.6-gated (§2.2).**

**Circuit actuals (2026-08-07):**
- **Interior-reading actuals (§3.1): four of eighteen interiors READ this session** — SRC-0165 (PMC full text), SRC-0172 (live article), SRC-0176 (PMC full text), SRC-0178 (live page); SRC-0161's **abstract retrieved verbatim** (PubMed) and used at abstract level only. **Fourteen interiors NOT read, disclosed and confined per claim:** SRC-0162/0163/0164/0166/0167/0168/0169/0170/0171/0174/0175 (paywalled or no open copy located; the one repository copy attempt for SRC-0169 failed on a certificate error), SRC-0173 (both hosted mirrors are JBIG2 page-image scans with no text layer — the INV-0019 SRC-0152 access-failure class), SRC-0177 (book form, no interior access). Per-source verification strength is recorded in each claim's Verification section, not averaged.
- **The domain discipline held:** no organization, brand, product, or application decision is named anywhere in the six claims, the finding, or this record; the practitioner artifact's own use of brand logos is described generically in the records that cite it.
- **The legibility boundary held:** SRC-0171's reading-behavior territory and the typeface literature's readability adjacency were noted and left unabsorbed (boundary notes in the reflexive section).
- **Two candidate (iv) inferences were withheld at write time** rather than removed post-hoc, per §3.2, and are recorded in the reflexive section.

---

# Reserved Reflexive Section (EMPTY at scaffold — filled and ROUTED at circuit, never applied)

**Governing rule (in force from scaffold):**

> **Observations about what this investigation implies for Relatio's own structure, grading vocabulary, or method are RECOMMENDATIONS.** They are **routed to the Governance Backlog per ADR-GOV-0007 §3**, are **§7.6-reflexively-gated**, and are **NEVER self-applied in session.** No refinement to Relatio follows from this investigation except through separately recorded governance after closure.

**Mandated contents at circuit (per the brief):** (a) any element-(iv) removals re-routed here; (b) the carried-forward **Moderate-discrimination observation** (does Moderate discriminate adequately when the content is absence? — including whether the CLM-C/D calibration anchors graded flat with the rest); (c) any routed Governance Backlog candidates, with identifiers; (d) the boundary notes toward the queued legibility investigation.

## FILLED at circuit (2026-08-07) — ROUTED, NOT APPLIED

**Independence disclosure (ADR-GOV-0011, binding):** this circuit is Claude-family throughout — it supplies **no independence of kind** for any §7.6 purpose, and nothing below may count toward promoting any anchor or practice from provisional toward durable.

**Nothing below is enacted.** No standard, template, tool, field, or vocabulary was created or amended on account of anything in this section; no existing record was revised on account of it.

### (a) Element-(iv) dispositions — two candidate inferences withheld at write time

Per §3.2, an analyst-visible weakness no source discusses is an observation, not a claim element. Two candidate (iv) entries were identified during drafting and **withheld from the claims at write time** (so no post-hoc removal was needed; the reviewer is asked to verify none remains):

1. *"Nationally modulated associations imply a single global hue code misfits somewhere"* — the modulation is documented (SRC-0162 abstract); the implication for palettes is analyst inference. Recorded here only.
2. *"Documented individual-difference moderators imply uniform physiological prescriptions are unreliable"* — the moderation is documented (SRC-0174 abstract); the implication for prescriptions is analyst inference. Recorded here only.

### (b) The Moderate-discrimination observation (carried forward from INV-0019's closure — second data point)

**The question materialized in this circuit, sharply.** Level 3 (Moderate) is carrying at least three distinguishable epistemic situations in this investigation's grades: (1) a **well-documented absence** (CLM-0104 (iii): the emptiness is the finding, and it is well-established over the fixed base); (2) a **measured-but-access-capped positive** (CLM-0105 (iii): real peer-reviewed measurement, establishable only at abstract level); and (3) a **measured-and-read mixed picture** (CLM-0103 (iii): a fully read meta-analysis inside an otherwise surface-level element). The calibration anchors (CLM-C/D) **did grade flat with the absence-dominated claims** — driven substantially by access limits rather than by evidential equivalence — so within this record the discrimination among these situations is being done by prose and `reliance_note`, not by the grade. This is the second investigation in which the observation has arisen (INV-0019's reviewer raised it; this circuit reproduces it with more component contrast). **Routed as GB-2026-058** (below); nothing changed in-session.

### (c) Routed Governance Backlog candidates

- **GB-2026-058** — *Moderate-on-absence discrimination: second data point.* The observation in (b), routed per ADR-GOV-0007 §3 as an owner-reserved candidate (input only; no scale change, no new field, no vocabulary proposed by this session). Recorded in the Governance Backlog concurrently with this circuit's close-out.

### (d) Boundary notes toward the queued reading-performance/legibility investigation

1. **SRC-0171** (eye-tracking monograph) contains reading-behavior territory (how people read, not just where they look) that this investigation deliberately did not use; the queued INV should treat it as a candidate source rather than assuming this record consumed it.
2. **SRC-0172's F-pattern** is a reading-of-text observation; its comprehension and reading-efficiency implications (as opposed to attention allocation) were left unabsorbed and belong to the queued INV.
3. **The typeface literature (SRC-0167/0168) adjoins legibility research** (readability, reading speed) that is a different measured object from impression/congruence; the queued INV needs its own catalog pass there — nothing in this base covers legibility psychophysics, contrast thresholds, or aging vision, and that absence is a coverage note for the queued brief, not a finding of this one.

### Analyst observations recorded here because they fail the element bar

1. **The (i) pole was hardest to source for the strongest-sounding claims:** the physiological and combination families' canonical prescriptions could not be sourced in-base at all, while their measured literatures could — an inversion worth noting for future prep phases (catalog the prescription artifacts, not only the measurement literature).
2. **The base's one live prescription artifact carries zero citations** (the executed trace); whether the wider practitioner literature is better-cited is unknown to this base and recorded as unknown.

---

# 7. Acceptance Criteria for Closing

INV-0020 may close only when all ten of the following hold, each **independently checkable**:

1. **Six claims exist**, one per prescription territory (A–F), each with elements **(i)/(ii)/(iii)/(iv) as discrete headed sections, separately graded**, and **(iii) never merged with (iv)**.
2. **Every claim element cites the specific source(s) supporting it**; no element rests on a source whose interior was unread unless what it rests on is establishable without the interior, and this is stated.
3. **Replication status is visibly recorded inside element (iii) wherever a cited effect has a replication record, positive or failed**, and stated as absent where the base carries none.
4. **Elements (iii) and (iv) are each populated or EXPLICITLY EMPTY for every prescription family discussed**; no element (iv) entry rests on analyst inference (removals routed to the reflexive section).
5. **The domain discipline held:** no organization, brand, product, or application decision is named anywhere in the investigation record.
6. **Population and cultural variation are recorded as sub-elements** within CLM-A/C/D as the base supports, with absence stated where the base is silent; no seventh claim exists.
7. **Per-source verification strength is disclosed**, including which interiors were read and which were not.
8. **A finding (FND) synthesizes the six claims at grades no stronger than their weakest necessary components, with no Level 5**; the CLM-E three-strata distinction and the CLM-A prescriptive-strength verdict are stated in the finding.
9. **The reserved reflexive section is completed and ROUTED, not applied** — carrying its four mandated contents ((iv) removals; the Moderate-discrimination observation; routed GB candidates with identifiers; legibility boundary notes).
10. **Base coverage limits are recorded as limits**, and the record contains no reach outside the fixed base.

**Verification & reliance (§7.5 analog).** Per-source verification strength is disclosed and not averaged. **Everything lands R0 — findings are NOT cleared for external reliance regardless of closure.** The reflexive section's output is additionally **§7.6-reflexively-gated.**

---

# 8. Relationships (STD-0004)

- `part_of` the Knowledge Base — a **classification** statement, not a typed graph edge (no resolvable `part_of` target is declared in frontmatter, matching INV-0009…INV-0019).
- **Frontmatter edges at opening: NONE.** Per **ADR-GOV-0004 D4**, frontmatter references are graph claims and may name only existing objects; no claim or finding exists at scaffold. The catalogued sources attach to **child claims** created at circuit, not to INV-0020 itself. The planned subgraph is declared in **prose** here and edged at execution (existing STD-0004 types only; none invented): each CLM `derived_from` its sources, `supports` the FND, `part_of` INV-0020; the FND `derived_from` the CLMs, `part_of` INV-0020.

## 8.1 Expected source-to-claim bearing — PROSE, and EXPECTATION IS NOT FINDING

From the catalog surface only; a source may bear on other claims, or on none — the circuit reads each source and records what it actually supports:

| Source (catalog) | Expected primary bearing |
|---|---|
| SRC-0161 Elliot & Maier 2014 (color-in-context review) | **A**, **F** |
| SRC-0162 Jonauskaite et al. 2020 (30-nation associations) | **A** (cultural variation) |
| SRC-0163 LoBue & DeLoache 2011 (developmental preference) | **A** (age/developmental variation) |
| SRC-0164 Labrecque & Milne 2012 (brand color measurement) | **A**, **B** |
| SRC-0165 Palmer & Schloss 2010 (ecological valence / preference) | **A**, **B** |
| SRC-0166 O'Connor 2010 (harmony critique) | **B** |
| SRC-0167 Henderson, Giese & Cote 2004 (typeface impressions) | **C** |
| SRC-0168 Doyle & Bottomley 2006 (font-product congruity) | **C** |
| SRC-0169 Henderson & Cote 1998 (logo measurement) | **D** |
| SRC-0170 Jiang et al. 2016 (circular/angular shapes) | **D** |
| SRC-0171 Wedel & Pieters 2008 (eye-tracking review) | **E** |
| SRC-0172 Nielsen 2006 (F-pattern) | **E** (middle stratum candidate) |
| SRC-0173 Markowsky 1992 (golden-ratio misconceptions) | **E** (third stratum verification) |
| SRC-0174 Küller et al. 2009 (EEG/EKG room color) | **F** |
| SRC-0175 Lehmann & Calin-Jageman 2017 (failed replications) | **A**, **F** (replication record) |
| SRC-0176 Lehmann, Elliot & Calin-Jageman 2018 (meta-analysis) | **A**, **F** (replication record) |
| SRC-0177 Wheeler 2017 (brand guide) | (i)/(ii) pole for **B**, **D** (and others as read) |
| SRC-0178 The Logo Company (Color Emotion Guide) | (i)/(ii) pole for **A**; the executed trace |

- The prep-phase source-to-source edges (`contrasts_with` SRC-0161↔SRC-0175; `related_to` SRC-0175↔SRC-0176, SRC-0167↔SRC-0168, SRC-0169↔SRC-0170) are existing catalogued edges recording documented literature relations; they are **not modified by this scaffold**.
- The timeline-program types (`branches_from` / `projects_to` / `influenced_by`) do not apply; **no ENT is created and no timeline edge is contemplated.**

## 8.2 Realized subgraph at circuit (2026-08-07)

The subgraph now exists, carried on the child records per the house pattern (this record itself declares no frontmatter edges; the children edge to it):

- **CLM-0103** `derived_from` SRC-0161, SRC-0162, SRC-0163, SRC-0164, SRC-0175, SRC-0176, SRC-0178 · `supports` FND-0020 · `part_of` INV-0020.
- **CLM-0104** `derived_from` SRC-0165, SRC-0166, SRC-0177 · `supports` FND-0020 · `part_of` INV-0020.
- **CLM-0105** `derived_from` SRC-0167, SRC-0168, SRC-0177 · `supports` FND-0020 · `part_of` INV-0020.
- **CLM-0106** `derived_from` SRC-0169, SRC-0170, SRC-0177 · `supports` FND-0020 · `part_of` INV-0020.
- **CLM-0107** `derived_from` SRC-0171, SRC-0172, SRC-0173 · `supports` FND-0020 · `part_of` INV-0020.
- **CLM-0108** `derived_from` SRC-0161, SRC-0174, SRC-0176 · `supports` FND-0020 · `part_of` INV-0020.
- **FND-0020** `derived_from` CLM-0103…CLM-0108 · `part_of` INV-0020.

**Totals: 22 `derived_from` (claims→sources) + 6 `derived_from` (finding→claims) + 6 `supports` + 7 `part_of`. Every one of the eighteen catalogued sources is cited by at least one claim; no source is cited outside its claims.** Actual bearing versus the §8.1 expectation table: expectations held throughout, with one refinement — SRC-0176 additionally bore on **F** (its lab-vs-field supplementary analyses), which §8.1 anticipated under "A, F (replication record)"; SRC-0177 bore on **B/C/D only at publisher-surface level**, each citing claim saying so. **Identifiers consumed at circuit: CLM-0103…CLM-0108, FND-0020. No ENT consumed; SRC-0179 unconsumed; no new relationship type minted; the catalogued source-base records byte-unmodified.**

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.2|2026-08-07|Draft|**Specialist pass (ROLE-0002) executed under the owner's three-phase brief.** Created CLM-0103 (hue), CLM-0104 (combination/harmony), CLM-0105 (typeface), CLM-0106 (mark shape), CLM-0107 (placement), CLM-0108 (physiological) — each with the four separable elements (i)–(iv) as discrete headed sections, separately graded, (iii) and (iv) never merged, replication status recorded inside (iii) per effect — and FND-0020 (eight components, no Level 5, no Level 4, weakest Low = unread-interior coverage). §4/§5 filled with actuals; §6 gains circuit actuals (interior-reading: four of eighteen READ — SRC-0165/0172/0176/0178 — plus the SRC-0161 abstract verbatim; fourteen unread, disclosed and confined; SRC-0173 scan-blocked at two mirrors; SRC-0169 repository attempt failed on a certificate error). Reserved Reflexive Section FILLED and ROUTED: two withheld (iv) inferences recorded; the carried-forward Moderate-discrimination observation materialized (three distinguishable situations under one label; calibration anchors graded flat, access-driven) and routed as **GB-2026-058**; legibility boundary notes recorded; nothing enacted. §8.2 records the realized subgraph (22+6 `derived_from`, 6 `supports`, 7 `part_of`; all eighteen sources cited). Identifiers consumed: CLM-0103…0108, FND-0020 only; no ENT; SRC-0179 unconsumed. Everything R0. Pending Critical Review (ROLE-0004) and structural validation (ROLE-0001).|
|0.1|2026-08-07|Draft|**Opened as a scaffold (UNFILLED) — the scaffold commit creates no claim, entity, edge, or finding** (house pattern per INV-0016…INV-0019 and ADR-GOV-0004 D4; the executing brief directs scaffold and circuit in one session, a recorded deviation from the two-brief pattern — the circuit fills this record under the same brief after this commit). Authored from **TPL-0003**. Records the §1 primary RQ **verbatim from the owner's 2026-08-06 transfer brief** (which directs end-to-end execution; no separate owner freeze checkpoint is scheduled between scaffold and circuit — reported in the execution report); the §1.1 **six-claim decomposition mandate** (CLM-A hue / CLM-B combination-harmony / CLM-C typeface / CLM-D mark shape / CLM-E placement-attention / CLM-F physiological) with the four separable elements **(i) prescriptive approach / (ii) stated rationale / (iii) measured response evidence incl. mandatory replication status / (iv) documented costs and failure modes**, the (iii)-vs-(iv) separability test, and the (iv) analyst-inference removal rule; the §2 scope disciplines (domain-general; practitioner (i)/(ii) pole; association ≠ response; preference ≠ response outcome; replication mandatory; absence is a finding; the legibility boundary; base limits); the §3 method with operative blockquote rules incl. **prescriptive-strength testing**; §4/§5 reserved; §6 standing brackets; the **Reserved Reflexive Section** (named, empty, §7.6-gated, four mandated contents incl. the carried-forward Moderate-discrimination question); the **ten §7 acceptance criteria**; §8 prose relationships (no frontmatter edges to non-existent objects). Source base **fixed at eighteen (SRC-0161…SRC-0178, Registry v1.48)**; no SRC/CLM/ENT/FND identifier consumed by this scaffold. Template-section mapping matches the INV-0019 precedent (template §7 Relationships → §8 here; template §8 Revision History → §9 here; §7 here is Acceptance Criteria).|

# End INV-0020
