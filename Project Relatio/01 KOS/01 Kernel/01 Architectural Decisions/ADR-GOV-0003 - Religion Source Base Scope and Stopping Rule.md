---
title: ADR-GOV-0003 - Religion Source Base Scope and Stopping Rule
document_type: Architecture Decision Record
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-19
decision_status: Accepted
decision_date: 2026-07-19
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - Governance Backlog
  - OPS-0001
  - KOS-0007
  - INV-0014 (named candidate)
tags:
  - ProjectRelatio
  - ADR
  - Governance
  - Sources
  - ComparativeReligion
---

# ADR-GOV-0003

# Religion Source Base — Scope and Stopping Rule

## Adopted Architecture Decision Record

> Records the fork resolution and standing stopping rule for the comparative-religion
> source corpus. Inline standing record: Governance Backlog GB-2026-030; this ADR is
> the constitutional record per CON-0003 §7.

---

# 1. Context

The Iranian-family source slice (SRC-0104–SRC-0123, 20 records) completed on
2026-07-18 with no CLM/FND produced, raising a fork: is the comparative-religion
corpus an **investigation** (a driving question, an INV number, stops when
answered) or a **standing source base** (breadth, requiring an explicit written
stopping rule)?

A read-only fork-resolution recon (2026-07-19) supplied the vault facts. The
decision rule: the fork resolves to "investigation" only if an existing written,
unanswered question in the vault would be served by this corpus. Findings: the
only named candidate (INV-0014, historical reconstruction of Jesus) draws on New
Testament material, not this corpus; INV-0001's exclusions are bracketing
language, not open threads; the Kernel comparative-religion sections
(KOS-0004–0007) are declarative, with KOS-0007 §9 providing an output template
for future studies without posing any; and no scope or stopping rule for the
corpus existed anywhere in the vault. A subsequent vault-wide open-question sweep
(same date) confirmed: four category-(a) open questions exist, all in wellness,
clinical-psych, and child-development domains; none is served by this corpus. No
fork-revisit trigger.

Without a stopping rule, a standing source base is an unbounded cataloguing
attractor — the over-collection failure mode the fork existed to prevent.

---

# 2. Decision

> The comparative-religion source corpus is a **standing source base** governed by
> a hybrid stopping rule: **demand-driven trigger, family-complete unit.**

1. **STATUS.** The comparative-religion source corpus is a STANDING SOURCE BASE,
   not an investigation. No INV number attaches to it.
2. **TRIGGER (demand-driven).** No new family/tradition is opened for cataloguing
   unless a written investigation (INV-####) or a Kernel-conformant comparative
   study (per the KOS-0007 §9 output standard) cites a concrete need for that
   family's sources. Absent a trigger, the base does not grow.
3. **UNIT & COMPLETION (family-complete).** When a trigger fires, cataloguing
   proceeds at the family level using the object/edition rule established in the
   Iranian-family slice (SRC-0104–SRC-0123). At family-open time, a one-line
   extent statement is written: which traditions the family includes and which
   source classes are in scope. "Complete" means that extent statement is
   satisfied — not exhaustion of the literature.
4. **EXISTING CONTENT.** The Iranian family is complete per its build. INV-0014
   remains a named candidate untouched by this decision; if opened, it
   constitutes a trigger only for the source families its written question cites.

---

# 3. Alternatives Considered

1. **Resolve the fork to "investigation."** Rejected — the decision rule requires
   an existing written question served by the corpus; recon and sweep confirmed
   none exists. Stretching INV-0014 to fit would invent a new question, not
   answer a written one.
2. **Demand-driven trigger alone, no family unit.** Rejected — discards the
   object/edition rule investment from the Iranian slice and leaves each
   trigger's cataloguing extent undefined, hiding a scope question inside every
   future pull.
3. **Bounded enumeration (name every family the base will ever contain).**
   Rejected — false precision about future research needs; the same defect class
   as the rejected Phase II milestones 4 and 6.
4. **No stopping rule (leave OPS-0001's open-ended placement rule as the only
   boundary).** Rejected — OPS-0001 governs where sources live, not when
   collection stops; open-ended growth without demand is cataloguing for its own
   sake.

---

# 4. Reasoning

The corpus's build behavior was already source-base-shaped: cataloguing work
only, no claims or findings produced, a reusable object/edition rule built for
future families, and the one genuine investigation the territory contained (the
historical-evidence scale discrimination test) already run and closed.

The hybrid rule binds growth to demand while preserving the completed structural
investment. Clause 2 makes the trigger a *written* artifact — an INV or a
KOS-0007 §9-conformant study — so growth is always traceable to a recorded need,
never to momentum. Clause 3 converts the family-complete tradeoff (that
"complete" needs defining per family) into an explicit requirement: the extent
statement is written at open time, not discovered at stopping time.

This keeps the source library consistent with OPS-0001's rationale ("any future
investigation may cite it") while adding the boundary OPS-0001 never supplied.

---

# 5. Consequences

**Accepted costs**
- No ambient breadth-building; the library grows only as fast as written
  questions do.
- Each family-open carries a small ceremony (the extent statement).

**Benefits**
- Unbounded cataloguing is fenced off by recorded rule, not by session-to-session
  judgment.
- The Iranian-family edition rule becomes standing machinery rather than a
  one-off artifact.
- INV-0014's candidacy is preserved and correctly decoupled from this corpus.

**Affected objects**
- Recorded inline: Governance Backlog GB-2026-030 (v1.24), which gains a pointer
  line to this ADR.
- Governs: the comparative-religion source corpus (SRC-0104–SRC-0123 and any
  future families).
- Created: this ADR.

---

# 6. Decision Authority

Architectural decision (CON-0003 §5.2), reserved to the **Vision Steward**. Fork
resolution and rule shape proposed on the support surface (claude.ai) 2026-07-19
from Claude Code recon findings; hybrid rule selected and **adopted by Brian Noon
on 2026-07-19**.

---

# 7. Review Date

Revisit if (a) a written category-(a) open question served by this corpus emerges
in the vault, (b) INV-0014 is formally opened, or (c) a trigger fires and the
family-open extent-statement mechanism proves unworkable in practice.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-19|Adopted|Records the source-base fork resolution and the hybrid stopping rule (GB-2026-030).|

---

# End ADR-GOV-0003