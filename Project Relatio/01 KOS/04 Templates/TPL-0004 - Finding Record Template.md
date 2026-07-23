---
title: TPL-0004 - Finding Record Template
document_type: Template
version: 1.5
status: Adopted
operational_status: Active
created: 2026-07-09
template_type: Finding Record
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0010 Reasoning & Synthesis Framework
  - STD-0002 Metadata & YAML Standard
tags:
  - ProjectRelatio
  - Templates
  - FindingRecord
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# TPL-0004 — Finding Record Template

## Adopted Template

> **How to use:** Copy the block below into a new `FND-NNNN - <Title>.md` file. A Finding is a synthesized answer/conclusion — a first-class, citable, confidence-rated object distinct from the Investigation that produced it and the Claims that support it. Body structure follows KOS-0012 §5.2.

---

```markdown
---
title: FND-NNNN - <Finding Title>
document_type: Finding Record
version: 0.1
status: Draft
operational_status: Active
created: <YYYY-MM-DD>
category:
  - Knowledge Base
  - Finding
  - <Topic>
parent_documents:
  - <INV-NNNN parent investigation>
  - KOS-0010 Reasoning & Synthesis Framework
related_documents:
  - <CLM-NNNN supporting claims>
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Finding
  - <TopicTag>
relationships:            # typed (STD-0002 §7 / STD-0004) — prefer the most specific type
  - type: derived_from
    target: <CLM-NNNN>
  - type: part_of
    target: <INV-NNNN>
confidence:               # epistemic axis (STD-0008 / STD-0002 §11) — ALWAYS a list; one item (component: overall) for a single grade, one item per component for a split/layered verdict (never averaged)
  - component: overall
    level: <1-5>
    label: <matching STD-0008 §5.1 label — Very High/High/Moderate/Low/Very Low>
    # bounded_by: [<CLM-NNNN>]   # OPTIONAL — only where this component's dependencies differ from the record's derived_from edges (STD-0009 §9); entries must resolve (graph claims, STD-0002 §12.1)
reliance_tier: R0         # R0/R1/R2 per ADR-GOV-0006; floor roll-up across load-bearing loci
reliance_note: <provenance of the tier — e.g. verification posture at closure>
review_cycle: <months>    # from STD-0009 §7 cadence (weakest confidence component; ×1.5 if all load-bearing loci R1/R2)
review_date: <YYYY-MM-DD>       # next review due = last_reviewed + review_cycle
last_reviewed: <YYYY-MM-DD>     # most recent review act (at creation: the closure date)
attribution:              # provenance (STD-0002 §6 / ADR-GOV-0011 Decision B) — REQUIRED
  - actor: <named human>                 # an AI is never the actor; disclose it below
    role: <ROLE-NNNN … or free string>   # no controlled enum (ADR-GOV-0011 §7)
    event: created                       # the only Stage 1 value; Stage 2 adds entries, not keys
    date: <YYYY-MM-DD>
    ai_degree: ai-delegated              # unassisted | ai-assisted | ai-delegated
    ai_model_family: Claude              # vendor/family free string; `none` iff unassisted
---

# FND-NNNN

# <Finding Title>

## Draft Finding Record

---

# 1. Statement
> <The finding, as a single proposition.>

# 2. Supporting Claims
- <CLM-NNNN — one line on how it supports this finding>

# 3. Confidence (KOS-0003 §8)
Level <0–5> (<Very High | High | Moderate | Low | Very Low | Unsupported>) — <justification; note if lower than the weakest supporting claim>.

# 4. Scope & Limitations
- <what the finding does and does not cover>

# 5. Relationships (STD-0004)
- `derived_from` <CLM-NNNN…>
- `part_of` <INV-NNNN>

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|<YYYY-MM-DD>|Draft|Created|

# End FND-NNNN
```

---

# Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial Finding Record template; encodes STD-0002 + KOS-0012 §5.2|
|1.1|2026-07-11|Adopted|Confidence line updated to the canonical hybrid **Level N (Label)** format (GB-2026-021).|
|1.2|2026-07-11|Adopted|Added `operational_status` (GB-2026-006) and the typed `relationships` example (GB-2026-001) to the object frontmatter block.|
|1.3|2026-07-21|Adopted|Frontmatter skeleton gains the epistemic fields (`confidence` list with optional `bounded_by`, `reliance_tier`, `reliance_note` — STD-0008 / STD-0002 §11) and the review fields (`review_cycle`, `review_date`, `last_reviewed` — STD-0009 §8) with placeholder guidance, per ADR-GOV-0008: new Finding Records are born conformant and review-ready.|
|1.4|2026-07-22|Adopted|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|
|1.5|2026-07-22|Adopted|Added the required `attribution` stub to the emitted frontmatter (STD-0002 v1.12 §6 / ADR-GOV-0011 Decision B), so records created from this template are **born conformant** against the now-error-level attribution check. Template-side only — no field, rule, or body section changed.|

---

# End TPL-0004
