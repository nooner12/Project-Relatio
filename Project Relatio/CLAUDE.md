# CLAUDE.md — Project Relatio

This file is Relatio Reference Implementation (RRI) tooling. It is not a Knowledge Object and is not governed by KOS lifecycle rules. It exists to orient Claude Code sessions working inside this vault.

## What this vault is

This vault is the **Relatio Reference Implementation (RRI)** — the Obsidian implementation of the **Relatio Knowledge Architecture (RKA)**. Maintain this distinction at all times:

- **RKA** = the abstract, platform-independent architecture (principles, standards, governance, object types, relationships).
- **RRI** = this vault: folders, Markdown, YAML, templates, workflows, plugins.
- Folder structure is an *implementation expression*, not the architecture. Folders represent classification only; the knowledge graph lives in semantic relationships, not the file tree.

Central principle: **Knowledge is a structured network of meaningful relationships, not a collection of stored information.**

## Purpose and scope guardrail (owner, 2026-07-09; reframed by ADR-GOV-0002, 2026-07-11)

**Project Relatio's purpose is to conduct thorough and disciplined research on Brian's research questions — and to become an excellent knowledge architecture in the process.** Both are legitimate aims; the research is primary, and building toward the architecture Brian has named ("eventually the world's best") is a genuine concurrent goal, not a deferred one.

The operative discipline is a **merit principle, not a brake**: **every addition — from any contributor — earns its place on its merits, by improving a real answer or the system's ability to produce one.** Additions are justified by *use*, not by symmetry or completeness; a standard, object type, role, or workflow step that catches no real failure and improves no real answer is removed. When in doubt, run a research question through the system and see what breaks. Apply this test to contributions **by their merit, not their source** (including your own).

> *This reframes an earlier, fear-based version. The original guardrail was a defence against a specific collaborator (ChatGPT) that over-generated architecture; it was never a description of the owner, who does not apply it to himself. With that framing removed, the point is discipline-by-use, not reflexive refusal — do not suppress genuinely warranted work to be "safe." See ADR-GOV-0002.*

## Health / clinical-evidence scope (ADR-GOV-0002)

The system may **investigate any question to full depth and rigour** — the scope is not a limit on inquiry. What it does **not** do is give **individualized** medical/clinical advice: it lacks the person's history, labs, and exam, so it reports *general evidence* and brackets the individual case. That is epistemic honesty, not a restriction. Health findings are framed for **expert application** and are **gated from third-party external reliance** (STD-0006 §7.5) pending genuine independent and clinician review. **The system informs expert judgment — including Brian's own clinical background — it does not replace a clinician.** The boundary is on outward-facing individualized claims, not on what may be researched.

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
- **`ADR-GOV-0004` + `ADR-GOV-0005`** — **standing rules that bind every session; read them.** ADR-GOV-0004: **D1** investigation closure · **D2** decision tiering (standing rule → ADR + inline Backlog pointer; one-off → Backlog only) · **D3** close-out back-update · **D4** frontmatter references are graph claims. ADR-GOV-0005 extends it: **§1** closure state lives in the banner + history row, *not* frontmatter · **§2** out-of-record evidence may satisfy an acceptance criterion only via an in-record citation naming document *and version* · **§3** D3 has **no document home** (deferred to second use, GB-2026-034) — the ADR text *is* the operative rule · **§4** close-out includes a **CLAUDE.md currency check** (tier-1 fixes made directly, commit citing D3) · **§5** path-length constraint, placed in STD-0001 §8
- `STD-0001` — Naming & Identification
- `STD-0002` — Metadata & YAML
- `STD-0003` — Classification & Discovery
- `STD-0004` — Relationship & Linking
- `STD-0005` — Lifecycle & Revision
- `STD-0007` — Terminology & Semantic Stewardship
- `STD-0006` — Review & Validation (Adopted 2026-07-09)
- `STD-0008` — Epistemic State (Adopted 2026-07-20). **The epistemic axis exists**: every Claim/Finding Record carries two independent sub-axes — `confidence` (always a **list** of graded components, KOS-0003 §8 canonical labels Very High/High/Moderate/Low/Very Low, split grades never averaged) and `reliance_tier` (**R0/R1/R2** per ADR-GOV-0006, per-locus with floor roll-up; the gate travels with the data). Field format/placement in STD-0002 §11 (v1.8).
- **`ADR-GOV-0006` + `ADR-GOV-0007`** (owner-authored, Adopted 2026-07-20): the tiered external-reliance model (R0 parametric / R1 retrieval-verified under edition-discipline / R2 independently verified — replaces the binary reliance gate) and reflexive architecture evolution (provisional anchors; reflexive findings inform, never self-execute).

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

Use `related_to` sparingly — it is the weakest relation. Prefer a specific relation when one applies. These types are now carried in a typed **`relationships:`** frontmatter block (STD-0002 §7 v1.6 / STD-0004 §7.1), not only in object prose (GB-2026-001, implemented 2026-07-11); `graph_integrity.py` is type-aware.

## Lifecycle (STD-0005) — two independent dimensions

- **Maturity:** Proposed → Draft → Reviewed → Adopted — carried in `status:`
- **Operational:** Active → Superseded → Archived — carried in `operational_status:`

Every Knowledge Object carries both, in the two separate fields (STD-0002 v1.5, implemented across the vault 2026-07-11 — GB-2026-006). Never collapse them into one field.

## Working rules for Claude Code sessions

> **Authoritative source.** A Claude Code session doing architecture work operates *as* the **Knowledge Architect (ROLE-0001)**. That role's Adopted definition — its §4 Authority, §6 Workflows (including *verify before removing*), and boundaries — is the **canonical statement** of these rules. This section is a short orientation, not a second rulebook; where it and ROLE-0001 differ, **ROLE-0001 wins** (and fix the drift). Research work operates as ROLE-0002; independent review as ROLE-0004; owner-reserved decisions belong to ROLE-0005. See the **Roles Index**.

The essentials (full detail in ROLE-0001):

1. **Survey before writing**, and **verify before removing** — never delete a reference/object on a belief it doesn't exist; search and confirm first (ROLE-0001 §6, learned from a real error).
2. **Propose, then execute.** Multi-file change → present plan + file list first. New/amended Standards, object types, batch migrations, renames, Adopted-status changes, and role authority are **owner-reserved** (ROLE-0001 §4.2 / ROLE-0005). The `.claude/settings.json` permission gate enforces this for Constitution/Kernel/Standards/Roles edits.
3. **Formalize on demonstrated need — justify by use** (per the merit principle above; ADR-GOV-0002). Propose and **log to the Governance Backlog**; don't create unprompted, but don't suppress warranted work either. Still deferred (no demonstrated need yet): AD-002 (Architecture Discovery Log), AD-003 (Patterns Catalog).
4. **No spontaneous restructuring.** Batch migrations; never rename incrementally.
5. **Follow the architectural-document workflow**: Architecture Review → **one refinement maximum** → Canonical Specification → Critique → Integration Update.
6. **New documents follow the standards** (STD-0001/0002/0005) and are recorded in the **Identifier Registry**.
7. **Maintain RKA/RRI separation.** Obsidian/Claude-Code mechanics (plugins, Dataview, agent files, settings) are RRI; the architecture is platform-independent. The anti-fabrication rule lives in the Kernel (KOS-0003 §12.1), not the agent files.
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

Done (2026-07-11, Phase II re-scope — owner-directed):
11. ~~Architecture Baseline v1.0~~ (`05 Operations/Architecture Baseline.md`): a one-page **freeze** of the stable concepts (Phase II brief M1) — changes to a frozen concept now require implementation evidence, not further design. The backlog stays open; the freeze guards concepts, not the backlog.
12. ~~Two-dimensional lifecycle field~~ (GB-2026-006): `status` (maturity) + `operational_status` (operational) implemented across 109 objects; STD-0002 v1.5, STD-0005 §24 v1.1.
13. ~~Typed relationships in frontmatter~~ (GB-2026-001): typed `relationships:` block (STD-0002 §7 v1.6, STD-0004 §7.1 v1.1); 52 KB objects back-encoded; `graph_integrity.py` made type-aware; templates updated.

Open / next (all tracked in `05 Operations/Governance Backlog.md` — consult it first):
- ~~Role authority ratification (GB-2026-011)~~ — **done 2026-07-09.** All active roles Adopted; two refinements applied (ROLE-0002 §4.2a scope boundary; ROLE-0004 §5 procedural-independence limit). The research circuit now runs on Adopted definitions.
- **Agent circuit:** operational. The Specialist → Critical Reviewer → Knowledge Architect circuit has run live; sessions execute via transfer briefs. Current priorities live in the Backlog, not here.
- **Graph-integrity automation:** built (`tools/graph_integrity.py`, per OPS-0002 §6 — dangling-reference and one-directional-link checks over `related_documents`/`parent_documents`). Run it every session; do not trace by hand.
- **Epistemic-field automation:** built (2026-07-20) — `validate.py` shape-checks `confidence`/`reliance_tier` on Claim/Finding Records (STD-0008 / STD-0002 §11 v1.8). **Currently WARNING-gated pending migration (GB-2026-038):** the 101 pre-existing CLM/FND records predate the fields and are a known migration gap, not defects — they surface as one aggregate migration-pending warning and the vault still exits PASS. Do **not** backfill them opportunistically; migration is its own later brief, which flips `EPISTEMIC_FIELDS_ENFORCED` to `True` (plus the test guard) to promote the check to error-level. Malformed or half-authored epistemic fields on a *new* record warn individually — fix those immediately.
- **Version-coherence automation:** built (GB-2026-035, 2026-07-20) — `validate.py` checks that a document's `version:` frontmatter, its `## Version` heading, and the newest row of its `# Revision History` table agree. **Mismatches are ERRORS and fail validation** (owner ruling 2026-07-21, promoted from warning: a stale version field is a record lying about itself). **Do not reconcile versions by hand — run the tool.** Two rules it enforces and you should follow when editing by hand: the **newest history row is found by parsing and taking the max, never by position** (rows are not always in order — GB-2026-029), and **an edit that bumps a version must also write its history row** — the 40th drift instance (ROLE-0003) was exactly that omission, and it now fails the build.
- **Investigation closure state (as of 2026-07-20, INV-0015 circuit close):** **all fifteen investigations INV-0001…INV-0015 are formally CLOSED; none open.** INV-0015 (Academic Classification of Yiguandao, Reading C) executed its full OPS-0003 circuit and closed 2026-07-20 under the owner's conditional pre-authorization (Critical Review – RQ-0015 Conformant with Flags, all three non-determinate flags adopted; no confidence level changed; ROLE-0001 validation in-record at INV-0015 v0.4; Registry v1.28). Its circuit was **verification-light throughout** (paywalled scholarly interiors; Chinese-language corpus a recorded gap) — the thin-base Level-2 components are completed findings per the pre-authorized outcome class, and **INV-0015's findings remain §7.5-analog-gated: not cleared for external reliance (thesis-supporting or public use) regardless of closure**. "Closed" is still not a maturity promotion (INVs stay `status: Draft`). INV-0014 (The Historical Jesus) executed its full OPS-0003 circuit and closed 2026-07-20 under the owner's conditional pre-authorization (Critical Review – RQ-0014 Conformant with Flags, all determinate flags remediated; no confidence level changed; ROLE-0001 validation in-record at INV-0014 v0.3; Registry v1.26). INV-0011 closed 2026-07-21 after its criterion-#2 sub-question circuit (met at v0.5, not v0.2). "Closed" means the inquiry is complete; it is **not** a maturity promotion (INVs stay `status: Draft`) and **not** a clearance for external reliance — INV-0014's findings in particular remain §7.5-gated (verification-split review; independent re-verification required before thesis-supporting or public use).
- **Any tool that enumerates the vault MUST use extended-length path handling** (`\\?\` or equivalent) — a scan without it is non-conforming and its results invalid *even when it reports clean*, because files past the Windows 260-char `MAX_PATH` go silently unscanned. **This requirement is unconditional and does not depend on any file currently being over the ceiling.** As of 2026-07-21 **no vault file exceeds either limit** — the four formerly-grandfathered `INV-0006` claims were renamed under owner approval, and the grandfather set is now empty (longest path is 179). Rule and the ≤180-char relative-path budget: **STD-0001 §8** (Path Length Constraint).

**The Governance Backlog is now the single source of open items** (replacing the scattered lists). Deferred-by-decision items (GB-2026-002 quantitative evidence, GB-2026-003 entity template, GB-2026-008 ST-003) live there with their decision status — do not action without demonstrated need or the Vision Steward's approval. *(GB-005 phantom ADRs, GB-2026-007 KOS-0200 fate, GB-2026-006 two-dimensional lifecycle field, GB-2026-001 typed relationships, GB-2026-031 INV closure convention, and GB-2026-028 version-vs-history drift are now resolved — see the Backlog §3.)* *(GB-2026-035, the durable `validate.py` coherence check carried forward when GB-2026-028 closed on remediation rather than prevention, was **built and resolved 2026-07-20** — the class now has a countermeasure, not just a sweep.)*

## Owner

Brian Noon. All Adopted-status changes, migrations, and new standards require his explicit approval.
