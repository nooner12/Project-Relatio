# CLAUDE.md — Project Relatio

This file is Relatio Reference Implementation (RRI) tooling. It is not a Knowledge Object and is not governed by KOS lifecycle rules. It exists to orient Claude Code sessions working inside this vault.

## What this vault is

This vault is the **Relatio Reference Implementation (RRI)** — the Obsidian implementation of the **Relatio Knowledge Architecture (RKA)**. Maintain this distinction at all times:

- **RKA** = the abstract, platform-independent architecture (principles, standards, governance, object types, relationships).
- **RRI** = this vault: folders, Markdown, YAML, templates, workflows, plugins.
- Folder structure is an *implementation expression*, not the architecture. Folders represent classification only; the knowledge graph lives in semantic relationships, not the file tree.

Central principle: **Knowledge is a structured network of meaningful relationships, not a collection of stored information.**

## Purpose and scope guardrail (owner, 2026-07-09)

**Project Relatio's current purpose is to be a system that conducts thorough and disciplined research on Brian's research questions.** Being an exemplary knowledge architecture may eventually be a goal in its own right — Brian has named "the world's best knowledge architecture" as a long-term horizon — but **it is not the current brief.**

Practical consequence, and the primary defence against over-architecture: **every addition must make the research better, not the architecture more complete.** A standard, object type, role, or workflow step that does not catch a real failure or improve a real answer should be removed, not preserved for symmetry. When in doubt, run a research question through the system and see what breaks.

## Authoritative sources — read before acting

The governing documents live under `01 KOS/`. Before creating, renaming, moving, or restructuring anything, read the relevant standard. The transfer summary below is orientation only — **the STD/KOS documents in the vault are authoritative**. If this file and a vault document conflict, the vault document wins; flag the conflict to Brian.

Key documents:
- `KOS-0001` — Research OS Charter (mission/identity)
- `KOS-0004` — Ontological Framework & Reality Modeling System (Adopted; supersedes the archived KOS-0002 draft)
- `KOS-0009` — Knowledge Representation & Information Architecture Framework
- `KOS-0011` — Governance, Stewardship & Evolution Framework (how the architecture changes)
- `KOS-0012` — Knowledge Object Model (what a Knowledge Object is; the object typology; adopted 2026-07-09)
- **Roles Index** (`03 Roles/`) — canonical mapping of stewardship Functions → ST-roles → ROLE definitions → agents; read before touching any role
- **Governance Backlog** (`05 Operations/`) — the single list of open items and decisions
- **Standing Authorizations** (`05 Operations/`) — what a session may do without asking
- `ADR-GOV-0001` — the governance/role reconciliation decision (first ADR)
- `STD-0001` — Naming & Identification
- `STD-0002` — Metadata & YAML
- `STD-0003` — Classification & Discovery
- `STD-0004` — Relationship & Linking
- `STD-0005` — Lifecycle & Revision
- `STD-0007` — Terminology & Semantic Stewardship
- `STD-0006` — Review & Validation (Adopted 2026-07-09)

## Non-negotiable architectural decisions (already adopted)

1. Project Relatio is a knowledge architecture, not a note-taking system.
2. **Knowledge Object** is the primary architectural abstraction (per STD-0007, the preferred term).
3. Obsidian is the reference implementation, not the architecture.
4. Folders = classification only.
5. Tags = discovery mechanisms, not classification.
6. Indexes and MOCs are distinct object types: Index = authoritative inventory; MOC = interpretive navigation.
7. Links are not relationships. Relationships require semantic meaning. Bare backlinks are insufficient.
8. Architecture evolves through governance (KOS-0011), never through spontaneous restructuring.

## Relationship vocabulary (STD-0004)

`defines · implements · extends · depends_on · derived_from · supports · contrasts_with · supersedes · part_of · instance_of · explains · related_to`

Use `related_to` sparingly — it is the weakest relation. Prefer a specific relation when one applies.

## Lifecycle (STD-0005) — two independent dimensions

- **Maturity:** Proposed → Draft → Reviewed → Adopted
- **Operational:** Active → Superseded → Archived

Every Knowledge Object carries both. Never collapse them into one field.

## Working rules for Claude Code sessions

> **Authoritative source.** A Claude Code session doing architecture work operates *as* the **Knowledge Architect (ROLE-0001)**. That role's Adopted definition — its §4 Authority, §6 Workflows (including *verify before removing*), and boundaries — is the **canonical statement** of these rules. This section is a short orientation, not a second rulebook; where it and ROLE-0001 differ, **ROLE-0001 wins** (and fix the drift). Research work operates as ROLE-0002; independent review as ROLE-0004; owner-reserved decisions belong to ROLE-0005. See the **Roles Index**.

The essentials (full detail in ROLE-0001):

1. **Survey before writing**, and **verify before removing** — never delete a reference/object on a belief it doesn't exist; search and confirm first (ROLE-0001 §6, learned from a real error).
2. **Propose, then execute.** Multi-file change → present plan + file list first. New/amended Standards, object types, batch migrations, renames, Adopted-status changes, and role authority are **owner-reserved** (ROLE-0001 §4.2 / ROLE-0005). The `.claude/settings.json` permission gate enforces this for Constitution/Kernel/Standards/Roles edits.
3. **Formalize only on demonstrated need** (Risk 1: over-architecture). Propose and **log to the Governance Backlog**; don't create unprompted. Still deferred: AD-002 (Architecture Discovery Log), AD-003 (Patterns Catalog).
4. **No spontaneous restructuring.** Batch migrations; never rename incrementally.
5. **Follow the architectural-document workflow**: Architecture Review → **one refinement maximum** → Canonical Specification → Critique → Integration Update.
6. **New documents follow the standards** (STD-0001/0002/0005) and are recorded in the **Identifier Registry**.
7. **Maintain RKA/RRI separation** (Risk 3). Obsidian/Claude-Code mechanics (plugins, Dataview, agent files, settings) are RRI; the architecture is platform-independent. The anti-fabrication rule lives in the Kernel (KOS-0003 §12.1), not the agent files.
8. **Log architectural insights instead of acting on them** — record for the Vision Steward's review rather than folding in mid-task.

**Delegated standing authority** (what a session may do without asking) is recorded in `05 Operations/Standing Authorizations.md`. In-session grants like "keep going" are **session-scoped only** and don't persist.

## Current position and priority order

Conceptual foundation is complete. The project has **entered the use-driven phase** — the first real research workflow has run, and further building is now steered by demonstrated friction rather than a strict sequence.

Done (2026-07-09):
1. ~~STD-0006 Review & Validation Standard.~~
2. ~~Standards Architecture Retrospective~~ (first STD-0006 §4.4 audit): reconciled the versioning and lifecycle-vocabulary conflicts (STD-0001/0002 defer to STD-0005); adopted KOS-0003; consolidated meta-document types.
3. ~~Integration documents~~: Kernel-scoped ones already existed; Standards-layer siblings added (`Standards Index/Dependency Map/Status`).
4. ~~First research workflow (RQ-0001, Jesus/Daoism)~~ in `06 Knowledge Base/INV-0001`, with a Pressure Test Report evaluating the architecture through use.
5. ~~KOS-0012 Knowledge Object Model~~ — un-deferred and adopted after the pressure test demonstrated the need (introduced INV/FND types; reconciled STD-0002 metadata layer with KOS-0003 §12 content layer).

Done (2026-07-09, continued):
6. ~~Templates layer~~: `04 Templates` — TPL-0001…0004 (Claim/Source/Investigation/Finding).
7. ~~Three research workflows~~: INV-0001 (Jesus/Daoism), INV-0002 (phantom traffic jams), INV-0003 (wu wei). Friction fell across runs and **migrated up the stack** (object-model → evidence-structure → graph/operations); verdict each time: **converging, not bloating** (see the three assessment reports in `06 Knowledge Base`).
8. ~~Operations layer begun~~: OPS-0001 (KB Organization, F-11), OPS-0002 (Relationship Integrity & Graph Maintenance, F-12), and the Identifier Registry (F-9, fulfilling STD-0001 §18). Sources/Entities moved to shared KB folders.

Done (2026-07-09, continued):
9. ~~Roles layer authored + implemented as agents~~: **ROLE-0001 Knowledge Architect (Adopted)**; ROLE-0002 Research Specialist, ROLE-0004 Critical Reviewer, ROLE-0005 Vision Steward (Draft, authority proposed). `.claude/agents/`: research-specialist, critical-reviewer, knowledge-architect. **OPS-0003 Research Workflow** defines the circuit (Specialist → Critical Reviewer → Knowledge Architect; Vision Steward coordinates).
10. ~~Governance reflexive assessment~~ (CON-0003 GP-005; **ADR-GOV-0001**): reconciled the three role vocabularies (CON-0003 Functions → KOS-0011 ST-roles → ROLE-NNNN; canonical **Roles Index**); **retired ROLE-0003** (no warrant); created **ROLE-0005 Vision Steward** (owner authority, with constitutional limits); **elevated anti-fabrication into KOS-0003 §12.1** (out of the agent files); split STD-0006 §8 validation authority (structural=ROLE-0001, epistemic=ROLE-0004) + added appeal/dissent (§7.4); created the **Governance Backlog** (KOS-0011 §9), **Standing Authorizations**, **ADR practice** (TPL-0005), and a **settings.json permission gate**.

Open / next (all tracked in `05 Operations/Governance Backlog.md` — consult it first):
- ~~Role authority ratification (GB-2026-011)~~ — **done 2026-07-09.** All active roles Adopted; two refinements applied (ROLE-0002 §4.2a scope boundary; ROLE-0004 §5 procedural-independence limit). The research circuit now runs on Adopted definitions.
- **First real agent run (top priority):** put a 4th research question through the full agent circuit (Specialist → Critical Reviewer → Knowledge Architect) — the first genuine test of the specialists as agents.
- **Graph-integrity automation** (OPS-0002 §6 / GB-2026-004): build only when the KB outgrows manual checks.

**The Governance Backlog is now the single source of open items** (replacing the scattered lists). Deferred-by-decision items (M-1 lifecycle migration, GB-2026-002 quantitative evidence, GB-2026-003 entity template, GB-2026-006 two-dimensional lifecycle field, GB-2026-008 ST-003) live there with their decision status — do not action without demonstrated need or the Vision Steward's approval. *(GB-005 phantom ADRs and GB-2026-007 KOS-0200 fate are now resolved — see the Backlog §3.)*

## Owner

Brian Noon. All Adopted-status changes, migrations, and new standards require his explicit approval.
