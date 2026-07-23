---
title: ADR-GOV-0002 - Guardrail and Scope Reframe
document_type: Architecture Decision Record
version: 1.1
status: Adopted
operational_status: Active
created: 2026-07-11
decision_status: Accepted
decision_date: 2026-07-11
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - Architecture Baseline
  - OPS-0003 Research Workflow
  - ROLE-0005 Vision Steward
tags:
  - ProjectRelatio
  - ADR
  - Governance
  - ScopeGuardrail
relationships:
  - type: derived_from
    target: CON-0003
  - type: related_to
    target: Architecture Baseline
  - type: related_to
    target: OPS-0003
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-11
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# ADR-GOV-0002

# Guardrail and Scope Reframe

## Adopted Architecture Decision Record

---

# 1. Context

Two constraints had governed the project's growth:

1. **The over-architecture guardrail** — "every addition must make the research better, not the architecture more complete," framed as *the primary defence against the project's single standing risk*.
2. **The health / "education-only" scope** — health investigations framed as educational evidence reviews, not medical advice.

The owner (Vision Steward) clarified the **origin and intent** of the first: the over-architecture guardrail was put in place to **constrain a specific collaborator (ChatGPT) that tended to run wild with architectural ideas** — to keep its contributions practical. It was **not** a description of the owner's own thinking, and the owner does not apply that restraint to himself. With that collaborator's involvement now much reduced, the guardrail's *defensive, fear-based framing* is miscalibrated: in this very session it was observed suppressing useful, evidence-warranted work (the assistant had to rhetorically re-label good additions to slip past it), which is a sign the rule — not the work — was mis-tuned.

The owner asked whether the guardrail (and the education-only scope) should be adjusted to better fit the project's values, and whether the question should be routed through the research circuit. **Reasoning that a project's own governance is a normative Vision-Steward decision, not an evidence-determinable research question** (the research circuit answers scholarly/empirical questions; governance decisions are owner-reserved — CON-0003 §5.2), the owner decided the reframe directly. A separate, genuinely *researchable* question — what is known about the value and failure modes of formal constraints in evolving knowledge systems — may be run later to *inform* future governance, without *making* the decision.

**Transparency note (recorded deliberately).** The reframe was recommended by an AI assistant — i.e. an AI recommending that a constraint on AI contributions be loosened. That is a textbook motivated-reasoning hazard, and this project is built to catch it. The decision was adopted only in the form that **keeps** the underlying discipline (justify-by-use, applied to all contributors by merit regardless of source); the fear framing and the collaborator-specific origin are what were removed.

---

# 2. Decision

> **(a)** The over-architecture guardrail is **reframed from a defensive constraint into a purpose principle**: the system exists to do excellent research *and* to become an excellent knowledge architecture; **every addition — from any contributor — earns its place on its merits, by improving a real answer or the system's ability to produce one.** Additions are justified by *use*, not by symmetry or completeness; what does not earn its keep is removed. This discipline applies to contributions **by their merit, not their source**, and no longer casts architectural growth as a standing risk to be defended against.
>
> **(b)** The health / "education-only" scope is **clarified, not lifted**: the system may investigate **any** question to full depth and rigour. What it does not do is give **individualized** medical/clinical advice (it lacks the person's history, labs, and exam), so it reports general evidence and brackets the individual case — this is *epistemic honesty, not a limit on inquiry*. Health findings are framed for expert application and remain **gated from third-party external reliance** pending genuine independent and clinician review. **The system informs expert judgment (including the owner's clinical background); it does not replace a clinician.** The scope constrains outward-facing individualized claims, not what may be investigated.

---

# 3. Alternatives Considered

1. **Remove the over-architecture guardrail entirely** — rejected. Its defensive framing was miscalibrated, but its core (justify-by-use, delete what doesn't earn its keep) is genuinely good design discipline independent of any collaborator, and removing it would forfeit the protection that makes AI contribution safe.
2. **Keep the guardrail unchanged** — rejected. Framing architectural growth as the "single standing risk" was overfit to a departed collaborator and was observed suppressing warranted work.
3. **Route the decision through the research circuit** — rejected as a category error: a normative governance decision is not evidence-determinable. Research may *inform* it later; it cannot *make* it.
4. **Lift the education-only scope** — rejected. The individualized-advice limit is epistemic honesty (the system genuinely lacks the data), and the third-party reliance gate reflects real safety and the owner's professional boundary.

---

# 4. Reasoning

The healthy content of the guardrail was always the *value* ("does this make the research better?"), never the *fear* ("beware over-architecture"). Restated as a value, it (i) keeps AI and human contributions disciplined by merit, (ii) stops penalising genuinely useful architectural evolution, and (iii) sits correctly *beneath* the owner's stated aspiration ("eventually the world's best knowledge architecture") rather than forbidding richness. The education-scope clarification separates two things that were blurred: the system's *inquiry* (unbounded, rigorous) from its *outward-facing claims* (bounded by epistemic honesty and the owner's professional/legal boundary).

---

# 5. Consequences

**Accepted costs:**
- Loss of a simple, blunt brake. The replacement ("justify by use, on merit") requires judgment rather than reflexive refusal — the Vision Steward and Knowledge Architect must actually weigh whether an addition earns its place.
- Building toward an excellent architecture is now a legitimate concurrent aim, which invites more architectural work; the justify-by-use test must be applied honestly to keep that from drifting back into over-production.

**Benefits:**
- Warranted improvements are no longer suppressed or forced into rhetorical contortions.
- The discipline now applies uniformly by merit, not by which tool proposed it.
- The health scope is understood accurately — the system's usefulness to the owner is not limited, only its outward individualized claims.

**Affected objects:** CLAUDE.md (scope-guardrail section + working rules), OPS-0003 §2, Architecture Baseline §1/§4/§5, ROLE-0005 §6. Historical records (Standards Architecture Retrospective, Pressure Test / assessment reports, past investigations) are **not** rewritten — they are point-in-time records. Identifier Registry updated (ADR-GOV-0002 registered).

---

# 6. Decision Authority

**Brian Noon, Vision Steward (ROLE-0005) and owner.** Governance/architectural reframe is Vision-Steward-reserved (CON-0003 §5.2; ROLE-0005). Decided and authorised in session, 2026-07-11.

---

# 7. Review Date

Revisit if (a) the justify-by-use test is observed drifting back into either over-production or over-suppression, or (b) the informing research question (on constraints in knowledge systems) returns findings that materially bear on the guardrail's form.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-11|Adopted|Initial decision record. Reframes the over-architecture guardrail (fear → merit-based purpose principle; origin as a ChatGPT-restraint disclosed) and clarifies the health/education scope (inquiry unbounded; outward individualized claims and third-party reliance bounded). Motivated-reasoning hazard of an AI recommending looser AI-constraints recorded and mitigated by keeping the justify-by-use discipline.|
|1.1|2026-07-22|Adopted|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

# End ADR-GOV-0002
