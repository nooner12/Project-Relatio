---
title: CLM-0027 - Analytic Flexibility Inflates Error
document_type: Claim Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-12
category:
  - Knowledge Base
  - Claim
  - Research Methodology
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0007 Formal Constraints in Knowledge Systems
related_documents:
  - SRC-0037 Simmons Nelson Simonsohn 2011 False-Positive Psychology
  - CLM-0032 Formalization Biases Toward Exploitation and Can Ossify
  - FND-0007 Value and Failure of Formal Constraints
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - ResearcherDegreesOfFreedom
  - Preregistration
relationships:
  - type: derived_from
    target: SRC-0037
  - type: contrasts_with
    target: CLM-0032
  - type: supports
    target: FND-0007
  - type: part_of
    target: INV-0007
---

# CLM-0027

# Undisclosed Analytic Flexibility Inflates Error, and Formal Disclosure/Protocol Constraints Are a Demonstrated Remedy

## Draft Claim Record

---

# Claim
> In research, **undisclosed flexibility in data collection and analysis ("researcher degrees of freedom") sharply inflates false-positive/error rates**, and **formal constraints — pre-specified protocols, disclosure/reporting standards, preregistration — are a demonstrated remedy** for this specific failure. This is the strongest concrete case for the *value* of formal constraints in an evolving knowledge system.

---

# Claim Type (KOS-0003 §3)
**Causal** (analytic flexibility → inflated false positives; constraint → reduced inflation), resting on a **descriptive/quantitative** simulation demonstration.

---

# Evidence (KOS-0003 §4)
Type: **Empirical** (Monte-Carlo simulation + two demonstration experiments).
- **SRC-0037 (Simmons, Nelson & Simonsohn 2011):** exploiting four common researcher degrees of freedom (choice of dependent variable, optional stopping/sample size, covariates, reporting subsets of conditions) **combined** raised the false-positive rate to **61%** against a nominal 5% α (verified this session). The proposed remedy is a formal disclosure constraint (six author requirements + four reviewer guidelines).
- Per-degree rates (each of the four exploited alone) fell in the **~8–13%** band against the nominal 5% (e.g., optional stopping ≈7.7%; adding gender as a covariate ≈11.7%) — reported as approximate; the **combined 61%** is the verified load-bearing figure.
- Corroborating context (widely reported, not separately catalogued here): the same concern motivated the subsequent preregistration / Registered Reports movement across psychology, biomedicine (clinical-trial registration), and beyond.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 4** — a rigorous, reproducible simulation plus demonstrations, peer-reviewed and among the most-cited methods papers of the decade.
- **Relevance: 5** — directly about the value of a formal constraint (disclosure/protocol) against a named failure.
- **Independence: 3** — the strongest single anchor is one paper; the *phenomenon* is independently corroborated across fields, but I catalogue one primary source here.
- **Quality: 4** — high; the 61% is a simulation under stated assumptions (its purpose is to show *capacity*, not measure the literature's actual false-positive base rate).
- **Limitations:** Establishes that flexibility *can* inflate error and disclosure *can* curb it; does **not** establish the real-world false-positive rate, does not prove preregistration is costless, and does not show constraints improve *theory* (contested by SRC-0038 / CLM-0032).

---

# Consensus (KOS-0003 §9)
- Evidence strength: **High** that undisclosed flexibility inflates error.
- Consensus strength: **High** — this is mainstream in open-science/methods reform; the *inflation* claim is near-universally accepted even by critics of preregistration.
- Relationship: strongly supported; disagreement is about the *cure's* scope, not the *disease*.

---

# Source Evaluation
SRC-0037: high authority, high transparency, academic, self-critical intent. The 61% combined figure was verified this session via multiple secondary summaries of the paper's tables; per-degree decimal rates are reported as approximate (not re-derived to the decimal this session).

---

# Assumptions (KOS-0003 §10)
- **Methodological:** the simulated degrees of freedom represent real analytic practice — well supported.
- **Epistemological:** false-positive control is a legitimate proxy for research quality — largely true, but SRC-0038 argues it is insufficient (constrains procedure, not theory).

---

# Reasoning (KOS-0003 §7)
**Deductive-within-simulation + inductive generalisation.** Given the statistical setup, exploiting multiple analytic choices necessarily multiplies the chance of a spurious "hit"; disclosure/pre-specification removes those hidden choices. **Risks checked:** *overgeneralisation* (named — the 61% is capacity, not prevalence); *false precision* (per-degree decimals flagged as approximate); *confirmation bias toward "constraints are good"* (checked — the claim is bounded to the specific failure the evidence addresses, and the limits are stated).

---

# Confidence (KOS-0003 §8)
**Level 4 (High)** that undisclosed analytic flexibility inflates error and that disclosure/protocol constraints demonstrably reduce that specific inflation. Not Level 5: rests on one primary anchor as catalogued, the 61% is a simulation figure, and the *sufficiency* of such constraints for research quality is contested.

---

# Limitations
- Speaks to *error control*, one value of constraints; not to codification, coordination, or legitimacy values.
- The remedy addresses procedure-level flexibility, not theory quality or question quality.
- Field-specific magnitude; the mechanism generalises, the numbers do not.

---

# Alternative Interpretations
1. **"The real false-positive rate isn't that high, so the constraint is over-sold."** Partly conceded — 61% is capacity, not prevalence — but even critics accept undisclosed flexibility inflates error; refined, not rejected.
2. **"Preregistration fixes the wrong thing (procedure, not theory)."** A genuine counter (SRC-0038); it limits the *sufficiency* of the constraint, not the reality that flexibility inflates error. Carried forward into CLM-0032/CLM-0033, not used to reject this claim.

---

# Relationships (STD-0004)
- `derived_from` SRC-0037.
- `supports` FND-0007.
- `contrasts_with` CLM-0032 (the over-reliance/ossification limit).
- `part_of` INV-0007.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-12|Draft|Created for RQ-0007. Simmons 2011 combined 61% figure verified this session; per-degree decimals flagged approximate. Level 4 for the value-of-constraint case, bounded to error control.|
|0.2|2026-07-12|Draft|Post-review remediation (Critical Review - RQ-0007). #7: added the per-degree band ~8–13% (optional stopping ≈7.7%, gender covariate ≈11.7%) as approximate. #9: encoded the load-bearing `contrasts_with CLM-0032` edge in frontmatter relationships + related_documents. Short title (STD-0001 §10). No confidence change — remains Level 4.|

# End CLM-0027
