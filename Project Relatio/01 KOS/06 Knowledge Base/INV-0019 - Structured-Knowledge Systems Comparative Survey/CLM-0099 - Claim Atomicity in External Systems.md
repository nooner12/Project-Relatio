---
title: CLM-0099 - Claim Atomicity in External Systems
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
  - SRC-0152 Kunz and Rittel 1970 Issues as Elements of Information Systems IBIS
  - SRC-0153 Chan et al 2024 Steps Towards an Infrastructure for Scholarly Synthesis
  - SRC-0154 Groth Gibson Velterop 2010 The Anatomy of a Nanopublication
  - SRC-0155 Clark Ciccarese Goble 2014 Micropublications
  - FND-0019 Structured-Knowledge Systems Survey Synthesis
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - KnowledgeSystems
  - ClaimAtomicity
relationships:
  - type: derived_from
    target: SRC-0152
  - type: derived_from
    target: SRC-0153
  - type: derived_from
    target: SRC-0154
  - type: derived_from
    target: SRC-0155
  - type: supports
    target: FND-0019
  - type: part_of
    target: INV-0019
confidence:
  - component: a_approach_described
    level: 3
    label: Moderate
  - component: a_stated_rationale_recorded
    level: 3
    label: Moderate
  - component: a_evidence_of_performance
    level: 3
    label: Moderate
  - component: a_documented_costs_failure_modes
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "two of four source interiors read (SRC-0153, SRC-0155); SRC-0152 scanned/unreadable and SRC-0154 access-blocked, both disclosed; not cleared for external reliance"
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

# CLM-0099

# Claim Atomicity in External Systems (CLM A)

## Draft Claim Record

---

# Claim
> **The surveyed systems individuate a claim in three distinct ways — by formalized assertion (nanopublication), by argumentative role (micropublication: the single principal statement an argument argues), and by author judgment under no stated rule (discourse graphs) — and none of the four enforces its split line by tooling.** Where the split line is defined at all, it is defined structurally, not operationally: no surveyed source states a procedure for deciding whether a candidate statement is one claim or two. Context loss under isolation is a named design concern in the literature itself: the micropublications model exists in explicit response to what its authors document as statement-based models' loss of evidential and qualifying context, and the discourse-graphs deployment observed "non-atomic" authoring in the field when no rule governed the split.

---

# Element (i) — Approach (descriptive)

Where each surveyed system puts the split line, and what governs it:

- **Nanopublication (SRC-0154 — interior NOT read; recorded from the catalogued surface and from SRC-0155's read interior):** the unit is a **single formalized scientific assertion** packaged with provenance and publication metadata, serialized as RDF named graphs. SRC-0155 quotes the nanopublication guidelines' own definition — a layer on RDF-encoded data providing "the identification of individual scientific assertions within a dataset" with provenance assignable to each assertion. The split line falls at the individual machine-formalized assertion; formalization is required by construction.
- **Micropublication (SRC-0155 — interior read):** the unit is an **argument**, whose principal statement is the claim: "A Claim is the single principal Statement arguedBy a Micropublication." The minimal micropublication is "a statement with its attribution"; the maximal is a statement with its complete supporting argument (evidence, methods, discussion, challenges). Claims are natural-language statements — hedges and qualifiers retained — with formalization "an optional curatorial step." Support is structured as a directed acyclic graph rooted at the claim. What counts as one assertion is thus fixed by argumentative role (one principal claim per argument), not by a granularity rule; any attributed statement may be formalized as a citable claim.
- **Discourse graphs (SRC-0153 — interior read):** the units are **question, claim, evidence, and source nodes** with claims "as the central unit," deliberately more granular than documents. **The paper states no rule for what constitutes one claim or one evidence node** — individuation is by the author's annotation act (the design intent was that factoring notes into nodes should feel "similar to highlighting or annotating"), and users themselves invented finer distinctions in the field (e.g., higher-level conclusions versus "more atomic" propositions). One evidence node is bound to one source via a citekey — a mechanism, not a stated rule.
- **IBIS (SRC-0152 — interior NOT read; recorded from the bibliographic surface only):** deliberation is decomposed into **issues, positions, and arguments** — the unit is the element of deliberation, not the assertion of a finding. Nothing beyond this element model is asserted here, because nothing more is establishable without the interior.
- **What happens to context when a claim is isolated** is answered differently by design family: nanopublications carry provenance and descriptive tags but — as SRC-0155 documents — not the argumentative support; micropublications carry the support graph precisely so isolation does not sever the claim from its evidence; discourse graphs attach methodological context to evidence nodes in practice only when authors populate them (see element (iv)).

# Element (ii) — Stated Rationale (design-intent register ONLY)

- **Nanopublication:** at the level the surface and citing literature establish, the stated purpose is making individual scientific assertions identifiable, citable, and machine-readable with attached provenance — presented in the guidelines (as quoted by SRC-0155) chiefly for data integration across curated datasets.
- **Micropublication (SRC-0155):** designed for "representing the key arguments and evidence in scientific articles" and for layering annotations and formalizations on full-text papers; the value proposition its authors state is enabling "individual statements in the literature to be cited and referenced directly … and grounded in their supporting evidence," reducing the labor of checking a claim's support. The natural-language requirement is argued from adoption: formal-language-only requirements are "a potential barrier to adoption," and "structured digital abstracts have faltered" for incentive and tooling reasons.
- **Discourse graphs (SRC-0153):** the stated diagnosis is a "fundamental mismatch" between synthesis information needs and the document-centric data model; the granular claims-and-evidence model is designed so synthesis-relevant units are directly addressable, with users authoring "a shareable discourse graph as a natural byproduct" of note-taking they already do.
- **IBIS (SRC-0152, surface only):** a semi-formal structure for deliberation around wicked planning problems — the design intent recorded at catalog level; no interior-level rationale is asserted.

# Element (iii) — Evidence of Performance (measured, including absence)

**EXPLICITLY EMPTY for three of the four systems, and qualitative-only for the fourth:**

- **Nanopublication: EMPTY.** No measurement of the nanopublication model performing as designed exists anywhere in this base. (SRC-0154's own interior was not readable this session; whether it contains an evaluation is unknown, and nothing is asserted about it.)
- **Micropublication: EMPTY, by the paper's own statement.** SRC-0155 validates by use-case analysis and hand-built worked examples; its authors state that "an evaluation of the model in this context will be presented in a forthcoming article." The quantitative figures the paper cites (reproducibility rates, citation-distortion findings) are third-party motivation, not measurements of the model.
- **Discourse graphs: NO controlled measurement; qualitative deployment observation only.** SRC-0153 reports ~2.5–3 years of research-through-design deployment (48 direct participants; an estimated ~30 daily active users; a 41-response usage survey; N=5 interviews; N=4+1 graph exports averaging 1.4k nodes in the first year), with self-reported benefits for synthesis, retrieval, and research training. The paper contains no experiment, no comparison condition, and no outcome metric; its analysis is interpretive and primarily by the first author, who is also the designer and a subject. This is recorded as deployment experience, not as evidence that the atomicity design performs as intended.
- **IBIS: EMPTY.** Interior unread; no measurement is establishable from the surface, and none is asserted.

# Element (iv) — Documented Costs and Failure Modes (from the sources; not inferred)

- **Context loss in statement-based models, documented by SRC-0155 (its central critique):** "Nanopublications model only the indicated statement"; none of the statement-based models it examines (nanopublications, SWAN, BEL) "provide a means to build claim networks of arbitrary depth" or to trace claims to underlying empirical evidence "because they do not represent it"; the nanopublication "Support" graph is descriptive filtering metadata, "not intended to represent argumentative support or evidence." Its historical example (the malaria-vector case) documents that an isolated statement without its evidence "could not have motivated reasoned belief" while the question was live.
- **Formalization burden, documented by SRC-0155:** the requirement that statements be expressed in formal language is "likely an impediment" to direct use on articles and "a potential barrier to adoption"; forced translation into formal language "can do violence to the natural language presentation."
- **Non-atomic authoring in the field, documented by SRC-0153:** the deployment observed nodes with undefined abbreviations and unresolved references, and evidence nodes that were often "empty" placeholders lacking descriptions or methodological links — atomicity and self-containedness failing in practice where no rule and no tooling enforced them. SRC-0153 also documents (citing the gIBIS deployment literature) that early-imposed formal structure "can interfere with the very work" it supports, with gIBIS users wanting semi-structured "proto-nodes."
- **Micropublication's own costs, documented in SRC-0155:** the model's richness is answered with an explicit incremental-adoption escape hatch ("you do not have to buy the whole package"); annotation effort is acknowledged and argued to be repaid in utility — an argument, not a measurement; and for the predecessor SWAN model, the paper records that per-pair inconsistency labelling "was the task of the knowledge base curator," a design its authors contrast with the micropublication model's curator-free "scalable" collaborative ecosystem — the scalability cost of the curator design is the authors' contrast, recorded here as such.
- **IBIS: EXPLICITLY EMPTY** — no cost or failure mode of IBIS is documented in the readable base (the gIBIS reception facts above are documented by SRC-0153 about the *later tool deployment*, and are recorded there).

---

# Claim Type (KOS-0003 §3)
**Descriptive** — where each system's split line falls, what its documentation says that is for, what was measured, and what the sources record about costs. No system is ranked; no design is endorsed.

# Evidence (KOS-0003 §4)
Type: **Historical/Documentary** (model papers, read where accessible) and **Experiential** (SRC-0153's deployment reports, recorded as such).
- SRC-0155 — **interior READ this session** (publisher full text; structured extraction with grep-verified verbatim quotes).
- SRC-0153 — **interior READ this session** (arXiv full text; structured extraction with grep-verified verbatim quotes).
- SRC-0154 — **interior NOT read** (publisher access blocked by an anti-bot challenge; no archived or repository full text located). Supports only what its catalogued surface and SRC-0155's read interior establish, and that is all it is cited for.
- SRC-0152 — **interior NOT read** (the eScholarship PDF is a scan with no text layer; no OCR tooling available this session). Supports only the element model recorded at cataloguing, and that is all it is cited for.

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: **3** — the two read interiors are the systems' own defining papers; the two unread systems rest on weaker surfaces.
- Relevance: **5** — these are exactly the atomicity-defining documents of the surveyed systems.
- Independence: **2** — each model paper describes its authors' own design; SRC-0153's deployment observations are by the system's designers; SRC-0155's critique of nanopublications is a rival model's critique and is recorded as such.
- Quality: **3** — read interiors with verified quotes; unread interiors disclosed and confined.
- Limitations: no independent evaluation of any of these systems exists in the base; the inter-model critique is partisan by construction.

# Source Evaluation
SRC-0155 and SRC-0153 are authoritative for their own models' definitions and their own documented observations; both are interested parties in their models' favor, and SRC-0155 is additionally an interested party *against* statement-based models — its critique is recorded as documented critique, not as adjudicated fact. SRC-0154 and SRC-0152 are catalogued records with unread interiors; their systems' descriptions are pitched at the level the accessible surfaces support.

# Assumptions (KOS-0003 §10)
- **The inter-model tension is carried as a tension** (the catalogued `contrasts_with` between SRC-0154 and SRC-0155): SRC-0155's account of nanopublications is the record of what one source documents, not this investigation's verdict on nanopublications.
- **Unread-interior confinement:** nothing about SRC-0152's or SRC-0154's interior content is asserted; per INV-0019 §3.2, each supports only what its surface or the citing literature establishes.
- **Deployment experience ≠ performance evidence:** SRC-0153's observations are recorded in element (iii) as qualitative and in element (iv) where the paper itself documents failure, never as measurement.

# Reasoning (KOS-0003 §7)
**Descriptive comparison without adjudication.** The three-way individuation taxonomy (formalized assertion / argumentative role / author judgment) is a summary of what the read and catalogued sources state, not an evaluative ordering. Reasoning risks: (1) **adopting SRC-0155's critique as fact** — controlled by attributing every critical statement to its source and recording the model-design tension as a tension; (2) **treating deployment anecdote as measurement** — controlled by the (iii)/(iv) separation; (3) **over-describing the two unread systems** — controlled by surface confinement and by grading down.

# Confidence (KOS-0003 §8)
- **a_approach_described — Level 3 (Moderate):** the two central model descriptions rest on read interiors with verified quotes (which would support High), but the element spans four systems and two of them (IBIS, nanopublication) rest on unread interiors; the mixed posture caps the element at Moderate.
- **a_stated_rationale_recorded — Level 3 (Moderate):** same structure — direct quotation for two systems, surface-level recording for two.
- **a_evidence_of_performance — Level 3 (Moderate):** the emptiness determinations for micropublications and discourse graphs rest on full readings (the former's deferral is the paper's own statement); the nanopublication emptiness is within-base only, since its interior could not be checked. The element asserts absence *within this base*, and that is what the grade covers.
- **a_documented_costs_failure_modes — Level 3 (Moderate):** the documented costs are verbatim-verified from two read interiors, but they are the documentation of interested parties (a rival model's critique; a design team's own deployment reflections), and for two systems the element is empty rather than populated.
- **No Level 5. Everything R0.**

# Limitations
- Asserts nothing about how these systems perform outside what element (iii) records; asserts nothing about IBIS or nanopublication interiors; does not adjudicate the nanopublication–micropublication design dispute; does not generalize any system's approach beyond its documented domain (biomedical publishing; scholarly synthesis tooling; planning deliberation).
- **Terminological drift (STD-0007), recorded:** *"claim"* is defined differently in each source — micropublications define Claim formally as the principal Statement of an argument (with Statement = declarative Sentence); discourse graphs leave "claim" undefined and central; nanopublications' unit is an *assertion* in the RDF sense. None of these is Relatio's Claim Record, and no source's term is translated into Relatio's vocabulary. Micropublications' Toulmin-derived *"warrant"/"backing"* usage (a paraphrase and its cited source) is likewise not Relatio's edge-warrant concept.
- **May not be cited outside Relatio or for any external reliance (R0), regardless of INV-0019's closure state.**

# Alternative Interpretations
1. **Read SRC-0155's critique as establishing that nanopublications fail.** Rejected — the critique is one model's documented case against another; recording it in (iv) is not adopting it, and no adjudication is made.
2. **Read SRC-0153's deployment as evidence the discourse-graph atomicity design works.** Rejected — the paper contains no controlled measurement, its analysis is interpretive by the designers, and its own text documents non-atomic authoring in the field.
3. **Infer that IBIS has no individuation rule because none is recorded here.** Rejected — the interior was not read; absence of a recorded rule is a fact about this survey's access, not about the paper.

# Relationships (STD-0004)
- `derived_from` SRC-0152, SRC-0153, SRC-0154, SRC-0155.
- `supports` FND-0019.
- `part_of` INV-0019.
- The catalogued `contrasts_with` between SRC-0154 and SRC-0155 is relied on as context and not modified.

# Verification (STD-0006 §7.5 — Specialist disclosure)
**Mixed posture, disclosed per source.** SRC-0155 and SRC-0153 interiors were **READ this session** — full texts retrieved (publisher HTML; arXiv PDF), read via structured extraction, with every load-bearing quotation grep-verified verbatim against the retrieved text. SRC-0154's interior was **NOT read**: the publisher page is behind an anti-bot challenge that could not be passed this session, and no Wayback, repository, or aggregator full text exists (checked); it is cited only at surface level and through SRC-0155's read interior. SRC-0152's interior was **NOT read**: the eScholarship copy is a page-image scan with no extractable text layer and no OCR tooling was available; it is cited only at the catalogued surface level. Everything **R0; not cleared for external reliance regardless of closure.**

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.2|2026-07-24|Draft|**Critical Review – RQ-0019 remediation (Flag F1, determinate).** Element (iv) SWAN entry reworded: the curator design's scalability cost is now attributed as the SRC-0155 authors' own contrast (per-pair curator labelling vs the curator-free "scalable" collaborative ecosystem) rather than asserted as a documented non-scalability finding. **No grade changed; no other content changed.**|
|0.1|2026-07-24|Draft|Created for RQ-0019 (Specialist pass), CLM A of four (warrant: GB-2026-045). Four separable elements recorded and separately graded: **(i)** three distinct individuation approaches — formalized assertion (nanopublication), argumentative role (micropublication's single principal Statement, minimal form statement+attribution, DAG support), author judgment with no stated rule (discourse graphs; users invented finer granularity in the field), IBIS element model at surface level; no system enforces its split line by tooling (Moderate); **(ii)** stated rationales in their own register — identifiability/data integration, direct citation of statements grounded in evidence, synthesis-granularity mismatch diagnosis (Moderate); **(iii)** EXPLICITLY EMPTY for nanopublication, micropublication (evaluation deferred by the paper's own statement), and IBIS; qualitative-only deployment observation for discourse graphs, recorded as such (Moderate); **(iv)** documented costs — SRC-0155's statement-based-model critique (context loss, no claim networks of arbitrary depth, formalization impediment, structured-abstract failure), SRC-0153's observed non-atomic authoring and empty evidence placeholders plus the gIBIS early-formalization interference it cites, micropublication's own acknowledged complexity/annotation burden and SWAN curator non-scalability; explicitly empty for IBIS (Moderate). Interiors READ: SRC-0153, SRC-0155 (grep-verified extraction). NOT read, disclosed: SRC-0152 (scan, no text layer), SRC-0154 (access-blocked). Inter-model critique carried as tension, not verdict. No Level 5; R0. Pending Critical Review and structural validation.|

# End CLM-0099
