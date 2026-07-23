---
title: ADR-GOV-0004 - Governance Hygiene Closure Decision Tiering and Reference Integrity
document_type: Architecture Decision Record
version: 1.1
status: Adopted
operational_status: Active
created: 2026-07-20
decision_status: Accepted
decision_date: 2026-07-20
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - Governance Backlog
  - ADR-GOV-0003 - Religion Source Base Scope and Stopping Rule
tags:
  - ProjectRelatio
  - ADR
  - Governance
  - Closure
  - ReferenceIntegrity
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-20
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ADR-GOV-0004

# Governance Hygiene: Closure, Decision Tiering, and Reference Integrity

## Adopted Architecture Decision Record

> Records four standing rules resolving convention-vs-practice divergences
> accumulated through 2026-07-19. Closes GB-2026-031; governs GB-2026-028
> remediation. Inline pointer: Governance Backlog.

---

# 1. Context

Between 2026-07-09 and 2026-07-19, four divergences accumulated between written
convention and vault practice:

1. **Closure.** INV-0010 carries a closure banner and ticked acceptance
   criteria; INV-0001 answered its research question (§5) yet remains
   status: Draft / operational_status: Active. No written closure convention
   existed (GB-2026-031).
2. **Decision recording.** CON-0003 §7 makes ADRs the constitutional home for
   significant decisions, but six-plus decisions were recorded inline in
   Governance Backlog entries — a de facto second decision store beside the
   constitutional one, with no rule stating which decisions go where.
3. **Back-updating.** Four instances of the same failure class — documents
   never updated when the state they described changed: a stale 00 Inbox memo
   claim, the version-drift class (GB-2026-028, now reaching Knowledge Base
   objects), the Standards Architecture Retrospective / Standards Status
   staleness (corrected 2026-07-19), and the Standards Status "layers not yet
   built" assertions (corrected 2026-07-20).
4. **Reference integrity.** ADR-GOV-0003 v1.0 listed a named-but-unopened
   candidate (INV-0014) in related_documents, producing the vault's first
   dangling reference since GB-2026-005 — revealing that no written rule
   stated that frontmatter reference fields are graph claims.

---

# 2. Decision

> Four standing rules, adopted together as one governance-hygiene package.

**D1 — Investigation closure convention.** An investigation is Closed when it
carries: (a) an explicit answer statement to its research question; (b) an
acceptance-criteria section ticked, or a stated reason none applies; (c) a
closure banner with date; (d) frontmatter status fields updated to the closed
state. INV-0010 is the model instance; the exact field vocabulary matches its
convention. Back-application: all existing INVs are audited; those meeting the
bar are formally closed (including INV-0001, whose research question is
answered); those not meeting it are listed with what is missing. No forced
closures.

**D2 — Decision tiering.** Standing rules that future sessions must apply are
recorded as ADRs in the owner-reserved Architectural Decisions directory
(CON-0003 §7), with an inline Governance Backlog pointer. One-off resolutions
of a specific problem are recorded inline in the Governance Backlog only.
Prior inline-decided entries are grandfathered — no migration. A one-time
inventory notes which grandfathered entries are standing-rule class, for owner
awareness only; authoring ADRs for any of them is at owner discretion, with no
default action.

**D3 — Close-out back-update rule.** At any session close-out that resolves a
Governance Backlog entry or records a decision changing a documented state,
the session searches the vault for documents asserting the superseded state.
Tier-1 status corrections are fixed in-session; anything heavier is reported.
This rule is amended into whichever operations document owns session close-out
procedure; if no such home exists, the gap is reported rather than a home
invented.

**D4 — Frontmatter references are graph claims.** Entries in related_documents
and any typed reference field must resolve to existing files. Named candidates
and non-existent objects are referenced in prose only. Enforcement exists
(graph_integrity.py fails on violations); this rule is written into whichever
document owns reference conventions, same locate-don't-invent instruction.

---

# 3. Alternatives Considered

1. **Four separate ADRs.** Rejected — the rules share one cause
   (convention-vs-practice drift), were decided in one session, and splitting
   them multiplies ceremony without adding traceability.
2. **Migrate prior inline-decided GB entries to ADRs (D2 alternative).**
   Rejected — retroactive migration churns records that are accurate and
   citable where they stand; grandfathering with an awareness inventory
   preserves the record and the owner's option.
3. **Leave closure to per-INV judgment (D1 alternative).** Rejected — the
   INV-0001/INV-0010 divergence shows per-instance judgment produces
   inconsistent states that cost every future reader an ambiguity
   determination.
4. **Treat back-updating as session discipline rather than written rule (D3
   alternative).** Rejected — four instances in ten days demonstrates
   disposition without structure does not hold.
5. **Rely on graph_integrity.py alone for reference integrity (D4
   alternative).** Rejected — the tool catches violations after commit; the
   rule prevents them at authoring time and states *why* the field is
   load-bearing.

---

# 4. Reasoning

All four rules share one principle: **the vault's value is that its records
can be trusted without re-derivation.** A closure state that must be inferred,
a decision whose authoritative home is ambiguous, a document asserting a
superseded state, and a reference edge that resolves to nothing are the same
defect at different layers — each forces a future reader to reconstruct what
the record should simply state.

D1 and D2 repair the two convention-vs-practice divergences directly. D3
prevents the accumulation pattern that produced four staleness instances. D4
converts a tool-enforced constraint into an authoring-time rule with stated
rationale. Grandfathering (D2) and no-forced-closures (D1) both apply the
preservation-over-overwrite principle (CON-0003 §9.4): the rules govern
forward; they do not falsify the past.

---

# 5. Consequences

**Accepted costs**
- Closure ceremony added to every future investigation.
- ADR authoring remains an owner-only step, serializing standing-rule
  recording through the owner.
- Close-out gains a search obligation.

**Benefits**
- GB-2026-031 closed; INV closure states become uniform and auditable.
- The decision-store ambiguity ends: one rule states what goes where.
- The staleness class gains a standing countermeasure.
- Reference integrity becomes an authoring convention, not just a CI failure.
- GB-2026-028 remediation is unblocked (closure and drift fixes no longer
  fenced).

**Affected objects**
- Closes: GB-2026-031.
- Governs remediation of: GB-2026-028.
- To be amended (locate, not invent): the operations document owning close-out
  procedure (D3); the document owning reference conventions (D4).
- To be audited: all INV objects (D1 back-application).
- Created: this ADR; a grandfathered-decisions inventory (D2, report only).

---

# 6. Decision Authority

Architectural decision (CON-0003 §5.2), reserved to the **Vision Steward**.
Four-decision package proposed on the support surface (claude.ai) 2026-07-20
from accumulated session findings; **ratified in full by Brian Noon on
2026-07-20**.

---

# 7. Review Date

Revisit if (a) the D1 closure bar proves unworkable for a future INV class,
(b) the D2 tiering line produces a decision that fits neither tier, or (c) a
fifth back-update failure instance occurs despite D3 — which would indicate
the rule's home or trigger is wrong.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-20|Adopted|Records the four-rule governance-hygiene package (D1–D4). Closes GB-2026-031.|
|1.1|2026-07-22|Adopted|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End ADR-GOV-0004