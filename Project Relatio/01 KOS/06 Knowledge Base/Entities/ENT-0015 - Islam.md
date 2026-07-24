---
title: ENT-0015 - Islam
document_type: Entity Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-07-23
category:
  - Knowledge Base
  - Entity
  - Tradition
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0004 Ontological Framework & Reality Modeling System
related_documents:
  - INV-0018 Islam Origins and Abrahamic Relationships
  - CLM-0095 Islam Emergence and Dating
  - CLM-0096 Islam Relationship to Judaism
  - CLM-0097 Islam Relationship to Christianity
  - FND-0018 Islam Origins and Abrahamic Relationship Shape
  - ADR-GOV-0012 - Entity Resolution, Projection, and the influenced_by Relation
  - ENT-0016 Seventh-Century Arabian Jewish Communities
  - ENT-0017 Syriac Christianity
  - ENT-0018 Ethiopic Christianity
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Tradition
  - Islam
  - WorldReligionsTimeline
rendering_class: tradition
tradition_type: founded
dating_claims:
  - CLM-0095
display_range: "7th c. CE (ministry c. 610-632 CE) - present"
range_start_year: 610
range_end_year: present
range_uncertainty: moderate
relationships:
  - type: derived_from
    target: SRC-0143
  - type: derived_from
    target: SRC-0150
  - type: influenced_by
    target: ENT-0016
    qualifier: documented
    warrant:
      - CLM-0096
      - FND-0018
    not_descent: CLM-0096
  - type: influenced_by
    target: ENT-0017
    qualifier: documented
    warrant:
      - CLM-0097
      - FND-0018
    not_descent: CLM-0097
  - type: influenced_by
    target: ENT-0018
    qualifier: documented
    warrant:
      - CLM-0097
      - FND-0018
    not_descent: CLM-0097
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-23
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ENT-0015

# Islam

## Draft Entity Record

---

# 1. Identification
**Tradition:** Islam — the religious tradition that emerged in seventh-century western Arabia around the movement associated with Muhammad. Treated here as **one tradition with internal plurality**; the **Sunni/Shia division and all other sub-traditions are out of scope** and deferred to a later separate investigation (INV-0018 §2.4), so **no sub-tradition entity exists and no internal lineage edge is drawn**.
**Region / language of origin:** Western Arabia (the Ḥijāz) and the adjoining late-antique Near East; Arabic.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious tradition.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **tradition_type:** `founded` — in the **historical register**, the community forms around a named founder-figure within his lifetime. This is a structural descriptor about the shape of the historical account; it carries **no theological or evaluative weight** and asserts nothing about the origin of what was taught (the metaphysical bracket, INV-0018 §2.1, is total). **Two strains recorded (CLM-0095, `tradition_type_classification_fit` Moderate):** (1) **the tradition's own self-account is neither founding nor emergence but RESTORATION** (*millat Ibrāhīm*, CLM-0098) — a fifth shape the four-value list does not contain; (2) the **late-crystallisation readings** (Donner; the revisionist pole) pressure toward `emergent`. `founded` is retained as **least-wrong for the historical register**, both strains routed to the INV-0018 Anchor Fit Assessment. **Asymmetry note:** ENT-0013 Christianity carries `emergent` while this entity carries `founded`; the difference is **evidenced, not conventional, and is not a ranking** — Christianity's founder-question is itself contested in the field, Muhammad's role as the community's founder-figure is not contested in the same way even by the base's most sceptical work (CLM-0095).

# 3. Dating (dates are claims — ADR-GOV-0009 D3)
- `dating_claims`: **CLM-0095** — seventh-century CE emergence (Level 4/High); confessional crystallisation dating contested (Level 3/Moderate); the traditional chronology reported as the tradition's chronology, not asserted as this record's finding. The **claim** carries the sourced, graded, epistemic-fielded content; `display_range` is render-only.
- **Render-only positioning bounds (STD-0002 §11 v1.11):** `range_start_year: 610`, `range_end_year: present`, `range_uncertainty: moderate`. **Derived from and bounded by CLM-0095.** Start at **610** — the traditional beginning of the ministry, taken as the **earliest defensible emergence bound** per the standard, with **622** (the *hijra*, the community-formation anchor and calendar epoch) recorded in CLM-0095 as the firmer alternative; the contestedness is carried by `range_uncertainty` and by the claim, never by a false-precision point. `present` because Islam is a living tradition (a render instruction, not a historical claim). **`moderate` inherits the weakest EMERGENCE-DATING component of CLM-0095** — `confessional_crystallisation_dating` at Moderate — per the STD-0002 §11 v1.11 mapping; CLM-0095's `revisionist_redating_adjudication` (Low) and `tradition_type_classification_fit` (Moderate) are **non-temporal by construction** (they grade this record's adjudicative reach and a classification fit, not when the tradition emerged) and therefore do not govern this field. **Non-evidential; `display_range` remains authoritative.**

# 4. Lineage (branches_from — PROVISIONAL, ADR-GOV-0009 D4)
- **NO `branches_from` EDGE. This entity is deliberately unconnected, and the refusal is the finding.**
- **To Judaism (CLM-0096):** the relationship is **influence and engagement, not descent**. Additionally, **no existing Jewish entity would be an honest target**: **ENT-0012 Second Temple Judaism fails the chronological-coherence check** (`range_end_year: 70` against a seventh-century relationship), and **ENT-0014 Rabbinic Judaism over-specifies** (the rabbinisation of seventh-century Arabian Jewish communities is an open question the base does not cover). **Entity gap recorded and routed to Anchor Fit.**
- **To Christianity (CLM-0097):** the relationship is **influence and engagement, not descent**, reasoned independently. **ENT-0013 Christianity passes the chronological check but is too coarse** — the documented contact was with eastern Syriac, Ethiopic/Aksumite, Arab-confederation and Najrānī Christianity, which the vault does not model and which §2.4 forbids this family to create. **Second-shape entity gap recorded and routed.**
- **`disputed` is NOT used and could not be.** It means *descent is disputed*; here descent is **not established**, and the qualifier may never hedge for influence (INV-0018 §3.1).
- **A disconnected node is an honest rendering and requires no repair** (INV-0018 §3.1). The influence relationships are recorded in prose (CLM-0096, CLM-0097, FND-0018) and the modelling gap is routed to **Anchor Fit Part 2** — with INV-0011 as the pre-existing first case, this is the **second** case for a possible `influenced_by` edge type. **No such type is created here.**
- **Self-account note (does NOT license an edge).** The tradition's own account (CLM-0098) is **restorationist** — claimed descent from *millat Ibrāhīm*, prior to and independent of both later traditions. Under the dual-track rule a self-account may **never** be encoded as a lineage edge, and it is not. It is recorded as an observation in Anchor Fit Part 3.

# 4.1 Influence (influenced_by — ADR-GOV-0012 D6/D9)

**Three `influenced_by` edges are now drawn, and NOTHING in §4 changes.** The refusal of descent stands exactly as recorded; what has changed is that the graph acquired a type that can carry *influence* and an entity resolution that gives that influence an honest target. `influenced_by` is **not** a weakened `branches_from` and is not a repair of the unconnected node — Islam still has **no lineage edge**, still renders as a **root**, and these edges **do not render on the default timeline** (D7).

*(Numbered §4.1 rather than inserted as a new §5 so the existing section numbers — and every reference to them — stay valid; the STD-0002 §6.1 precedent.)*

**Per-edge warrant reasoning.** Each edge names its graded warrant and its **recorded not-descent determination**, the requirement ADR-GOV-0012 D6 makes constitutive: an influence edge must state *why `branches_from` was refused*, because influence is far easier to over-assert than descent.

| → target | qualifier | warrant | not-descent determination | why this qualifier |
|---|---|---|---|---|
| **ENT-0016** Seventh-Century Arabian Jewish Communities | `documented` | CLM-0096; FND-0018 | **CLM-0096 element (ii)** — the descent bar was stated before the evidence was measured, the base's one descent-shaped reading (*Hagarism*, SRC-0146) was weighed and failed on its own recorded reception, and §(d) refuses the edge | `documented_engagement_with_judaism` is **Moderate**: engagement is well attested across the base. It is not `contested` — Rival C (back-projection) **relocates** the engagement, it does not delete it, and CLM-0096 records that it cannot lower this component below Moderate. What is thin here is the communities' **character**, not the fact of engagement, and that thinness is carried by ENT-0016's own record |
| **ENT-0017** Syriac Christianity | `documented` | CLM-0097; FND-0018 | **CLM-0097 element (ii)** — the bar was re-stated and measured on Christian-side evidence alone, the base contains **no** descent-shaped Christian thesis, and §(d) refuses the edge | `documented_engagement_with_christianity` and `eastern_christianity_specificity` are both **Moderate**; SRC-0149, the base's principal surface, has Christianity in the Arabic-speaking world as its subject. Nothing in the record **contests** that this contact occurred, so `contested` would misstate the epistemic situation |
| **ENT-0018** Ethiopic Christianity | `documented` | CLM-0097; FND-0018 | **CLM-0097 element (ii)** — as above; the same determination covers both Christian-side edges, which were reasoned as one | Same **Moderate** `eastern_christianity_specificity` component, which names **eastern (Syriac and Ethiopic)** Christianity together. **This is the thinner of the two Christian strands** — the record devotes materially less to it and its temporal anchor is parametric — but thinness is not contestedness: `contested` is the analogue of `disputed` and means *the influence claim itself is disputed*, which nothing in the record says. The thinness is carried by ENT-0018's own record and by `attestation_uncertainty`, not by a qualifier that would assert a dispute that does not exist |

**No edge to ENT-0013 or ENT-0014 directly** (D9): the honest targets are the community entities, which is the entire point of the joint package. **No edge to Najrān**, whose entity was considered under D8's conditional and **not minted** (determination at ENT-0018 §5) — an edge whose target was not minted is simply not created.

**Multi-target, from birth.** Three edges from one node, to two traditions' worth of communities, assessed independently. FND-0018 Part 1 recorded that although multi-parent *descent* did not fire, multi-parent *relation* did; this is that observation instantiated.

**No grade moved.** These edges encode findings the closed record already carried at their existing grades. Everything remains **R0** and **not cleared for external reliance** (FND-0018 §5).

# 5. Relationships (STD-0004)
- **No `branches_from` edge** — see §4. ENT-0012, ENT-0013, and ENT-0014 are **unmodified**.
- `influenced_by` ENT-0016, ENT-0017, ENT-0018 — each `documented`, each with its graded warrant and recorded not-descent determination (§4.1). **Not rendered on the default timeline** (ADR-GOV-0012 D7).
- `derived_from` SRC-0143 (Donner — formation and early Islam), SRC-0150 (al-Azmeh — the Arabian / late-antique milieu).
- Warranting and dating claims: CLM-0095 (dating), CLM-0096 and CLM-0097 (the relationship determinations and the two entity-gap findings), CLM-0098 (self-understanding, self-understanding register only).

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-23|Draft|Created at INV-0018 circuit — **FAMILY 3 of the ADR-GOV-0009 timeline program, and the program's first deliberately UNCONNECTED tradition node.** Born timeline-ready (TPL-0006 v1.1 / STD-0002 v1.11): `tradition_type: founded` (least-wrong for the historical register, with the restorationist-self-account strain and the late-crystallisation strain both recorded and routed, and the ENT-0013 `emergent` asymmetry justified on evidence rather than convention); `dating_claims` CLM-0095; `display_range` render-only; positioning bounds `range_start_year: 610` (earliest defensible emergence bound; 622 *hijra* recorded as the firmer alternative), `range_end_year: present`, `range_uncertainty: moderate` inheriting CLM-0095's weakest **emergence-dating** component with the non-temporal components' exclusion documented. **NO `branches_from` edge — a reasoned refusal under the edge-restraint rule, not an omission:** influence-not-descent to both Judaism (CLM-0096) and Christianity (CLM-0097), plus two distinct entity-target gaps (chronological incoherence/character mismatch on the Jewish side; over-generality on the Christian side), both recorded and routed to Anchor Fit. `disputed` explicitly refused as an influence hedge. No sub-tradition entity (Sunni/Shia deferred). Metaphysical bracket total; no confessional or supersessionist framing in any direction. Pending Critical Review and structural validation.|
|0.2|2026-07-24|Draft|**ADR-GOV-0012 D3 backfill.** Added `rendering_class: tradition`, declaring the resolution this entity occupies now that the entity layer is multi-granularity (D2). **Field addition and this history row ONLY — no other content in this record changed.** Migration discipline: define → backfill → enforce; the validator's presence check is promoted from warning to error level in the commit immediately after this one.|
|0.3|2026-07-24|Draft|**ADR-GOV-0012 D6/D9 enactment — three `influenced_by` edges drawn, and the §4 refusal of descent UNCHANGED.** `influenced_by` ENT-0016 (Seventh-Century Arabian Jewish Communities), ENT-0017 (Syriac Christianity), ENT-0018 (Ethiopic Christianity), each qualifier `documented`, each warranted by its graded claim (CLM-0096 / CLM-0097) plus FND-0018 and each naming its **recorded not-descent determination** — the requirement D6 makes constitutive, because influence is far easier to over-assert than descent. New **§4.1** records the per-edge reasoning, including why `documented` and not `contested` on each: nothing in the closed record contests that these contacts occurred, and `contested` (the analogue of `disputed`) would assert a dispute that does not exist — **thinness is not contestedness**, and ENT-0018's thinner strand is carried by its own record and its `attestation_uncertainty`, not by a qualifier. **Nothing about the lineage position moved:** no `branches_from` edge, no lineage claim, no confidence grade changed, and ENT-0012/0013/0014 and every INV-0018 record remain unmodified. **No edge to ENT-0013 or ENT-0014 directly** (D9 — the honest targets are the community entities) and **no edge to Najrān**, whose entity was considered under D8's conditional and not minted. **These edges do NOT render on the default timeline** (D7): Islam still has no lineage edge and still renders as a **root**, which remains the honest rendering. Multi-target from birth, instantiating FND-0018 Part 1's observation that multi-parent *relation* fired where multi-parent *descent* did not. Section numbered 4.1 so existing section references stay valid (the STD-0002 §6.1 precedent). R0; not cleared for external reliance.|

# End ENT-0015
