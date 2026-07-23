---
title: ADR-GOV-0011 - Contributor Attribution, AI-Assistance Disclosure, and the Provisional Single-Seat Anchor
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
  - ADR-GOV-0006 - Tiered External-Reliance Model and Live-Retrieval Verification Channel
  - ADR-GOV-0007 - Reflexive Architecture Evolution
  - STD-0002 - Metadata & YAML Standard
  - STD-0006 - Review & Validation Standard
  - Governance Backlog
tags:
  - ProjectRelatio
  - ADR
  - Attribution
  - Contributors
  - Provenance
---

# ADR-GOV-0011

# Contributor Attribution, AI-Assistance Disclosure, and the Provisional Single-Seat Anchor

## Adopted Architecture Decision Record

> Records the current single-seat governance model as a provisional anchor on
> the human layer; requires record-level attribution with AI-assistance
> disclosure on every formal Knowledge Object and backfills the corpus; sets the
> direction for structured review-outcome capture; and installs a tripwire
> forbidding any computed contributor metric absent its own governance decision.
> Per-event attribution is deliberately deferred to a Stage 2 design pass with
> verification events. Inline pointer: Governance Backlog.

---

# 1. Context

Relatio is fully open to read and verify, effectively closed to contribute:
governance has one seat (Vision Steward, CON-0003, held by the owner), the
workflow is brief-mediated, and the conformance bar is largely tacit.
Near-horizon contributors are real and named, with n expected to grow.

Three prerequisites must exist before any contributor track record, lane
structure, or standing computation is possible: (a) honest acknowledgment that
the current governance model is a provisional anchor, (b) attribution captured
as data from now on, and (c) the incentive and independence failure modes named
before any metric can harden around them. This ADR supplies all three. It builds
no contributor infrastructure; it starts the record that later infrastructure
will require.

**Staging.** The originating candidate specified attribution on *every
record-creating or record-altering event*. Schema assessment established that
events are recorded as prose rows in revision-history tables with no structured
actor field, so per-event attribution requires a design pass it does not yet
have. This ADR therefore enacts **record-level attribution (Stage 1)** in a
list-shaped field that per-event attribution extends additively, and defers
**per-event attribution (Stage 2)** to a joint design pass with verification
events (§8). The staging exists so that records created from now on are
attributed rather than accruing as unrecoverable unattributed data.

---

# 2. Decision A — The single-seat model is a provisional anchor

The current governance structure, all ratification authority in the Vision
Steward seat held by the owner, is recorded as a **provisional anchor** under
ADR-GOV-0007 §2 anchor discipline, applied to the human layer rather than the
schema layer.

- It is knowingly biased: placed by the person it empowers.
- It is explicitly expected to be corrected by evidence the system accumulates.
- The seat is a role, not a person (ADR-GOV-0007 §5's transferable ratification
  seat); a human co-contributor slots into the same structure designed for the
  eventual AI-autonomy case.
- **No investigation run under this structure can certify the structure's own
  legitimacy.** Internal findings about seat distribution are candidate criteria
  for the owner to weigh, never validation that the seat should be retained.
  Recorded here so it cannot be forgotten at the moment it matters.

---

# 3. Decision B — Record-level attribution is required, and the corpus is backfilled

Every formal Knowledge Object carries an **`attribution`** field: a **list**,
holding at Stage 1 exactly one entry for the record's creation.

Each entry states **who** (named actor), **in what role**, **when**, **at what
AI-assistance degree**, and **with what model family** (Decision C).

**List-shaped by design.** A single-entry list is used rather than a scalar
block so that Stage 2's per-event attribution is purely additive: further
entries (review, verification, ratification) join the same list without a schema
migration. This follows the `confidence` precedent, where always-a-list made the
split-grade case structural rather than exceptional.

**Retroactive backfill.** The existing corpus is attributed in one lossless
pass. Every current record traces to the owner, executed through the OPS-0003
circuit; the default backfill entry is the owner at degree `ai-delegated` with
model family `Claude`. This makes single-operator provenance **visible in the
record itself** and makes future track-record queries clean from record one.
The backfill is a **best-effort characterization at record level**: known
exceptions (records the owner authored or repaired without AI assistance) are
hand-corrected, and the backfill is recorded as such rather than asserted as
exact.

**Selective visibility (binding).** Attribution is durable but selectively
visible: always recorded, surfaced in the permanent record, and **withholdable
at review time when a review's independence depends on it.** The discrete
`attribution` block exists partly to make that withholding mechanically clean.
Schema and tooling MUST NOT render attribution unconditionally visible in any
surface used for blinded review; doing so would foreclose the review STD-0006
§7.6 requires.

**Honesty note on blinding at small n.** With few contributors in barely
overlapping lanes, withholding the field produces **procedural blindness only**:
a reviewer can often infer authorship from domain and style. Withholding remains
required (it removes the explicit cue and establishes the durable pattern), but
a review at small n MUST NOT be recorded as blinded in the §7.6 sense on the
strength of field-withholding alone. Whether a given review was epistemically
blind is a judgment recorded with the review, not an automatic consequence of
the mechanism.

---

# 4. Decision C — AI-assistance disclosure on every attribution entry

Each attribution entry carries an AI-assistance disclosure with two components:

1. **Degree** (self-disclosed, three levels):
   - `unassisted` — hand work; no AI involvement in the judgments recorded.
   - `ai-assisted` — AI used as a tool; the human's judgment set the conclusions.
   - `ai-delegated` — AI produced the work; the human reviewed and adopted it.
2. **Model family** — vendor/family as a free string (version optional);
   `none` if unassisted. Convention, not enum. **Independence is computed at
   family level: same family is same-kind regardless of version or operator.**
   A Claude-family review of Claude-family work is not independence of kind.

**Rationale (binding on future use).** Correlated AI assistance is the
tooling-layer instance of the correlated-agreement failure. As n grows, many
contributors assisted by the same model family converge for model reasons, not
truth reasons. Therefore all independence assessments — reliance-tier
computation (ADR-GOV-0006), reflexive-gate review eligibility (STD-0006 §7.6),
and any future R2 determination — MUST treat shared model family as a
correlation factor. Same-family-assisted work does not sum toward independence
of kind. (Precedent: INV-0015's consensus-asymmetry rule reports consensus as a
fact about a field while refusing to treat it as truth; this applies the same
discipline internally.)

**Verification backing, tiered.**
- **General records:** self-disclosure suffices. Its integrity rests on the
  permanent-record principle: a false disclosure on an attributed record is an
  outright false statement, not a shrug.
- **Gate-critical events** (any review offered toward lifting the §7.6 reflexive
  gate; any event claimed as R2): self-disclosure alone is insufficient. A
  **method description** is required — how the work was conducted, with what
  materials, through what channel — so thin or misrepresented work leaves
  visible fingerprints. This extends ADR-GOV-0006 §3's edition-discipline
  pattern (mechanically checkable conditions rather than a bare "did you verify"
  judgment) to human process.
- **Encouraged, not mandated:** a sentence of free-text specifics on what was
  and was not delegated ("drafted by model, grades set by hand"), following the
  vault's existing self-disclosed-strength convention. Degree alone cannot
  capture which judgments were the model's.

**Circuit events.** OPS-0003 circuit passes are AI-executed under human
direction. Circuit-produced records attribute to the **ratifying human** at
degree `ai-delegated`, model family recorded. The circuit gets no exemption;
this is what makes Decision B's backfill honest.

---

# 5. Decision D — Structured review-outcome capture (direction set; enactment separate)

When review-outcome capture is enacted, records MUST include, beyond
verdict/flags/remediations:

1. A **stakes/depth descriptor** for the contribution: what it touches, what
   depends on it.
2. Classification of each flag as **substantive** (reasoning, evidence
   representation, warrant) or **conformance** (shape, fields, formatting).

**Rationale.** A track record computed from verdicts alone rewards safe,
polished, low-stakes work — the well-formedness standard's own gameability.
These two fields make that incentive detectable at query time rather than
invisible. Field-level design is enactment detail, not this ADR.

---

# 6. Decision E — Metric tripwire

No computed standing, gating, ranking, or contributor metric may be introduced
by tooling or accreted by practice. Activating computed gating requires its own
governance ADR, which MUST explicitly address, at minimum:

1. The safe-contribution incentive (Decision D's fields as inputs).
2. The overturned-but-well-formed case: a well-formed, honestly disclosed
   contribution later overturned is scored neutral or positive, **never
   negative**. (Precedent: the Zurvanism proposal — overturned, and INV-0016's
   most valuable output.)
3. The distinction between disagreement-with-adjudicator and error: authority
   derived from owner approval cannot produce the independence the reflexive
   gate needs.

Until such an ADR exists, all standing judgments are human, lane-specific, and
owner-ratified. **Any validator, script, or tool found computing contributor
scores absent that ADR is nonconformant by definition.**

---

# 7. Evidence conditions for introducing lanes (named, not designed)

Lanes and roles are introduced from real friction, not pre-designed. Conditions
that would justify a lane-introduction ADR include:

- A contributor repeatedly producing conformant work in a domain such that
  per-item owner review is the bottleneck.
- A class of contribution (tooling changes vs. content claims) demonstrably
  needing different review depth.
- A verification-event record showing sustained independent checking in a
  domain.

None currently obtains. This section exists so the future decision cites
recorded criteria rather than improvising them.

---

# 8. What this ADR deliberately does not do

- **Does not enact per-event attribution (Stage 2).** Deferred to a joint design
  pass with verification events as first-class objects, which are the same shape
  (actor, date, method, independence disclosure). **Re-open trigger:** taking up
  the verification-events build, or a demonstrated need to distinguish per-event
  actors before then.
- Does not build verification events (the R2 unlock).
- Does not define lanes, roles, or permissions.
- Does not create any metric.
- Does not modify the reflexive gate, which remains unlifted; all anchors remain
  provisional.

---

# 9. Alternatives Considered

1. **Hold the whole decision until per-event attribution is designed.**
   Rejected — every record created in the interim would be unattributed data
   that cannot be recovered later. Stage 1 stops that immediately, and the
   list-shaped field makes Stage 2 additive rather than a migration.
2. **Record-level attribution as a scalar block.** Rejected — per-event
   attribution is known to be coming; a scalar would force a migration. The
   `confidence` precedent (always-a-list) applies directly.
3. **Attribution recorded in revision-history prose.** Rejected — unparseable
   for track-record queries, and impossible to excise cleanly for blinded
   review (Decision B's selective-visibility constraint).
4. **Defer AI-assistance disclosure until contributors exist.** Rejected — the
   backfill is the moment the corpus's own AI provenance becomes visible, and
   the disclosure vocabulary must exist before any independence assessment is
   attempted.

---

# 10. Consequences

**Benefits:** provenance becomes visible and queryable from record one; the
single-operator reality is stated in data rather than assumed; independence
assessment gains the model-family factor it needs; the metric tripwire prevents
scoring from accreting by accident.
**Costs:** STD-0002 gains a required field on every formal object; a
full-corpus backfill pass; validator presence-checking at error level; the
backfill is best-effort at record level with hand-corrected exceptions.
**Deferred:** per-event attribution; verification events; lanes; metrics.
**Unchanged:** the reflexive gate; all provisional anchors; the Architecture
Baseline.

---

# 11. Decision Authority

Governance-architecture decision reserved to the **Vision Steward** (CON-0003
§5.2). Originating candidate produced on the contributor-participation design
surface; schema staging assessed on the owning surface. **Ratified in full by
Brian Noon.**

---

# 12. Review Trigger

Revisit if (a) the Stage 2 per-event design proves the list shape wrong;
(b) a contributor's work cannot be honestly characterized by the three
assistance degrees; (c) blinded review reveals that field-withholding is
insufficient in practice; or (d) computed gating is taken up, which requires its
own ADR under Decision E.

---

# 13. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-22|Adopted|Records the single-seat governance model as a provisional anchor on the human layer; requires record-level `attribution` (list-shaped, one entry at Stage 1) with AI-assistance degree and model-family disclosure on every formal Knowledge Object; backfills the corpus as best-effort with hand-corrected exceptions; binds independence assessment to family-level model matching; sets direction for structured review-outcome capture; installs the metric tripwire. Per-event attribution deferred to Stage 2 with verification events.|

---

# End ADR-GOV-0011
