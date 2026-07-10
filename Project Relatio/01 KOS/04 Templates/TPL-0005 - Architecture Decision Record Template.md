---
title: TPL-0005 - Architecture Decision Record Template
document_type: Template
version: 1.0
status: Adopted
created: 2026-07-09
template_type: Architecture Decision Record
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - STD-0002 Metadata & YAML Standard
tags:
  - ProjectRelatio
  - Templates
  - ADR
  - Governance
---

# TPL-0005 — Architecture Decision Record Template

## Adopted Template

> **When to use.** CON-0003 §7 requires that **significant decisions** be preserved as ADRs. In practice: any **Architectural Decision** (CON-0003 §5.2) — changing system structure, introducing a major component, amending a Standard or Kernel document, creating or retiring a role, or modifying a foundational workflow.
>
> **Not** for Operational (§5.3) or Exploratory (§5.4) decisions; those are captured in revision histories and assessment reports.
>
> **No backfill.** ADR practice begins 2026-07-09 and applies going forward. Historical decisions remain recorded in revision histories, the Standards Architecture Retrospective, and the research assessment reports.
>
> **Identifier:** `ADR-[CATEGORY]-NNNN` per STD-0001 §5 — e.g. `ADR-GOV-0001`. Use a category (GOV, KOS, STD…) to avoid collision with the phantom `ADR-KOS-000N` references tracked in Governance Backlog GB-2026-005. Take the next number from the Identifier Registry.
>
> Copy the block below into `01 KOS/01 Kernel/01 Architectural Decisions/`.

---

```markdown
---
title: ADR-CAT-NNNN - <Decision Title>
document_type: Architecture Decision Record
version: 1.0
status: Adopted
created: <YYYY-MM-DD>
decision_status: <Proposed | Accepted | Superseded>
decision_date: <YYYY-MM-DD>
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - <documents this decision changes>
tags:
  - ProjectRelatio
  - ADR
  - <TopicTag>
---

# ADR-CAT-NNNN

# <Decision Title>

## Adopted Architecture Decision Record

---

# 1. Context
<What situation forced a decision? What evidence or event triggered it?>

# 2. Decision
> <The decision, stated as a single unambiguous proposition.>

# 3. Alternatives Considered
1. **<Alternative>** — <why rejected>
2. **<Alternative>** — <why rejected>

# 4. Reasoning
<Why this option. Cite the standards, principles, or evidence relied upon.>

# 5. Consequences
**Accepted costs:** <what gets worse or harder>
**Benefits:** <what gets better>
**Affected objects:** <documents amended, created, retired>

# 6. Decision Authority
<Who decided. Constitutional/architectural decisions are Vision-Steward-reserved.>

# 7. Review Date
<When this should be revisited, or the condition that would reopen it.>

# 8. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|1.0|<YYYY-MM-DD>|Adopted|Initial decision record|

# End ADR-CAT-NNNN
```

---

# Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial ADR template; adopts CON-0003 §7 ADR practice going forward, without backfill (Governance Backlog GB-2026-010)|

---

# End TPL-0005
