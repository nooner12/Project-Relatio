---
title: TPL-0003 - Investigation Record Template
document_type: Template
version: 1.1
status: Adopted
operational_status: Active
created: 2026-07-09
template_type: Investigation Record
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0008 Research Methodology & Investigation Framework
  - STD-0002 Metadata & YAML Standard
related_documents:
  - INV-0001 Comparative Teachings of Jesus and Philosophical Daoism
tags:
  - ProjectRelatio
  - Templates
  - InvestigationRecord
---

# TPL-0003 — Investigation Record Template

## Adopted Template

> **How to use:** Copy the block below into a new `INV-NNNN - <Title>.md` file (typically the anchor of an investigation folder in `06 Knowledge Base/`). Body structure follows KOS-0012 §5.1. An Investigation frames Source and Claim records and produces Finding records.

---

```markdown
---
title: INV-NNNN - <Investigation Title>
document_type: Investigation Record
version: 0.1
status: Draft
operational_status: Active
created: <YYYY-MM-DD>
category:
  - Knowledge Base
  - <Domain>
  - Investigation
parent_documents:
  - KOS-0008 Research Methodology & Investigation Framework
  - KOS-0007 Comparative Analysis Framework   # if comparative
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - <SRC-NNNN…>
  - <CLM-NNNN…>
  - <FND-NNNN…>
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Investigation
  - <TopicTag>
relationships:            # typed (STD-0002 §7 / STD-0004) — prefer the most specific type
  - type: derived_from
    target: <SRC-NNNN>
  - type: related_to
    target: <INV-NNNN>
---

# INV-NNNN

# <Investigation Title>

## Draft Investigation Record

---

# 1. Research Question
Original: <as posed>
Refined: <refined question + rationale for refinement>

# 2. Scope & Disambiguation
<What is in/out of scope; disambiguate ambiguous terms and corpora.>

# 3. Method
<Which frameworks/pipeline; how claims and sources are handled.>

# 4. Findings / Synthesis
<The answer. Reference FND-NNNN records, or state findings inline.>

# 5. Confidence Summary (KOS-0003 §8)
<Per-finding confidence levels.>

# 6. Assumptions & Bracketing (KOS-0003 §10)
- <assumptions; what is deliberately bracketed>

# 7. Relationships (STD-0004)
- `derived_from` <SRC…>
- `part_of` the Knowledge Base

# 8. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|<YYYY-MM-DD>|Draft|Created|

# End INV-NNNN
```

---

# Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial Investigation Record template; encodes STD-0002 + KOS-0012 §5.1|
|1.1|2026-07-11|Adopted|Added `operational_status` (GB-2026-006) and the typed `relationships` example (GB-2026-001) to the object frontmatter block.|

---

# End TPL-0003
