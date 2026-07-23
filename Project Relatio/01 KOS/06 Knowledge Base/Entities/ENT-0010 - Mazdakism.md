---
title: ENT-0010 - Mazdakism
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
  - CLM-0090 Mazdakite Origins and Descent
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Tradition
  - Mazdakism
  - IranianReligions
tradition_type: reform
dating_claims:
  - CLM-0090
display_range: "late 5th–early 6th c. CE (fl. under Kavad I)"
range_start_year: 490
range_end_year: 531
range_uncertainty: high
relationships:
  - type: branches_from
    target: ENT-0008
    qualifier: heterodox-offshoot
  - type: derived_from
    target: SRC-0123
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-21
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ENT-0010

# Mazdakism

## Draft Entity Record

---

# 1. Identification
**Tradition:** Mazdakism (the heterodox movement associated with Mazdak; a precursor figure, "Zaradusht of Fasa," is reported in the scholarship but is parametric — not itemised in the SRC-0123 catalog record and not live-verified).
**Region / language of origin:** Sasanian Iran.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious-and-social movement within the Sasanian Zoroastrian world.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **tradition_type:** `reform` — the movement is reported as a religious-and-social reform. **Note:** the `reform` tradition_type describes its *own emergence mode*; the `branches_from` **qualifier** `heterodox-offshoot` describes the *nature of its descent link* to Zoroastrianism. The two vocabularies are deliberately not conflated; their near-coincidence here is recorded for Anchor Fit. **The `reform` classification rests on the same late/hostile, Low-confidence base (SRC-0123 over the Perso-Arabic tradition) as everything else about Mazdakism (ROLE-0004 Flag 4); `emergent` is nearly as defensible — this is a least-wrong classification, not an established one.**

# 3. Dating (dates are claims — ADR-GOV-0009 D3)
- `dating_claims`: **CLM-0090** — floruit under Kavad I, late 5th–early 6th c. CE; suppression c. 528–531 CE (debated). The **claim** carries the sourced, graded content and its heavy caveat (the whole picture is reconstructed from a late, largely hostile Perso-Arabic tradition — Crone 1991). `display_range` ("late 5th–early 6th c. CE (fl. under Kavad I)") is render-only.

# 4. Lineage (branches_from — PROVISIONAL, ADR-GOV-0009 D4)
- `branches_from` **ENT-0008 (Zoroastrianism)** — qualifier **`heterodox-offshoot`**. **Warrant:** CLM-0090 (element (ii)) — Mazdakism arose as a heterodoxy/heresy within Sasanian Zoroastrianism (Crone: "Kavād's Heresy and Mazdak's Revolt"). The edge renders; CLM-0090 warrants.
- **Qualifier note (Anchor Fit):** the scaffold offered `heterodox-offshoot` **or** `reform` for the descent link; `heterodox-offshoot` chosen because the sources frame Mazdakism as heresy departing from orthodoxy rather than an accepted internal reform. The `reform` near-miss is recorded. The warrant grade is Low (hostile, late, uncorroborated base) — honest thinness, not a defect.

# 5. Relationships (STD-0004)
- `branches_from` ENT-0008 (qualifier `heterodox-offshoot`) — warranted by CLM-0090.
- `derived_from` SRC-0123 (Crone 1991).

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.3|2026-07-22|Draft|Added the OPTIONAL render-only positioning bounds (STD-0002 §11 v1.11) for the proportional SVG timeline: `range_start_year: 490`, `range_end_year: 531`, `range_uncertainty: high`. **Derived from and bounded by the dating claim CLM-0090** — the defensible span is the late-5th-c. floruit under Kavad I (r. 488–531) to the suppression c. 528–531 CE; `high` inherits CLM-0090's Low emergence-dating component (the family's thinnest, hostile-and-late Perso-Arabic base). This is the shortest bar and, per the uncertainty mapping, renders visibly weakest (dashed/faded) — the honest geometry of a Low-confidence dating. **Non-evidential, render-only; `display_range` remains authoritative.** No other field touched.|
|0.2|2026-07-21|Draft|**ROLE-0004 remediation (Flags 2+4):** hedged the "Zaradusht of Fasa" precursor as parametric/not-itemised-in-record (§1); recorded that the `reform` `tradition_type` classification rests on the same late/hostile Low-confidence base as the graded components, with `emergent` nearly as defensible (§2, least-wrong not established). No `tradition_type`, edge, qualifier, or `dating_claims` changed.|
|0.1|2026-07-21|Draft|Created at INV-0016 circuit. `tradition_type: reform` (distinct from the descent qualifier); `dating_claims` CLM-0090 (Kavad-era; hostile/late base, Low); `display_range` render-only. `branches_from` ENT-0008 qualifier `heterodox-offshoot` (warrant CLM-0090; chosen over the scaffold alternative `reform`, recorded for Anchor Fit). Distinctness threshold met. Pending Critical Review and structural validation.|
|0.4|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

# End ENT-0010
