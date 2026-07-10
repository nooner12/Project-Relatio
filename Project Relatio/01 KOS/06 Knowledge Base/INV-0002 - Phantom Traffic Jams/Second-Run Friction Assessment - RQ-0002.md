---
title: Second-Run Friction Assessment - RQ-0002
document_type: Review Report
version: 1.0
status: Adopted
created: 2026-07-09
category:
  - Knowledge Operating System
  - Review
  - Architecture Evaluation
parent_documents:
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - STD-0006 Review & Validation Standard
related_documents:
  - INV-0002 Phantom Traffic Jams
  - Pressure Test Report - RQ-0001
  - KOS-0012 Knowledge Object Model
tags:
  - ProjectRelatio
  - Review
  - PressureTest
  - Convergence
---

# Second-Run Friction Assessment — RQ-0002

## Version 1.0

## Adopted Review Report

---

# 1. Purpose

This is the **measurement** the second workflow was run to obtain. RQ-0001 exposed friction and drove the KOS-0012 + Templates build. RQ-0002 (a *different domain* — complexity science — and a *different shape* — explanatory, not comparative) tests two things:

1. **Convergence** — with the object model and templates in place, did friction drop?
2. **Generality** — does the architecture work outside comparative religion?

The verdict decides the strategic question CLAUDE.md cares about: **is the architecture converging (earning its complexity) or bloating?**

---

# 2. Prior Findings — Did They Recur?

| Finding (from RQ-0001) | Recurred in RQ-0002? | Notes |
|---|---|---|
| F-1 no Investigation type | **No** | INV-0002 conformant from the start (KOS-0012). |
| F-2 no Finding type | **No** | FND-0002 created directly. |
| F-5 no templates | **No** | INV/SRC/CLM/FND all authored from TPL-0001…0004. Faster, and structurally consistent with run 1 by construction. |
| F-6 two required-field sets | **No** | The two-layer model (KOS-0012) made "what goes where" unambiguous. |
| **F-3 source metadata (ancient texts)** | **No — and this is informative** | Modern scientific sources (SRC-0003/0004) filled `source_author`/`source_url`(DOI)/`publication_date` cleanly. **Confirms F-3 was specific to ancient/anonymous sources, not a general schema flaw.** |
| F-4 typed relations in frontmatter | **Yes** | Still expressed in prose. General, unresolved gap (as expected). |
| F-7 KB folder convention | **Eased** | Reused the `INV-NNNN - …/` precedent from run 1; no longer had to invent it. Still not formally standardized. |
| F-9 identifier registry | **Yes (minor)** | Assigned SRC-0003/0004, CLM-0003/0004, INV-0002, FND-0002 by manually continuing the sequence. No collision, but still no registry. |

**Four of the four high-severity findings did not recur.** The two that recurred (F-4, F-9) are the pre-known Medium/Low gaps.

---

# 3. New Findings

| ID | Finding | Severity |
|---|---|---|
| **F-10** | **No structured field for quantitative evidence.** KOS-0003 §5's 0–5 scale grades evidence *quality* but has nowhere to record sample size, effect size, replication count, or numeric results — which empirical/causal claims (CLM-0003/0004) carry and interpretive claims (RQ-0001) did not. Partly compensated by KOS-0003 §9 "Consensus Evaluation," which this run *did* use (RQ-0001 barely did). | Medium |

Only **one** new finding — and it is Medium, domain-specific to empirical work, and partially mitigated by an existing component (§9). It is not a structural gap.

**Positive generality signals:** two Kernel components unused in RQ-0001 were exercised cleanly here — **KOS-0006 (Systems Modeling)** framed the phenomenon (emergence), and **KOS-0003 §9 (Consensus)** fit empirical claims naturally. The architecture reached into parts of itself that the first question never touched, without strain.

---

# 4. Friction Delta (summary)

```
RQ-0001:  9 findings  (4 High, 4 Medium, 1 Low)   — first contact, nothing built
RQ-0002:  1 new finding (Medium) + 2 recurring known-Medium/Low gaps
```

The trend is unambiguous: **friction fell sharply**, the resolved items **stayed resolved**, one domain-specific gap surfaced (already the expected behavior — a new domain finds a new edge), and the architecture **generalized** to empirical science.

---

# 5. Verdict

> **Converging, not bloating.**

Evidence: (a) every RQ-0001 high-severity finding was closed by a *single* Kernel doc + one layer and did not return; (b) a genuinely different domain and inquiry shape produced only one modest new finding; (c) previously-idle components (KOS-0006, KOS-0003 §9) did real work, indicating the existing architecture was already broad enough to absorb the new domain rather than needing new scaffolding. This is the healthy signature: the system is being *used into* its existing capacity, not being *expanded to chase* hypothetical needs.

---

# 6. Recommendations

Do **not** build reflexively. The open items are now well-characterized and can wait for accumulated need:

1. **F-10 (quantitative evidence):** do not act on one instance. If a *third* empirical investigation also strains against it, add optional quantitative-evidence fields to the Claim structure (a KOS-0003 minor revision) — the same demonstrated-need discipline that justified KOS-0012.
2. **F-4 (typed relations) and F-9 (registry):** batch these into a single future "operational hardening" pass; neither blocks research.
3. **Highest-value next step remains use:** a *third* investigation (ideally a third distinct domain, or one requiring an Entity record — the one research type not yet exercised) would further map the architecture's real edges.

---

# 7. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Friction measurement for the second workflow (RQ-0002); verdict: converging, not bloating|

---

# End Second-Run Friction Assessment — RQ-0002
