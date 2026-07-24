---
title: ENT-0009 - Manichaeism
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
  - CLM-0089 Manichaean Origins and Descent
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Tradition
  - Manichaeism
  - IranianReligions
rendering_class: tradition
tradition_type: founded
dating_claims:
  - CLM-0089
display_range: "3rd c. CE"
range_start_year: 240
range_uncertainty: moderate
relationships:
  - type: branches_from
    target: ENT-0008
    qualifier: syncretic-descent
  - type: derived_from
    target: SRC-0111
  - type: derived_from
    target: SRC-0113
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-21
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ENT-0009

# Manichaeism

## Draft Entity Record

---

# 1. Identification
**Tradition:** Manichaeism (the religion founded by Mani).
**Region / language of origin:** Sasanian Mesopotamia (near Seleucia-Ctesiphon); Mani wrote in Syriac and, for the *Šābuhragān*, Middle Persian.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious tradition.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **tradition_type:** `founded` — deliberately founded by Mani (3rd c. CE). **Anchor Fit note:** `syncretic` co-applies (Manichaeism is a paradigmatically syncretic religion); the single-valued field takes `founded` (the defining act was Mani's founding), with the syncretic character carried by the `branches_from` qualifier. The founded/syncretic co-application is recorded as an Anchor Fit tension.

# 3. Dating (dates are claims — ADR-GOV-0009 D3)
- `dating_claims`: **CLM-0089** — founded 3rd c. CE (Mani born early 3rd c. near Seleucia-Ctesiphon per the Cologne Mani Codex; public ministry from c. 240 CE under Shapur I; death under Bahram I, exact year contested 274/277 CE). The **claim** carries the sourced, graded content; `display_range` ("3rd c. CE") is render-only. This is the best-dated emergence in the family.

# 4. Lineage (branches_from — PROVISIONAL, ADR-GOV-0009 D4)
- `branches_from` **ENT-0008 (Zoroastrianism)** — qualifier **`syncretic-descent`**. **Warrant:** CLM-0089 (element (ii)) — Manichaeism incorporated Iranian-Zoroastrian two-principle dualism as one of its constituent sources (the *Šābuhragān* addressed the Zoroastrian Sasanian court). The edge renders; CLM-0089 warrants.
- **Load-bearing caveat (Anchor Fit):** this is a **partial, multi-parent** descent. Mani's primary formative matrix was a **Jewish-Christian baptist (Elchasaite) community** (out-of-family; Cologne Mani Codex), and Christian/gnostic and (eastward) Buddhist elements are further parents. Those parents lie **outside the Iranian family and are noted in prose only, not edged** (§2.4). The single-target `branches_from` edge therefore represents one parent as if it were the parent — flagged to the INV-0016 Anchor Fit Assessment; CLM-0089's `zoroastrian_as_infamily_parent` component is graded Low to encode this.

# 5. Relationships (STD-0004)
- `branches_from` ENT-0008 (qualifier `syncretic-descent`) — warranted by CLM-0089.
- `derived_from` SRC-0111 (Cologne Mani Codex), SRC-0113 (MacKenzie, *Šābuhragān*).

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-21|Draft|Created at INV-0016 circuit — first `branches_from` edge in the vault. `tradition_type: founded` (syncretic co-applies — Anchor Fit); `dating_claims` CLM-0089 (3rd c. CE, best-dated in the family); `display_range` render-only. `branches_from` ENT-0008 qualifier `syncretic-descent` (warrant CLM-0089), with the multi-parent partiality (primary Elchasaite matrix out-of-family) flagged for Anchor Fit. Pending Critical Review and structural validation.|
|0.2|2026-07-22|Draft|Added the OPTIONAL render-only positioning bounds (STD-0002 §11 v1.11) for the proportional SVG timeline: `range_start_year: 240`, `range_uncertainty: moderate`. **Derived from and bounded by the dating claim CLM-0089** — the earliest defensible bound is Mani's public ministry (from c. 240 CE, the 3rd-c. founding); `moderate` inherits CLM-0089's Moderate emergence-dating component (the descent component graded Low does not govern temporal positioning — STD-0002 §11 v1.11). **`range_end_year` is deliberately OMITTED: CLM-0089 states no terminus** (it dates only the founding; `display_range` is "3rd c. CE"). Manichaeism is historically extinct, but no extinction date is claim-supported, so none is invented — the timeline renders it as terminus-undated rather than assigning a fabricated end (the brief's suggested ~1400 is not in the claim; claim wins — reported). Non-evidential, render-only; `display_range` remains authoritative. No other field touched.|
|0.3|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|
|0.4|2026-07-24|Draft|**ADR-GOV-0012 D3 backfill.** Added `rendering_class: tradition`, declaring the resolution this entity occupies now that the entity layer is multi-granularity (D2). **Field addition and this history row ONLY — no other content in this record changed.** Migration discipline: define → backfill → enforce; the validator's presence check is promoted from warning to error level in the commit immediately after this one.|

# End ENT-0009
