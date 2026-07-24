---
title: CLM-0100 - Expert-to-Lay Register in External Systems
document_type: Claim Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-24
category:
  - Knowledge Base
  - Claim
  - Knowledge Systems
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0019 Structured-Knowledge Systems Comparative Survey
related_documents:
  - SRC-0157 Guyatt et al 2008 GRADE Emerging Consensus
  - SRC-0158 Cochrane 2013 PLEACS Standards for Plain Language Summaries
  - SRC-0159 Jelicic Kadic et al 2016 Cochrane Plain Language Summaries Heterogeneous
  - FND-0019 Structured-Knowledge Systems Survey Synthesis
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - KnowledgeSystems
  - ExpertToLayRegister
relationships:
  - type: derived_from
    target: SRC-0157
  - type: derived_from
    target: SRC-0158
  - type: derived_from
    target: SRC-0159
  - type: supports
    target: FND-0019
  - type: part_of
    target: INV-0019
confidence:
  - component: b_approach_described
    level: 4
    label: High
  - component: b_stated_rationale_recorded
    level: 4
    label: High
  - component: b_evidence_of_performance
    level: 3
    label: Moderate
  - component: b_documented_costs_failure_modes
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "interior-read base (all three sources read this session); single domain (medicine); single adherence study; not cleared for external reliance"
review_cycle: 9
review_date: 2027-04-24
last_reviewed: 2026-07-24
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-24
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# CLM-0100

# Expert-to-Lay Register in External Systems (CLM B)

## Draft Claim Record

---

# Claim
> **In the one surveyed practice that addresses the expert-to-lay register problem — evidence synthesis in medicine, and only there in this base — the approach is a MANDATED PARALLEL SUMMARY governed by an organizational reporting standard: the expert record (a Cochrane systematic review, carrying GRADE certainty ratings) is accompanied by a stand-alone plain-language summary whose required content and form are prescribed item-by-item by PLEACS (2013), including a mandated translation of evidence certainty into the lay register. The single empirical study of this approach in the base (SRC-0159) measured adherence, not comprehension, and found it low and heterogeneous: of 1738 summaries, not one adhered fully to the measured items, overall adherence was 57%, and the certainty-communication item — the register's epistemic core — was met by 0.7% of summaries.** All three sources are from one domain (medicine, one organization); nothing in this claim is asserted for any other domain.

---

# Element (i) — Approach (descriptive)

**The surveyed approach serves expert and lay readers from a single record by attaching a second, parallel register to the expert document rather than by making one text serve both.** As documented in the sources read this session:

- **The Cochrane plain-language summary (PLS)** is a stand-alone summary of a systematic review, aimed at the general public, published alongside the review's scientific abstract (SRC-0159 Background; SRC-0158 PLS1). The expert record and the lay record are the same publication; the lay register is a mandated component of it, not a separate product.
- **PLEACS (SRC-0158, v3.0, 28 February 2013) prescribes the lay register item-by-item.** The archived standard read this session contains **twelve items, PLS1–PLS12: ten mandatory, two "highly desirable" (PLS9 study-funding sources; PLS11 use of statistics)**, where "Mandatory means that a new review should not be published if this is not reported" — on its face, an editorial publication gate. The items govern: plain-language title (PLS2); a 400–700-word stand-alone summary in language "understood by most readers without a university education," with named jargon terms to avoid (PLS1); standard headings in a prescribed interim set — review question, background, study characteristics, key results, quality of the evidence (PLS3); consistency of key messages with the review text and Summary of Findings tables (PLS4); the review question with population/intervention/comparison/outcomes (PLS5); background (PLS6); search date, without search-strategy detail (PLS7); study characteristics including counts of studies and participants (PLS8); key results for all main outcomes including harms, with a standardized uncertainty wording ("will, may, probably, little, uncertain") (PLS10); statistics, if given, as natural frequencies with absolute effects drawn from the review (PLS11); and **evidence quality for each main outcome based on the five GRADE considerations, with the GRADE levels named if used and key reasons given in lay terms (PLS12)**.
- **GRADE (SRC-0157) supplies the expert-side certainty vocabulary that PLS12 mandates be translated:** four quality-of-evidence levels (high / moderate / low / very low) with plain-language definitions of each; five explicit downgrade criteria (study limitations, inconsistency, indirectness, imprecision, reporting bias) and named upgrade criteria; and a deliberate separation of evidence quality from recommendation strength (strong / weak). The lay register's certainty item is thus anchored to a controlled expert vocabulary rather than left free-form.
- **Discrepancy between sources, recorded as such (not adjudicated):** SRC-0159 (Methods) describes PLEACS as containing "14 items, of which 12 are marked as 'mandatory' and two as 'highly desirable' (PLS9 and PLS11)." The archived v3.0 standard itself — retrieved this session from the exact URL SRC-0159's reference 2 cites — contains **twelve** items (PLS1–PLS12), of which **ten** are mandatory and two (PLS9, PLS11 — matching SRC-0159's identification) are highly desirable. SRC-0159's own extraction instrument separately collected "14 data items," which is a fact about its instrument, not about the standard. The divergence in the two sources' description of the standard's item count is recorded here as a divergence; neither source is corrected from the other.

**No other system in this base addresses the expert-to-lay register problem.** The argumentation-modelling and semantic-publishing sources (SRC-0152…0156) and the citator study (SRC-0160) document no lay-register mechanism; that absence is recorded in FND-0019, and this claim is about the one practice that does.

# Element (ii) — Stated Rationale (design-intent register ONLY)

What the systems' own documentation says the approach is for — recorded in that register and carrying no evidential weight for element (iii):

- **PLEACS** (SRC-0158 Preface and item rationales): the standards were established by a working group "comprised of consumers, methodologists and editors," refined through an open consultation in 2012; the PLS should "convey succinctly and clearly the key question and findings" as a stand-alone summary understandable without a university education; each standard is published with a stated reason.
- **SRC-0159's framing of the design intent** (Background): systematic reviews are long and technical; the PLS is the "main building block" for dissemination to end-users of health information, and — with thirteen Cochrane translation teams, most translating only the PLS — an internationally load-bearing knowledge-translation instrument, which is the stated reason standardization matters.
- **GRADE** (SRC-0157): the design intent is explicit, comprehensive, transparent, and pragmatic communication of evidence certainty and recommendation strength — "simplicity, transparency, and vividness" — motivated in the article by named historical failure cases (hormone-replacement therapy; encainide/flecainide; delayed thrombolytics) where inattention to evidence quality misled clinicians. Those cases motivate the design; they are not measurements of GRADE's own performance and populate nothing in element (iii).

# Element (iii) — Evidence of Performance (measured, including absence)

**Populated for the PLEACS/PLS approach — one adherence study, derived directly from SRC-0159's interior this session (§3.3 of INV-0019; the support-surface hypothesis was tested against the source, and the source governs):**

- **Sample and method:** all Cochrane PLSs published March 2013 – January 2015 (1799 found, 61 withdrawn, **1738 analyzed**, of which 176 were empty reviews); duplicate independent data extraction by six authors with discrepancies resolved by a seventh; adherence scored against the **measurable** mandatory PLEACS items only (0–19 points for reviews with studies; 0–13 for empty reviews) — PLS4 (consistency) was excluded as not measurable from the PLS alone. The study is an adherence audit; **it did not measure lay-reader comprehension or health-decision outcomes, and it explicitly did not evaluate the PLEACS standard itself** ("It is possible that these standards … are not ideal themselves and not evidence-based, but this is another topic").
- **Results, as the source reports them:** **not a single one of the 1738 PLSs adhered fully to the measured items.** Overall adherence for reviews with included studies was **57%** (mean score 11 of 19; range 4–18); for empty reviews **59%**. The distribution: 0.6% of PLSs at 0–25% adherence, 20% at 26–50%, 67% at 51–75%, 12.4% at 75–100%. **The lowest-adhered item was addressing evidence quality according to the GRADE system: 0.7%.** The highest were absence of search-strategy details (99%) and absence of unexplained complex statistics (98%). Word counts: mean 319, median 304, range 46–1125; **76% fell below the 400-word floor** and 0.5% exceeded 700. Adherence varied by Cochrane Review Group from **43% to 81%** across the 53 groups publishing in the window; the group devoted to consumers and communication scored 61%. Adherence rose weakly over time (Pearson r = 0.235; regression slope significantly non-zero, p < 0.001).
- **Support-surface hypothesis (a) disposition (INV-0019 §3.3):** the hypothesis — that PLS adherence to PLEACS is low with the evidence-certainty item especially poorly adhered to — **is what the source itself reports** ("highly heterogeneous with a low adherence to the PLEACS standards"; 0.7% on the GRADE item). No discrepancy between the hypothesis's shape and the source was found; the figures above are the source's, carried with their scope conditions (Cochrane intervention-review PLSs, March 2013 – January 2015, measurable mandatory items only, one organization, one domain).
- **EXPLICITLY EMPTY for GRADE:** this base contains **no measurement of GRADE's performance** as a certainty-communication vocabulary — SRC-0157 reports adoption (25+ organizations), and under the maturity-is-not-efficacy discipline adoption populates nothing here. **EXPLICITLY EMPTY for comprehension:** no source in this base measures whether lay readers understand or correctly use a PLS; the one measured quantity is adherence of the written summaries to the standard.

# Element (iv) — Documented Costs and Failure Modes (from the sources; not inferred)

- **Enforcement gap (documented by SRC-0159):** PLEACS's mandatory status is nominally publication-gating, yet zero of 1738 published summaries fully adhered — the standard was published, the summaries were published anyway, and adherence averaged 57%. SRC-0159 attributes the heterogeneity in part to Cochrane Review Groups that "do not necessarily use the recommended editorial processes," and reports that "certain Cochrane review groups consistently use their own format of preparing the PLS, which is different from PLEACS items."
- **The register's epistemic core is what fails hardest (documented by SRC-0159):** the item mandating certainty communication per GRADE — the element that makes the lay register epistemically honest rather than merely readable — is the least-adhered item measured (0.7%).
- **Under-length rather than over-length failure (documented by SRC-0159):** 76% of PLSs fell below the 400-word floor, with a 46-word, three-sentence summary cited as an extreme; the source states such brevity "may not necessarily allow proper explanation" of what the review did and what the results mean.
- **The standard itself may be part of the problem (documented as an open possibility by SRC-0159):** the study states it did not analyze PLEACS itself and that the standards may not be "ideal themselves and not evidence-based" — recorded there as a limitation, recorded here as a documented open question about the approach, not as a finding.
- **Categorisation arbitrariness (self-documented by SRC-0157 for GRADE):** "Quality of evidence is a continuum; any discrete categorisation involves some degree of arbitrariness" — GRADE's own statement of what the four-level vocabulary trades away; the article judges the trade worth making, and that judgment is design-intent, not measurement. SRC-0157 also documents the ecosystem cost that motivated GRADE: a "plethora of systems" that clinicians cannot realistically learn.
- **EXPLICITLY EMPTY beyond the above:** no further costs or failure modes of this approach are documented in the base. In particular, the cost of *producing* PLSs (author effort, editorial load) is documented nowhere in these sources and is therefore not asserted here.

---

# Claim Type (KOS-0003 §3)
**Descriptive** — what one surveyed practice does about the expert-to-lay register problem, what its documentation says that is for, what was measured, and what is documented about where it fails. No element is causal, normative, or comparative-evaluative; no system is ranked or recommended.

# Evidence (KOS-0003 §4)
Type: **Empirical** (SRC-0159, for element (iii)) and **Historical/Documentary** (SRC-0157, SRC-0158, for elements (i), (ii), (iv)).
- SRC-0158 — the PLEACS standard itself, v3.0 (28 Feb 2013); **interior READ this session** from the Wayback Machine capture (23 Oct 2014) of the exact URL SRC-0159's reference 2 cites; item structure, statuses, and wording taken from the document.
- SRC-0157 — GRADE consensus statement (BMJ 2008); **interior READ this session** (PMC full text).
- SRC-0159 — the adherence study (BMC Med Res Methodol 2016); **interior READ this session** (publisher full text); all figures in element (iii) derived from it directly.

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: **4** — elements (i)/(ii) rest on direct reading of the governing documents; element (iii) on one peer-reviewed study with duplicate independent extraction. Not 5: one study, no replication in the base.
- Relevance: **5** — the sources are exactly the standard, its expert-side vocabulary, and its measured adherence.
- Independence: **3** — SRC-0159 is independent of Cochrane's editorial apparatus in authorship but measures Cochrane's own standard within the Cochrane corpus; SRC-0157 authors are GRADE's developers (their article's competing-interests statement says so).
- Quality: **4** — full interiors read; the adherence study's method is stated and reproducible from the record.
- Limitations: one domain (medicine), one organization (Cochrane), one adherence study, no comprehension measurement, no second edition of the standard checked beyond the catalogued v3.0.

# Source Evaluation
SRC-0158 is an organizational standard (authority: the organization's own editorial rules — definitive for what the standard says, no authority on whether it works); SRC-0157 is a consensus statement by the system's own working group (authoritative for design intent; its performance assertions are interested and are confined to element (ii)); SRC-0159 is a peer-reviewed empirical audit (the only performance measurement in this claim; its own limitations are carried into element (iii)).

# Assumptions (KOS-0003 §10)
- **Single-domain bracket (binding).** Everything here is medicine; no portability to law, scholarly publishing, or any other domain is asserted, and any future portability claim must be made as an explicit inference elsewhere.
- **Adherence ≠ effectiveness.** The measured quantity is conformance of written summaries to a reporting standard, not whether lay readers are actually served; the claim never converts the former into the latter.
- **The archived standard is the operative edition.** The Wayback capture (2014) of the URL SRC-0159 cites is taken to be the v3.0 PLEACS the study measured against; the document's own version line (v3.0, 28 Feb 2013) matches SRC-0158's catalogued edition.
- **Terminological bracket.** GRADE's "quality of evidence" is defined in SRC-0157 as confidence in effect estimates; it is not Relatio's `confidence` axis, and the two are not translated into each other (STD-0007; see Limitations).

# Reasoning (KOS-0003 §7)
**Descriptive reporting with one derivation.** Elements (i), (ii), (iv) report what read documents say, in their registers. Element (iii) derives the performance picture from the one measurement in the base, carrying the study's scope conditions with the figures. The main reasoning risks: (1) **letting the rationale register leak into the evidence register** — controlled by the element structure itself and by confining SRC-0157's motivating cases and adoption reports to (ii); (2) **over-reading an adherence audit as an effectiveness result** — controlled by naming comprehension as explicitly unmeasured; (3) **generalizing one organization's practice** — controlled by the single-domain bracket.

# Confidence (KOS-0003 §8)
- **b_approach_described — Level 4 (High):** the description of the approach rests on this session's direct reading of all three interiors, including the standard itself in the exact edition the adherence study cites. Not Level 5: the base is three documents from one organization and one domain, and the 14-vs-12 item-count divergence between SRC-0159 and the archived standard, while recorded, is unresolved.
- **b_stated_rationale_recorded — Level 4 (High):** the rationale is quoted or closely paraphrased from the read documents' own statements of intent; the register confinement is structural.
- **b_evidence_of_performance — Level 3 (Moderate):** one peer-reviewed study, large sample, duplicate extraction — but a single unreplicated study, self-limited to measurable items, measuring adherence rather than comprehension, in one organization. The grade is on the performance picture this element asserts, which is scoped to exactly that.
- **b_documented_costs_failure_modes — Level 3 (Moderate):** the documented costs are real and sourced (enforcement gap, certainty-item collapse, under-length, categorisation arbitrariness) but partly live in the sources' discussion registers, and the production-cost side is documented nowhere in the base.
- **No Level 5. Everything R0.**

# Limitations
- Asserts nothing about any domain but medicine, any organization but Cochrane, or any register mechanism other than the mandated parallel summary; asserts nothing about lay comprehension; does not evaluate whether PLEACS is a good standard; does not compare this approach to any other system's, and produces no recommendation.
- **Terminological drift (STD-0007), recorded:** *"quality of evidence"* in GRADE means confidence in an effect estimate for an outcome — a different object from Relatio's per-component record `confidence`, despite the shared High/Moderate/Low/Very Low surface labels; *"mandatory"* in PLEACS means an editorial publication condition, which SRC-0159 shows was not enforced as one; *"adherence"* in SRC-0159 is conformance of a text to a reporting standard, not compliance behavior of people. None of these terms is translated into Relatio's vocabulary anywhere in this record.
- **May not be cited outside Relatio or for any external reliance (R0), regardless of INV-0019's closure state.**

# Alternative Interpretations
1. **Read the 57% / 0.7% result as evidence the parallel-summary approach fails.** Rejected as stated — the study measures adherence to one standard in one window; the approach's effectiveness for readers was not measured. The claim records low adherence, not failure of the register concept.
2. **Read GRADE's wide adoption as evidence the certainty vocabulary works.** Rejected — maturity is not efficacy (INV-0019 §2); adoption is recorded in (ii) as a fact about uptake and deliberately excluded from (iii).
3. **Treat SRC-0159's "14 items" as an error and correct it from the archived standard.** Rejected — the divergence is recorded as a divergence between sources; adjudicating it is neither needed by this claim nor this circuit's to do.
4. **Fold the discrepancy into a claim that the standard was unstable across editions.** Rejected — no second edition is in the base; that would be inference beyond the sources.

# Relationships (STD-0004)
- `derived_from` SRC-0157, SRC-0158, SRC-0159.
- `supports` FND-0019.
- `part_of` INV-0019.
- The precise SRC-0159 → SRC-0158 "empirically evaluates adherence to" relationship remains routed as **GB-2026-047** and is **not resolved or re-typed by this claim** (owner-reserved).

# Verification (STD-0006 §7.5 — Specialist disclosure)
**Strongest verification posture of the four claims: all three source interiors were READ this session.** SRC-0159 from the publisher's open-access full text; SRC-0157 from PMC; SRC-0158 from a Wayback Machine capture (23 October 2014) of the exact editorial-unit.cochrane.org URL that SRC-0159's reference 2 cites — the live URL no longer resolves, and the archived document self-identifies as v3.0, 28 February 2013, matching the catalogued edition. All element-(iii) figures were derived from SRC-0159's text directly (INV-0019 §3.3 discipline); nothing was transcribed from the brief or scaffold. Everything **R0; not cleared for external reliance regardless of closure.**

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-24|Draft|Created for RQ-0019 (Specialist pass), CLM B of four (warrant: GB-2026-044). Four separable elements recorded and separately graded: **(i)** the mandated-parallel-summary approach — PLS alongside the expert review, prescribed item-by-item by PLEACS v3.0 (twelve items read from the archived standard: ten mandatory, two highly desirable), with GRADE as the expert-side certainty vocabulary PLS12 mandates be translated (High); **(ii)** stated rationale in its own register — consumer-involved standard-setting, stand-alone lay accessibility, knowledge translation; GRADE's transparency/simplicity intent with its motivating failure cases confined here (High); **(iii)** evidence of performance derived directly from SRC-0159's interior — 1738 PLSs, zero full adherence, 57% overall, GRADE-certainty item 0.7%, 76% under-length, 43–81% CRG spread, weak positive time trend; support-surface hypothesis (a) confirmed in shape by the source with scope conditions carried; explicitly empty for GRADE performance and for lay comprehension (Moderate); **(iv)** documented costs — unenforced mandatory status, certainty-core collapse, under-length failure, the standard's own evidence base recorded as an open question, GRADE's self-documented categorisation arbitrariness; explicitly empty beyond the sources, production costs undocumented (Moderate). **14-vs-12 item-count divergence between SRC-0159 and the archived standard recorded as a divergence, not adjudicated.** Single-domain (medicine) bracket binding throughout. Interiors of all three sources READ (SRC-0158 via Wayback capture of the exact cited URL). No Level 5; R0; GB-2026-047 untouched. Pending Critical Review and structural validation.|

# End CLM-0100
