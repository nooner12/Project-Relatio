---
title: ADR-GOV-0010 - Continuation Qualifier and the First Reflexive Anchor Revision
document_type: Architecture Decision Record
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-22
decision_status: Accepted
decision_date: 2026-07-22
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - ADR-GOV-0007 - Reflexive Architecture Evolution
  - ADR-GOV-0009 - World-Religions Timeline Program and Lineage Anchors
  - STD-0004 - Relationship & Linking Standard
  - STD-0006 - Review & Validation Standard
  - Governance Backlog
tags:
  - ProjectRelatio
  - ADR
  - ReflexiveEvolution
  - Lineage
  - AnchorRevision
---

# ADR-GOV-0010

# Continuation Qualifier and the First Reflexive Anchor Revision

## Adopted Architecture Decision Record

> Adjudicates the anchor-vocabulary review due before family 3 (ADR-GOV-0009
> §7(a)). Adds a `continuation` qualifier to the provisional `branches_from`
> vocabulary in response to INV-0017's demonstrated inability to name a
> main-line-continuation edge (Rabbinic Judaism); re-qualifies that edge;
> adds a disambiguation note for the `reform` collision; and DEFERS the
> Iranian-family cardinality/target/type recommendations under the
> defer-to-second-use principle. This is the first structural change to
> Project Relatio driven by the system's own investigative findings — the
> ADR-GOV-0007 reflexive loop completing its first full turn. Inline pointer:
> Governance Backlog (GB-2026-041).

---

# 1. Context

The world-religions timeline program (ADR-GOV-0009) laid provisional anchors —
the `branches_from` edge, its five-qualifier list, the `tradition_type`
vocabulary, and the §2.3 distinctness threshold — under ADR-GOV-0007 §2 anchor
discipline, with the first two family investigations named as the pressure
test (§7(a)) and their findings routed as recommendations to GB-2026-041.

Both families have now run. INV-0016 (Iranian) found the five-qualifier list
fit every edge it drew, and surfaced strains in edge *cardinality* (Manichaeism's
multi-parent descent), edge *target* (Yazidism's broader-than-Zoroastrianism
antecedent), and `tradition_type` co-application. INV-0017 (Judaism–Christianity)
produced the first case the qualifier list **could not name**: Rabbinic Judaism
is Second Temple Judaism's least-departed main line carried forward after 70 CE,
but every listed qualifier connotes departure. `reform` was applied
least-wrong-under-protest, with the warrant claim's `reform_qualifier_fit`
component graded **Low to encode vocabulary strain — not doubt about the descent,
which is Moderate.**

This ADR is the anchor-vocabulary review ADR-GOV-0009 §7(a) requires before
family 3.

---

# 2. Decision

## D1 — Add a `continuation` qualifier to `branches_from`

Add `continuation` to the controlled qualifier list in STD-0004 (the
`branches_from` entry, §7.2, and the `graph_integrity.py` enforced set):

> `continuation` — B `branches_from` A where B carries forward A's principal
> or main line rather than departing from it: the least-departed descendant
> after a rupture or transformation. Distinguished from `reform`
> (reconstitution-with-change) by the absence of a departure connotation.

The list becomes: `schism` / `reform` / `syncretic-descent` /
`heterodox-offshoot` / `disputed` / `continuation`.

## D2 — Re-qualify the Rabbinic Judaism edge

ENT-0014's `branches_from` edge to ENT-0012 changes qualifier `reform` →
`continuation`. CLM-0094's `reform_qualifier_fit` component is re-graded to its
honest fit under the correct word by the reviewer (the Low grade encoded only
"wrong word," never descent doubt, so the fit rises with the right qualifier).
ENT-0014's `tradition_type` question (`reform` vs. `emergent`) is a SEPARATE
field and is left as recorded; only the lineage qualifier changes.

## D3 — Disambiguation note for the `reform` collision

STD-0004 §7.2 gains a note that the `branches_from` qualifier `reform` and the
STD-0002 `tradition_type` value `reform` are different vocabularies on different
fields that coincidentally share a word; they are never conflated. (ENT-0014
already carries this note locally; this lifts it to the standard.)

## D4 — Defer the Iranian-family recommendations (defer-to-second-use)

AF-2 (multi-parent edges), AF-3 (broader-than-named edge target / an explicit
"ancient Iranian religion" root), and AF-4 (multi-value `tradition_type`) are
each **single-instance strains from one family**. Per the merit principle
established in GB-2026-026/027 (n=1 is a candidate, not a demonstrated need;
a second independent case grounds the generalization and prevents locking the
wrong shape), they are **logged as deferred candidates in GB-2026-041**, NOT
enacted. Re-open trigger: a second family investigation exhibiting the same
strain. Acting now would be the over-architecture the Baseline discipline
guards against.

## D5 — The reflexive gate is NOT lifted; the anchors stay provisional

Adding `continuation` responds to a **demonstrated failure to name an edge** —
a gap visible on its face (the investigation could not name the edge; no
independent opinion is needed to see that `reform` did not fit). This is
additive repair of a demonstrated gap, which does **not** require blinded
independent review. It is expressly **NOT** a promotion of the qualifier list,
`branches_from`, the §2.3 threshold, or `tradition_type` from provisional toward
durable. Both family circuits were same-underlying-model (procedural
independence only, STD-0006 §7.6); the *vindicating* findings (AF-1, the
list-fit result, the threshold holding) remain gated and may not be cited to
graduate any anchor until blinded independent review. The qualifier list stays
provisional — it simply has one more tool in it.

---

# 3. Alternatives Considered

1. **Do nothing; keep `reform` under protest.** Rejected — INV-0017 demonstrated
   a real inability to name the edge, and left a Low fit-grade specifically
   flagging the gap for this review. Leaving a known-wrong qualifier in place
   would be ignoring the reflexive finding the loop was built to act on.
2. **Enact all eight recommendations (AF-1…4, AF17-1…4) now.** Rejected —
   most are single-instance strains or gated vindications; enacting them would
   lock shapes on n=1 evidence (over-architecture) and would misread the
   reflexive gate as lifted.
3. **Treat this as promoting the anchors to durable (gate-lift).** Rejected —
   the gate lifts only on blinded independent review, still outstanding. D5
   states the non-promotion explicitly.
4. **Record via STD-0004 amendment only, no ADR.** Rejected — this is the first
   structural change driven by the system's own findings; the reflexive loop's
   first completed turn warrants a decision record, distinct from the mechanical
   amendment that carries it.

---

# 4. Reasoning

The reflexive loop (ADR-GOV-0007: findings inform → owner governs → structure
changes, never self-executing) has completed its first full turn on a genuine
gap. The discipline that makes it trustworthy is the same one that constrains
it: additive repair of a demonstrated failure is warranted, while promotion of
the design to durable on the strength of self-generated praise is withheld
pending independent review. Adding `continuation` because an edge could not be
named is the former; it is not the latter. Deferring the one-off strains honors
the evidence-before-formalization principle the project has applied twice before
(GB-2026-026/027).

---

# 5. Consequences

**Benefits:** the qualifier vocabulary can now honestly name main-line
continuation, the most common descent relationship among living traditions;
the Rabbinic Judaism edge is correctly qualified; family 3 inherits a vocabulary
that survived its first demonstrated failure.
**Costs:** STD-0004 → next version; `graph_integrity.py` enforced set updated;
ENT-0014 + CLM-0094 re-qualified/re-graded; the timeline connector legend gains
a `continuation` style.
**Deferred (not lost):** AF-2/3/4 remain live candidates in GB-2026-041 awaiting
a second demonstrating case.
**Unchanged:** the reflexive gate; the provisional status of all anchors; the
§2.3 threshold; `tradition_type`; the Architecture Baseline.

---

# 6. Decision Authority

Structural/vocabulary decision on a provisional anchor, reserved to the
**Vision Steward** (CON-0003 §5.2). The anchor-vocabulary review named in
ADR-GOV-0009 §7(a). **Ratified in full by Brian Noon.**

---

# 7. Review Trigger

Revisit if (a) a later family finds `continuation` itself ill-fitting or in need
of sub-distinction; (b) a second case triggers any of the deferred AF-2/3/4
items; (c) blinded independent review becomes available and the question of
graduating the anchors from provisional to durable is taken up (a separate
decision this ADR explicitly does not make); or (d) the `reform` collision proves
to need more than a disambiguation note.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-22|Adopted|Anchor-vocabulary review (ADR-GOV-0009 §7(a)): added the `continuation` qualifier to provisional `branches_from` in response to INV-0017's demonstrated main-line-continuation gap (Rabbinic Judaism); re-qualified that edge reform→continuation; lifted the reform-collision disambiguation note to STD-0004; deferred the Iranian-family cardinality/target/type recommendations (AF-2/3/4) under defer-to-second-use; explicitly did NOT lift the reflexive gate or promote any anchor from provisional to durable. First structural change driven by the system's own findings — the ADR-GOV-0007 reflexive loop's first completed turn.|

---

# End ADR-GOV-0010
