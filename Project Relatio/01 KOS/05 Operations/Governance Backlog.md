---
title: Governance Backlog
document_type: Governance Record
version: 1.1
status: Active
created: 2026-07-09
parent_documents:
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - Standards Architecture Retrospective
  - Pressure Test Report - RQ-0001
  - Second-Run Friction Assessment - RQ-0002
  - Third-Run Assessment - RQ-0003
  - Identifier Registry
tags:
  - ProjectRelatio
  - Governance
  - Backlog
---

# Governance Backlog

## Version 1.0

## Active Governance Record

---

# 1. Purpose

The single, authoritative list of **unresolved decisions, improvement opportunities, architectural questions, and future revisions** — as mandated by **KOS-0011 §9 (GB-001)**, which required a governance backlog that was never built.

Before this document existed, open items were scattered across five places: the Standards Architecture Retrospective's migration register, CLAUDE.md's deferred list, and three research assessment reports. Consolidating them is the point.

**Entry format (GB-001):** Issue → Context → Impact → Priority → Potential Solutions → Decision Status.

**Discipline:** an item on this list is *not* a commitment to build. Per the scope guardrail, nothing is actioned without **demonstrated need** or Vision Steward approval. Deferral is a legitimate, recorded outcome.

---

# 2. Open Items

---

## GB-2026-001 — Typed relationships in frontmatter
- **Issue:** STD-0004 defines a relationship vocabulary (`supports`, `derived_from`, `contrasts_with`…) but STD-0002 frontmatter carries only untyped `related_documents`. Types live in object bodies.
- **Context:** Pressure Test F-4; recurred in every investigation.
- **Impact:** Medium. Tooling (Dataview) can see links but not their meaning; graph queries are weaker than the architecture promises.
- **Solutions:** (a) extend STD-0002 to carry typed relations; (b) formally rule that types live in the body only.
- **Status:** Open. No demonstrated blocker yet.

## GB-2026-002 — Quantitative evidence fields
- **Issue:** KOS-0003 §5 grades evidence 0–5 but has no field for sample size, effect size, replication count, or numeric results.
- **Context:** Second-Run Friction Assessment F-10 (surfaced by an empirical investigation; absent from interpretive ones).
- **Impact:** Medium, domain-specific. Partly mitigated by KOS-0003 §9 (Consensus Evaluation).
- **Solutions:** add optional quantitative-evidence fields to the Claim structure (KOS-0003 minor revision).
- **Status:** **Deferred by decision.** Threshold: act only if a *third* empirical investigation strains against it. One instance is not demonstrated need.

## GB-2026-003 — Entity template (TPL)
- **Issue:** No template for Entity records; ENT-0001/0002 were hand-authored from KOS-0012 §5.5.
- **Context:** Third-Run Assessment F-13.
- **Impact:** Low.
- **Solutions:** create an Entity template.
- **Status:** **Deferred.** Threshold: entities recur in a future investigation.

## GB-2026-004 — Graph-integrity automation
- **Issue:** Relationship reciprocity and dangling-reference checks are manual (OPS-0002 §6).
- **Context:** Third-Run Assessment F-12; a first manual pass found and repaired four one-directional links.
- **Impact:** Medium now; **High at scale.** Touches Relatio's defining claim (a graph the system cannot keep consistent).
- **Solutions:** a Dataview-generated integrity report, run as a periodic STD-0006 audit.
- **Status:** Open. Threshold: when the KB grows past reliable manual checking.

## GB-2026-005 — Phantom ADR references
- **Issue:** `ADR-KOS-0001` … `ADR-KOS-0010` are cited in KOS-0003 and KOS-0011 but do not exist.
- **Context:** Retrospective C-9 / migration M-3.
- **Impact:** Medium. Dangling references in Adopted Kernel documents; a standing STD-0006 non-conformance.
- **Solutions:** (a) remove/reword the references; (b) write the ADRs (rejected — over-architecture).
- **Status:** **Deferred by owner decision** to a future Kernel review pass. Note: an ADR practice now exists (see GB-2026-010), using the `ADR-GOV-NNNN` form to avoid collision.

## GB-2026-006 — Two-dimensional lifecycle field
- **Issue:** STD-0005 and CLAUDE.md mandate independent Maturity and Operational states; documents carry a single `status`.
- **Context:** Retrospective M-1.
- **Impact:** Low today.
- **Solutions:** add `operational_status` across ~24 documents.
- **Status:** **Deferred by owner decision** until the first real supersession event. *(Note: ROLE-0003's retirement on 2026-07-09 may be that event — re-evaluate.)*

## GB-2026-007 — KOS-0200 fate
- **Issue:** KOS-0200 "Standards Framework" (Draft, v0.1) appears to duplicate the purpose of the Standards Index and Manifest.
- **Context:** Retrospective M-5 / C-11. Still carries an unapproved `document_type` ("Operational Framework").
- **Impact:** Low. Confusing but inert.
- **Solutions:** supersede and archive it, or adopt and retype it.
- **Status:** Open. Candidate for supersession.

## GB-2026-008 — ST-003 Domain Specialist unimplemented
- **Issue:** KOS-0011 §10 defines ST-003 Domain Specialist; no ROLE implements it.
- **Context:** Governance assessment. Three investigations (religion, physics, Chinese philosophy) showed no need — the Research Specialist handled all domains.
- **Impact:** Low.
- **Solutions:** implement as ROLE-NNNN if domain depth becomes a bottleneck.
- **Status:** **Deferred.** Do not implement speculatively.

## GB-2026-009 — Source metadata for non-modern sources
- **Issue:** STD-0002 §11 (`source_author`, `source_url`, `publication_date`) assumes a modern, single-author, dated source.
- **Context:** Pressure Test F-3. **Confirmed domain-specific** — modern scientific sources (SRC-0003/0004) fit cleanly; ancient/composite texts did not.
- **Impact:** Low. Honest prose qualification in the fields is an adequate interim.
- **Solutions:** add optional fields/guidance for composite and ancient sources.
- **Status:** Open, low priority.

## GB-2026-010 — ADR practice adopted, not backfilled
- **Issue:** CON-0003 §7 states significant decisions **shall** be preserved as ADRs. None existed; many significant decisions were made.
- **Context:** Governance assessment R8.
- **Impact:** Medium — institutional memory of *why* decisions were made.
- **Solutions:** adopt ADRs going forward (done: TPL-0005, ADR-GOV-0001); do **not** backfill.
- **Status:** **Resolved going forward.** Backfill explicitly declined as bureaucracy.

## GB-2026-011 — Role authority ratification outstanding
- **Issue:** ROLE-0002, ROLE-0004, and ROLE-0005 carried **PROPOSED** Authority (§4) and Boundaries (§5). Only ROLE-0001 was ratified.
- **Context:** Authority definition is Vision-Steward-reserved (ROLE-0001 §4.2).
- **Impact:** High while open — the research circuit ran on Draft definitions.
- **Status:** **RESOLVED 2026-07-09.** The Vision Steward ratified all three to **Adopted v1.0**, with two refinements applied at ratification: (1) ROLE-0002 §4.2a scope boundary (disambiguation vs. material redirection); (2) ROLE-0004 §5 procedural-independence limit. ROLE-0005's constitutional limits were accepted as binding on the owner. SA-002/SA-003 made non-provisional. Moved to §3.

## GB-2026-012 — Layer-stack vs governance-level mismatch
- **Issue:** The Manifest §12 layer stack (Kernel→Standards→Roles→Templates→Operations→Research) does not align with KOS-0011 §8 governance levels (Constitution→Kernel→Standards→Procedures→Experiments). Roles appear in one, not the other.
- **Context:** Governance assessment.
- **Impact:** Low. Cosmetic inconsistency; no operational effect.
- **Solutions:** reconcile the two hierarchies in a future Kernel review.
- **Status:** Open, low priority.

---

# 3. Resolved (retained for institutional memory)

| Item | Resolution |
|---|---|
| Anti-fabrication rule lived only in `.claude/agents` (RRI) | Elevated to KOS-0003 §12.1; enforced by STD-0006 §5.7/§7.3 |
| Three competing role vocabularies (Functions / ST-roles / ROLE) | Reconciled; Roles Index is canonical; KOS-0011 §10 note added |
| ROLE-0003 had no architectural warrant | Retired to `07 Archive`; function absorbed by ROLE-0005 |
| Owner authority undocumented | ROLE-0005 Vision Steward created, with constitutional limits |
| STD-0006 §8 validation authority unassigned | Split: structural → ROLE-0001; epistemic → ROLE-0004 |
| No appeal path; dissent could be erased | STD-0006 §7.4 (GP-004); CR-001/2/3 taxonomy wired in |
| Identifier Registry missing (STD-0001 §18) | Created |
| KB organization / graph maintenance undefined | OPS-0001, OPS-0002 |
| No governance backlog (KOS-0011 §9) | *This document* |
| Role authority unratified (GB-2026-011) | Vision Steward ratified ROLE-0002/0004/0005 to Adopted (2026-07-09), with two refinements applied |

---

# 4. Maintenance

Any role may **add** an item. Only the Vision Steward may mark an item **Decided** or **Deferred by decision**. Items resolved move to §3 rather than being deleted (CON-0003 §9.4: historical preservation).

---

# 5. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Active|Created per KOS-0011 §9 (GB-001), consolidating open items previously scattered across the Retrospective, CLAUDE.md, and three assessment reports.|
|1.1|2026-07-09|Active|GB-2026-011 resolved: ROLE-0002/0004/0005 ratified to Adopted with two refinements. Moved to §3.|

---

# End Governance Backlog
