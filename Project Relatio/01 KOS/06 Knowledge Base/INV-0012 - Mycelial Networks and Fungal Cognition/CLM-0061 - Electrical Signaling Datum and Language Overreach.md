---
title: CLM-0061 - Electrical Signaling Datum and Language Overreach
document_type: Claim Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-19
category:
  - Knowledge Base
  - Claim
  - Electrophysiology
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0012 Mycelial Networks and Fungal Cognition
related_documents:
  - SRC-0079 Olsson Hansson 1995 Action Potential-Like Activity in Fungi
  - SRC-0080 Adamatzky 2022 Language of Fungi Electrical Spiking
  - SRC-0081 Blatt et al 2024 Does Electrical Activity in Fungi Function as a Language
  - SRC-0082 Buffi et al 2025 Electrical Signaling in Fungi Review
  - FND-0012 Mycelial Network Signaling and the Bounds of Fungal Cognition
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - ElectricalSignaling
  - DatumVsInterpretation
relationships:
  - type: derived_from
    target: SRC-0079
  - type: derived_from
    target: SRC-0080
  - type: derived_from
    target: SRC-0081
  - type: derived_from
    target: SRC-0082
  - type: supports
    target: FND-0012
  - type: part_of
    target: INV-0012
confidence:
  - component: electrical_signaling_datum
    level: 3
    label: Moderate
  - component: language_information_encoding
    level: 1
    label: Very Low
reliance_tier: R0
reliance_note: "unassessed floor; predates verification-pass procedure."
---

# CLM-0061

# Fungal Mycelia Exhibit Propagating, Stimulus-Sensitive Electrical Potential Fluctuations ("Spikes") — a Real but Methodologically Fragile DATUM Held at Moderate — Which Does NOT Establish the Separate, Contested INTERPRETATION That These Spikes Constitute a "Language" or Encode Information (Very Low); the Two Are Graded Apart

## Draft Claim Record

> **This claim exists to hold a datum apart from an interpretation (INV-0012 §3.1, the operative discipline).** It carries **two confidence levels**: one for the measured phenomenon, a much lower one for the "language" reading. They must not be collapsed.

---

# Claim
> **(Datum, Moderate):** Fungal hyphae and mycelia produce **spontaneous, propagating electrical potential fluctuations ("spikes"/oscillations) that change in response to stimuli** (chemical/physical), a phenomenon reported independently since at least Olsson & Hansson (1995). **(Interpretation, Very Low):** the further claim that these spikes constitute a **"language," encode/transmit information, or communicate propositional content** (Adamatzky 2022) is **not established** — critics attribute much of the signal to noise/artifact and find **no** language-like structure, and the field's own reviewers stress the measurements are hard to replicate.

---

# Claim Type (KOS-0003 §3)
**Descriptive datum** (electrical spiking exists and is stimulus-sensitive) **+ flagged interpretive over-reach** (the "language"/information-encoding reading). Explicitly two claim-modes at two confidences.

---

# Evidence (KOS-0003 §4)
Type: **Empirical** (electrophysiology) **+ critical review**.
- **SRC-0079 (Olsson & Hansson 1995):** action-potential-like spikes in *Pleurotus*/*Armillaria* hyphae, **stimulus-sensitive** (activity changed when mycelium contacted wood). Reported (via secondary summaries) amplitude ~5–50 mV, duration ~20–500 ms, ~0.5–5 Hz. **This is the independent grounding of the datum.**
- **SRC-0080 (Adamatzky 2022):** species-specific spike trains across four species grouped into a "lexicon" of up to ~50 "words"; reported spike duration ~1–21 h, amplitude ~0.03–2.1 mV. **The datum (spike statistics) is admissible; the "language" framing is the contested interpretation.**
- **SRC-0081 (Blatt et al. 2024):** the "language" reading is **premature and unsupported**; fluctuations are **likely partly non-biological noise/artifact**; patterns show **no** similarity to properties of language.
- **SRC-0082 (Buffi et al. 2025, review):** fungal electrical signaling is **real but poorly characterized**; recordings are hard to replicate on microscopic hyphae — counsels caution on both the datum's precise character and any strong interpretation.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: 3 — the *existence* of stimulus-sensitive electrical activity is independently attested (Olsson 1995 → Adamatzky → others), **but** methods are fragile (electrode artifacts; Buffi review) and the reported signal parameters differ by **orders of magnitude** across studies (ms vs. hours), so the phenomenon is real yet ill-defined.
- Relevance: 5 — central to the "signal internally" part of the primary question and to the neural analogy.
- Independence: 4 — Olsson (1995) and Adamatzky are independent; Blatt and Buffi supply independent critical/ review perspectives.
- Quality: 2 for the *language* interpretation (analyst-imposed statistics, contested); 3–4 for the *datum*.
- Limitations: establishes stimulus-linked electrical activity; establishes **nothing** about semantic content, communication, or cognition.

---

# Source Evaluation
The four sources bracket the question well: a pre-hype 1995 datum (Olsson), the provocative interpretation (Adamatzky), a sharp rebuttal (Blatt et al.), and a balanced 2025 review (Buffi et al.). Adamatzky's standing interest in "fungal computing" is a motivated-reasoning vector on the interpretation; the datum survives without him (Olsson 1995), which is why it holds at Moderate.

---

# Assumptions (KOS-0003 §10)
- **Methodological:** extracellular electrode recordings on hyphae reflect genuine biological potentials — **partly contested** (artifact risk is real; Blatt, Buffi).
- **Semantic:** "spike"/"signal" is used descriptively; "language"/"word" are treated as claims under examination, not adopted vocabulary.

---

# Reasoning (KOS-0003 §7)
**For the datum: inductive** from independent recordings. **For rejecting the strong interpretation: abductive** — "noise/artifact + analyst-imposed pattern" is a better-supported explanation of the "lexicon" than "language," given the absence of language-like structure and the artifact evidence. **Risks checked:** *datum→interpretation slide* (the whole point — named and enforced); *pattern-imposition / apophenia* (named — a word-length statistic can be computed on noise); *argument from evocative labelling* (named — calling spikes "words" does not make them words); *anthropomorphic projection* (named).

---

# Confidence (KOS-0003 §8)
- **Datum — Level 3 (Moderate):** fungi exhibit stimulus-sensitive propagating electrical activity. Not higher, because the signal is methodologically fragile and inconsistently characterized across labs (ms vs. hour timescales; artifact concerns). Not lower, because it is independently attested since 1995.
- **"Language"/information-encoding interpretation — Level 1 (Very Low):** actively contested, plausibly artifactual in part, with no demonstrated language-like structure or semantic function.
- **Headline for the claim as framed — Level 3 (Moderate)**, because the claim's assertion is precisely the *pairing* (real datum + unsupported interpretation); its Moderate rests on the datum, and it explicitly denies the high-confidence "language" reading. *(Headline-selection rule for two-level split claims — shared with CLM-0063, stated there per Critical Review – RQ-0012 F-2: the headline sits at the sub-level carrying the claim's principal assertive burden. This claim is a **hold-the-datum** claim (its burden is "spikes are real"; it merely denies "language"), so it headlines at the **higher** sub-level (Moderate). CLM-0063, a **deny-the-strong-narrative** claim, headlines at its **lower** sub-level (Low). Same rule, opposite direction.)*

---

# Limitations
- Licenses "fungi show stimulus-sensitive electrical spiking (Moderate)"; **does NOT** license "fungi have a language," "fungi communicate information electrically," or any cognitive reading.
- The datum itself is not yet a clean, single, well-defined signal class — an honest weakness.

---

# Alternative Interpretations
1. **Adamatzky's "language."** Steelmanned: species-specificity and non-random spike structure are genuinely intriguing and could, in principle, index internal state changes. Rejected as *established* at Very Low: no language-like structure, artifact-plausible, analyst-imposed lexicon.
2. **Pure artifact/noise (strong deflation).** Steelmanned via Blatt et al.: some signal is surely artifact. Not fully accepted: Olsson's stimulus-coupling (activity changes on contact with wood) is hard to explain as pure artifact, so *some* real biological electrical response is likely — hence the datum sits at Moderate, not Very Low.
3. **Real signaling, non-linguistic (middle).** Accepted as most probable: electrical activity plausibly participates in coordination (cf. CLM-0062) without being a language — the position the claim occupies.

---

# Relationships (STD-0004)
- `derived_from` SRC-0079, SRC-0080, SRC-0081, SRC-0082.
- `contrasts_with` (Adamatzky interpretation vs. Blatt critique — held within this claim).
- `supports` FND-0012.
- `part_of` INV-0012.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-19|Draft|Created for RQ-0012. Two-level claim: datum (stimulus-sensitive electrical spiking) Level 3 (Moderate), independently attested since Olsson & Hansson 1995; "language"/information-encoding interpretation (Adamatzky) Level 1 (Very Low), contested (Blatt et al.) and cautioned (Buffi et al. review). Datum≠interpretation enforced per §3.1. Pending review/validation.|
|0.2|2026-07-21|Draft|epistemic-field backfill, Stage 3|
|0.1a|2026-07-19|Draft|**Remediated per Critical Review – RQ-0012 F-2 (documentation only; no level change).** Added a cross-note to the Confidence section pointing to the shared two-level headline-selection rule (stated in full in CLM-0063): this is a hold-the-datum claim, so it headlines at the higher sub-level (Moderate) — the same rule that lands CLM-0063 at its lower sub-level. No confidence changed.|

# End CLM-0061
