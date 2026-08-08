---
title: CLM-0114 - Small-Screen and Handheld Reading Prescriptions
document_type: Claim Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-08-08
category:
  - Knowledge Base
  - Claim
  - Design Psychology
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0021 Reading Performance Evidence
related_documents:
  - SRC-0179 Legge and Bigelow 2011 Does Print Size Matter for Reading
  - SRC-0191 Delgado et al 2018 Reading Media Meta-Analysis
  - SRC-0192 Bababekova et al 2011 Font Size and Viewing Distance of Smartphones
  - SRC-0193 Apple Human Interface Guidelines Typography
  - FND-0021 Reading Performance Evidence Synthesis
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - ReadingPerformance
  - SmallScreen
relationships:
  - type: derived_from
    target: SRC-0179
  - type: derived_from
    target: SRC-0191
  - type: derived_from
    target: SRC-0192
  - type: derived_from
    target: SRC-0193
  - type: supports
    target: FND-0021
  - type: part_of
    target: INV-0021
confidence:
  - component: c_prescriptive_approach
    level: 3
    label: Moderate
  - component: c_stated_rationale
    level: 3
    label: Moderate
  - component: c_measured_performance_evidence
    level: 2
    label: Low
  - component: c_documented_costs_failure_modes
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "the vendor artifact live-read (zero cited measurement); the viewing-distance measurement at abstract level (journal platform migration blocked full text this session, disclosed); no direct small-screen reading-performance study in-base at accessible surfaces; not cleared for external reliance"
review_cycle: 6
review_date: 2027-02-08
last_reviewed: 2026-08-08
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-08-08
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# CLM-0114

# Small-Screen / Handheld vs Desktop Reading (CLM-F)

## Draft Claim Record

---

# Claim
> **The small-screen typography prescriptions in this base are platform-vendor assertions without cited measurement: the live-read vendor artifact states per-platform default and minimum text sizes (iOS 17 pt default / 11 pt minimum, through tvOS 29/23 pt) and weight rules with zero cited studies anywhere on the read page — the citation trail terminates in assertion at the artifact — while the measured leg of the territory in-base is real but narrow: viewing-distance measurement (mean working distances of 36.2 cm for text messages and 32.2 cm for internet viewing, closer than the conventional 40 cm near-work assumption, at abstract level) and the read visual-angle frame under which any physical size prescription is a proxy for angular size at an assumed distance. No source in this base measures reading performance for small-screen typography at prescribed sizes at any surface accessible this session; the read media meta-analysis's device contrast (computers vs handhelds) is explicitly non-significant.**

---

# Element (i) — The Prescriptive Approach (as stated in the practice literature)

- **The platform-vendor artifact (SRC-0193, live-read):** the per-platform default/minimum table — iOS/iPadOS 17 pt default, 11 pt minimum; macOS 13/10; tvOS 29/23; visionOS 17/12; watchOS 16/12 — plus "avoid light font weights" at small sizes, Dynamic Type scales, and per-size tracking tables. The most widely applied small-screen prescription set.
- The tvOS row's far larger values embody an unstated viewing-distance adjustment across platforms — recorded as a fact about the table's structure (the page does not state the distance reasoning).

# Element (ii) — The Stated Rationale

- SRC-0193 (read): "Use font sizes that most people can read easily. People need to be able to read your content at various viewing distances and under a variety of conditions" — the stated register is reader-capability and viewing-distance variation, plus testing guidance ("Test legibility in different contexts"). **No study, measurement, or research reference appears anywhere on the read page — the trail terminates in assertion at the artifact** (the executed-trace discipline, applied at cataloguing and re-confirmed at circuit).
- **The angular frame (SRC-0179, read):** the psychophysics states the rationale structure the vendor table implies — physical print size maps to performance only through visual angle at a viewing distance (the read review's 40 cm standard-distance conversions make the dependence explicit).

# Element (iii) — Measured Human-Performance Evidence (including explicit bounded absence)

- **Viewing-distance measurement (SRC-0192, interior unread; abstract-establishable):** mean working distances of **36.2 cm for text messages and 32.2 cm for internet viewing** on handheld phones — closer than the conventional 40 cm near-work distance, shortening the effective visual angle of any fixed physical size. Single study; no replication record in this base.
- **The angular conversion base (SRC-0179, read):** the fluent range (0.2°–2° x-height) and critical print size (0.15°–0.3°) are distance-relative; the read review's conversions at 40 cm are the measured frame against which any handheld-distance shift matters.
- **Device contrast in the read media meta (SRC-0191, read):** the computers-vs-handhelds difference is explicitly **non-significant** ("although they did not reach significance, the results suggest stronger media differences on computers than on hand-held devices") — carried at the source's own framing.
- **EXPLICITLY ABSENT at the surfaces accessible this session:** any measured reading-performance study of small-screen typography at the prescribed sizes (11 pt minimums, Dynamic Type scales); any eye-tracking or scanning-behavior measurement for handheld reading in-base; any population sub-element (aging or young readers) for small screens. The unread interiors (SRC-0192's full text; the vendor documentation beyond the read page) are the disclosed holes these absence claims do not cover.

# Element (iv) — Documented Costs and Failure Modes (from the sources; not inferred)

- **The vendor's own documented failure modes (SRC-0193, read):** text truncation at large accessibility sizes ("Keep text truncation to a minimum as font size increases"); multicolumn readability loss at large sizes ("Multicolumn text can also be less readable at large sizes"); light-weight legibility failure ("Ultralight, Thin, and Light font weights … can be difficult to see, especially when text is small"); 3D-text depth cost in visionOS ("The more visual depth text characters have, the more difficult they can be to read"). The artifact documents the failure modes of its own type system — as assertions, in the same uncited register as its prescriptions, and they are carried as documentation, not measurement.
- **The closer-distance fact (SRC-0192, abstract level):** working distances closer than the 40 cm convention are the documented condition under which fixed-size prescriptions deliver smaller visual angles than their print-derived rationale assumes. (The performance consequence of that shift is **not** asserted — see the reflexive section for the withheld inference.)

---

# Claim Type (KOS-0003 §3)
**Descriptive** — what the vendor prescribes and on what stated basis, what the narrow measured leg establishes, and the bounded absence of direct performance measurement. No element is normative.

# Evidence (KOS-0003 §4)
Type: **Empirical** (SRC-0192, SRC-0179, SRC-0191) and **Documentary** (SRC-0193).
- SRC-0193 — live-read this session (twice across prep and circuit). SRC-0179, SRC-0191 — interiors read.
- SRC-0192 — abstract level: the journal's platform migration (LWW → Wiley) broke the catalogued full-text URL this session; no accessible full-text located. Disclosed.

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: **3** — the vendor artifact and the angular frame are read; the one direct handheld measurement is abstract-level.
- Relevance: **5** — exactly the small-screen prescription and measurement territory.
- Independence: **4** — vendor, optometry measurement, psychophysics review, and media meta are four distinct provenances.
- Quality: **2** — the territory's direct performance question is unmeasured in-base; the measured leg is narrow (distances, not performance).
- Limitations: the absence claims bind accessible surfaces; the vendor's internal research, if any, is invisible to this base.

# Source Evaluation
The vendor artifact carries its recorded commercial stake and contributes (i)/(ii) plus its own documented failure modes; the measurement sources are peer-reviewed academic work.

# Assumptions (KOS-0003 §10)
- **Assertion-trail findings bind the read page**, not the vendor's unpublished practice: "no cited measurement" is a fact about the artifact's surface, and the record does not claim the vendor performed no research.
- **Absence claims bind accessible surfaces only** (bounded in place above).
- **The vendor's documented failure modes are documentation, not measurement** — carried in (iv) under exactly that label.

# Reasoning (KOS-0003 §7)
**Descriptive reporting.** Risk checked: **inference from distance to performance** — the closer-distance finding invites "therefore small-screen sizes underperform," which no in-base source measures; the inference was withheld at write time and recorded in the reflexive section instead. Risk: **vendor-bashing register** — "asserted without cited measurement" is kept strictly descriptive, with the artifact's own testing-guidance register recorded fairly.

# Confidence (KOS-0003 §8)
- **c_prescriptive_approach — Level 3 (Moderate):** the prescription table read directly, twice.
- **c_stated_rationale — Level 3 (Moderate):** the stated register read directly; the zero-citation fact re-confirmed at circuit.
- **c_measured_performance_evidence — Level 2 (Low):** the element's direct question — measured small-screen reading performance at prescribed sizes — is EMPTY at accessible surfaces, and what exists is narrow (abstract-level distances; a read angular frame; an explicitly non-significant device contrast). The one absence-dominated (iii) in this investigation, graded Low **with the access cap contributing** (SRC-0192's full text was blocked by a platform migration) — recorded for the reflexive section's GB-2026-058 taxonomy as the contrast case to CLM-D.
- **c_documented_costs_failure_modes — Level 3 (Moderate):** the vendor's own read failure-mode statements plus the abstract-level distance fact.
- **No Level 4 or 5. Everything R0.**

# Limitations
- Asserts nothing about the vendor's internal research; nothing about SRC-0192's interior beyond its abstract; nothing about small-screen eye-tracking literature outside this base; no application decision.
- **May not be cited outside Relatio or for any external reliance (R0), regardless of INV-0021's closure state.**

# Alternative Interpretations
1. **"The vendor's testing-guidance register is itself an evidence practice."** Partly conceded — "test your text" delegates measurement to the designer rather than citing it; recorded as the artifact's honest register, which still leaves the prescribed values uncited.
2. **"The non-significant device contrast shows handheld reading is fine."** Refused — a non-significant trend in a comprehension meta is not evidence of equivalence, and the source frames it as a suggestion only.
3. **"The absence of small-screen performance studies in-base reflects the field."** Not asserted — the base is sixteen sources; the absence binds accessible surfaces, and the catalog deliberately admitted only one direct handheld measurement.

# Relationships (STD-0004)
- `derived_from` SRC-0179, SRC-0191, SRC-0192, SRC-0193.
- `supports` FND-0021.
- `part_of` INV-0021.

# Verification (STD-0006 §7.5 — Specialist disclosure)
**Mixed access, disclosed per source:** SRC-0193 live-read (prep and circuit); SRC-0179 and SRC-0191 interiors read; SRC-0192 abstract-level — the catalogued LWW full-text URL now 301-redirects to the Wiley journal home (platform migration) and no accessible full text was located this session (disclosed; the catalog record's "full-text page" expectation did not survive the migration). Everything **R0; not cleared for external reliance regardless of closure.**

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-08-08|Draft|Created for RQ-0021 (Specialist pass), CLM-F of six. Four separable elements: (i) the vendor per-platform size/weight table, live-read (Moderate); (ii) the stated capability/distance register with the zero-citation trail re-confirmed (Moderate); (iii) the absence-dominated element — abstract-level viewing distances (36.2/32.2 cm), the read angular frame, the explicitly non-significant device contrast, and bounded absence of any direct small-screen performance measurement (Low, access-contributing — the GB-2026-058 contrast case); (iv) the vendor's own documented failure modes (truncation, multicolumn, light weights, 3D depth) + the closer-distance fact, with the performance inference withheld to the reflexive section (Moderate). No Level 4/5; R0. Pending Critical Review and structural validation.|

# End CLM-0114
