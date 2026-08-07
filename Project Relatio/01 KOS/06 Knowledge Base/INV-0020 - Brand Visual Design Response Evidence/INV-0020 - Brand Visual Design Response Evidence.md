---
title: INV-0020 - Brand Visual Design Response Evidence
document_type: Investigation Record
version: 0.1
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

**RESERVED for the circuit.** The six mandated claims and the synthesis (FND) do not exist at scaffold; identifiers are assigned at execution.

---

# 5. Confidence Summary (KOS-0003 §8)

**RESERVED for the circuit.** Native `Level N (Label)`, per component, never averaged: twenty-four claim components (four separable elements × six claims) plus the finding's components, filled at execution.

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

---

# Reserved Reflexive Section (EMPTY at scaffold — filled and ROUTED at circuit, never applied)

**Governing rule (in force from scaffold):**

> **Observations about what this investigation implies for Relatio's own structure, grading vocabulary, or method are RECOMMENDATIONS.** They are **routed to the Governance Backlog per ADR-GOV-0007 §3**, are **§7.6-reflexively-gated**, and are **NEVER self-applied in session.** No refinement to Relatio follows from this investigation except through separately recorded governance after closure.

**Mandated contents at circuit (per the brief):** (a) any element-(iv) removals re-routed here; (b) the carried-forward **Moderate-discrimination observation** (does Moderate discriminate adequately when the content is absence? — including whether the CLM-C/D calibration anchors graded flat with the rest); (c) any routed Governance Backlog candidates, with identifiers; (d) the boundary notes toward the queued legibility investigation.

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

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-08-07|Draft|**Opened as a scaffold (UNFILLED) — the scaffold commit creates no claim, entity, edge, or finding** (house pattern per INV-0016…INV-0019 and ADR-GOV-0004 D4; the executing brief directs scaffold and circuit in one session, a recorded deviation from the two-brief pattern — the circuit fills this record under the same brief after this commit). Authored from **TPL-0003**. Records the §1 primary RQ **verbatim from the owner's 2026-08-06 transfer brief** (which directs end-to-end execution; no separate owner freeze checkpoint is scheduled between scaffold and circuit — reported in the execution report); the §1.1 **six-claim decomposition mandate** (CLM-A hue / CLM-B combination-harmony / CLM-C typeface / CLM-D mark shape / CLM-E placement-attention / CLM-F physiological) with the four separable elements **(i) prescriptive approach / (ii) stated rationale / (iii) measured response evidence incl. mandatory replication status / (iv) documented costs and failure modes**, the (iii)-vs-(iv) separability test, and the (iv) analyst-inference removal rule; the §2 scope disciplines (domain-general; practitioner (i)/(ii) pole; association ≠ response; preference ≠ response outcome; replication mandatory; absence is a finding; the legibility boundary; base limits); the §3 method with operative blockquote rules incl. **prescriptive-strength testing**; §4/§5 reserved; §6 standing brackets; the **Reserved Reflexive Section** (named, empty, §7.6-gated, four mandated contents incl. the carried-forward Moderate-discrimination question); the **ten §7 acceptance criteria**; §8 prose relationships (no frontmatter edges to non-existent objects). Source base **fixed at eighteen (SRC-0161…SRC-0178, Registry v1.48)**; no SRC/CLM/ENT/FND identifier consumed by this scaffold. Template-section mapping matches the INV-0019 precedent (template §7 Relationships → §8 here; template §8 Revision History → §9 here; §7 here is Acceptance Criteria).|

# End INV-0020
