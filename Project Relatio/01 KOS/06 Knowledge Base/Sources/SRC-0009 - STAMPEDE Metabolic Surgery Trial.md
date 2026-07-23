---
title: SRC-0009 - STAMPEDE Metabolic Surgery Trial
document_type: Source Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-10
category:
  - Knowledge Base
  - Source
  - Randomised Controlled Trial
source_author: "Philip R Schauer et al. (Cleveland Clinic)"
source_url: "5-year outcomes: https://doi.org/10.1056/NEJMoa1600869 (NEJM 2017) · https://pubmed.ncbi.nlm.nih.gov/28199805/"
publication_date: "2017 (5-year outcomes; earlier reports 2012, 2014)"
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - INV-0004 Metformin Discontinuation and T2D Remission
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Source
  - Type2Diabetes
  - BariatricSurgery
relationships:
  - type: supports
    target: CLM-0007
  - type: related_to
    target: SRC-0006
  - type: related_to
    target: SRC-0008
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-10
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# SRC-0009

# STAMPEDE Metabolic Surgery Trial

## Draft Source Record

---

# 1. Identification

**STAMPEDE** (Surgical Treatment And Medications Potentially Eradicate Diabetes Efficiently): a single-centre **randomised controlled trial** comparing **intensive medical therapy alone** vs intensive medical therapy **plus metabolic/bariatric surgery** (Roux-en-Y gastric bypass or sleeve gastrectomy) in patients with type 2 diabetes.

Verified this session:
- **Design:** **150 patients**, BMI 27–43, randomised across three arms (medical therapy; gastric bypass; sleeve gastrectomy).
- **Primary outcome:** proportion achieving **HbA1c ≤6.0%** (with or without diabetes medication).
- **5-year outcomes — Schauer et al., *NEJM*, 2017** (DOI 10.1056/NEJMoa1600869; PubMed 28199805): surgery produced **superior glycaemic control, greater weight loss, and fewer medications** than medical therapy; **gastric bypass outperformed sleeve gastrectomy** on durability of glycaemic benefit.
- Consequence noted in the literature: leading bodies (ADA/EASD) now endorse metabolic surgery even at moderate obesity (BMI 30–35).

> **Evidence-integrity flag:** the *exact* 5-year percentages achieving HbA1c ≤6.0% by arm (commonly cited around 29% bypass / 23% sleeve / 5% medical) were **NOT independently re-verified to the primary this session** and are therefore **not asserted as precise** here. The *direction and superiority* are verified; the specific numbers should be confirmed on the NEJM primary before quotation.

---

# 2. Source Evaluation (KOS-0003 §6)

- **Authority:** Very high — RCT in *NEJM*, major academic centre.
- **Transparency:** High — pre-specified primary outcome, arms, and follow-up.
- **Independence:** Industry-funded in part (Ethicon/J&J supported STAMPEDE) — a COI flag, though it is an RCT with hard endpoints.
- **Intent:** Inform — test surgery vs medical therapy.

---

# 3. Limitations (what this source does NOT establish)

- **Single-centre, n=150** — modest size; generalisability is limited.
- Surgery carries **operative and long-term nutritional risks** not weighed in a glycaemic-outcome headline; this record does not establish net benefit for any individual.
- Uses HbA1c ≤6.0% (a stricter glycaemic target), not identical to the 2021 consensus remission definition (off-medication requirement); "control on fewer meds" is not the same as consensus remission.
- Partial industry funding is a COI.

---

# 4. Key Content / Passages Used

- Surgery produces superior, more durable glycaemic control and weight loss than medical therapy; bypass > sleeve (CLM-0007 as the most-durable route; contextualised in FND-0004).

---

# 5. Relationships (STD-0004)

- `supports` CLM-0007.
- `related_to` SRC-0006, SRC-0008 (alternative intervention intensities for the same goal).

---

# 6. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-10|Draft|Created for RQ-0004. Direction verified; exact 5-year percentages flagged as not-re-verified.|
|0.2|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End SRC-0009
