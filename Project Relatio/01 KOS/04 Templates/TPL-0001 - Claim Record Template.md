---
title: TPL-0001 - Claim Record Template
document_type: Template
version: 1.3
status: Adopted
operational_status: Active
created: 2026-07-09
template_type: Claim Record
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - STD-0002 Metadata & YAML Standard
related_documents:
  - CLM-0001 Non-Striving Convergence
tags:
  - ProjectRelatio
  - Templates
  - ClaimRecord
---

# TPL-0001 — Claim Record Template

## Adopted Template

> **How to use:** Copy the block below into a new `CLM-NNNN - <Title>.md` file. Replace every `<…>` placeholder. The frontmatter satisfies STD-0002 (metadata layer); the body satisfies KOS-0003 §12 (content layer) as required by KOS-0012. Delete this instruction block and the horizontal rule above the template.
>
> *(Obsidian note (RRI): this is a plain-Markdown template; Templater variables — e.g. `<% tp.date.now() %>` — may be layered on in the implementation without changing the structure.)*

---

```markdown
---
title: CLM-NNNN - <Short Claim Title>
document_type: Claim Record
version: 0.1
status: Draft
operational_status: Active
created: <YYYY-MM-DD>
category:
  - Knowledge Base
  - Claim
  - <Topic>
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - <INV-NNNN parent investigation>
related_documents:
  - <SRC-NNNN source(s)>
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - <TopicTag>
relationships:            # typed (STD-0002 §7 / STD-0004) — prefer the most specific type
  - type: derived_from
    target: <SRC-NNNN>
  - type: supports
    target: <FND-NNNN>
  - type: part_of
    target: <INV-NNNN>
confidence:               # epistemic axis (STD-0008 / STD-0002 §11) — ALWAYS a list; one item (component: overall) for a single grade, one item per component for a split grade (never averaged)
  - component: overall
    level: <1-5>
    label: <matching STD-0008 §5.1 label — Very High/High/Moderate/Low/Very Low>
    # bounded_by: [<SRC-NNNN>]   # OPTIONAL — only where this component's dependencies differ from the record's derived_from edges (STD-0009 §9); entries must resolve (graph claims, STD-0002 §12.1)
reliance_tier: R0         # R0/R1/R2 per ADR-GOV-0006; floor roll-up across load-bearing loci
reliance_note: <provenance of the tier — e.g. verification posture at closure>
review_cycle: <months>    # from STD-0009 §7 cadence (weakest confidence component; ×1.5 if all load-bearing loci R1/R2)
review_date: <YYYY-MM-DD>       # next review due = last_reviewed + review_cycle
last_reviewed: <YYYY-MM-DD>     # most recent review act (at creation: the closure date)
---

# CLM-NNNN

# <Short Claim Title>

## Draft Claim Record

---

# Claim
> <The claim, stated as a single proposition.>

# Claim Type (KOS-0003 §3)
<Descriptive | Causal | Interpretive | Predictive | Normative | Metaphysical> — <why>.

# Evidence (KOS-0003 §4)
Type: <Empirical | Historical | Philosophical | Experiential | Traditional | Testimonial>.
- <evidence item, with source reference>

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: <0–5> — <note>
- Relevance: <0–5> — <note>
- Independence: <0–5> — <note>
- Quality: <0–5> — <note>
- Limitations: <what this evidence does NOT establish>

# Source Evaluation
<Reference the SRC record(s); note authority/transparency/independence/intent.>

# Assumptions (KOS-0003 §10)
- <ontological | epistemological | methodological | cultural | linguistic assumptions>

# Reasoning (KOS-0003 §7)
<Deductive | Inductive | Abductive | Analogical> — <the inference>. Reasoning risks checked: <…>.

# Confidence (KOS-0003 §8)
Level <0–5> (<Very High | High | Moderate | Low | Very Low | Unsupported>) — <justification>.

# Limitations
- <bounds of the claim>

# Alternative Interpretations
1. <alternative> — <accepted/rejected + why>

# Relationships (STD-0004)
- `derived_from` <…>
- `contrasts_with` / `related_to` / `supports` <…>
- `part_of` <INV-NNNN>

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|<YYYY-MM-DD>|Draft|Created|

# End CLM-NNNN
```

---

# Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial Claim Record template; encodes STD-0002 + KOS-0003 §12 per KOS-0012|
|1.1|2026-07-11|Adopted|Confidence line updated to the canonical hybrid **Level N (Label)** format (GB-2026-021).|
|1.2|2026-07-11|Adopted|Added `operational_status` (GB-2026-006) and the typed `relationships` example (GB-2026-001) to the object frontmatter block.|
|1.3|2026-07-21|Adopted|Frontmatter skeleton gains the epistemic fields (`confidence` list with optional `bounded_by`, `reliance_tier`, `reliance_note` — STD-0008 / STD-0002 §11) and the review fields (`review_cycle`, `review_date`, `last_reviewed` — STD-0009 §8) with placeholder guidance, per ADR-GOV-0008: new Claim Records are born conformant and review-ready.|

---

# End TPL-0001
