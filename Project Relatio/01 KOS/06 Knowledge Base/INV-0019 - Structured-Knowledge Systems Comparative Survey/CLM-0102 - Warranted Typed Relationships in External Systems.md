---
title: CLM-0102 - Warranted Typed Relationships in External Systems
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
  - SRC-0152 Kunz and Rittel 1970 Issues as Elements of Information Systems IBIS
  - SRC-0153 Chan et al 2024 Steps Towards an Infrastructure for Scholarly Synthesis
  - SRC-0155 Clark Ciccarese Goble 2014 Micropublications
  - SRC-0156 Shotton 2010 CiTO the Citation Typing Ontology
  - SRC-0160 Hellyer 2018 Evaluating Shepards KeyCite and BCite
  - FND-0019 Structured-Knowledge Systems Survey Synthesis
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - KnowledgeSystems
  - TypedRelationships
relationships:
  - type: derived_from
    target: SRC-0152
  - type: derived_from
    target: SRC-0153
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
  - component: d_approach_described
    level: 3
    label: Moderate
  - component: d_stated_rationale_recorded
    level: 3
    label: Moderate
  - component: d_evidence_of_performance
    level: 3
    label: Moderate
  - component: d_documented_costs_failure_modes
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "four of five source interiors read; SRC-0152 scan-unreadable, disclosed; single accuracy study for the one measured vocabulary practice; not cleared for external reliance"
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

# CLM-0102

# Warranted Typed Relationships in External Systems (CLM D)

## Draft Claim Record

---

# Claim
> **Across the surveyed systems, typed-relationship vocabularies range from three elements to nearly a hundred classes, and in every case the type applied to a relationship is an ASSERTION by an author, annotator, or editor — no surveyed system requires a warrant for a typed relationship, and none checks one by tooling.** CiTO offers 23 citation-relationship properties chosen by the author "after consulting their ontology textual definitions"; micropublications deliberately collapse finer relation semantics into a broad transitive `supports` and make relation-assertions themselves attributable objects with no validation mechanism; discourse graphs shipped three base relations, let users extend the grammar, and observed in deployment that the typed-relation layer largely went unauthored; the legal citators apply controlled treatment vocabularies through editorial pipelines whose output — the one measured case in this base — substantively agreed across all three products on treatment type in only 11% of examined relationships, with 11–15% of applied negative labels incorrect. Where enforcement exists at all, it is editorial process, and the one measurement of such a process shows it disagreeing with itself across vendors while rendering every label as fact.

---

# Element (i) — Approach (descriptive)

**Vocabularies and their sizes:**

- **IBIS (SRC-0152 — interior NOT read; surface only):** the originating typed-deliberation model — **issues, positions, arguments** as element types with typed connections among them. Nothing finer is asserted here without the interior.
- **CiTO v1.6 (SRC-0156 — interior read):** **23 relationship properties** between citing and cited works (all but `cites`/`isCitedBy` sub-properties of `cites`), spanning factual and rhetorical relations; the full ontology carries 98 classes, 31 object properties, and 5 data properties, layered on FRBR's Work/Expression/Manifestation. A single citation may carry several types at once.
- **Micropublications (SRC-0155 — interior read):** a compact predicate set (about twenty are named in the paper: `supports`, `challenges`, `directlyChallenges`, `indirectlyChallenges`, `qualifiedBy`, `asserts`, `quotes`, `arguedBy`, `elementOf`, `supportedByData`, `supportedByMethod`, and structural others) with `supports` and `challenges` doing the argumentative work.
- **Discourse graphs (SRC-0153 — interior read):** **three base discourse relations shipped** — informs, supports, opposes — with a user-editable grammar; deployed users added relations (Substantiates, Makes, Constrains, Enables, Jointly Necessary, ConsistentWith) and node types.
- **Legal citators (SRC-0160 — interior read):** each product applies a **controlled list of descriptive treatment phrases** (overruled, distinguished, criticized, questioned/called into doubt, not followed, …). The lists differ: BCite's is "significantly shorter" (six negative labels); some labels in one product have no counterpart in another (KeyCite's "not followed"; Shepard's ACAN, treated as neutral where KeyCite's analogue is negative).

**How a type is warranted versus merely asserted, and how application is enforced:**

- **CiTO:** author assertion, guided only by definitions — "It is for the user to decide which relationships are most appropriate, after consulting their ontology textual definitions." No warrant object, no checking mechanism.
- **Micropublications:** a typed relation is itself an attributable assertion — inconsistency annotations "are themselves micropublications," each view carrying "its own attribution and authorship status." The paper provides **no automated validation** of whether an asserted `supports` or `challenges` is correct; detection of a warrant that "distorts, or fabricates its backing" is left to human inspection.
- **Discourse graphs:** relations are authored by users or recognized from writing patterns (indentation, linking); the grammar editor defines the patterns. No warrant requirement exists.
- **Citators:** the warrant is the **editorial process itself** — staff read citing cases and apply labels per internal procedures; the procedures are proprietary, and SRC-0160 evaluates only their end results.
- **No surveyed system attaches a required, checkable warrant to a typed relationship.** That is a statement about this base, at the depth read.

# Element (ii) — Stated Rationale (design-intent register ONLY)

- **CiTO (SRC-0156):** capture "the intent of the author when citing," distinguishing assistance from critique or refutation, so citation networks become interrogable for *why* works cite each other; designed "to be as simple as possible while yet being fit for purpose" for biomedical citation.
- **Micropublications (SRC-0155):** the deliberate collapse of finer types is argued from network needs — "Using a graph model requires common connective properties to allow transitive closure," and Toulmin's backing/warrant distinction is avoided as a class structure "because these concepts become relativized across a large network: one publication's backing is another's warrant."
- **Discourse graphs (SRC-0153):** a minimal base grammar with user extension — the rationale is matching "key rhetorical relationships" needed for synthesis while keeping authoring as close to normal note-writing as possible.
- **IBIS (surface only):** typed deliberation elements for wicked-problem argumentation, at the level the catalog records.
- **Citators (as SRC-0160 reports):** descriptive phrases exist because "some forms of negative treatment are more severe than others, and users may choose to examine only certain types"; Bloomberg's short list is defended by the vendor from market research that "most users don't want as many negative labels" — vendor rationale, quoted as such.

# Element (iii) — Evidence of Performance (measured, including absence)

**Populated for exactly one practice — the citators' typed treatment vocabularies — from SRC-0160, read this session (shared derivation with CLM-0101 element (iii); the type-specific results):**

- Across the 357 examined relationships, the three products **substantively agreed on the type of negative treatment in only 40 (11%)**; even where all three agreed treatment was negative, "their descriptions often conflict."
- **Incorrect applied labels:** of the relationships each citator labeled negative, 12% (Shepard's), 11% (KeyCite), and 15% (BCite) were incorrect — either not negative at all or the wrong treatment type; incorrectly *described* negative treatments alone were 18 / 11 / 11 cases (6% / 4% / 4% of the 309 clearly negative relationships).
- **Label-vocabulary effects are measurable in the failure pattern:** roughly one-fifth of BCite's missing negative labels trace to its shorter label list (no applicable label existed); labels with no cross-product counterpart produced systematic divergence (ACAN vs "Disagreement Recognized By"; the absence of "not followed" equivalents).
- Scope conditions as in CLM-0101: one study, one coder with ambiguity-filtering and vendor review, one seed sample, negative-treatment identification only. **Not generalized beyond its subjects.**
- **EXPLICITLY EMPTY for CiTO** — no measurement of CiTO's application (annotator consistency, inter-annotator agreement, correctness) exists in the base; the paper reports usage illustrations and that CiTO "has not yet been widely used elsewhere." **EXPLICITLY EMPTY for micropublications** (evaluation deferred by its authors). **EXPLICITLY EMPTY for IBIS** (interior unread; nothing establishable). **Qualitative-only for discourse graphs:** the deployment observed — without controlled measurement — that explicit typed relations "were less frequently present" than nodes, with users relying on indentation and "(often unwritten) convention"; one user's shared graph contained "essentially no discourse relations." Recorded as field observation, not measurement.

# Element (iv) — Documented Costs and Failure Modes (from the sources; not inferred)

- **Typed-relation authoring is the part users skip (SRC-0153, documented):** the designers report "desire paths for smoother and less effortful means of specifying discourse relations"; relation authoring lagged node authoring throughout; grammar maintenance had real documented friction (pattern-editor layout loss called "a real pain point"; requested subtype inheritance absent; the first author personally assisting users with relation patterns). The typed layer — "the thing that makes it a graph" — was the least-adopted part of the system in its own deployment report.
- **Vocabulary size trades against application consistency (SRC-0160, documented):** the short-list product missed labels it had no word for; the long-list products disagreed with each other on which word applied; providers themselves called the determinations "subjective"; and a citator "can be reliable or … idiosyncratic, but they can't be both." The semantic dispute over "distinguished" (versus "distinguishable," versus positive factual-difference references) is documented as a live source of cross-product divergence.
- **Semantic collapse as a designed cost (SRC-0155, documented):** folding interpretation and citation into one `supports` relation buys transitive closure at the price of finer relation semantics — the paper says so itself; and similarity judgments underpinning claim-network normalization are documented as assertions on which "Your 'similarity' may not be my 'similarity'."
- **Author burden without tooling (SRC-0156, documented):** CiTO typing awaits authoring tools ("scope for the development of an ontology-backed tool … that would assist authors"); version churn through v1.3–v1.6 (renamed and deprecated classes) is recorded in the paper itself as revision at an early stage.
- **Early forced typing interferes with work (SRC-0153, citing the gIBIS deployment literature):** users of the classic typed-deliberation tooling "found the ontology of issues, arguments, and positions, helpful … but also wanted ways to integrate this into their work in a more semi-structured way."
- **EXPLICITLY EMPTY for IBIS itself** (interior unread; the gIBIS reception facts are SRC-0153's documentation about the later tool, recorded above as such).

---

# Claim Type (KOS-0003 §3)
**Descriptive** — the vocabularies, their warrant/enforcement postures, the one measured application picture, and the documented costs. No adjudication among vocabulary sizes or enforcement models, and no recommendation.

# Evidence (KOS-0003 §4)
Type: **Empirical** (SRC-0160, element (iii)) and **Historical/Documentary** (the ontology and model papers).
- SRC-0156, SRC-0160 — **interiors READ this session** (directly).
- SRC-0155, SRC-0153 — **interiors READ this session** (structured extraction, grep-verified quotes).
- SRC-0152 — **interior NOT read** (scan without text layer; disclosed); cited at surface level only.

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: **3** — design descriptions from the systems' own papers; the one measurement from a single provider-reviewed study.
- Relevance: **5** — these sources define and (once) measure exactly the typed-relationship practices surveyed.
- Independence: **3** — SRC-0160 independent of the vendors (disputes on file); the rest describe their authors' own designs.
- Quality: **4** — four of five interiors read; quotes verified.
- Limitations: one measured practice, one study, one domain; annotator-consistency evidence absent for every semantic-publishing vocabulary; IBIS at surface only.

# Source Evaluation
As in CLM-0099/0101: the model and ontology papers are authoritative for their own designs and interested in them; SRC-0160 carries the strongest independence posture in the base and prints the vendors' objections; SRC-0152's unread interior confines its use to the catalogued element model.

# Assumptions (KOS-0003 §10)
- **"No surveyed system requires a checkable warrant" is a base-scoped statement** at the depth read — it is not asserted of systems or features outside this base, nor of unread interiors beyond what their surfaces establish.
- **The citator measurement is not generalized** to editorial typing as a class, to other domains, or to the semantic-publishing vocabularies.
- **Vendor design defenses are rationale**, recorded in (ii)/(iv) as vendor statements.

# Reasoning (KOS-0003 §7)
**Descriptive comparison plus one derivation.** The organizing observation — typing is assertion everywhere in this base, with editorial process the only enforcement instance and that instance measured once — follows from the read texts and is stated with its base-scope condition. Risks: (1) **over-extending SRC-0160** — controlled as in CLM-0101; (2) **reading the discourse-graphs relation shortfall as a measurement** — controlled by labeling it field observation; (3) **treating "no warrant requirement" as a defect finding** — controlled by the no-adjudication rule: it is recorded as a description, not a criticism.

# Confidence (KOS-0003 §8)
- **d_approach_described — Level 3 (Moderate):** vocabularies and warrant postures are read directly for four systems (verified quotes); IBIS rests on its surface; the citators' internal procedures are known only from outside.
- **d_stated_rationale_recorded — Level 3 (Moderate):** direct quotation for four; surface for one.
- **d_evidence_of_performance — Level 3 (Moderate):** one careful but single study populates the one cell; the emptiness determinations rest on full readings except IBIS (surface, disclosed).
- **d_documented_costs_failure_modes — Level 3 (Moderate):** richly documented for citators and discourse graphs, self-acknowledged for micropublications and CiTO, empty for IBIS.
- **No Level 5. Everything R0.**

# Limitations
- Does not assert that any vocabulary size or enforcement model is right; does not assert that warrant requirements would have prevented the measured errors (untested anywhere in the base); does not assert anything about IBIS beyond its element model; does not generalize the citator results.
- **Terminological drift (STD-0007), recorded:** *"supports"* in micropublications is a transitive graph relation spanning what Relatio distinguishes as `derived_from`, `supports`, and citation — the shared word is not the shared concept; *"warrant"* in micropublications is Toulmin's (a paraphrase standing in for cited backing), not Relatio's edge-warrant rule; *"argument"* in IBIS (a deliberation element) differs from *"argument"* in micropublications (the whole claim-with-support structure); the citators' treatment phrases are a controlled vocabulary whose members ("distinguished," "questioned") carry contested domain-internal meanings documented in SRC-0160. No source term is translated into Relatio's vocabulary.
- **May not be cited outside Relatio or for any external reliance (R0), regardless of INV-0019's closure state.**

# Alternative Interpretations
1. **Read the base as showing warrant requirements are unnecessary (no one else has them).** Rejected — absence of a practice in nine sources is not evidence against it; and the one measured unwarranted practice shows substantial error, though that is not evidence a warrant would fix it. Both directions are unmeasured; both are refused.
2. **Read the citator disagreement as showing controlled vocabularies fail.** Rejected — one study, one domain, and the documented failure sources include vocabulary *differences* between products, not controlled vocabularies as such.
3. **Read discourse graphs' unauthored relations as user error.** Rejected — the source itself treats it as a design finding about authoring effort ("desire paths"), and the record follows the source.

# Relationships (STD-0004)
- `derived_from` SRC-0152, SRC-0153, SRC-0155, SRC-0156, SRC-0160.
- `supports` FND-0019.
- `part_of` INV-0019.
- The catalogued `related_to` between SRC-0156 and SRC-0160 (typed vocabularies at scale) is exactly the shared-subject relation this claim reads across; unmodified.

# Verification (STD-0006 §7.5 — Specialist disclosure)
**Four of five interiors READ this session:** SRC-0156 and SRC-0160 directly; SRC-0153 and SRC-0155 via structured extraction with grep-verified verbatim quotes. SRC-0152 **NOT read** (page-image scan, no text layer, no OCR available), disclosed and confined to the catalogued element model. The element-(iii) figures are derived from SRC-0160's text directly; nothing transcribed from the brief or scaffold. Everything **R0; not cleared for external reliance regardless of closure.**

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-24|Draft|Created for RQ-0019 (Specialist pass), CLM D of four (warrant: GB-2026-043). Four separable elements recorded and separately graded: **(i)** vocabularies from 3 base relations (discourse graphs) through ~20 predicates (micropublications) and 23 citation-typing properties / 98 classes (CiTO v1.6) to controlled editorial treatment lists of differing lengths (citators); typing is author/annotator/editor ASSERTION in every case — no surveyed system requires or tool-checks a warrant; enforcement, where it exists, is editorial process (Moderate); **(ii)** rationales in register — author-intent capture, transitive-closure economy over finer semantics, minimal-grammar-plus-extension, severity differentiation, vendor short-list defense (Moderate); **(iii)** the one measured practice, derived from SRC-0160: 11% three-way substantive agreement on treatment type, 11–15% incorrect applied negative labels, ~1/5 of BCite misses from label-list gaps, cross-product label mismatches; explicitly empty for CiTO ("not yet widely used"), micropublications (deferred), IBIS (unread); qualitative-only for discourse graphs (relations "less frequently present," one graph with "essentially no discourse relations") (Moderate); **(iv)** documented costs — relation-authoring friction and grammar-maintenance burden, vocabulary-size vs consistency trade, designed semantic collapse for transitivity, author burden without tooling, gIBIS early-formalization interference as documented by SRC-0153; empty for IBIS itself (Moderate). Interiors read: SRC-0153/0155/0156/0160; SRC-0152 not read (disclosed). Both directions of the warrant question left unmeasured and refused. No Level 5; R0. Pending Critical Review and structural validation.|

# End CLM-0102
