---
title: ENT-0008 - Zoroastrianism
document_type: Entity Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-21
category:
  - Knowledge Base
  - Entity
  - Tradition
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0004 Ontological Framework & Reality Modeling System
related_documents:
  - INV-0016 Iranian Religious Family Origins and Branching
  - CLM-0087 Zoroastrian Origins and Root Status
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Tradition
  - Zoroastrianism
  - IranianReligions
tradition_type: founded
dating_claims:
  - CLM-0087
display_range: "2nd–early 1st millennium BCE (contested)"
relationships:
  - type: derived_from
    target: SRC-0104
  - type: derived_from
    target: SRC-0105
---

# ENT-0008

# Zoroastrianism

## Draft Entity Record

---

# 1. Identification
**Tradition:** Zoroastrianism (Mazdayasna; the religion attributed to the prophet Zarathustra / Zoroaster).
**Region / language of origin:** eastern Iranian / Central Asian milieu; Old Avestan (Gathic) and Younger Avestan.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious tradition.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **tradition_type:** `founded` — Zoroastrianism is founder-attributed (the Gathas are ascribed to Zarathustra). The contestation is over *when/whether* the founder is historically datable, not over whether the tradition claims a founder. **Anchor Fit note:** an `emergent` reading is defensible (the religion grew out of Old Iranian religion and the founder's historicity is disputed); `founded` chosen as least-wrong because the tradition is founder-attributed. Tension recorded, not resolved (routed to INV-0016 Anchor Fit Assessment).

# 3. Dating (dates are claims — ADR-GOV-0009 D3)
- `dating_claims`: **CLM-0087** — emergence contested; the traditional "258 years before Alexander" (6th c. BCE) date is a demonstrable late-Sasanian construct (rejected); the competing early dating places the Old Avestan/Gathic material c. 1500–1000 BCE by linguistic archaism (indirect, unsettled). The **claim** carries the sourced, graded, epistemic-fielded content and inherits INV-0011 CLM-0056; `display_range` ("2nd–early 1st millennium BCE (contested)") is render-only and carries no evidential weight.

# 4. Lineage (branches_from — PROVISIONAL, ADR-GOV-0009 D4)
- **NONE. Zoroastrianism is the root of the Iranian religious family** as bounded by INV-0016 — it carries no `branches_from` edge. Its own antecedent (the common Old Iranian / Indo-Iranian religious inheritance) lies outside the family under study and is noted here in prose only, not edged.
- **Zurvanism is recorded here as a heterodox CURRENT of Zoroastrianism, not a distinct tradition** (INV-0016 CLM-0088; §2.3 distinctness threshold not cleared — no attested separate community/sect; the sources frame it as a current within Zoroastrianism). It therefore has no entity of its own; the Zurvanite cosmogony (Zurvan/Time begetting Ohrmazd and Ahriman) is a current within this tradition.

# 5. Relationships (STD-0004)
- `derived_from` SRC-0104 (Shahbazi — traditional date as late construct), SRC-0105 (Hintze — linguistic early dating).
- Warranted by CLM-0087; branched-into by ENT-0009 (Manichaeism, `syncretic-descent`), ENT-0010 (Mazdakism, `heterodox-offshoot`), and ENT-0011 (Yazidism, `disputed`) — those edges are declared on the child entities.

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-21|Draft|Created at INV-0016 circuit — the family root; first tradition-class Entity Record in the vault (TPL-0006). `tradition_type: founded` (founder-attributed; emergent tension flagged for Anchor Fit); `dating_claims` CLM-0087; `display_range` render-only. No `branches_from` (root). Zurvanism recorded as a current here rather than as a distinct tradition. Pending Critical Review and structural validation.|

# End ENT-0008
