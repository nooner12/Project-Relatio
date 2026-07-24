---
title: INV-0019 - Structured-Knowledge Systems Comparative Survey
document_type: Investigation Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-24
category:
  - Knowledge Base
  - Knowledge Systems
  - Investigation
parent_documents:
  - KOS-0008 Research Methodology & Investigation Framework
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - KOS-0007 Comparative Analysis Framework
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Investigation
  - KnowledgeSystems
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-24
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# INV-0019

# How External Structured-Knowledge Systems Solve Four Recurring Design Problems — A Comparative Survey (Claim Atomicity · Expert-to-Lay Register · Recoverable Source-to-Claim Mapping · Warranted Typed Relationships)

## Draft Investigation Record

> ## 🟡 OPENED AS A SCAFFOLD — 2026-07-24 (UNFILLED; the circuit fills it under a separate brief)
> **This record OPENS INV-0019 and does nothing else.** Per **STD-0006 §7.6** independence, **the session that opens a scaffold does not fill it**: **no claim, entity, edge, or finding is created here.** The scaffold states the question, the decomposition mandate, the scope disciplines, the method, and the acceptance criteria. The **circuit brief (3 of 3)** answers it after the owner reviews this scaffold. Authored using **TPL-0003** (mapping to the template's section numbering recorded in the Revision-History note and reported in the scaffold report). Nineteenth research workflow (RQ-0019).
>
> **RQ FREEZE CHECKPOINT.** The §1 primary wording is **authoritative pending owner freeze**, and the freeze happens at the **owner's review of THIS scaffold report** — not in this session. The RQ is recorded **verbatim as authored** and is **not** edited, improved, narrowed, or broadened here.
>
> **"Opened" is NOT a maturity promotion** — the frontmatter `status` stays **Draft** (ADR-GOV-0005 §1: closure/opening state lives in this banner and the history row, not in frontmatter).

> **WHAT THIS INVESTIGATION IS.** A **comparative survey of how OTHER, EXTERNAL structured-knowledge systems** — in argumentation modelling, evidence synthesis, semantic publishing, and professional citation practice — solve four recurring design problems. **It is not a review of Relatio, and it produces no recommendation about Relatio in this session or the next.** External systems only (§2).

> **THE FOUR DESIGN PROBLEMS — each answers a RECORDED Governance Backlog item, not a session intuition. The backlog linkage is the investigation's WARRANT FOR EXISTING; it is NOT permission to answer those items here** (they are answered later, by recorded governance, after the survey closes):
> | Design problem | Backlog warrant |
> |---|---|
> | **A. Claim atomicity** | **GB-2026-045** (atomicity under-firing) |
> | **B. Expert-to-lay register** | **GB-2026-044** (register legibility to an outside reader) |
> | **C. Source-to-claim mapping recoverable from the record** | **GB-2026-046** (application transparency) |
> | **D. Warranted typed relationships** | **GB-2026-043** (typed-relationship / anchor-fit residue) |

> **THE SOURCE BASE IS FIXED AT NINE — SRC-0152…SRC-0160 — and is NOT extended by this brief.** It does **not** represent four fields; **under-coverage is DISCLOSED, never compensated for by reaching outside the base** (§2 base-limits; §8). **Conklin & Begeman's gIBIS (1988) was cut by recorded owner decision — it is not restored.** No SRC identifier is consumed here (next-free stays **SRC-0161**).

> **TWO SUPPORT-SURFACE OBSERVATIONS — HYPOTHESES TO BE TESTED AT CIRCUIT, NOT FACTS TO BE RECORDED.** Two characterizations arose in support-surface searching on 2026-07-24; they are **NOT in the vault, NOT verified, and NOT findings**, and **neither is transcribed into any record here or at circuit.** They concern (a) the adherence of Cochrane plain-language summaries to the PLEACS standard, and (b) the accuracy and inter-tool agreement of mature legal citators. **If the circuit uses either, it DERIVES it from SRC-0159 / SRC-0160 directly and reports what those sources actually say; where a source says something different, THE SOURCE WINS and the discrepancy is reported.** This is the transcription anti-pattern being fenced deliberately: a value that inherits confidence from a source must be derived at execution, never carried through the support surface. (Neither figure nor characterization is stated in this scaffold, by design.)

> **STANDING DISCIPLINES (bind throughout the investigation).**
> - **Everything lands R0.** Findings are **NOT cleared for external reliance regardless of closure** (STD-0006 §7.5-analog). The **reserved reflexive section is additionally §7.6-gated**.
> - **Native `Level N (Label)` is the only on-record confidence vocabulary** (KOS-0003 §8). **No H-band and no ★-glyphs in any frontmatter or grading field.** Split confidence is a **LIST, never averaged**.
> - **All new records at circuit are born conformant PER THE TEMPLATE AND `validate.py`** (the template and validator are authoritative; any discrepancy is reported, not worked around).
> - **Actual execution dates on every row.** Extended-length path handling (STD-0001 §8) applies to any tooling touched.
> - **CI is live** and runs on every push. **A red CI run is a STOP-AND-REPORT, never a thing to patch around**; no tool, validator, or test is edited to make a build pass.

---

# 1. Research Question

**Primary (authoritative wording pending owner freeze at this scaffold's review — recorded verbatim, not edited, narrowed, or broadened):**

> Across established structured-knowledge systems — in argumentation modelling, evidence synthesis, semantic publishing, and professional citation practice — how does each system individuate a claim, serve expert and lay readers from a single record, make the path from source to claim recoverable, and warrant its typed relationships; what empirical evidence exists that these approaches perform as their designers intended; and what is documented about where they break down and what they cost to operate?

## 1.1 Claim decomposition mandate (recorded now; NO claim created this session)

**The circuit will produce FOUR claims, one per design problem.** The mandate is recorded here; **this session creates no claim.** Each claim carries **four SEPARABLE elements**, and **separability is a reviewer-checked criterion** — the lesson carried from INV-0011 criterion #2 (and applied through INV-0016/0017/0018) that "treated in prose" is not "answered separably." Elements **(i) / (ii) / (iii) / (iv)** must appear as **discrete headed sections** of each claim record.

- **(i) APPROACH.** What the surveyed systems actually **do** about this problem, as documented by the sources. **Descriptive.**
- **(ii) STATED RATIONALE.** What each system's **own documentation** says the approach is **for**. This is a fact **ABOUT the system's design intent** and is recorded **in that register only**.
- **(iii) EVIDENCE OF PERFORMANCE.** What was **MEASURED** and what it **showed** — **including its ABSENCE.** An **empty (iii) is the expected result for most systems and is a real finding.**
- **(iv) DOCUMENTED COSTS AND FAILURE MODES.** What the sources record about **where the approach breaks down, what it burdens its users with, and what it trades away.** Includes **structural costs the sources identify without measuring** (vocabulary size against annotator consistency; training required to apply a notation correctly; effort to keep a record current).

> **SEPARABILITY TEST for (iii) vs (iv) — reviewer-checked.** **(iii) is a measurement result; (iv) is what is documented about where and why the approach breaks down or what it costs.** A single source may populate **both** — a study reporting a low adherence rate populates **(iii)** with the measurement and **(iv)** with whatever that study documents about the **causes** — but the two are **recorded and GRADED SEPARATELY and are never merged.**

**The four claims (identifiers assigned at execution, NOT here):**

- **CLM A — CLAIM ATOMICITY** *(warrant: GB-2026-045)*. How systems **individuate a claim**: where the split line falls, what counts as one assertion, and what rules (if any) govern it.
- **CLM B — EXPERT-TO-LAY REGISTER** *(warrant: GB-2026-044)*. How systems **serve expert and lay readers from a single record**, and what governs what **must** appear in the lay register.
- **CLM C — RECOVERABLE SOURCE-TO-CLAIM MAPPING** *(warrant: GB-2026-046)*. How systems make the **path from a source to a claim inspectable by a reader** — what is captured, what is rendered, and what is left implicit.
- **CLM D — WARRANTED TYPED RELATIONSHIPS** *(warrant: GB-2026-043)*. What **typed-relationship vocabularies** exist, how a type is **warranted or merely asserted**, how **large** the vocabularies are, and how they are **enforced** (if at all).

**No claim is created, and no element is populated, in this session.** The four-element shape is the circuit's specification, not a result.

---

# 2. Scope & Disambiguation

All of the following disciplines bind the investigation and are recorded now:

- **EXTERNAL SYSTEMS ONLY.** Relatio is **not a subject** of this investigation. **No claim, and no element of a claim, is about Relatio. Comparisons to Relatio do not appear in §1–§8.**
- **DESIGN INTENT IS NOT EVIDENCE.** What a system's designers say it achieves is **element (ii)**, **never element (iii)**. A well-argued design rationale does **not** populate the evidence element.
- **MATURITY IS NOT EFFICACY.** Wide adoption, institutional backing, and long life are **not** evidence that an approach works. **A dominant system with an empty (iii) is recorded as exactly that.**
- **ABSENCE IS A FINDING.** "No system in this base addresses this," "no empirical evidence exists," and "the sources do not say" are **legitimate, recordable, and expected** outcomes. **They are not filled.**
- **DOMAIN TRANSFER IS NOT ASSUMED.** Medicine, law, intelligence, and scholarly publishing differ in stakes, incentives, and institutional enforcement. **A solution's portability across domains is NOT inferred from its success in one**, and **any portability observation is disclosed as an inference.**
- **TERMINOLOGICAL DRIFT (STD-0007).** These fields use "claim," "evidence," "warrant," "assertion," "argument," and "annotation" in **overlapping but NON-IDENTICAL** senses. **Where a source's usage differs from Relatio's, say so**; do **not** silently translate a source's term into Relatio's vocabulary, and do **not** treat a shared word as a shared concept.
- **ADOPTION AND PERSISTENCE ARE OUT OF SCOPE AS CLAIMS, AND ARE ROUTED.** This base carries a field-level observation that is **not about any one design problem**: that structured-knowledge systems have repeatedly failed to displace document-based practice, and that several named systems were built, adopted, and then abandoned. **That question — why these systems do or do not persist, who bears the maintenance burden, and what happens when the originator stops — is a DIFFERENT INVESTIGATION** with different evidence and different methods. **It is not a fifth claim here and is not folded into A–D.** Where such an observation arises, it is **recorded in the reserved reflexive section and ROUTED to the Governance Backlog as the warrant for a successor investigation** — not developed, not graded, and not allowed to reshape claims A–D.
- **BASE LIMITS.** **Nine sources do not represent four fields.** The base's coverage limits are **recorded as limits** (§8), not silently absorbed.

## 2.1 Scale posture

Native **`Level N (Label)`** only in every frontmatter and grading field (KOS-0003 §8). The optional H-band typology may appear in **prose only** and carries no grading authority. **No ★-glyphs anywhere in any Knowledge Object.**

## 2.2 Reliance posture

**Everything lands R0.** The base is largely open-access and its interiors can be read (§3), which **raises the achievable grade ceiling** for the elements that reading supports — but **verification strength is recorded per source, not averaged**, and **findings are NOT cleared for external reliance regardless of closure** (§7.5-analog, declared here at opening). The **reserved reflexive section is additionally §7.6-reflexively-gated.**

---

# 3. Method / Protocol

Execution follows the KOS-0003 pipeline (Question → Claims → Assumptions → Evidence → Confidence) through the **full OPS-0003 circuit** (Research Specialist → Critical Reviewer → Knowledge Architect; Vision Steward/owner closes). Claims are authored via **TPL-0001** (born epistemic-, review-, and attribution-conformant); the synthesis via **TPL-0004**. **Sources are cited from the fixed base SRC-0152…SRC-0160** (§8); **no source is created and no SRC identifier consumed** — the base is not extended by this investigation (§2, base limits). All identifiers are registered in the Identifier Registry at execution.

## 3.1 Interior-reading posture

Unlike prior investigations, **most of this base is open-access and its interiors CAN be read.** **Interiors MAY therefore be read where accessible**, and **reading raises the achievable grade ceiling** for the claim elements it supports. **Where an interior is inaccessible, that is DISCLOSED per source**, and the affected component **grades down for the limit.** **Per-source verification strength is recorded, not averaged across the base.**

## 3.2 Operative disciplines (bind at circuit)

> **NO PAGE-LEVEL CLAIM FROM AN UNREAD INTERIOR.** A source whose interior was not read supports **only** what its abstract, metadata, or the citing literature **actually establishes**, and the record **says which.**

> **DESIGN RATIONALE MAY NEVER SATISFY ELEMENT (iii).** If the only support for "it works" is that its designers **designed** it to, **element (iii) is empty and is recorded as empty.**

> **ELEMENT (iv) RECORDS DOCUMENTED COSTS AND FAILURE MODES — what the sources say, not what the analyst infers.** A weakness the analyst can see but **no source discusses is NOT a claim element**: it is an **observation, recorded in the reserved reflexive section and routed.** **Element (iv) is not a speculation slot**, and a grade there must be **warrantable against a source** like any other.

> **DISAGREEMENT IS RECORDED AS DISAGREEMENT, at the grade each side earns.** Where two sources in the base disagree, the disagreement is recorded **as** a disagreement. **The circuit does not adjudicate between external systems, and does not rank them.**

## 3.3 The two support-surface observations — derived, never transcribed

The two characterizations named in the opening banner **(a)** (Cochrane PLS adherence to PLEACS) and **(b)** (legal-citator accuracy and inter-tool agreement) are **hypotheses to test, not facts to record.** At circuit they are **either derived independently from SRC-0159 and SRC-0160 directly — reporting what those sources actually say, with any discrepancy against the support-surface characterization reported — or not used.** **Neither figure nor characterization is transcribed from the brief or this scaffold into any record.** A value that inherits confidence from a source is derived at execution.

---

# 4. Findings / Synthesis

**FILLED at circuit (brief 3 of 3, 2026-07-24).** The four mandated claims and the synthesis exist:

- **CLM-0099 — Claim Atomicity (CLM A; warrant GB-2026-045).** Three individuation approaches — formalized assertion (nanopublication), argumentative role (micropublication's single principal Statement), author judgment under no stated rule (discourse graphs) — with IBIS at surface level; no surveyed system states an operational split procedure or enforces one by tooling. Elements (i)–(iv): Moderate / Moderate / Moderate / Moderate; (iii) explicitly empty for three systems, qualitative-only for the fourth.
- **CLM-0100 — Expert-to-Lay Register (CLM B; warrant GB-2026-044).** The one surveyed practice: medicine's mandated parallel plain-language summary under PLEACS with GRADE as the expert-side certainty vocabulary; the one measurement (SRC-0159, derived at execution): 1738 summaries, zero full adherence, 57% overall, 0.7% on the certainty item. **Single-domain basis stated in the claim itself.** Elements: High / High / Moderate / Moderate.
- **CLM-0101 — Recoverable Source-to-Claim Mapping (CLM C; warrant GB-2026-046).** A capture-depth spectrum from whole-work typed citation (CiTO) to full support-graph resolution (micropublications); the one measured practice (SRC-0160, derived at execution): three citators, 11% three-way substantive agreement, 33%/38%/72% failure on 309 clearly negative treatments, results rendered as fact with no ambiguity marking. Elements: Moderate / Moderate / Moderate / Moderate.
- **CLM-0102 — Warranted Typed Relationships (CLM D; warrant GB-2026-043).** Vocabularies from 3 relations to ~98 classes; **typing is assertion in every surveyed system — none requires or tool-checks a warrant**; the only enforcement instance (editorial) is the measured one above; the one deployment report shows the typed-relation layer under-authored in practice. Elements: Moderate / Moderate / Moderate / Moderate.
- **FND-0019 — the synthesis:** approaches articulate, rationales explicit, **measured evidence confined to exactly two studies**, both finding deployed practice far short of design; element (iii) explicitly empty everywhere else; recurrent documented pressure points (formalization burden, unenforced standards, unauthored relation layers, editorial subjectivity rendered as fact). Six components, no Level 5 and no Level 4, weakest Low (the disclosed unread-interior cost).

Full content, per-element sourcing, and the two support-surface-hypothesis dispositions (both derived from SRC-0159/SRC-0160 directly, both matching the sources in shape, scope conditions carried) are in the claim records; the coverage limits are in FND-0019 §4.

---

# 5. Confidence Summary (KOS-0003 §8)

**FILLED at circuit.** Native `Level N (Label)`, per component, never averaged. Sixteen claim components (four separable elements × four claims) plus six finding components:

| Record | (i) approach | (ii) stated rationale | (iii) evidence of performance | (iv) documented costs |
|---|---|---|---|---|
| **CLM-0099** (A — atomicity) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) |
| **CLM-0100** (B — register) | 4 (High) | 4 (High) | 3 (Moderate) | 3 (Moderate) |
| **CLM-0101** (C — mapping) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) |
| **CLM-0102** (D — typed relationships) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) | 3 (Moderate) |

- **FND-0019:** atomicity_picture 3 (Moderate) · register_picture 3 (Moderate) · mapping_picture 3 (Moderate) · typed_relationships_picture 3 (Moderate) · measured_evidence_confined_to_two_studies 3 (Moderate) · **unread_interior_coverage 2 (Low)**.
- **The only two High components are CLM-0100's descriptive elements (i)/(ii)**, earned on full interior reading of all three of that claim's sources including the standard itself in the exact edition its adherence study cites. **No Level 5 anywhere; the finding carries no Level 4** (capped at its weakest necessary components). The one Low is deliberate: what the survey can say about the two unread-interior sources (SRC-0152, SRC-0154).
- **Everything R0** — not cleared for external reliance regardless of closure; the reflexive section is additionally §7.6-gated.

---

# 6. Assumptions & Bracketing (KOS-0003 §10)

*Expanded at circuit execution (2026-07-24). The standing brackets and disciplines below bound throughout; the circuit actuals follow the list.*

- **External systems only (§2).** No claim or element is about Relatio; no Relatio comparison appears in §1–§8.
- **Design intent ≠ evidence; maturity ≠ efficacy (§2).** Element (ii) never populates element (iii); a dominant system with an empty (iii) is recorded as such.
- **Absence is a finding (§2).** Empty (iii)/(iv) are explicit, expected outcomes, never filled to look complete.
- **Domain transfer is not assumed (§2).** Portability is disclosed as an inference, never inferred from success in one domain.
- **Terminological drift (§2, STD-0007).** A shared word is not a shared concept; source usage is not silently translated into Relatio's vocabulary.
- **Element (iv) is documented, not inferred (§3.2).** An undocumented weakness is an observation to route, not a claim element.
- **The base is fixed at nine and does not represent the field (§2, §8).** Under-coverage is disclosed, never compensated for by reaching outside the base; gIBIS stays cut.
- **Adoption/persistence is out of scope as a claim (§2).** It is routed to the reserved reflexive section and the Governance Backlog as a successor-investigation warrant, not developed here.
- **Everything R0; reflexive output additionally §7.6-gated (§2.2).** No finding is cleared for external reliance regardless of closure; no reflexive observation is self-applied.

**Circuit actuals (2026-07-24):**
- **Interior-reading actuals (§3.1):** seven of nine interiors READ this session — SRC-0156, SRC-0157, SRC-0158 (via the Wayback Machine capture of the exact URL SRC-0159 cites; live URL dead), SRC-0159, SRC-0160 read directly; SRC-0153 and SRC-0155 read via structured extraction with every load-bearing quotation grep-verified verbatim against the retrieved full texts. **Two NOT read, disclosed and confined:** SRC-0152 (the eScholarship copy is a page-image scan with no text layer; no OCR tooling available) and SRC-0154 (publisher access blocked by an anti-bot challenge; Wayback and repository/aggregator routes checked and empty). Per-source verification strength is recorded in each claim's Verification section, not averaged.
- **The two support-surface observations (§3.3):** both were DERIVED from their sources directly at execution. Hypothesis (a) matched SRC-0159's own reported result (zero full adherence; 57%; certainty item 0.7%); hypothesis (b) matched SRC-0160's (substantial missed negative treatment; 11% three-way type agreement). No discrepancy of shape; scope conditions carried with every figure; neither characterization was transcribed from the brief or scaffold.
- **A cross-source divergence found and recorded, not adjudicated (CLM-0100):** SRC-0159 describes PLEACS as containing 14 items (12 mandatory); the archived v3.0 standard itself contains 12 items (10 mandatory, 2 highly desirable). Recorded as a divergence between sources.
- **Adoption/persistence observations surfaced by the sources** (named prior systems no longer active; maintenance-role and originator-scaffolding documentation; a build-adopt-abandon arc inside the base) are recorded in the Reserved Reflexive Section and appended to GB-2026-048 — **not** developed into any claim element.

---

# Reserved Reflexive Section (FILLED at circuit, 2026-07-24 — ROUTED, NOT APPLIED)

**Governing rule (from scaffold, in force):**

> **Observations about what these external systems imply for Relatio's own architecture are RECOMMENDATIONS.** They are **routed to the Governance Backlog per ADR-GOV-0007 §3**, are **§7.6-reflexively-gated**, and are **NEVER self-applied in session.** **No refinement to Relatio follows from this investigation except through separately recorded governance after closure.**

**Independence disclosure (ADR-GOV-0011, binding):** this circuit is Claude-family throughout — it supplies **no independence of kind** for any §7.6 purpose, and nothing below may count toward promoting any anchor or practice from provisional toward durable.

**Nothing below is enacted.** No standard, template, tool, field, or vocabulary was created or amended on account of anything in this section; no existing record was revised; **GB-2026-047 is untouched (owner-reserved).**

## Routed to GB-2026-044 (register legibility)

What the survey found that bears on the recorded question, offered as input only:
1. **The only surveyed mechanism serving expert and lay readers from one record is a SECOND, MANDATED REGISTER** — a parallel plain-language summary — governed by an itemized standard naming what MUST appear (CLM-0100 (i)). No surveyed system makes the expert record itself legible to outsiders; the documented pattern is a second artifact with its own governance.
2. **The surveyed standard operationalizes legibility as an item list** (title, wording, headings, word band, named jargon to avoid, standardized uncertainty wording, certainty translation) rather than as a principle.
3. **The item that fails without enforcement is the epistemic one:** measured adherence collapsed precisely on certainty communication (0.7%), and the standard's nominal publication gate went unenforced (zero of 1738 fully adherent). A register standard without an enforcement mechanism decayed in the one place it was measured.
4. **Single-domain caution:** all of this is medicine; portability to Relatio's context is an inference the owner would be making, not a surveyed result.

## Routed to GB-2026-045 (atomicity under-firing)

1. **No surveyed system states an operational split rule, and none enforces atomicity by tooling** (CLM-0099 (i)). Where the split line is defined at all it is structural (one formalized assertion; one principal claim per argument); where it is undefined, the one field deployment observed **non-atomic authoring** — the same shape as the under-firing GB-2026-045 records.
2. **The surveyed experience suggests atomicity does not self-enforce:** the discipline fired in systems that made the unit structural, and under-fired where individuation was left to author judgment. If the owner wants Relatio's splitting discipline to fire reliably, the surveyed material points toward an operational rule and/or a review-checked separability test rather than a stated principle — offered as input, not as a proposal.
3. One deployed community, allowed to extend its grammar, **invented a finer granularity distinction itself** (higher-level conclusions vs "more atomic" propositions) — evidence that the need for a split-line vocabulary recurs in practice.

## Routed to GB-2026-046 (application transparency)

1. **The most complete documented design for a recoverable source-to-claim path is micropublications'** (support graph; asserts/quotes responsibility localization; claim lineages resolvable past the whole work to the statement, data, and method) — a design, with no performance evidence (CLM-0101).
2. **Capture-at-writing versus reconstruction-later:** SRC-0155 documents that backing "was readily available" at extraction time and is "laborious" to reconstruct afterwards. Bearing on GB-2026-046's open question (uncaptured vs unrendered): the surveyed literature's documented failure is *uncaptured-at-source*, and its documented remedy is capturing the mapping when the mapping is made.
3. **Rendered mappings that carry no uncertainty marking are the documented anti-pattern:** the citators render every editorial judgment as fact, and the one measurement shows what that conceals (11% three-way agreement). If Relatio ever renders its source→claim mappings, the surveyed failure mode argues for uncertainty marking on the rendering — consonant with, not additional to, the view generators' existing confidence/reliance badges; offered as input only.
4. **Designed capture is not practiced capture:** discourse graphs' evidence nodes were observed as empty placeholders often enough for the designers to name it a limitation. A capture field existing does not mean it is populated; only review catches that.

## Routed to GB-2026-043 (warrant asymmetry residue — bearing on enactment observation 2)

1. **Unwarranted typing is the surveyed field's norm:** every surveyed system types relationships by bare assertion (author, annotator, or editor); **no surveyed counterpart exists to a tool-checked warrant** of the kind `influenced_by` carries (CLM-0102 (i)). Relatio's structured-warrant design is beyond surveyed practice, not behind it.
2. **The one measured unwarranted practice was substantially inconsistent** (cross-product type agreement 11%; 11–15% incorrect applied labels) — but **no source tests whether warrant requirements improve consistency**, so the counterfactual GB-2026-043's observation 2 turns on (would `branches_from` benefit from a structured `warrant` pointer?) is **unmeasured in this base**. The survey supplies context for the owner's decision, not a verdict.
3. **Vocabulary-size trade documented once:** the short-label product missed what it had no word for; the long-label products disagreed on which word applied. Bearing (input only) on any future extension of Relatio's qualifier or relationship vocabularies: both directions of the size trade have documented costs in the one measured practice.

## APPENDED to GB-2026-048 (adoption/persistence — successor-investigation warrant; recorded, not developed, not graded)

1. **SRC-0153 documents by name that three prior discourse-graph infrastructures are "no longer active"** — ScholOnto; SWAN (in Alzforum); micropublications (in Domeo) — attributing this partly to "changes in funding and infrastructure … leading to deprecation of technical infrastructure," and states that "the impact of these deployments has not been empirically evaluated."
2. **A build-adopt-abandon arc exists inside the base itself:** SRC-0155's Domeo implementation (reported in 2014 as deployed, open-source, with industrial users) is among the systems SRC-0153 lists as no longer active in 2024.
3. **Maintenance burden is documented as a paid role** (a lab "cybrarian" hired to structure and enforce conventions) and **originator dependence as standing scaffolding** (designer-led office hours; the first author personally assisting users; one team's documented departure over substrate frictions).
4. **SRC-0156 records CiTO at publication as "not yet widely used elsewhere,"** with early version churn (renamed/deprecated classes across v1.3→v1.6).
5. **SRC-0159 documents that a mandated organizational standard decayed in practice without enforcement** — an institutional-persistence observation as much as a register one.

These are appended to the existing GB-2026-048 as recorded observations strengthening the successor-investigation warrant. **They are not a fifth claim, they reshape nothing in claims A–D, and no remedy is proposed** (the GB-2026-048 no-remedy note binds).

## Analyst observations that failed the element-(iv) documentation bar (§3.2 — observations only, routed)

1. **No surveyed source documents any review or re-verification cadence** for previously captured claims or relations — how a captured graph ages is unaddressed across the base. (Possibly a base-coverage artifact; recorded as an observation, not an absence claim.)
2. **The instrument-description drift found between SRC-0159 and the archived PLEACS** (14 vs 12 items — recorded as a source divergence in CLM-0100) is, reflexively, an instance of exactly the checkability problem a knowledge system might make structural: the description of a standard drifted from the standard, and nothing in the surveyed practice would have caught it.
3. **Both empirical studies measure human editorial application, and both found practice diverging from design.** No source measures a tool-enforced discipline; Relatio's validator-enforced fields have no surveyed counterpart. Recorded as an observation about the base's coverage, with no inference drawn.

---

# 7. Acceptance Criteria for Closing

INV-0019 may close only when all ten of the following hold, each **independently checkable**:

1. **Four claims exist**, one per design problem, with elements **(i)/(ii)/(iii)/(iv) separable and separately graded**, and **(iii) not merged with (iv).**
2. **Every claim element cites the specific source(s) supporting it**; **no element rests on a source whose interior was unread unless what it rests on is establishable without the interior, and this is stated.**
3. **Elements (iii) and (iv) are each populated or EXPLICITLY EMPTY for every system discussed**; no empty element is left ambiguous or implied, and **no element (iv) entry rests on analyst inference rather than a source.**
4. **Per-source verification strength is disclosed**, including **which interiors were read and which were not.**
5. **The two support-surface observations were derived independently from SRC-0159 and SRC-0160 or not used**, with **any discrepancy reported.**
6. **No claim, and no element, is about Relatio.**
7. **Terminological differences** between the sources' vocabularies and Relatio's **are recorded where they arise.**
8. **Base coverage limits are recorded as limits.**
9. **A finding (FND) synthesizes the four claims at grades no stronger than their weakest necessary components, with no Level 5.**
10. **The reserved reflexive section is completed and ROUTED, not applied** — including any adoption/persistence observation, **routed as the warrant for a successor investigation** rather than developed here.

**Verification & reliance (§7.5 analog).** Interior-readable base (§3.1), so the achievable ceiling is higher than in verification-light investigations — **but findings are NOT cleared for external reliance regardless of closure**, and per-source verification strength is disclosed and not averaged. **Everything lands R0.** The reserved reflexive section's output is additionally **§7.6-reflexively-gated.**

---

# 8. Relationships (STD-0004)

- `part_of` the Knowledge Base — a **classification** statement, not a typed graph edge ("Knowledge Base" is not a resolvable object; no `part_of` target is declared in frontmatter, matching INV-0009…INV-0018).
- **Frontmatter edges at opening: NONE.** Per **ADR-GOV-0004 D4**, frontmatter references are **graph claims** and may name only existing objects. **This scaffold may NOT reference CLM, FND, or ENT objects that do not yet exist** — none has been created. The catalogued sources attach to **child claims** created at circuit, not to INV-0019 itself; declaring any source, child, or inheritance edge now would assert a relationship the record does not yet have. The planned subgraph is declared in **prose** here and edged at execution (existing STD-0004 types only; none invented).

## 8.1 Expected source-to-problem bearing — PROSE, and EXPECTATION IS NOT FINDING

The nine catalogued sources are recorded below against the design problem each is **expected** to bear on, from what the **catalog already records** about each (title, domain). **This is expectation, not finding.** A source **may bear on problems other than those listed, or on none**; the circuit reads each source and records what it actually supports, at the grade it earns. **No characterization of any source's content beyond the catalog is made here.**

| Source (catalog) | Field | Expected primary bearing |
|---|---|---|
| **SRC-0152** — Kunz & Rittel 1970, *Issues as Elements of Information Systems* (IBIS) | argumentation modelling | **D** (issue/position/argument as typed relations); may bear on **A** |
| **SRC-0153** — Chan et al. 2024, *Steps Towards an Infrastructure for Scholarly Synthesis* (discourse graphs) | scholarly synthesis / semantic publishing | **A**, **C**, **D** |
| **SRC-0154** — Groth, Gibson & Velterop 2010, *The Anatomy of a Nanopublication* | semantic publishing | **A** (atomic assertion), **C** (provenance) |
| **SRC-0155** — Clark, Ciccarese & Goble 2014, *Micropublications* | semantic publishing | **A**, **C** (evidence/argument chain), **D** |
| **SRC-0156** — Shotton 2010, *CiTO, the Citation Typing Ontology* | semantic publishing / citation typing | **D** (citation typing), **C** |
| **SRC-0157** — Guyatt et al. 2008, *GRADE: an emerging consensus* | evidence synthesis | **B** (certainty communication); context for (iii)/(iv) on evidence-certainty |
| **SRC-0158** — Cochrane 2013, *PLEACS: Standards for Plain Language Summaries* | evidence synthesis (plain language) | **B** (lay-register standard) |
| **SRC-0159** — Jelicic Kadic et al. 2016, *Cochrane Plain Language Summaries Heterogeneous* | evidence synthesis (register performance) | **B**; the source from which support-surface observation **(a)** is **derived**, never transcribed (§3.3) |
| **SRC-0160** — Hellyer 2018, *Evaluating Shepard's, KeyCite and BCite* | professional citation practice | **C** (recoverable source-to-treatment mapping), **D** (typed treatment/warrant); the source from which support-surface observation **(b)** is **derived**, never transcribed (§3.3) |

- **The `contrasts_with` / `related_to` edges catalogued among these sources at PREP** (including the honest weak `related_to` between SRC-0159 and SRC-0158 whose precise "evaluates-adherence-of" relationship is routed as **GB-2026-047**) are **existing catalogued edges** and are **not modified by this scaffold.**
- **`branches_from` / `projects_to` / `influenced_by` (the timeline-program types) do not apply** — this investigation is knowledge-systems engineering, not the world-religions timeline program; **no ENT is created and no timeline edge is contemplated.**

## 8.2 Realized subgraph at circuit (2026-07-24)

The subgraph now exists, carried on the child records per the house pattern (this record itself declares no frontmatter edges; the children edge to it):

- **CLM-0099** `derived_from` SRC-0152, SRC-0153, SRC-0154, SRC-0155 · `supports` FND-0019 · `part_of` INV-0019.
- **CLM-0100** `derived_from` SRC-0157, SRC-0158, SRC-0159 · `supports` FND-0019 · `part_of` INV-0019.
- **CLM-0101** `derived_from` SRC-0153, SRC-0154, SRC-0155, SRC-0156, SRC-0160 · `supports` FND-0019 · `part_of` INV-0019.
- **CLM-0102** `derived_from` SRC-0152, SRC-0153, SRC-0155, SRC-0156, SRC-0160 · `supports` FND-0019 · `part_of` INV-0019.
- **FND-0019** `derived_from` CLM-0099…CLM-0102 · `part_of` INV-0019.

**Actual bearing versus the §8.1 expectation table:** the expectations held, with these recorded refinements — SRC-0152 bore on **A and D at surface level only** (interior unreadable); SRC-0154 bore on **A and C at surface level only** (interior blocked), with its model's characterization carried substantially by SRC-0155's read interior; SRC-0153 bore on **A, C, and D** as expected; SRC-0155 additionally bore on **D** (its predicate vocabulary and warrant posture), as the table anticipated; SRC-0156 bore on **D and C** as expected; SRC-0157/0158/0159 bore on **B** as expected; SRC-0160 bore on **C and D** as expected. No source bore on nothing; no source was cited outside its claims. **Identifiers consumed at circuit: CLM-0099, CLM-0100, CLM-0101, CLM-0102, FND-0019. No ENT consumed; SRC-0161 unconsumed; no new relationship type minted; the catalogued source-base edges unmodified.**

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.2|2026-07-24|Draft|**Specialist pass (ROLE-0002) executed under the circuit brief (3 of 3) with the RQ FROZEN BY THE OWNER as authored.** Created CLM-0099 (atomicity), CLM-0100 (register), CLM-0101 (mapping), CLM-0102 (typed relationships) — each with the four separable elements (i)–(iv) as discrete headed sections, separately graded, (iii) and (iv) never merged — and FND-0019 (six components, no Level 5, no Level 4, weakest Low). §4/§5 filled with actuals; §6 gains circuit actuals (interior-reading: seven of nine READ — SRC-0156/0157/0158/0159/0160 directly, SRC-0153/0155 via grep-verified structured extraction; SRC-0152 scan-unreadable and SRC-0154 access-blocked, both disclosed); both support-surface hypotheses DERIVED from SRC-0159/SRC-0160 directly, matching the sources in shape, scope conditions carried; the SRC-0159-vs-archived-PLEACS item-count divergence recorded, not adjudicated. Reserved Reflexive Section FILLED and ROUTED (GB-2026-044/045/046/043 inputs; adoption/persistence observations APPENDED to GB-2026-048; three analyst observations failing the (iv) bar routed) — nothing enacted, GB-2026-047 untouched. §8.2 records the realized subgraph and actual-vs-expected bearing. Identifiers consumed: CLM-0099…0102, FND-0019 only; no ENT; SRC-0161 unconsumed. Everything R0. Pending Critical Review (ROLE-0004) and structural validation (ROLE-0001).|
|0.1|2026-07-24|Draft|**Opened as a scaffold (UNFILLED), per STD-0006 §7.6 independence — the opening session creates no claim, entity, edge, or finding.** Authored from **TPL-0003**. Records the §1 primary RQ **verbatim, authoritative pending owner freeze** (freeze happens at the owner's review of this scaffold report, not here); the §1.1 **four-claim decomposition mandate** with the four separable elements **(i) approach / (ii) stated rationale / (iii) evidence of performance / (iv) documented costs and failure modes** and the **(iii)-vs-(iv) separability test**; the §2 **scope disciplines**; the §3 **method** with its operative blockquote rules and the interior-reading posture; §4/§5 **reserved for the circuit**; §6 **standing brackets**; the **Reserved Reflexive Section** named, empty, with its governing rule (ADR-GOV-0007 §3, §7.6-gated); the **ten §7 acceptance criteria**; and §8 **prose relationships** (no frontmatter edges to non-existent objects, ADR-GOV-0004 D4). Source base **fixed at nine (SRC-0152…SRC-0160)**; gIBIS stays cut; no SRC/CLM/ENT/FND identifier consumed. Template-section mapping (TPL-0003 → this record): §1 RQ → §1; §2 Scope → §2; §3 Method → §3; §4 Findings → §4 (reserved); §5 Confidence → §5 (reserved); §6 Assumptions → §6; template §7 Relationships → **§8** here; template §8 Revision History → **§9** here; the record additionally carries a **§7 Acceptance Criteria** section and a **Reserved Reflexive Section** (house pattern per INV-0016/0017/0018, which the brief's numbering matches).|

# End INV-0019
