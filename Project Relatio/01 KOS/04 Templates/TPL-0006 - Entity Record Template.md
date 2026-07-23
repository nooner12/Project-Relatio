---
title: TPL-0006 - Entity Record Template
document_type: Template
version: 1.3
status: Adopted
operational_status: Active
created: 2026-07-21
template_type: Entity Record
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0004 Ontological Framework & Reality Modeling System
  - STD-0002 Metadata & YAML Standard
  - STD-0004 Relationship & Linking Standard
related_documents:
  - ADR-GOV-0009 - World-Religions Timeline Program and Lineage Anchors
tags:
  - ProjectRelatio
  - Templates
  - EntityRecord
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-21
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# TPL-0006 — Entity Record Template

## Adopted Template

> **How to use:** Copy the matching skeleton below into a new `ENT-NNNN - <Title>.md` file. An Entity is a modelled thing — a concept, an entity, or (per ADR-GOV-0009) a religious tradition — that claims and findings attach to. Body structure follows KOS-0012 §5.5 and the classification in KOS-0004 §4/§6.
>
> **Two classes:**
> - **Concept class** — the shape of the existing seven entities (ENT-0001…ENT-0007). Carries **no** tradition fields.
> - **Tradition class** — a religious tradition (ADR-GOV-0009 D2/D3). Adds `tradition_type`, `dating_claims`, and `display_range`; may carry `branches_from` lineage edges. **Created on demand** as an investigation reaches the tradition — no pre-populated gazetteer (ADR-GOV-0009 D2).
>
> Choose one skeleton; do **not** mix them (the tradition fields are required-together and forbidden on concept entities — the validator enforces this at error level, STD-0002 §11).

---

## Concept-class skeleton

```markdown
---
title: ENT-NNNN - <Concept Name>
document_type: Entity Record
version: 0.1
status: Draft
operational_status: Active
created: <YYYY-MM-DD>
category:
  - Knowledge Base
  - Entity
  - Concept
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0004 Ontological Framework & Reality Modeling System
related_documents:
  - <SRC-NNNN / CLM-NNNN / INV-NNNN referencing this entity>
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - <TopicTag>
relationships:            # typed (STD-0002 §7 / STD-0004) — prefer the most specific type
  - type: related_to
    target: <ENT-NNNN>
  - type: derived_from
    target: <SRC-NNNN>
attribution:              # provenance (STD-0002 §6 / ADR-GOV-0011 Decision B) — REQUIRED
  - actor: <named human>                 # an AI is never the actor; disclose it below
    role: <ROLE-NNNN … or free string>   # no controlled enum (ADR-GOV-0011 §7)
    event: created                       # the only Stage 1 value; Stage 2 adds entries, not keys
    date: <YYYY-MM-DD>
    ai_degree: ai-delegated              # unassisted | ai-assisted | ai-delegated
    ai_model_family: Claude              # vendor/family free string; `none` iff unassisted
---

# ENT-NNNN

# <Concept Name>

## Draft Entity Record

---

# 1. Identification
**Term:** <term / label>.
**Domain:** <field or tradition in which it is defined>.

# 2. Definition
<A precise definition of the entity.>

# 3. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** <Physical | Biological | Psychological | Social | Abstract>.
- **Reality layer (KOS-0004 §4):** <Layer N …>.

# 4. Related Concepts
- <[[ENT-NNNN - …]] — one line on the relationship>

# 5. Relationships (STD-0004)
- `related_to` <ENT-NNNN>
- `derived_from` <SRC-NNNN>

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|<YYYY-MM-DD>|Draft|Created|

# End ENT-NNNN
```

---

## Tradition-class skeleton (ADR-GOV-0009)

```markdown
---
title: ENT-NNNN - <Tradition Name>
document_type: Entity Record
version: 0.1
status: Draft
operational_status: Active
created: <YYYY-MM-DD>
category:
  - Knowledge Base
  - Entity
  - Tradition
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0004 Ontological Framework & Reality Modeling System
related_documents:
  - <INV-NNNN origins-and-branching investigation>
  - <CLM-NNNN dating / lineage claims>
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Tradition
  - <TraditionTag>
tradition_type: founded        # founded | emergent | reform | syncretic (STD-0002 §11)
dating_claims:                 # graph-claim pointers to the graded dating claim(s) (§12.1 — must resolve)
  - <CLM-NNNN>
display_range: "<e.g. 3rd c. CE>"   # render-only string; the claims carry the truth and the contestedness
# --- Render-only positioning bounds (STD-0002 §11 v1.11 — OPTIONAL; for the SVG timeline) ---
# Render-only, NON-EVIDENTIAL: derived from and bounded by the dating claim; display_range stays authoritative;
# range_uncertainty maps from the dating claim's (weakest) emergence-dating-component confidence (STD-0002 v1.11).
# OPTIONAL as a set — omit all three and the tradition renders in the "undated / sequence-only" fallback lane.
# If ANY is present, range_start_year + range_uncertainty are co-required (range_end_year may be omitted).
range_start_year: <int; negative = BCE>        # render-only, dating-claim-derived
range_end_year: <int, or: present>             # render-only
range_uncertainty: <low | moderate | high>     # from dating-claim confidence
relationships:            # typed (STD-0002 §7 / STD-0004)
  - type: branches_from   # PROVISIONAL, ENT → ENT only, qualifier REQUIRED (STD-0004 §7.2)
    target: <ENT-NNNN parent tradition>
    qualifier: schism      # schism | reform | syncretic-descent | heterodox-offshoot | disputed
  - type: derived_from
    target: <SRC-NNNN>
attribution:              # provenance (STD-0002 §6 / ADR-GOV-0011 Decision B) — REQUIRED
  - actor: <named human>                 # an AI is never the actor; disclose it below
    role: <ROLE-NNNN … or free string>   # no controlled enum (ADR-GOV-0011 §7)
    event: created                       # the only Stage 1 value; Stage 2 adds entries, not keys
    date: <YYYY-MM-DD>
    ai_degree: ai-delegated              # unassisted | ai-assisted | ai-delegated
    ai_model_family: Claude              # vendor/family free string; `none` iff unassisted
---

# ENT-NNNN

# <Tradition Name>

## Draft Entity Record

---

# 1. Identification
**Tradition:** <name, and principal alternative names>.
**Region / language of origin:** <…>.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious tradition.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **tradition_type:** <founded | emergent | reform | syncretic> — <one line justifying the category>.

# 3. Dating (dates are claims — ADR-GOV-0009 D3)
- `dating_claims`: <CLM-NNNN — one line each>. The entity fields point; the **claims** carry the sourced, graded, epistemic-fielded date. `display_range` is render-only.
- **Render-only positioning bounds (STD-0002 §11 v1.11 — OPTIONAL):** `range_start_year` / `range_end_year` / `range_uncertainty` exist only so the SVG timeline can position the bar. They are **non-evidential**, **derived from and bounded by the dating claim**, and inherit its confidence — a bar never renders more certain than the claim behind it. `display_range` remains authoritative; `range_uncertainty` maps from the (weakest) emergence-dating component's confidence. Omit all three to render in the "undated / sequence-only" fallback lane; never invent coordinates.

# 4. Lineage (branches_from — PROVISIONAL, ADR-GOV-0009 D4)
- `branches_from` <ENT-NNNN> — qualifier `<…>`. **Warrant rule:** this edge MUST be supported by a graded claim asserting the descent (the edge renders; the claim warrants). An unwarranted edge is a graph-integrity error. Record the warranting <CLM-NNNN> here.

# 5. Relationships (STD-0004)
- `branches_from` <ENT-NNNN> (qualifier `<…>`)
- `derived_from` <SRC-NNNN>

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|<YYYY-MM-DD>|Draft|Created|

# End ENT-NNNN
```

---

# Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-21|Adopted|Initial Entity Record template, closing the gap the seven hand-authored entities (ENT-0001…0007) predated. Two skeletons: **concept-class** (the existing entities' shape) and **tradition-class** (adding `tradition_type`/`dating_claims`/`display_range` and a `branches_from`+`qualifier` example), enacting ADR-GOV-0009 D2/D3/D4 and STD-0002 v1.10 / STD-0004 v1.2. States the warrant rule for lineage edges. Registered TPL-0006.|
|1.1|2026-07-22|Adopted|Added the three STD-0002 §11 v1.11 render-only positioning fields (`range_start_year`/`range_end_year`/`range_uncertainty`) to the tradition-class skeleton with placeholder guidance, the OPTIONAL/co-requirement rule, and the render-only/non-evidential honesty note; added a §3 dating note on the same. Concept-class skeleton unchanged. Owner-ratified template refresh (INV-0017 prep brief); makes tradition entities born-conformant with v1.11 so the timeline bounds need not be hand-added post hoc as at INV-0016.|
|1.2|2026-07-22|Adopted|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|
|1.3|2026-07-22|Adopted|Added the required `attribution` stub to the emitted frontmatter (STD-0002 v1.12 §6 / ADR-GOV-0011 Decision B), so records created from this template are **born conformant** against the now-error-level attribution check. Template-side only — no field, rule, or body section changed.|

---

# End TPL-0006
