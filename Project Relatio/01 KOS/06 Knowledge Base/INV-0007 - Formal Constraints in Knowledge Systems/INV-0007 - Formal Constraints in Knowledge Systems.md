---
title: INV-0007 - Formal Constraints in Knowledge Systems
document_type: Investigation Record
version: 0.4
status: Draft
operational_status: Active
created: 2026-07-12
category:
  - Knowledge Base
  - Knowledge Management & Organizational Design
  - Investigation
parent_documents:
  - KOS-0008 Research Methodology & Investigation Framework
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - SRC-0035 Adler Borys 1996 Two Types of Bureaucracy Enabling and Coercive
  - SRC-0036 Hansen Nohria Tierney 1999 Strategy for Managing Knowledge
  - SRC-0037 Simmons Nelson Simonsohn 2011 False-Positive Psychology
  - SRC-0038 Szollosi et al 2020 Is Preregistration Worthwhile
  - SRC-0039 Meyer Rowan 1977 Institutionalized Organizations Myth and Ceremony
  - SRC-0040 Campbell 1979 Assessing the Impact of Planned Social Change
  - SRC-0041 March 1991 Exploration and Exploitation in Organizational Learning
  - SRC-0042 Ostrom 1990 Governing the Commons Design Principles
  - SRC-0043 Merton 1940 Bureaucratic Structure and Personality
  - SRC-0044 Polanyi 1966 The Tacit Dimension
  - SRC-0045 Timmermans Epstein 2010 A World of Standards
  - CLM-0027 Analytic Flexibility Inflates Error
  - CLM-0028 Enabling vs Coercive Design Governs Effect
  - CLM-0029 Codification Value and Tacit Tradeoff
  - CLM-0030 Formal Structures Can Decouple From Practice
  - CLM-0031 Constraints as Targets Get Gamed
  - CLM-0032 Formalization Biases Toward Exploitation and Can Ossify
  - CLM-0033 Constraints Capture Value When Enabling Fitted Revisable
  - ENT-0005 Enabling vs Coercive Formalization
  - FND-0007 Value and Failure of Formal Constraints
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Investigation
  - Formalization
  - KnowledgeManagement
  - OrganizationalDesign
relationships:
  - type: derived_from
    target: SRC-0035
  - type: derived_from
    target: SRC-0036
  - type: derived_from
    target: SRC-0037
  - type: derived_from
    target: SRC-0038
  - type: derived_from
    target: SRC-0039
  - type: derived_from
    target: SRC-0040
  - type: derived_from
    target: SRC-0041
  - type: derived_from
    target: SRC-0042
  - type: derived_from
    target: SRC-0043
  - type: derived_from
    target: SRC-0044
  - type: derived_from
    target: SRC-0045
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-12
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# INV-0007

# Formal Constraints in Knowledge Systems

## Draft Investigation Record

> Authored using **TPL-0003**; Sources via TPL-0002, Claims via TPL-0001, Entity from KOS-0012 §5.5, Finding via TPL-0004. Seventh research workflow (RQ-0007). **Literature-synthesis question — general evidence, not health/clinical; no individualized-advice concerns.** All **eleven** sources were live-verified this session via WebSearch/WebFetch (eight at authoring; three — **SRC-0043 Merton 1940, SRC-0044 Polanyi 1966, SRC-0045 Timmermans & Epstein 2010** — catalogued during post-review remediation to convert previously-invoked companions/steelman into verified SRCs). Verification status is recorded on each SRC; two full-text PDFs (Adler & Borys; Simmons) were located but not machine-readable, so a few specifics rest on converging secondary summaries and are flagged as such.
>
> **Reflexive-relevance note (per coordinator instruction).** The question bears obviously on Project Relatio itself, which is a governed, formally constrained knowledge system. This investigation answers the *general literature question on its merits* and does **not** conduct a self-review of Project Relatio; applicability is noted briefly in FND-0007 §implications only, and the self-flattering direction of the synthesis is named and guarded (§6).

> **CLOSED 2026-07-20 — formal closure under ADR-GOV-0004 §2 D1 (back-application).** This investigation answered its research question at authoring time (**§4 Findings / Synthesis**); what it lacked were the *formal* closure elements, because the D1 closure convention postdates it. **Acceptance criteria: none apply** — the acceptance-criteria practice began with INV-0010, this record predates it, and no criteria were ever declared for it, so there are none to tick (D1(b)'s stated-reason path). **No research content, claim, confidence level, or finding was altered by this closure; the elements added are additive only.** Maturity `status` remains `Draft` and `operational_status` remains `Active`, matching the model instance **INV-0010** — under this vault's convention "closed" means the inquiry is complete, **not** a maturity promotion and **not** a clearance for external reliance.

---

# 1. Research Question

**Original (verbatim):** "What do the literatures on knowledge-management, research methodology, and organizational/epistemic design say about the value and failure modes of formal constraints in evolving knowledge systems?"

**Refined (Specialist):** Retained as posed, with **clarifying (not redirecting)** disambiguations of three terms (§2). The two-part structure is kept intact: **(a) value** of formal constraints and **(b) failure modes**, across the **three named literatures**, for **evolving** knowledge systems.

*Rationale for the refinement.* The additions are definitional only — fixing what counts as a "formal constraint," what "evolving knowledge system" denotes, and which slices of three very large literatures are load-bearing. None **materially redirects or narrows** what was asked (ROLE-0002 §4.2a): the value/failure duality and all three literatures are answered in full. No Steward pre-confirmation was required; the scope reading is surfaced here and in the review brief for the reviewer/owner to catch.

---

# 2. Scope & Disambiguation

**"Formal constraints"** — explicit, codified rules that govern how knowledge is produced, represented, or validated. Includes: **standards, schemas/ontologies, taxonomies, controlled vocabularies, protocols, preregistration, reporting standards, governance rules, defined roles, and review gates**. Excludes purely informal norms and tacit conventions (these appear only as the *contrast* case, e.g., personalization).

**Three literatures** (deliberately sampled, not exhaustively surveyed):
- **Knowledge management** — codification vs. personalization; tacit/explicit knowledge (Hansen et al.; Polanyi/Nonaka tradition).
- **Research methodology** — researcher degrees of freedom, disclosure/preregistration/reporting standards, and the critique of method-idolatry (Simmons et al.; Szollosi et al.).
- **Organizational / epistemic design** — enabling vs. coercive formalization, institutional decoupling, metric gaming/goal displacement, exploration/exploitation, and design principles for enduring institutions (Adler & Borys; Meyer & Rowan; Campbell; March; Ostrom).

**"Evolving knowledge systems"** — knowledge systems whose content and/or structure change over time and must adapt: scientific fields, organizational knowledge bases, KM systems, and governed knowledge architectures. The "evolving" qualifier makes **ossification/adaptability** (CLM-0032) and **revisability** (CLM-0033) especially load-bearing.

**In scope:** the value case, the four principal failure modes, and the design/governance conditions that reconcile them.
**Out of scope / bracketed:**
- A **complete survey** of any of the three literatures — the investigation selects the **strongest, best-evidenced anchors** (per the coordinator's instruction) rather than covering everything.
- A **self-review of Project Relatio** (reflexive relevance noted, not conducted).
- **Quantified, validated causal recipes** — much of the relevant evidence is theoretical/case-based/simulation; effect sizes are largely unavailable and not invented (§12.1).

---

# 3. Method

Followed the KOS-0003 pipeline (Question → Claims → Assumptions → Evidence → Confidence). Eight sources were located and **live-verified this session** (WebSearch across all eight; WebFetch attempted on two full-text PDFs, which were located but not machine-readable — noted on the relevant SRC/CLM records). Because several anchors are **seminal but conceptual/simulation** works, **§12.1 (no fabrication / no false precision)** governed source handling: the one hard quantitative anchor (Simmons' combined **61%** false-positive rate) is reported at verified precision, per-degree decimals are reported as approximate, and no effect sizes were invented for the theoretical sources.

One entity (**ENT-0005 Enabling vs Coercive Formalization**) is modelled because it is load-bearing: the enabling/coercive design distinction is the **pivot** on which the whole value-vs-failure synthesis turns, and it is a plausibly cross-investigation construct.

```
RQ-0007
  ↓
Sources: SRC-0035 (Adler & Borys enabling/coercive) · SRC-0036 (Hansen codification) ·
         SRC-0037 (Simmons flexibility) · SRC-0038 (Szollosi preregistration critique) ·
         SRC-0039 (Meyer & Rowan decoupling) · SRC-0040 (Campbell's Law) ·
         SRC-0041 (March exploration/exploitation) · SRC-0042 (Ostrom design principles)
  ↓
Entity:  ENT-0005 (Enabling vs Coercive Formalization)
  ↓
Claims:  VALUE      → CLM-0027 error-control · CLM-0028 enabling design · CLM-0029 codification/tacit tradeoff
         FAILURE    → CLM-0030 decoupling · CLM-0031 gaming/goal displacement · CLM-0032 ossification/over-reliance
         SYNTHESIS  → CLM-0033 enabling + fitted + revisable governance
  ↓
Finding: FND-0007
```

---

# 4. Findings / Synthesis

See **[[FND-0007 - Value and Failure of Formal Constraints]]**. In brief:

**(a) Value.** Formal constraints deliver real, demonstrated value: they **control error** by removing undisclosed analytic flexibility (Simmons' 61% simulation; the strongest single quantitative case — CLM-0027); they enable **reuse and scale** through codification where problems are standardized (CLM-0029); and, when designed as **enabling** rather than coercive, they *support* competent work rather than alienating it (CLM-0028). They also confer coordination and legitimacy.

**(b) Failure modes.** Four recur across the literatures: **decoupling / ceremonial compliance** — structures adopted for legitimacy and buffered from real work (Meyer & Rowan — CLM-0030); **gaming / goal displacement** — metrics-as-targets get optimised at the expense of the goal (Campbell's Law; Merton — CLM-0031); **ossification / over-exploitation** — codified constraints bias systems toward exploiting current knowledge and can lock in, a specific danger for *evolving* systems (March; plus method-idolatry, Szollosi — CLM-0032); and the **tacit-knowledge / context-stripping** cost of over-codification (CLM-0029).

**(c) The reconciling variable.** The deciding factor is **not the amount of formalization but its design and governance** (CLM-0028, CLM-0033): constraints that are **enabling** (repairable, transparent, flexible), **locally fitted/congruent**, and **revisable through participatory, multi-level governance** (Ostrom) capture the value while limiting the failure modes. The constraint system must itself be able to **evolve**, and no single formal method is a self-justifying proxy for quality.

**Bottom line.** The literatures do not say formal constraints are good or bad; they say constraints are **valuable but failure-prone**, and the failure modes are **governable by design** — chiefly by making constraints enabling, fitted, and revisable. *(This is stated in the literature's own terms; it is deliberately not restated in Project Relatio's "earns its place… by use, not symmetry or completeness" merit-principle vocabulary, which is the vault's frame rather than a finding of the cited literature — see §6 and FND-0007 §5.)*

---

# 5. Confidence Summary (KOS-0003 §8)

| Claim | Confidence | Note |
|---|---|---|
| CLM-0027 Flexibility inflates error; constraint remedies | **Level 4 (High)** | One rigorous simulation anchor; 61% verified; bounded to error control |
| CLM-0028 Enabling vs coercive design governs effect | **Level 3 (Moderate)** | Seminal but conceptual anchor; empirical support in uncatalogued follow-on; analogical transfer |
| CLM-0029 Codification value / tacit tradeoff | **Level 3 (Moderate)** | Case-based practitioner anchor; no measured optimum |
| CLM-0030 Decoupling / ceremonial compliance | **Level 3 (Moderate)** | Near-consensus mechanism; magnitude unquantified; single catalogued anchor |
| CLM-0031 Gaming / goal displacement | **Level 3 (Moderate)** | Robust directional tendency; illustrative anchor; stakes-dependent |
| CLM-0032 Ossification / over-reliance | **Level 3 (Moderate)** | Interpretive mapping of March's model; a risk, not a measured outcome |
| CLM-0033 Enabling + fitted + revisable governance | **Level 3 (Moderate)** | Cross-domain interpretive synthesis; analogical transfer; Level 5 reserved |
| **FND-0007 synthesis** | **Level 3 (Moderate)** | Capped at its weakest necessary links (the six Moderate claims) |

No claim reaches Level 5. Confidence 5 remains reserved (interpretive/cross-domain synthesis does not warrant it).

---

# 6. Assumptions & Bracketing (KOS-0003 §10)

- **Motivated-reasoning guard (named, per instruction).** The convenient conclusion here is **self-flattering to any governed, formally constrained system — including Project Relatio itself**: "well-designed formal constraints are good." The evidence was read *against* that prior, and the convenient conclusion **did not survive unqualified**. The **failure-mode literature is strong and pointed**: formal structures can be **ceremonial and decoupled** (looking rigorous while not governing real work — directly relevant to any elaborate metadata/standards regime), metrics get **gamed**, and codified constraints can **ossify** an evolving system and be **idolised as a proxy for quality**. The pro-constraint conclusion survives only in its **heavily conditioned** form (enabling + fitted + revisable + earning its place), and every failure-mode claim is retained at equal weight rather than softened. The synthesis (CLM-0033) is graded **Moderate**, not inflated.
- **Selection assumption.** Three vast literatures are represented by **eight anchors**. This is deliberate (strongest-anchor strategy) but means the synthesis could shift if a well-chosen additional source (e.g., red-tape research — Bozeman; Goodhart/Strathern; path-dependence/lock-in) pulled against it. Anchors were chosen for authority and fit, not to engineer the conclusion; still, the reviewer should treat coverage as *representative*, not *exhaustive*.
- **Analogical-transfer assumption (the key limitation).** Adler & Borys (workplace procedures), March (organizational learning), and Ostrom (natural-resource commons) are transferred to *knowledge-system* constraints by analogy. This transfer is made explicit on every affected claim and is the single most contestable move in the investigation.
- **Evidence-type assumption.** Much of the relevant literature is **theoretical, case-based, or simulation**, not RCT/effect-size evidence. Absence of quantified effects is treated as a **limit on precision**, not licence to invent figures (§12.1). Only Simmons supplies a hard number (61%, verified).
- **Bracketed:** an exhaustive survey of each literature; any self-review or audit of Project Relatio; validated causal recipes for constraint design.

---

# 7. Relationships (STD-0004)

- `derived_from` SRC-0035 … SRC-0042.
- `produces` FND-0007; frames CLM-0027 … CLM-0033 and ENT-0005.
- `part_of` the Knowledge Base.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-12|Draft|Seventh research workflow (RQ-0007); literature-synthesis question (general evidence). Eight sources (all live-verified; two full texts not machine-readable), seven claims (three value, three failure-mode, one synthesis), one entity (ENT-0005), one finding (FND-0007). Motivated-reasoning guard (self-flattering-to-governed-systems direction) named and guarded; reflexive relevance to Project Relatio noted but self-review bracketed. Awaiting Critical Reviewer (ROLE-0004) and Knowledge Architect (ROLE-0001).|
|0.2|2026-07-12|Draft|Post-review remediation (Critical Review - RQ-0007). Catalogued three verified sources (SRC-0043 Merton, SRC-0044 Polanyi, SRC-0045 Timmermans & Epstein) — added to references/relationships and the source count. Removed the vault merit-principle vocabulary from the §4 bottom line and attributed it as the vault's frame. Short-title cross-references (STD-0001 §10). No confidence change. (Claim-level remediations recorded on each CLM.)|
|0.3|2026-07-20|Draft|**Formally CLOSED under ADR-GOV-0004 §2 D1 (closure-convention back-application).** D1 bar assessed: **(a)** explicit RQ answer — satisfied at authoring in §4 Findings / Synthesis; **(b)** acceptance criteria — **none apply**, stated-reason path (the criteria practice began at INV-0010; this record predates it and none were ever declared); **(c)** closure banner — added, dated 2026-07-20; **(d)** frontmatter — matches the model instance INV-0010, which holds `status: Draft` / `operational_status: Active` at closure (no Draft→Adopted closure step exists in this vault, and STD-0005's vocabulary has no distinct closed-state value). **No research content altered** — no claim, confidence level, assumption, or finding touched; closure elements are purely additive. Also corrected this record's version-drift instance under **GB-2026-028** (frontmatter read 0.1 against a 0.2 revision-history row; both now coherent at 0.3).|
|0.4|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End INV-0007
