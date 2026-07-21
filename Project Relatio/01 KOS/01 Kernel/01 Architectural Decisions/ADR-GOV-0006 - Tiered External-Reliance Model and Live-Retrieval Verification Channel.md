---
title: ADR-GOV-0006 - Tiered External-Reliance Model and Live-Retrieval Verification Channel
document_type: Architecture Decision Record
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-20
decision_status: Accepted
decision_date: 2026-07-20
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - Governance Backlog
  - ADR-GOV-0003 - Religion Source Base Scope and Stopping Rule
tags:
  - ProjectRelatio
  - ADR
  - Reliance
  - Verification
  - EpistemicIntegrity
---
# ADR-GOV-0006

# Tiered External-Reliance Model and Live-Retrieval Verification Channel

## Adopted Architecture Decision Record

> Replaces the binary external-reliance gate with a three-tier, per-locus model (R0 parametric / R1 retrieval-verified / R2 fully independent), grounded in the 2026-07-20 live-retrieval capability probe. Constitutional source of the reliance-tier vocabulary used by the Epistemic State Standard. Inline pointer: Governance Backlog.

---

# 1. Context

INV-0011, INV-0014, and INV-0015 each closed with findings NOT cleared for external reliance: their reviews were verification-light / verification-split (single-model; primary-text loci verified parametrically, from model knowledge rather than re-checked against the text). The reliance gate exists because a single model checking its own recall is not independent verification.

The reliance posture to date has been **binary** — a finding is either cleared or not, and nothing short of a full independent pass clears it. The 2026-07-20 capability probe (recorded in the support-surface probe report) established empirically that a live-retrieval channel (Claude-in-Chrome) can independently verify _some_ classes of locus but not others:

- Primary text in an open critical edition, original language, was retrieved and matched verbatim (Josephus _Ant._ 18.63 Greek, Niese via Perseus — an exact match to a claim's cited phrase).
- The same locus in a translated/interpolated edition (Whiston English) confirmed only substance, not the cited original-language text.
- Paywalled secondary scholarship (JSTOR) returned an uncrossable CAPTCHA wall.

A binary gate cannot represent this: a claim can now be _partly_ verified.

---

# 2. Decision

Adopt a **three-tier external-reliance model**, assessed **per locus**. A claim's overall reliance status is the **floor** of its load-bearing loci.

**R0 — Parametric (unverified).** Supported only by model knowledge or a verification-light review. Current status of all closed-INV loci. NOT citable into thesis or public work.

**R1 — Retrieval-verified (primary-text).** A primary-text locus confirmed by live retrieval against an **open critical edition in the original language**, under the edition-discipline of §3. Citable into external work with the edition named.

**R2 — Independently verified (full).** A locus — including paywalled secondary scholarship — confirmed by a channel single-model retrieval cannot reach: institutional/library access, a human with the source, or an independent second model. Required for any locus resting on a peer-reviewed monograph's _argument_. Citable at full strength.

---

# 3. Edition-Discipline (the R1 gate, mechanically checkable)

An R1 verification is valid only if the pass confirms, in-record:

1. the retrieved page contains the **original-language critical text** (not a translation) — the Whiston-English case (zero Greek) fails at this step;
2. the edition is **named** (e.g., Niese via Perseus) and recorded with retrieval date and URL;
3. known interpolation/variant status is **flagged** where the claim's grade depends on authenticity (the _Testimonium_ is the paradigm case);
4. the retrieved text is quoted **verbatim at the exact locus** and matches the claim's cited text, character-for-character for original-language phrases.

A single model can perform all four mechanically. None requires interpretive independence — which is precisely why R1 is defensible from a single model and R2 is not.

---

# 4. Load-Bearing (Floor) Rule

A claim clears to the **lowest** tier among its load-bearing loci. Example: CLM-0080 would reach R1 on its Josephus-Greek element but remains R0 on the Meier judgment (SRC-0127) until that is raised to R2 — so the _claim_ stays sub-R2. Partial verification is recorded as partial, never rounded up.

---

# 5. Alternatives Considered

1. **Keep the binary gate.** Rejected — it cannot represent a partly-verified claim, and the probe proves partial verification is now real; a binary gate would either over-claim (treat R1 as full) or waste it (treat R1 as R0).
2. **Treat live retrieval as full independent verification (collapse R1/R2).** Rejected — the channel cannot reach paywalled monograph argument, and a single model interpreting a retrieved page is still single-model for _interpretation_. R1 is honest only when scoped to mechanical primary-text matching.
3. **Mandate second-model verification as the R2 mechanism now.** Deferred — not yet tested from this environment; belongs to a future probe, not this ADR.

---

# 6. Reasoning

The vault's value is that its records can be trusted without re-derivation, and external reliance is the point at which that trust leaves Relatio. A binary gate misrepresents a now-demonstrated reality: verification is not all-or-nothing. The tiers are drawn to match exactly what the retrieval channel can and cannot do, so the model claims no more independence than it possesses — R1 is bounded to mechanical primary-text matching, and R2 (interpretive/paywalled) is explicitly held to require a channel outside single-model retrieval.

---

# 7. Consequences

**Benefits**

- Gated findings gain a path to partial, honest clearance; primary-text-heavy claims can reach R1 without institutional access.
- The caveat stops being all-or-nothing: external work can rely on R1 loci while transparently flagging R0/sub-R2 ones.

**Costs**

- Per-locus assessment is more work than a per-claim stamp.
- R2 still requires a channel outside this toolchain (library/human/second model) — the paywall wall is real and unmovable by retrieval.

**Standing infrastructure**

- A channel-availability check becomes a mandatory precondition of any verification pass (an unpaired retrieval channel silently verifies nothing).

**Affected objects**

- Constitutional source of the R-tier vocabulary consumed by the Epistemic State Standard.
- The candidate live-retrieval verification-pass procedure operationalizes R1.

---

# 8. Decision Authority

Reliance policy is fork-adjacent — it governs what leaves Relatio for external work. Reserved to the **Vision Steward** (CON-0003 §5.2). Proposed on the support surface 2026-07-20 from the probe evidence; **ratified in full by Brian Noon.**

---

# 9. Review Trigger

Revisit if (a) a second-model or institutional-access channel is tested and proves an R2 mechanism, (b) an R1 verification is later found wrong (edition- discipline failure), or (c) the open-critical-edition source set proves too thin for the corpora Relatio actually cites.

---

# 10. Revision History

| Version | Date       | Status  | Description                                                                                                                                                                                                                    |
| ------- | ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1.0     | 2026-07-20 | Adopted | Initial tiered external-reliance model (R0/R1/R2), per-locus with floor roll-up; edition-discipline for R1; grounded in the 2026-07-20 live-retrieval capability probe. Constitutional source of the reliance-tier vocabulary. |

---

# End ADR-GOV-0006