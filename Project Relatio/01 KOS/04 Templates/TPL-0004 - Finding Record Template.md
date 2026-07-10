---
title: TPL-0004 - Finding Record Template
document_type: Template
version: 1.0
status: Adopted
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
Level <0–5> — <justification; note if lower than the weakest supporting claim>.

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

---

# End TPL-0004
