---
title: ENT-0011 - Yazidism
document_type: Entity Record
version: 0.4
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
  - CLM-0091 Yazidi Origins and Descent
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Tradition
  - Yazidism
  - IranianReligions
rendering_class: tradition
tradition_type: syncretic
dating_claims:
  - CLM-0091
display_range: "12th c. CE crystallisation (earlier substrate disputed)"
range_start_year: 1100
range_end_year: present
range_uncertainty: moderate
relationships:
  - type: branches_from
    target: ENT-0008
    qualifier: disputed
  - type: derived_from
    target: SRC-0118
  - type: derived_from
    target: SRC-0119
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-21
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ENT-0011

# Yazidism

## Draft Entity Record

---

# 1. Identification
**Tradition:** Yazidism (Êzidîtî; the religion of the Yazidi/Êzidî people).
**Region / language of origin:** northern Mesopotamia / Kurdistan; Kurdish (Kurmanji) oral tradition; cult centre at Lalish.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a living religious tradition with its own community and caste/priesthood structure.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **tradition_type:** `syncretic` — under either descent account (Iranian-substrate or Sufi-origin), Yazidism is an Iranian-substrate / Sufi-Islamic blend crystallised in a Sufi milieu. The *descent* is disputed (see §4); the *syncretic character* is not.

# 3. Dating (dates are claims — ADR-GOV-0009 D3)
- `dating_claims`: **CLM-0091** — crystallised around Sheikh ʿAdī ibn Musāfir (12th c. CE, ʿAdawiyya Sufi order) and the Lalish centre; any earlier substrate is undated and disputed; the published "sacred books" are modern (19th–20th c.) compilations (Kreyenbroek; Guest). The **claim** carries the sourced, graded content; `display_range` ("12th c. CE crystallisation (earlier substrate disputed)") is render-only.

# 4. Lineage (branches_from — PROVISIONAL, ADR-GOV-0009 D4)
- `branches_from` **ENT-0008 (Zoroastrianism)** — qualifier **`disputed`**. **Warrant:** CLM-0091 (element (ii)) — a genuine, live scholarly dispute over whether Yazidism descends primarily from a pre-Islamic Western Iranian religion (Kreyenbroek's substrate thesis, itself advocacy) or primarily from the Sufi tradition around Sheikh ʿAdī. The `disputed` qualifier **is the finding**, not a hedge. The edge renders; CLM-0091 warrants the *disputedness*.
- **Two strains (Anchor Fit):** (1) the substrate thesis's "Iranian" antecedent is *ancient Western Iranian religion broadly*, not specifically Zoroastrianism — so ENT-0008 stands in as the family-root representative, a target stretch; (2) the strongest single alternative (Sufi/Islamic origin) is **out-of-family** and unedgeable, so the contestation is carried entirely by the `disputed` qualifier rather than by a competing edge.

# 5. Relationships (STD-0004)
- `branches_from` ENT-0008 (qualifier `disputed`) — warranted by CLM-0091.
- `derived_from` SRC-0118 (Kreyenbroek 1995), SRC-0119 (Guest 1993).

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.2|2026-07-22|Draft|Added the OPTIONAL render-only positioning bounds (STD-0002 §11 v1.11) for the proportional SVG timeline: `range_start_year: 1100`, `range_end_year: present`, `range_uncertainty: moderate`. **Derived from and bounded by the dating claim CLM-0091** — the earliest defensible bound is the 12th-c. crystallisation around Sheikh ʿAdī ibn Musāfir (the bar deliberately does NOT extend into the undated, disputed pre-Islamic substrate — that contestation lives in CLM-0091 and the `disputed` lineage qualifier, not in a fabricated earlier start); `present` because Yazidism is a living tradition; `moderate` inherits CLM-0091's Moderate crystallization-dating component. (The brief's looser "high uncertainty on any earlier extension" concerns the substrate the bar excludes; the crystallisation the bar represents is Moderate — claim wins. Reported.) **Non-evidential, render-only; `display_range` remains authoritative.** No other field touched.|
|0.3|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|
|0.4|2026-07-24|Draft|**ADR-GOV-0012 D3 backfill.** Added `rendering_class: tradition`, declaring the resolution this entity occupies now that the entity layer is multi-granularity (D2). **Field addition and this history row ONLY — no other content in this record changed.** Migration discipline: define → backfill → enforce; the validator's presence check is promoted from warning to error level in the commit immediately after this one.|

# End ENT-0011
