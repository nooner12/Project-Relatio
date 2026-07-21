---
title: STD-0008 - Epistemic State Standard
document_type: Standards Document
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-20
category:
  - Knowledge Operating System
  - Standards
  - Epistemic Architecture
parent_documents:
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - STD-0002 Metadata & YAML Standard
  - STD-0004 Relationship & Linking Standard
  - STD-0005 Lifecycle & Revision Standard
  - ADR-GOV-0006 - Tiered External-Reliance Model and Live-Retrieval Verification Channel
  - ADR-GOV-0007 - Reflexive Architecture Evolution
relationships:
  - type: depends_on
    target: ADR-GOV-0006
tags:
  - ProjectRelatio
  - Standards
  - EpistemicState
  - Confidence
  - Reliance
---

# STD-0008

# Project Relatio Epistemic State Standard

## Version 1.0

## Adopted Standards Document

---

# 1. Purpose

This standard defines the **epistemic axis** of a Knowledge Object: how strong its evidence is, and how far that evidence has been independently verified. It owns the vocabularies and the rules for both. It is the epistemic counterpart to STD-0005 (which owns the lifecycle axis).

Where STD-0005 answers *"how mature is this object, and is it operational,"* this standard answers *"how well-supported is this claim, and can it be relied upon outside Relatio."*

---

# 2. Standard Principle

Project Relatio adopts:

> Epistemic state is not one number. Evidential strength and verification independence are distinct properties, and a Knowledge Object must state both without collapsing them.

---

# 3. Scope

Governs, for Claim Records and Finding Records (and any future object carrying a graded conclusion):

- the **confidence** sub-axis (evidential strength),
- the **reliance** sub-axis (verification independence),
- the rules binding how these are assigned, split, and inherited.

Does **not** define: relationship vocabulary (STD-0004), lifecycle/maturity (STD-0005), metadata *format/placement* (STD-0002 §11 owns where these fields live; this standard owns what they *mean*). The division mirrors STD-0002 §5 holding the `status` field while STD-0005 owns what maturity means.

---

# 4. The Two Sub-Axes (independent, never collapsed)

An object's epistemic state has two independent sub-axes, modeled on STD-0005's independent maturity/operational dimensions:

1. **Confidence** — evidential strength. How well the evidence supports the claim. Answered on the merits of the sources and reasoning.
2. **Reliance** — verification independence. How far the supporting evidence has been independently verified, and therefore whether the finding may be relied upon *outside* Relatio (thesis, public, cross-stream).

These are orthogonal. A claim may be high-confidence and low-reliance (well argued from sources not independently re-verified) — the state of all closed INVs as of adoption. The two are carried in **two independent fields** and are never averaged into or substituted for one another.

---

# 5. The Confidence Sub-Axis

## 5.1 On-record vocabulary — Level N (Label)

The authoritative on-record confidence value is the canonical **KOS-0003 §8 hybrid scale** — a numeric level paired with its qualitative label, always written together (e.g. **"Level 4 (High)"**):

| Level | Label |
|-------|-------|
| Level 5 | Very High |
| Level 4 | High |
| Level 3 | Moderate |
| Level 2 | Low |
| Level 1 | Very Low |

The level definitions defer to **KOS-0003 §8**, which remains the substantive definition of the scale; this standard governs its use as a *field value* and the rules around it, not its internal semantics. KOS-0008 §8 restates the same scale — one scale, not two vocabularies.

KOS-0003 §8 additionally defines **Level 0 — Unsupported**. Level 0 is **not a valid field value**: an Unsupported conclusion does not qualify for the permanent Knowledge Base (KOS-0003 §12), so no Claim or Finding Record can carry it. The field range is therefore 1–5.

## 5.2 Supporting grading systems (inform the field; are NOT the field)

Two other systems inform Level N but are **never** the on-record field value:

- **Four-tier evidence grading** (★★★ meta-analysis/SR · ★★☆ RCT/prospective cohort · ★☆☆ observational/small trial/consensus · ◇◇◇ theoretical/mechanistic): grades the *underlying evidence*. It informs the Level N a claim receives but is recorded in prose/evidence sections, not the confidence field. The export-boundary translation between the native scale and this system is governed by STD-0006 Appendix A.
- **H-band investigation protocol** (H-a…H-e): a reusable-but-uncodified analysis protocol (GB-2026-027, option b). **Prose only. Never in any frontmatter or grading field.** This standard does not change that fence.

## 5.3 Confidence is a LIST, always (the split-grade rule)

The `confidence` field is **always a list of one or more graded components.**

- A single-grade claim is a **one-item** list, component name `overall`.
- A split-grade claim is a **multi-item** list, one entry per component.

Each component carries: `component` (a short name for what is graded), `level` (Level N), and `label` (the matching label). Example shapes appear in STD-0002 §11.

**Split grades are never averaged.** A claim whose components differ (e.g. placement Level 3, criteria-mechanics Level 2 — CLM-0083) records both; it does not report a blended "Level 2.5" or round to one. The list structure makes the non-averaging rule structural rather than advisory.

## 5.4 Layer-inheritance bound

Where a claim rests on another graded object (an investigation's source layer, a cited finding), each component's Level N is **bounded by** the layer(s) it rests on and by its own weakest sub-element. No component may exceed the grade of its load-bearing support. (This generalizes the per-investigation layer-inheritance rules used in INV-0014/0015 into a standing rule.)

## 5.5 No-inheritance-across-adaptation (grading doctrine)

**An educational, applied, or cross-stream adaptation of a finding does NOT inherit the finding's confidence level.** When a Relatio finding is used to inform work in another register (wellness education, curriculum, public content), the adaptation is graded on its *own* evidential footing for *its own* claim. A ★★★ or Level-4 source finding can support only an appropriately downgraded applied claim; both grades must be visible, never one silently standing in for the other. (Codifies the standing cross-stream rule; prevents grade-laundering from research into application.)

---

# 6. The Reliance Sub-Axis

## 6.1 On-record vocabulary — Reliance Tier

The authoritative reliance value is the **Reliance Tier**, whose constitutional source is **ADR-GOV-0006 - Tiered External-Reliance Model and Live-Retrieval Verification Channel**:

| Tier | Name | Meaning | External-citable? |
|------|------|---------|-------------------|
| R0 | Parametric | Supported by model knowledge / verification-light review only | No |
| R1 | Retrieval-verified | Primary-text locus confirmed against an open critical edition under edition-discipline | Yes, edition named |
| R2 | Independently verified | Confirmed via a channel outside single-model retrieval (institutional access, human, or independent second model) | Yes, full strength |

R1's edition-discipline conditions and R2's mechanisms are defined in ADR-GOV-0006 (§3 and §2 respectively); this standard carries the tier as a field value and the roll-up rule below.

## 6.2 Reliance is assessed PER LOCUS; a claim rolls up to its floor

Reliance is assessed per supporting locus. A claim's overall `reliance_tier` is the **lowest** tier among its load-bearing loci (a claim with any R0 load-bearing locus is R0 overall). Partial verification is recorded as partial — never rounded up. (CLM-0083: its placement rests on live-read surfaces but its criteria-mechanics locus is paywalled/unread → the claim does not clear.)

## 6.3 The reliance gate travels with the data

Any representation of a finding outside its record — visualization, export, cross-stream citation, public display — **must carry the reliance tier visibly.** Stripping reliance status for presentation is prohibited: it is the precise vector by which a gated finding leaks into unwarranted reliance. In visual/exported contexts the tier is a first-class element, not a footnote.

---

# 7. Required Epistemic Fields

Claim Records and Finding Records require:

- `confidence` — list (§5.3), at least one component.
- `reliance_tier` — one of R0 / R1 / R2 (§6.1).

The field *format and placement* are specified in STD-0002 §11 (this standard's companion amendment); the *values and rules* are specified here.

---

# 8. Relationship to Other Standards

- **STD-0002** — owns the field format/placement (§11 document-specific fields).
- **STD-0005** — parallel axis (lifecycle); this standard follows its two-independent-dimensions pattern.
- **KOS-0003** — owns the substantive Level N scale semantics; this standard governs its use as a field and the surrounding rules.
- **ADR-GOV-0006 - Tiered External-Reliance Model and Live-Retrieval Verification Channel** — constitutional source of the R-tier vocabulary.
- **ADR-GOV-0007 - Reflexive Architecture Evolution** — reflexive recommendations about Relatio's own structure are themselves graded work and carry confidence/reliance under this standard like any finding.

---

# 9. Governance

Maintained under KOS-0011. Changes require documentation, review, version update. The confidence and reliance vocabularies are controlled; adding or altering a tier or level is a standards change, not a maintenance edit.

---

# 10. Revision History

| Version | Date | Status | Description |
|---|---|---|---|
| 1.0 | 2026-07-20 | Adopted | Initial epistemic state standard: two independent sub-axes (confidence / reliance); Level N on-record with ★-tier and H-band as informing-not-field; confidence-as-list split rule (never averaged); layer-inheritance bound; no-inheritance-across-adaptation doctrine; reliance tier R0/R1/R2 per ADR-GOV-0006, per-locus with floor roll-up; gate-travels-with-data rule. §5.1 labels verified against KOS-0003 §8 at authoring — the candidate text's proposed labels (Level 5 "Established", Level 1 "Minimal / Speculative") were corrected to the canonical **Very High / High / Moderate / Low / Very Low**, and Level 0 (Unsupported) documented as KB-excluded, fixing the field range at 1–5. |

---

# End STD-0008
