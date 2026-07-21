---
title: CLM-0089 - Manichaean Origins and Descent
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
  - SRC-0111 Cologne Mani Codex
  - SRC-0113 MacKenzie 1979-80 Manis Sabuhragan
  - SRC-0114 Henning 1942 Manis Last Journey
  - SRC-0116 Lieu 1992 Manichaeism in the Later Roman Empire and Medieval China
  - FND-0016 Origins and Branching of the Iranian Religious Family
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - Manichaeism
  - IranianReligions
relationships:
  - type: derived_from
    target: SRC-0111
  - type: derived_from
    target: SRC-0113
  - type: derived_from
    target: SRC-0114
  - type: derived_from
    target: SRC-0116
  - type: supports
    target: FND-0016
  - type: part_of
    target: INV-0016
confidence:
  - component: emergence_dating
    level: 3
    label: Moderate
  - component: syncretic_character
    level: 3
    label: Moderate
  - component: zoroastrian_as_infamily_parent
    level: 2
    label: Low
reliance_tier: R0
reliance_note: "verification-light review; not cleared for external reliance"
review_cycle: 6
review_date: 2027-01-21
last_reviewed: 2026-07-21
---

# CLM-0089

# Manichaean Origins and Descent

## Draft Claim Record

---

# Claim
> Manichaeism was **founded by Mani in the 3rd century CE** (the best-dated emergence in the family) as a deliberately **syncretic** universal religion. Its descent is **multi-parent**: Mani's own formative matrix was a Jewish-Christian baptist (Elchasaite) community, and the tradition drew on Christian, Iranian-Zoroastrian dualist, and (in its eastward diffusion) Buddhist elements. Within the Iranian family, the edgeable relationship is to Zoroastrianism, qualifier **`syncretic-descent`** — but this captures only **one** of several parents, and arguably not the primary one, so the single-target edge **understates the syncretism and risks overstating Zoroastrianism's parental role.** That strain is routed to the Anchor Fit Assessment.

---

# Element (i) — Emergence Dating
- **Founded, 3rd c. CE.** SRC-0111 (Cologne Mani Codex) places Mani's birth near Seleucia-Ctesiphon in the early 3rd c. CE and records his upbringing in, and break from, a Jewish-Christian baptist (Elchasaite) community. SRC-0113 (MacKenzie) edits the surviving Middle Persian *Šābuhragān*, the work Mani composed for Shapur I — anchoring his public ministry to Shapur I's reign (from c. 240 CE). SRC-0114 (Henning) reconstructs Mani's death under Bahram I.
- **The founding era is firm; the precise death year is not.** SRC-0114 records that the death year is contested (274 vs 277 CE both defended); the *event* (death in imprisonment under Bahram I) is far better supported than any exact date. Sources for the biography are in-group and hagiographically shaped (SRC-0111 §2: "Independence: None").
- **Disposition:** 3rd c. CE emergence, well-grounded relative to the family; precise dates within it carry the in-group-source caveat. Graded Moderate (the verification-light posture and hagiographic sourcing forbid higher). `display_range` on ENT-0009: "3rd c. CE."

# Element (ii) — Descent Relationship
- **Multi-parent syncretic descent.** Mani's *personal* religious matrix was the Elchasaite Jewish-Christian baptist community (SRC-0111) — a **non-Iranian** source. Manichaeism additionally incorporated (a) Christian/gnostic material, (b) **Iranian-Zoroastrian dualism** (the two-principle cosmic framework, and the Middle Persian *Šābuhragān* addressed to the Zoroastrian Sasanian court, SRC-0113), and (c) Buddhist elements in its eastward diffusion (SRC-0116).
- **In-family edge:** `branches_from` ENT-0008 (Zoroastrianism), qualifier **`syncretic-descent`** — warranted by the incorporation of Iranian-Zoroastrian dualism. **The Christian/Jewish-Christian and Buddhist parents are noted in prose only, not edged** (they lie outside the Iranian family; those entities do not exist — §2.4).
- **Honest caveat (load-bearing, Anchor Fit):** because `branches_from` takes a **single target**, edging Manichaeism → Zoroastrianism alone represents a *partial* descent as if it were *the* descent, and risks implying a Zoroastrian primacy the evidence does not support (the Elchasaite matrix is at least as formative). The edge is drawn because the Zoroastrian input is real and is the only in-family parent; the confidence component `zoroastrian_as_infamily_parent` is graded **Low** precisely to encode this partiality. `tradition_type` on ENT-0009 is **`founded`** (Mani deliberately founded it); the co-applying `syncretic` value is recorded as an Anchor Fit tension.

# Element (iii) — Rival Reading (steelmanned)
- **Rival A — Manichaeism as essentially Christian-gnostic, the Iranian element cosmetic.** On this reading the *Šābuhragān* is missionary accommodation to a Zoroastrian court, not genuine descent, and a `branches_from` Zoroastrianism edge is a category error. **Survives, partially** — it correctly identifies the risk of overstating the Iranian parent; it is the reason the in-family-parent component is Low and the qualifier is `syncretic-descent` (incorporation) rather than `reform`/`schism` (which would imply Zoroastrianism as *the* parent). **Cost:** it understates the real, structural role of two-principle dualism in Manichaean cosmology, which is more than veneer.
- **Rival B — Manichaeism as a wholly independent founded religion, not a "branch" of anything.** Steelmanned: Mani presented a new universal revelation superseding all prior prophets. **Survives** as a caution against reading `branches_from` as "subordinate to." **Cost:** the family/timeline program models incorporation-descent explicitly via the `syncretic-descent` qualifier, so a partial-descent edge is not a claim of subordination; the founded-and-syncretic character is captured, not denied.

---

# Claim Type (KOS-0003 §3)
**Descriptive / historical** — emergence and genealogical composition of a founded tradition; metaphysics bracketed.

# Evidence (KOS-0003 §4)
Type: **Historical (in-group primary + philological secondary).**
- SRC-0111 (Cologne Mani Codex): Elchasaite upbringing, early-3rd-c. birth; in-group hagiography, no independence (parametric; weak, disclosed).
- SRC-0113 (MacKenzie): the *Šābuhragān* for Shapur I; Mani's self-authored scripture in Middle Persian (live-verified citation; strong bibliographic verification).
- SRC-0114 (Henning): death under Bahram I; death year contested (live-verified citation; strong).
- SRC-0116 (Lieu): westward (Roman) and eastward (Chinese/Buddhist-contact) diffusion (parametric; weak).

# Consensus (KOS-0003 §9)
- Evidence strength: **Moderate** — Manichaeism is comparatively well-documented (self-authored scriptures survive in fragments), but the biography rests on in-group hagiography.
- Consensus strength: **High** that Manichaeism is a 3rd-c. founded syncretic religion; **contested** on the relative weight of its several sources (hence the Low in-family-parent grade).

# Assumptions (KOS-0003 §10)
- **Single-parent edge limitation accepted and flagged:** the in-family edge represents one of several parents; the out-of-family parents are prose-only (§2.4).
- **Metaphysical bracket** held; the truth of Mani's revelation is not at issue.

# Confidence (KOS-0003 §8)
- **emergence_dating — Level 3 (Moderate):** 3rd-c. CE founding firm relative to the family; in-group sourcing and verification-light posture cap it.
- **syncretic_character — Level 3 (Moderate):** the deliberately syncretic composition is well-established.
- **zoroastrian_as_infamily_parent — Level 2 (Low):** that Zoroastrianism specifically is *the* in-family parent is partial — the primary matrix (Elchasaite) is out-of-family; the single-target edge overstates. **No Level 4/5.** R0.

# Limitations
- Establishes a 3rd-c. founded syncretic tradition with a real Iranian-Zoroastrian component; does **not** establish Zoroastrianism as its primary source, and does not resolve the relative weighting of its parents.

# Relationships (STD-0004)
- `derived_from` SRC-0111, SRC-0113, SRC-0114, SRC-0116.
- `supports` FND-0016; **warrants the ENT-0009 → ENT-0008 `branches_from` (`syncretic-descent`) edge** (partial, in-family only).
- `part_of` INV-0016.

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-21|Draft|Created for RQ-0016 (Specialist pass). Founded 3rd c. CE (Cologne Codex, Šābuhragān, Henning); deliberately syncretic; multi-parent with the primary (Elchasaite Jewish-Christian) matrix out-of-family. In-family `branches_from` Zoroastrianism qualifier `syncretic-descent` (scaffold hypothesis confirmed as the qualifier) — but single-target edge understates syncretism; `zoroastrian_as_infamily_parent` graded Low to encode the partiality; flagged for Anchor Fit. `tradition_type: founded` with `syncretic` co-applying (Anchor Fit tension). Both rivals steelmanned. Verification-light; R0; not cleared for external reliance. Pending Critical Review and structural validation.|

# End CLM-0089
