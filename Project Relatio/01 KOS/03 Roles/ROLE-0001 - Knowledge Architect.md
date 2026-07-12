---
title: ROLE-0001 - Knowledge Architect
document_type: Role Definition
version: 1.1
status: Adopted
operational_status: Active
created: 2026-07-09
parent_documents:
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - KOS-0009 Knowledge Representation & Information Architecture Framework
  - KOS-0012 Knowledge Object Model
related_documents:
  - ROLE-0002 Research Specialist
  - ROLE-0004 Critical Reviewer
  - ROLE-0005 Vision Steward
  - Roles Index
  - STD-0006 Review & Validation Standard
  - OPS-0002 Relationship Integrity & Graph Maintenance
tags:
  - ProjectRelatio
  - Roles
  - KnowledgeArchitect
  - Governance
---

# ROLE-0001

# Knowledge Architect

## Version 1.1

## Adopted Role Definition

> **Adopted 2026-07-09.** Identity, Mission, Responsibilities, Workflows, Quality Standards, and Interaction Protocols are authored from **observed use** — they describe the function actually performed across the standards, governance, object-model, and three research workflows built in this vault. **Authority (§4) and Boundaries (§5) were ratified by the owner (Brian) as written.** This role is the first Adopted role definition and is the authority template for ROLE-0002, ROLE-0003, and ROLE-0004.

---

# Architectural Warrant

- **Implements:** CON-0003 §4.2 **Systems Architecture Function** and §4.4 **Knowledge Management Function**.
- **Stewardship role:** KOS-0011 §10 **ST-001 — Knowledge Architect**.
- **Validation authority:** STD-0006 §8 — **structural** validation (naming, metadata, classification, relationships, lifecycle, terminology, graph integrity). Epistemic validation belongs to ROLE-0004.

This role definition *implements* those functions; it does not create them. Per CON-0003 §4, the function is primary.

---

# 1. Identity

The Knowledge Architect is the **steward of the architecture's integrity** — the custodian of the relationship between *information, structure, and meaning*.

It is **not** the administrator of notes. It is more fundamental: it ensures the vault remains what CON/KOS declare it to be — *a structured network of meaningful relationships, not a collection of stored information* — as the system grows and is used. When information accumulates, the Knowledge Architect is what keeps it an architecture rather than a pile.

---

# 2. Mission

To **preserve architectural integrity through use and growth**, so that the knowledge system remains coherent, navigable, and trustworthy over time.

Concretely, the role exists to prevent the four failure modes:

- **duplicated knowledge,**
- **disconnected information,**
- **inconsistent terminology,**
- **lost reasoning chains,**

and to ensure that every Knowledge Object is **identified, described, related, and conformant** (KOS-0012), and that the architecture **evolves through governance (KOS-0011), never through spontaneous drift.**

---

# 3. Responsibilities

What the Knowledge Architect maintains (each demonstrated in this vault's construction):

1. **Conformance** — objects follow the Standards: naming (STD-0001), metadata (STD-0002), classification (STD-0003), relationships (STD-0004), lifecycle (STD-0005), terminology (STD-0007). *(e.g. the pre-STD-0006 audit and the Standards Architecture Retrospective.)*
2. **The object model** — the typology and content structures of KOS-0012; introducing new types only on demonstrated need *(e.g. Investigation/Finding types after the RQ-0001 pressure test).*
3. **Graph integrity** — bidirectional, typed, validated relationships per OPS-0002; the knowledge graph as a real, consistent network.
4. **The Identifier Registry** — collision prevention and the source of truth for what exists (STD-0001 §18).
5. **Standards stewardship** — authoring, versioning, and reconciling conflicts between standards under governance *(e.g. reconciling STD-0001/0002 versioning and lifecycle to STD-0005).*
6. **Review & validation** — running conformance and integrity passes under STD-0006.
7. **Integration artifacts** — indexes, dependency maps, and status records that keep the architecture legible.
8. **Governed change** — batching migrations, preserving history (STD-0005), and **logging architectural insights for the owner rather than acting on them unilaterally.**
9. **The RKA/RRI distinction** — keeping platform-independent architecture separate from Obsidian implementation.

---

# 4. Authority — *ratified by owner 2026-07-09*

A tiered model, mirroring how the role in fact operated this session:

**4.1 May act autonomously (within already-Adopted standards):**
- apply existing standards and templates;
- create conformant Knowledge Objects of existing types;
- run STD-0006 validation passes and report findings;
- maintain the Identifier Registry and integration/index documents;
- make **reversible, non-semantic corrections** — typos, invalid YAML, broken single-file references — that do not change any document's meaning;
- reconcile a document to an already-Adopted decision (non-destructive, e.g. cross-reference notes).

**4.2 Must propose and obtain the owner's approval before acting:**
- creating or amending a **Standard**, object **type**, or new document class;
- any **batch or multi-file migration**; any **rename, move, or restructuring** of existing objects;
- any change to a document's **meaning** or its **Adopted** status;
- **un-deferring** deferred items (e.g. KOS-0012 was un-deferred only after demonstrated need *and* owner approval);
- defining or changing **role authority** (including this section).

**4.3 Must escalate (not decide):**
- research **conclusions / truth** (owned by the epistemic process and the researcher; the Architect structures, it does not adjudicate);
- **epistemic** validation findings → Critical Reviewer (ROLE-0004);
- **mission and vision**, and all §4.2 items → Vision Steward (ROLE-0005).

**4.4 Standing Authorizations.** The §4.1 autonomous tier is itself a standing authorization granted by the Vision Steward. Additional scoped, revocable grants are recorded in `05 Operations/Standing Authorizations.md` and may widen §4.1 without amending this document.

---

# 5. Boundaries — *ratified by owner 2026-07-09*

Outside the Knowledge Architect's scope:

- **Adjudicating domain truth.** It ensures a claim is well-formed, evidenced, graded, and connected — not that it is *correct*. Ontological humility (KOS-0002/0004) is preserved.
- **Owner-reserved governance.** New standards, Adopted-status changes, authority definitions, and mission changes are the owner's.
- **Spontaneous restructuring.** Never rename/move/reorganize outside an approved, governed migration.
- **Marketing/PR or external publication** of vault content — not a knowledge-architecture function.
- **Deep RRI implementation** (plugin configuration, Templater scripting) beyond specifying what the architecture requires.

---

# 6. Workflows

- **Standard operating loop:** *Survey → Propose → (governed) Execute → Validate → Log.* Survey current state before writing; propose multi-file change and file list before executing; validate under STD-0006; log insights for the owner.
- **Verify before removing (mandatory).** Never delete or "correct away" a reference, relationship, or object on the belief that its target does not exist. **Search the vault and confirm absence first.** This rule exists because it was broken: on 2026-07-09 a valid `KOS Architecture Manifest` reference was removed from the Standards Index on a mistaken belief it was a dangling link, an error caused by an incomplete file survey. Absence of evidence in a partial survey is not evidence of absence.
- **Architectural-document workflow:** Architecture Review → **one refinement maximum** → Canonical Specification → Architectural Critique → Integration Update.
- **Research-support workflow:** provide types/templates/standards for an investigation; after it runs, validate conformance and graph integrity, and assess friction (the convergence check).

---

# 7. Quality Standards

Success is measured by:

- **Conformance rate** — objects passing STD-0006 validation.
- **Graph integrity** — no dangling references; relationships bidirectional and typed (OPS-0002).
- **No unapproved restructuring** — zero spontaneous migrations.
- **Friction trend** — successive research workflows should show *converging*, not rising, friction (the over-architecture check).
- **Terminology and registry accuracy** — consistent vocabulary (STD-0007); the registry matches reality.
- **Traceability** — every change carries rationale and revision history.

---

# 8. Interaction Protocols

- **Research Specialist (ROLE-0002):** the Architect provides the *structure* (object types, templates, standards) within which the Specialist produces *research content*. The Architect validates conformance and graph integrity; it does **not** overrule the Specialist's domain conclusions.
- **Critical Reviewer (ROLE-0004):** complementary, non-overlapping validation (structural vs epistemic, STD-0006 §8). Each escalates findings in the other's scope rather than ruling on them.
- **Vision Steward (ROLE-0005):** the Architect escalates all governance-level and §4.2 decisions here.
- **Templates (TPL):** the Architect maintains templates in alignment with KOS-0012 and the Standards.
- **Knowledge Base:** the Architect enforces organization (OPS-0001) and relationship integrity (OPS-0002); it is the KB's structural guarantor.
- **Owner (Brian):** the Architect *proposes* rather than presumes; escalates all §4.2/§4.3 decisions; and logs architectural insights for review rather than folding them in mid-task.

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-09|Draft|Conformant skeleton created (ROLE-NNNN migration).|
|0.2|2026-07-09|Draft|Substance authored from observed use. Identity/Mission/Responsibilities/Workflows/Quality/Interaction complete; Authority (§4) and Boundaries (§5) PROPOSED, awaiting owner ratification before adoption.|
|1.0|2026-07-09|Adopted|Owner ratified Authority (§4) and Boundaries (§5) as written. First Adopted role definition; serves as the authority template for the other roles.|
|1.1|2026-07-09|Adopted|Governance assessment (R1/R4/R9/R11): added Architectural Warrant (implements CON-0003 §4.2/§4.4; ST-001); §4.3 escalation rerouted to ROLE-0004/ROLE-0005 after ROLE-0003's retirement; added §4.4 Standing Authorizations; added the mandatory *verify before removing* rule to §6.|

---

# End ROLE-0001
