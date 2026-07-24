---
title: ENT-0014 - Rabbinic Judaism
document_type: Entity Record
version: 0.4
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
rendering_class: tradition
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
    qualifier: continuation
  - type: derived_from
    target: SRC-0142
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
- **tradition_type:** `reform` — Rabbinic Judaism reconstituted an existing tradition (Second Temple Judaism, most directly the Pharisaic stream) around Torah study and halakhah after the Temple's loss, rather than emerging fresh or being founder-attributed. **Note (§2.8) — the two `reform` vocabularies (disambiguation, resolved).** This `tradition_type` value `reform` is a **different vocabulary** from the `branches_from` **qualifier** on the lineage edge below — different fields, never conflated (the disambiguation is now lifted to STD-0004 §7.2 per ADR-GOV-0010 D3). **The earlier double-`reform` coincidence no longer arises on this edge:** the anchor-vocabulary review (ADR-GOV-0010 D1) added a `continuation` qualifier, and the lineage edge has been re-qualified `reform` → **`continuation`** (D2). The `tradition_type` field is a **separate question and is left unchanged** (ADR-GOV-0010 D2): `reform` (with `emergent` the defensible alternative) still captures that Rabbinic Judaism reconstituted a prior tradition; only the lineage qualifier moved.

# 3. Dating (dates are claims — ADR-GOV-0009 D3)
- `dating_claims`: **CLM-0094** — post-70 CE consolidation (the rabbinic movement after the Temple's destruction; Yavneh/Yohanan ben Zakkai the conventional early locus), with the Mishnah's redaction c. 200 CE (under Judah ha-Nasi) as the standard dating anchor; the consolidation *process* is contested. The **claim** carries the sourced, graded content; `display_range` ("post-70 CE (Mishnah c. 200 CE)") is render-only.
- **Render-only positioning bounds (STD-0002 §11 v1.11):** `range_start_year: 70`, `range_end_year: present`, `range_uncertainty: moderate`. Derived from and bounded by CLM-0094 — start at 70 CE (the destruction that triggers the consolidation); `present` because Rabbinic Judaism is the living mainline of Judaism today; `moderate` inherits CLM-0094's Moderate emergence-dating component. Non-evidential; `display_range` remains authoritative.

# 4. Lineage (branches_from — PROVISIONAL, ADR-GOV-0009 D4)
- `branches_from` **ENT-0012 (Second Temple Judaism)** — qualifier **`continuation`** (re-qualified from `reform` per ADR-GOV-0010 D2). **Warrant:** CLM-0094 (element (ii)) — Rabbinic Judaism continues the Second-Temple tradition as its **main line** (most directly the Pharisaic stream), reconstituted around Torah and halakhah after the Temple's loss. The edge renders; CLM-0094 warrants.
- **THE ANCHOR STRESS-TEST — now RESOLVED by ADR-GOV-0010 (this edge is the case that drove the fix):** the controlled qualifier list, as it stood at INV-0017 (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed`), **contained no right word for MAIN-LINE CONTINUATION.** `reform` was applied **least-wrong under protest** — it connotes departure-with-change, whereas Rabbinic Judaism is the **least-departed** line, the parent's own line carried forward, not a departure — and CLM-0094's qualifier-fit component was graded **Low** to encode that **vocabulary strain (not doubt about the descent, which is Moderate)**. The anchor-vocabulary review (ADR-GOV-0009 §7(a)) **acted on that routed recommendation: ADR-GOV-0010 D1 added a `continuation` qualifier to STD-0004 §7.2, and D2 re-qualified this edge `reform` → `continuation`.** The edge now carries its right word; CLM-0094's fit component is renamed `continuation_qualifier_fit` and re-graded to its honest level under the correct qualifier (the descent grade, Moderate, is unchanged — only the word changed). **The list stays PROVISIONAL (ADR-GOV-0010 D5) — this is additive repair of a demonstrated gap, not a graduation of the anchors.** **Neutrality note:** the edge does **not** frame Rabbinic Judaism as a "residue" left by Christianity; both branches descend from the shared parent and neither is the normatively "true" continuation.

# 5. Relationships (STD-0004)
- `branches_from` ENT-0012 (qualifier `continuation`, re-qualified from `reform` per ADR-GOV-0010 D2) — warranted by CLM-0094.
- `derived_from` SRC-0142 (Strack–Stemberger — Mishnah dating), SRC-0138 (Cohen — the Second-Temple→rabbinic bridge).

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-22|Draft|Created at INV-0017 circuit — the **continuation / main-line branch and the anchor stress-test**; born timeline-ready (TPL-0006 v1.1 / STD-0002 v1.11). `tradition_type: reform` (reconstituted an existing tradition; noted DISTINCT from the qualifier `reform` per §2.8 — same word, different vocabulary; emergent alternative flagged); `dating_claims` CLM-0094 (post-70 CE; Mishnah c. 200 CE); `display_range` render-only; positioning bounds `range_start_year: 70`, `range_end_year: present`, `range_uncertainty: moderate`. `branches_from` ENT-0012 qualifier `reform` (warrant CLM-0094) — **least-wrong under protest**: the controlled list has no value for main-line continuation; `reform_qualifier_fit` graded Low to encode the vocabulary strain, with a routed recommendation for a new `continuation`/`main-line` qualifier (Anchor Fit centerpiece). Metaphysical/neutrality bracket acute — no "residue" framing. Pending Critical Review and structural validation.|
|0.2|2026-07-22|Draft|**Anchor stress-test RESOLVED — ADR-GOV-0010 enactment (D2).** The routed recommendation was adopted: ADR-GOV-0010 D1 added a `continuation` qualifier (STD-0004 v1.3), and this edge is re-qualified **`branches_from` ENT-0012 `reform` → `continuation`** (frontmatter + §4 Lineage + §5). §2.8 note updated: the double-`reform` coincidence no longer arises on this edge (the disambiguation is lifted to STD-0004 §7.2 per D3); `tradition_type` **left `reform` unchanged** (a separate field, ADR-GOV-0010 D2). Warrant CLM-0094 concurrently re-graded (component renamed `continuation_qualifier_fit`, Low → Moderate; descent grade unchanged). Anchors stay PROVISIONAL (ADR-GOV-0010 D5) — additive repair, not graduation.|
|0.3|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|
|0.4|2026-07-24|Draft|**ADR-GOV-0012 D3 backfill.** Added `rendering_class: tradition`, declaring the resolution this entity occupies now that the entity layer is multi-granularity (D2). **Field addition and this history row ONLY — no other content in this record changed.** Migration discipline: define → backfill → enforce; the validator's presence check is promoted from warning to error level in the commit immediately after this one. The entity gap recorded on this record by INV-0018 **stands as history** — the community entities minted under D8 are the remedy, not a retrofit, and no part of that record is revised here.|

# End ENT-0014
