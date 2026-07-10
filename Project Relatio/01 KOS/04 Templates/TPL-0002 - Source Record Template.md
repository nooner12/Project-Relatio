---
title: TPL-0002 - Source Record Template
document_type: Template
version: 1.0
status: Adopted
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

---

# End TPL-0002
