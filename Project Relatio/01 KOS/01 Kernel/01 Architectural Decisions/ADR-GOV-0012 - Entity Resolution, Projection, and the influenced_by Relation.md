---
title: ADR-GOV-0012 - Entity Resolution, Projection, and the influenced_by Relation
document_type: Architecture Decision Record
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-24
decision_status: Accepted
decision_date: 2026-07-24
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - ADR-GOV-0007 - Reflexive Architecture Evolution
  - ADR-GOV-0009 - World-Religions Timeline Program and Lineage Anchors
  - ADR-GOV-0010 - Continuation Qualifier and the First Reflexive Anchor Revision
  - STD-0002 - Metadata & YAML Standard
  - STD-0004 - Relationship & Linking Standard
  - INV-0016 - Iranian Religious Family Origins and Branching
  - INV-0018 - Islam Origins and Abrahamic Relationships
  - Governance Backlog
tags:
  - ProjectRelatio
  - ADR
  - Entities
  - Relationships
  - Timeline
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-24
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ADR-GOV-0012

# Entity Resolution, Projection, and the influenced_by Relation

## Adopted Architecture Decision Record

> Resolves GB-2026-041. Establishes that entities may coexist at multiple
> granularities under a required `rendering_class` vocabulary; mints a
> non-evidential `projects_to` relation so finer entities can re-anchor to
> the tradition layer for display without asserting history; creates the
> `influenced_by` edge type to its INV-0018 specification; mints Islam's
> honest influence targets as community entities under governance warrant;
> and holds the default timeline to the tradition class, deferring both
> roll-up and substrate rendering. Entity resolution and `influenced_by` are
> ratified as one package that may never be scoped separately. Inline
> pointer: Governance Backlog.

---

# 1. Context

The timeline program (ADR-GOV-0009) exposed a structural limit that the
investigations then demonstrated twice, in opposite directions. The entity
layer carries one resolution — the tradition — while the evidence lives at
several.

INV-0018 established that Islam's documented relationships to Judaism and
Christianity are influence-shaped, not descent-shaped. The edge refusal is
the finding, and it was reviewer-verified as rigorously as a drawn edge
would have been. In reaching it, the entity-precision requirement fired for
the first time: ENT-0012 (Second Temple Judaism, ending 70 CE) is
chronologically impossible as the target of a seventh-century relationship;
ENT-0014 is over-specific; ENT-0013 (Christianity, the tradition whole) is
too coarse, because the documented contact was with Syriac, Ethiopic, and
Najrānī Christianity. Two entity gaps were recorded and no edge was forced.
The honest influence targets are not tradition-resolution entities, and the
entity layer cannot represent them.

AF-3 had already identified the same limit in the coarser direction:
substrate-scale context — the milieu within which traditions arise — has no
honest node either. AF18-4 names the finer direction. One problem, two
directions, two independent demonstrating cases.

The `influenced_by` relation cleared the defer-to-second-use bar (INV-0011
first case, INV-0018 second) and was fully specified in INV-0018's Anchor
Fit, but deliberately not created. An ENT-to-ENT edge is only as honest as
the entity layer's resolution; created alone it would either sit empty or be
forced onto wrong-resolution targets — precisely the failure the
entity-precision requirement exists to block.

# 2. Decision

> Entity resolution and the `influenced_by` relation are resolved together
> as one governance package: the entity layer becomes multi-granularity, a
> non-evidential projection relation carries finer entities to the tradition
> layer for display, `influenced_by` is created and instantiated only
> against honest targets, and the default view renders the tradition class
> alone.

## D1 — Joint scoping (ratified rule)

Entity resolution and `influenced_by` are one governance package. Neither
half may be scoped, enacted, or amended separately from the other; any
future amendment to either reopens both. Ruled by the owner 2026-07-23 and
ratified here.

## D2 — Multi-granularity entity layer

Entities may coexist at multiple granularities. Three rendering classes are
established as a controlled vocabulary on the entity model:

- `tradition` — the existing resolution; lineage actors on the timeline.
- `substrate` — coarser context within which traditions arise; temporally
  native but not a lineage actor.
- `community` — finer, regionally or temporally bounded populations or
  expressions; edge-capable but temporally soft.

Class membership is a modeling judgment recorded at mint and warranted like
any other field.

## D3 — The `rendering_class` field

STD-0002 gains a `rendering_class` field, required at mint, carrying the D2
vocabulary. Existing entities ENT-0008 through ENT-0015 are backfilled as
`tradition`; the backfill adds the field and a history row only and changes
no other content. The recorded entity gaps on ENT-0012/0013/0014 stand as
history — the community entities minted under D8 are the remedy, not a
retrofit. Enforcement follows the migration discipline: define, backfill,
then enforce.

## D4 — Community-class dating semantics

Community entities carry attestation windows, not founding dates: bounds
derived from warranting claims, confidence-inheriting, with honest
imprecision preserved. A community entity is never assigned a
founding-date-style range, and its window is never rendered as one.

## D5 — The `projects_to` relation (newly created)

`projects_to` is added to the STD-0004 approved relationship vocabulary with
exactly these semantics and no others:

- **Directional**, non-tradition entity to tradition entity; **multi-target**
  where a node honestly projects to more than one.
- **Machine-traversable** and validated: entries are graph claims, and a
  dangling `projects_to` is an integrity error. Roll-up rendering (D7) will
  traverse it, so it may not be annotational.
- **Non-evidential.** It asserts a modeling projection for display — "for
  rendering, re-anchor here" — and asserts nothing about the world. It
  carries no qualifier key, no warrant rule, and no confidence component,
  and is never read as a historical relationship. Any substantive
  relationship between the two entities remains a claim, graded and
  reviewable in the normal way.

**The defer-to-second-use bar is cleared, not bypassed.** ADR-GOV-0010 D4
deferred AF-3 as a logged candidate with an explicit re-open trigger: a
second family investigation exhibiting the same strain. INV-0018 is that
second family, and AF18-4 is that strain — the same single-resolution entity
layer failing, in the opposite direction. Two independent demonstrating
cases therefore exist, which is the demonstrated-need threshold the bar sets
(GB-2026-026 / GB-2026-027 precedent, merit principle ADR-GOV-0002). No
exemption is claimed and none is needed.

`projects_to` is additionally **non-evidential**, which is a property worth
recording but is not what clears the bar. It matters because it keeps the
new type out of the evidential vocabulary entirely: it needs no warrant
rule, no qualifier list, and no review cadence, so it adds no grading
surface and cannot be reached for as a hedge. Nothing in this decision
licenses creating an evidential edge type on first use.

**Scope limit.** `projects_to` is defined and demonstrated for the
community-to-tradition case only. Its adequacy for the substrate direction
is untested: a substrate renders as a containing band rather than a
projecting node, which may require the reverse reading or no projection
relation at all. That question is settled when substrate rendering is built,
which D7 defers. This is a deferral of a build question, not a reopening of
D2's principle, and `projects_to` sets no precedent for how the substrate
case is eventually modeled.

## D6 — `influenced_by` created

STD-0004 gains the `influenced_by` edge type exactly as specified in
INV-0018's Anchor Fit Part 2: asymmetric, ENT-to-ENT, multi-target, minimal
qualifier list (`documented` / `contested`), warrant rule = graded claim(s)
plus a required recorded not-descent determination. The not-descent
requirement is constitutive: it is what prevents this type from becoming a
hedge that empties the edge-restraint rule, and no instance may be created
without it.

## D7 — Render posture

The default timeline renders the `tradition` class only. Community entities
are off-timeline at launch; `influenced_by` edges do not render at launch.

Roll-up rendering — an influence edge whose honest target is off-timeline
re-anchored upward through `projects_to` to the bound tradition node,
visibly marked as a projection so the display never claims what the model
does not — is specified here as the intended future view behavior. Building
it is a later ADR-GOV-0009 amendment, not part of this enactment. Substrate
rendering (background bands, not peer bars) is likewise deferred, together
with D5's scope-limit question. The D3 field makes both reachable later
without reopening this ADR.

## D8 — Entity minting under governance warrant

Islam's influence-target entities are minted as community-class entities
under this ADR, warranted by INV-0018's closed record (CLM-0095 through
CLM-0098, FND-0018). No new investigation opens for this. Candidates: the
seventh-century Arabian Jewish communities; Syriac Christianity; Ethiopic
Christianity; Najrānī only if the closed record warrants its distinctness.
Names at honest precision, attestation windows per D4, all values derived
from the record at execution.

An entity the closed record cannot warrant at any honest grade is not
minted; the gap is recorded instead. A smaller honest set is a legitimate
outcome of this ADR, not a failure of it.

## D9 — Edge instantiation

`influenced_by` edges are instantiated from ENT-0015 to each entity minted
under D8, qualifier derived per edge, warrant citing the specific graded
claim(s) and the INV-0018 not-descent determination. No `influenced_by` edge
attaches to a tradition-class target directly; the honest targets are the
community entities. An edge whose target was not minted is not created.

## D10 — Standing determinations affirmed

AF-2 remains negative and deferred (INV-0016 the sole multi-parent case).
Part 3's restorationist observation remains a pressure case only; a
self-account is never encoded as a lineage edge. INV-0018's `branches_from`
refusal stands untouched. AF-3's build is deferred per D7; its principle is
ratified by D2.

# 3. Alternatives Considered

1. **Scope `influenced_by` alone; defer entity resolution** — Rejected. The
   edge is ENT-to-ENT, so its honesty ceiling is the entity layer's
   resolution. Created alone it would sit empty or be forced onto
   wrong-resolution targets, relitigating INV-0018's own finding.

2. **Reuse `bounded_by` as the projection mechanism** — Rejected.
   `bounded_by` (STD-0002 §11, semantics STD-0009 §9) is a field inside a
   confidence component naming the objects that bound that component's
   grade, consumed by the review queue for trigger resolution. It is
   epistemic dependency structure on claims and findings, not an edge
   between entities.

3. **Use `part_of` or `instance_of` for projection** — Rejected on three
   grounds: it substitutes a generic structural relationship where a
   specific one is required (STD-0004 §11); it makes a substantive
   historical assertion, requiring evidential warrant and grading discipline
   to serve a rendering need; and neither reads correctly in the substrate
   direction, guaranteeing a second mint later under D1.

4. **Render community entities as peer bars on the timeline** — Rejected. It
   double-counts lineage mass, asserts a peer-hood the model explicitly
   denies, and forces date precision the evidence does not carry.

5. **Keep finer entities off-timeline permanently, with no projection
   relation** — Rejected. Influence edges would terminate at invisible
   targets whenever influence renders, and a two-class entity system would
   exist with no recorded rule for which class a new entity joins.

6. **Mint substrate nodes now, alongside community nodes** — Rejected. No
   demonstrating case forces substrate instantiation yet, and the D3 field
   makes it reachable later without reopening governance. Deferral costs
   nothing; premature minting would fix a resolution before evidence
   requires one.

# 4. Reasoning

The entity-precision requirement and the edge-restraint rule together
produced INV-0018's central result: an edge was refused because the evidence
did not support descent and no honest target existed. Honouring that result
means changing the entity layer, not the edge discipline. D2 does exactly
that, and does it in both directions at once because AF-3 and AF18-4 are one
problem — a single-resolution entity layer facing multi-resolution evidence.

Separating projection from assertion (D5) follows STD-0004 §9's precision
principle and §11's structural-substitution anti-pattern, and it buys
something further: the renderer's convenience can never silently make a
historical claim, and the view can change later without touching the
evidential graph. That separation is what makes a non-evidential relation
the honest choice rather than a shortcut.

Restraint is preserved where evidence has not spoken. Both new types are
created only because two demonstrating cases exist in each instance —
`influenced_by` per INV-0011 and INV-0018, `projects_to` per AF-3 and
AF18-4 under ADR-GOV-0010 D4's own re-open trigger. Entities are minted only
where the closed record warrants them; substrate and roll-up are deferred
because nothing yet forces their shape. The package decides the principle
and the field once, and lets the build grow into the specification.

Reflexive observations arising during enactment route to the Governance
Backlog per ADR-GOV-0007 §3 and are never self-applied in session.

# 5. Consequences

**Accepted costs:** one new required entity field with a corpus backfill;
one new relationship type in a vocabulary deliberately kept minimal; a
two-class rendering rule the view tooling must enforce with fixtures; a
`projects_to` relation that is load-bearing for a renderer not yet built;
and a known unfinished edge — D5's substrate adequacy is expressly untested.

**Benefits:** the timeline can represent the one relationship INV-0018
established without ever rendering a precision the evidence lacks; the
entity layer stops forcing wrong-resolution targets; projection and
assertion are cleanly separated; and GB-2026-041 closes with both anchor-fit
directions governed under one principle.

**Affected objects:** STD-0002 (amended — `rendering_class`); STD-0004
(amended — `projects_to`, `influenced_by`); ENT-0008 through ENT-0015
(field backfill only); new community entities from ENT-0016; new
`influenced_by` and `projects_to` edges; `validate.py` and
`graph_integrity.py` (extended, with fixtures); view emitter (class filter);
Identifier Registry; Governance Backlog (GB-2026-041 resolved).

# 6. Decision Authority

Vision Steward. This is an Architectural Decision under CON-0003 §5.2 —
it amends two Standards and changes the entity model — and is
Vision-Steward-reserved. Enactment is delegated and mechanical; the enacting
session may not decide anything this ADR leaves silent.

# 7. Review Trigger

This ADR is reopened by any of:

- the substrate rendering build, which must settle D5's untested direction;
- the roll-up renderer build, which amends ADR-GOV-0009's view behavior;
- a case in which `projects_to` proves inadequate for an honest
  community-to-tradition projection;
- a second demonstrating case for AF-2 multi-parent descent, which would
  reopen the D10 deferral;
- any proposal to amend `influenced_by` or the entity-resolution principle,
  which under D1 reopens both together.

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-24|Adopted|Initial decision record. Resolves GB-2026-041: joint-scoping rule, multi-granularity entity layer with `rendering_class`, non-evidential `projects_to`, `influenced_by` created to its INV-0018 specification, community entities minted under governance warrant, tradition-only default render with roll-up and substrate deferred.|

# End ADR-GOV-0012
