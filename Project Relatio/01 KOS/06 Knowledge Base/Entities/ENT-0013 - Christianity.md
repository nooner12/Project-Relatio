---
title: ENT-0013 - Christianity
document_type: Entity Record
version: 0.1
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
  - CLM-0093 Christian Origins and Descent
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Tradition
  - Christianity
  - JudaismChristianity
tradition_type: emergent
dating_claims:
  - CLM-0093
display_range: "1st c. CE"
range_start_year: 30
range_end_year: present
range_uncertainty: low
relationships:
  - type: branches_from
    target: ENT-0012
    qualifier: schism
  - type: derived_from
    target: SRC-0103
  - type: derived_from
    target: SRC-0140
---

# ENT-0013

# Christianity

## Draft Entity Record

---

# 1. Identification
**Tradition:** Christianity (the movement that formed around Jesus of Nazareth and, through its gradual separation from its Second-Temple Jewish matrix, became a distinct tradition).
**Region / language of origin:** Roman Judaea and Galilee, spreading through the eastern Mediterranean diaspora; Aramaic and Greek.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious tradition.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **tradition_type:** `emergent` — Christianity is modelled as an emergent movement (it grew from the Jesus movement and its gradual separation), not `founded`: asserting that Jesus *founded a new religion* is a contested, confession-adjacent claim the metaphysical bracket forbids the record to assert. **Anchor Fit note:** a `founded` reading (Jesus, or Paul, as founder) is defensible in other framings; `emergent` chosen as least-wrong and most neutral, tension recorded (routed to INV-0017 Anchor Fit Assessment).

# 3. Dating (dates are claims — ADR-GOV-0009 D3)
- `dating_claims`: **CLM-0093** — 1st-c. CE emergence, inheriting the closed anchors CLM-0075 (Jesus existence, High), CLM-0076 (crucifixion c. 30 CE, High), CLM-0068 (undisputed Pauline letters c. 50–60 CE, High). The **claim** carries the sourced, graded content (cited, not re-derived); `display_range` ("1st c. CE") is render-only.
- **Render-only positioning bounds (STD-0002 §11 v1.11):** `range_start_year: 30`, `range_end_year: present`, `range_uncertainty: low`. Derived from and bounded by CLM-0093 — start at 30 CE (the movement's origin at the crucifixion per CLM-0075/0076, not 50 CE, the earliest surviving documents — the movement, not the first letter, is what the tradition dates from); `present` because Christianity is a living tradition; `low` inherits CLM-0093's High emergence-dating component (the descent-qualifier component is Moderate/Low but does not govern temporal positioning — STD-0002 §11 v1.11). Non-evidential; `display_range` remains authoritative.

# 4. Lineage (branches_from — PROVISIONAL, ADR-GOV-0009 D4)
- `branches_from` **ENT-0012 (Second Temple Judaism)** — qualifier **`schism`**. **Warrant:** CLM-0093 (element (ii)) — the earliest Jesus movement was a Second-Temple Jewish sect that inherited its whole apocalyptic frame from Second Temple Judaism (seed warrant CLM-0058, Level 4/High), and separated to become a distinct tradition. The edge renders; CLM-0093 warrants.
- **Load-bearing caveat (Anchor Fit):** `schism` is the **least-wrong** value for "separated to become distinct" (against `reform`/`heterodox-offshoot`/`syncretic-descent`/`disputed`, each wrong here), **but it connotes a formal, datable break, and the historical "parting of the ways" was gradual, late, uneven, and locally variable** (SRC-0139 Boyarin; SRC-0141 Becker & Reed; against the earlier-partings pole, SRC-0140 Dunn). CLM-0093's `schism_qualifier_fit` component is graded Moderate to encode this; the sharpness caveat is routed to the INV-0017 Anchor Fit Assessment. Later Hellenistic/Greco-Roman inputs are prose-only, not edged (the single in-family parent is Second Temple Judaism).

# 5. Relationships (STD-0004)
- `branches_from` ENT-0012 (qualifier `schism`) — warranted by CLM-0093.
- `derived_from` SRC-0103 (NT primary texts), SRC-0140 (Dunn — the partings debate).

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-22|Draft|Created at INV-0017 circuit — the schism-class branch of the fork; born timeline-ready (TPL-0006 v1.1 / STD-0002 v1.11). `tradition_type: emergent` (founded tension flagged); `dating_claims` CLM-0093 (1st c. CE, inheriting CLM-0068/0075/0076); `display_range` render-only ("1st c. CE"); positioning bounds `range_start_year: 30` (movement origin at the crucifixion), `range_end_year: present`, `range_uncertainty: low` (inherits CLM-0093's High emergence dating). `branches_from` ENT-0012 qualifier `schism` (warrant CLM-0093; seed CLM-0058), least-wrong for "separated to become distinct" with the gradual/late-parting sharpness caveat flagged for Anchor Fit (`schism_qualifier_fit` Moderate). Metaphysical bracket acute — no supersessionist framing. Pending Critical Review and structural validation.|

# End ENT-0013
