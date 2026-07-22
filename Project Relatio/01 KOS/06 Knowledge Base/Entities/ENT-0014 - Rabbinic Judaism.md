---
title: ENT-0014 - Rabbinic Judaism
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
  - CLM-0094 Rabbinic Judaism Origins and Descent
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Tradition
  - RabbinicJudaism
  - JudaismChristianity
tradition_type: reform
dating_claims:
  - CLM-0094
display_range: "post-70 CE (Mishnah c. 200 CE)"
range_start_year: 70
range_end_year: present
range_uncertainty: moderate
relationships:
  - type: branches_from
    target: ENT-0012
    qualifier: reform
  - type: derived_from
    target: SRC-0142
  - type: derived_from
    target: SRC-0138
---

# ENT-0014

# Rabbinic Judaism

## Draft Entity Record

---

# 1. Identification
**Tradition:** Rabbinic Judaism (the form of Judaism that consolidated after 70 CE around the rabbis, Torah study, and halakhah, and that became the dominant historical mainline of Judaism; the tradition of the Mishnah and the Talmuds).
**Region / language of origin:** Roman/Byzantine Palestine and Sasanian Babylonia; Hebrew and Aramaic.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious tradition.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **tradition_type:** `reform` — Rabbinic Judaism reconstituted an existing tradition (Second Temple Judaism, most directly the Pharisaic stream) around Torah study and halakhah after the Temple's loss, rather than emerging fresh or being founder-attributed. **Note (§2.8):** this `tradition_type` value `reform` is a **different vocabulary** from the `branches_from` **qualifier** `reform` on the lineage edge below — the two fields coincidentally land on the same word for this tradition but are not the same field and are not conflated. **Both carry the same understatement tension** (each connotes departure where main-line continuation is meant); an `emergent` `tradition_type` is the defensible alternative. `reform` chosen as least-wrong; the double-`reform` coincidence is flagged to the INV-0017 Anchor Fit Assessment.

# 3. Dating (dates are claims — ADR-GOV-0009 D3)
- `dating_claims`: **CLM-0094** — post-70 CE consolidation (the rabbinic movement after the Temple's destruction; Yavneh/Yohanan ben Zakkai the conventional early locus), with the Mishnah's redaction c. 200 CE (under Judah ha-Nasi) as the standard dating anchor; the consolidation *process* is contested. The **claim** carries the sourced, graded content; `display_range` ("post-70 CE (Mishnah c. 200 CE)") is render-only.
- **Render-only positioning bounds (STD-0002 §11 v1.11):** `range_start_year: 70`, `range_end_year: present`, `range_uncertainty: moderate`. Derived from and bounded by CLM-0094 — start at 70 CE (the destruction that triggers the consolidation); `present` because Rabbinic Judaism is the living mainline of Judaism today; `moderate` inherits CLM-0094's Moderate emergence-dating component. Non-evidential; `display_range` remains authoritative.

# 4. Lineage (branches_from — PROVISIONAL, ADR-GOV-0009 D4)
- `branches_from` **ENT-0012 (Second Temple Judaism)** — qualifier **`reform`**. **Warrant:** CLM-0094 (element (ii)) — Rabbinic Judaism continues the Second-Temple tradition as its **main line** (most directly the Pharisaic stream), reconstituted around Torah and halakhah after the Temple's loss. The edge renders; CLM-0094 warrants.
- **THE ANCHOR STRESS-TEST (load-bearing, Anchor Fit centerpiece):** the controlled qualifier list (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed`) **contains no right word for MAIN-LINE CONTINUATION.** `reform` is the **least-wrong** — Rabbinic Judaism reformed/reconstituted the tradition — **but it understates the case**: it connotes departure-with-change, whereas Rabbinic Judaism is the **least-departed** line, the parent's own line carried forward, not a departure. CLM-0094's `reform_qualifier_fit` component is graded **Low** to encode this **vocabulary strain (not doubt about the descent, which is Moderate)**. A recommendation — likely a new `continuation`/`main-line` qualifier — is routed to the INV-0017 Anchor Fit Assessment / GB-2026-041 and is **never self-applied**. **Neutrality note:** the edge does **not** frame Rabbinic Judaism as a "residue" left by Christianity; both branches descend from the shared parent and neither is the normatively "true" continuation.

# 5. Relationships (STD-0004)
- `branches_from` ENT-0012 (qualifier `reform`) — warranted by CLM-0094.
- `derived_from` SRC-0142 (Strack–Stemberger — Mishnah dating), SRC-0138 (Cohen — the Second-Temple→rabbinic bridge).

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-22|Draft|Created at INV-0017 circuit — the **continuation / main-line branch and the anchor stress-test**; born timeline-ready (TPL-0006 v1.1 / STD-0002 v1.11). `tradition_type: reform` (reconstituted an existing tradition; noted DISTINCT from the qualifier `reform` per §2.8 — same word, different vocabulary; emergent alternative flagged); `dating_claims` CLM-0094 (post-70 CE; Mishnah c. 200 CE); `display_range` render-only; positioning bounds `range_start_year: 70`, `range_end_year: present`, `range_uncertainty: moderate`. `branches_from` ENT-0012 qualifier `reform` (warrant CLM-0094) — **least-wrong under protest**: the controlled list has no value for main-line continuation; `reform_qualifier_fit` graded Low to encode the vocabulary strain, with a routed recommendation for a new `continuation`/`main-line` qualifier (Anchor Fit centerpiece). Metaphysical/neutrality bracket acute — no "residue" framing. Pending Critical Review and structural validation.|

# End ENT-0014
