---
title: CLM-0095 - Islam Emergence and Dating
document_type: Claim Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-23
category:
  - Knowledge Base
  - Claim
  - Islam
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0018 Islam Origins and Abrahamic Relationships
related_documents:
  - SRC-0143 Donner 2010 Muhammad and the Believers
  - SRC-0144 Berkey 2003 The Formation of Islam
  - SRC-0145 Wansbrough 1977 Quranic Studies
  - SRC-0146 Crone and Cook 1977 Hagarism
  - SRC-0147 Sinai 2017 The Quran A Historical-Critical Introduction
  - SRC-0150 al-Azmeh 2014 The Emergence of Islam in Late Antiquity
  - FND-0018 Islam Origins and Abrahamic Relationship Shape
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - Islam
  - WorldReligionsTimeline
relationships:
  - type: derived_from
    target: SRC-0143
  - type: derived_from
    target: SRC-0144
  - type: derived_from
    target: SRC-0145
  - type: derived_from
    target: SRC-0146
  - type: derived_from
    target: SRC-0147
  - type: derived_from
    target: SRC-0150
  - type: supports
    target: FND-0018
  - type: part_of
    target: INV-0018
confidence:
  - component: seventh_century_emergence
    level: 4
    label: High
  - component: confessional_crystallisation_dating
    level: 3
    label: Moderate
  - component: revisionist_redating_adjudication
    level: 2
    label: Low
  - component: tradition_type_classification_fit
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "verification-light circuit; parametric source interiors; not cleared for external reliance"
review_cycle: 6
review_date: 2027-01-23
last_reviewed: 2026-07-23
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-23
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# CLM-0095

# Islam Emergence and Dating

## Draft Claim Record

---

# Claim
> **Islam emerged as a religious tradition in the seventh century CE, in western Arabia and the adjoining late-antique Near East** — a monotheist movement associated with Muhammad, whose community formation the tradition itself dates from the *hijra* (622 CE, the epoch of the Islamic calendar) and whose ministry the traditional chronology places c. 610–632 CE. **The seventh-century emergence is firm; the point at which a distinctly *Islamic* confessional identity crystallised is not** — the mainstream range runs from "within the founder's lifetime" (the traditional account) through "somewhat later than the tradition allows" (the Donner reading) to the strong revisionist re-datings (Wansbrough; Crone & Cook), which place the text's canonisation and/or the confession's formation substantially later and outside Arabia. **The rival readings are reported at their strongest and the field's distribution is reported as the record evidences it; this claim adjudicates the crystallisation question only to the extent its thin base permits, which is not far.** Dates are claims: no false precision is asserted, and `display_range` on ENT-0015 is render-only.

---

# Element (i) — Datable Bounds

- **The century and the region are not in serious dispute.** Every work in the catalogued base — mainstream (SRC-0143 Donner, SRC-0144 Berkey, SRC-0147 Sinai, SRC-0150 al-Azmeh) *and* revisionist (SRC-0145 Wansbrough, SRC-0146 Crone & Cook) — proceeds from a **seventh-century CE emergence of an Arab monotheist movement**. The revisionist pole relocates the *text's* stabilisation and the *confession's* self-definition; **it does not relocate the movement's seventh-century origin**, and in the case of SRC-0146 it is built precisely on seventh-century contemporary non-Muslim testimony. That agreement across the field's two poles is the reason this component grades **High**.
- **The traditional chronology, reported as traditional.** Ministry c. 610–632 CE; *hijra* to Medina 622 CE; death 632 CE; the conquests from the 630s. These bounds derive from the Muslim historiographical tradition, which is **later than the events it narrates** (the *sīra* survives principally through the ninth-century recension, the annalistic corpus later still) — the source-critical problem that the revisionist current made unavoidable and that the mainstream now shares. **This record does not assert the fine-grained internal chronology**; it reports it as the tradition's chronology and grades the assertion of its precision low (see the `revisionist_redating_adjudication` component).
- **Documentary and material anchors for the formation period (live-verified this session at general-reference level; see §Verification).** The **Dome of the Rock, dated 72 AH / 691–692 CE**, carries extensive Arabic inscriptions including explicitly anti-Christological material; the **coinage reform of ʿAbd al-Malik, from 77 AH / 696–697 CE**, replaces images with the same confessional formula. These are the earliest large-scale *public* expressions of a distinctly Islamic confession that this circuit could verify. Independently, **radiocarbon dating of early Qur'anic parchment** (the Birmingham leaves, 568–645 CE at 95.4%; the Ṣanʿāʾ palimpsest reported with a majority probability before 646 CE) places written Qur'anic material very early — with the standing caveat, stated on the reporting surfaces themselves, that radiocarbon dates the **parchment**, not the writing.
- **What the bounds therefore are.** Earliest defensible emergence bound: **c. 610 CE** (the traditional beginning of the ministry). Firmer community-formation anchor: **622 CE** (*hijra*). Formation period extending through the first century AH, with **691/692 and 696/697 CE** as verified termini *ante quem* for public confessional distinctness. **`range_start_year` on ENT-0015 uses 610** — the earliest defensible bound, per STD-0002 §11 v1.11 — with 622 recorded here as the firmer alternative; the contestedness is carried by `range_uncertainty: moderate` and by this claim, **not** by a false-precision point.
- **Disposition:** `display_range` reads "7th c. CE (ministry c. 610–632 CE) – present." Graded **High (Level 4)** for the seventh-century emergence; **not Level 5** (reserved; and the internal chronology's precision is not established here).

# Element (ii) — What the Formation Context Establishes

- **It establishes a saturated monotheist environment, and that is a great deal.** Late-antique Arabia and its Near Eastern surroundings held Jewish communities (including a Judaising royal house in Ḥimyar), Syriac and Ethiopic Christian communities and Christianised Arab tribal confederations, and an indigenous Arabian cultic landscape (SRC-0150 al-Azmeh; SRC-0144 Berkey — whose framing places Islam inside the *continuous* religious history of the Near East rather than at a discontinuity). Biblical and post-biblical narrative material was demonstrably present in that environment.
- **It establishes the *mode* of that presence, at least negatively.** SRC-0149 Griffith's subject is that a **written Arabic Bible is not demonstrable before Islam** — so biblical material was present in Arabic-speaking environments **orally, liturgically, homiletically**, mediated through Syriac, Greek, and Ethiopic-speaking Christian and Jewish communities, rather than through an Arabic scriptural text. That is a finding about availability and channel.
- **It does NOT establish genealogy, and the distinction is load-bearing.** A shared milieu is compatible with hypothesis (a), (b), or (c) alike (INV-0018 §1). **Milieu is not descent.** SRC-0150 is explicit in its own record that establishing a shared late-antique environment does not establish descent; this claim adopts that limit rather than arguing past it. The relationship-type determinations are made independently in CLM-0096 and CLM-0097 under the edge-restraint rule, not inferred from context here.
- **Nor does it establish exceptionalism in the other direction.** The record equally does **not** endorse a *sui generis* framing in which Islam arrives without a context. Both the "discontinuity" and the "dissolution into late antiquity" framings are positions; SRC-0150's is recorded as a strong interpretive framing, not a consensus statement (its own source record says so).

# Element (iii) — Rival Readings (each steelmanned; distribution reported)

- **Reading 1 — the traditional chronology.** Steelmanned: a coherent, internally dense account transmitted by a community with strong transmissional institutions; corroborated at the outer edges by early Qur'anic parchment dates and by seventh-century non-Muslim testimony to an Arab monotheist movement; and it is the framework within which the documentary anchors (691/692, 696/697) sit intelligibly. **Cost:** its detailed narrative reaches us through markedly later compilations, so its *precision* is not underwritten by its *general shape*, and this record separates the two.
- **Reading 2 — Wansbrough's late crystallisation (SRC-0145).** Steelmanned: applying form-critical and literary methods, the received Qur'anic text reached stable canonical form considerably later than the tradition allows, in a sectarian milieu outside Arabia, and the historiographical corpus functions as salvation history rather than documentary record. **This is a serious methodological challenge, not a curiosity** — its insistence that the tradition's own account cannot be assumed is now ordinary practice in the field. **Cost:** SRC-0145's own record documents the standing criticisms — that the transposed form-critical apparatus does not straightforwardly fit the material, that the argument leans on absence-of-evidence for the early period, and that **manuscript and documentary findings published since 1977 bear on the dating in ways the book could not address**. The parchment dates and the 691/692 inscription this session verified are exactly that class of evidence, and they press against the strongest form of the late-crystallisation thesis.
- **Reading 3 — the *Hagarism* reconstruction (SRC-0146).** Steelmanned: setting aside the Muslim historiographical tradition as too late, and reconstructing from contemporary Syriac, Greek, Armenian, and Hebrew testimony, one arrives at an early messianic Judeo-Arab movement out of which Islam later differentiated. If sustained, this would be the strongest available warrant for a **descent** relationship to Judaism, and it is treated as such in CLM-0096 rather than dismissed. **Cost:** SRC-0146's own record carries the central methodological objection — that the non-Muslim sources privileged are **not demonstrably better informed or less tendentious** than the Muslim sources set aside — and records that **both authors are reported to have distanced themselves from the central thesis** (Cook reported 2006; Crone reported likewise, revisiting hypotheses in her later work), **from secondary and reference surfaces, not read in their originals** — a verification limit disclosed at cataloguing and honoured here.
- **Reading 4 — the Donner "Believers movement" reading (SRC-0143).** Steelmanned: the earliest movement is best understood, following its own usage, as an ecumenically-bounded monotheist and eschatological community whose confessional boundaries with other monotheists were initially porous, with a distinctly Islamic identity crystallising somewhat later. **This is a middle position and is the single most direct challenge to the crystallisation dating.** **Cost:** SRC-0143's own record notes it is influential and contested — including that its narrative may under-weight diversity already recognised in prior scholarship — and INV-0018 may not inherit it as the field's verdict.
- **Field distribution, reported under the consensus-asymmetry rule and evidenced, not asserted.** The record's evidence for the asymmetry is **in the source base itself**: SRC-0145 and SRC-0146 each state on-record, from reception surfaces read at cataloguing, that their theses are **not consensus positions**; SRC-0146 additionally records **authorial distancing**; and the four mainstream works proceed on a seventh-century Arabian emergence without adopting either revisionist reconstruction. **The field is therefore lopsided, and this record reports it as lopsided.** It does **not** follow that the revisionist pole is negligible: its source-critical challenge was absorbed into mainstream method, and SRC-0147 is catalogued precisely as the surface that takes that challenge on its merits rather than by reputation. **Neither pole is caricatured; neither is adopted as verdict.**
- **Cost to confidence, stated.** Because (a) this circuit did not read any source interior, (b) the base holds no dedicated documentary/epigraphic source, and (c) the adjudication between the traditional chronology and the re-datings turns on exactly that unread technical literature, the component grading this record's **ability to adjudicate the re-dating question** is **Low (Level 2)**. That is a statement about this record's reach, **not** a statement that the question is undecidable in the field.

---

# Claim Type (KOS-0003 §3)
**Descriptive / historical** — the emergence and dating of a religious tradition. No theological claim about revelation, prophethood, or scriptural inspiration is made or implied in any direction (bracketed, INV-0018 §2.1).

# Evidence (KOS-0003 §4)
Type: **Historical.**
- SRC-0143 (Donner), SRC-0144 (Berkey): mainstream formation and the late-antique-continuity framing.
- SRC-0147 (Sinai): the historical-critical surface on the Qur'anic text's chronology and the evidentiary state of the dating question.
- SRC-0150 (al-Azmeh): the Arabian / late-antique milieu.
- SRC-0145 (Wansbrough), SRC-0146 (Crone & Cook): the revisionist pole, **as scholarship**, with the contested standing recorded in their own source records.
- **All six interiors are parametric/unread** (each source record discloses this at §6). **No page-level claim is drawn from any of them.**
- **General-reference framing anchors live-verified this session** (Dome of the Rock 72 AH / 691–692 CE; ʿAbd al-Malik coinage reform from 77 AH / 696–697 CE; Birmingham parchment 568–645 CE at 95.4%; Ṣanʿāʾ palimpsest reported majority-probability pre-646 CE) — strong for the framing, **not** a source-interior claim.

# Evidence Evaluation (KOS-0003 §5, 0–5)
- Reliability: **4** — six academic-press works by recognised specialists; the framing anchors independently verifiable.
- Relevance: **5** — the base was catalogued for exactly this question.
- Independence: **3** — the works are independent of one another, but this circuit's *access* to them is uniform (bibliographic surfaces only), so the apparent independence is not fully exploited.
- Quality: **2** — interiors unread; no documentary/epigraphic source in the base; no Arabic- or Syriac-language scholarship.
- Limitations: establishes the century and region firmly; does **not** establish the crystallisation point, does **not** adjudicate the re-datings, does **not** underwrite the traditional chronology's internal precision.

# Source Evaluation
Six secondary works, all academic-press, authority high across the base (SRC-0143 Belknap/Harvard; SRC-0144 Cambridge; SRC-0145 Oxford/London Oriental Series; SRC-0146 Cambridge; SRC-0147 Edinburgh; SRC-0150 Cambridge). **Institutional authority is recorded as credential, not as evidence that a thesis is correct** — a discipline the revisionist records state explicitly and this claim applies **symmetrically to the mainstream works**. Intent varies from survey (SRC-0144, SRC-0147) through argued monograph (SRC-0143, SRC-0150) to methodologically revisionist (SRC-0145, SRC-0146); none is confessional in register.

# Assumptions (KOS-0003 §10)
- **Verification-light ceiling accepted, not worked around.** Where a determination would require an unread interior, the record grades down rather than asserting.
- **Traditional chronology reported, not adopted.** Its dates appear as the tradition's dates and as the field's working frame, not as this record's independent finding.
- **Metaphysical bracket, acute.** Revelation and prophethood are outside what this record adjudicates, in either direction.
- **Milieu ≠ genealogy.** The formation context is not permitted to do relationship-type work; that is CLM-0096 / CLM-0097 under the edge-restraint rule.

# Reasoning (KOS-0003 §7)
**Abductive, with an explicit convergence test.** The seventh-century emergence is affirmed because it is the one proposition on which the field's two poles converge *despite* their opposed method — convergence across adversarial method is stronger warrant than agreement within a school. The crystallisation dating is graded Moderate because the same test **fails** there: the poles diverge, and the evidence that would separate them (manuscript, documentary, epigraphic, and the technical literature on it) is precisely what this circuit did not read. Reasoning risks checked: **argument from authority** (rejected symmetrically — institutional standing is not treated as evidence for mainstream or revisionist); **argument from silence** (noted as the standing objection to Reading 2 and not reused by this record in the opposite direction); **hindsight/teleology** (the 691/692 and 696/697 anchors are termini for *public* distinctness, not evidence that distinctness began then).

# Confidence (KOS-0003 §8)
- **seventh_century_emergence — Level 4 (High):** affirmed by mainstream and revisionist poles alike; corroborated by early parchment dates and contemporary non-Muslim testimony. **Not Level 5** — reserved, and no source interior was read.
- **confessional_crystallisation_dating — Level 3 (Moderate):** the traditional, Donner, and revisionist positions genuinely diverge; the verified public-expression anchors (691/692, 696/697) bound the question without settling it.
- **revisionist_redating_adjudication — Level 2 (Low):** this record can *report* the field's distribution with in-record evidence; it cannot *adjudicate* the re-dating question on a base whose interiors are unread and which holds no dedicated documentary/epigraphic source. **A statement about this record's reach.** *(Non-temporal by construction: it grades an adjudicative capacity, not when the tradition emerged, and therefore does not govern `range_uncertainty` — STD-0002 §11 v1.11. Flagged to the Critical Reviewer as a judgement call.)*
- **tradition_type_classification_fit — Level 3 (Moderate):** `founded` is least-wrong for the historical register (see below), with two recorded strains. **Non-temporal**; does not govern `range_uncertainty`.
- **`range_uncertainty` derivation:** the emergence-dating components are `seventh_century_emergence` (Level 4) and `confessional_crystallisation_dating` (Level 3); the weakest is **Moderate → `moderate`** (STD-0002 §11 v1.11 mapping). R0 throughout.

# `tradition_type` determination and its recorded strain
- **ENT-0015 carries `tradition_type: founded`.** In the historical register the community forms around a named founder-figure within his lifetime; that is a structural descriptor about the shape of the historical account, **not** a theological or evaluative statement, and it carries no implication about the truth or origin of what was taught.
- **Strain 1 — the self-account is neither founding nor emergence.** The tradition's own account is **restoration** of a prior monotheism (*millat Ibrāhīm*), a fifth shape the four-value list (`founded`/`emergent`/`reform`/`syncretic`) does not contain. **Recorded, not force-fit**; routed to Anchor Fit Part 3. **CLM-0098's grade does not move on this** (dual-track separation).
- **Strain 2 — the late-crystallisation readings pressure toward `emergent`.** On the Donner reading and *a fortiori* on the revisionist readings, a distinct Islamic confession forms after and beyond the founder-figure, which is an emergence shape. `founded` is retained as least-wrong for the historical register with this pressure recorded; `tradition_type_classification_fit` is graded Moderate to encode it.
- **Asymmetry check against ENT-0013 (neutrality, both directions).** ENT-0013 Christianity carries `emergent` while ENT-0015 Islam carries `founded`. **This asymmetry is evidenced, not conventional, and it is not a ranking.** Christianity's founder-question is itself contested in the field (whether Jesus intended a new religion; Paul as a second founder), which is why `founded` there would assert a contested, confession-adjacent proposition. Muhammad's role as the community's founder-figure is **not** contested in the same way — SRC-0146, the base's most sceptical work, contests the movement's *character*, not the existence of an Arabian prophet-led movement. **`founded` is not a lesser category than `emergent`, and no supersessionist or apologetic reading in either direction is licensed by the pairing.**

# Limitations
- Establishes a seventh-century CE Arabian emergence at High and a bounded-but-contested crystallisation at Moderate. Does **not** fix the crystallisation point, does **not** adjudicate the revisionist re-datings, does **not** underwrite the traditional chronology's internal precision, and asserts **nothing** about the truth of the tradition's claims.
- Carries **no** relationship-type content: whether Islam descends from, was influenced by, or stands apart from Judaism and Christianity is determined in CLM-0096 and CLM-0097, not here.

# Alternative Interpretations
1. **A single-point founding date (e.g. 610 or 622 as *the* origin).** Rejected — dates are claims (ADR-GOV-0009 D3); a point would be false precision, and the render-only bound exists so the picture need not lie.
2. **Adopting Donner's later crystallisation as the record's dating.** Rejected — it is a contested middle position, and adopting it would inherit a reading the consensus-asymmetry rule requires be reported rather than inherited.
3. **Treating the revisionist re-datings as settled-wrong.** Rejected — the field's lopsidedness is reported as lopsidedness, but a minority position with a live methodological legacy is not a refuted one, and this record's own adjudicative reach is graded Low.
4. **`tradition_type: emergent`.** Considered seriously (Strain 2) and not adopted; `founded` retained as least-wrong with the tension graded and routed.

# Relationships (STD-0004)
- `derived_from` SRC-0143, SRC-0144, SRC-0145, SRC-0146, SRC-0147, SRC-0150.
- `supports` FND-0018.
- `part_of` INV-0018.
- **Warrants no lineage edge.** This claim dates the tradition; it is ENT-0015's `dating_claims` target. It does **not** warrant any `branches_from` edge, and none is drawn (CLM-0096 / CLM-0097).

# Verification (STD-0006 §7.5 — Specialist disclosure)
**Verification-light, and asymmetrically so.** All six cited source interiors are **parametric/unread**, as each source record discloses; **no page-level claim is asserted from any of them**, and the theses and criticisms reported above are taken from the source records' own §1/§3 sections (recorded at cataloguing from review and reception surfaces), not from the books. **Four general-reference framing anchors were live-verified this session** — the Dome of the Rock inscription date (72 AH / 691–692 CE), ʿAbd al-Malik's coinage reform (from 77 AH / 696–697 CE), the Birmingham Qur'an parchment radiocarbon range (568–645 CE, 95.4%), and the Ṣanʿāʾ palimpsest's reported majority probability before 646 CE — at general-reference level, **strong for the framing and not a source-interior claim**; the standing caveat that radiocarbon dates the parchment rather than the writing is carried from the reporting surfaces. **PARAMETRIC GENERAL-REFERENCE DISCLOSURE** (remediation, Critical Review – RQ-0018 Flag 2). Beyond the four anchors named above, the general-reference particulars stated in this record's own voice — the traditional ministry/*hijra*/death dates, the 630s conquests, and the lateness of the *sīra* and annalistic recensions relative to the events they narrate — are **parametric and were NOT live-verified this session**. They are reported as the tradition's chronology and as the field's working frame, they are **not** source-interior claims, and **no grade in this record rests on their precision** (the `revisionist_redating_adjudication` component exists to carry exactly that shortfall). **No Arabic-, Syriac-, or other non-English-language scholarship was consulted** (a base gap recorded at INV-0018 §2.5). Everything **R0**; **not cleared for external reliance regardless of closure.**

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-23|Draft|Created for RQ-0018 (Specialist pass), CLM A of four. Seventh-century CE Arabian emergence graded **High** on the mainstream/revisionist convergence test; confessional crystallisation **Moderate** (traditional vs Donner vs revisionist genuinely divergent, bounded by the verified 691/692 and 696/697 public-expression anchors); revisionist re-dating **adjudication** graded **Low** as a statement of this record's reach on unread interiors; `tradition_type` fit **Moderate**. Four rival readings steelmanned (traditional chronology; Wansbrough late crystallisation; *Hagarism*; Donner Believers movement), with the field's lopsidedness **evidenced from the source records' own recorded reception** rather than asserted, and neither pole caricatured or adopted. Milieu-is-not-genealogy limit stated and honoured — no relationship-type content in this claim. `tradition_type: founded` chosen as least-wrong for the historical register with both strains recorded (restorationist self-account; late-crystallisation pressure) and the ENT-0013 `emergent` asymmetry justified on evidence, not convention. `range_uncertainty` derivation documented (weakest **dating** component Moderate → `moderate`), with the non-temporal reading of two components flagged to the Critical Reviewer. Four framing anchors live-verified at general-reference level; all six source interiors parametric/unread, no page-level claim. R0; not cleared for external reliance. Pending Critical Review and structural validation.|
|0.2|2026-07-23|Draft|**Critical Review – RQ-0018 remediation (Flag 2, determinate).** Added the PARAMETRIC GENERAL-REFERENCE DISCLOSURE to §Verification: the traditional ministry/*hijra*/death dates, the 630s conquests, and the lateness of the *sīra* and annalistic recensions are parametric and were **not** live-verified this session, are not source-interior claims, and carry no grade. **No confidence level raised or lowered; no content otherwise changed.** Reviewer confirmed at this version: the (i)/(ii)/(iii) separability, the `seventh_century_emergence` Level 4 retained with explicit justification (coarse proposition + two independently live-verified material anchors), the `range_uncertainty: moderate` derivation, the `range_start_year: 610` choice, and the `founded`/`emergent` asymmetry against ENT-0013 as evidenced rather than conventional.|

# End CLM-0095
