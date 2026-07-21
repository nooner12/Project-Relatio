---
title: ADR-GOV-0009 - World-Religions Timeline Program and Lineage Anchors
document_type: Architecture Decision Record
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-21
decision_status: Accepted
decision_date: 2026-07-21
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - ADR-GOV-0003 - Religion Source Base Scope and Stopping Rule
  - ADR-GOV-0007 - Reflexive Architecture Evolution
  - STD-0004 - Relationship & Linking Standard
  - STD-0008 - Epistemic State Standard
  - Governance Backlog
tags:
  - ProjectRelatio
  - ADR
  - Timeline
  - Lineage
  - ProvisionalAnchor
---
# ADR-GOV-0009

# World-Religions Timeline Program and Lineage Anchors

## Adopted Architecture Decision Record

> Establishes the world-religions timeline as a standing research program built from a per-family repeatable unit (source-base family → origins-and-branching investigation → auto-extending timeline), and lays the provisional structural anchors it requires: tradition entities on demand, dates-as-claims with a tradition_type vocabulary, and a provisional `branches_from` lineage edge with a controlled qualifier list — the first live application of ADR-GOV-0007 §2's provisional-anchor doctrine. Inline pointer: Governance Backlog.

---

# 1. Context

The owner directed a historical timeline of religions — origins and branches — with scope reaching toward general world coverage. The vault contains no timeline structure: its seven entities are concepts, not traditions; no origin dates exist as structured data; no lineage edge type exists (STD-0004's `derived_from` means evidential derivation, not tradition descent). Timeline facts are claims: every origin date and branch edge must be sourced, graded, and circuit-reviewed before rendering — an ungraded timeline would be evidence- laundering in visual form.

The repeatable unit already exists in embryo: ADR-GOV-0003 made the Iranian catalog (SRC-0104…0123, cataloguing-only, no investigation attached) the seed instance of a standing source-base library and the reference implementation any future family reuses. A world program is that pattern, iterated.

This is the bootstrap case ADR-GOV-0007 §2 anticipated: the right timeline structure should be discovered by investigation, but investigations need structure to attach to. Resolution: minimal provisional anchors, laid under anchor discipline, expected to be revised by the families they enable.

---

# 2. Decision

## D1 — Program structure: the per-family repeatable unit

The timeline grows family by family through a repeatable unit:

1. The family's source base is catalogued into the standing library (the Iranian/ADR-GOV-0003 pattern);
2. An origins-and-branching investigation consumes it through the full OPS-0003 circuit, producing graded claims for each origin date and lineage edge;
3. The timeline renderer reads the resulting structure — each completed family extends the timeline automatically; nothing renders that is not graded.

## D2 — Tradition entities on demand

Traditions become ENT records only as investigations reach them. No pre-populated gazetteer of unstudied religions. An entity exists when a graded claim needs to attach to it; absence on the timeline means un-investigated, never non-existent.

## D3 — Temporal representation: dates are claims

Origin and branching dates live as CLAIMS (sourced, graded, epistemic-fielded — contestedness is carried by the claim's confidence, natively). A tradition entity carries only: a structured pointer to its dating claim(s) and a display range for rendering. Entities additionally carry a `tradition_type` from a controlled vocabulary — founded / emergent / reform / syncretic — so the schema never demands a founding date from a tradition that has none (the Hinduism-class category error is excluded structurally).

## D4 — Provisional lineage edge: `branches_from`

A new typed relationship, `branches_from` (tradition B branches_from tradition A), asymmetric, entity-to-entity, with a REQUIRED qualifier from a controlled list: schism / reform / syncretic-descent / heterodox-offshoot / disputed. Different kinds of branching render differently. PROVISIONAL under ADR-GOV-0007 §2 anchor discipline: (a) labelled provisional in STD-0004; (b) revision trigger named — the first two family investigations pressure-test the qualifier list and edge semantics, and their findings feed the review queue as recommendations; (c) maximally revisable — a vocabulary entry, not load-bearing architecture. Every `branches_from` edge must be supported by a graded claim (the edge is the render; the claim is the warrant).

## D5 — Sequencing by existing coverage

Iranian family first (INV next — sources complete, zero new cataloguing) → Judaism→Christianity arc (largely consolidation: INV-0011/0013/0014 already carry dating at graded confidence) → Chinese line (Daoism→Xiantiandao→ Yiguandao; INV-0015 partially graded; modest source extension) → genuinely new families (Islam completing the Abrahamic picture; Indian family next) in thesis-priority order.

## D6 — Reliance travels

All timeline content lands R0 until verification passes run. The timeline renders the reliance gate per the visualizer's standing invariant; public- facing ambitions raise the value of the R1/R2 promotion path but change nothing about the gate.

---

# 3. Alternatives Considered

1. **Vault-grounded scope only (three arcs, no world program).** Rejected by owner — and designing anchors for three arcs then stretching to thirty traditions is the retrofit the epistemic-axis work just taught against; world-scale design once is cheaper.
2. **Dates as entity fields (structured origin_date on the entity).** Rejected — religious origins are contested ranges and sometimes category errors; a date field would force false precision and demand foundings from continuous traditions. Claims already carry contestedness natively.
3. **Reuse `derived_from` for lineage.** Rejected — semantic collision with evidential derivation; queries and tooling could not distinguish "this claim derives from this source" from "this tradition descends from that one."
4. **Pre-populate tradition entities for planned families.** Rejected — empty entities are assertions without warrant; the timeline must show what is investigated, not what is intended.
5. **Wait to design lineage structure until after the first family investigation.** Rejected — the bootstrap circularity ADR-GOV-0007 §2 resolves; provisional anchors under anchor discipline are the recorded resolution.

---

# 4. Reasoning

The program applies the architecture's proven splits at a new scale: the repeatable unit is ADR-GOV-0003's seed pattern iterated; the anchors are ADR-GOV-0007's doctrine in first live use; the render-only-graded rule is the evidence discipline extended to visualization; and dates-as-claims reuses the epistemic axis instead of inventing a parallel temporal one. Nothing here is a new kind of thing — it is the existing system, composed.

---

# 5. Consequences

**Benefits:** the timeline accretes family by family, real and useful after family one; every rendered element traceable to a graded claim; anchor revisions flow through the review queue rather than ad-hoc restructuring. **Costs:** each new family is a source-catalog session plus a full circuit investigation (two to four sessions at the established quality bar); world coverage is a program of months; the timeline renderer is a second view mode to build once data exists. **Affected objects:** STD-0004 (branches_from, provisional), STD-0002 (entity document-specific fields), an entity template (created or amended per what exists), the visualizer (future timeline view), the standing source-base library (grows per family).

---

# 6. Decision Authority

Program and structural decision reserved to the **Vision Steward** (CON-0003 §5.2). Proposed on the support surface from the timeline scoping; **ratified in full by Brian Noon.**

---

# 7. Review Trigger

Revisit if (a) the first two family investigations find the qualifier list or branches_from semantics wrong (the named anchor-revision trigger — findings route through the review queue per ADR-GOV-0007 §3), (b) tradition_type proves unable to classify a real tradition, (c) a family cannot be honestly represented by the repeatable unit, or (d) the program's public-facing use makes the R0 gate untenable — which triggers the verification-pass ratification question, not a gate relaxation.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-21|Adopted|Initial world-religions timeline program: per-family repeatable unit on the ADR-GOV-0003 seed pattern; provisional anchors (entities on demand, dates-as-claims + tradition_type, branches_from + qualifier list) under ADR-GOV-0007 §2 anchor discipline; sequencing Iranian → Judaism/Christianity → Chinese → new families; reliance gate travels.|

---

# End ADR-GOV-0009