---
title: CLM-0087 - Zoroastrian Origins and Root Status
document_type: Claim Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-21
category:
  - Knowledge Base
  - Claim
  - Iranian Religions
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0016 Iranian Religious Family Origins and Branching
related_documents:
  - SRC-0104 Shahbazi 1977 Traditional Date of Zoroaster Explained
  - SRC-0105 Hintze 2015 Zarathustras Time and Homeland
  - CLM-0056 The Dating Problem Is Load-Bearing
  - FND-0016 Origins and Branching of the Iranian Religious Family
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - Zoroastrianism
  - IranianReligions
relationships:
  - type: derived_from
    target: SRC-0104
  - type: derived_from
    target: SRC-0105
  - type: depends_on
    target: CLM-0056
  - type: supports
    target: FND-0016
  - type: part_of
    target: INV-0016
confidence:
  - component: emergence_dating
    level: 3
    label: Moderate
  - component: family_root_status
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "verification-light review; not cleared for external reliance"
review_cycle: 9
review_date: 2027-04-21
last_reviewed: 2026-07-21
---

# CLM-0087

# Zoroastrian Origins and Root Status

## Draft Claim Record

---

# Claim
> Zoroastrianism is the **root tradition** of the Iranian religious family: the earliest of the five and the reference point from which the family's later branching is described. Its **emergence cannot be dated absolutely** — the traditional "258 years before Alexander" (6th c. BCE) date is a demonstrable late-Sasanian back-calculation, while the competing early dating (Old Avestan/Gathic material c. 1500–1000 BCE) rests on linguistic archaism, not on any dated text — so its origin is reported as **contested-and-reconstructed, not fixed**. This claim inherits its dating posture from INV-0011 CLM-0056 (the evidence-class asymmetry) and does not re-derive it.

---

# Element (i) — Emergence Dating
- **The traditional date is a late construct.** SRC-0104 (Shahbazi 1977) establishes that the "258 years before Alexander" figure — placing Zoroaster in the 6th c. BCE — is a Sasanian-era scholastic back-calculation, not preserved historical memory. Scholarship accordingly rejects a 6th-century Zoroaster. (Shahbazi's negative result does **not** by itself supply an alternative date.)
- **The competing early dating is indirect.** SRC-0105 (Hintze 2015) reports the comparative-linguistic case placing the Old Avestan (Gathic) material in roughly the second millennium BCE (commonly given as c. 1500–1000 BCE) on grounds of its archaism and closeness to Rigvedic Sanskrit. This is a **relative, not absolute** chronology; the conversion to calendar dates carries wide margins and the question is genuinely unsettled.
- **Inheritance (layer-bound).** The governing fact — that Zoroastrian early dating is *reconstructed, not attested* — is INV-0011 **CLM-0056** ("The Dating Problem Is Load-Bearing," Level 4). This claim is **bounded by CLM-0056** and does not exceed it: it inherits the asymmetry, applies it to the family-root question, and grades the *specific emergence date* lower (Moderate) than the *asymmetry itself* (High), because no absolute anchor exists.
- **Disposition:** emergence contested; no false precision. `display_range` on ENT-0008 reads "2nd–early 1st millennium BCE (contested)" as a render-only summary; the truth and the contestedness live here.

# Element (ii) — Descent Relationship
- **Zoroastrianism is the family root — it carries NO `branches_from` edge.** It is not modelled as descending from another tradition within this investigation's scope. Its own antecedent (the common Old Iranian / Indo-Iranian religious inheritance shared with Vedic religion) lies **outside the Iranian religious family as bounded here** and is noted in prose only, not edged.
- **What bounds the root claim:** "root" is a temporal-and-genealogical *reference position*, secure to the degree that (a) Zoroastrianism is the earliest attested member of the family and (b) the later four traditions relate to it (as offshoot, heterodoxy, or syncretic incorporation). Both hold on the surveyed base; the residual uncertainty is the dating margin (element (i)), which is why the grade is Moderate rather than higher.
- `tradition_type` on ENT-0008 is **`founded`** — Zoroastrianism attributes itself to a prophet-founder (Zarathustra), to whom the Gathas are ascribed; the contestation concerns *when/whether he is historically datable*, not whether the tradition is founder-attributed. (That founded/emergent tension is recorded for the Anchor Fit Assessment.)

# Element (iii) — Rival Reading (steelmanned)
- **Strongest rival — faithful-transmission maximalism (Boyce/Hultgård type).** A conservative priesthood may have preserved archaic doctrine verbatim across a millennium of oral transmission, so late written attestation need not mean late origin; on this reading Zoroastrianism's genuine antiquity (and a firmer early date) is defensible. **Survives, partially:** it keeps genuine antiquity live and is why the early dating is not dismissed — but per CLM-0056 it is an *argument*, not attestation, and it does not dissolve the reconstruction-not-attestation asymmetry. **Cost:** it cannot convert the relative chronology into an absolute one, so it does not raise the specific-date grade above Moderate.
- **Second rival — the traditional 6th-c.-BCE date as genuine memory.** Rejected on SRC-0104: the figure is a demonstrable calculation artifact.

---

# Claim Type (KOS-0003 §3)
**Descriptive / historical** — about the emergence and genealogical position of a tradition, not a theological claim about its truth (bracketed).

# Evidence (KOS-0003 §4)
Type: **Historical / philological.**
- SRC-0104 (Shahbazi): the traditional date is a late back-calculation (live-verified citation; strong bibliographic verification).
- SRC-0105 (Hintze): the comparative-linguistic early dating and its indirectness (parametric; weak verification, disclosed).
- Inherited: CLM-0056 (INV-0011) — the reconstruction-not-attestation asymmetry (Level 4).

# Consensus (KOS-0003 §9)
- Evidence strength: **Moderate** — the *negative* result (traditional date is late) is secure; the *positive* early dating is a reasoned majority view, not a demonstrated result.
- Consensus strength: **Moderate-to-high on the negative, Moderate on the positive.** The unsettledness of the absolute date is itself a consensus.

# Assumptions (KOS-0003 §10)
- **Family-boundary assumption:** the Old Iranian / Indo-Iranian substrate is treated as *outside* the family under study, so Zoroastrianism functions as the family root. This is a scoping decision, recorded as such.
- **Metaphysical bracket:** the tradition's own truth claims are set aside; only historical emergence and genealogical position are at issue.

# Confidence (KOS-0003 §8)
- **emergence_dating — Level 3 (Moderate):** the contested-and-reconstructed dating picture is well-understood; no absolute date is establishable; bounded by CLM-0056.
- **family_root_status — Level 3 (Moderate):** secure as the earliest/reference member on the surveyed base, bounded by the dating margin. **No Level 4 or 5** — verification-light posture (SRC-0105 parametric), R0.

# Limitations
- Establishes emergence-as-contested and root position; does **not** fix an absolute date, and does not adjudicate the tradition's antecedent Indo-Iranian religion.

# Relationships (STD-0004)
- `derived_from` SRC-0104, SRC-0105.
- `depends_on` CLM-0056 (INV-0011, layer inheritance; one-directional into a closed record — INV-0011 unmodified).
- `supports` FND-0016; warrants ENT-0008 (root; no lineage edge).
- `part_of` INV-0016.

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-21|Draft|Created for RQ-0016 (Specialist pass). Root tradition; emergence contested (traditional 6th-c.-BCE date rejected per SRC-0104; early linguistic dating indirect per SRC-0105); dating inherited from CLM-0056, not re-derived. `tradition_type: founded` with the founded/emergent tension flagged for Anchor Fit. No `branches_from` (root). Verification-light; R0; not cleared for external reliance. Pending Critical Review and structural validation.|

# End CLM-0087
