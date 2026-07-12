---
title: SRC-0037 - Simmons Nelson Simonsohn 2011 False-Positive Psychology
document_type: Source Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-12
category:
  - Knowledge Base
  - Source
  - Simulation Study
source_author: "Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011)"
source_url: "Psychological Science 22(11):1359–1366; https://doi.org/10.1177/0956797611417632"
publication_date: "2011"
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - INV-0007 Formal Constraints in Knowledge Systems
  - CLM-0027 Analytic Flexibility Inflates Error
  - SRC-0038 Szollosi et al 2020 Is Preregistration Worthwhile
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Source
  - ResearcherDegreesOfFreedom
  - Preregistration
relationships:
  - type: supports
    target: CLM-0027
  - type: contrasts_with
    target: SRC-0038
---

# SRC-0037

# Simmons, Nelson & Simonsohn 2011 — False-Positive Psychology

## Draft Source Record

---

# 1. Identification
Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011), "False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant," *Psychological Science* 22(11):1359–1366. Combines Monte-Carlo simulation with two demonstration experiments to show that undisclosed **"researcher degrees of freedom"** dramatically inflate false-positive rates, and proposes **disclosure requirements** (a formal reporting constraint) as the remedy. It is the primary empirical anchor for the *value* of formal constraints in research methodology.

# 2. Source Evaluation (KOS-0003 §6)
- **Authority:** High — peer-reviewed in a leading psychology journal; among the most-cited papers of the "credibility revolution"; authors are recognised methodologists.
- **Transparency:** High — simulation assumptions, the four degrees of freedom tested, and the proposed requirements are all stated explicitly and are reproducible.
- **Independence:** High — academic; the conclusion is self-critical of the authors' own field.
- **Intent:** Inform / reform methodology.

# 3. Limitations (what this source does NOT establish)
- The headline **61% combined false-positive rate** is a **simulation result** under specified assumptions (four degrees of freedom exploited together); it demonstrates *capacity for inflation*, not the *actual* base rate of false positives in the published literature.
- Evidence is drawn from **experimental psychology**; the general lesson (analytic flexibility inflates error) transfers to other empirical fields by analogy, but the magnitude is field-specific.
- It establishes that **disclosure/constraint helps**; it does **not** establish that preregistration is costless or that it improves *theory* (a point contested by SRC-0038).

# 4. Key Content / Passages Used
- Four common researcher degrees of freedom examined: flexibility in (a) dependent variables, (b) sample size / optional stopping, (c) covariates, (d) reporting subsets of conditions.
- **Combining all four** degrees of freedom raised the false-positive rate to **61%** (against a nominal 5% α) — "a researcher is more likely than not" to obtain a significant result from noise. *(61% combined figure verified this session via multiple secondary summaries of Table 1/Table 3; individual per-degree rates fell in the **~8–13%** band — e.g., optional stopping ≈7.7%, adding gender as a covariate ≈11.7% — reported here as approximate, not re-derived to the decimal this session.)*
- Proposed remedy: **six author requirements + four reviewer guidelines** — disclosure of all conditions, all measures, sample-size rules, and excluded observations — i.e., a low-cost **formal reporting constraint**.

# 5. Relationships (STD-0004)
- `supports` CLM-0027 (analytic flexibility inflates error; disclosure/constraint is a demonstrated remedy).
- `contrasts_with` SRC-0038 (the preregistration-critique anchor); together they frame the value/limit tension of formal constraints.

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-12|Draft|Created for RQ-0007. Citation (Psych Science 22(11):1359–1366, 2011), the four degrees of freedom, and the combined 61% false-positive rate verified this session via SAGE/SSRN records and multiple secondary summaries. Per-degree decimal rates reported as approximate (not re-derived to the decimal this session); full-text PDFs located but not machine-readable.|
|0.2|2026-07-12|Draft|Post-review remediation (Critical Review - RQ-0007, #7): corrected the per-degree band "~9–13%" → "~8–13%" (optional stopping ≈7.7%, gender covariate ≈11.7% — the latter re-confirmed by the reviewer this session). Combined 61% and citation unchanged (verified).|
|0.1.1|2026-07-12|Draft|ROLE-0001 structural validation (SA-001): added the reciprocal `contrasts_with` SRC-0038 edge (typed block + `related_documents` + §5) to complete the symmetric peer relationship SRC-0038 already asserted one-directionally. Non-semantic reciprocity correction; no content change.|

# End SRC-0037
