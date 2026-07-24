---
title: STD-0002 - Metadata & YAML Standard
document_type: Standards Document
version: 1.13
status: Adopted
operational_status: Active
category:
  - Knowledge Operating System
  - Standards
  - Metadata Architecture
created: 2026-07-09
parent_documents:
  - KOS-0009 Knowledge Representation & Information Architecture Framework
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - STD-0001 Naming & Identification Standard
  - STD-0003 Tagging Standard
  - STD-0004 Linking & Relationship Standard
  - STD-0008 Epistemic State Standard
  - TPL-0001 Formal Document Template
tags:
  - ProjectRelatio
  - Standards
  - Metadata
  - YAML
  - InformationArchitecture
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# STD-0002

# Project Relatio Metadata & YAML Standard

## Version 1.13
## Adopted Standards Document

---

# 1. Purpose

The Metadata & YAML Standard defines the rules for describing Project Relatio knowledge objects.

Metadata provides structured information about documents, allowing the system to:

- identify documents,
- classify documents,
- establish relationships,
- track lifecycle,
- support future automation.

---

# 2. Standard Principle

Project Relatio adopts:

> Every knowledge object should describe what it is, where it belongs, how it relates, and how it changes over time.

---

# 3. Metadata Architecture

Every formal document consists of two layers:

```
Human Layer

↓

Document Content

↓

Metadata Layer

↓

Machine Interpretation
```

---

# 4. YAML Frontmatter Requirement

All formal Project Relatio documents require YAML frontmatter.

Structure:

```
---
metadata:
---
```

The YAML block must appear at the beginning of the document.

---

# 5. Required Metadata Fields

All formal documents require:

```
---
title:
document_type:
version:
status:
operational_status:
created:
category:
tags:
attribution:
---
```

*(v1.12 note: `attribution` — provenance, with AI-assistance disclosure — is required on every formal Knowledge Object per ADR-GOV-0011 Decision B. Definition and rules in §6; the binding provenance/independence/visibility rules in §6.1.)*

---

# 6. Field Definitions

---

# title

Purpose:

Defines the official document name.

Format:

```
title: STD-0002 - Metadata & YAML Standard
```

Rules:

- must match filename,
- must preserve identifier,
- must remain stable.

---

# document_type

Purpose:

Defines the classification of the document.

Approved values:

```
Kernel Operating System Document

Standards Document

Constitutional Instrument

Navigation Document

Architecture Document

Governance Record

Architecture Decision Record

Role Definition

Template

Operations Document

Source Record

Entity Record

Claim Record

Investigation Record

Finding Record

Review Report
```

**Content types** ("Kernel Operating System Document," "Standards Document," "Constitutional Instrument") name a document's substantive class and are layer-specific by nature. **Meta-document types** ("Navigation Document," "Architecture Document," "Governance Record," "Review Report") are deliberately **layer-agnostic** — the same type is reused across the Kernel, Standards, and future layers (e.g. both `Kernel Index` and `Standards Index` are Navigation Documents). This avoids a proliferation of near-duplicate, layer-prefixed types.

Notes:
- "Kernel Operating System Document" and "Constitutional Instrument" were added in v1.1 to match consistent, already-established vault usage.
- "Review Report" was added in v1.2 for the outputs of reviews and audits conducted under STD-0006 (e.g. the Standards Architecture Retrospective).
- v1.3 consolidated the meta-document types: the layer-prefixed values previously in use ("Standards Navigation Document," "Kernel Navigation Document," "Kernel Architecture Document/Manifest," "Kernel Governance Document") were replaced by the three layer-agnostic values above.
- v1.4 added the Knowledge Base content types "Investigation Record" and "Finding Record," defined by KOS-0012 (Knowledge Object Model).
- Draft-era values used only by not-yet-adopted documents ("Foundational Framework," "Operational Framework") remain unapproved pending the Standards Architecture Retrospective.

---

# version

Purpose:

Tracks document maturity.

Format:

```
version: 1.0
```

Uses:

Major.Minor

---

# status

Purpose:

Records a Knowledge Object's **maturity** — its development stage. Lifecycle is governed by STD-0005, which is authoritative.

> **Reconciliation note (v1.5):** STD-0005 defines a **two-dimensional** lifecycle: Maturity (Proposed → Draft → Reviewed → Adopted) and Operational (Active → Superseded → Archived), which are independent. As of v1.5 these are carried in **two fields**: `status` holds **maturity**; `operational_status` (below) holds the operational state. The migration adding `operational_status` across the vault (GB-2026-006) was executed 2026-07-11 — the deferral's trigger (a real supersession/archival event) having occurred. Earlier single-field usage where `status` held an operational value (`Active`/`Archived`/`Superseded`) was migrated: the operational value moved to `operational_status` and `status` was set to the object's maturity.

Approved values (maturity):

```
Proposed

Draft

Reviewed

Adopted
```

(Legacy `Review` reads as `Reviewed`.)

---

# operational_status

Purpose:

Records a Knowledge Object's **operational** state — its current role, independent of maturity (STD-0005 §10–13).

Approved values (operational):

```
Active

Superseded

Archived
```

Rules:

- Required on every formal Knowledge Object alongside `status` (v1.5).
- `Active` — currently in force / in use (this includes Draft-maturity research objects that are in active use; operational state is not gated on adoption in practice, and the vault applies `Superseded`/`Archived` to non-adopted objects — e.g. KOS-0200 — so `operational_status` is carried by all governed objects).
- `Superseded` — replaced by another object; pair with a `superseded_by` relationship (STD-0005 §12).
- `Archived` — retained for reference, no longer operational.

---

# created

Purpose:

Records initial creation date.

Format:

```
created: YYYY-MM-DD
```

Example:

```
created: 2026-07-09
```

---

# updated

Purpose:

Records the most recent modification date.

Recommended:

```
updated: YYYY-MM-DD
```

---

# category

Purpose:

Defines conceptual placement.

Format:

```
category:
  - Knowledge Operating System
  - Standards
```

Rules:

- use controlled terminology,
- avoid unnecessary categories.

---

# tags

Purpose:

Supports discovery and grouping.

Format:

```
tags:
  - ProjectRelatio
  - Standards
```

Rules:

- PascalCase,
- meaningful concepts,
- no filler tags.

---

# attribution

Purpose:

Records **provenance** — who brought the record into being, in what role, when, and at what degree of AI assistance. Required on every formal Knowledge Object (v1.12, enacting **ADR-GOV-0011** Decision B and Decision C).

Format:

```
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-22
    ai_degree: ai-delegated
    ai_model_family: Claude
```

**Field rules:**

- **`attribution` is ALWAYS A LIST**, minimum one entry. **Never a scalar block.** At **Stage 1** (the current stage) it holds **exactly one entry**, whose `event` is `created`.
- Each entry requires all six keys: `actor`, `role`, `event`, `date`, `ai_degree`, `ai_model_family`.
- `actor` — the **named human**. Free string. An AI system is never the actor; it is disclosed through `ai_degree` / `ai_model_family` (ADR-GOV-0011 §4, *Circuit events*: circuit-produced records attribute to the **ratifying human** at degree `ai-delegated`).
- `role` — free string. Use a **ROLE-#### identifier** where one applies (e.g. `ROLE-0002 Research Specialist`). **There is no controlled enum**, because lanes and roles for contributors do not yet exist (ADR-GOV-0011 §7); introducing one would pre-design the structure that ADR reserves for real friction.
- `event` — at Stage 1 the **only** value is `created`. The key nonetheless exists now so that Stage 2's per-event values (`reviewed`, `verified`, `ratified`, …) join **additively**, without a shape change.
- `date` — `YYYY-MM-DD` (§10).
- `ai_degree` — **controlled vocabulary**, exactly one of:
  - `unassisted` — hand work; no AI involvement in the judgments recorded.
  - `ai-assisted` — AI used as a tool; the human's judgment set the conclusions.
  - `ai-delegated` — AI produced the work; the human reviewed and adopted it.
- `ai_model_family` — the vendor/family as a **free string** (version optional, e.g. `Claude` or `Claude Opus 4.8`), or the literal `none` when `ai_degree: unassisted`. **Convention, not enum** — the vocabulary of model families is not the vault's to fix. The validator enforces only the pairing: `ai_model_family: none` **if and only if** `ai_degree: unassisted`.
- **Encouraged, not required** (ADR-GOV-0011 §4): a sentence of free-text specifics on what was and was not delegated ("drafted by model, grades set by hand"), recorded in the record's prose. Degree alone cannot capture *which* judgments were the model's.

**Why a list and not a scalar.** Stage 2 (per-event attribution) is known to be coming and is deferred only for design (ADR-GOV-0011 §8). A scalar would force a migration; a single-entry list makes Stage 2 purely additive. This follows the `confidence` precedent (§11), where always-a-list made the split-grade case structural rather than exceptional.

---

## 6.1 Attribution Is Provenance — Three Fields That Must Not Be Conflated

`attribution` is **provenance**: the record of **who made this record, and how**. Two neighbouring fields answer different questions and are **not** substitutes for it:

| Field | Answers | Domain |
|---|---|---|
| **`attribution`** (§6, required) | **Who produced *this record*, in what role, when, at what AI-assistance degree** | **Provenance** |
| `owner` (§8, optional/reserved) | Who is *responsible for maintaining* this record going forward | **Stewardship** |
| `source_author` (§11, Source Records) | Who wrote **the external source** the record describes | **The source's authorship** |

- **`attribution` ≠ `owner`.** Stewardship can transfer; provenance cannot. A record whose steward changes still has the same creation provenance, and populating one never populates the other.
- **`attribution` ≠ `source_author`.** On a Source Record these two are *both* present and mean opposite things: `source_author` is the author of the work being catalogued (an external human, often centuries dead); `attribution` is the vault contributor who created the catalogue record. Conflating them would credit a source's author with a vault record they never saw.

**Independence is assessed at FAMILY level (binding — ADR-GOV-0011 Decision C).** Same model family is **same-kind regardless of version or operator**: a Claude-family review of Claude-family work is **not** independence of kind. Therefore **same-family-assisted work does not sum toward independence**, and every independence assessment — reliance-tier computation (ADR-GOV-0006), reflexive-gate review eligibility (STD-0006 §7.6), and any future R2 determination — MUST treat a shared `ai_model_family` as a **correlation factor**. Correlated AI assistance is the tooling-layer instance of the correlated-agreement failure: many contributors assisted by one model family converge for model reasons, not truth reasons.

**Selective visibility (binding — ADR-GOV-0011 Decision B).** Attribution is **durable but selectively visible**. It is always recorded and always present in the permanent record, and it MUST be **withholdable at review time when a review's independence depends on it**. No tool or surface used for blinded review may render it unconditionally. The discrete `attribution` block exists partly to make that excision **mechanically clean** — which is why provenance is a structured field and not revision-history prose.

> **Honesty limit on blinding at small n** (ADR-GOV-0011 Decision B). With few contributors in barely overlapping lanes, withholding the field produces **procedural blindness only** — a reviewer can often infer authorship from domain and style. Withholding remains required, but a review MUST NOT be recorded as blinded in the STD-0006 §7.6 sense on the strength of field-withholding alone. Whether a review was *epistemically* blind is a judgment recorded with the review.

**Backfill honesty (v1.12).** The 2026-07-22 corpus backfill applied the default entry (owner / Vision Steward / `ai-delegated` / `Claude`, dated from each record's own `created` field) to every pre-existing object. It is a **best-effort characterization at record level**, not an exact per-judgment claim; owner-reserved records that may warrant `unassisted` or `ai-assisted` were reported as a candidate exception list for hand-correction rather than guessed at.

**No metric may be computed from this field** (ADR-GOV-0011 Decision E). Attribution exists to make provenance visible and queryable. Any computed contributor standing, ranking, or gating requires its own governance ADR; **any validator, script, or tool found computing contributor scores absent that ADR is nonconformant by definition.**

---

# 7. Relationship Metadata

Documents may contain:

```
parent_documents:

related_documents:
```

---

## parent_documents

Purpose:

Identifies governing or originating documents.

Example:

```
parent_documents:
  - KOS-0009 Knowledge Representation Framework
```

---

## related_documents

Purpose:

Identifies connected documents.

Example:

```
related_documents:
  - STD-0001 Naming & Identification Standard
```

---

## relationships (typed — v1.6)

Purpose:

Carries **typed** relationships in the frontmatter, so tooling can read a relationship's *meaning*, not merely its existence. This closes the standing gap recorded as Pressure Test **F-4** / **GB-2026-001**: STD-0004 defines a relationship vocabulary that the flat `parent_documents`/`related_documents` lists could not express.

Optional block. Each entry pairs a **type** (drawn from the STD-0004 approved vocabulary) with a **target** (an identifier):

```
relationships:
  - type: derived_from
    target: SRC-0006
  - type: supports
    target: FND-0004
  - type: contrasts_with
    target: CLM-0002
```

Rules:

- `type` must be an approved STD-0004 relationship type (`defines`, `implements`, `extends`, `depends_on`, `derived_from`, `supports`, `contrasts_with`, `supersedes`, `part_of`, `instance_of`, `explains`, `related_to`). Prefer the most specific type (STD-0004 §9).
- `target` is the **identifier** of an existing object (e.g. `SRC-0006`). The Identifier Registry / object title resolves it to a name.
- The block **enriches**, it does not replace, `parent_documents`/`related_documents` (which remain the flat, tooling-read lists and STD-0002-required structure). `graph_integrity.py` reads both: the flat lists for dangling-reference checks, `relationships` for **type-aware** reciprocity.
- Directionality follows STD-0004 §8 — the entry reads *this object* `type` *target*.
- Adopted for **Knowledge Base objects** (INV/CLM/SRC/ENT/FND), where research edges carry semantic weight; other layers may use it where a relationship's type matters.

---

# 8. Optional Governance Metadata

Future-compatible fields:

```
owner:

revision_history:
```

*(v1.9 note: `review_date` and `review_cycle` were reserved here from v1.0; they are now **active, document-class-specific fields** on Claim Records and Finding Records — see §11 — per ADR-GOV-0008 and the Review & Revision Standard (STD-0009).)*

*(v1.12 note: `owner` records **stewardship** — who maintains the record going forward. It is **not** provenance and is **not** satisfied by, nor does it satisfy, the required `attribution` field (§6). Stewardship transfers; provenance does not. See §6.1.)*

---

# 9. Field Naming Convention

All YAML fields use:

```
lowercase_with_underscores
```

Correct:

```
parent_documents:
```

Incorrect:

```
Parent Documents:
```

Correct:

```
document_type:
```

Incorrect:

```
DocumentType:
```

---

# 10. Date Standard

All dates use:

```
YYYY-MM-DD
```

Example:

```
created: 2026-07-09
```

---

# 11. Document-Specific Metadata

Some document classes require additional fields.

---

## Source Records

May include:

```
source_author:

source_url:

publication_date:
```

*(v1.12 note: `source_author` is the author of **the external source being catalogued** — not the vault contributor who created the Source Record. That contributor is recorded in the required `attribution` field (§6). Both are present on a Source Record and mean opposite things; see §6.1.)*

---

## Architecture Decision Records

May include:

```
decision_status:

decision_date:
```

---

## Templates

May include:

```
template_type:
```

---

## Claim Records and Finding Records

Require the epistemic-axis fields (values and rules per the Epistemic State Standard, STD-0008):

```
confidence:
  - component: overall
    level: 3
    label: Moderate
reliance_tier: R0
```

Split-grade example (a claim whose components differ — never averaged):

```
confidence:
  - component: placement
    level: 3
    label: Moderate
  - component: criteria_mechanics
    level: 2
    label: Low
reliance_tier: R0
```

**Field rules (format; semantics in STD-0008):**

- `confidence` is **always a list**, minimum one component. A single-grade claim uses one item with `component: overall`. Never a scalar.
- Each component requires `component` (short lowercase_with_underscores name), `level` (integer 1–5), and `label` (the matching Level-N label per STD-0008 §5.1).
- `reliance_tier` is a single value: `R0`, `R1`, or `R2`.
- Both fields are **required on Claim Records and Finding Records**; other object classes do not carry them.
- These are content fields (like Source Records' `source_author`), not lifecycle fields — they sit alongside, and are independent of, `status` and `operational_status`.

**Review fields (v1.9; semantics owned by the Review & Revision Standard, STD-0009 §8):**

```
review_cycle: 9        # months, per the Review & Revision Standard §7 cadence
review_date: 2027-04-20    # next review due
last_reviewed: 2026-07-20  # most recent review act (or initialization)
```

- All three are **required on Claim Records and Finding Records**.
- Dates use YYYY-MM-DD (§10); `review_cycle` is a positive integer (months).
- Semantics — what sets the cycle, what a review act may do, when the dates advance — are owned by STD-0009 §8; this standard owns only format and placement.
- Initialization of existing records is **mechanical** (scripted from each record's weakest confidence component per the STD-0009 §7 cadence schedule; `last_reviewed` = the record's epistemic-backfill date).

**Optional `bounded_by` inside confidence components (v1.9; semantics in STD-0009 §9):**

```
confidence:
  - component: criteria_mechanics
    level: 2
    label: Low
    bounded_by: [SRC-0129]
```

- `bounded_by` is **OPTIONAL** per component; entries are identifiers of **existing** objects and are **graph claims** (§12.1 applies — dangling `bounded_by` entries fail integrity).
- Required only where a component's dependencies differ from the record's `derived_from` edges.
- **No retroactive backfill** (ADR-GOV-0008 D5); graph tooling reads `bounded_by` for trigger resolution.

---

## Entity Records — the `rendering_class` field (v1.13 — ADR-GOV-0012 D2/D3)

The entity layer is **multi-granularity**: entities may coexist at several resolutions, and every entity that participates in the world-religions timeline program declares which resolution it occupies.

```
rendering_class: tradition     # tradition | substrate | community
```

**The controlled vocabulary (ADR-GOV-0012 D2):**

- `tradition` — the original resolution; a lineage actor on the timeline.
- `substrate` — coarser context within which traditions arise; temporally native but **not** a lineage actor.
- `community` — finer, regionally or temporally bounded populations or expressions; edge-capable but temporally soft.

**Field rules:**

- **REQUIRED AT MINT** on every entity carrying a class field set — i.e. any entity carrying any tradition-class field (`tradition_type` / `dating_claims` / `display_range`) or any community-class field (`attestation_claims` / `attestation_window` / `attestation_uncertainty`).
- **ABSENT on concept entities.** The seven concept entities (ENT-0001…ENT-0007) are outside the timeline program, carry no class field set, and carry no `rendering_class`. They are untouched.
- `rendering_class: tradition` requires the tradition-class field set below; `rendering_class: community` requires the community-class field set below, and **forbids** both the tradition-class fields and the render-only positioning bounds (a community entity never carries a founding-date-style bar — D4).
- `rendering_class: substrate` is **established as a class but has no field set yet.** Substrate rendering — and with it the question of how a substrate entity is dated and bound — is deferred by ADR-GOV-0012 D7; no substrate entity is minted. The value exists so the class is reachable later without reopening governance.
- **Class membership is a modeling judgment recorded at mint** and warranted like any other field (ADR-GOV-0012 D2). It is not derivable from the record's other fields and is never inferred by tooling.
- Existing entities ENT-0008…ENT-0015 were backfilled as `tradition` (ADR-GOV-0012 D3): field addition and a history row only, no other content changed. Enforcement followed the migration discipline — **define, backfill, then enforce**.

---

## Entity Records (tradition class)

Entity Records representing **religious traditions** carry `rendering_class: tradition` (above) plus three additional fields (per ADR-GOV-0009 D3):

```
tradition_type: founded        # founded | emergent | reform | syncretic
dating_claims:                 # pointers to the graded claim(s) dating the tradition
  - CLM-00XX
display_range: "3rd c. CE"     # render-only string; the claims are the truth
```

**Field rules:**

- These fields are **REQUIRED on tradition-class entities** and **ABSENT on concept entities** (the existing seven concept entities — ENT-0001…ENT-0007 — are untouched). Presence of any one of the three requires all three (the validator enforces this at error level).
- `tradition_type` takes one value from the controlled vocabulary `founded` / `emergent` / `reform` / `syncretic`, so the schema never demands a founding date from a tradition that has none (the "Hinduism-class" category error is excluded structurally).
- `dating_claims` entries are **graph claims** (§12.1 — must resolve to existing objects; dangling entries fail integrity).
- `display_range` is **presentation only** and carries **no evidential weight** — a tradition's contestedness lives in the confidence of its dating claims, not in this string.
- **No `origin_date` (or any other temporal) field exists on entities, by decision** (ADR-GOV-0009, Alternatives §2): dates are claims, not entity fields. `display_range` is the sole render string.

### Render-only positioning bounds (v1.11 — OPTIONAL)

A tradition-class entity **may** additionally carry three optional fields whose sole purpose is to let a renderer position the tradition on a proportional time axis (the SVG timeline view). They are **not** part of the evidential record:

```
range_start_year: -1500        # integer; negative = BCE, positive = CE; the earliest DEFENSIBLE bound
range_end_year: -1000          # integer (same convention), OR the literal token: present
range_uncertainty: high        # low | moderate | high
```

**Field rules:**

- **RENDER-ONLY, APPROXIMATE, NON-EVIDENTIAL.** These are positioning hints for a proportional axis, nothing more. They carry **no evidential weight** and must **never** be read as a claim, cited, or treated as authoritative. **`display_range` remains the authoritative human label**; where the two ever appear to disagree, `display_range` and the dating claim behind it win.
- **DERIVED FROM AND BOUNDED BY the entity's `dating_claim`(s).** They are the earliest / latest **defensible** bounds the dating claim supports, **never a false point**, and they **inherit that claim's confidence** — a bar drawn from them must never render as *more certain* than the dating claim warrants. `range_start_year` is the earliest defensible emergence bound; `range_end_year` is the latest defensible bound, or `present` for a living tradition.
- **OPTIONAL.** A tradition that omits them is not malformed — it renders by a documented fallback (an "undated / sequence-only" lane showing its verbatim `display_range`, never invented coordinates). When **any** of the three is present, **`range_start_year` and `range_uncertainty` are co-required**; `range_end_year` is optional (absent = terminus not dated by the claim; `present` = living tradition).
- **`range_uncertainty` is reproducible, not ad hoc.** It maps from the confidence of the dating claim's **emergence/crystallisation-dating component** — the component that grades *when* the tradition emerged (where more than one dating-bearing component exists, the weakest of them). Non-temporal components (descent, classification, qualifier) grade the lineage, not the position in time, and do **not** govern this field. The mapping:

  | dating-component confidence (KOS-0003 §8) | `range_uncertainty` |
  |---|---|
  | High / Very High | `low` |
  | Moderate | `moderate` |
  | Low / Very Low | `high` |

  A renderer encodes `range_uncertainty` **into the geometry** — `high` renders as a visibly dashed / faded bar so that low confidence *looks* weak. This preserves, in the picture, the contestedness the architecture refuses to erase.
- The validator shape-checks these at **error** level: `range_start_year` an integer; `range_end_year` an integer or the literal `present`; `range_uncertainty` one of `low`/`moderate`/`high`; and the start+uncertainty co-presence rule. Whether a bound is *correctly derived* from the claim is a review question, not a shape question.

---

## Entity Records (community class) — attestation windows (v1.13 — ADR-GOV-0012 D4)

Entity Records representing a **regionally or temporally bounded population or expression** — the resolution below the tradition-whole — carry `rendering_class: community` plus three additional fields:

```
attestation_claims:                       # graph-claim pointers to the graded record(s) attesting this community
  - CLM-00XX
attestation_window: "7th c. CE — the period of documented contact"   # render-only string; a WINDOW, never a founding date
attestation_uncertainty: moderate         # low | moderate | high
```

**Field rules:**

- These three are **REQUIRED on community-class entities** and **ABSENT on every other class** (the validator enforces co-presence at error level, as it does the tradition trio).
- **A COMMUNITY ENTITY CARRIES AN ATTESTATION WINDOW, NOT A FOUNDING DATE (ADR-GOV-0012 D4).** The window states *when the warranting record attests this community*, not when it began or ended. A community entity is **never** assigned a founding-date-style range and its window is **never rendered as one** — which is why the tradition-class fields and the render-only positioning bounds (`range_start_year` / `range_end_year` / `range_uncertainty`) are **forbidden** here. There is no numeric geometry for a community entity, because there is no honest point to draw.
- **Bounds are derived from the warranting record(s) and never precisified beyond them.** Where the record attests a community only through a contact period, the window **is** that contact period, and the record says so. Honest imprecision is preserved rather than resolved: widening a window under uncertainty is permitted; narrowing it to look decisive is not.
- **`attestation_uncertainty` is confidence-inheriting and reproducible, not ad hoc.** It maps from the weakest **temporally relevant** component of the warranting record(s) — the component that grades *when* the community is attested — using the same table the tradition-class positioning bounds use:

  | weakest temporally-relevant component (KOS-0003 §8) | `attestation_uncertainty` |
  |---|---|
  | High / Very High | `low` |
  | Moderate | `moderate` |
  | Low / Very Low | `high` |

  Non-temporal components (character, mechanism, target adequacy, classification fit) grade something other than *when*, and do **not** govern this field — the same exclusion STD-0002 v1.11 established for `range_uncertainty`, and for the same reason. **The exclusion is recorded in the entity's own body**, per entity, so the derivation is auditable.
- `attestation_claims` entries are **graph claims** (§12.1 — must resolve to existing objects; dangling entries fail integrity). They may name Claim Records or Finding Records; both are graded records.
- `attestation_window` is **presentation only** and carries **no evidential weight**. The contestedness lives in the confidence of the warranting records, not in this string.
- **Community entities are off-timeline at launch** (ADR-GOV-0012 D7). They are bound to the tradition layer for future display by the non-evidential `projects_to` relation (STD-0004 §7), which asserts a rendering projection and never a historical relationship.
- The validator shape-checks these at **error** level: co-presence; `attestation_claims` a non-empty list of identifiers; `attestation_window` a non-empty string; `attestation_uncertainty` one of `low`/`moderate`/`high`; and the forbidden-field rule. Whether a window is *correctly derived* from its warranting records is a review question, not a shape question.

---

# 12. Metadata Integrity Rules

Metadata must:

- match document content,
- remain current,
- use approved values,
- avoid ambiguity.

Incorrect metadata creates structural errors.

## 12.1 Frontmatter References Are Graph Claims (ADR-GOV-0004 §2 D4)

Entries in **`related_documents`**, **`parent_documents`**, and any typed reference field (the `relationships` block, §7) **must resolve to existing files.** A frontmatter reference is not a note or an intention — it is a **claim that an edge exists in the knowledge graph**, and it is read as such by tooling.

**Named candidates and non-existent objects are referenced in prose only.** A reserved-but-unopened identifier, a planned object, or a candidate follow-on may be discussed freely in an object's body; it may **not** appear in a reference field until the object exists.

*Rationale.* Enforcement already exists — `graph_integrity.py` fails on a dangling reference — but the tool catches the violation only after it is committed. This rule states the constraint at **authoring time**, and states *why* the field is load-bearing: a reference that resolves to nothing silently corrupts the graph the architecture is built on. The occasioning case is recorded in ADR-GOV-0004 §1.4 (a named-but-unopened candidate listed in `related_documents` produced the vault's first dangling reference since GB-2026-005).

---

# 13. Metadata Change Rules

Changes to:

- title,
- document type,
- category,
- status,

require review.

Changes to:

- updated date,
- minor tags,
- relationships,

may occur during maintenance.

---

# 14. Example Complete Metadata Block

```
---
title: Example Document
document_type: Standards Document
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Operating System
  - Standards
parent_documents:
  - KOS-0009 Knowledge Representation Framework
related_documents:
  - STD-0001 Naming & Identification Standard
tags:
  - ProjectRelatio
  - Example
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---
```

---

# 15. Relationship to Future Templates

All future templates must implement this standard.

Templates provide:

- convenience,
- consistency,
- reduced error.

STD-0002 provides:

- authority.

---

# 16. Governance

STD-0002 is maintained under:

KOS-0011 — Governance, Stewardship & Evolution Framework.

Changes require:

- documentation,
- review,
- version update.

---

# 17. Closing Principle

Project Relatio adopts:

> Metadata is the structural memory of the knowledge system.

---

# 18. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial metadata and YAML standard|
|1.1|2026-07-09|Adopted|Widened approved document_type values to include Kernel Operating System Document, Standards Navigation Document, and Constitutional Instrument, matching documented vault usage found during the pre-STD-0006 Architecture Status Note audit|
|1.2|2026-07-09|Adopted|Added "Review Report" document_type for STD-0006 review/audit outputs; added a status-field reconciliation note deferring to STD-0005's two-dimensional lifecycle model|
|1.3|2026-07-09|Adopted|Consolidated meta-document types: replaced layer-prefixed values (Standards/Kernel Navigation Document, Kernel Architecture Document/Manifest, Kernel Governance Document) with layer-agnostic Navigation Document, Architecture Document, and Governance Record; documented the content-type vs meta-type distinction|
|1.4|2026-07-09|Adopted|Added Investigation Record and Finding Record document_types, defined by KOS-0012 and demonstrated needed by the RQ-0001 pressure test|
|1.5|2026-07-11|Adopted|Implemented STD-0005's two-dimensional lifecycle in metadata (GB-2026-006): `status` narrowed to **maturity** (Proposed/Draft/Reviewed/Adopted); added the required **`operational_status`** field (Active/Superseded/Archived). Migrated the vault — operational values previously held in `status` moved to the new field. Trigger: the KOS-0200/ROLE-0003 supersession/archival events the deferral was waiting on.|
|1.6|2026-07-11|Adopted|Added the optional **typed `relationships`** frontmatter block (`type` + `target`), closing Pressure Test F-4 / GB-2026-001 — STD-0004's vocabulary can now be expressed in metadata, not only prose. Additive: the flat `parent_documents`/`related_documents` lists are retained for tooling. Adopted for Knowledge Base objects; `graph_integrity.py` made type-aware.|
|1.7|2026-07-20|Adopted|Added **§12.1 Frontmatter References Are Graph Claims**, enacting **ADR-GOV-0004 §2 D4**. Entries in `related_documents`, `parent_documents`, and the typed `relationships` block must resolve to existing files; named candidates and non-existent objects are referenced in **prose only**. Placed here rather than in STD-0004 because D4 governs what the frontmatter *fields* must contain (STD-0002's domain), whereas STD-0004 governs which relationship *types* exist and what they mean. Additive rule statement only — no field added, removed, or redefined, and no existing requirement changed; `graph_integrity.py` already enforced the constraint after commit, and this states it at authoring time with its rationale.|
|1.8|2026-07-20|Adopted|Added §11 subsection **Claim Records and Finding Records**, requiring the epistemic-axis fields `confidence` (always-a-list, per-component level/label) and `reliance_tier` (R0/R1/R2). Additive document-class fields per the existing §11 pattern; values and rules governed by the Epistemic State Standard (STD-0008), whose R-tier vocabulary is constitutionally sourced from ADR-GOV-0006. Labels follow the canonical KOS-0003 §8 scale (Very High / High / Moderate / Low / Very Low). No existing field removed, renamed, or redefined. Migration of existing Claim/Finding records gated separately (GB-2026-038); until it completes, the validator's epistemic-field check is warning-gated.|
|1.9|2026-07-21|Adopted|Activated review fields (review_cycle/review_date/last_reviewed) as required Claim/Finding fields per ADR-GOV-0008 and the Review & Revision Standard (STD-0009); promoted them out of §8 reserved status; added optional bounded_by to confidence components (graph-claim rule §12.1 applies). Additive.|
|1.10|2026-07-21|Adopted|Added §11 subsection **Entity Records (tradition class)**, requiring `tradition_type` (founded/emergent/reform/syncretic), `dating_claims` (graph-claim pointers, §12.1), and `display_range` (render-only string) on tradition-class entities and forbidding them on concept entities (ENT-0001…0007 untouched), enacting ADR-GOV-0009 D3. No `origin_date` field exists by decision (dates are claims). Additive document-class fields per the existing §11 pattern; validator shape-checks co-presence and the tradition_type vocabulary at error level.|
|1.11|2026-07-22|Adopted|Added to the §11 **Entity Records (tradition class)** subsection three **OPTIONAL, render-only positioning fields** — `range_start_year` (integer, BCE negative), `range_end_year` (integer or the literal `present`), and `range_uncertainty` (`low`/`moderate`/`high`) — enabling the proportional SVG timeline view (owner-ratified upgrade from Path A). **Non-evidential:** derived from and bounded by the entity's dating claim(s), inheriting that claim's confidence; a bar drawn from them must never render more certain than the claim warrants; `display_range` remains the authoritative label. `range_uncertainty` maps reproducibly from the confidence of the claim's **emergence/crystallisation-dating component** (High/VeryHigh→low, Moderate→moderate, Low/VeryLow→high; non-temporal descent/classification components do not govern it — refines the ADR-GOV-0009-brief phrasing "weakest component," which read literally would let a Low *descent* grade mis-mark a well-dated tradition). OPTIONAL: a tradition without them renders by a documented undated/sequence-only fallback (never invented coordinates); when any is present, `range_start_year` and `range_uncertainty` are co-required, `range_end_year` optional (absent = terminus not claim-dated; `present` = living). Additive only — no existing field removed, renamed, or redefined. Validator shape-check (integer years or `present`; uncertainty vocabulary; start+uncertainty co-presence) at error level, enabled only after the four existing tradition entities were backfilled this session (vault green at every boundary).|
|1.12|2026-07-22|Adopted|Added the **required `attribution` field** on every formal Knowledge Object, enacting **ADR-GOV-0011** Decisions B and C (Stage 1, record-level). Added to §5's required-field list; defined as a new `# attribution` section in §6 (the home of universally-required fields, chosen over a new numbered section so that §7–§18 are **not renumbered** and every external citation of §7/§8/§10/§11/§12.1 stays valid); binding rules in new **§6.1**. **ALWAYS A LIST**, minimum one entry, exactly one at Stage 1 with `event: created` — never a scalar, so Stage 2's per-event attribution (deferred, ADR-GOV-0011 §8) extends it **additively** rather than by migration (the `confidence` always-a-list precedent). Each entry carries `actor` (named human; an AI is never the actor), `role` (free string, ROLE-#### where applicable — **no controlled enum**, lanes/roles do not exist, ADR-GOV-0011 §7), `event` (`created` only at Stage 1), `date` (§10), `ai_degree` (controlled: `unassisted`/`ai-assisted`/`ai-delegated`), and `ai_model_family` (free string, or `none` iff `unassisted`). §6.1 states the three-field distinction that must not be conflated (**`attribution` = provenance** vs §8 `owner` = **stewardship** vs §11 `source_author` = **the external source's author**), the **binding family-level independence rule** (same model family is same-kind regardless of version or operator; same-family-assisted work does not sum toward independence — Decision C), the **binding selective-visibility constraint** (durable but withholdable at review time; no surface used for blinded review may render it unconditionally) with its small-n honesty limit, and the **Decision E metric prohibition**. Cross-reference notes added to §8 and §11; §14's example block updated. The full corpus (335 formal Knowledge Objects, this standard included) was backfilled in **this same commit**, each entry dated from that record's own `created` field — never the migration date — as a **best-effort record-level characterization**, with a candidate exception list reported for owner hand-correction rather than the degree being guessed at. The validator's presence/shape check was enabled at **error** level only in the **following** commit (backfill before enforcement; vault green at every boundary). Additive only — no existing field removed, renamed, or redefined.|
|1.13|2026-07-24|Adopted|**Enacts ADR-GOV-0012 D2/D3/D4 — the multi-granularity entity layer.** Added to §11 the **REQUIRED-AT-MINT `rendering_class` field** carrying the D2 controlled vocabulary `tradition` / `substrate` / `community`, required on any entity carrying a class field set and **absent on the seven concept entities**, which stay outside the timeline program and untouched. Added the §11 subsection **Entity Records (community class)** with the D4 **attestation-window** semantics — `attestation_claims` (graph-claim pointers, §12.1; Claim or Finding Records), `attestation_window` (render-only string), and `attestation_uncertainty` (`low`/`moderate`/`high`, confidence-inheriting from the weakest **temporally relevant** component of the warranting records, non-temporal components excluded per the v1.11 precedent and the exclusion recorded per entity). **A community entity carries a WINDOW, NEVER a founding date:** the tradition-class trio and the render-only positioning bounds are **forbidden** on the community class, so no numeric geometry and no founding-date-style bar can exist for one; honest imprecision is preserved, and widening a window under uncertainty is permitted where narrowing it is not. `rendering_class: substrate` is established as a class with **no field set** — substrate rendering and its dating question are deferred by ADR-GOV-0012 D7 and no substrate entity is minted; the value exists so the class is reachable later without reopening governance. Community entities are **off-timeline at launch** (D7) and bind to the tradition layer through the non-evidential `projects_to` relation (STD-0004). Additive only — no existing field removed, renamed, or redefined; ENT-0008…ENT-0015 were backfilled as `tradition` (field + history row only) in a **separate, preceding commit**, and the validator's `rendering_class` presence check was promoted from warning to **error** only in the commit **after** that backfill (define → backfill → enforce; vault green at every boundary). Community-class shape checks (co-presence, list/string/vocabulary, forbidden-field rule) land at error level from introduction, since they guard births and no community entity existed before this ADR.|

---

# End STD-0002