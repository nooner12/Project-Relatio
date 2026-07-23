---
title: ENT-0012 - Second Temple Judaism
document_type: Entity Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-22
category:
  - Knowledge Base
  - Entity
  - Tradition
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0004 Ontological Framework & Reality Modeling System
related_documents:
  - INV-0017 Judaism-Christianity Family Origins and Branching
  - CLM-0092 Second Temple Judaism Origins and Root Status
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Tradition
  - SecondTempleJudaism
  - JudaismChristianity
tradition_type: emergent
dating_claims:
  - CLM-0092
display_range: "c. 516 BCE – 70 CE (Second Temple period)"
range_start_year: -516
range_end_year: 70
range_uncertainty: moderate
relationships:
  - type: derived_from
    target: SRC-0137
  - type: derived_from
    target: SRC-0138
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-22
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ENT-0012

# Second Temple Judaism

## Draft Entity Record

---

# 1. Identification
**Tradition:** Second Temple Judaism (Judaism of the Second Temple period; the shared Jewish matrix of the late Persian, Hellenistic, Hasmonean, and Roman phases, encompassing its internal parties — Pharisees, Sadducees, Essenes, and the apocalyptic and Hellenistic currents).
**Region / language of origin:** Judaea and the wider Jewish diaspora; Hebrew, Aramaic, and Greek.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious tradition.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **tradition_type:** `emergent` — Second Temple Judaism emerged from the post-exilic reconstitution of Jewish life around the rebuilt Temple and the Torah; it is not founder-attributed *as this tradition* (its Mosaic/Sinai narrative is an earlier layer, and asserting Moses as historical founder would breach the metaphysical bracket). **Anchor Fit note:** a `founded` reading (via the Mosaic covenant) is conceivable but historically and neutrally weaker; `emergent` chosen as least-wrong, tension recorded (routed to INV-0017 Anchor Fit Assessment).

# 3. Dating (dates are claims — ADR-GOV-0009 D3)
- `dating_claims`: **CLM-0092** — the Second Temple period runs c. 516 BCE (completion of the rebuilt Temple) to 70 CE (destruction); the *period* bounds are secure (live-verified), the *tradition-emergence* point is contested. The **claim** carries the sourced, graded, epistemic-fielded content; `display_range` ("c. 516 BCE – 70 CE (Second Temple period)") is render-only and carries no evidential weight.
- **Render-only positioning bounds (STD-0002 §11 v1.11):** `range_start_year: -516`, `range_end_year: 70`, `range_uncertainty: moderate`. Derived from and bounded by CLM-0092 — start at the Temple-completion anchor (c. 516 BCE; the claim records the 538/516 BCE spread as contestedness), **end at 70 CE because Second Temple Judaism in its Temple-centred form does not continue past the destruction — its heirs are the two branches** (this is the fork, §2.2). `moderate` inherits CLM-0092's Moderate emergence-dating component. Non-evidential; `display_range` remains authoritative.

# 4. Lineage (branches_from — PROVISIONAL, ADR-GOV-0009 D4)
- **NONE. Second Temple Judaism is the ROOT of this family** as bounded by INV-0017 — it carries **no `branches_from` edge**. Its own upstream descent — from **Israelite / Yahwistic religion and the Canaanite substrate** — lies **outside this family as bounded here and is DEFERRED to a later "family 2-deep" investigation (§2.5)**; it is noted in prose only, not asserted and not edged. Placing no edge on the hub is deliberate and load-bearing: the fork must not read as "Second Temple Judaism became Christianity."
- **Branched-into by TWO edges (the fork):** ENT-0013 (Christianity, `schism`) and ENT-0014 (Rabbinic Judaism, `reform`) — both edges are declared on the **child** entities and warranted by CLM-0093 and CLM-0094 respectively. The internal parties (Pharisees, Sadducees, Essenes, apocalyptic, Hellenistic currents) are **currents/parties within this tradition, not distinct traditions** (CLM-0092 element (ii); §2.3 distinctness threshold applied — the common-Judaism substrate of Temple, Torah, and covenant God holds them as one). They therefore have **no entities of their own**; any sub-stream that later clears the threshold is a flagged future-investigation candidate (the Essene/Qumran community the nearest, but extinct and treated as a sect, not a branch).

# 5. Relationships (STD-0004)
- `derived_from` SRC-0137 (Sanders — "common Judaism"), SRC-0138 (Cohen — the period arc).
- Warranted by CLM-0092; branched-into by ENT-0013 (Christianity, `schism`) and ENT-0014 (Rabbinic Judaism, `reform`) — those edges declared on the child entities. No lineage edge on this hub (root).

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-22|Draft|Created at INV-0017 circuit — the family root and the hub of the Judaism–Christianity fork; born timeline-ready (TPL-0006 v1.1 / STD-0002 v1.11). `tradition_type: emergent` (founded tension flagged for Anchor Fit); `dating_claims` CLM-0092; `display_range` render-only ("c. 516 BCE – 70 CE (Second Temple period)"); positioning bounds `range_start_year: -516`, `range_end_year: 70`, `range_uncertainty: moderate`, derived from CLM-0092 (end at 70 CE — Temple-centred tradition superseded by its two branches). **No `branches_from` (root; upstream Israelite/Yahwistic descent deferred to a later family 2-deep, not asserted/edged).** Internal parties recorded as currents within one tradition (§2.3), not entities. Branched-into by ENT-0013 and ENT-0014 (edges on the children). Pending Critical Review and structural validation.|
|0.2|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

# End ENT-0012
