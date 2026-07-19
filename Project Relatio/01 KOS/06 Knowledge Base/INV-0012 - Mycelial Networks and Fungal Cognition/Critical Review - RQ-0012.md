---
title: Critical Review - RQ-0012
document_type: Review Report
version: 1.0
status: Draft
operational_status: Active
created: 2026-07-19
category:
  - Knowledge Base
  - Review
  - Mycology
  - Cognitive Science
parent_documents:
  - INV-0012 Mycelial Networks and Fungal Cognition
  - STD-0006 Review & Validation Standard
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - ROLE-0004 Critical Reviewer
related_documents:
  - FND-0012 Mycelial Network Signaling and the Bounds of Fungal Cognition
  - CLM-0059 Growth and Adaptive Foraging
  - CLM-0060 Resource Transport
  - CLM-0061 Electrical Signaling Datum and Language Overreach
  - CLM-0062 Chemical Signaling and Whole-Colony Integration
  - CLM-0063 Mycorrhizal Inter-Plant Transfer Wood Wide Web
  - CLM-0064 Learning and Memory-Like Behavior
  - CLM-0065 The Neural-Network Analogy
  - CLM-0066 The Cognition Verdict
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Review
  - CriticalReviewer
  - FungalNetworks
  - BasalCognition
  - NeuralAnalogy
relationships:
  - type: related_to
    target: INV-0012
  - type: related_to
    target: FND-0012
  - type: derived_from
    target: STD-0006
  - type: derived_from
    target: KOS-0003
---

# Critical Review — RQ-0012

## Epistemic Validation Report (ROLE-0004)

> **Scope (STD-0006 §8):** epistemic review only — evidence grading, reasoning risks, confidence calibration, assumptions, steelmanned alternatives, motivated reasoning, source fidelity/fabrication, the datum≠interpretation spine, and the *Physarum*-is-not-a-fungus firewall. Structural/metadata/graph conformance (validate.py / graph_integrity.py, Identifier Registry, the long H1 title) is ROLE-0001's and is escalated, not ruled, here (§9).
>
> *Conducted in a separate ROLE-0004 invocation; independence is procedural only (§1). Runs the standard adversarial pass plus the six targets the RQ-0012 handoff named: press CLM-0064 (single-group memory) and CLM-0063 (headline placement) hardest; check CLM-0062 for Ca²⁺ over-reach; verify the two flagged-uncertain citations (SRC-0079 Olsson, SRC-0080 Adamatzky) and the Karst kin-provisioning finding; confirm the datum≠interpretation and Physarum firewalls hold; and give an independent read on whether the asymmetric verdict is fair or tips into reflexive debunking.*

---

# 1. Honest limits & verification strength (read first)

- **Procedural independence only.** Reviewer and Specialist are the same underlying model. This pass catches overclaiming, calibration drift, single-group reliance, register slides, and citation error — **not** a systematic blind spot we share (ROLE-0004 §5). INV-0012 is **not** health/high-stakes and **not** child-facing, so no health gate applies — but it **is externally-consequential** (it may be cited into other streams), so STD-0006 §7.5 governs and a passed procedural review does **not** by itself clear the finding for external reliance. For a cross-disciplinary claim spanning mycology, electrophysiology, mycorrhizal ecology, and philosophy of cognition, genuine independent review (a different model, or a qualified human specialist) is the appropriate gate-lift.
- **Verification — STRONG, not verification-light.** I independently re-located **7 of the 14 sources this session** plus the CLM-0063 rebuttal, prioritizing the two the Specialist flagged as uncertain and the most load-bearing contested items:
  - **SRC-0079 Olsson & Hansson 1995** — *Naturwissenschaften* 82(1):30–31, DOI 10.1007/BF01167867. **Confirmed** (Springer, ADS 1995NW.....82...30O). Species *Pleurotus ostreatus* and *Armillaria* (*A. bulbosa*); the stimulus-sensitivity (spiking altered when the cord contacted beech wood 1–2 cm away) confirmed verbatim. The specific numeric parameters remain from secondary summaries — honestly flagged by the Specialist; I did not re-derive them from the 1995 PDF.
  - **SRC-0080 Adamatzky 2022** — *R. Soc. Open Sci.* 9(4):211926, DOI 10.1098/rsos.211926. **Confirmed, including the figures the Specialist read from the abstract (primary PDF had returned HTTP 403):** spike duration **1–21 h**, amplitude **0.03–2.1 mV**, four species (*Omphalotus nidiformis, Flammulina velutipes, Schizophyllum commune, Cordyceps militaris*), "lexicon" up to ~50 words. The figures are real; the "language" framing is genuinely the paper's own (speculative) framing.
  - **SRC-0081 Blatt et al. 2024** — *Fungal Ecology* 68:101326, DOI 10.1016/j.funeco.2023.101326, ADS 2024FunE...6801326B. **Confirmed, including the full author list** (Blatt, Pullum, Draguhn, Bowman, Robinson, Taiz — the item the Specialist flagged as summary-derived) and the "presumption of a fungal language is premature and unsupported" thesis.
  - **SRC-0084 Karst, Jones & Hoeksema 2023** — *Nature Ecology & Evolution* 7:501–511, DOI 10.1038/s41559-023-01986-1, plus Author Correction s41559-023-02035-7. **Confirmed, and the load-bearing finding confirmed near-verbatim:** the mother-tree preferential-kin-provisioning claim "has **no peer-reviewed, published evidence**." The insider-correction signal is real — **Melanie D. Jones** co-authored **both** Simard et al. 1997 (SRC-0083) and this review.
  - **SRC-0086 Fukasawa, Savoury & Boddy 2020** — *ISME J* 14(2):380–388, DOI 10.1038/s41396-019-0536-3, PubMed 31628441. **Confirmed;** single Boddy-group study, directional-regrowth carry-over, authors' own "intelligence"-hedged framing. This confirmation is what grounds F-1.
  - **SRC-0087 Lyon 2006** — "The biogenic approach to cognition," *Cognitive Processing* 7(1):11–29, PubMed 16628463. **Confirmed** (the 2020 *Adaptive Behavior* companion is well-attested; not separately re-paginated).
  - **SRC-0088 Baluška & Reber 2019** — *BioEssays* 41(3):e1800229, DOI 10.1002/bies.201800229. **Confirmed,** including the CBC substrates (excitable membranes, oscillating cytoskeletal polymers, flexible proteins) and its avowedly speculative status.
  - **CLM-0063 rebuttal** — "Belowground carbon transfer across mycorrhizal networks among trees: Facts, not fantasy" (PMC10751480, 2023) **confirmed real**; see the soft note in §8 on the "Klein et al." first-author attribution, which I could not confirm this session.
- **Not individually re-located this session (real, well-known standard works; Specialist-verified):** SRC-0077 (Boddy program), SRC-0078 (Fricker et al. 2017), SRC-0082 (Buffi et al. 2025), SRC-0083 (Simard et al. 1997), SRC-0085 (Kiers et al. 2011), SRC-0089 (Money 2021), SRC-0090 (Tero et al. 2010). These are among the most-cited papers in their subfields; I have high confidence they are genuine, but I did not re-verify each against its primary this session.
- **No fabrication found in any object** (KOS-0003 §12.1 clear). Where the Specialist self-graded verification "moderate" (Olsson parameters, Adamatzky figures, Blatt author list), my independent check **confirmed the items** — the honest direction of error. On CLM-0062 the Specialist was, if anything, *over*-cautious: fungal calcium/calcineurin signaling is a substantial real literature, not merely "general cell biology," so the Ca²⁺ mention is *under*-claimed, not over-claimed.
- **Net:** a **strong** verification pass covering both flagged-uncertain items and every load-bearing contested claim. But per STD-0006 §7.5 this **may not clear INV-0012 for external reliance** — it is procedural same-model review of an externally-consequential cross-disciplinary finding.

---

# 2. Steelman (given before attacking)

This is disciplined, well-instrumented work, and its central architecture is correct. The investigation's hardest design problem is that the domain is a trap in *both* directions — asymmetric enthusiasm ("fungi think/talk/mother their young") and asymmetric skepticism ("mere chemistry; cognition talk is nonsense") — and the Specialist names and structurally resists **both** (FND §1 motivated-reasoning guard). Three disciplines are genuinely enforced, not merely declared:

1. **The datum→interpretation spine (CLM-0061).** The electrical-spiking *datum* (Moderate) and the "language" *interpretation* (Very Low) are held at two clearly-separated levels with two distinct evidential bases, and the headline explicitly refuses to let the datum's Moderate lift the interpretation. This is the model instance of the discipline the investigation exists to enforce.
2. **The *Physarum* firewall.** SRC-0090 (Tero et al.) is typed `related_to` (not `supports`/`derived_from`) on CLM-0064 and CLM-0065 and carries **zero** fungal-evidential weight. I checked every claim: no *Physarum* result is imported as a fungal capacity anywhere. The famous maze/Tokyo-rail results are explicitly quarantined as the very error the investigation guards against. Clean.
3. **Both poles steelmanned, and the deflation earns its asymmetry.** The enthusiast pole is given real strength — basal cognition (rung d) is graded "Low, **not zero**," explicitly as "a legitimate scientific research program"; the carbon-movement datum is held at Moderate and the Klein rebuttal is steelmanned rather than dismissed; adaptive foraging is graded genuinely High. The deflation of "language," "wood-wide web," and "fungal brain" is reached on **specific evidential grounds** (Blatt's artifact critique; Karst's citation-bias audit with verbatim "no peer-reviewed field support"; concrete neural disanalogies), not on a blanket anti-cognition prior. My independent read (§7) is that the verdict does **not** tip into reflexive debunking.

The weakest-link discipline (FND bounded at Level 2 for the cognition verdict while carrying the High descriptive base separately), the explicit bracketing of rung (e), and the framework-relative handling of the "what counts as thought" sub-claim (biogenic vs representation-requiring, no single verdict) are all correctly executed. The flags below are calibration and consistency sharpening, not demolition.

---

# 3. The adversarial pass (the brief's named tests)

**Test A — press CLM-0064 (single-group memory) hardest. Verdict: the carry-over sub-grade (Moderate) is at or above its ceiling. FLAGGED (F-1) — lower to Level 2 or defend.**
This is my primary finding, and it aligns with the brief's steer. The "memory-like carry-over" sits at **Level 3 (Moderate)**, but its *entire* evidential weight is **one study from one group**: SRC-0086 (Fukasawa, Savoury & Boddy 2020). The other two sources on the claim contribute nothing to the datum — SRC-0089 (Money) is quarantined opinion, SRC-0090 (*Physarum*) is firewalled to zero weight. The claim's own evaluation records **Independence 2** (the lowest in the investigation), **Reliability 3**, and "not yet broadly replicated across labs," and the confidence line itself concedes the grade is "**bordering Low given single-group reliance.**"
- By KOS-0003 §8, **Level 2 (Low)** = "limited support; major unresolved issues"; **Level 3 (Moderate)** = "reasonable support; meaningful uncertainty." A single unreplicated study from a single group is the textbook signature of "limited support." The Specialist's own hedge signals they know it is at the boundary.
- I re-located SRC-0086 and confirmed it is genuinely a lone Boddy-group result (Cardiff/Tohoku), not a replicated line. Nothing in the evidence set independently corroborates the carry-over datum.
- **Remedy:** F-1. Lower the **carry-over sub-grade** to Level 2 (Low), *or* defend Moderate with an explicit paragraph on why one well-designed experiment plus the mechanistic plausibility of structural carry-over licenses Moderate despite Independence 2 and no replication. The **headline stays Level 2 (Low) either way** (the weakest-necessary-link — cognitive learning — already governs it), so the finding's shape does not move; this is a sub-grade honesty fix. Knock-on: FND-0012 §1 rung (c) ("CLM-0064, Moderate for the carry-over datum") must track the resolution.

**Test B — CLM-0063 headline placement: does Level 2 under-sell established carbon movement? Verdict: the finding does not under-sell it, but the headline-selection *rule* is inconsistent with CLM-0061. FLAGGED (F-2) — consistency fix; no level change.**
CLM-0063 and CLM-0061 are structurally identical two-level split claims, but they headline in **opposite directions**:
- **CLM-0061** headlines at the **higher** sub-level — **Moderate** (the datum), not Very Low (the interpretation) — reasoning "the claim's assertion is precisely the pairing… its Moderate rests on the datum."
- **CLM-0063** headlines at the **lower** sub-level — **Low** (the strong CMN claims), not Moderate (the movement datum) — reasoning "the claim's principal work is to *deny* the strong narrative."
Both individual choices are defensible in isolation, and FND §2 correctly extracts both sub-levels ("movement Level 3 (Moderate); strong CMN claims Level 2 (Low)"), so the *established* carbon movement is **not** actually deflated in the finding. But the two claims apply **different headline-selection rules** without stating that they do, which could mislead a downstream reader of the INV §4 table (who sees only "Level 2 (Low)" for CLM-0063). **Remedy:** F-2. State one explicit headline rule for split claims and apply it to both, or justify the asymmetry in each claim's Confidence section. **Note: I do not — and cannot — require raising CLM-0063 to Moderate; that would be an upward revision (OPS-0003 §4). This is a documentation/consistency fix only.**

**Test C — CLM-0062: over-reach on Ca²⁺ / "ionic signaling"? Verdict: NO. Conformant.**
The Ca²⁺-specific language is honestly disclosed as parametric ("flagged as not independently re-verified with a fungal-Ca²⁺ primary this session"), the confidence is capped at "integration, **likely** including ionic signaling" rather than a precise pathway, and Quality is scored 3 precisely because the mechanism rests partly on general knowledge. The word "Ca²⁺" is hedged with "likely/e.g." in the claim itself. If anything the Specialist **under**-claimed: fungal calcium/calcineurin signaling is a real, substantial literature, so the honest direction of error is caution, not over-reach. The "coordination ≠ cognition" firewall (Kiers demonstrating the non-cognitive market route) is enforced. No remediation; a Specialist wishing to firm the sub-claim could pin a fungal-Ca²⁺ primary, but it is not required and would not change the Moderate grade.

**Test D — citation verification (the two flagged items + the load-bearing kin-provisioning finding).** Spent the bulk of my verification budget here (§1). **Result: both flagged-uncertain items confirmed** — Olsson & Hansson 1995 is real with the described stimulus-coupling; Adamatzky's 1–21 h / 0.03–2.1 mV figures (read from the abstract because the PDF 403'd) are **accurate**. The Karst "no peer-reviewed field support for preferential mother-tree provisioning" finding is **confirmed near-verbatim**, as is the Jones-on-both-papers insider signal. Blatt's flagged author list is confirmed. **No fabrication in any checked cluster.**

**Test E — the datum→interpretation spine and the *Physarum* firewall.** Verified claim-by-claim. CLM-0061 holds datum/interpretation at two well-separated levels. No other claim slides from "observed" to "means cognition": CLM-0059 caps "adaptive" at behavioral; CLM-0060 caps "regulation" at physiological; CLM-0062 caps "coordination" at non-cognitive; CLM-0064 holds carry-over apart from learning. SRC-0090 is `related_to` only on CLM-0064/0065 with zero weight; no fungal claim imports a *Physarum* result. **Both firewalls hold.**

**Test F — scope, ladder, and bracketing.** Exactly 8 claims (CLM-0059…CLM-0066), each explicitly claim-typed. No applied/individualized claims (agriculture/medicine/pharmacology excluded by construction). No magnitude ranking (explicitly disclaimed). "Intelligence" is graded against the §1 ladder throughout, never assumed or dismissed; rung (e) sentience is **genuinely bracketed** in CLM-0066 and FND (neither asserted nor denied); the bounded philosophical sub-claim is handled with competing definitions and no single yes/no verdict. **Conformant.**

---

# 4. Independence / proponent-program risk

The corpus is genuinely multi-polar and the strongest independence signal in the set is real and verified: **Melanie D. Jones co-authored both Simard 1997 (pro-transfer) and Karst 2023 (skeptical correction)** — an insider self-correction, not an outside attack, correctly credited as Independence 5 on CLM-0063. Two residual, minor non-independence points:
- **CLM-0059 Independence 4 is mildly generous (F-3).** Both anchor sources share **Boddy** as a (co-)author — SRC-0077 *is* Boddy, and SRC-0078 is Fricker, Heaton, Jones & **Boddy**. They are not two fully independent programs *for this claim's sources*. The phenomenon (adaptive foraging) is genuinely replicated across species and labs beyond these two records, so the Level 4 confidence stands; but the independence *sub-score* should read 3, not 4. Recordable.
- **CLM-0064 Independence 2** is correctly the lowest in the set and is the basis of F-1 (Test A).
The strongest *epistemic* limit is not in the sources but in **this review**: procedural-only, same-model (§1, §10).

---

# 5. Motivated reasoning

Both convenient stories are named and resisted in structure, not just prose (FND §1). The marketable "fungi think/talk/mother their young" narrative is checked by the datum≠interpretation discipline, the *Physarum* firewall, and Karst's citation-bias evidence; the over-corrective "mere chemistry" story is checked by the genuinely High rungs (a)–(b) and the explicit legitimacy of basal cognition as a research program (rung d Low, not zero). Adamatzky's standing "fungal computing" interest and Simard's "mother tree" public advocacy are both named as motivated-reasoning vectors on the specific claims they touch. The one reflexive item — the **GB-2026-002 quantitative-fields watch-item** (INV §5) — reaches a **deflationary, anti-bloat** verdict ("prose carried the content; mild non-decisive strain; do not enact"), which is *anti*-flattering to adding architecture and therefore lowers, not raises, the motivated-reasoning hazard; it is owner-reserved and logged only, and I concur it is honest (§7). No motivated-reasoning *defect* is charged; F-1/F-2/F-3 are calibration and consistency slips, not a tilt.

---

# 6. Per-object verdicts (STD-0006 §7)

| Object | Verdict | Criterion |
|---|---|---|
| **INV-0012** | **Conformant** | Protocol sound; datum≠interpretation and *Physarum* firewalls declared and enforced; claim-type discipline present; scale discipline clean (native `Level N` only); scope/ladder/bracketing intact; GB-2026-002 watch-item honestly assessed and owner-reserved. |
| **FND-0012** | **Flagged → remediation specified** | F-1 knock-on: §1 rung (c) "CLM-0064, Moderate for the carry-over datum" must track the sub-grade resolution. Otherwise weakest-link discipline correct; asymmetric shape earned; rung (e) bracketed; no claim exceeds its weakest necessary link. |
| **CLM-0059** | **Conformant (note)** | Level 4 (High) well-earned and uncontested across poles; "adaptive" capped at behavioral. F-3: Independence sub-score 4 → 3 (both sources share Boddy). No confidence change. |
| **CLM-0060** | **Conformant** | Level 4 (High) defensible; datum agreed even by CMN skeptics; firewalled from the contested inter-plant transfer (CLM-0063). |
| **CLM-0061** | **Conformant** | The model instance of the datum≠interpretation spine: datum Level 3 / "language" Level 1, well-separated, two evidential bases; headline Moderate justified as the pairing. Olsson + Adamatzky figures independently confirmed. |
| **CLM-0062** | **Conformant** | Level 3 (Moderate) for integration; Ca²⁺ honestly hedged/parametric and capped; coordination framed non-cognitively (Kiers). Over-reach test passed (if anything under-claimed). |
| **CLM-0063** | **Flagged → remediation specified** | F-2 (calibration consistency, KOS-0003 §8): headline-selection rule (Low = the deflationary work) is the *inverse* of CLM-0061's (Moderate = the datum) without stating so. State one rule or justify the asymmetry. Split verdict itself honest; Karst finding verified; **no level change (cannot raise).** |
| **CLM-0064** | **Flagged → remediation specified** | F-1 (calibration, KOS-0003 §8): carry-over Level 3 (Moderate) rests on a single unreplicated Boddy-group study (Independence 2, Reliability 3), with Money quarantined and *Physarum* zero-weight. **Lower carry-over to Level 2, or defend Moderate against the single-group/no-replication problem.** Headline Level 2 (Low) unchanged. *Physarum* firewall clean. |
| **CLM-0065** | **Conformant** | Structural Moderate / strong analogy Low; §7 analogical sufficiency test applied explicitly; ML-vs-biological "neural network" equivocation named; disanalogies (no neurons/synapses/AP, ms-vs-hours) concrete and decisive; does not exceed its base. |
| **CLM-0066** | **Conformant** | Ladder verdict correctly weakest-link-bounded (headline Low); rungs (a)–(b) High inherited; (d) Low "not zero" (anti-debunking guard); (e) bracketed; bounded philosophical sub-claim framework-relative with competing definitions, no single verdict. |
| **SRC-0077** (Boddy) | **Flagged → remediation specified** | F-4 (source-internal cross-reference, minor): §4 "directional carry-over (developed further in **SRC-0085**)" — SRC-0085 is Kiers (reciprocal rewards), which does not develop carry-over; intended reference is **SRC-0086** (Fukasawa memory). Fix the pointer. Substance/authority otherwise sound; 1999 pagination disclosed parametric. |
| **SRC-0078** (Fricker 2017) | **Conformant** | Real standard synthesis; Specialist-verified strong; paraphrases match; correctly used for structure/transport, not cognition. |
| **SRC-0079** (Olsson 1995) | **Conformant** | Citation and stimulus-coupling finding independently confirmed; numeric parameters honestly disclosed as secondary-verified. |
| **SRC-0080** (Adamatzky 2022) | **Conformant** | Citation and the exact figures (1–21 h; 0.03–2.1 mV) independently confirmed despite the primary PDF 403; motivated-reasoning vector on the interpretation correctly named; datum/interpretation split honored. |
| **SRC-0081** (Blatt 2024) | **Conformant** | Citation, full author list, and three critique points independently confirmed; skeptical pole not overread into "no signaling at all." |
| **SRC-0082** (Buffi 2025) | **Conformant** | Measured-middle review; Specialist-verified strong; correctly used to hold datum at Moderate / interpretation Low. |
| **SRC-0083** (Simard 1997) | **Conformant** | Landmark pro-transfer primary; ~6% net-gain figure and reciprocal-labelling design consistent with the record; strong downstream WWW claims correctly firewalled to CLM-0063; Simard advocacy named as a vector. |
| **SRC-0084** (Karst 2023) | **Conformant** | Load-bearing skeptical anchor; three-claim structure and the "no peer-reviewed field support" finding confirmed near-verbatim; insider-correction (Jones) independence signal verified. |
| **SRC-0085** (Kiers 2011) | **Conformant** | Non-cognitive market-regulation anchor; correctly used to show "coordination ≠ decision." Well-known *Science* paper; Specialist-verified strong. |
| **SRC-0086** (Fukasawa 2020) | **Conformant (note)** | Independently confirmed; genuinely a single Boddy-group study — the fact that grounds F-1. Authors' own operational hedging correctly captured. |
| **SRC-0087** (Lyon) | **Conformant** | 2006 biogenic-approach article confirmed; framework role (grading instrument, not confidence-raiser) correct; contested-construct status and sentience-exclusion flagged. |
| **SRC-0088** (Baluška & Reber 2019) | **Conformant** | Citation and CBC substrates independently confirmed; correctly steelmanned as the bracketed maximal pole and **not adopted**; "cannot discriminate" reasoning sound. |
| **SRC-0089** (Money 2021) | **Conformant** | Honestly labelled opinion; quarantined from grading; enthusiast pole stated fairly, lifts no confidence. |
| **SRC-0090** (Tero 2010, *Physarum*) | **Conformant** | Comparandum only; `related_to` typing enforces zero fungal-evidential weight; non-fungal (protist) status correctly load-bearing; firewall honored on every touching claim. |

**No object Blocked. No fabrication. 7 of 14 sources (plus the CLM-0063 rebuttal) independently re-located this session, covering both flagged-uncertain items and every load-bearing contested claim.**

---

# 7. Independent read on the asymmetric verdict — is the deflation fair, or reflexive debunking?

**My read: the asymmetry is fair and evidence-driven; it does NOT tip into reflexive debunking, and the enthusiast pole is genuinely steelmanned rather than strawmanned.** Four checks:

1. **The deflations are each grounded in a specific, verified source, not a general prior.** "Language" Very Low rests on Blatt's artifact critique + Buffi's replication caution + the absence of language-like structure (all real). Strong "wood-wide web" Low rests on Karst's citation-bias audit with the verbatim "no peer-reviewed field support" finding (confirmed). "Fungal brain" Low rests on concrete neural disanalogies. None is a bare "it's just chemistry."
2. **The verdict grades UP the real biology.** Rungs (a)–(b) at High and the carbon-movement datum at Moderate show the Specialist is not reflexively minimizing — the affirmative half of the answer is genuinely affirmative, and "agreed even by deflationary experts" is an accurate characterization.
3. **The anti-debunking guard is explicit and load-bearing.** Basal cognition (rung d) is "Low, **not zero**," framed as "a legitimate scientific research program, not a nonsense," and the Klein rebuttal is steelmanned (movement held at Moderate, not "refuted"). This is the single clearest evidence that the deflation is disciplined rather than reflexive: the Specialist repeatedly stops the skeptical pole from over-swinging.
4. **The residual risk is the *opposite* one — mild over-caution, not over-debunking.** CLM-0062's under-claim of fungal Ca²⁺ signaling and the conservative self-grading of confirmed citations both err toward caution. The one genuine over-grade I found (F-1, the single-group memory carry-over) runs in the *enthusiast* direction, not the skeptic direction — i.e., the Specialist was slightly too generous to a "fungal memory" datum, which is the honest failure mode for a reviewer worried about reflexive debunking to catch.

So the split verdict is the right answer at honest confidence, and both poles are represented at strength. The correction I press (F-1) makes the verdict *marginally more* deflationary on one sub-grade — which is the direction downward-pressure review is licensed to move — while leaving the overall asymmetric shape intact.

**I also concur with the GB-2026-002 watch-item assessment** (INV §5): the prose evidence fields carried the quantitative content, and the one soft signal (the ms-vs-hour spike-timescale discrepancy, which a structured units+method field would surface more sharply) is a mild, non-decisive strain, not a break. Honest and owner-appropriate; logged only, not enacted.

---

# 8. Required remediation — exact fixes

**F-1 (CLM-0064 §Confidence + §Evidence Evaluation; knock-on to FND-0012 §1 rung (c) and §2). Single-group carry-over over-graded.**
Apply **one** path:
- **(a) Lower (reviewer-preferred under the downward-pressure mandate):** change the **carry-over sub-grade** in CLM-0064 from **Level 3 (Moderate)** to **Level 2 (Low)**, on the ground that a single unreplicated study from one group (SRC-0086; Independence 2; Reliability 3; "not yet broadly replicated"), with the other two sources contributing zero datum-weight (Money quarantined; *Physarum* firewalled), fits KOS-0003 §8's Level-2 definition ("limited support; major unresolved issues") at least as well as Level 3. Update FND-0012 §1 rung (c) and §2 to read "Low (single-group carry-over)".
- **(b) Defend (permitted — defends the existing sub-grade, does not raise it):** retain the carry-over at Moderate only by adding to CLM-0064 an explicit paragraph stating why one well-designed experiment plus the mechanistic plausibility of structural carry-over licenses Moderate *despite* Independence 2 and the absence of cross-lab replication. Absent that paragraph, use path (a).
Either way the **headline stays Level 2 (Low)** (cognitive learning already governs it).

**F-2 (CLM-0063 §Confidence; cross-check CLM-0061 §Confidence). Headline-selection rule inconsistency.**
Add to CLM-0063's Confidence section an explicit statement of the headline-selection rule for two-level split claims, and reconcile it with CLM-0061's rule (which headlines at the higher sub-level). Either adopt one consistent rule across both claims or state why a "deny-the-strong-narrative" claim (CLM-0063) headlines low while a "hold-the-datum" claim (CLM-0061) headlines at the datum. **No confidence level changes; I cannot raise CLM-0063 to Moderate.** Documentation/consistency fix.

**F-3 (CLM-0059 §Evidence Evaluation). Independence sub-score.**
Change the Independence score from **4** to **3**, noting that both anchor sources (SRC-0077, SRC-0078) share Boddy as a (co-)author and are therefore not fully independent *programs* for this claim. **No change to the Level 4 (High) confidence** — the phenomenon is independently replicated beyond these two records. Recordable.

**F-4 (SRC-0077 §4 Key Content). Internal cross-reference error.**
Correct "directional carry-over (developed further in **SRC-0085**)" to **SRC-0086** (Fukasawa/Boddy memory); SRC-0085 (Kiers) does not develop carry-over. Recordable; no confidence change; no fabrication.

**Soft note (no remediation required, logged):** In CLM-0063 §Evidence and FND-0012 §5, the "Facts, not fantasy" rebuttal is attributed to "**Klein et al., 2023**." The paper "Belowground carbon transfer across mycorrhizal networks among trees: Facts, not fantasy" (PMC10751480, 2023) is confirmed real, but I could not confirm this session that **Klein** is the first author. Recommend the Specialist pin the exact first-author citation. Low-stakes: it is a steelman-pole marker, not a confidence-lifter.

**No confidence level is raised anywhere (a reviewer may not; OPS-0003 §4). F-1 applies downward pressure only; F-2/F-3/F-4 are consistency, sub-score, and citation-fidelity fixes.**

---

# 9. Escalations to Knowledge Architect (ROLE-0001 — not ruled here)

- Run `validate.py` + `graph_integrity.py`; register **INV-0012, CLM-0059–0066, SRC-0077–0090, FND-0012, Critical Review – RQ-0012** in the Identifier Registry.
- Verify the typed-relationship graph resolves with no dangling targets across INV-0012 ↔ FND-0012 ↔ CLM-0059–0066 ↔ SRC-0077–0090. Confirm the `supports` / `derived_from` / `part_of` direction convention matches the other INVs, and — load-bearing here — confirm **SRC-0090 (*Physarum*) is typed `related_to` (never `supports`/`derived_from`)** on CLM-0064 and CLM-0065 in the frontmatter, so the firewall is machine-enforced, not merely prose.
- **Structural note (not epistemic):** FND-0012's H1 title is a full multi-clause paragraph (as with FND-0011). Whether that conforms to STD-0001 title conventions is ROLE-0001's call.
- **F-4** (SRC-0077 → SRC-0086 cross-reference) is a content-fidelity fix I flag here but which also touches the citation graph — confirm the corrected pointer resolves.
- Confirm the acceptance-criteria claim that **STD-0006, Appendix A, GB-2026-002, and the Architecture Baseline are unmodified** by this investigation (intent stated; verifying no-change is structural).
- Reviewer's epistemic read on the deferred ENT candidates ("basal cognition"; "adaptive network"): **concur they are not yet warranted** — single-use so far; revisit only if the basal-cognition ladder is reused in a second investigation (as INV §8 already flags).

---

# 10. Verification-strength & reliance gate (STD-0006 §7.5)

- **Independence:** procedural only (same model). For this externally-consequential, cross-disciplinary finding, procedural review is **not** independent verification; genuine independent review (a different model, or a qualified human specialist across mycology / electrophysiology / mycorrhizal ecology / philosophy of cognition) is required before external reliance.
- **Verification:** **STRONG (not verification-light)** — 7/14 sources independently re-located this session plus the CLM-0063 rebuttal, covering **both** flagged-uncertain items (Olsson, Adamatzky — the Adamatzky figures confirmed despite the primary's HTTP 403) and every load-bearing contested claim (Karst kin-provisioning verbatim; Blatt author list; Baluška/Reber CBC; the single-group Fukasawa datum). No fabrication in any checked object. The 7 unchecked sources are well-known standard works, Specialist-verified.
- **Reliance gate (§7.5):** **INTACT.** This verdict clears the objects for **internal use pending remediation** (F-1…F-4); it does **not** clear FND-0012 for any external / cross-stream reliance. Any Appendix A ★-translation is an off-object boundary step and does not occur before the gate lifts.

---

# 11. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-19|Draft|Initial epistemic review of INV-0012 (ROLE-0004): **Conformant with Flags**; no Blocked objects; **no fabrication** (7/14 sources independently re-located this session — Olsson 1995, Adamatzky 2022 incl. exact figures despite PDF 403, Blatt 2024 incl. author list, Karst 2023 incl. verbatim "no peer-reviewed field support", Fukasawa 2020, Lyon 2006, Baluška & Reber 2019 — plus the "Facts, not fantasy" rebuttal confirmed real). Four flags: **F-1** (CLM-0064 carry-over Moderate rests on a single unreplicated Boddy-group study — lower to Level 2 or defend; headline unchanged; FND knock-on), **F-2** (CLM-0063 vs CLM-0061 headline-selection rule inconsistency — consistency fix, no level change/no raise), **F-3** (CLM-0059 Independence 4→3, both sources share Boddy; confidence unchanged), **F-4** (SRC-0077 §4 cross-reference SRC-0085→SRC-0086). Soft note: pin the "Klein et al." rebuttal first author. No confidence level raised. Datum≠interpretation spine and *Physarum* firewall verified clean; scale discipline clean (native `Level N` only; no ★); scope/ladder/bracketing intact. **Independent read: the asymmetric deflation of the "language"/"wood-wide web"/"fungal brain" claims is fair and evidence-grounded, does NOT tip into reflexive debunking, and steelmans the enthusiast pole (basal cognition graded Low-not-zero; movement held at Moderate); the one over-grade (F-1) runs in the enthusiast direction.** Reliance gate (§7.5) intact; independent domain review required before external use.|

---

# End Critical Review - RQ-0012
