---
title: INV-0002 - Phantom Traffic Jams
document_type: Investigation Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Base
  - Complexity Science
  - Investigation
parent_documents:
  - KOS-0012 Knowledge Object Model
  - KOS-0008 Research Methodology & Investigation Framework
  - KOS-0006 Systems Modeling & Complexity Framework
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - SRC-0003 Sugiyama 2008 Circular-Track Experiment
  - SRC-0004 Traffic-Flow Instability & Jamiton Modeling
  - CLM-0003 Endogenous Instability, Not Bottleneck
  - CLM-0004 Backward Stop-and-Go Waves
  - FND-0002 Jams as Emergent Instability
  - Second-Run Friction Assessment - RQ-0002
tags:
  - ProjectRelatio
  - KnowledgeBase
  - ComplexityScience
  - TrafficFlow
  - Investigation
relationships:
  - type: derived_from
    target: SRC-0003
  - type: derived_from
    target: SRC-0004
  - type: related_to
    target: KOS-0006
---

# INV-0002

# Phantom Traffic Jams

## Draft Investigation Record

> Authored using **TPL-0003** (Investigation Record Template); Sources via TPL-0002, Claims via TPL-0001, Finding via TPL-0004. Second research workflow — its purpose is both to answer the question and to test whether the architecture generalizes beyond comparative religion and whether friction has dropped since INV-0001. See [[Second-Run Friction Assessment - RQ-0002]].

> **CLOSED 2026-07-20 — formal closure under ADR-GOV-0004 §2 D1 (back-application).** This investigation answered its research question at authoring time (**§4 Findings / Synthesis**); what it lacked were the *formal* closure elements, because the D1 closure convention postdates it. **Acceptance criteria: none apply** — the acceptance-criteria practice began with INV-0010, this record predates it, and no criteria were ever declared for it, so there are none to tick (D1(b)'s stated-reason path). **No research content, claim, confidence level, or finding was altered by this closure; the elements added are additive only.** Maturity `status` remains `Draft` and `operational_status` remains `Active`, matching the model instance **INV-0010** — under this vault's convention "closed" means the inquiry is complete, **not** a maturity promotion and **not** a clearance for external reliance.

---

# 1. Research Question

**RQ-0002:** Why do traffic jams form on highways with no bottleneck, accident, or obstruction? What is the mechanism, and how well-established is it?

(Chosen to test architecture *generality*: a different domain — complexity/systems science — and a different *shape* — explanatory rather than comparative — from INV-0001.)

---

# 2. Scope & Disambiguation

- **In scope:** the "phantom" / bottleneck-free jam — spontaneous congestion on a road with no external trigger.
- **Out of scope:** ordinary bottleneck jams (accidents, merges, tolls), which have obvious external causes.
- The question is *mechanistic and empirical*, not interpretive — so it exercises causal claims and empirical evidence rather than the interpretive/metaphysical machinery INV-0001 used.

---

# 3. Method

Followed the KOS-0003 pipeline, with the phenomenon framed through **KOS-0006 (Systems Modeling & Complexity)** — emergence, feedback, instability. Empirical evidence (a controlled experiment) and modeling literature were captured as Source records; the mechanism and phenomenology as Claim records; the answer as a Finding record.

```
RQ-0002
  ↓
Sources: SRC-0003 (experiment), SRC-0004 (models)
  ↓
Claims:  CLM-0003 (instability, not bottleneck), CLM-0004 (backward waves)
  ↓
Finding: FND-0002
```

---

# 4. Findings / Synthesis

Highway jams can form with **no bottleneck**. Above a **critical density**, uniform traffic flow is **dynamically unstable**; ordinary reaction-time delays amplify small perturbations into **self-sustaining stop-and-go waves that travel backward** through traffic (~15–20 km/h, approximate). The jam is an **emergent, self-organized** property of the collective system — a textbook case of the emergence KOS-0006 describes — demonstrated experimentally (SRC-0003) and explained by convergent models (SRC-0004).

The integrated answer is recorded as [[FND-0002 - Jams as Emergent Instability]].

---

# 5. Confidence Summary (KOS-0003 §8)

- Bottleneck-free jams exist and arise from instability (CLM-0003): **Level 4.**
- Congestion propagates backward as stop-and-go waves (CLM-0004): **Level 4** (direction), **Level 3** (exact speed).
- Overall finding (FND-0002): **Level 4.**

Higher confidence than INV-0001's findings — as expected for an empirical, experimentally-tested question versus a cross-tradition interpretive one.

---

# 6. Assumptions & Bracketing (KOS-0003 §10)

- Closed-track experimental results generalize to open highways (supported by field data).
- Aggregate driver behavior is adequately modeled by car-following dynamics.
- Quantitative thresholds are treated as approximate/condition-dependent.

---

# 7. Relationships (STD-0004)

- `derived_from` SRC-0003, SRC-0004.
- `related_to` KOS-0006 (the phenomenon instantiates emergence/self-organization).
- `produces` FND-0002 (expressed via `part_of`/`derived_from` per STD-0004; see KOS-0012 §7).
- `part_of` the Knowledge Base.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-09|Draft|Second research workflow (RQ-0002); authored with the KOS-0012 object model and the Templates layer|
|0.2|2026-07-20|Draft|**Formally CLOSED under ADR-GOV-0004 §2 D1 (closure-convention back-application).** D1 bar assessed: **(a)** explicit RQ answer — satisfied at authoring in §4 Findings / Synthesis; **(b)** acceptance criteria — **none apply**, stated-reason path (the criteria practice began at INV-0010; this record predates it and none were ever declared); **(c)** closure banner — added, dated 2026-07-20; **(d)** frontmatter — matches the model instance INV-0010, which holds `status: Draft` / `operational_status: Active` at closure (no Draft→Adopted closure step exists in this vault, and STD-0005's vocabulary has no distinct closed-state value). **No research content altered** — no claim, confidence level, assumption, or finding touched; closure elements are purely additive.|

---

# End INV-0002
