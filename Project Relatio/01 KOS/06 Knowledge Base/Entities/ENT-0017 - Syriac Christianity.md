---
title: ENT-0017 - Syriac Christianity
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
  - CLM-0097 Islam Relationship to Christianity
  - FND-0018 Islam Origins and Abrahamic Relationship Shape
  - ENT-0013 Christianity
  - ENT-0015 Islam
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Community
  - Christianity
  - WorldReligionsTimeline
rendering_class: community
attestation_claims:
  - CLM-0097
  - FND-0018
attestation_window: "7th c. CE - attested through the period of documented contact (the Qur'anic milieu); the community's own span is not dated by the record"
attestation_uncertainty: moderate
relationships:
  - type: projects_to
    target: ENT-0013
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-24
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ENT-0017

# Syriac Christianity

## Draft Entity Record

---

# 1. Identification
**Community:** Syriac Christianity — the Syriac-language Christian communities that were the dominant Christian presence to Arabia's north and east in the period of Islam's emergence, and one of the specific eastern bodies the Qur'anic milieu's documented Christian contact was with (CLM-0097).

**Region / period:** the Syriac-speaking Christian east — Mesopotamia, Syria, and the Sasanian and Byzantine frontier zones — in the period of documented contact, seventh century CE.

**Internal plurality held inside the entity, not resolved.** CLM-0097 names **both the East Syrian tradition and the miaphysite churches** — bodies distinguished from one another (and from the Chalcedonian imperial church) precisely on the Christological questions the Qur'anic material engages. **The closed record does not determine which of them the documented contact ran through**, and this record does not split them. Naming one would assert a channel the base cannot support.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious community.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **rendering_class:** `community` — the **inverse** of ENT-0016's case, and INV-0018 recorded the difference rather than smoothing it. **ENT-0013 Christianity passes the chronological-coherence check** (30 CE → present) but **is too coarse**: it models Christianity as such, whereas the documented contact was with **particular eastern communities**. Minted under **ADR-GOV-0012 D8** on the warrant of INV-0018's closed record; **no new investigation was opened, and none of INV-0018's records was revised.**

# 3. Attestation window (NOT a founding date — ADR-GOV-0012 D4)
- `attestation_claims`: **CLM-0097** (the documented-contact finding, `eastern_christianity_specificity` **Moderate**, and the second-shape entity gap) and **FND-0018** (`entity_target_gaps`, Moderate).
- **Window — `7th c. CE`.** Derived from **CLM-0097 element (i)**: the Syriac Christian presence in and around the formation region during the period of documented contact, whose dating is fixed by CLM-0095's seventh-century emergence. **This states WHEN THE RECORD ATTESTS THIS COMMUNITY — through the period of contact — and NOT when Syriac Christianity began or ended.** It manifestly existed long before the seventh century and long after it; **the closed record dates neither bound, so neither appears here.** A window that ran wider would be asserting general knowledge the record does not carry; a window that read as a lifespan would be a different error again. This is an **attestation** window in the strict D4 sense.
- **Parametric disclosure, carried forward rather than absorbed.** CLM-0097's §Verification marks the milieu particulars stated in its own voice — the East Syrian and miaphysite presence to Arabia's north and east — as **parametric general-reference statements, not live-verified and not drawn from any source interior**, and records that the entity-gap finding rests on the **general** fact of eastern-community contact rather than on any particular. This entity is minted on that general fact, warranted by the **Moderate** `eastern_christianity_specificity` component whose subject is SRC-0149's own subject matter; the particulars are reported at parametric strength and nothing here turns on any one of them.
- **`attestation_uncertainty: moderate`** — inherits the weakest **TEMPORALLY RELEVANT** components of the warranting records: **`eastern_christianity_specificity` (Moderate)** and **`documented_engagement_with_christianity` (Moderate)**, which together grade whether contact with this specific eastern body is attested in this period. **Excluded as non-temporal** (STD-0002 §11): `transmission_mechanism` (**Low** — it grades *how* material reached the milieu, oral/liturgical/homiletic, not *when* the community is attested), `relationship_type_influence_not_descent`, and `entity_target_adequacy`.
- **No positioning bounds**, by rule (STD-0002 §11 v1.13) and by honesty: this community's real span exceeds its attested window in both directions, and a bar would show the window as the span.

# 4. Projection (projects_to — NON-EVIDENTIAL, ADR-GOV-0012 D5)
- `projects_to` **ENT-0013 Christianity** — **a rendering instruction, and nothing else.** *For display, re-anchor this node to the tradition layer here.*
- It carries **no qualifier, no warrant, and no confidence**, and asserts **nothing** about institutional continuity, ecclesial standing, or Christological position relative to the tradition-whole — questions INV-0018 brackets entirely (§2.1 metaphysical bracket; Rival B refused on historical evidence rather than on register). The relationship that *is* asserted is the graded influence edge on ENT-0015, not this.
- **Why the projection is honest where an evidential edge to ENT-0013 was not.** CLM-0097 refused an *evidential* edge to ENT-0013 because it would "assert a relation to the whole where the evidence documents relations to parts." A **projection** asserts no relation at all — only where to draw the node. That separation is the whole purpose of D5.

# 5. Relationships (STD-0004)
- `projects_to` ENT-0013 (non-evidential rendering projection).
- **No `derived_from` source edge, deliberately** — CLM-0097's five cited source interiors are **parametric/unread**, and no page-level claim is asserted from any of them. The warrant runs through the **graded records** (`attestation_claims`), which carry that disclosure with them.
- The `influenced_by` edge from **ENT-0015 Islam** to this entity sits on ENT-0015, warranted by CLM-0097 and FND-0018 with CLM-0097 as the recorded not-descent determination.

# 6. Limitations
- Asserts that Syriac-language Christian communities were a documented presence in the milieu of Islam's emergence and among the specific eastern bodies the contact was with. Asserts **nothing** about which Syriac body, about the transmission mechanism (`transmission_mechanism` is **Low** and inferential), or about any doctrinal question.
- **The derivation-shaped Syriac-substratum literature is absent from the INV-0018 base and was disclosed as absent rather than treated as refuted** (CLM-0097 element (ii)(b); the stated reason that claim's determination is Moderate and not High). This entity **neither adopts nor forecloses** that literature; minting it changes nothing about that gap, which remains the highest-value target for any owner-approved base extension.
- Creates **no** claim, opens **no** investigation, moves **no** grade. **R0; not cleared for external reliance.**

# 7. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-24|Draft|Created under **ADR-GOV-0012 D8** as the remedy for the **second shape** of INV-0018's entity gap — over-generality, distinct from ENT-0016's chronological-incoherence-plus-character-mismatch case, and recorded here as the inverse it is. Warranted by the **closed** INV-0018 record (CLM-0097 `eastern_christianity_specificity` Moderate, FND-0018 `entity_target_gaps` Moderate); **no investigation opened, no INV-0018 record revised, no grade moved.** Name held at "Syriac Christianity" — the East Syrian / miaphysite distinction is **held inside** the entity as unresolved, because the closed record does not determine which body the contact ran through and naming one would assert a channel the base cannot support. **Attestation window `7th c. CE` — an ATTESTATION window in the strict D4 sense, NOT a lifespan and NOT a founding date:** this community demonstrably existed before and after the window, the record dates neither bound, and neither is invented. CLM-0097's **parametric general-reference disclosure** on the milieu particulars is carried forward in-record, with the mint resting on the **general** fact of eastern-community contact exactly as the entity-gap finding does. `attestation_uncertainty: moderate` inherits `eastern_christianity_specificity` and `documented_engagement_with_christianity` (both Moderate), with `transmission_mechanism` (Low), `relationship_type_influence_not_descent`, and `entity_target_adequacy` **excluded as non-temporal** and the exclusion recorded. No positioning bounds. `projects_to` **ENT-0013** as a **non-evidential rendering projection only** — honest precisely where an evidential edge to the tradition-whole was refused, since a projection asserts no relation at all. The absent Syriac-substratum literature is restated as an open gap this entity neither adopts nor forecloses. R0; not cleared for external reliance.|

# End ENT-0017
