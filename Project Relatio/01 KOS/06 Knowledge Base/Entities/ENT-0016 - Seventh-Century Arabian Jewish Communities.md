---
title: ENT-0016 - Seventh-Century Arabian Jewish Communities
document_type: Entity Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-24
category:
  - Knowledge Base
  - Entity
  - Community
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0004 Ontological Framework & Reality Modeling System
related_documents:
  - ADR-GOV-0012 - Entity Resolution, Projection, and the influenced_by Relation
  - INV-0018 Islam Origins and Abrahamic Relationships
  - CLM-0096 Islam Relationship to Judaism
  - FND-0018 Islam Origins and Abrahamic Relationship Shape
  - ENT-0014 Rabbinic Judaism
  - ENT-0015 Islam
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Community
  - Judaism
  - WorldReligionsTimeline
rendering_class: community
attestation_claims:
  - CLM-0096
  - FND-0018
attestation_window: "7th c. CE - attested through the period of documented contact; beginning and terminus not dated by the record"
attestation_uncertainty: moderate
relationships:
  - type: projects_to
    target: ENT-0014
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-24
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ENT-0016

# Seventh-Century Arabian Jewish Communities

## Draft Entity Record

---

# 1. Identification
**Community:** the Jewish communities present in seventh-century Arabia — in the Ḥijāz and more widely — that stood in documented engagement with the earliest Muslim community (CLM-0096).

**Region / period:** the Arabian peninsula, seventh century CE.

**The name is deliberately generic, and that is the finding.** CLM-0096 §(c) records that the RQ-level wording "Judaism" was *correct* precisely because naming a seventh-century Arabian Jewish entity more specifically would over-specify a contested object — and that "the over-specification the RQ avoided must not be re-introduced at the edge layer." This record honours that: it names a **population in a place and a century**, and asserts nothing about that population's character.

**Internal plurality held inside the entity, not resolved:** **how rabbinised these communities were, and how connected to the wider Jewish world, is an open scholarly question that the INV-0018 base does not cover** (CLM-0096 element (i); `arabian_jewish_community_character` graded **Low**). That question is **not answered here and is not answerable from the closed record.** No sub-community, tribe, or regional formation is split out.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious community.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **rendering_class:** `community` — this is a **regionally and temporally bounded population**, not a tradition. It is the resolution INV-0018 demonstrated the entity layer could not represent: **ENT-0012 Second Temple Judaism fails the chronological-coherence check** (`range_end_year: 70` against a seventh-century relationship) and **ENT-0014 Rabbinic Judaism over-specifies**. Minted under **ADR-GOV-0012 D8** on the warrant of INV-0018's closed record; **no new investigation was opened, and none of INV-0018's records was revised.**

# 3. Attestation window (NOT a founding date — ADR-GOV-0012 D4)
- `attestation_claims`: **CLM-0096** (the documented-engagement finding and the recorded entity gap) and **FND-0018** (`entity_target_gaps`, Moderate — the finding that no existing entity would have been an honest target).
- **Window — `7th c. CE`.** Derived from **CLM-0096 element (i)**: Jewish communities present in seventh-century Arabia, in documented engagement with the earliest Muslim community, whose own emergence CLM-0095 places in the seventh century at **Level 4 (High)**. **This states WHEN THE RECORD ATTESTS THIS COMMUNITY — through the period of contact — and NOT when it began or ended.** The closed record dates neither bound, and neither is invented here.
- **What was deliberately NOT used to widen the window.** CLM-0096 element (i) also reports a Judaising Ḥimyarite royal house in South Arabia "in the centuries before Islam." That is a **parametric general-reference statement** which CLM-0096's §Verification marks as **not live-verified and not drawn from any source interior**, and which the record does not bound in time. It is recorded here as context and **does not extend the attestation window**; an unbounded prior presence is not a bound.
- **`attestation_uncertainty: moderate`** — inherits the **weakest TEMPORALLY RELEVANT** component of the warranting records: **`documented_engagement_with_judaism`, Level 3 (Moderate)**, which is the component grading whether the engagement (and therefore the contact period) is attested. **Excluded as non-temporal**, per the STD-0002 §11 v1.11 rule this standard extends: `arabian_jewish_community_character` (**Low** — it grades *what these communities were like*, not *when* they are attested), `relationship_type_influence_not_descent` (grades the kind of relationship), and `entity_target_adequacy` (grades a modelling fit). **The Low component is not hidden by that exclusion** — it governs this entity's *characterisation*, which is why §1 states the rabbinisation question as unresolved rather than resolving it.
- **No positioning bounds, by rule and by honesty.** This record carries no `range_start_year` / `range_end_year` / `range_uncertainty` and can carry none (STD-0002 §11 v1.13): a bar drawn between two coordinates would assert a beginning and an end the record does not have.

# 4. Projection (projects_to — NON-EVIDENTIAL, ADR-GOV-0012 D5)
- `projects_to` **ENT-0014 Rabbinic Judaism** — **a rendering instruction, and nothing else.** It says: *for display, re-anchor this node to the tradition layer here.*
- **This is expressly NOT an assertion that these communities were rabbinic.** CLM-0096 records the opposite epistemic position — the degree of rabbinisation of seventh-century Arabian Jewish communities is an **open question the base does not cover**, and it is exactly why an *evidential* edge to ENT-0014 was refused. `projects_to` carries **no qualifier, no warrant, and no confidence** because it makes no such claim; it is the mechanism ADR-GOV-0012 D5 created so that a rendering need can never quietly become a historical one.
- **Why ENT-0014 and not ENT-0012.** ENT-0012 Second Temple Judaism ends at 70 CE and is chronologically incapable of standing in any seventh-century relationship (CLM-0096 §(c)). ENT-0014 is **the only chronologically live Jewish tradition entity in the vault**, so it is the only honest re-anchor point for display. Chronological liveness is the whole of the reason; no characterological claim is smuggled in with it.
- **Single target.** `projects_to` permits multiple targets where a node honestly projects to more than one; this one does not.

# 5. Relationships (STD-0004)
- `projects_to` ENT-0014 (non-evidential rendering projection).
- **No `derived_from` source edge, deliberately.** CLM-0096's five cited source interiors are **parametric/unread**, and the milieu particulars stated in its own voice are disclosed there as **parametric general-reference statements not drawn from any source interior**. A `derived_from` edge from this record to those sources would assert a source-interior derivation that did not occur. The warrant runs through the **graded records** (`attestation_claims`), which carry the disclosure with them.
- The `influenced_by` edge from **ENT-0015 Islam** to this entity sits on ENT-0015 (the edge lives on the receiving tradition), warranted by CLM-0096 and FND-0018 with CLM-0096 as the recorded not-descent determination.

# 6. Limitations
- This record asserts that a Jewish population existed in seventh-century Arabia and was in documented engagement with the earliest Muslim community. It asserts **nothing** about that population's rabbinisation, institutions, internal composition, origin, or fate.
- It creates **no** claim, opens **no** investigation, and moves **no** confidence grade. Everything remains **R0** and **not cleared for external reliance** (FND-0018 §5), and this entity inherits that posture from the records that warrant it.
- Its attestation window is a determination **on this base**. A base containing the missing Arabian-Judaism literature and documentary evidence could move it in either direction.

# 7. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-24|Draft|Created under **ADR-GOV-0012 D8** — the vault's **first community-class entity**, and the remedy for the first of INV-0018's two recorded entity gaps. Warranted by the **closed** INV-0018 record (CLM-0096, FND-0018); **no investigation opened, no INV-0018 record revised, no grade moved.** Name held at the record's own honest precision — a population in a place and a century — so the over-specification the RQ deliberately avoided is not re-introduced at the entity layer; the rabbinisation question is held **inside** the entity as unresolved rather than split into entities the record cannot warrant. **Attestation window `7th c. CE`, derived from CLM-0096 element (i) and bounded by the contact period; NOT a founding date** — the community's own beginning and terminus are undated by the record and are not invented, and the parametric, time-unbounded Ḥimyarite report is recorded as context without widening the window. `attestation_uncertainty: moderate` inherits `documented_engagement_with_judaism` (Moderate), with `arabian_jewish_community_character` (Low), `relationship_type_influence_not_descent`, and `entity_target_adequacy` **excluded as non-temporal** and the exclusion recorded. No positioning bounds (forbidden on the class, and dishonest here). `projects_to` **ENT-0014** as a **non-evidential rendering projection only**, chosen because ENT-0014 is the only chronologically live Jewish tradition entity and ENT-0012 fails the chronological check — **explicitly not an assertion that these communities were rabbinic**, which is the very question the record leaves open. No `derived_from` source edge, because the source interiors are parametric/unread. R0; not cleared for external reliance.|

# End ENT-0016
