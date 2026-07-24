---
title: STD-0004 - Relationship & Linking Standard
document_type: Standards Document
version: 1.5
status: Adopted
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Operating System
  - Standards
  - Relationship Architecture
parent_documents:
  - KOS-0009 Knowledge Representation & Information Architecture Framework
  - STD-0007 Terminology & Semantic Stewardship Standard
  - STD-0003 Classification & Discovery Standard
related_documents:
  - STD-0005 Lifecycle & Revision Standard
  - STD-0006 Review & Validation Standard
tags:
  - ProjectRelatio
  - Standards
  - Relationships
  - KnowledgeGraph
  - SemanticArchitecture
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# STD-0004

# Project Relatio Relationship & Linking Standard

## Version 1.5
## Adopted Standards Document

---

# 1. Purpose

The Relationship & Linking Standard defines how Knowledge Objects connect within the Relatio Knowledge Architecture.

The purpose of this standard is to establish meaningful semantic connections between Knowledge Objects rather than merely increasing the number of links.

---

# 2. Standard Principle

Project Relatio adopts:

> Links connect objects. Relationships explain why objects connect.

The value of a knowledge architecture is determined not by the quantity of connections, but by the quality and meaning of those connections.

---

# 3. Scope

This standard governs:

- relationship principles,
- relationship categories,
- approved relationship vocabulary,
- semantic linking practices.

This standard does not govern:

- implementation-specific linking methods,
- database structures,
- Obsidian syntax,
- visualization systems.

---

# 4. Knowledge Relationship Model

A relationship consists of:

```
Subject

↓

Relationship Type

↓

Object
```

Example:

```
STD-0004

depends_on

STD-0007
```

The relationship itself carries architectural meaning.

---

# 5. Relationship Requirements

Every formal relationship should:

1. Have identifiable source and destination objects.
2. Use the most precise available relationship type.
3. Represent meaningful semantic connection.
4. Avoid unnecessary duplication.

---

# 6. Relationship Categories

Project Relatio recognizes five initial relationship categories.

---

# 6.1 Structural Relationships

Describe organization and composition.

Examples:

- part_of
- contains
- instance_of

---

# 6.2 Semantic Relationships

Describe conceptual meaning.

Examples:

- explains
- supports
- contrasts_with

---

# 6.3 Dependency Relationships

Describe requirements and implementation.

Examples:

- depends_on
- implements
- requires

---

# 6.4 Evolutionary Relationships

Describe change over time.

Examples:

- supersedes
- revises
- derived_from

---

# 6.5 Navigational Relationships

Describe exploration paths.

Examples:

- related_to
- see_also

---

# 7. Approved Relationship Vocabulary

Version 1.0 adopts the following foundational relationship types.

---

# defines

Meaning:

A Knowledge Object establishes the meaning, rules, or structure of another object.

Example:

```
STD-0003 defines classification principles.
```

---

# implements

Meaning:

A Knowledge Object applies another object's principles or requirements.

Example:

```
A template implements a standard.
```

---

# extends

Meaning:

A Knowledge Object expands another while maintaining compatibility.

---

# depends_on

Meaning:

A Knowledge Object requires another object for interpretation or operation.

---

# derived_from

Meaning:

A Knowledge Object originates from another.

---

# supports

Meaning:

A Knowledge Object contributes to the purpose or function of another.

---

# contrasts_with

Meaning:

Two Knowledge Objects represent meaningfully different perspectives, approaches, or conclusions.

---

# supersedes

Meaning:

A Knowledge Object replaces a previous version or approach.

---

# part_of

Meaning:

A Knowledge Object belongs to a larger structure.

---

# instance_of

Meaning:

A Knowledge Object represents a specific example of a broader class.

---

# explains

Meaning:

A Knowledge Object provides understanding or interpretation of another.

---

# related_to

Meaning:

A general relationship used only when a more precise relationship cannot yet be determined.

---

# branches_from (PROVISIONAL — ADR-GOV-0009 D4)

Meaning:

Tradition B `branches_from` tradition A — the historical descent of one religious tradition from another. **Entity-to-entity ONLY (ENT → ENT).** Asymmetric; never reciprocated; not a symmetric-advisory candidate (it is directional by construction, like `derived_from`, and `graph_integrity.py` treats it as such).

**Required qualifier.** Every `branches_from` edge carries a `qualifier` naming the *kind* of branching, one of:

- `schism`
- `reform`
- `syncretic-descent`
- `heterodox-offshoot`
- `disputed`
- `continuation`

An edge without a qualifier is **malformed** (a graph-integrity error, not an advisory). Different kinds of branching render differently.

**`continuation` (added v1.3 — ADR-GOV-0010 D1).**

> `continuation` — B `branches_from` A where B carries forward A's principal or main line rather than departing from it: the least-departed descendant after a rupture or transformation. Distinguished from `reform` (reconstitution-with-change) by the absence of a departure connotation.

This value was added by the anchor-vocabulary review (ADR-GOV-0009 §7(a)) in response to INV-0017's demonstrated inability to name a main-line-continuation edge (Rabbinic Judaism carrying forward Second Temple Judaism after 70 CE): every prior value connoted departure. Adding it is **additive repair of a demonstrated gap, not a promotion of the list from provisional to durable** — the qualifier list stays provisional (ADR-GOV-0010 D5); it simply has one more tool in it.

**Warrant rule.** Every `branches_from` edge must be supported by a **graded claim** — the edge is the render; the claim is the warrant. An unwarranted edge is a graph-integrity error. (Because a warrant is a claim about lineage rather than a structured pointer on the edge, this rule is **review-checked, not tool-checked** — see §7.2 and `tools/README.md`.)

**Provisional status (ADR-GOV-0007 §2 anchor discipline).** This type and its qualifier list are *scaffolding*, expected to be revised by the first two family investigations of the world-religions timeline program (ADR-GOV-0009); their findings on edge semantics route to the review queue as recommendations (ADR-GOV-0007 §3). It is a vocabulary entry, not load-bearing architecture — maximally revisable. **Named revision trigger: ADR-GOV-0009 §7(a).**

---

# projects_to (NON-EVIDENTIAL — ADR-GOV-0012 D5)

Meaning:

A **non-tradition entity** `projects_to` a **tradition entity**: *for rendering, re-anchor this node here.* It asserts a **modeling projection for display** and asserts **nothing about the world**.

**Directionality and domain.** Directional, non-tradition entity → tradition entity (`rendering_class: community` or `substrate` → `rendering_class: tradition`). Asymmetric; never reciprocated; never a symmetric-advisory candidate. **Multi-target** where a node honestly projects to more than one tradition.

**Machine-traversable, not annotational.** Entries are **graph claims** (STD-0002 §12.1): a dangling `projects_to` is an integrity **error**. Roll-up rendering (ADR-GOV-0012 D7) will traverse this edge, so it may not be a comment or a prose note.

**NON-EVIDENTIAL — the constitutive property.** `projects_to` takes:

- **NO `qualifier` key** (there is no kind-of-projection vocabulary and none is coming),
- **NO warrant rule** (there is no claim to warrant — nothing is asserted about history),
- **NO confidence component** (a projection has no grade; grading it would make it evidential).

An entry carrying a `qualifier` or a `confidence` component is **malformed** and is rejected by `graph_integrity.py` at error level. **`projects_to` is never read as a historical relationship.** Any substantive relationship between the two entities remains a claim — graded, warranted, and reviewable in the normal way — and is encoded, if at all, by an evidential type such as `influenced_by`.

**Scope limit, carried from ADR-GOV-0012 D5.** `projects_to` is **defined and demonstrated for the community-to-tradition case only.** Its adequacy for the **substrate** direction is **expressly untested**: a substrate renders as a containing band rather than a projecting node, which may require the reverse reading or no projection relation at all. That question is settled when substrate rendering is built (deferred, ADR-GOV-0012 D7). **`projects_to` sets no precedent for how the substrate case is eventually modeled.**

---

# influenced_by (ADR-GOV-0012 D6)

Meaning:

Tradition B `influenced_by` tradition/community A — a **documented influence relationship that is NOT descent**. It is the type that lets the graph carry what `branches_from` may never be stretched to carry.

**Directionality and domain.** **ENT → ENT only**, parallel to `branches_from`. **Asymmetric; never auto-reciprocated** — mutual influence is **two explicit edges**, never one symmetric edge. `graph_integrity.py` treats it as directional and raises no reciprocity advisory on it. **Multiple targets are permitted from birth**; it does not inherit `branches_from`'s de-facto single-parent practice.

**Required qualifier.** Every `influenced_by` edge carries a `qualifier` from a deliberately **minimal, explicitly provisional** two-value list:

- `documented` — the influence relationship is attested in the record.
- `contested` — the influence relationship is itself contested; the analogue of `branches_from`'s `disputed`, and what makes a contested influence claim *render* as contested.

The list is minimal **by design and on evidence**: freezing a controlled list before use is the error ADR-GOV-0010 had to repair. A speculative taxonomy of influence kinds (thematic / structural / textual / institutional) is **not** invented in advance of a case that needs one; the list is expected to be extended by the third case.

**Warrant rule — graded claim(s) PLUS a required not-descent determination.** Every `influenced_by` edge must be backed by a **graded claim** (the edge renders; the claim warrants) **and** must carry a **recorded not-descent determination** stating why `branches_from` was refused. **The not-descent requirement is constitutive** (ADR-GOV-0012 D6): influence is far easier to over-assert than descent, and without this rule `influenced_by` becomes the soft option that empties the edge-restraint rule of force. **No instance may be created without it.** Unlike `branches_from`'s warrant rule, both are carried as **structured, resolvable pointers on the edge** (§7.3) and are therefore **tool-checked**, not review-checked.

**What it must NOT collapse into.** (1) A `related_to` for traditions — it carries a graded warrant or it does not exist. (2) A **comfort edge** drawn to relieve the visual discomfort of a disconnected node. (3) A substitute for `branches_from` + `disputed` where descent is genuinely in question but unproven — **that remains a descent case**, and conflating the two destroys the distinction the edge-restraint rule protects.

**Render posture at creation.** `influenced_by` does **not** render on the default timeline (ADR-GOV-0012 D7); roll-up rendering through `projects_to` is specified as intended future view behavior and is **not built**. The hard constraint recorded for that future build: **a node whose only edges are `influenced_by` must still read as a ROOT, never as a branch** — if an influence connector can make an unconnected tradition look like a child of anything, the render is wrong.

---

# 7.1 Machine-Readable Encoding (v1.1)

The vocabulary above is expressed in metadata through the typed **`relationships`** block defined by STD-0002 §7 — each entry pairs a `type` from this vocabulary with a `target` identifier. This closes Pressure Test **F-4** / **GB-2026-001**, where these types could previously live only in an object's prose. The flat `parent_documents`/`related_documents` lists remain the tooling-read graph for dangling-reference checks; the typed block adds the *meaning* of each edge, which `graph_integrity.py` uses for type-aware reciprocity (§11 *False Reciprocity* — directional types such as `derived_from`, `supports`, `part_of` are not expected to reciprocate; symmetric types such as `related_to`, `contrasts_with` are).

---

# 7.2 The `qualifier` key (v1.2 — branches_from; extended v1.5)

The typed `relationships` block gains an optional **`qualifier`** key, **required** on `branches_from` (this section) and on `influenced_by` (§7.3), each drawing from its **own** controlled list. It is **expressly forbidden on `projects_to`**, which is non-evidential and takes no qualifier — a qualified `projects_to` is malformed, not ignored (v1.5). On any other type a `qualifier` is meaningless and ignored.

```
relationships:
  - type: branches_from
    target: ENT-00XX
    qualifier: schism
```

`qualifier` takes one value from the controlled list in the `branches_from` entry above (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed` / `continuation`). `graph_integrity.py` enforces the qualifier-required rule, the vocabulary, and the ENT → ENT restriction as errors.

**Disambiguation note — the two `reform` vocabularies (D3, ADR-GOV-0010).** The `branches_from` **qualifier** `reform` (this field, STD-0004 §7.2 — a *kind of descent relationship*) and the STD-0002 §11 **`tradition_type`** value `reform` (a different field — *how a tradition came to be*) are **different vocabularies on different fields that coincidentally share a word.** They are never conflated: a tradition may carry `tradition_type: reform` while its lineage edge carries any qualifier (or vice versa), and the two are graded and reviewed independently. (Rabbinic Judaism is the case that exposed the collision: `tradition_type: reform` with a `branches_from` qualifier of `continuation`.)

---

# 7.3 Encoding `influenced_by` and `projects_to` (v1.5 — ADR-GOV-0012 D5/D6)

## `influenced_by` — qualifier + the two warrant keys

```
relationships:
  - type: influenced_by
    target: ENT-00XX          # ENT → ENT; repeat the block for each target
    qualifier: documented     # documented | contested — REQUIRED
    warrant:                  # REQUIRED, non-empty; graded record(s) — graph claims
      - CLM-00XX
      - FND-00XX
    not_descent: CLM-00XX     # REQUIRED; the record carrying the not-descent determination
```

- `qualifier` takes one value from the `influenced_by` list above (`documented` / `contested`). An unqualified or out-of-vocabulary edge is **malformed**.
- **`warrant`** is a non-empty list of identifiers of **graded records** (Claim or Finding Records). Entries are **graph claims** (STD-0002 §12.1) and must resolve; a dangling warrant is an integrity error.
- **`not_descent`** names the record carrying the **recorded not-descent determination** — the statement of why `branches_from` was refused for this pair. It is a graph claim and must resolve. **It may name a record that also appears in `warrant`** (usually it does: the claim that establishes the influence is normally the claim that refuses the descent). What matters is that the determination is **named explicitly**, so an edge can never be created without one.
- **Why these are structured pointers when `branches_from`'s warrant is prose.** `branches_from`'s warrant rule is review-checked because a lineage warrant is a claim *about* descent, not a pointer. `influenced_by`'s is different in kind: ADR-GOV-0012 D6 makes the not-descent determination **constitutive** of the type, so it is encoded where a tool can refuse an edge that lacks it. `graph_integrity.py` enforces the ENT → ENT restriction, the qualifier vocabulary, warrant presence and resolvability, and `not_descent` presence and resolvability — **all as errors**.

## `projects_to` — no qualifier, no warrant, no confidence

```
relationships:
  - type: projects_to
    target: ENT-00XX          # a tradition-class entity; repeat the block for each target
```

- **That is the entire encoding.** `projects_to` takes **no** `qualifier`, **no** `warrant`, **no** `not_descent`, and **no** confidence component. Any of them present makes the entry **malformed** and is rejected at error level — the enforcement that keeps a non-evidential relation out of the evidential vocabulary rather than trusting it to stay there.
- Source must be a non-tradition entity (`rendering_class: community` or `substrate`); target must be a `tradition`-class entity. A dangling target is an integrity error, because roll-up rendering will traverse this edge.

---

# 8. Relationship Directionality

Relationships may be directional.

Example:

Correct:

```
STD-0004

depends_on

STD-0007
```

Incorrect assumption:

```
STD-0007

depends_on

STD-0004
```

Direction is part of meaning.

---

# 9. Relationship Precision Principle

Project Relatio prefers:

```
specific relationship
```

over:

```
generic relationship
```

Example:

Preferred:

```
implements
```

instead of:

```
related_to
```

when implementation exists.

---

# 10. Linking Principle

Project Relatio adopts:

> Create relationships because they improve understanding, not because links are available.

---

# 11. Relationship Anti-Patterns

## Link Quantity Optimization

Creating links merely to increase graph density.

---

## Relationship Ambiguity

Using broad relationships when specific meaning exists.

---

## False Reciprocity

Assuming every relationship works in both directions.

---

## Structural Substitution

Using folders or tags as replacements for relationships.

---

# 12. Relationship Evolution

The relationship vocabulary will evolve through use.

New relationship types require:

- definition,
- purpose,
- examples,
- compatibility review.

---

# 13. Relationship to Other Standards

STD-0004 depends on:

- STD-0007 Terminology & Semantic Stewardship
- STD-0003 Classification & Discovery

STD-0004 supports:

- research modeling,
- knowledge graphs,
- future automation,
- advanced discovery.

---

# 14. Governance

Relationship vocabulary is governed through:

KOS-0011 Governance, Stewardship & Evolution Framework.

Changes require:

- rationale,
- review,
- version control.

---

# 15. Closing Principle

Project Relatio adopts:

> The purpose of linking is not connection. The purpose of linking is understanding.

Meaningful relationships transform stored information into structured knowledge.

---

# 16. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial relationship and linking standard|
|1.1|2026-07-11|Adopted|Added §7.1 Machine-Readable Encoding: the vocabulary is now carried in the typed `relationships` frontmatter block (STD-0002 §7 v1.6), closing F-4 / GB-2026-001. No vocabulary change — the twelve approved types are unchanged.|
|1.2|2026-07-21|Adopted|Added the **provisional `branches_from`** relationship type (ENT → ENT, asymmetric, REQUIRED qualifier from schism/reform/syncretic-descent/heterodox-offshoot/disputed, warrant-by-graded-claim) enacting ADR-GOV-0009 D4; added §7.2 defining the optional `qualifier` frontmatter key (valid only on branches_from). PROVISIONAL under ADR-GOV-0007 §2 anchor discipline; revision trigger ADR-GOV-0009 §7(a). Additive — the existing twelve types are unchanged.|
|1.3|2026-07-22|Adopted|**Anchor-vocabulary review (ADR-GOV-0009 §7(a)) enacting ADR-GOV-0010 D1/D3.** Added a sixth `branches_from` qualifier **`continuation`** (B carries forward A's principal/main line rather than departing — the least-departed descendant after a rupture; distinguished from `reform` by the absence of a departure connotation) in response to INV-0017's demonstrated inability to name a main-line-continuation edge (Rabbinic Judaism); list now schism/reform/syncretic-descent/heterodox-offshoot/disputed/continuation. Added §7.2 the two-`reform`-vocabularies disambiguation note (the `branches_from` qualifier `reform` and the STD-0002 `tradition_type` value `reform` are different fields sharing a word, never conflated). **Additive repair of a demonstrated gap — the qualifier list stays PROVISIONAL (ADR-GOV-0010 D5); NOT a promotion toward durable.** The `graph_integrity.py` enforced set was extended to match.|
|1.4|2026-07-22|Adopted|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|
|1.5|2026-07-24|Adopted|**Enacts ADR-GOV-0012 D5 and D6 in ONE bump** (both landed in a single commit; the two vocabulary entries are one governance package under D1 and are never scoped separately). **D5 — `projects_to` created (NON-EVIDENTIAL).** Directional non-tradition entity → tradition entity, multi-target, **machine-traversable** (entries are graph claims; a dangling `projects_to` is an error, because roll-up rendering will traverse it). It asserts a **modeling projection for display** and nothing about the world: **no `qualifier` key, no warrant rule, no confidence component** — each recorded explicitly and enforced at error level so a later reader cannot mistake it for an evidential edge. Reuse of `bounded_by`, `part_of`, and `instance_of` was considered and rejected on the record (ADR-GOV-0012 §3). **Scope limit carried into the entry: defined and demonstrated for the community-to-tradition case ONLY; substrate adequacy expressly untested and deferred (D7), and `projects_to` sets no precedent for how the substrate case is eventually modeled.** **D6 — `influenced_by` created**, exactly to INV-0018's Anchor Fit Part 2 specification and neither weakened nor extended: **asymmetric** (mutual influence is two explicit edges; never auto-reciprocated, never a reciprocity-advisory candidate), **ENT → ENT**, **multi-target from birth**, a **minimal, explicitly provisional** `documented` / `contested` qualifier list (minimal by design — freezing a list before use is the error ADR-GOV-0010 had to repair), and a warrant rule of **graded claim(s) PLUS a REQUIRED recorded not-descent determination**, the latter **constitutive**: without it the type becomes the soft option that empties the edge-restraint rule of force, so no instance may exist without one. **Render posture at creation: NOT rendered on the default timeline** (D7); roll-up through `projects_to` is specified as intended future behavior and **not built**, carrying the hard constraint that a node whose only edges are `influenced_by` must still read as a **root**. Added **§7.3** defining the encoding of both types — `influenced_by`'s `qualifier` + the two **structured, resolvable** keys `warrant` (non-empty list of graded records) and `not_descent` (the record carrying the determination, which may also appear in `warrant`), and `projects_to`'s deliberately empty encoding — with the reason the `influenced_by` warrant is **tool-checked** where `branches_from`'s is review-checked. Extended **§7.2**: `qualifier` is now required on two types with **separate** controlled lists and is **expressly forbidden on `projects_to`** (malformed, not ignored). `graph_integrity.py` enforces every rule above at error level, with fixtures proving each check FIRES. Additive — the thirteen existing types are unchanged, and INV-0018's `branches_from` refusal is untouched.|

---

# End STD-0004