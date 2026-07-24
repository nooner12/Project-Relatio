---
title: Critical Review - RQ-0019
document_type: Review Record
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-24
category:
  - Knowledge Base
  - Review
  - Knowledge Systems
parent_documents:
  - STD-0006 Review & Validation Standard
  - INV-0019 Structured-Knowledge Systems Comparative Survey
related_documents:
  - CLM-0099 Claim Atomicity in External Systems
  - CLM-0100 Expert-to-Lay Register in External Systems
  - CLM-0101 Source-to-Claim Mapping in External Systems
  - CLM-0102 Warranted Typed Relationships in External Systems
  - FND-0019 Structured-Knowledge Systems Survey Synthesis
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Review
  - CriticalReview
  - KnowledgeSystems
---

# Critical Review — RQ-0019

# Independent Adversarial Review of the INV-0019 Circuit (ROLE-0004)

## Adopted Review Record

> Performed by the Critical Reviewer (ROLE-0004) on the Specialist pass, 2026-07-24. **Independence is procedural only** — reviewer and Specialist are the same underlying model (STD-0006 §7.5 / ROLE-0004 §5; ADR-GOV-0011 binds independence at **family** level, so a Claude-family review of Claude-family work is **not** independence of kind). This review issues a verdict and gates conditional closure; it **does not and cannot clear any finding for external reliance** — everything stays R0. The Reserved Reflexive Section's output is additionally **§7.6-reflexively-gated**.
>
> **Calibration authority (owner condition, this circuit):** LOWERING a confidence level is permitted with justification; **RAISING requires explicit reviewer justification.** **Outcome: no level was raised and none was lowered.** Every grade is confirmed as the Specialist set it; the confirmations that required real adjudication are recorded in §4.

---

# 1. Verdict: **CONFORMANT WITH FLAGS**

**Two determinate flags, both remediated in-session** (§3). **Three advisory findings, non-blocking, recorded** (§3). **No confidence level raised; none lowered.** The circuit's central discipline — four separable, separately graded elements per claim, with measured evidence and documented failure modes never merged and emptiness always explicit — is verified as executed, not merely asserted. The review's method: every load-bearing figure in elements (iii) was re-checked against the retrieved source texts; every (iv) entry was traced to a source passage; every explicit-emptiness statement was checked against the reading record.

---

# 2. The eleven checks (brief Task 2 (a)–(k)), each addressed

**(a) SEPARABILITY of (i)/(ii)/(iii)/(iv); (iii) never merged with (iv).** **VERIFIED on all four claims.** Each claim carries the four elements as discrete headed sections with per-element grades. The one place a measurement figure recurs inside an element (iv) — CLM-0100's enforcement-gap entry restates the zero-of-1738 and 57% results — was inspected against the scaffold's separability test and passes it: the (iv) entry's content is the **documented causes** (review groups bypassing recommended editorial processes; groups using their own formats), with the figures present as the evidence that the gate went unenforced. A measurement result and a documented failure mode remain different objects in the record. Recorded as advisory A1, no change required.

**(b) NO DESIGN-INTENT LEAKAGE into (iii).** **VERIFIED, element by element.** Every (iii) entry was checked for whether its support is a measurement or a designer's assertion: CLM-0100's (iii) carries only SRC-0159's audit (GRADE's adoption reports are confined to (ii) under maturity≠efficacy); CLM-0101's and CLM-0102's (iii) carry only SRC-0160's figures (vendor reliability marketing is quoted in (ii) and pointedly so); CLM-0099's (iii) is empty statements plus SRC-0153's deployment observations, which are explicitly labelled qualitative field observation and not measurement — deployment experience by the designers is the closest thing to leakage risk in the circuit, and the record's handling (observation, not evidence of performing-as-designed) is correct.

**(c) EVERY (iv) ENTRY SOURCE-BACKED.** **VERIFIED with two exceptions, both remediated (determinate flags F1, F2, §3).** All other (iv) entries trace to source passages: SRC-0155's statement-based-model critique (verbatim-verified), SRC-0153's non-atomic authoring and relation-authoring friction (verbatim-verified), SRC-0159's causes discussion, SRC-0160's subjectivity/label-list documentation, SRC-0157's self-documented categorisation arbitrariness. **No (iv) entry had to be removed to the reflexive section** — the Specialist had already routed the three analyst observations that fail the documentation bar (review-cadence absence; instrument-description drift as a reflexive observation; the human-vs-tool-enforcement observation), and the reviewer confirms none of them appears as a claim element.

**(d) NO OVER-EXTENSION of SRC-0159 / SRC-0160.** **VERIFIED at every citation site.** SRC-0159 is cited in CLM-0100 (iii)/(iv) and FND-0019 — every use is scoped to Cochrane intervention-review PLSs, 2013–2015, measurable mandatory items, one organization, one domain; the claim statement itself opens with the single-domain limit. SRC-0160 is cited in CLM-0101 (iii)/(iv), CLM-0102 (iii)/(iv), and FND-0019 — every use is scoped to the three named products on the one sample, with the study's own disclaimer ("not an assessment of any citator's overall merit") carried in-record. CLM-0102's use for "the only enforcement instance … measured once" was checked hardest: it is within scope, because the claim asserts it of this base, not of editorial enforcement as a class. FND-0019 states both studies "bind only their subjects." **No over-extension found.**

**(e) EXPLICIT EMPTINESS.** **VERIFIED per system per claim.** Every system discussed has (iii) and (iv) populated or explicitly empty: CLM-0099 — nanopublication (iii) empty / (iv) populated-by-rival-documentation, micropublication (iii) empty by its authors' own deferral / (iv) populated, discourse graphs (iii) qualitative-only / (iv) populated, IBIS (iii) and (iv) both explicitly empty; CLM-0100 — PLS/PLEACS populated/populated, GRADE (iii) explicitly empty / (iv) populated, lay comprehension explicitly named unmeasured; CLM-0101 — citators populated/populated, micropublications, nanopublications, CiTO (iii) explicitly empty, nanopublications (iv) explicitly empty; CLM-0102 — citators populated/populated, CiTO/micropublications/IBIS (iii) explicitly empty, IBIS (iv) explicitly empty. **No ambiguous silence found.**

**(f) EXTERNAL-SYSTEMS-ONLY.** **VERIFIED.** No claim, no element, and no part of FND-0019 is about Relatio, and no comparison to Relatio appears in INV-0019 §1–§8. The Relatio mentions that do occur inside claim records are exactly the two kinds the scaffold mandates: terminological-drift notes stating that source terms are **not** translated into Relatio's vocabulary (§2 STD-0007 discipline requires saying so), and the R0 reliance boilerplate. Neither does comparative or evaluative work. All "what this implies for Relatio" content sits in the Reserved Reflexive Section, routed.

**(g) DOMAIN TRANSFER.** **VERIFIED.** CLM-0100's single-domain basis is stated in its claim statement, its assumptions, its history row, and FND-0019's limitations; no medical practice is presented as general anywhere; the one portability remark (reflexive routing to GB-2026-044, item 4) is explicitly disclosed as an inference the owner would be making.

**(h) TERMINOLOGICAL DRIFT.** **VERIFIED.** Each claim carries a drift note recording source-specific senses where they arose ("claim"/"statement"/"assertion" across the three model papers; "citation" as performative act; "supports" as deliberately broad transitive relation; Toulmin's "warrant"/"backing"; GRADE's "quality of evidence" vs the shared surface labels; "mandatory" as unenforced gate; the legal domain's internally contested "negative treatment"/"distinguished"). FND-0019 §4 directs any reader to the drift notes before citing. No silent translation found.

**(i) NO RANKING, ADJUDICATION, OR ADVOCACY.** **VERIFIED.** The nanopublication–micropublication design dispute is carried as a documented tension with the critique attributed to its interested source; the citators' mutual disagreement is reported as the finding it is; the SRC-0159-vs-archived-PLEACS item-count divergence is recorded unadjudicated; CLM-0102 refuses **both** directions of the warrant counterfactual as unmeasured. Two phrasings were pressure-tested: CLM-0101's "deepest documented design" (a capture-depth description, with merit-ordering explicitly disclaimed in the record — advisory A2) and FND-0019's "approaches articulate" (descriptive of documentation completeness). Neither ranks.

**(j) SOURCE DISCIPLINE.** **VERIFIED.** No page-level claim from an unread interior: SRC-0152 is cited only for the issue/position/argument element model recorded at cataloguing; SRC-0154 only for the assertion+provenance surface description and through SRC-0155's read interior, each use so labelled. No fabrication found: every figure in every (iii) was re-derived from the retrieved texts during this review (SRC-0159: 1738 / zero full / 57% / 0.7% / 99% / 98% / 319 mean / 76% under-length / 43–81% / r=0.235; SRC-0160: 357 / 53 / 40 / 11% / 309 / 103=33% / 116=38% / 222=72% / 78-7, 99-6, 178-33 / 12%-11%-15% / 3-2-1 of 4 / 470 — all confirmed). Verification strength is disclosed per source in every claim and never averaged; the two unread interiors are disclosed in every record that cites them.

**(k) REFLEXIVE ROUTED, NOT APPLIED; GB-2026-047 UNTOUCHED.** **VERIFIED.** The Reserved Reflexive Section routes to GB-2026-044/045/046/043 and appends to GB-2026-048; it enacts nothing — no standard, template, tool, field, or vocabulary was created or amended, and no existing record was revised on account of any reflexive item. GB-2026-047 is untouched and named as owner-reserved in the section itself and in CLM-0100. The adoption/persistence material appears only in the reflexive section and FND-0019's scope-limitation pointer — **no fifth claim exists**, and claims A–D are free of persistence content.

---

# 3. Flags

## Determinate (both remediated in-session)

- **F1 — CLM-0099 element (iv): SWAN curator "non-scalability" was asserted as documented when the source documents a contrast.** SRC-0155's text records that inconsistency-labelling "was the task of the knowledge base curator" in SWAN and that the micropublication model "does not require a central curator … which is a scalable model." The non-scalability of the curator design is the authors' implication by contrast, not a stated finding. **Remediation:** reworded to attribute the contrast to the authors rather than asserting a documented non-scalability finding. No grade affected.
- **F2 — CLM-0101 element (iv): CiTO's "fussy" acknowledgment was presented without the source's immediate defense.** SRC-0156 concedes the FRBR layering "might seem a little fussy" and then argues the granularity "is of enormous value" against ambiguity in flatter ontologies. Quoting the concession without the defense misrepresents the source's register — the passage is an acknowledged-and-defended design choice, not a confessed limit. **Remediation:** the defense added alongside the concession. No grade affected.

## Advisory (non-blocking, recorded)

- **A1 — CLM-0100 (iv) restates (iii) figures inside the enforcement-gap entry.** Passes the scaffold's separability test (measurement vs documented causes); no change required; noted so a future reviewer does not mistake recurrence for merging.
- **A2 — CLM-0101 (i) "deepest documented design."** Depth is a descriptive dimension and the record disclaims merit ordering explicitly; retained; noted because depth language sits close to ranking language.
- **A3 — SRC-0153's extracted text carries internal inconsistencies of its own** (57% vs 60% for the same feature statistic; 2.5 vs 3 years vs 30 months for deployment duration; one relation-list line inconsistent with the rest of the paper, likely a PDF-extraction artifact). The circuit used only cross-confirmed values (the relation triad confirmed at three separate passages; "~30 daily active users" as the paper's own synthesized estimate) and cited no figure the source states inconsistently. Recorded as a caution on the source, not a defect in the records.

---

# 4. Calibration adjudications (grades confirmed, with reasons)

- **CLM-0100 (i)/(ii) at Level 4 (High) — CONFIRMED, the circuit's only High grades.** Challenged on the 14-vs-12 item-count divergence: does an unresolved divergence about the standard's item count cap the descriptive element below High? **No** — the element describes the archived standard's contents from direct reading of the document itself in the exact edition the adherence study cites; the divergence concerns SRC-0159's *description* of that standard and is recorded, quarantined, and non-load-bearing for the description. High (not Very High) already prices the residue.
- **All sixteen claim elements at Moderate elsewhere — CONFIRMED.** Challenged in both directions. Downward pressure (should mixed-posture elements be Low?): no — where an unread interior is load-bearing the records disclose and confine it, and FND-0019 carries the unread-interior cost as an explicit Low component instead of hiding it inside claim grades. Upward pressure (should verbatim-verified (iv) elements be High?): no — the documented costs are the documentation of interested parties (a rival model's critique; designers' own deployment reflections), which is exactly what Moderate prices.
- **FND-0019's Low component (unread_interior_coverage) — CONFIRMED** as deliberately taken, matching the two-source access failure honestly.
- **No Level 5 anywhere; no Level 4 in the finding; split confidence everywhere a list; nothing averaged. CONFIRMED by inspection of every confidence block.**

---

# 5. Verification-strength disclosure (reviewer's own)

This review re-read the retrieved source texts for every figure it confirmed (SRC-0159, SRC-0160, SRC-0158, SRC-0157, SRC-0156 directly; SRC-0153 and SRC-0155 via the session's grep-verified extractions, with the reviewer re-running verbatim greps on every quote it relied on). It did **not** independently re-retrieve any source, and it inherits the Specialist's two access failures (SRC-0152, SRC-0154) — the reviewer confirms the failures are disclosed everywhere they bite, and could not itself do better this session. **Procedural independence only; same model family; nothing here counts toward independence of kind (ADR-GOV-0011).**

---

# 6. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-24|Adopted|Critical Review of the INV-0019 Specialist pass (ROLE-0004). **Verdict: Conformant with Flags** — two determinate flags (F1 SWAN-scalability attribution; F2 CiTO fussy-quote register), both remediated in-session; three advisory (A1 figure recurrence in CLM-0100 (iv), passes separability; A2 depth-language caution; A3 SRC-0153 internal inconsistencies, cross-confirmed values only used). All eleven brief checks (a)–(k) addressed individually: separability verified on all four claims including the (iii)/(iv) boundary; no design-intent leakage into any (iii); every (iv) entry source-traced (two rewordings; none removed — analyst observations were already correctly routed); no over-extension of SRC-0159/SRC-0160 at any citation site; explicit emptiness verified per system per claim; external-systems-only verified (Relatio mentions are mandated drift notes and reliance boilerplate only); single-domain basis of CLM B stated everywhere it matters; drift notes present; no ranking or adjudication; source discipline held (all (iii) figures re-derived; unread interiors confined); reflexive section routed not applied, GB-2026-047 untouched. **No confidence level raised; none lowered**; CLM-0100's two High grades and FND-0019's deliberate Low confirmed under challenge. Everything R0; procedural independence only.|

# End Critical Review — RQ-0019
