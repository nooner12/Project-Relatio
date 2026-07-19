---
title: SRC-0080 - Adamatzky 2022 Language of Fungi Electrical Spiking
document_type: Source Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-19
source_author: "Adamatzky, Andrew (2022)"
source_url: "'Language of fungi derived from their electrical spiking activity', Royal Society Open Science 9(4):211926; doi:10.1098/rsos.211926"
publication_date: "2022-04-06"
category:
  - Knowledge Base
  - Source
  - Primary Study
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
related_documents:
  - INV-0012 Mycelial Networks and Fungal Cognition
  - CLM-0061 Electrical Signaling Datum and Language Overreach
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Source
  - ElectricalSignaling
  - FungalLanguage
relationships:
  - type: supports
    target: CLM-0061
  - type: part_of
    target: INV-0012
---

# SRC-0080

# Adamatzky 2022 — "Language of Fungi Derived from Their Electrical Spiking Activity"

## Draft Source Record

---

# 1. Identification
Andrew Adamatzky (Unconventional Computing Laboratory, UWE Bristol), "Language of fungi derived from their electrical spiking activity," *Royal Society Open Science* 9(4):211926 (2022). Records extracellular electrical potential in four species (*Omphalotus nidiformis*, *Flammulina velutipes*, *Schizophyllum commune*, *Cordyceps militaris*), groups spike trains into "words," and argues the patterns resemble features of human language. **In this KB it is the flashpoint source for CLM-0061: its measured spiking is admissible as a descriptive datum, but its central "language" claim is the contested interpretation held apart and graded much lower.**

# 2. Source Evaluation (KOS-0003 §6)
- **Authority:** Mixed. Adamatzky is a serious, prolific researcher in unconventional computing; the venue (*R. Soc. Open Sci.*) is peer-reviewed. But the paper is **exploratory/speculative by its own framing** and heavily contested (SRC-0081).
- **Transparency:** Good on data/methods (electrode recordings, spike-detection algorithm, information-theoretic word-length analysis); the **interpretive leap from spike statistics to "language" is where transparency of inference weakens.**
- **Independence:** The author has a standing research interest in fungal computing, which predisposes toward a "language/computation" reading — a motivated-reasoning vector to name.
- **Intent:** To explore whether spike-train structure carries language-like statistical properties; explicitly speculative.

# 3. Limitations (what this source does NOT establish)
- Establishes **spike-train statistics and species-specific patterning** (a datum); does **NOT** establish that fungi have a language, communicate propositional content, or process information cognitively. The "words/lexicon" are an analyst-imposed statistical construct, not demonstrated semantics.
- Critics (SRC-0081) argue some recorded fluctuations may be **non-biological noise/artifacts**, and that the patterns show **no similarity to actual properties of language** — so even the datum's biological status is partly contested at the margins.

# 4. Key Content / Passages Used
- Spike characteristics are **species-specific**; reported spike duration ~1–21 h and amplitude ~0.03–2.1 mV (note: **hour-scale**, vs. the millisecond-scale of Olsson & Hansson 1995 — SRC-0079).
- A fungal "lexicon" of up to ~50 "words," with a core of ~15–20 most-frequent "words," derived from grouping spike trains by inter-spike structure.

# 5. Relationships (STD-0004)
- `supports` CLM-0061 (as the datum; the interpretation is graded separately).
- `contrasts_with` (in prose) SRC-0081 (the language critique) and SRC-0079 (timescale).
- `part_of` INV-0012.

# 6. Verification (STD-0006 §5.7 / §7.5)
**Live-verified this session (strong on citation; the primary PDF page returned HTTP 403).** Title, author, venue (*R. Soc. Open Sci.* 9(4):211926, 1 April 2022), the four species, and the "lexicon up to 50 words / core 15–20" claim confirmed via the Royal Society landing page metadata, the arXiv preprint (2112.09907), and multiple independent news/blog summaries. The specific figures (spike duration 1–21 h; amplitude 0.03–2.1 mV) were read from the publisher's search-result abstract summary, **not from a full read of the primary article this session** (the DOI page returned 403) — flagged accordingly.

# 7. Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-19|Draft|Created for RQ-0012. The contested "language" source; datum admissible, interpretation graded low in CLM-0061. Citation verified strong; figures from abstract summary (primary PDF 403).|

# End SRC-0080
