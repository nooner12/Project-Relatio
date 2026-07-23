---
title: INV-0003 - Wu Wei
document_type: Investigation Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Base
  - Chinese Philosophy
  - Investigation
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0008 Research Methodology & Investigation Framework
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - ENT-0001 Wu Wei
  - ENT-0002 Ziran
  - SRC-0002 Philosophical Daoist Corpus
  - SRC-0005 Slingerland Effortless Action
  - CLM-0005 Wu Wei as Effortless Action
  - CLM-0006 Three Interpretive Registers
  - FND-0003 Wu Wei as Non-Forcing Action
  - Third-Run Assessment - RQ-0003
tags:
  - ProjectRelatio
  - KnowledgeBase
  - WuWei
  - Investigation
relationships:
  - type: derived_from
    target: SRC-0002
  - type: derived_from
    target: SRC-0005
  - type: related_to
    target: ENT-0001
  - type: related_to
    target: ENT-0002
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# INV-0003

# Wu Wei

## Draft Investigation Record

> Third research workflow. Focal point: the concept *wu wei* as a first-class **Entity** ([[ENT-0001 - Wu Wei]]). Purpose beyond the answer: exercise the **Entity type** and test whether the Knowledge Base functions as a **graph** — *wu wei* is shared across INV-0001 and INV-0003, and a source (SRC-0002) is reused rather than duplicated. See [[Third-Run Assessment - RQ-0003]].

> **CLOSED 2026-07-20 — formal closure under ADR-GOV-0004 §2 D1 (back-application).** This investigation answered its research question at authoring time (**§4 Findings / Synthesis**); what it lacked were the *formal* closure elements, because the D1 closure convention postdates it. **Acceptance criteria: none apply** — the acceptance-criteria practice began with INV-0010, this record predates it, and no criteria were ever declared for it, so there are none to tick (D1(b)'s stated-reason path). **No research content, claim, confidence level, or finding was altered by this closure; the elements added are additive only.** Maturity `status` remains `Draft` and `operational_status` remains `Active`, matching the model instance **INV-0010** — under this vault's convention "closed" means the inquiry is complete, **not** a maturity promotion and **not** a clearance for external reliance.

---

# 1. Research Question

**RQ-0003:** What does *wu wei* (無為) mean, and how should its central paradox — "action through non-action" — be understood across its major interpretations?

---

# 2. Scope & Disambiguation

- **Focus:** the concept *wu wei* in early Chinese thought, primarily philosophical Daoism (*Daodejing*, *Zhuangzi*), with scholarly interpretation (Slingerland).
- **Reused source:** SRC-0002 (Philosophical Daoist Corpus), first created for INV-0001 — **not duplicated**. This is deliberate: it tests whether the KB supports cross-investigation source reuse.
- **New shared entities:** ENT-0001 (wu wei), ENT-0002 (ziran), placed in `06 Knowledge Base/Entities/` because they are not owned by any single investigation.

---

# 3. Method

KOS-0003 pipeline. The focal concept is modeled as an Entity (ENT-0001, per KOS-0012 §5.5 and KOS-0004 classification); its meaning and scope are evaluated as Claims (CLM-0005, CLM-0006); the answer as a Finding (FND-0003).

```
RQ-0003
  ↓
Entity:  ENT-0001 (wu wei), ENT-0002 (ziran)
Sources: SRC-0002 (reused), SRC-0005 (Slingerland)
  ↓
Claims:  CLM-0005 (meaning), CLM-0006 (scope/registers)
  ↓
Finding: FND-0003
```

---

# 4. Findings / Synthesis

*Wu wei* is **not passivity** but **effortless, non-forcing action in accord with *ziran* (spontaneous naturalness)**. The "action through non-action" paradox (為無為; 無為而無不為) dissolves once *wu wei* is read as the absence of *forced, self-conscious striving* rather than of *activity* — the *Zhuangzi*'s exemplars (Cook Ding) are highly skilled, absorbed action. The concept spans three complementary registers — **political**, **self-cultivational**, **metaphysical** — as facets of one ideal.

Recorded as [[FND-0003 - Wu Wei as Non-Forcing Action]].

---

# 5. Confidence Summary (KOS-0003 §8)

- Meaning (CLM-0005): **Level 4.**
- Three-register scope (CLM-0006): **Level 3.**
- Overall finding (FND-0003): **Level 3** (bounded by the interpretive component).

---

# 6. Assumptions & Bracketing (KOS-0003 §10)

- That the *Daodejing* and *Zhuangzi* share enough of a concept to speak of one *wu wei*.
- That paradoxical formulations are meant coherently.
- Cross-linguistic interpretation is lossy.

---

# 7. Relationships (STD-0004) — and a graph note

- `derived_from` SRC-0002, SRC-0005.
- `related_to` ENT-0001, ENT-0002.
- `part_of` the Knowledge Base.

> **Graph accumulation:** ENT-0001 (wu wei) is now referenced by both INV-0003 and INV-0001 (whose CLM-0001 was retroactively linked to it). This is the first time the Knowledge Base forms an actual cross-investigation graph — the central promise of Project Relatio. The mechanics of maintaining that graph surfaced new friction; see the Third-Run Assessment (F-11, F-12).

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-09|Draft|Third research workflow (RQ-0003); first Entity records; first cross-investigation graph link|
|0.2|2026-07-20|Draft|**Formally CLOSED under ADR-GOV-0004 §2 D1 (closure-convention back-application).** D1 bar assessed: **(a)** explicit RQ answer — satisfied at authoring in §4 Findings / Synthesis; **(b)** acceptance criteria — **none apply**, stated-reason path (the criteria practice began at INV-0010; this record predates it and none were ever declared); **(c)** closure banner — added, dated 2026-07-20; **(d)** frontmatter — matches the model instance INV-0010, which holds `status: Draft` / `operational_status: Active` at closure (no Draft→Adopted closure step exists in this vault, and STD-0005's vocabulary has no distinct closed-state value). **No research content altered** — no claim, confidence level, assumption, or finding touched; closure elements are purely additive.|
|0.3|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End INV-0003
