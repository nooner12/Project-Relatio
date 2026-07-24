---
title: ENT-0018 - Ethiopic Christianity
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
  - ENT-0017 Syriac Christianity
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
attestation_window: "6th-7th c. CE - Aksumite involvement in sixth-century South Arabia through the period of documented contact; the community's own span is not dated by the record"
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

# ENT-0018

# Ethiopic Christianity

## Draft Entity Record

---

# 1. Identification
**Community:** Ethiopic Christianity — the Christianity of the Aksumite realm across the Red Sea, the second of the two eastern Christian bodies CLM-0097's `eastern_christianity_specificity` component names, and a documented presence in South Arabia in the century before Islam's emergence.

**Region / period:** the Aksumite realm and its South Arabian involvement; sixth to seventh century CE.

**Alternative name recorded, not adopted:** CLM-0097 writes "Ethiopic/Aksumite Christianity." **Ethiopic** is used here as the name of the community and **Aksumite** as the polity through which the record attests its South Arabian presence; the record does not distinguish them as two objects, and neither does this entity.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious community.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **rendering_class:** `community` — the same over-generality gap as ENT-0017: **ENT-0013 Christianity is chronologically coherent but too coarse** for a documented contact that was with particular eastern bodies. Minted under **ADR-GOV-0012 D8** on the warrant of INV-0018's closed record; **no new investigation was opened, and none of INV-0018's records was revised.**

# 3. Attestation window (NOT a founding date — ADR-GOV-0012 D4)
- `attestation_claims`: **CLM-0097** (`eastern_christianity_specificity` **Moderate** — the component whose subject is precisely that the contact was with **eastern (Syriac and Ethiopic)** Christianity rather than with an undifferentiated whole) and **FND-0018** (`entity_target_gaps`, Moderate).
- **Window — `6th–7th c. CE`.** Derived from **CLM-0097 element (i)**, which is the only place the closed record gives this community a temporal anchor at all: **documented Aksumite involvement in sixth-century South Arabia**, running forward through the seventh-century period of documented contact. **This states WHEN THE RECORD ATTESTS THIS COMMUNITY, NOT when Ethiopic Christianity began or ended** — it long predates and long outlasts the window, and the closed record dates neither bound.
- **Widening, not precisifying.** Taking the sixth century as the earlier bound makes the window **wider** than ENT-0017's, not sharper. That is the permitted direction under D4: honest imprecision is preserved, and where the record offers one anchor and no other, the window is drawn to include it rather than narrowed to look decisive.
- **Parametric disclosure.** CLM-0097's §Verification marks *Aksumite involvement in sixth-century South Arabia* as a **parametric general-reference statement, not live-verified and not drawn from any source interior**. It is used here at exactly that strength — as the record's own temporal anchor, carried with its disclosure — and this entity's existence rests on the **general** eastern-contact fact that the Moderate component grades, not on that particular.
- **`attestation_uncertainty: moderate`** — inherits **`eastern_christianity_specificity` (Moderate)** and **`documented_engagement_with_christianity` (Moderate)**, the temporally relevant components. **Excluded as non-temporal:** `transmission_mechanism` (**Low** — grades *how*, not *when*), `relationship_type_influence_not_descent`, and `entity_target_adequacy`.
- **No positioning bounds** (forbidden on the class, STD-0002 §11 v1.13): a two-coordinate bar would render a window as a lifespan.

# 4. Projection (projects_to — NON-EVIDENTIAL, ADR-GOV-0012 D5)
- `projects_to` **ENT-0013 Christianity** — **a rendering instruction, and nothing else**, carrying no qualifier, no warrant, and no confidence. It asserts nothing about ecclesial standing, Christological position, or institutional relation to the tradition-whole.
- ENT-0017 and this entity project to the **same** tradition node. That is correct and is not a merge: they remain **two distinct community entities** with distinct attestation windows and distinct warrants, and the influence edges on ENT-0015 run to each separately. Projection is about **where to draw**, not about what is the same.

# 5. NAJRĀN — CONSIDERED AND NOT MINTED (ADR-GOV-0012 D8)
ADR-GOV-0012 D8 lists "Najrānī **only if** the closed record warrants its distinctness." **It does not, and the entity is therefore not minted.** The determination, recorded here because Najrān sits in the same South Arabian context this entity occupies:

1. **It is absent from the graded component.** `eastern_christianity_specificity` (Moderate) — the component that warrants ENT-0017 and this entity — has as its subject that the contact was with **eastern (Syriac and Ethiopic) Christianity**. Najrān appears only in CLM-0097 element (i)'s list of communities and in the §Verification parametric disclosure. **No graded component of the closed record has Najrānī Christianity as its subject.**
2. **The record gives it no distinguishing property.** CLM-0097 says only that "Najrān in southern Arabia held a Christian community" — a **place** and the fact of a community. It records **no** confessional affiliation, institutional independence, or separate lineage for it, and it is disclosed as a **parametric general-reference statement, not live-verified and not drawn from any source interior**, with the record stating that the entity-gap finding rests on the general eastern-contact fact "**not on any particular among them.**"
3. **Distinctness from what already exists cannot be shown.** Najrān lies in the **South Arabian** context this entity's own attestation window covers, and among the **miaphysite** bodies ENT-0017 holds unresolved inside itself. On the closed record, Najrānī Christianity is as consistent with being a **local expression** of the Ethiopic or Syriac-miaphysite presence as with being a distinct body. **The record does not discriminate, and an entity minted on an undiscriminated case would assert a distinctness that is not in evidence.**
4. **Precedent.** This is the INV-0016 **Zurvanism** discipline applied at the community layer: a candidate that cannot clear a distinctness assessment is modelled as a **current within** what exists, not given an entity. There, the refusal was recorded as the finding; here likewise.

**Consequence, stated plainly:** no ENT is created for Najrān, and **no `influenced_by` edge to it exists** — an edge whose target was not minted is simply not created (ADR-GOV-0012 D9). **The gap is recorded, not filled by assumption.** Opening evidence work on it is out of scope for this enactment; it is a candidate for a future investigation with a base that covers South Arabian Christianity, and it is logged as such in the Governance Backlog.

**The Christianised Arab tribal confederations** — also named in CLM-0097 element (i), also parametric, also absent from any graded component — are **not on D8's candidate list and are not minted**, for the same reasons and with the same record.

# 6. Relationships (STD-0004)
- `projects_to` ENT-0013 (non-evidential rendering projection).
- **No `derived_from` source edge, deliberately** — CLM-0097's source interiors are parametric/unread; the warrant runs through the graded records in `attestation_claims`.
- The `influenced_by` edge from **ENT-0015 Islam** to this entity sits on ENT-0015, warranted by CLM-0097 and FND-0018 with CLM-0097 as the recorded not-descent determination.

# 7. Limitations
- Asserts that Ethiopic/Aksumite Christianity was a documented presence across the Red Sea and in sixth-century South Arabia, and was among the eastern bodies the Qur'anic milieu's Christian contact was with. Asserts **nothing** further: not the depth or channel of that contact, not any doctrinal question, and nothing about the Aksumite polity beyond what the record's own anchor states.
- **This is the thinner of the two Christian-side community entities.** Its identification rests on the same Moderate component as ENT-0017, but the record devotes materially less to it, and its single temporal anchor is parametric. That thinness is carried by the record and by this section rather than by a lower window bound that would imply a different kind of doubt.
- Creates **no** claim, opens **no** investigation, moves **no** grade. **R0; not cleared for external reliance.**

# 8. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-24|Draft|Created under **ADR-GOV-0012 D8**, the second Christian-side community entity and the third and last minted by this enactment. Warranted by the **closed** INV-0018 record (CLM-0097 `eastern_christianity_specificity` Moderate — the component that names **eastern (Syriac and Ethiopic)** Christianity as the contact — and FND-0018 `entity_target_gaps` Moderate); **no investigation opened, no INV-0018 record revised, no grade moved.** **Attestation window `6th–7th c. CE`**, derived from the record's only temporal anchor for this community (documented Aksumite involvement in sixth-century South Arabia) running through the seventh-century contact period; **an attestation window, NOT a lifespan and NOT a founding date**, and **wider** than ENT-0017's rather than sharper — widening under uncertainty is the permitted direction, narrowing to look decisive is not. The sixth-century anchor is carried at its recorded **parametric general-reference** strength, with the mint resting on the general eastern-contact fact. `attestation_uncertainty: moderate` inherits the two Moderate temporally-relevant components, with `transmission_mechanism` (Low), `relationship_type_influence_not_descent`, and `entity_target_adequacy` **excluded as non-temporal** and the exclusion recorded. No positioning bounds. `projects_to` **ENT-0013**, non-evidential — the same tradition node ENT-0017 projects to, which is a rendering fact and **not** a merge of two distinct communities. **§5 records the NAJRĀN DETERMINATION: considered under D8's conditional and NOT MINTED** — absent from every graded component, given no distinguishing property by the record, situated inside the same South Arabian and miaphysite context ENT-0017 and this entity already cover, and therefore indistinguishable on the closed record from a local expression of them; the INV-0016 Zurvanism discipline applied at the community layer. **No edge to it exists, because an edge whose target was not minted is not created (D9); the gap is recorded, not filled by assumption**, and the Christianised Arab tribal confederations are recorded as not on D8's candidate list and likewise not minted. R0; not cleared for external reliance.|

# End ENT-0018
