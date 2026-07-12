---
title: Architecture Baseline
document_type: Governance Record
version: 1.1
status: Adopted
operational_status: Active
created: 2026-07-11
parent_documents:
  - CON-0002 Project Relatio Architectural Principles
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - Governance Backlog
  - Standing Authorizations
  - Standards Architecture Retrospective
tags:
  - ProjectRelatio
  - Governance
  - Baseline
  - Stability
---

# Architecture Baseline

## Version 1.1

## Active Governance Record

---

# 1. Purpose

This record draws a **stability line** under Project Relatio's architecture.

The concepts named in §3 are considered **stable as of 2026-07-11**. Changing any of them requires **implementation evidence** — a real research run, migration, or tool that strains the concept — **not further design discussion**.

This is a deliberate commitment device serving the project's **justify-by-use** discipline (CLAUDE.md scope guardrail; ADR-GOV-0002): settled concepts change on *implementation evidence*, not on redesign impulse. It follows the "freeze the foundation" step of the Phase II execution brief (2026-07-11). It guards against churning the foundation faster than use can validate changes — **without** treating architectural growth itself as a risk to be defended against (building toward an excellent architecture is a legitimate aim; ADR-GOV-0002).

It is not a freeze on *work*, and not a bias against building. It is a freeze on *reopening settled concepts for redesign without evidence*. New work — including new architecture that earns its place by use — remains open, as does the Governance Backlog (§4).

---

# 2. Why now

Two conditions make a baseline useful at this moment rather than earlier:

1. **The conceptual foundation is complete and exercised.** Five investigations have run end-to-end (INV-0001…0005), across religion, physics, and clinical-evidence domains; the Standards Architecture Retrospective and KOS-0012 were adopted *from* that use. The concepts below have survived contact with real research.
2. **A sweeping Kernel audit just concluded.** GB-2026-018 revised KOS-0001/0003/0004/0005/0006/0009/0010 across 2026-07-09…11 (co-primacy, confidence-scale unification, ontological-humility propagation). A baseline draws the line *under* that churn, so the next change to a frozen concept must be earned by evidence, not preference.

---

# 3. Frozen concepts

Each concept is stable as of the date above. The governing document is authoritative for detail; this list fixes the *concept*, not every clause of its governing document.

## 3.1 Identity and separation
- **Knowledge Object** is the primary architectural abstraction. *(KOS-0012; STD-0007)*
- **RKA / RRI separation** — the platform-independent architecture is distinct from its Obsidian/Claude-Code implementation. *(CON-0002; CLAUDE.md)*
- **Purpose** — the system exists to conduct disciplined research on real questions; additions must improve the research, not the architecture's completeness. *(CLAUDE.md scope guardrail)*

## 3.2 Structure and graph
- **Folders = classification only.** The knowledge graph lives in typed semantic relationships, not the file tree. *(CON-0002; STD-0003)*
- **Tags = discovery, not classification.** *(STD-0003)*
- **Links are not relationships.** A relationship requires semantic meaning; bare backlinks are insufficient. *(STD-0004; KOS-0005)*
- **Index ≠ MOC** — an Index is an authoritative inventory; a MOC is interpretive navigation. *(KOS-0009)*

## 3.3 Epistemics
- **Single canonical confidence scale**: `Level N (Label)`, ordinal 0–5, label-carrying (Very High → Very Low, plus a Level-0 Unsupported floor). *(KOS-0003 §8 v1.4; KOS-0008 §8)*
- **Anti-fabrication is a Kernel rule** (KOS-0003 §12.1), operationalized by review (STD-0006 §5.7/§7.5), not an implementation-layer convenience.
- **Evidence before formalization** — architecture is extended on demonstrated need, logged to the Governance Backlog, not created speculatively. *(KOS-0011; CLAUDE.md)*

## 3.4 Ontology
- **Entity–Relationship co-primacy** is the default working modeling lens, held *under ontological humility* — entity-first and strong relationalism remain viable, non-rejected perspectives pending evidence. *(KOS-0004 v1.3; KOS-0005 v1.3; GB-2026-019)*

## 3.5 Lifecycle
- **Two independent lifecycle dimensions**: Maturity (Proposed → Draft → Reviewed → Adopted) and Operational (Active → Superseded → Archived). Never collapsed into one. *(STD-0005)*

## 3.6 Governance and roles
- **Governance-by-decision; no spontaneous restructuring.** The architecture changes only through KOS-0011 governance. *(KOS-0011; CON-0003)*
- **The research circuit**: Research Specialist (ROLE-0002) → Critical Reviewer (ROLE-0004) → Knowledge Architect (ROLE-0001), coordinated by the Vision Steward (ROLE-0005). *(OPS-0003; Roles Index)*
- **Owner-reserved changes**: new/amended Standards, new object types, batch migrations, renames, Adopted-status changes, and role authority. *(ROLE-0001 §4.2; ROLE-0005)*

## 3.7 The adopted corpus (as frozen)
- Constitution: CON-0001…0004.
- Kernel: KOS-0001, KOS-0003…0012 (KOS-0002 superseded).
- Standards: STD-0001…0007.
- Roles: ROLE-0001, 0002, 0004, 0005 (ROLE-0003 retired).
- Operations: OPS-0001…0003; the Identifier Registry, Governance Backlog, Standing Authorizations, and this Baseline.

---

# 4. Explicitly NOT frozen

Freezing concepts does not freeze the backlog. These remain open to evidence and may change without violating the baseline:

- Typed-relationship **frontmatter encoding** (GB-2026-001) — schema may evolve with tooling.
- Lifecycle **field implementation** (GB-2026-006) — the two-dimensional *model* is frozen; the metadata encoding is operational.
- Non-modern **source metadata** fields (GB-2026-009).
- **Tiered / lean workflow** build-out (GB-2026-013).
- Any item on the Governance Backlog carrying an Open or Deferred status.

Deferred-by-decision meta-structure — reflexive/architectural Knowledge Objects (AKOs), a learning engine, an architecture health dashboard, living-decision objects replacing ADRs — remains **out of scope** (Phase II brief stop-list). Reintroducing any of them requires demonstrated need and Vision-Steward approval, recorded as an ADR.

---

# 5. What this baseline forbids and permits

**Forbids:** reopening a §3 concept for redesign on aesthetic, symmetry, or completeness grounds alone.

**Permits:** revising any §3 concept when a documented failure in a real run, migration, or tool shows it does not serve the research. Such a revision is a governed change (KOS-0011), recorded as an ADR and reflected in a new version of this Baseline.

---

# 6. Amendment

A new version of this Baseline is issued when a frozen concept is changed through governance, or when a new concept has been exercised enough to be declared stable. Amendment is a Vision-Steward (owner) act. Superseded versions are preserved (STD-0005 §22).

---

# 7. Revision History

| Version | Date | Status | Description |
|---|---|---|---|
| 1.0 | 2026-07-11 | Active | Initial baseline. Freezes the concepts exercised across INV-0001…0005 and settled by the Standards Architecture Retrospective and the GB-2026-018 Kernel audit. Implements the Phase II brief's "freeze the foundation" step. |
| 1.1 | 2026-07-11 | Active | §1 reframed per **ADR-GOV-0002**: the baseline serves the justify-by-use discipline rather than defending against "over-architecture" as a standing risk; architectural growth that earns its place by use is a legitimate aim. The freeze still bars redesign-without-evidence; it does not bias against building. |

---

# End Architecture Baseline
