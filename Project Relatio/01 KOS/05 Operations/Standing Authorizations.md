---
title: Standing Authorizations
document_type: Governance Record
version: 1.2
status: Adopted
operational_status: Active
created: 2026-07-09
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
  - ROLE-0005 Vision Steward
related_documents:
  - ROLE-0001 Knowledge Architect
  - ROLE-0002 Research Specialist
  - ROLE-0004 Critical Reviewer
  - Roles Index
tags:
  - ProjectRelatio
  - Governance
  - Authority
  - Delegation
---

# Standing Authorizations

## Version 1.2

## Active Governance Record

---

# 1. Purpose

The authoritative record of **delegated authority**: scoped, revocable grants by which the Vision Steward (ROLE-0005) permits a role to act without a per-instance approval.

Two problems this solves:

- **Approval fatigue.** Without recorded delegation, every governed action needs a round-trip. Grants that were in practice given ad hoc ("keep going", "do what you deem appropriate") become explicit and auditable.
- **Single-person dependency.** CON-0003 **GP-006** states *"the project shall not depend upon a single person for continued existence."* A governance model routing every decision through one individual is in tension with that principle. Recorded, transferable delegation is the remedy — the **function** is primary, not the person (CON-0003 §4).

---

# 2. Rules of Delegation

1. **Scoped.** A grant names exactly what may be done, and to which role.
2. **Revocable.** Any grant may be withdrawn by the Vision Steward at any time, effective immediately.
3. **Recorded.** A grant not written here does not exist. Verbal or in-session permission is **session-scoped only** and expires with the session.
4. **Non-delegable core.** Constitutional decisions (CON-0003 §5.1 — mission, foundational principles, project identity) may **never** be delegated.
5. **No self-granting.** A role may not widen its own authority. Only the Vision Steward grants.
6. **Auditable.** Actions taken under a standing authorization remain subject to STD-0006 review and appear in revision histories.

---

# 3. Active Grants

## SA-001 — Knowledge Architect: routine architectural maintenance
- **Granted to:** ROLE-0001
- **Granted:** 2026-07-09 (by ratification of ROLE-0001 §4.1)
- **Scope:** apply existing Adopted standards; create conformant Knowledge Objects of existing types; run STD-0006 validation passes; maintain the Identifier Registry, Governance Backlog, and integration/index documents; make **reversible, non-semantic corrections** (typos, invalid YAML, broken single-file references) that change no document's meaning; add non-destructive reconciliation notes aligning a document to an already-Adopted decision.
- **Explicitly excluded:** anything in ROLE-0001 §4.2 (new/amended standards, object types, batch migrations, renames, restructuring, meaning changes, Adopted-status changes, un-deferrals, role authority).
- **Constraint:** bound by the *verify before removing* rule (ROLE-0001 §6).
- **Status:** Active.

## SA-002 — Research Specialist: conduct investigations
- **Granted to:** ROLE-0002
- **Granted:** 2026-07-09 (ratified; ROLE-0002 Adopted v1.0)
- **Scope:** refine and scope an assigned research question; select, evaluate, and record sources; form, classify, evidence, and grade claims; assign confidence; synthesize findings; create conformant INV/CLM/SRC/ENT/FND objects using existing types and templates, within `06 Knowledge Base/`.
- **Explicitly excluded:** creating new object types, standards, or templates; restructuring; altering any document outside the Knowledge Base; **certifying its own work**.
- **Constraint:** absolutely bound by KOS-0003 §12.1 (no fabrication); and by ROLE-0002 §4.2a — a *material* redirection of the question is confirmed with the Steward before deep work (mere disambiguation is not).
- **Status:** Active.

## SA-003 — Critical Reviewer: epistemic validation
- **Granted to:** ROLE-0004
- **Granted:** 2026-07-09 (ratified; ROLE-0004 Adopted v1.0; STD-0006 §8 grants the underlying authority)
- **Scope:** review any Claim, Finding, or Investigation; issue Conformant / Flagged / Blocked verdicts citing specific criteria; require that confidence be lowered or that a limitation, assumption, or alternative be added.
- **Explicitly excluded:** conducting research; rewriting the objects it reviews; raising confidence; ruling on structural conformance; adjudicating truth.
- **Constraint:** every verdict cites a specific criterion; Blocked verdicts are appealable (STD-0006 §7.4) with dissent preserved. Per ROLE-0004 §5, this is *procedural* independence (same model as the Specialist); high-stakes findings warrant a different model or human review.
- **Status:** Active.

## SA-004 — Session: auto-commit validated work (RRI / operational)

- **Granted to:** the Claude Code main session (an **RRI** implementation grant, not an RKA role authority — git is Claude Code mechanics, not architecture; the RKA/RRI separation is preserved).
- **Granted:** 2026-07-11 (by the owner, in session).
- **Scope:** **commit** a completed, coherent unit of work to the **local** git repository **without per-instance approval** — with a descriptive message — once the change is at a clean resting state (for tooling/vault changes, `validate.py` and `graph_integrity.py` green). Rationale: committing is local and fully reversible, preserves granular history, and prevents loss; it aligns with the vault's own preservation ethos (STD-0005 §22, CON-0003 §9.4). Replaces the prior "leave everything in the working tree and ask each time" default.
- **Explicitly excluded:** **`git push` to the public remote** (`nooner12/Project-Relatio`) — publishing is outward-facing and hard to reverse, and **remains owner-gated, requested per batch**. Also excluded: committing broken or mid-migration states, force-pushing, history rewriting, and `--no-verify`.
- **Constraint:** each commit is a coherent completed unit; never commit with failing validators; never push without explicit owner approval (see memory [[github-remote]]).
- **Status:** Active.

---

# 4. Revoked / Expired Grants

*(none)*

Session-scoped permissions granted in conversation are not recorded here and expire with the session. They are never a substitute for a written grant.

---

# 5. Review

Grants are reviewed whenever a role definition is amended, and at each STD-0006 §4.4 periodic audit. Per GP-006, **delegation should broaden over time**, not concentrate.

---

# 6. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Active|Created by the governance assessment (R9). Records SA-001 (ratified) and SA-002/SA-003 (provisional, pending role-authority ratification).|
|1.1|2026-07-09|Active|SA-002 and SA-003 made non-provisional on ratification of ROLE-0002 and ROLE-0004; added their ratification-refinement constraints (§4.2a scope, §5 procedural independence).|
|1.2|2026-07-11|Active|Added **SA-004** (owner-granted, in session): the session may auto-commit completed, validated units of work locally without asking; `git push` to the public remote stays owner-gated per batch. An RRI/operational grant — RKA/RRI separation preserved.|

---

# End Standing Authorizations
