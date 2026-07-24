---
title: TPL-0006 - Entity Record Template
document_type: Template
version: 1.4
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
> **Three classes:**
> - **Concept class** — the shape of the existing seven entities (ENT-0001…ENT-0007). Outside the timeline program: carries **no** `rendering_class` and **no** tradition or community fields.
> - **Tradition class** — a religious tradition (ADR-GOV-0009 D2/D3). Carries `rendering_class: tradition` plus `tradition_type`, `dating_claims`, and `display_range`; may carry `branches_from` lineage edges. **Created on demand** as an investigation reaches the tradition — no pre-populated gazetteer (ADR-GOV-0009 D2).
> - **Community class** — a regionally or temporally bounded population or expression, the resolution *below* the tradition-whole (ADR-GOV-0012 D2/D4/D8). Carries `rendering_class: community` plus `attestation_claims`, `attestation_window`, and `attestation_uncertainty`; binds to the tradition layer by the **non-evidential** `projects_to` relation. **Off-timeline at launch** (ADR-GOV-0012 D7).
>
> *(A fourth class, `substrate`, is established by ADR-GOV-0012 D2 but has **no field set and no skeleton**: substrate rendering is deferred by D7 and no substrate entity is minted. Do not invent one.)*
>
> Choose one skeleton; do **not** mix them. The tradition trio and the community trio are each required-together, mutually exclusive, and forbidden on concept entities; a community entity additionally may **never** carry the render-only positioning bounds — it has an **attestation window, not a founding date**. The validator enforces all of this at error level (STD-0002 §11).

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
rendering_class: tradition     # REQUIRED AT MINT — tradition | substrate | community (STD-0002 §11 / ADR-GOV-0012 D3)
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

## Community-class skeleton (ADR-GOV-0012)

```markdown
---
title: ENT-NNNN - <Community Name at honest precision>
document_type: Entity Record
version: 0.1
status: Draft
operational_status: Active
created: <YYYY-MM-DD>
category:
  - Knowledge Base
  - Entity
  - Community
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0004 Ontological Framework & Reality Modeling System
related_documents:
  - <INV-NNNN whose closed record warrants this entity>
  - <CLM-NNNN / FND-NNNN attesting claims>
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Entity
  - Community
  - <TopicTag>
rendering_class: community     # REQUIRED AT MINT (STD-0002 §11 / ADR-GOV-0012 D3)
# --- Attestation window, NOT a founding date (ADR-GOV-0012 D4) ---
attestation_claims:            # graph-claim pointers to the graded record(s) attesting this community (§12.1 — must resolve)
  - <CLM-NNNN>
  - <FND-NNNN>
attestation_window: "<e.g. 7th c. CE — the period of documented contact>"   # render-only string; a WINDOW, never a founding date
attestation_uncertainty: <low | moderate | high>   # from the WEAKEST TEMPORALLY RELEVANT component of the warranting record(s)
# NO tradition_type / dating_claims / display_range, and NO range_start_year /
# range_end_year / range_uncertainty. A community entity has no numeric geometry
# and no founding-date-style bar — that is the point of the class.
relationships:            # typed (STD-0002 §7 / STD-0004)
  - type: projects_to     # NON-EVIDENTIAL rendering projection → a tradition-class entity (STD-0004 §7.3)
    target: <ENT-NNNN tradition entity>
    # no qualifier, no warrant, no confidence — any of them makes the entry malformed
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

# <Community Name>

## Draft Entity Record

---

# 1. Identification
**Community:** <name at honest precision — never more specific than the warranting record supports>.
**Region / period:** <…>.
**Internal plurality:** <what the record does NOT resolve about this community, held inside the entity rather than split into entities the record cannot warrant>.

# 2. Classification (KOS-0004)
- **Entity category (KOS-0004 §6):** Social Entity — a religious community.
- **Reality layer (KOS-0004 §4):** Layer 4 (Social) with Layer 5 (Abstract) doctrinal content.
- **rendering_class:** `community` — <one line on why this is a community-resolution object and not a tradition>.

# 3. Attestation window (NOT a founding date — ADR-GOV-0012 D4)
- `attestation_claims`: <CLM-NNNN / FND-NNNN — one line each>. The entity fields point; the **records** carry the graded content.
- **Window:** `<attestation_window>` — **derived from** <which component of which record>, and stating *when the record attests this community*, **not** when it began or ended. The community's own beginning and terminus are **not dated by the record**, and no bound is invented for them.
- **`attestation_uncertainty`:** `<value>` — inherits the **weakest TEMPORALLY RELEVANT** component of the warranting record(s) (<name it, with its level/label>). **Excluded as non-temporal:** <name each excluded component and say what it grades instead> — the same exclusion STD-0002 v1.11 established for `range_uncertainty`.
- **Not minted as anything finer.** <If the record named finer bodies it could not distinguish, say so here.>

# 4. Projection (projects_to — NON-EVIDENTIAL, ADR-GOV-0012 D5)
- `projects_to` <ENT-NNNN> — **a rendering instruction, not a historical relationship.** It says "for display, re-anchor here"; it asserts **nothing** about descent, membership, or institutional continuity between this community and that tradition, and it carries no qualifier, no warrant, and no confidence. Any substantive relationship remains a claim, graded in the normal way.

# 5. Relationships (STD-0004)
- `projects_to` <ENT-NNNN>
- <inbound `influenced_by` edges live on the INFLUENCED entity, not here — the edge sits on the receiving tradition>

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
|1.4|2026-07-24|Adopted|**Made the template mint ADR-GOV-0012-conformant entities.** Added the REQUIRED-AT-MINT `rendering_class` field to the tradition-class skeleton (D3) and added a third, **community-class skeleton** (D2/D4/D8): `rendering_class: community`, the attestation-window trio (`attestation_claims` / `attestation_window` / `attestation_uncertainty`), a `projects_to` example with its no-qualifier/no-warrant/no-confidence rule stated inline, and a body whose §3 forces the derivation to be shown — which component the window comes from, and **which components were excluded as non-temporal and what they grade instead**. The skeleton carries **no** tradition fields and **no** render-only positioning bounds, and says why: a community entity has an **attestation window, not a founding date**, so it has no numeric geometry to draw. The `substrate` class is named in the how-to-use note as **established but skeleton-less** (D7 defers its build) so no session invents one. Concept-class skeleton unchanged except for the note that it carries no `rendering_class`. **Not named in ADR-GOV-0012 §5's affected-objects list, and updated anyway on a mechanical reading of D3:** a field required *at mint* whose mint instrument does not emit it would make every future entity born non-conformant. Template-side only — no field, rule, or vocabulary was decided here that STD-0002 v1.13 and STD-0004 v1.5 do not already carry.|

---

# End TPL-0006
