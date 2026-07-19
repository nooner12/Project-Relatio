---
title: DRAFT - Historical-Evidence Scale Discrimination Test - Governance Memo
created: 2026-07-19
tags:
  - ProjectRelatio
  - Draft
  - Governance
  - ScaleDiscriminationTest
---

# DRAFT — Governance Memo: A Historical-Evidence Typology for Project Relatio

> **STATUS: WORKING DRAFT. Not a Knowledge Object, not a Finding, not a governance decision.**
> Prepared 2026-07-19 by a Claude Code session executing an owner handoff brief (claude.ai → Claude Code transfer). It has **not** been through the OPS-0003 circuit. It proposes; it decides nothing. Companion evidence: `DRAFT - Historical-Evidence Scale Discrimination Test - Coded Sample` (same folder).

---

## 1. Question under test

The house ★-scale (★★★ meta-analysis/SR · ★★☆ RCT/cohort · ★☆☆ observational · ◇◇◇ theoretical) is an intervention-evidence typology. The hypothesis: applied to historical claims it fails to discriminate, and a five-band historical-evidence typology — **H-a** contemporaneous primary text · **H-b** archaeological/epigraphic attestation · **H-c** near-contemporary secondary account · **H-d** later tradition attributing backward · **H-e** modern scholarly reconstruction — discriminates where it collapses. Per owner instruction, each claim was additionally coded on the vault's native canonical confidence scale (KOS-0003 §8, Level 0–5), to locate *where* the problem lives: in the vault, or only at the export boundary.

Test material: 15 discrete datable/attributable claims from a single family — the Iranian religions (Zoroastrianism, Zurvanism, Manichaeism, Mazdakism, Yazidism) — chosen because the family concentrates extinction, contested dating, and hostile-source-only attestation. No corpus was built; no INV opened.

---

## 2. Discrimination verdict: **YES — with a locating qualification**

| Scale | Bands used (of available) | Spread across 15 claims |
|---|---|---|
| House ★-scale | 1 of 4 | 0 / 0 / 0 / **15** — total collapse |
| Proposed historical scale | **5 of 5** | 2 / 2 / 5 / 2 / 4 |
| Native Level 0–5 | 4 of 6 | L5:1 · L4:7 · L3:5 · L2:2 |

1. **The house scale flattens completely.** All 15 claims land in ◇◇◇ — and strictly they are not *codable* on a study-design typology at all; ◇◇◇ is merely the honest floor. The hypothesis's premise is confirmed on the sample.
2. **The historical scale discriminates fully.** All five bands are populated; no band takes more than a third of the sample. The hypothesis is confirmed on the sample.
3. **The qualification that changes the picture: the vault does not have this problem.** The native confidence scale discriminates fine (four bands used). The collapse exists only where the house ★-vocabulary is applied — i.e., **at the export boundary (STD-0006 Appendix A), not inside the vault**. KOS-0003 §8 rates *confidence*, which is domain-general; the ★-scale encodes *study-design typology*, which is domain-specific to intervention evidence.
4. **A sharpened problem statement falls out of the data.** The live defect is not "historical claims can't be graded" — they can, natively. It is that the authorized crosswalk exports, e.g., a Level 4 historical claim (Darius's Mazda-worship would export ★★☆) into a vocabulary whose receiving-stream semantics are "RCT / prospective cohort" — a **semantically false signal** for a claim resting on royal epigraphy. The crosswalk's tiers translate confidence honestly (no tier gained), but the ★-glyphs *connote study designs* the underlying evidence does not have.
5. **Secondary result:** the historical typology and native confidence are **orthogonal, non-redundant axes** (H-e claims span L2–L4; an H-a text ranks below an H-b inscription in confidence). So the proposed scale is a *typology that feeds confidence assessment* — a peer of the house ★-scale's role in its own stream — not a rival confidence scale.

Sample-size caveat: 15 claims, one family, one coder, no adversarial review. Sufficient to answer the narrow discrimination question; insufficient for adoption without a governed pass.

---

## 3. Governance classification of the proposed change

**Tier: Standards/Operations. Not content. Not a Baseline change — with the argument made explicit, as required:**

- **Baseline §3.3 freezes the "single canonical confidence scale: Level N (Label)."** A historical-evidence typology is a **different kind of object** from a confidence scale: it classifies *kinds of evidence* (what sort of thing attests the claim), not *degrees of warranted belief*. The sample data demonstrate the difference empirically — historical band does not predict native Level (§2.5). Adopting the typology would leave KOS-0003 §8 untouched as the *only* confidence vocabulary; every claim would still carry exactly one native Level. **The §3.3 freeze is therefore not implicated** — on the same logic already embedded in Appendix A, where the house ★-typology coexists with the canonical scale without threatening its singularity.
- **The freeze would be implicated** only if the typology were positioned as a second *confidence* scale, or as bands that replace/override Levels on Knowledge Objects. This memo does not propose that, and any adoption should expressly forbid it.
- **It is nonetheless owner-reserved.** New or amended Standards are reserved to the owner (Baseline §3.6; ROLE-0001 §4.2; ROLE-0005). Appendix A amendments are additionally owner-reserved by its own change-control clause (A.4). Nothing here can be enacted by a session.

## 4. Governance route to adoption (if pursued)

> **Owner decision recorded 2026-07-19 (Backlog v1.18): route (c) → (a).** The typology is **not** authored now. The trigger for enactment is a real full-circuit historical investigation exercising the candidate scale in use; at that point STD-0008 + the Appendix A domain qualifier are authored as owner-reserved changes. The steps below are retained as the route that decision selected.

1. **Log a Governance Backlog item** — done: **GB-2026-027** logged 2026-07-19 with owner authorization (Backlog v1.17), superseding the candidate text in §6 below (retained for the record).
2. **Owner (Vision Steward, ROLE-0005) decides** whether the demonstrated need justifies formalization, per the merit principle (ADR-GOV-0002).
3. **If adopted, the natural home is a new Standards document — STD-0008** (next per the Identifier Registry), plausibly seated in the existing empty `02 Standards/02 Evidence Standards/` folder — defining the historical-evidence typology, its coding rules, and its relation to KOS-0003 §8. Alternatively (lighter): an amendment extending **STD-0006 Appendix A** with domain-qualified export semantics. Either path is a governed standards change requiring documentation, review, and version update (STD-0006 §10), recorded as an ADR if it touches settled interpretation.
4. **Validation:** the scale itself, once drafted, should be exercised on at least one full-circuit investigation in a historical domain before Adopted status — evidence-before-formalization, per the Baseline.

## 5. What the change would add and touch

**Adds:** one evidence-typology (five bands) applicable to historical/textual-attestation claims; coding rules; a rule for how typology informs (but never substitutes for) native Level assignment.

**Touches:** the **export boundary only** — Appendix A would need a companion rule so that historical-domain findings crossing into the house stream either (a) carry a domain qualifier (e.g., "★★☆ — historical-evidence basis, see H-band") or (b) map from H-bands via a separate authorized mini-crosswalk. Without this, the existing mapping will keep emitting study-design connotations that are false for historical claims — the actual defect the test isolated.

**Displaces: nothing.** The native confidence scale remains sole and canonical; the house ★-scale remains external vocabulary; no existing Knowledge Object requires migration (INV-0001's two claims are the only historical-domain claims in the KB, and they carry native Levels already).

**Rights posture: unchanged.** No license or rights grant is added or implied by this test or this memo; the repository remains all-rights-reserved.

## 6. Candidate Backlog entry (for owner to approve logging)

> **GB-2026-027 — Historical-evidence typology (second grading scale) for historical claims**
> **Type:** Standards proposal (owner-reserved). **Origin:** owner-directed discrimination test, 2026-07-19 (see `00 Inbox` drafts).
> **Statement:** The house ★-scale collapses on historical claims (15/15 → ◇◇◇ on a 15-claim Iranian-family sample) while a five-band historical-evidence typology discriminates fully (2/2/5/2/4) and the native KOS-0003 §8 scale discriminates adequately (1/7/5/2). The defect is located at the export boundary (STD-0006 Appendix A semantics), not in the vault's canonical scale. Proposal: adopt the typology as STD-0008 (or an Appendix A extension) with domain-qualified export semantics. Baseline §3.3 argued not implicated (typology ≠ confidence scale); adoption owner-reserved regardless (§3.6, A.4).
> **Status:** Proposed — awaiting Vision Steward decision.

---

## 7. Verification disclosure

Per the spirit of STD-0006 §7.5: this memo and its coded sample are **verification-light**. Six load-bearing citations were live-verified during the session (Shahbazi 1977; Henning 1942; MacKenzie 1979/80; Crone 1991; the Cao'an 1339 donor inscription; ʿAdī ibn Musāfir d. 1162 / Kreyenbroek 1995). The remaining citations are standard works cited from parametric knowledge and not re-located this session. No source is invented; no claim was left needing an UNSOURCED flag. Nothing here is cleared for external reliance; promotion of any part requires the full circuit with live re-verification.

---

*End of draft governance memo. Decision rests with the owner (ROLE-0005).*
