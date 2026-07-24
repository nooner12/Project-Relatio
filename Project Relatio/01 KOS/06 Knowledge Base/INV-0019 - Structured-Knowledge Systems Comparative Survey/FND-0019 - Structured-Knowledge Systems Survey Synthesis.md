---
title: FND-0019 - Structured-Knowledge Systems Survey Synthesis
document_type: Finding Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-24
category:
  - Knowledge Base
  - Finding
  - Knowledge Systems
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0019 Structured-Knowledge Systems Comparative Survey
related_documents:
  - CLM-0099 Claim Atomicity in External Systems
  - CLM-0100 Expert-to-Lay Register in External Systems
  - CLM-0101 Source-to-Claim Mapping in External Systems
  - CLM-0102 Warranted Typed Relationships in External Systems
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Finding
  - KnowledgeSystems
relationships:
  - type: derived_from
    target: CLM-0099
  - type: derived_from
    target: CLM-0100
  - type: derived_from
    target: CLM-0101
  - type: derived_from
    target: CLM-0102
  - type: part_of
    target: INV-0019
confidence:
  - component: atomicity_picture
    level: 3
    label: Moderate
  - component: register_picture
    level: 3
    label: Moderate
  - component: mapping_picture
    level: 3
    label: Moderate
  - component: typed_relationships_picture
    level: 3
    label: Moderate
  - component: measured_evidence_confined_to_two_studies
    level: 3
    label: Moderate
  - component: unread_interior_coverage
    level: 2
    label: Low
reliance_tier: R0
reliance_note: "nine-source base; seven interiors read, two not (disclosed); two empirical studies only; CLM B single-domain; not cleared for external reliance"
review_cycle: 6
review_date: 2027-01-24
last_reviewed: 2026-07-24
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-24
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# FND-0019

# Structured-Knowledge Systems Survey Synthesis

## Draft Finding Record

---

# 1. Finding (the honest picture across the four design problems)

> **On this nine-source base, established structured-knowledge systems answer the four design problems chiefly by DESIGN rather than by demonstrated performance: the approaches are articulate, the rationales are explicit, the measured evidence is confined to exactly two studies — an adherence audit of one lay-summary standard and an accuracy study of three legal citators — and both measurements found the deployed practice falling far short of its design; everywhere else, evidence of performance is ABSENT, and the sources' own documentation of costs and failure modes points repeatedly at the same pressure points: formalization burden, unenforced standards, unauthored relation layers, and editorial subjectivity rendered as fact.**

Per design problem, at the grade each claim earned:

- **Atomicity (CLM-0099, all elements Moderate).** Three individuation approaches — formalized assertion (nanopublication), argumentative role (micropublication's single principal Statement), and author judgment under no stated rule (discourse graphs) — with IBIS's issue/position/argument model recorded at surface level. **No surveyed system states an operational procedure for the split line, and none enforces it by tooling.** Measured performance: none. Documented failure: context loss in statement-based models (documented by their rival), formalization as an adoption impediment, and "non-atomic" authoring observed in the one field deployment.
- **Expert-to-lay register (CLM-0100, elements High/High/Moderate/Moderate — the base's strongest descriptive footing and its single-domain limit).** One practice in the base addresses the problem at all: medicine's mandated parallel plain-language summary, prescribed item-by-item (PLEACS) with a controlled expert-side certainty vocabulary (GRADE) to be translated for lay readers. The one measurement (1738 summaries): **zero full adherence, 57% average, and 0.7% on the certainty item — the register's epistemic core is precisely what failed hardest.** **This picture is single-domain (medicine, one organization) and is not presented as a general practice.**
- **Source-to-claim mapping (CLM-0101, all elements Moderate).** A capture-depth spectrum from whole-work typed citation (CiTO), through result-anchored evidence nodes (discourse graphs), to full support-graph resolution designed for traversal to data and methods (micropublications). The one measured mapping practice — the legal citators — showed three mature products **agreeing substantively on only 11% of examined relationships and individually failing on 33%/38%/72% of clearly negative treatments, while rendering every mapping as unqualified fact.** Designed capture was also observed unpopulated in practice (empty evidence placeholders).
- **Warranted typed relationships (CLM-0102, all elements Moderate).** Vocabularies from three relations to ~a hundred classes; **in every surveyed system the applied type is an assertion — no system requires or tool-checks a warrant.** The only enforcement instance is editorial process, measured once with the disagreement figures above; the one deployment report shows the typed-relation layer is what users skip when authoring costs anything.

**Where the evidence exists and where it is absent (the survey's central meta-result, expected at opening and confirmed):** element (iii) is populated for exactly two practices — Cochrane PLS adherence (SRC-0159) and citator accuracy (SRC-0160) — and **explicitly empty for every semantic-publishing and argumentation system in the base** (nanopublications: nothing; micropublications: evaluation deferred by its own authors; CiTO: "not yet widely used"; discourse graphs: qualitative deployment only; IBIS: unread interior, nothing establishable). Neither empirical study generalizes beyond its subjects, and neither is used to do so anywhere in this investigation.

# 2. Supporting Claims

- **CLM-0099** — atomicity: the three individuation approaches, the absence of operational split rules and enforcement, the documented context-loss and formalization costs.
- **CLM-0100** — register: the mandated-parallel-summary approach, its governing standard and certainty vocabulary, the adherence measurement, the single-domain bracket.
- **CLM-0101** — mapping: the capture-depth spectrum, the citator accuracy measurement and its scope conditions, the documented subjectivity-rendered-as-fact and unpopulated-capture failures.
- **CLM-0102** — typed relationships: the vocabulary inventory, the typing-is-assertion posture across the base, the type-agreement and label-error figures, the documented authoring-friction and vocabulary-size trades.

# 3. Confidence (KOS-0003 §8)

Native `Level N (Label)`, per component, never averaged; **grades no stronger than the weakest necessary components; no Level 5, and no Level 4** (the two High components in CLM-0100 are descriptive elements; every synthesis component here also rests on Moderate elements and is capped accordingly):

- **atomicity_picture — Level 3 (Moderate):** rests on CLM-0099's four Moderate elements.
- **register_picture — Level 3 (Moderate):** CLM-0100's (i)/(ii) are High, but this component necessarily also rests on its Moderate (iii)/(iv).
- **mapping_picture — Level 3 (Moderate):** rests on CLM-0101's four Moderate elements.
- **typed_relationships_picture — Level 3 (Moderate):** rests on CLM-0102's four Moderate elements.
- **measured_evidence_confined_to_two_studies — Level 3 (Moderate):** the absence determinations rest on full readings for seven sources; the base's two unread interiors (below) mean within-base absence is asserted with one unreadable cell, and absence beyond the base is not asserted at all.
- **unread_interior_coverage — Level 2 (Low):** what this survey can say about IBIS and the nanopublication paper specifically rests on bibliographic surfaces and citing literature only — graded Low deliberately, the disclosed cost of two inaccessible interiors (a scan without a text layer; an access-blocked publisher page).

Everything **R0**.

# 4. Scope & Limitations (base coverage limits, recorded as limits)

- **Nine sources do not represent four fields.** The base holds one argumentation-modelling source (1970, unread interior), one contemporary synthesis-infrastructure report, three semantic-publishing sources (one unread), three evidence-synthesis sources (one domain, one organization), and one citation-practice study (one domain). Under-coverage is disclosed, not compensated for; nothing outside the base was consulted for any claim element.
- **CLM B rests on a single domain (medicine).** The mandated-parallel-summary picture is Cochrane's; no generality across domains is asserted anywhere.
- **The two empirical studies bind only their subjects.** SRC-0159 supports claims about Cochrane PLS adherence to PLEACS in 2013–2015; SRC-0160 about three named citators on one sample. They are the whole of element (iii) in this investigation and carry none of it beyond their scope.
- **Two interiors were not read** (SRC-0152 scan; SRC-0154 blocked), each disclosed in the claims that cite them and graded down where load-bearing.
- **Absence-of-evidence findings are within-base findings.** "No measurement exists in this base" is what is asserted; whether measurements exist elsewhere was not surveyed.
- **No adjudication, no ranking, no recommendation.** Disagreements (the nanopublication–micropublication design dispute; the citators' mutual disagreement; the PLEACS item-count divergence between SRC-0159 and the archived standard) are recorded as disagreements at the grade each side earns.
- **Terminological cautions for any reader of this finding (STD-0007):** "claim," "assertion," "statement," "argument," "warrant," "support," "evidence," "citation," "quality," and "mandatory" are each used in source-specific senses recorded in the four claims; a shared word is not a shared concept, and none of these terms has been translated into Relatio's vocabulary. Read the claims' drift notes before citing any element.
- **Adoption and persistence are OUT OF SCOPE as claims.** Observations of that kind surfaced by the sources are recorded in INV-0019's Reserved Reflexive Section and routed to GB-2026-048; nothing of that kind is asserted here.
- **May not be cited outside Relatio or for any external reliance (R0), regardless of INV-0019's closure state.**

# 5. Relationships (STD-0004)

- `derived_from` CLM-0099, CLM-0100, CLM-0101, CLM-0102.
- `part_of` INV-0019.
- The subgraph this finding synthesizes: four claims over nine catalogued sources; **no entity, no timeline edge, no new relationship type; SRC-0161 unconsumed; GB-2026-047 untouched.**

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-24|Draft|Created for RQ-0019 (Specialist pass). Synthesizes CLM-0099…CLM-0102 across the four design problems: approaches articulate, rationales explicit, **measured evidence confined to exactly two studies** (PLS adherence; citator accuracy), both finding deployed practice far short of design (zero full adherence / 57% / 0.7% certainty item; 11% three-way agreement / 33–72% failure rates); element (iii) explicitly empty for every semantic-publishing and argumentation system; recurrent documented pressure points — formalization burden, unenforced standards, unauthored relation layers, editorial subjectivity rendered as fact. Six components: four per-problem pictures Moderate, measured-evidence-scarcity Moderate, unread-interior coverage Low (the disclosed cost of SRC-0152/SRC-0154). Grades capped at weakest necessary components; **no Level 5, no Level 4**. Base limits recorded as limits (nine sources; CLM B single-domain; two studies bind only their subjects; absence findings within-base). Adoption/persistence routed to the reflexive section and GB-2026-048, not asserted here. R0; not cleared for external reliance regardless of closure. Pending Critical Review and structural validation.|

# End FND-0019
