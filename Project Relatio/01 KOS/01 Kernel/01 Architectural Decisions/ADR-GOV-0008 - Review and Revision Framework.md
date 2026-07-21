---
title: ADR-GOV-0008 - Review and Revision Framework
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
  - KOS-0011 - Governance, Stewardship & Evolution Framework
  - STD-0008 - Epistemic State Standard
  - ADR-GOV-0007 - Reflexive Architecture Evolution
  - Governance Backlog
tags:
  - ProjectRelatio
  - ADR
  - Review
  - Revision
  - Governance
---
# ADR-GOV-0008

# Review and Revision Framework

## Adopted Architecture Decision Record

> Operationalizes KOS-0011 §12's declared-but-unbuilt review cycles (GR-001/002/ 003): a typed trigger vocabulary, a trigger→scope→act resolution table, bounded review acts, epistemic-strength-tied cadence, and component-level sensitivity structure (`bounded_by`) captured at ingestion. Enacted through a new Review & Revision Standard, KOS-0011 v1.3, and STD-0002 v1.9. Inline pointer: Governance Backlog.

---

# 1. Context

KOS-0011 §12 declares that "Project Relatio requires periodic evaluation" and names three review types — GR-001 Architecture, GR-002 Standards, GR-003 Knowledge ("outdated information, contradictions, unresolved questions") — but provides no trigger, cadence, criteria, mechanism, or queue. STD-0002 §8 reserved `review_date` / `review_cycle` as future-compatible fields, unused. The result: revision happens only when the owner personally notices a need, which does not scale, and closed knowledge ages with no mechanism to resurface it.

The Stage 3 epistemic-field migration (GB-2026-038) made confidence and reliance queryable on all Claim/Finding records — the precondition that makes GR-003 mechanizable for the first time.

---

# 2. Decision

Adopt a review-and-revision framework with the following elements, enacted via a new Review & Revision Standard (operational body), a KOS-0011 §12 amendment (pointing the declared cycles at that standard), and an STD-0002 amendment (activating the review fields and the sensitivity structure).

## D1 — Typed trigger vocabulary

Reviews are surfaced by defined triggers, not personal noticing: `time_decay` (cadence elapsed) · `source_superseded` (a load-bearing source superseded/contradicted — graph event) · `upstream_grade_change` (a bounded-by object re-graded) · `contradiction` (a new finding conflicts with a closed one) · `field_prose_divergence` (structured field disagrees with record prose). Graph-event triggers are IN SCOPE for v1 (owner decision: fuller v1).

## D2 — Trigger → scope → act resolution

Each trigger type resolves to a scope (whole record vs. specific components via `bounded_by`) and a bounded review act:

- `time_decay` → whole record → **light re-affirmation**;
- `source_superseded` / `upstream_grade_change` → affected components only → **targeted re-grade** (mini-circuit on those components);
- `contradiction` → the conflicting claims → **full OPS-0003 circuit**;
- `field_prose_divergence` → the divergent field → **reconciliation act** (align field and prose; no re-research).

## D3 — Review-act bounds (the grade-authority rule)

**Light re-affirmation may NEVER change a grade.** It records only "reviewed, unchanged, clock reset." Any grade change — up or down — requires at least the targeted mini-circuit; contradiction-class changes require the full circuit. The circuit's authority over grades is absolute; the framework makes routine review cheap without diluting it.

## D4 — Cadence tied to epistemic strength

Review cadence is set from a record's epistemic state (its weakest confidence component, modifiable by reliance tier), per the schedule the Review & Revision Standard owns. Weaker knowledge is revisited sooner. Cadence values are maintenance-adjustable within the standard (minor version), not constitutional.

## D5 — Sensitivity structure at ingestion (`bounded_by`)

Confidence components MAY carry a `bounded_by` list naming the objects (sources, claims) that bound that component's grade — capturing at ingestion the dependency structure the prose already states, so graph triggers resolve to components mechanically. OPTIONAL per component; required only where a component's dependencies differ from the record's `derived_from` edges. **No retroactive backfill migration**: existing records are enriched opportunistically when next touched; templates are updated so new records are born review-ready.

## D6 — One queue, reflexive connection

Trigger-surfaced items and reflexive structural recommendations (ADR-GOV-0007) feed the SAME review queue, reviewed by the same (currently human-held, transferable) ratification seat. The queue is produced by tooling that runs the trigger criteria against the vault.

---

# 3. Alternatives Considered

1. **Age-only v1 (defer graph triggers).** Rejected by owner — the graph events the fuller v1 needs (supersession edges, grade-change history on queryable fields) are already recorded by existing machinery; only tooling is required, and the trigger→act table absorbs both trigger classes uniformly.
2. **Full circuit for every review.** Rejected — crushing at scale; D3's bounded acts preserve circuit authority over grades while making routine re-affirmation cheap.
3. **Mandatory `bounded_by` backfill across the 101 records.** Rejected — a second migration tax for enrichment that record-level graph edges already approximate; opportunistic enrichment plus born-ready templates suffices.
4. **Leave review to owner attention.** Rejected — the status quo; does not scale and contradicts KOS-0011 §12's own commitment.

---

# 4. Reasoning

The framework completes an adopted commitment rather than inventing an axis: KOS-0011 declared the review cycles; this decision gives them an operational body. It follows the architecture's established splits — KOS declares, STD operationalizes, STD-0002 carries field format — and its central discipline mirrors the system's oldest rule: mechanism surfaces candidates, recorded governance decides. Knowledge aging is treated as a first-class event class, with the epistemic fields (GB-2026-038) as the query surface that makes detection mechanical.

---

# 5. Consequences

**Benefits:** staleness becomes detectable rather than noticed; triggers resolve to components, so review effort is proportional to actual impact; the reflexive queue and the staleness queue unify; new records are born review-ready. **Costs:** a queue tool must be built and maintained; graph-event triggers will run rarely and must be kept honest by tests; review fields require mechanical initialization on existing records (scripted, no human walk). **Affected objects:** KOS-0011 → v1.3; STD-0002 → v1.9; new Review & Revision Standard; TPL-0001/TPL-0004 updated; a review-queue tool added to tools/.

---

# 6. Decision Authority

Governance-architecture decision reserved to the **Vision Steward** (CON-0003 §5.2). Proposed on the support surface from the KOS-0011 §12 gap analysis; **ratified in full by Brian Noon.**

---

# 7. Review Trigger

Revisit if (a) the trigger vocabulary proves incomplete (a real revision need arises that no trigger names), (b) light re-affirmation is found changing grades in practice (D3 violated — mechanism failure), (c) the queue tool's graph triggers fire incorrectly or fail to fire on a real supersession, or (d) the reflexive-evolution graduation (ADR-GOV-0007 §5) consolidates governance — this framework graduates with it.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-20|Adopted|Initial review-and-revision framework: typed triggers (graph events in scope), trigger→scope→act resolution, grade-authority bound on re-affirmation, epistemic-strength cadence, optional bounded_by sensitivity structure at ingestion (no retroactive migration), unified queue with ADR-GOV-0007. Operationalizes KOS-0011 §12.|

---

# End ADR-GOV-0008