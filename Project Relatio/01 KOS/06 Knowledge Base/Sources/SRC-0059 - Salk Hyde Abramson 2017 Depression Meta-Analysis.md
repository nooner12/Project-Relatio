---
title: SRC-0059 - Salk Hyde Abramson 2017 Depression Meta-Analysis
document_type: Source Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-15
source_author: "Salk, R. H., Hyde, J. S., & Abramson, L. Y. (2017)"
source_url: "Gender differences in depression in representative national samples: Meta-analyses of diagnoses and symptoms. Psychological Bulletin 143(8):783-822; https://doi.org/10.1037/bul0000102"
publication_date: "2017"
category:
  - Knowledge Base
  - Source
  - Meta-Analysis
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - INV-0010 Psychosocial Stressor Onset Divergence
  - CLM-0044 Depression Onset-Timing Divergence
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Source
  - Depression
  - SexGenderConstructs
relationships:
  - type: supports
    target: CLM-0044
  - type: part_of
    target: INV-0010
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-15
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# SRC-0059

# Salk, Hyde & Abramson 2017 — Gender Differences in Depression: Meta-Analyses of Diagnoses and Symptoms

## Draft Source Record

---

# 1. Identification
Salk, R. H., Hyde, J. S., & Abramson, L. Y. (2017), "Gender differences in depression in representative national samples: Meta-analyses of diagnoses and symptoms," *Psychological Bulletin* 143(8):783–822, DOI 10.1037/bul0000102. Two large meta-analyses of **representative national samples** (diagnoses: 65 studies; symptoms: 95 studies; ~1.7–1.9 million people across 90+ nations). Reports the **age at which the female-preponderant depression ratio emerges** and its trajectory. Citation and headline figures verified this session via the PMC full text (PMC5532074) and the *Psychological Bulletin* record.

# 2. Source Evaluation (KOS-0003 §6)
- **Construct-provenance code: `CONFLATED`.** The meta-analysis compares rates by the recorded **female/male category** (an administrative/self-report sex label) and never assesses a biological mechanism, nor measures gender as socialization. It applies sex labels to epidemiological data without drawing the sex-vs-gender distinction. It therefore **documents that rates diverge by recorded category and when**; it **cannot** attribute that divergence to biological sex on a mechanism (operative rule §3.1). Justification: the primary variable is a demographic female/male tag on prevalence data.
- **Authority:** High — flagship meta-analysis in the top review journal in psychology, by senior authorities on the topic.
- **Transparency:** High — effect sizes by age reported (d ≈ .02 ages 8–11, .14 at 12, .26 at 13, .38 at 14; diagnosis OR = 2.37 at 12, peaking OR = 3.02 at 13–15; overall diagnosis OR = 1.95, symptom d = 0.27).
- **Independence:** High — aggregates many independent national datasets; not tied to a single research program's paradigm.
- **Intent:** Establish the magnitude and developmental timing of the female/male depression gap across representative samples.

# 3. Limitations (what this source does NOT establish)
- **No mechanism.** It does not test whether the divergence is driven by biology, gendered socialization, differential exposure to stressors, or reporting/measurement artifact. It is agnostic by design.
- **Category, not construct.** "Female/male" is a recorded demographic tag; the paper does not assess pubertal status, hormones, gender role, or identity — so it cannot license a sex-attributed causal claim.
- **Aggregation smooths heterogeneity.** Cross-national pooling can mask setting-specific patterns; diagnosis and symptom analyses used different instrument classes (structured interview vs self-report scales).
- **Prevalence, not onset per se.** It tracks the age at which the ratio diverges in cross-sectional/period data, a strong proxy for onset-timing divergence but not incident-onset dating in every included study.

# 4. Key Content / Passages Used
- The female/male depression gap is near-zero pre-adolescence and **emerges around ages 12–13**, reaching a roughly 2:1 (up to ~3:1 for diagnoses) ratio by mid-adolescence.
- Effect sizes rise monotonically across ages 12–16, then the gap stabilizes into adulthood.
- The emergence is **earlier than the once-cited age-15 figure** — detectable by age 12.

# 5. Relationships (STD-0004)
- `supports` CLM-0044 (the depression onset-timing divergence — its strongest epidemiological anchor).
- `part_of` INV-0010.

# 6. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-15|Draft|Created for RQ-0010. Psychol. Bull. 143(8):783–822, DOI 10.1037/bul0000102 — verified via PMC5532074. Construct-provenance: `CONFLATED` (epidemiological female/male category, no mechanism assessed) — documents timing divergence, cannot support a sex-attributed causal claim.|
|0.2|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

# End SRC-0059
