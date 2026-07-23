---
title: SRC-0010 - ADA-EASD Consensus on Remission Definition
document_type: Source Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-10
category:
  - Knowledge Base
  - Source
  - Consensus Statement
source_author: "Matthew C Riddle et al. (ADA, EASD, Endocrine Society, Diabetes UK joint consensus)"
source_url: "https://doi.org/10.2337/dci21-0034 (Diabetes Care 2021) · https://pmc.ncbi.nlm.nih.gov/articles/PMC8929179/"
publication_date: "2021-10 (Diabetes Care 44(10):2438–2444)"
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - INV-0004 Metformin Discontinuation and T2D Remission
  - SRC-0006 DiRECT Trial Programme
  - SRC-0008 Virta Health Continuous-Care Trial
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Source
  - Type2Diabetes
  - Remission
  - Consensus
relationships:
  - type: supports
    target: CLM-0010
  - type: supports
    target: CLM-0011
  - type: related_to
    target: INV-0004
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-10
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# SRC-0010

# ADA/EASD Consensus on the Definition of Remission

## Draft Source Record

---

# 1. Identification

The **joint consensus report** of the American Diabetes Association (ADA), the European Association for the Study of Diabetes (EASD), the Endocrine Society, and Diabetes UK on the **definition and interpretation of remission in type 2 diabetes**.

Verified this session (Riddle et al., *Diabetes Care* 2021;44(10):2438–2444; DOI 10.2337/dci21-0034):
- **Definition of remission:** **HbA1c <6.5% (48 mmol/mol)** measured **at least 3 months after cessation of glucose-lowering pharmacotherapy** (i.e. sustained ≥3 months in the absence of medication).
- **Timing of the confirming measurement** depends on the intervention: pharmacotherapy — ≥3 months after stopping the drug; **lifestyle — ≥6 months after starting the intervention plus 3 months off medication**; surgery — ≥3 months post-procedure plus 3 months off medication.
- **Remission is not cure:** a state "in which diabetes is not present but which nonetheless requires continued observation because hyperglycaemia frequently recurs."
- **Ongoing monitoring:** HbA1c (or equivalent) **at least yearly**, plus continued screening for diabetes complications.

---

# 2. Source Evaluation (KOS-0003 §6)

- **Authority:** Very high — the governing multi-society consensus; this is the definitional standard the field uses.
- **Transparency:** High — reasoning and criteria explicit.
- **Independence:** High — a definitional/normative document, not a product study.
- **Intent:** Inform/standardise terminology and clinical interpretation.

---

# 3. Limitations (what this source does NOT establish)

- It is a **definitional/interpretive** document — it does **not** provide efficacy data for any intervention, nor remission *rates*.
- It sets a terminological standard; individual clinical practice and payer/coding use may differ.
- It explicitly does not settle long-term outcomes of the remission state.

---

# 4. Key Content / Passages Used

- The HbA1c <6.5% off-medication ≥3-month definition (used across the KB to score every remission claim consistently; anchors the "remission vs reversal" disambiguation in INV-0004 §2).
- "Requires continued observation because hyperglycaemia frequently recurs"; yearly monitoring (used by CLM-0011).

---

# 5. Relationships (STD-0004)

- `supports` CLM-0010, CLM-0011.
- `defines` the remission endpoint used to interpret SRC-0006 and SRC-0008.
- `related_to` INV-0004.

---

# 6. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-10|Draft|Created for RQ-0004. Definition and monitoring statements verified via the PMC full text this session.|
|0.2|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End SRC-0010
