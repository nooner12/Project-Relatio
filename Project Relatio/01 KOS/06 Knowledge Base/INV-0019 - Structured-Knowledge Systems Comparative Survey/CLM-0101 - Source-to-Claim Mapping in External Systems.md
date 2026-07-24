---
title: CLM-0101 - Source-to-Claim Mapping in External Systems
document_type: Claim Record
version: 0.2
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
  - SRC-0153 Chan et al 2024 Steps Towards an Infrastructure for Scholarly Synthesis
  - SRC-0154 Groth Gibson Velterop 2010 The Anatomy of a Nanopublication
  - SRC-0155 Clark Ciccarese Goble 2014 Micropublications
  - SRC-0156 Shotton 2010 CiTO the Citation Typing Ontology
  - SRC-0160 Hellyer 2018 Evaluating Shepards KeyCite and BCite
  - FND-0019 Structured-Knowledge Systems Survey Synthesis
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - KnowledgeSystems
  - SourceToClaimMapping
relationships:
  - type: derived_from
    target: SRC-0153
  - type: derived_from
    target: SRC-0154
  - type: derived_from
    target: SRC-0155
  - type: derived_from
    target: SRC-0156
  - type: derived_from
    target: SRC-0160
  - type: supports
    target: FND-0019
  - type: part_of
    target: INV-0019
confidence:
  - component: c_approach_described
    level: 3
    label: Moderate
  - component: c_stated_rationale_recorded
    level: 3
    label: Moderate
  - component: c_evidence_of_performance
    level: 3
    label: Moderate
  - component: c_documented_costs_failure_modes
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "four of five source interiors read; SRC-0154 access-blocked, disclosed; single accuracy study for the one measured system; not cleared for external reliance"
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

# CLM-0101

# Recoverable Source-to-Claim Mapping in External Systems (CLM C)

## Draft Claim Record

---

# Claim
> **The surveyed systems make the path from source to claim inspectable to very different depths — from whole-work citation (CiTO's typed links between publications), through result-level anchoring (discourse graphs' evidence nodes bound to a source), to full argument-graph resolution (micropublications' support graph, designed to let a reader traverse a claim to statements, data, and methods across works) — and the one mapping practice with measured performance in this base, the legal citator, shows that a mature, professionally-edited rendered mapping can carry substantial error while presenting itself as fact: in the one study, the three citators all agreed on what they mapped in only 11% of examined relationships, and individually failed to correctly identify 33%, 38%, and 72% of clearly negative treatments.** What is captured versus left implicit is a design choice each system makes differently; what a reader can actually reconstruct was measured for none of the semantic-publishing systems and once for the citators.

---

# Element (i) — Approach (descriptive)

What each system captures, what it renders, and what a reader can in principle reconstruct:

- **Micropublication (SRC-0155 — interior read):** the deepest documented design. Support is a **graph**: a claim is rooted in a DAG of supporting statements, data, and methods; references may be resolved past the whole-work level "to a specific Statement within the document"; *claim lineages* (chains of citing/cited claims) are first-class and transitively closable to empirical evidence; the `asserts`/`quotes` distinction localizes responsibility for what each record contributes to a merged graph; attribution is the provenance floor ("The minimal level of support for any Statement is its Attribution to some Agent"). A reader following the design can reconstruct why a claim is believed — down to the data and the method that produced it — and who asserted each link.
- **Nanopublication (SRC-0154 — interior NOT read; surface and citing literature only):** the assertion travels with a **provenance graph** for the assertion and its dataset/article of origin. At the level SRC-0155's read interior establishes, the model's third graph ("Support") carries descriptive filtering qualifiers, not evidence: provenance of origin is captured; the argumentative path is not.
- **Discourse graphs (SRC-0153 — interior read):** every evidence node is **bound to a source** (a citekey appended to the node title); evidence nodes can hold result snippets, key figures, and methodological details; inline citation becomes citation "to a specific result from that paper … rather than a reference to the whole paper"; relations are traversable in both directions. Reconstruction depth depends on what authors populate (see element (iv)).
- **CiTO (SRC-0156 — interior read):** the mapping is at **whole-work granularity** — typed relations between citing and cited publications, published as machine-readable RDF so citation networks can be built and interrogated. The paper itself notes that modern scientific citations "are typically made to the cited works as complete entities," with sentence- or element-level markup possible but early-stage. What a reader reconstructs is *which works* relate and *how the author says they relate* — not where in the cited work the support lives.
- **Legal citators (SRC-0160 — interior read):** the mature commercial instance of a rendered source-to-claim mapping: for a given case, the citator report lists every citing case with an editorially-applied treatment label (overruled, distinguished, criticized, …), so a reader reconstructs the case's validity path without reading every citing opinion. Capture is by editorial staff at scale; rendering is a per-case report; the underlying passages are recoverable by following the citations.

# Element (ii) — Stated Rationale (design-intent register ONLY)

- **Micropublication (SRC-0155):** to answer "on what grounds is this statement made?" — reducing the "far too laborious" cost of checking each cited document for the relevant claim, and exposing warrant-backing failures (a paraphrase that "distorts, or fabricates its backing" calls the claim into question).
- **Nanopublication (surface / citing literature):** assertions with assignable provenance, chiefly for data integration.
- **Discourse graphs (SRC-0153):** the document-centric infrastructure "largely do[es] not show *why* scholarly works cite each other: we cannot trace lines of evidence"; binding evidence to sources was designed to "enable writing and citing from a discourse graph."
- **CiTO (SRC-0156):** freely published machine-readable citation data would make "the construction and interrogation of citation networks … trivially simple, with enormous advantages to scholarship." The paper motivates the value of network-level inspection by reporting Greenberg's citation-network analysis — bias toward supportive citation, amplification without evidence, and conversion of hypothesis into "fact" "through the act of citation alone" — recorded here as SRC-0156's stated motivation, not as a base finding.
- **Legal citators (as SRC-0160 reports the vendors' claims):** the vendors advertise reliability — "rigorous quality controls," "[t]he industry's most accurate, up-to-the-minute citation service" — quoted by SRC-0160 from their marketing; design-intent register only, and pointedly so given element (iii).

# Element (iii) — Evidence of Performance (measured, including absence)

**Populated for exactly one system — the legal citators — from SRC-0160's interior, read this session (INV-0019 §3.3; the support-surface hypothesis was tested against the source, and the source governs):**

- **Design:** all 73 published Ninth Circuit decisions from January 1984 as the seed set; all **357 citing relationships** (citing cases 1984–2017) that at least one of Shepard's, KeyCite, or BCite labeled negative; reports for all three citators pulled same-day per case (April–June 2017); the author independently read each citing case, coding ambiguous relationships out (27 ambiguous; 21 not negative; **309 clearly negative**), with a blind re-review months later for consistency.
- **Agreement:** all three citators agreed that treatment was negative in only 53 of 357 relationships (**85% lacked three-way agreement**), and substantively agreed on the *type* of negative treatment in only 40 (**11%**). None of the three marks any relationship as ambiguous — "all three citators present their results as fact."
- **Accuracy:** of the 309 clearly negative relationships, **Shepard's failed to correctly identify 103 (33%)** (85 missed or mislabeled as positive/neutral + 18 incorrectly described); **KeyCite 116 (38%)** (105 + 11); **BCite 222 (72%)** (211 + 11). Most failures were mislabelings rather than omissions (78/7, 99/6, 178/33 respectively); all outright omissions were unpublished cases. Of relationships each citator *labeled* negative, 12% / 11% / 15% were incorrect labels. Of the four U.S. Supreme Court overrulings in the dataset, Shepard's mislabeled three, KeyCite two, BCite one. The author counted **470 total failures** and notes the design cannot catch treatment missed by all three, so the rates "may underestimate the extent of the problem."
- **Support-surface hypothesis (b) disposition (INV-0019 §3.3):** the hypothesis — that mature citators miss a substantial share of negative references and disagree on treatment type — **matches what the source reports**, with the figures above and these scope conditions: one study, one author's independent coding (with ambiguity-filtering and provider review), a seed set from one circuit and month chosen for its high reversal rate, negative-treatment identification only (not currency, retrieval, or overall merit — the author says explicitly it "is not an assessment of any citator's overall merit"). No discrepancy against the hypothesis's shape; the derivation replaces the hypothesis.
- **EXPLICITLY EMPTY for micropublications** (evaluation deferred by its own authors), **for nanopublications** (nothing in the base; interior unreadable this session), **for CiTO** (usage illustrations only; the paper states it "has not yet been widely used elsewhere"), and **for discourse graphs as measurement** (qualitative deployment only; the designed provenance capture was observed frequently unpopulated — recorded under (iv)).

# Element (iv) — Documented Costs and Failure Modes (from the sources; not inferred)

- **Editorial mapping at scale carries subjectivity and presents none of it (SRC-0160):** the author documents that "citation analysis is partly subjective" (ambiguous judicial language; contested label meanings), that providers themselves defended results as "subjective determinations" (Thomson Reuters), and that a prior vendor-commissioned expert panel reached unanimity "only about half the time" — while the products render every mapping as unqualified fact. Label-vocabulary design is itself a documented failure source: BCite's deliberately short negative-label list accounts for "roughly one-fifth" of its missing labels, and policy-driven withholding (Shepard's "citing convention" negatives; unpublished California decisions) reads to a user like error. The failures concentrate "in the editorial analysis process," not in citation retrieval.
- **Whole-work citation leaves the reader to find the support (SRC-0155, documenting BEL and conventional citation):** citing whole publications leaves "the reader to determine precisely where in the cited document a backing statement actually resides" — the documented cost that motivates statement-level resolution; reconstructing backing later is "laborious" even though it "was readily available" at extraction time.
- **Designed capture is not automatic capture (SRC-0153):** evidence nodes "lacked direct descriptions or links to methodological details or contextualizing snippets" often enough that the authors name it a limitation; the mapping a reader can reconstruct is bounded by what authors bothered to populate, and "additional labor is likely needed" for the graphs to be useful outside tight-knit groups.
- **CiTO's own documented limits:** the paper concedes the FRBR layering "might seem a little fussy" **and immediately defends it** — arguing the granularity "is of enormous value" against the ambiguities of flatter bibliographic ontologies — so this is recorded as an acknowledged-and-defended design cost, not a confessed defect; author-side typing needs tooling that did not yet exist ("scope for the development of an ontology-backed tool"); and the granularity of scientific citation practice itself (whole works) bounds what the ontology can express about *where* support lives.
- **EXPLICITLY EMPTY for nanopublications** — beyond SRC-0155's documented critique (recorded in CLM-0099 and bearing on recoverability via the Support-graph point in element (i)), no cost or failure mode specific to nanopublication provenance is documented in the readable base.

---

# Claim Type (KOS-0003 §3)
**Descriptive** — what each system captures and renders of the source-to-claim path, what its documentation says that is for, the one measured performance picture, and the documented costs. No ranking, no recommendation, no adjudication between systems.

# Evidence (KOS-0003 §4)
Type: **Empirical** (SRC-0160, element (iii)) and **Historical/Documentary** (the model papers and ontology paper).
- SRC-0160 — **interior READ this session** (AALL issue PDF, text-extracted); all figures derived directly from it.
- SRC-0155, SRC-0153 — **interiors READ this session** (structured extraction with grep-verified verbatim quotes).
- SRC-0156 — **interior READ this session** (publisher full text, read directly).
- SRC-0154 — **interior NOT read** (access-blocked; disclosed); cited at surface level and through SRC-0155 only.

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: **3** — the citator figures come from a single-author study with disclosed subjectivity management and provider disputes on file; the design descriptions come from the systems' own papers.
- Relevance: **5** — the sources are the mapping designs themselves and the one measurement of a deployed mapping practice.
- Independence: **3** — SRC-0160 is independent of all three vendors (and all three reviewed and disputed parts of it, which is recorded); the model papers describe their authors' own designs.
- Quality: **4** — four of five interiors read; the measured element carries its method with it.
- Limitations: one measured system, one study, one legal-domain practice; no measurement for any semantic-publishing mapping; SRC-0154 unread.

# Source Evaluation
SRC-0160 is a peer-context professional-journal study whose dataset was shared with the three vendors before publication, with their responses printed — the strongest independence posture in this base, though still a single coder's judgment on contested material. SRC-0155/0153/0156 are authoritative for their own designs and interested in them. SRC-0154's unread interior confines its use.

# Assumptions (KOS-0003 §10)
- **The citator result is not generalized:** it is evidence about three named products on one sample in one domain, and nothing else — expressly not about citators as a class over time, and not about semantic-publishing systems.
- **Reconstruction-in-principle vs reconstruction-in-practice are kept separate:** element (i) records designed capability; elements (iii)/(iv) record that practice was measured once (citators) and observed to under-populate designed capture once (discourse graphs).
- **Vendor claims are rationale, not evidence** — quoted only in (ii).

# Reasoning (KOS-0003 §7)
**Descriptive comparison plus one derivation.** The depth spectrum in element (i) organizes what the sources state; it implies no ordering of merit (deeper capture has documented costs of its own). The element-(iii) derivation carries the study's scope conditions with its figures. Risks: (1) **over-extending SRC-0160** to citators generally or to other domains — controlled by the scope-condition block and the assumptions; (2) **treating designed traversal as delivered traversal** — controlled by the (i)/(iv) separation; (3) **letting Greenberg-via-SRC-0156 function as a base finding** — controlled by confining it to SRC-0156's stated motivation in (ii).

# Confidence (KOS-0003 §8)
- **c_approach_described — Level 3 (Moderate):** four of five interiors read with verified quotes, but the spectrum spans a system whose interior could not be checked (nanopublication), and the citator systems' internal capture procedures are known only as SRC-0160 describes them from outside.
- **c_stated_rationale_recorded — Level 3 (Moderate):** direct quotation for four systems; surface-level for one.
- **c_evidence_of_performance — Level 3 (Moderate):** the one populated cell rests on a single study — carefully designed, provider-reviewed, but one author's coding of one sample; the empty cells rest on full readings for three systems and on within-base absence for the unreadable fourth.
- **c_documented_costs_failure_modes — Level 3 (Moderate):** well-documented for citators (in the measured source itself) and for the whole-work-citation cost (SRC-0155); thinner and partly self-acknowledged for CiTO and discourse graphs; empty for nanopublications.
- **No Level 5. Everything R0.**

# Limitations
- Says nothing about how any semantic-publishing mapping performs in use; says nothing about citator performance beyond the one sample; does not compare mapping depth to cost — the base cannot support that; does not adjudicate whether statement-level or whole-work citation is "better."
- **Terminological drift (STD-0007), recorded:** *"citation"* in CiTO denotes the performative act, not the cited work; *"support"* in micropublications is a deliberately broad transitive relation covering what other models would split into interpretation and citation; *"negative treatment"* and *"distinguished"* are contested terms **within** the legal domain itself — SRC-0160 documents the citators applying different meanings, and devotes a section to "distinguished" versus "distinguishable." None of these terms maps onto Relatio's `derived_from`/`supports` vocabulary, and no such mapping is made.
- **May not be cited outside Relatio or for any external reliance (R0), regardless of INV-0019's closure state.**

# Alternative Interpretations
1. **Read the citator figures as showing editorial mapping is inferior to formal semantic capture.** Rejected — the formal systems have no performance measurement at all in this base; an unmeasured design cannot be ranked against a measured one, in either direction.
2. **Read BCite's 72% failure rate as the headline.** Rejected as a stand-alone reading — SRC-0160 itself documents that a fifth of BCite's misses trace to a deliberate short-label design and that the statistics "treat all failures as equal"; the figure is carried with its context.
3. **Treat the Greenberg citation-distortion findings as this survey's evidence about citation practice.** Rejected — Greenberg is not in the base; what is recorded is that SRC-0156 reports those findings as motivation.

# Relationships (STD-0004)
- `derived_from` SRC-0153, SRC-0154, SRC-0155, SRC-0156, SRC-0160.
- `supports` FND-0019.
- `part_of` INV-0019.
- The catalogued `related_to` between SRC-0156 and SRC-0160 (typed vocabularies at scale) is context; unmodified.

# Verification (STD-0006 §7.5 — Specialist disclosure)
**Four of five interiors READ this session:** SRC-0160 (AALL PDF, text-extracted and read directly — methodology, statistical results, error examples, provider responses, conclusion); SRC-0156 (publisher full text, read directly); SRC-0155 and SRC-0153 (structured extraction with grep-verified verbatim quotes). SRC-0154 **NOT read** (anti-bot challenge; no archive or repository full text exists — checked via Wayback and OpenAlex), disclosed and confined to surface-level use. All element-(iii) figures derived from SRC-0160's text directly; nothing transcribed from the brief or scaffold. Everything **R0; not cleared for external reliance regardless of closure.**

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.2|2026-07-24|Draft|**Critical Review – RQ-0019 remediation (Flag F2, determinate).** Element (iv) CiTO entry reworded: the "might seem a little fussy" concession is now carried with the source's immediate defense (granularity "of enormous value" against flatter ontologies' ambiguities) and recorded as an acknowledged-and-defended design cost, not a confessed defect. **No grade changed; no other content changed.**|
|0.1|2026-07-24|Draft|Created for RQ-0019 (Specialist pass), CLM C of four (warrant: GB-2026-046). Four separable elements recorded and separately graded: **(i)** the capture-depth spectrum — whole-work typed citation (CiTO), result-level source-bound evidence nodes (discourse graphs), assertion+provenance (nanopublication, surface-level), full support-graph/claim-lineage resolution with asserts/quotes responsibility localization (micropublications), editorially-rendered validity reports (citators) (Moderate); **(ii)** stated rationales confined to their register, including vendor reliability marketing quoted by SRC-0160 and SRC-0156's Greenberg-motivated network-inspection case (Moderate); **(iii)** the one measured system — SRC-0160 derived directly: 357 relationships, 11% three-way substantive agreement, 33%/38%/72% failure on 309 clearly negative treatments, mislabeling dominant over omission, 3/2/1 of four Supreme Court overrulings mislabeled, 470 total failures, results presented as fact with no ambiguity marking; hypothesis (b) confirmed in shape by the source with scope conditions carried; explicitly empty for micropublications, nanopublications, CiTO, and (as measurement) discourse graphs (Moderate); **(iv)** documented costs — editorial subjectivity rendered as fact, label-list design losses (~1/5 of BCite misses), policy-withholding, whole-work citation's find-it-yourself burden, unpopulated designed capture, CiTO's self-acknowledged fussiness and tooling gap (Moderate). Interiors read: SRC-0153/0155/0156/0160; SRC-0154 not read (disclosed). No ranking; no Level 5; R0. Pending Critical Review and structural validation.|

# End CLM-0101
