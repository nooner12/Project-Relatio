---
title: TPL-0002 - Source Record Template
document_type: Template
version: 1.3
status: Adopted
operational_status: Active
created: 2026-07-09
template_type: Source Record
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - STD-0002 Metadata & YAML Standard
related_documents:
  - SRC-0001 Canonical Gospels
tags:
  - ProjectRelatio
  - Templates
  - SourceRecord
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# TPL-0002 — Source Record Template

## Adopted Template

> **How to use:** Copy the block below into a new `SRC-NNNN - <Title>.md` file. Replace every `<…>` placeholder. Body structure follows KOS-0012 §5.4 (uses KOS-0003 §6 source evaluation). For non-modern sources (anonymous/composite/ancient), record honest qualifications in the metadata fields rather than forcing a single author/date (open item: STD-0002 §11 refinement).

---

```markdown
---
title: SRC-NNNN - <Source Title>
document_type: Source Record
version: 0.1
status: Draft
operational_status: Active
created: <YYYY-MM-DD>
category:
  - Knowledge Base
  - Source
  - <Primary Text | Secondary | Dataset | …>
source_author: <author, or "anonymous/composite — <note>">
source_url: <url, or "n/a — <edition/translation pointer>">
publication_date: <YYYY-MM-DD, or composition range/"n/a">
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - <INV-NNNN / SRC-NNNN>
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Source
  - <TopicTag>
relationships:            # typed (STD-0002 §7 / STD-0004) — prefer the most specific type
  - type: supports
    target: <CLM-NNNN>
  - type: related_to
    target: <SRC-NNNN>
attribution:              # provenance (STD-0002 §6 / ADR-GOV-0011 Decision B) — REQUIRED
  - actor: <named human>                 # an AI is never the actor; disclose it below
    role: <ROLE-NNNN … or free string>   # no controlled enum (ADR-GOV-0011 §7)
    event: created                       # the only Stage 1 value; Stage 2 adds entries, not keys
    date: <YYYY-MM-DD>
    ai_degree: ai-delegated              # unassisted | ai-assisted | ai-delegated
    ai_model_family: Claude              # vendor/family free string; `none` iff unassisted
---

# SRC-NNNN

# <Source Title>

## Draft Source Record

---

# 1. Identification
<What the source is; how it is cited in this KB.>

# 2. Source Evaluation (KOS-0003 §6)
- Authority: <…>
- Transparency: <…>
- Independence: <…>
- Intent: <…>

# 3. Limitations
- <what this source does NOT establish>

# 4. Key Content / Passages Used
- <passages/data used by dependent claims>

# 5. Relationships (STD-0004)
- `related_to` / `derived_from` <…>

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|<YYYY-MM-DD>|Draft|Created|

# End SRC-NNNN
```

---

# Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial Source Record template; encodes STD-0002 + KOS-0012 §5.4 (KOS-0003 §6)|
|1.1|2026-07-11|Adopted|Added `operational_status` (GB-2026-006) and the typed `relationships` example (GB-2026-001) to the object frontmatter block.|
|1.2|2026-07-22|Adopted|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|
|1.3|2026-07-22|Adopted|Added the required `attribution` stub to the emitted frontmatter (STD-0002 v1.12 §6 / ADR-GOV-0011 Decision B), so records created from this template are **born conformant** against the now-error-level attribution check. Template-side only — no field, rule, or body section changed.|

---

# End TPL-0002
