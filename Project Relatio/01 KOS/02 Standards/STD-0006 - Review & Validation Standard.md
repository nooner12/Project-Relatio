---
title: STD-0006 - Review & Validation Standard
document_type: Standards Document
version: 1.4
status: Adopted
operational_status: Active
created: 2026-07-09
category:
  - Knowledge Operating System
  - Standards
  - Review Architecture
parent_documents:
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - KOS-0009 Knowledge Representation & Information Architecture Framework
  - STD-0005 Lifecycle & Revision Standard
related_documents:
  - STD-0001 Naming & Identification Standard
  - STD-0002 Metadata & YAML Standard
  - STD-0003 Classification & Discovery Standard
  - STD-0004 Relationship & Linking Standard
  - STD-0007 Terminology & Semantic Stewardship Standard
tags:
  - ProjectRelatio
  - Standards
  - Review
  - Validation
  - QualityAssurance
  - Governance
---

# STD-0006

# Project Relatio Review & Validation Standard

## Version 1.4

## Adopted Standards Document

---

# 1. Purpose

The Review & Validation Standard defines how compliance with the other Standards documents (STD-0001, STD-0002, STD-0003, STD-0004, STD-0005, STD-0007) is verified.

A standard that defines rules but never checks them is a suggestion. STD-0006 closes that gap: it is the mechanism by which Project Relatio confirms that a Knowledge Object actually follows the architecture it claims to belong to.

This standard was authored after a direct audit of the vault surfaced concrete, non-hypothetical validation failures — malformed YAML frontmatter, document_type values used inconsistently with the approved list, dangling references to documents that do not exist, and a document still in Draft being treated elsewhere as if it were Adopted. STD-0006 exists because these problems were found, not because they were anticipated.

---

# 2. Standard Principle

Project Relatio adopts:

> A rule that is never checked will eventually be violated without anyone noticing.

Review and validation are not bureaucratic overhead. They are how the architecture keeps its word to itself.

---

# 3. Scope

This standard governs:

- when review and validation occur,
- what is checked,
- how non-conformance is recorded,
- how findings relate to governance under KOS-0011.

This standard does not define:

- who performs review (a Roles-layer question, deferred — see Section 13),
- a mandatory calendar cadence for periodic audits (an Operations-layer question, deferred until Templates and Operations are built),
- remediation of any specific document's existing non-conformance (assigned to the Standards Architecture Retrospective, not to this standard).

---

# 4. Review Triggers

Validation against this standard occurs at four points:

---

## 4.1 Creation

Before a new Knowledge Object moves from Draft to Reviewed (per STD-0005 §7–8), it is checked against the Validation Checklist (Section 5).

---

## 4.2 Status Transition

Any change to a document's Maturity State or Operational State (STD-0005 §4) re-triggers validation. A document moving to Adopted, Superseded, or Archived must have its metadata and relationships updated to match — status text alone is not sufficient.

---

## 4.3 Standard Amendment

When a governing Standard itself changes (e.g., STD-0002's approved document_type list is widened), previously adopted documents are not automatically re-validated, but the amendment is logged as an open item for the next Standards Architecture Retrospective, so drift between old documents and the current standard is tracked rather than silently accumulating.

---

## 4.4 Periodic Audit

Independent of any single document's lifecycle, the vault as a whole may be audited against this checklist. The Architecture Status Note produced 2026-07-09 is the first instance of this — an ad hoc audit preceding STD-0006's own adoption. Future audits follow the same checklist this standard defines.

---

# 5. Validation Checklist

Every check below corresponds to an existing Standard. STD-0006 does not introduce new rules — it defines how the existing rules are verified.

---

## 5.1 Naming Conformance (STD-0001)

Check that:

- the identifier follows `TYPE-NNNN` with four digits,
- the filename follows `[IDENTIFIER] - [TITLE]`,
- the `title` field matches the filename exactly,
- the document sits in a folder following `[number] [category]`,
- tags use PascalCase.

---

## 5.2 Metadata Conformance (STD-0002)

Check that:

- all required fields are present (`title`, `document_type`, `version`, `status`, `created`, `category`, `tags`),
- `document_type` uses an approved value (STD-0002 §6, as amended),
- `status` uses an approved value (STD-0002 §6),
- YAML is syntactically valid — no unescaped control characters, no content duplicated outside the frontmatter block,
- field names use `lowercase_with_underscores`,
- dates use `YYYY-MM-DD`.

---

## 5.3 Classification Conformance (STD-0003)

Check that `category` and tag usage follow STD-0003's classification rules and do not substitute for genuine relationships.

---

## 5.4 Relationship Conformance (STD-0004)

Check that:

- every document listed in `parent_documents` or `related_documents` actually exists in the vault,
- relationship vocabulary is specific where possible (STD-0004; `related_to` used sparingly),
- a document does not list a Superseded or Archived document as a live parent or related document without acknowledging its status.

---

## 5.5 Lifecycle Conformance (STD-0005)

Check that:

- Maturity State and Operational State are both present and tracked independently,
- a Superseded document identifies its successor and vice versa,
- no document elsewhere in the vault cites a Superseded or Archived document as though it were current,
- version numbers move in the direction implied by the Revision History.

---

## 5.6 Terminology Conformance (STD-0007)

Check that preferred terminology (e.g., "Knowledge Object") is used consistently rather than superseded or ad hoc terms.

---

## 5.7 Evidence Integrity (KOS-0003 §12.1)

Applies to research objects (Claim, Source, Finding, Investigation). Check that:

- no source, citation, author, date, DOI, URL, page/verse reference, or numeric result has been **invented**;
- every cited source can be **located and verified**, or its unverifiability is explicitly recorded as a limitation;
- a cited passage **actually supports** what it is said to support (source fidelity);
- figures are reported at the precision the evidence supports (no false precision);
- uncertainty about a reference is **stated**, not filled in with a plausible substitute.

**Fabricated or unverifiable evidence is an automatic `Blocked` verdict (§7.3).** This check is not discretionary and is never downgraded to Flagged.

---

# 6. Non-Conformance Handling

Failing a check does not retroactively revoke a document's Adopted status, and does not require an immediate edit. Non-conformance is:

1. recorded — as a finding, with the specific check that failed,
2. attributed — to a specific document and field,
3. scheduled — for remediation during the next governed pass over that document (a Retrospective, an Integration Update, or a direct revision), rather than fixed reactively and incrementally.

This mirrors CLAUDE.md's existing rule against spontaneous restructuring: finding a problem is not, by itself, authorization to fix it outside a governed pass.

---

# 7. Review Outcomes

A validated document receives one of three outcomes. These are review outcomes, not values for the `status` metadata field (STD-0002 §6) — a Flagged or Blocked document keeps its existing `status`; the outcome is recorded as a finding (Section 6), not as new frontmatter.

---

## 7.1 Conformant

Passes all applicable checks in Section 5.

---

## 7.2 Flagged

Fails one or more checks but remains usable; the finding is logged per Section 6 and does not block continued use or citation of the document.

---

## 7.3 Blocked

Reserved for two cases:

1. **Structural:** non-conformance makes a document unreadable (e.g., invalid YAML that breaks parsing). Dependents cannot verify a reference they cannot parse.
2. **Epistemic:** **fabricated or unverifiable evidence** (KOS-0003 §12.1, checked at §5.7), an unsupported core claim, or incoherent reasoning.

A Blocked object must be corrected before anything depends on it. A Blocked verdict is never resolved by lowering its severity.

---

## 7.4 Appeal and Preservation of Disagreement

A **Blocked** verdict may be contested by the object's author. Per CON-0003 GP-004 (*Preserve Disagreement*):

- A contested Blocked verdict escalates to the **Vision Steward (ROLE-0005)** with **both positions recorded in full**.
- The dissenting position is **never deleted** when a dispute is resolved; it is retained in the object's record.
- Disputes are classified using the Kernel's existing taxonomy (KOS-0011 §11): **CR-001** Evidence Conflict, **CR-002** Interpretation Conflict, **CR-003** Framework Conflict — and resolved by the process in CON-0003 §8.

Consensus does not equal truth. A minority position may contain valid insight and is not discarded for lack of agreement.

---

## 7.5 Verification Integrity — a review must disclose the strength of its own check

The evidence-integrity check (§5.7) is only as strong as the verification the reviewer could actually perform. Its strongest form is **live re-location** of a sample of cited sources and figures against their primaries. When that is not possible — external tools unavailable or rate-limited, primaries inaccessible — the check degrades to internal-consistency-plus-parametric-knowledge, which is materially weaker and, for a same-model reviewer, shares the author's blind spots.

Therefore:

1. **A review must state the strength of its own verification.** If live re-location could not be performed, the review is marked **verification-light** and says so explicitly.
2. **A verification-light review may issue Conformant/Flagged verdicts but may NOT clear an object for external reliance.** Reliance on such an object is **gated** pending either (a) live re-verification of the flagged figures, or (b) genuine independent review (a *different* model and/or a qualified human — CON-0003 §4.5), as the stakes require. For **reflexive** findings see §7.6 — a different-model reviewer given the vault's framing does not satisfy independence of kind.
3. **Silence is non-conformance.** A review that does not disclose its verification strength is itself Flagged: an undisclosed weak check is worse than a disclosed one, because it invites unwarranted confidence.

This rule generalizes what the first agent-circuit run (RQ-0004) did voluntarily and correctly: the reviewer, unable to reach external tools, marked itself verification-light and gated reliance rather than presenting a weak check as a clean one. It is especially load-bearing for health, safety, financial, or otherwise externally-consequential findings.

---

## 7.6 Reflexive Findings — independence of kind

A **reflexive finding** is one whose conclusion bears on Project Relatio's own design, governance, or method. RQ-0007 / FND-0007 is the originating case.

Reflexive findings carry a hazard §7.5 does not reach. §7.5 governs the *strength* of a check — whether the reviewer could verify. This section governs its *kind* — whether the reviewer could be independent of what is being checked. A reviewer working from the vault's own documents inherits the vault's framing and vocabulary regardless of which model or person performs the review. Procedural independence (ROLE-0004 §5) does not cure this; neither does a different model reading the same framing.

Therefore:

1. **A reflexive finding is gated for reflexive use on creation.** It may not be cited as support for, or vindication of, Project Relatio's own design, governance, or method. Non-reflexive uses of the same finding are governed by §7.5 and the ordinary gates, not by this section.
2. **The gate lifts only on blinded independent review.** The reviewer — a qualified human specialist in the relevant field, or at minimum a different model — receives the question and the evidence *without* the vault's framing, vocabulary, or conclusion, and reaches a finding independently. A different-model reviewer given the vault's framing is **not** sufficient to lift this gate.
3. **A same-model reviewer may flag a reflexive leak but may not certify its absence.** Per Critical Review — RQ-0007 §3.6, a reviewer cannot certify it caught all of a bias it plausibly shares. Such a review is recorded; the gate stands.
4. **Silence is non-conformance**, as in §7.5: a finding that is reflexive and not marked as such is Flagged.

---

# 8. Validation Authority

Validation under this standard is discharged by two roles with **non-overlapping** authority:

| Authority | Role | Warrant | Scope |
|---|---|---|---|
| **Structural validation** | ROLE-0001 Knowledge Architect | KOS-0011 ST-001; CON-0003 §4.2, §4.4 | §5.1–§5.6: naming, metadata, classification, relationships, lifecycle, terminology, graph integrity |
| **Epistemic validation** | ROLE-0004 Critical Reviewer | KOS-0011 ST-004; CON-0003 §4.3, §4.5 | §5.7 and KOS-0003: evidence, reasoning, confidence calibration, bias, source fidelity, fabrication |

Neither role may issue a verdict in the other's scope; each escalates such findings to the other. Disputes between them, or between either and a research author, follow §7.4.

Consistent with CON-0003 GP-003 (*No Authority Over Truth*), **neither role adjudicates whether a claim is true.** They determine only whether it is *structurally sound* and *epistemically warranted*.

---

# 9. Relationship to Other Standards

STD-0006 depends on:

- STD-0001 Naming & Identification Standard
- STD-0002 Metadata & YAML Standard
- STD-0003 Classification & Discovery Standard
- STD-0004 Relationship & Linking Standard
- STD-0005 Lifecycle & Revision Standard
- STD-0007 Terminology & Semantic Stewardship Standard

STD-0006 does not supersede or restate any of them — it verifies them.

---

# 10. Governance

STD-0006 is maintained under:

KOS-0011 — Governance, Stewardship & Evolution Framework.

Changes require:

- documentation,
- review,
- version update.

---

# 11. Closing Principle

Project Relatio adopts:

> An architecture is only as trustworthy as its least-checked document.

Review and validation are how Project Relatio finds out whether that trust is earned, rather than assuming it.

---

# Appendix A — Cross-Stream Confidence Crosswalk (GB-2026-025; owner-ratified 2026-07-14)

## A.1 Purpose and boundary

Findings produced inside Project Relatio are sometimes cited into the owner's **external work streams**, which use a four-tier house evidence scale (★★★ / ★★☆ / ★☆☆ / ◇◇◇). This appendix records the **only authorized mapping** from the canonical native confidence scale ("Level N (Label)," KOS-0003 §8) to that house scale.

**Boundary rule.** The house scale is **external vocabulary**. Knowledge Objects in this vault carry **native ratings only**; the crosswalk is applied **on the way out**, at the citation boundary. No ★-tier is ever written onto a CLM/FND/INV record, and no house/business framing is imported into vault documents. (The glyphs appear in this appendix solely to define the mapping.)

## A.2 The mapping (conservative; floor-taking)

| Native (KOS-0003 §8) | House tier |
|---|---|
| Level 5 (Very High) | ★★★ |
| Level 4 (High) | ★★☆ |
| Level 3 (Moderate) | ★☆☆ |
| Level 2 (Low) | ◇◇◇ |
| Level 1 (Very Low) | ◇◇◇ |
| Level 0 (Unsupported) | **not citable** |

## A.3 Translation rules (all mandatory)

1. **No tier gained in translation.** When a native rating sits between tiers, or is expressed as a reach (e.g., "Level 2 → 3"), take the **lower** tier.
2. **Dual grades translate separately.** Where a claim carries both an underlying-evidence grade and an application/transfer grade, each is translated on its own; the application tier is never lifted by the underlying tier.
3. **Traceability travels.** Every cross-stream citation carries its **INV-####** (and CLM/FND identifier where applicable).
4. **Gates travel.** Any reliance gate on the finding (§7.5 — including health/high-stakes gating and independence-kind gating per GB-2026-023) travels with the citation and binds the receiving stream. Translation never clears a gate.
5. **Receiving-stream review is additional.** A crosswalked citation still passes the receiving stream's own evidence-grading and safety review where required; the crosswalk satisfies neither.

## A.4 Change control

This mapping is part of an Adopted Standard: amendments are **owner-reserved** and follow §10 Governance. Sessions apply the mapping as recorded; they do not improvise equivalences (KOS-0003 §12.1 — no false precision).

---

# 12. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial review and validation standard, grounded in findings from the pre-adoption Architecture Status Note audit|
|1.1|2026-07-09|Adopted|Governance assessment (R2/R6/R7): added §5.7 Evidence Integrity check; expanded §7.3 Blocked to cover fabrication; added §7.4 Appeal & Preservation of Disagreement (CON-0003 GP-004, KOS-0011 §11 conflict taxonomy); replaced role-agnostic §8 with the structural/epistemic validation-authority split (ROLE-0001 / ROLE-0004)|
|1.2|2026-07-10|Adopted|Added §7.5 Verification Integrity: a review must disclose its own verification strength; a verification-light review may not clear an object for external reliance. Owner-adopted from the RQ-0004 first-agent-circuit run (Backlog GB-2026-014).|
|1.3|2026-07-14|Adopted|**Appendix A — Cross-Stream Confidence Crosswalk** (GB-2026-025, owner-ratified): recorded the only authorized native-→-house-tier mapping (L5→★★★, L4→★★☆, L3→★☆☆, L2/L1→◇◇◇, L0 not citable) with five mandatory translation rules (no tier gained; dual grades separate; INV-#### and gates travel; receiving-stream review additional). Boundary rule: native ratings only on Knowledge Objects; crosswalk applied on the way out. Also reconciled the stale `## Version` heading (read 1.1 while frontmatter was 1.2).|
|1.4|2026-07-14|Adopted|**§7.6 Reflexive Findings — independence of kind** (GB-2026-023, owner-ratified): defined reflexive findings; gated them for reflexive use on creation; set blinded independent review (qualified human specialist, or at minimum a different model, working without the vault's framing) as the sole gate-lift; recorded that a same-model reviewer may flag but not certify absence of a shared bias (RQ-0007 §3.6). Enacted at a higher grade than the candidate one-line §7.5 addition, which would have restated §7.5 clause 2 without changing behavior. §7.5 clause 2 cross-referenced to §7.6.|

---

# End STD-0006
