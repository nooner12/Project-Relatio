---
title: INV-0018 - Islam Origins and Abrahamic Relationships
document_type: Investigation Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-23
category:
  - Knowledge Base
  - Religious Studies
  - Islam
  - Investigation
parent_documents:
  - KOS-0008 Research Methodology & Investigation Framework
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - KOS-0007 Comparative Analysis Framework
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Investigation
  - Islam
  - WorldReligionsTimeline
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-23
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# INV-0018

# The Emergence of Islam and the Nature of Its Historical Relationship to Judaism and Christianity — Descent, Influence, or Neither

## Draft Investigation Record

> ## ✅ CLOSED — 2026-07-23 (full OPS-0003 circuit complete)
> **This investigation is formally CLOSED per ADR-GOV-0004 D1, under the owner's conditional pre-authorization in the circuit brief (brief 2 of 2).** The full adversarial circuit ran: Research Specialist (ROLE-0002) → Critical Reviewer (ROLE-0004, verdict **Conformant with Flags**, [[Critical Review - RQ-0018]]) → Knowledge Architect (ROLE-0001, structural validation clean, §6b). All ten §7 acceptance criteria are met with in-record evidence (§7). Closure conditions verified: **(a)** all ten criteria met — **criterion 3 satisfied on its SECOND limb: no edge was drawn, and the refusal is recorded and reviewer-verified**; the entity-precision requirement worked in full on both sides with two entity gaps recorded and routed; the Anchor Fit Assessment completed and routed across **all three** parts; **(b)** verdict Conformant with Flags with **three determinate flags, all remediated in-session** (three advisory, non-blocking, reported); **(c)** **no confidence level raised — and none lowered**; **(d)** both validators clean (`validate.py` 391 files 0 errors / 0 warnings, exit 0; `graph_integrity.py` 0 dangling / 0 branch errors, exit 0).
>
> **This is FAMILY 3 of the ADR-GOV-0009 world-religions timeline program — and the program's FIRST DELIBERATELY UNCONNECTED TRADITION NODE.** Created: **CLM-0095/0096/0097/0098**, **ENT-0015**, **FND-0018**, and **ZERO `branches_from` edges**. The modelling question resolved to **hypothesis (b): a separate root with influence relationships and no descent edge.** A no-edge outcome was pre-authorized as a legitimate result and is **not** a bar to closure.
>
> **"Closed" is NOT a maturity promotion** — the frontmatter `status` stays **Draft** (ADR-GOV-0005 §1: closure state lives in this banner and the history row, not in frontmatter). **"Closed" is NOT a clearance for external reliance:** everything lands **R0** and the **findings are NOT cleared for external reliance regardless of closure** (STD-0006 §7.5-analog — verification-light throughout, with two named base holes; the world-religions timeline is public-facing in ambition and this family is a living tradition of roughly two billion adherents; genuinely independent re-verification is the gate-lift). The **Anchor Fit recommendations are additionally §7.6-reflexively-gated** (GB-2026-041) — they may not promote the provisional `branches_from` / qualifier / §2.3 / `tradition_type` anchors from provisional toward durable absent blinded independent review, and this circuit supplied **no independence of kind** (same model family throughout, ADR-GOV-0011).

> Authored using **TPL-0003**. Eighteenth research workflow (RQ-0018). **Opened as a scaffold**; to be executed and closed through the full adversarial circuit (OPS-0003: Research Specialist → Critical Reviewer → Knowledge Architect; Vision Steward/owner closes). The opening/closing split is structural (**STD-0006 §7.6** independence principle): the session that authored this scaffold does not itself generate and certify the findings that fill it. The circuit runs under a separate brief (brief 2 of 2) after owner review. **The RQ freeze checkpoint is the owner's review of this scaffold report** — the §1 primary wording is authoritative pending that freeze.

> **Program context — this is FAMILY 3 of the ADR-GOV-0009 world-religions timeline program (D5),** the successor to INV-0016 (the Iranian family) and INV-0017 (the Judaism–Christianity family). **Scope is ONE tradition entity: Islam.** The **Sunni/Shia division is DEFERRED** to a later separate investigation — the same discipline that deferred the Israelite/Yahwistic roots out of INV-0017 (§2.4). No sub-tradition entity is created by this family.

> **THE MODELING QUESTION IS OPEN AND IS THE CIRCUIT'S TO ANSWER.** Three named, testable hypotheses, **none pre-adopted** (§2.2): **(a)** multi-parent `branches_from` to Judaism and/or Christianity; **(b)** a separate root with **influence** relationships and **no descent edge**; **(c)** a mix. The evidence decides — exactly as INV-0016's evidence overturned the Zurvanism hypothesis (Zurvanism dissolved to a *current*, not an entity). This scaffold states the hypotheses; it adopts none.

> **EDGE-RESTRAINT RULE (operative, §3.1).** **No `branches_from` edge is drawn unless the evidence supports DESCENT.** An influence relationship, however well evidenced, is **not** descent and **must not** be encoded as a descent edge for the sake of connecting the timeline. If the honest answer is "no descent edge," **the entity stands unconnected**, the influence finding is recorded in prose, and the modelling gap is routed to Anchor Fit.

> **Anchor stress-test duty, TWO PARTS (ADR-GOV-0009 §7(a); reserved section below).** **(1) MULTI-PARENT** — if the evidence supports descent from more than one parent, this is the **second demonstrating case** for the deferred **AF-2** recommendation (GB-2026-041), and the circuit says so explicitly. **(2) EDGE-TYPE ADEQUACY** — `branches_from` is **descent-only**, and the vault already holds graded **influence** findings the timeline cannot render: **INV-0011 (Zoroastrian Eschatology and Second Temple Jewish Apocalypticism — Influence Pathways)** established influence relations between two families that appear as **disconnected clusters** in `views/relatio-timeline.html`. If Islam's relationship proves **influence-shaped rather than descent-shaped**, INV-0011 is the **pre-existing FIRST case** and Islam is the **SECOND** for a possible `influenced_by` edge type — which would clear the defer-to-second-use bar in one step. **Assess and recommend only.** Per **ADR-GOV-0007 §3** no new edge type is created and no recommendation is self-applied.

> ### NEUTRALITY REQUIREMENT — ACUTE; THE STRICTEST OF ANY FAMILY TO DATE
> Islam is a **living tradition with roughly two billion adherents**, and parts of the relevant scholarship have been deployed polemically. **The register must not inherit that.** Three guards bind every record in this investigation and are reviewer-checked **in both directions** (§2.1):
> 1. **DUAL-TRACK DISCIPLINE (INV-0015 §2.1, in full force).** Islam's **self-understanding** — that it *restores* the original Abrahamic monotheism (*millat Ibrāhīm*) rather than deriving from Judaism or Christianity, confirming and correcting earlier revelations — is **evidence about the tradition's self-understanding, a fact**, steelmanned at its strongest in that register. It does **NOT** settle the historical question, and it is **NOT** dismissed as mere error. **Guard BOTH slides.**
> 2. **REVISIONIST SCHOLARSHIP AS SCHOLARSHIP.** Wansbrough; Crone & Cook (*Hagarism*); and successors are represented **as scholarship** — neither adopted as verdict nor waved away. Historically important, widely and substantively criticised, and **its criticisms are part of the record.** Mainstream and revisionist poles are each represented **at their strongest**, and the field's **actual distribution** is reported under the **CONSENSUS-ASYMMETRY RULE (INV-0015 §2.2)**: symmetric framing does not require symmetric findings, a lopsided field is reported as lopsided — **but neither pole is caricatured.**
> 3. **NO CONFESSIONAL AND NO SUPERSESSIONIST FRAMING IN ANY DIRECTION** — not Islam toward Judaism/Christianity, and not the reverse. The **metaphysical claims of all three traditions are bracketed entirely.**

> **Source posture — the base was CATALOGUED WITH THIS SCAFFOLD (owner-ratified).** The source gap was **verified before this session**: the vault held no Islamic-studies base at all (only incidental mentions of Islam inside Iranian-family and comparative records). Cataloguing was therefore **folded into this session** rather than discovered at scaffold, under the **ADR-GOV-0003 pattern: catalog only, grade nothing.** The base is **SRC-0143…SRC-0151** (§2.5) — nine records, **bibliographically verified, interiors disclosed, no claim asserted and no evidence graded at cataloguing.** Residual coverage gaps are reported honestly in §2.5 and are **not** filled by assumption.

> **Verification & reliance note (STD-0006 §7.5 analog).** Historical religious-studies investigation — **not health/high-stakes, not child-facing** — no health gate. It is, however, **externally consequential** (the world-religions timeline is public-facing in ambition, and this family is a living tradition of ~2 billion people) **and verification-light-expected** (the catalogued interiors are parametric/unread at cataloguing; several are paywalled or library-only). The Specialist and the Critical Reviewer **must each disclose their verification strength**, and **everything lands R0 — the findings are NOT cleared for external reliance regardless of closure.** Genuinely independent re-verification is the gate-lift.

> **Scale discipline.** Every on-record confidence rating — frontmatter and every grading field — is native **`Level N (Label)`** (KOS-0003 §8), the only authorized on-record confidence vocabulary. **No H-band in any frontmatter or grading field; no ★-glyphs anywhere in any Knowledge Object.** The optional H-band typology may appear in prose only.

> **Provisional-anchor note (ADR-GOV-0007 §2 / STD-0004 v1.3 / STD-0002 v1.11).** `branches_from` and its six-value qualifier list remain **PROVISIONAL**; ADR-GOV-0010 D5 explicitly did **not** lift the reflexive gate. **No tradition entity, dating claim, or edge is created by this scaffold** — the entity is created on demand at circuit (ADR-GOV-0009 D2), born timeline-ready with the render-only STD-0002 v1.11 positioning fields derived from and bounded by its dating claim (TPL-0006 v1.1). This session lays no anchors and populates none; it frames the work brief 2 executes, and **catalogues the source base**.

---

# 1. Research Question

**Primary (authoritative wording pending owner freeze at scaffold review):**

> What can be established, and at what evidential grade, about the emergence and dating of Islam as a religious tradition, and about the nature of its historical relationship to Judaism and Christianity — including whether that relationship is one of descent, of influence, or of neither?

**Decomposition mandate (owner-ratified): FOUR claims** (identifiers assigned at execution, not here), **each answering three explicitly separable elements** — the lesson encoded from INV-0011 criterion #2 that "treated in prose" is not "answered separably", applied throughout INV-0016 and INV-0017. Elements **(i) / (ii) / (iii)** must appear as **discrete sections** of each claim record.

- **CLM A — EMERGENCE AND DATING.**
  - **(i) DATABLE BOUNDS.** What the sources establish about the datable bounds of Islam's emergence — seventh-century-CE Arabia; the ministry and the formation period — reported at grade, with contested bounds reported as contested (**dates are claims**, ADR-GOV-0009 D3; no false precision).
  - **(ii) WHAT THE FORMATION CONTEXT ESTABLISHES.** What the late-antique Arabian and Near Eastern formation context does and does not establish about the tradition's emergence.
  - **(iii) RIVAL READINGS.** The **traditional chronology** and the **revisionist re-datings** (Wansbrough's late-crystallisation of the Qur'anic text; the *Hagarism* reconstruction and its successors), **each steelmanned**, with the field's actual distribution reported under the consensus-asymmetry rule and the cost to confidence stated.

- **CLM B — RELATIONSHIP TO JUDAISM.**
  - **(i) DOCUMENTED ENGAGEMENT AND ITS EVIDENCE BASE.** Arabian Jewish communities; shared narrative material; the Medinan context — what is documented, and on what evidence.
  - **(ii) RELATIONSHIP-TYPE ASSESSMENT — the load-bearing element.** **Descent, influence, or neither**, with the reasoning that **would (or would not) warrant a graph edge, and which kind.** The edge-restraint rule (§3.1) governs: influence is not descent.
  - **(iii) RIVAL READINGS.** The strongest counter-readings, steelmanned, with their cost to confidence stated.

- **CLM C — RELATIONSHIP TO CHRISTIANITY.** The same three-element shape:
  - **(i)** Syriac and Ethiopian Christian contact; Qur'anic engagement with Christian material; the Christological material — what is documented, and on what evidence.
  - **(ii)** Its **own** relationship-type assessment (descent / influence / neither), independently reasoned — **not** inherited from CLM B's answer.
  - **(iii)** Rival readings, steelmanned, with their cost to confidence stated.

- **CLM D — SELF-UNDERSTANDING.**
  - **(i) WHAT THE TRADITION HOLDS,** sourced to **primary text** (SRC-0151): its own account of its relationship to the earlier Abrahamic traditions — restoration / confirmation-and-correction, *millat Ibrāhīm*.
  - **(ii) ITS STATUS AS A FACT ABOUT THE TRADITION** that **does not settle the historical question** — and equally is **not** dismissed as mere error (the dual-track rule, both slides guarded).
  - **(iii) HOW IT RELATES TO, AND WHERE IT DIVERGES FROM, THE SCHOLARLY PICTURE** — divergences **recorded, not adjudicated theologically.**

**Modeling hypotheses — TO BE TESTED at circuit, NONE pre-adopted:**

| # | Hypothesis | What it would require | Graph consequence |
|---|---|---|---|
| (a) | **Multi-parent descent** — `branches_from` to Judaism and/or Christianity | Evidence supporting **descent**, not merely contact or influence, from one or both parents; a qualifier from the six-value provisional list that actually fits | One or two `branches_from` edges, each warrant-paired; **if two, this is the second demonstrating case for AF-2 (multi-parent)** |
| (b) | **Separate root + influence** — no descent edge | Evidence supporting **influence/contact** without descent; Islam emerging as its own root in the late-antique milieu | **No `branches_from` edge**; the entity stands unconnected; the influence finding is prose + Anchor Fit (the possible `influenced_by` edge type, **second case after INV-0011**) |
| (c) | **A mix** | Descent-shaped toward one tradition and influence-shaped toward the other, or partial/disputed descent | Whatever the evidence warrants per-relationship; `disputed` is an available qualifier **only** where descent itself is genuinely disputed, never as a hedge for "influence" |

**None of these is a working expectation.** The circuit tests them; a "no descent edge" outcome is a **legitimate, pre-authorized result**, not a failure of the investigation.

---

# 2. Scope & Disambiguation

## 2.1 Neutrality — the acute requirement, stated as operative discipline

The three guards in the banner above are **operative**, not aspirational, and the Critical Reviewer checks each **in both directions**:

- **Dual-track (both slides guarded).** The self-understanding track and the historical track are kept **separate and both honest**. Slide 1 to guard: letting the tradition's self-account **settle** the historical question. Slide 2 to guard: **dismissing** the self-account as mere error rather than reporting it as the fact about the tradition that it is. **CLM D is a claim about the tradition, not about the history**, and no historical claim (A/B/C) may be graded up or down on the strength of CLM D.
- **Revisionist scholarship as scholarship.** Represented at its strongest, with its **critical reception disclosed in the same breath** (including, where documented, the authors' own later positions). Neither adopted as verdict nor waved away. Its **criticisms are part of the record**, not a reason to omit it.
- **Consensus asymmetry (INV-0015 §2.2).** Symmetric framing does **not** require symmetric findings. Where the field is lopsided, it is **reported as lopsided** — with the minority position stated at its strongest, not caricatured, and the asymmetry itself evidenced rather than asserted.
- **No confessional and no supersessionist framing in any direction.** Not Islam as fulfilment/correction of Judaism and Christianity; not Judaism or Christianity as the "authentic" original against which Islam is derivative. **All three traditions' metaphysical claims are bracketed entirely.** Revelation, prophethood, and scriptural inspiration are outside what this record adjudicates in any direction.
- **Register.** Neutral historical religious studies throughout. Terms of art from the tradition (*millat Ibrāhīm*, *ḥanīf*, *tanzīl*) may be used descriptively, transliterated and glossed, without endorsement.

## 2.2 The modeling question is OPEN (three hypotheses; none pre-adopted)

Whether Islam stands in a relationship of **descent**, **influence**, or **neither** to Judaism and Christianity is **the circuit's finding, not a scaffold assumption.** The three hypotheses are tabulated in §1 and are held open here. Two disciplines protect that openness:

- **No pre-adoption.** No record created at circuit may presuppose a modelling outcome. The claim structure (CLM B (ii), CLM C (ii)) requires the relationship-type assessment to be **argued**, per-tradition, with the reasoning that would warrant or refuse an edge.
- **Edge restraint (§3.1).** The convenience of a connected timeline is **not** a reason to draw a descent edge. The timeline may honestly show a disconnected node.

## 2.3 Distinctness threshold (§2.3 criterion carried forward)

The Iranian family's **§2.3 distinctness threshold applies unchanged**: a formation warrants its own tradition-class Entity Record when the source base treats it as a **distinct religious tradition** — evidenced by (a) an identifiable community, adherents, or transmission lineage of its own; (b) a distinguishing doctrinal or organizational core; and (c) recognition in the literature as a *named tradition* rather than a *period, tendency, or current*.

Islam itself clears the threshold uncontroversially. The criterion is carried forward for **any sub-stream that pressures it** during the circuit (early sectarian formations, the Kharijite/proto-Shīʿī currents of the first century AH, or any group the sources treat ambiguously): **flag the pressure, do not force the criterion.** A sub-stream that strains the threshold is recorded as strain and routed to Anchor Fit — it is **not** entified, and it is **not** silently suppressed either.

## 2.4 Sunni/Shia deferred — and why

The **Sunni/Shia division is OUT OF SCOPE**, deferred to a later separate investigation. The reasoning is the same discipline that deferred the Israelite/Yahwistic and Canaanite roots out of INV-0017: an internal division that is itself a **substantial branching question** deserves its own claims, its own source base, and its own adversarial pass, rather than being appended to a family whose primary question is the tradition's own emergence and external relationships. **No sub-tradition entity is created in this family**, and **no internal `branches_from` edge is drawn**. Internal plurality that the sources show is recorded **as currents within** the single Islam entity, exactly as INV-0017 recorded the Second Temple parties within its hub.

## 2.5 Source posture — the base catalogued this session, and the residual gaps

- **Gap verified before this session, catalogue folded in.** The vault held **no Islamic-studies base**; the only pre-existing occurrences of Islam in the corpus were **incidental** (Yazidism's Islamic milieu in ENT-0011/CLM-0091/SRC-0118; the Iranian-family context; the ADR-GOV-0009 program listing; comparative-framework examples). Cataloguing was therefore executed **with** this scaffold under the **ADR-GOV-0003 pattern — catalog only, grade nothing.**
- **The base (nine records, SRC-0143…SRC-0151):**
  - **Formation and early Islam (mainstream):** **SRC-0143** Donner, *Muhammad and the Believers* (2010); **SRC-0144** Berkey, *The Formation of Islam* (2003).
  - **Revisionist scholarship (catalogued as scholarship, reception disclosed in-record):** **SRC-0145** Wansbrough, *Quranic Studies* (1977); **SRC-0146** Crone & Cook, *Hagarism* (1977).
  - **Qur'anic studies (historical-critical):** **SRC-0147** Sinai, *The Qur'an: A Historical-Critical Introduction* (2017).
  - **The Judeo-Christian context:** **SRC-0148** Reynolds, *The Qur'ān and Its Biblical Subtext* (2010); **SRC-0149** Griffith, *The Bible in Arabic* (2013).
  - **The Arabian / late-antique milieu:** **SRC-0150** al-Azmeh, *The Emergence of Islam in Late Antiquity* (2014).
  - **Primary text (self-understanding track only):** **SRC-0151** the Qur'an in the **Abdel Haleem** English translation (Oxford World's Classics), catalogued under **edition discipline** — the SRC-0135 precedent (a tradition's own voice catalogued in the self-understanding register only). **Translation choice is itself interpretively loaded**, and the record discloses which edition is used and why.
- **Interiors are disclosed, not assumed.** Every record states its verification strength: **bibliographically live-verified; interiors parametric/unread at cataloguing.** **No page-level claim may be drawn from an unread interior at circuit** — the layer-inheritance bound (§3.1) applies, and a thin base yields an honestly lower grade.
- **Residual gaps reported (NOT filled by assumption):**
  - A dedicated treatment of the **Arabian Jewish communities** as such (the Medinan Jewish tribes, Ḥimyarite Judaism) is **not** in the base; CLM B (i) rests on what SRC-0148/0150 and the mainstream formation works carry on that question, and is **graded at that ceiling.**
  - **Documentary/epigraphic and non-Muslim contemporary evidence** (papyri, inscriptions, Syriac and Greek testimonia) is represented only indirectly through the catalogued works, not by a dedicated source.
  - **Arabic- and Syriac-language primary scholarship** is a recorded corpus gap (the INV-0015 Chinese-corpus precedent): the base is Anglophone.
  - Any extension to close these is a **SEPARATE owner-approved step**, decided at or after RQ-freeze — **not created or assumed here.** If the owner declines an extension, the circuit grades honestly on the available base; **thin-base outcomes are pre-authorized, not a failure.**

## 2.6 Boundaries

- **Sunni/Shia and all sub-traditions:** out of scope (§2.4); no entity, no internal edge.
- **The later history of the tradition** (the conquests, the caliphates, law schools, Sufism, modern movements) is out of scope except as it bears on **dating the tradition's emergence and formation period**.
- **With closed records (cite, never re-derive).** Anything inherited from INV-0011 / INV-0013 / INV-0014 / INV-0016 / INV-0017 is **cited at its grade**; those investigations are not edited, re-opened, or re-derived. Identifiers are verified at execution and the cited claim wins on any discrepancy.
- **With catalogued sources (consume, never modify).** The Iranian base (SRC-0104…0123), the NT corpus (SRC-0091…0103), and the Jewish-studies base (SRC-0137…0142) are **cited only**; no catalogued source record is touched.
- **Cross-family edges.** Whether **any** edge crosses from Islam to the Judaism–Christianity family is **exactly the open modeling question** (§2.2) — it is neither pre-authorized nor pre-forbidden here, and it is drawn **only** if descent is established (§3.1). **No edge to the Iranian family** is contemplated; any Iranian-milieu relation is prose only.

## 2.7 Scale posture

Native **`Level N`** only in every frontmatter and grading field. The H-band typology may be used in **prose only** (optional) and carries no grading authority. **No ★-glyphs anywhere.**

## 2.8 Reliance posture

**Everything lands R0.** Verification-light close is expected (parametric interiors, §2.5). Findings are **NOT cleared for external reliance regardless of closure** — the §7.5-analog gate is declared here, at opening, before any evidence. The **Anchor Fit findings are additionally §7.6-reflexively-gated** (they may not promote the provisional anchors toward durable absent blinded independent review).

## 2.9 Terminology

- **"Islam"** denotes, for this investigation, the religious tradition whose emergence is dated in CLM A — treated as **one tradition** with internal plurality (§2.4), not as a set of sub-traditions.
- **"Descent"** means the relationship `branches_from` encodes: tradition B **derives from** tradition A as its parent. **"Influence"** means documented transmission, contact, or shared material **without** derivation. **The two are not interchangeable** and the record never uses one word for the other (§3.1).
- **"Revisionist scholarship"** denotes the Wansbrough / Crone–Cook current and its successors — a **descriptive label for a scholarly position**, carrying no pejorative and no endorsement.
- ***millat Ibrāhīm*** ("the religion/creed of Abraham") is used descriptively for the tradition's self-account of restoration; its use is **not** an endorsement of that account (dual-track, §2.1).
- **`branches_from` qualifiers** (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed` / `continuation`, STD-0004 §7.2 v1.3) are **distinct from** `tradition_type` **values** (`founded` / `emergent` / `reform` / `syncretic`, STD-0002 §11). The word `reform` appears in **both** vocabularies with different meanings and is **never conflated** (STD-0004 §7.2).

---

# 3. Method / Protocol

Execution follows the KOS-0003 pipeline (Question → Claims → Assumptions → Evidence → Confidence) through the **full OPS-0003 circuit**. Claims via **TPL-0001** (born epistemic-, review-, and attribution-conformant); the tradition entity via **TPL-0006 v1.1** tradition-class skeleton, **born timeline-ready** (`tradition_type`, `dating_claims`, `display_range` per STD-0002 §11 v1.10, **plus** the render-only positioning fields `range_start_year` / `range_end_year` / `range_uncertainty` per v1.11, derived from and bounded by CLM A, confidence-inheriting, `display_range` authoritative) **and attribution-conformant**; the synthesis via **TPL-0004**. Sources are cited from the base catalogued this session (SRC-0143…SRC-0151) plus primary text; **no new source is created at circuit without a separate owner-approved catalog extension** (§2.5). All identifiers are registered in the Identifier Registry at execution.

## 3.1 Operative disciplines (bind at circuit)

> **EDGE-RESTRAINT RULE.** **No `branches_from` edge is drawn unless the evidence supports DESCENT.** An influence relationship, however well evidenced, is **NOT** descent and **must not** be encoded as a descent edge for the sake of connecting the timeline. If the honest answer is "no descent edge," **the entity stands unconnected**, the influence finding is **recorded in prose**, and the modelling gap is **routed to Anchor Fit**. Corollaries: the `disputed` qualifier means *descent is disputed*, and may **never** be used as a hedge for "this is influence, not descent"; and a visually disconnected timeline node is an **honest rendering**, not a defect to be repaired by an edge.

> **WARRANT RULE (review-checked, not tool-checked).** Every `branches_from` edge written at circuit **MUST be warranted by a graded claim** asserting the descent (the edge renders; the claim warrants). `graph_integrity.py` enforces only the *structural* constraints (ENT→ENT, required/controlled qualifier) — it **cannot** verify the warrant, because a warrant is a claim about lineage, not a structured pointer. **The Critical Reviewer therefore verifies each edge-warrant pair explicitly, per-edge.** An unwarranted edge is a defect the reviewer must catch. **If no edge is drawn, the reviewer instead verifies that the refusal is reasoned and recorded** (the negative case is reviewed as rigorously as the positive one).

> **LAYER-INHERITANCE.** A claim that **cites a closed investigation** is **bounded by the cited claims' grades** — the inheriting claim may not exceed the cited claim's grade on the shared question. A claim resting on **parametric/unread interiors** (the whole catalogued base at cataloguing, §2.5) is **bounded by that base**: no page-level assertion from an unread interior, and no grade a thin base has not earned.

> **DUAL-TRACK SEPARATION.** CLM D (self-understanding) is sourced to primary text and evidences **the tradition's self-understanding only**. It may **not** raise or lower the grade of CLM A/B/C, and CLM A/B/C may **not** be used to adjudicate the truth of CLM D. Divergences between the two tracks are **recorded** (CLM D (iii)), never resolved theologically.

## 3.2 Per-claim structure

Each of the four claims answers its elements **(i)**, **(ii)**, and **(iii)** in **explicit, separable sections** of the claim record — not diffused through prose (§1; acceptance criterion 1). CLM B (ii) and CLM C (ii) each carry the **relationship-type assessment** with the edge-warrant reasoning stated **either way** (what would warrant an edge, and whether it is met).

## 3.3 Entity-on-demand, dates-as-claims, born-timeline-ready positioning

- The tradition entity is created **only as its claims warrant it** (ADR-GOV-0009 D2) — no pre-populated gazetteer, and **one entity only** (§2.4).
- **Dates are claims** (D3): the entity carries `dating_claims` pointers and a render-only `display_range`; the sourced, graded, epistemic-fielded date lives in CLM A, and **there is no `origin_date` field.** Contested dating is carried as contestedness in the claim, never flattened into a false-precision range on the entity.
- **Born timeline-ready (STD-0002 v1.11):** the entity carries `range_start_year` / `range_end_year` / `range_uncertainty` **derived from and bounded by CLM A** (`range_uncertainty` mapping from the dating component's confidence; **a bar never renders more certain than the claim behind it**; `display_range` stays authoritative and is shown verbatim). Populating these at birth is a **circuit deliverable** — no backfill.
- **`range_end_year: present`** is the honest value for a living tradition; it is a render instruction, not a historical claim.

---

# 4. Findings / Synthesis

**Executed 2026-07-23 (brief 2 of 2). Primary synthesis: [[FND-0018 - Islam Origins and Abrahamic Relationship Shape]].**

**THE MODELLING OUTCOME: HYPOTHESIS (b) — A SEPARATE ROOT WITH INFLUENCE RELATIONSHIPS AND NO DESCENT EDGE.** Hypotheses (a) multi-parent descent and (c) a mix are **unsupported on this base**. The four claims:

- **[[CLM-0095 - Islam Emergence and Dating]]** — seventh-century CE emergence in western Arabia and the adjoining late-antique Near East (**High**, earned on the mainstream/revisionist **cross-pole convergence test**: the revisionist works relocate the text's stabilisation and the confession's self-definition, not the movement's century). Confessional crystallisation genuinely contested (**Moderate**), bounded but not settled by the public-expression anchors live-verified this session (Dome of the Rock 72 AH / 691–692 CE; ʿAbd al-Malik's coinage reform from 77 AH / 696–697 CE). This record's own ability to adjudicate the revisionist re-datings graded **Low**. Traditional chronology reported *as* the tradition's chronology; **no false precision, no `origin_date`.**
- **[[CLM-0096 - Islam Relationship to Judaism]]** — **influence and engagement, NOT descent** (**Moderate**). The base's one descent-shaped reading (*Hagarism*) was **weighed, not dismissed**, and failed on its own recorded reception. Arabian Jewish community character graded **Low** — the base gap §2.5 predicted, carried openly.
- **[[CLM-0097 - Islam Relationship to Christianity]]** — **influence and engagement, NOT descent** (**Moderate**), reasoned **independently** and reaching the same category by a different route: no descent-shaped thesis exists in the base at all, and the engagement is **simultaneously appropriative and repudiative** — an interlocutor's posture, not a descendant's. The absent Syriac-substratum literature is **disclosed as absent and treated as a limit, not as support** — the stated reason the grade is Moderate and not High.
- **[[CLM-0098 - Islam Self-Understanding]]** — the tradition's **restorationist** self-account (**Moderate** as a reported fact; terminology **Low** for the translation limit), recorded in its own register, steelmanned, and **structurally firewalled** from the historical track.

**THE EDGE DECISION — NO `branches_from` EDGE IS DRAWN. [[ENT-0015 - Islam]] carries ZERO lineage edges and renders as an unconnected node.** Under §3.1 this is an **honest rendering requiring no repair**, and the refusal is recorded and reviewer-verified as rigorously as an edge would be (Critical Review – RQ-0018 §2, six tests). **`disputed` was not used and could not be** — it means *descent is disputed*, whereas here descent is **not established**; `heterodox-offshoot` and `syncretic-descent` were each considered and refused with reasons.

**THE ENTITY-PRECISION OUTCOME — TWO RECORDED ENTITY GAPS, OF DIFFERENT SHAPES, both routed to Anchor Fit and neither used to prop up the edge decision:**
- **ENT-0012 Second Temple Judaism FAILS the chronological-coherence check** (`range_end_year: 70` against a seventh-century relationship) — the requirement's first real firing in the program, and the entity an unwary circuit was most likely to reach for, since the RQ says "Judaism."
- **ENT-0014 Rabbinic Judaism passes chronologically but OVER-SPECIFIES** — the rabbinisation of seventh-century Arabian Jewish communities is an open question the base does not cover.
- **ENT-0013 Christianity passes chronologically but is TOO COARSE** — the documented contact was with eastern Syriac, Ethiopic/Aksumite, Arab-confederation and Najrānī Christianity, which §2.4 forbids this family to model.
- **No entity was created and no edge was forced onto an approximate target.**

**Entity born:** **ENT-0015 Islam** — `tradition_type: founded` (least-wrong for the historical register, with the restorationist and late-crystallisation strains both recorded), `dating_claims: CLM-0095`, `display_range` render-only, positioning bounds `range_start_year: 610` / `range_end_year: present` / `range_uncertainty: moderate` (inheriting CLM-0095's weakest **emergence-dating** component). **No sub-tradition entity** (Sunni/Shia deferred, §2.4).

---

# 5. Confidence Summary (KOS-0003 §8)

Assigned at circuit execution; native `Level N` only, per-component, **never averaged**. FND-0018's seven components:

- **seventh_century_emergence — Level 4 (High)** — the circuit's only Level 4.
- **confessional_crystallisation_dating — Level 3 (Moderate).**
- **relationship_to_judaism_influence_not_descent — Level 3 (Moderate).**
- **relationship_to_christianity_influence_not_descent — Level 3 (Moderate).**
- **entity_target_gaps — Level 3 (Moderate).**
- **self_understanding_as_reported_fact — Level 3 (Moderate)** — capped by verification posture, not by scholarly doubt.
- **translation_limited_terminology — Level 2 (Low)** — taken deliberately under SRC-0151's binding limit.

**No Level 5 anywhere. NO qualifier-fit component exists, because no edge was drawn** — the anticipated "if and only if an edge is drawn" component correctly did not fire. Everything **R0**; **not cleared for external reliance** (§2.8).

---

# 6. Assumptions & Bracketing (KOS-0003 §10)

*Expanded at circuit execution. The standing brackets and disciplines below bind from opening:*

- **Metaphysical bracket, acute (§2.1).** All three traditions' truth claims are bracketed; the register is neutral historical religious studies, in **no** direction — neither confessional nor supersessionist, neither toward nor away from any of the three.
- **Dual-track, both slides guarded (§2.1, §3.1).** Self-understanding is a fact about the tradition; it neither settles nor is dismissed.
- **Revisionist scholarship represented as scholarship (§2.1),** with its critical reception disclosed; **the consensus-asymmetry rule governs how the field's distribution is reported.**
- **The modeling question is open (§2.2).** No hypothesis is adopted at opening; a **"no descent edge"** outcome is legitimate and pre-authorized.
- **Edge restraint (§3.1).** Influence ≠ descent; a disconnected node is an honest rendering.
- **Sunni/Shia deferred (§2.4).** Internal plurality is recorded as currents within one entity, not entified.
- **Source posture (§2.5).** Interiors are parametric at cataloguing and disclosed as such; residual gaps are reported, not filled by assumption; an extension is an owner decision; thin-base outcomes are pre-authorized.
- **Anchors stay provisional (ADR-GOV-0010 D5).** Nothing here promotes `branches_from`, its qualifier list, the §2.3 threshold, or `tradition_type` toward durable; **no new edge type is created and no Anchor Fit recommendation is self-applied** (ADR-GOV-0007 §3).

---

# 6b. Structural Validation (ROLE-0001, in-record — ADR-GOV-0005 §2)

Performed 2026-07-23 by the Knowledge Architect (ROLE-0001) after the Critical Reviewer's remediations were applied.

- **`validate.py` — PASS at error level.** **391 files scanned; 0 errors; 0 warnings; exit 0.** Epistemic fields (`confidence` list, each component `level` 1–5 with its matching STD-0008 label; `reliance_tier`), review fields (`review_cycle` 6; `last_reviewed` 2026-07-23; `review_date` 2027-01-23 — arithmetic checked by the tool), the required `attribution` list, and the tradition-class fields on ENT-0015 (`tradition_type` / `dating_claims` / `display_range` plus the v1.11 positioning bounds, with the `range_start_year` + `range_uncertainty` co-presence rule) are **well-formed at birth on every new object** — no hand-reconciliation was performed. **Version coherence** clean across the four records bumped to v0.2 at review remediation (each bump carries its history row).
- **`graph_integrity.py` — clean.** **391 objects scanned; 0 dangling references; 0 `branches_from` edge errors; exit 0.** Advisory counts **unchanged by this circuit** (39 non-reciprocated symmetric typed links; 2 legacy untyped one-directional KB links) — the circuit introduced **no** new advisory. `dating_claims: CLM-0095` resolves. **There is no ENT→ENT edge to check a qualifier on, because no `branches_from` edge exists** — the 0-branch-errors result is the honest one for a no-edge outcome, and criterion 3's second limb is satisfied by the reviewer-verified refusal, not by the tool.
- **Scale-discipline grep — clean.** No `★`/`☆` glyph and no H-band token appears in any frontmatter or grading field on any INV-0018 object; the only occurrences anywhere in the subgraph are **prose statements of the rule itself** (this record's §2.7 and the Critical Review's §6). All `level:` values are integers 1–5 with matching labels. **No `qualifier:` key exists anywhere in the subgraph.**
- **Subgraph matches §8 as planned.** INV-0018 is the hub; four claims `part_of` it and `supports` FND-0018, each `derived_from` its cited sources; CLM-0096 and CLM-0097 `depends_on` CLM-0095; **CLM-0098 deliberately carries NO typed edge to the historical claims** (the dual-track separation, enforced in the graph); one entity (ENT-0015) with `derived_from` to SRC-0143/0150 and **zero lineage edges**; FND-0018 `derived_from` the four claims and `part_of` INV-0018. **The `branches_from` count is ZERO — the pre-authorized honest outcome recorded at §8 as one of the possible results, not a defect.**
- **Nothing outside the circuit was touched.** Verified by working-tree inspection: the only changes are the six new INV-0018 objects, ENT-0015, and this record. **ENT-0012/0013/0014, INV-0011, INV-0016, INV-0017, SRC-0143…0151 and every other source base, the Standards, Roles, Templates, ADRs, the Architecture Baseline, and the tooling are UNMODIFIED.**

---

# Anchor Fit Assessment (ADR-GOV-0009 §7(a) stress-test deliverable — EXECUTED 2026-07-23, THREE PARTS)

> ## ✅ COMPLETED AND ROUTED — full text in [[FND-0018 - Islam Origins and Abrahamic Relationship Shape]] §4
> **Executed in THREE parts** — the two reserved at scaffold, plus **Part 3** added by owner flag in the circuit brief. **All findings routed to GB-2026-041; nothing self-applied; no relationship type created; no standard, template, tool, ADR, Baseline, prior investigation, or source base modified.** Reviewer verified all three parts as substantive (Critical Review – RQ-0018 §7). Output is **§7.6-reflexively-gated**; this circuit supplied **no independence of kind** (same model family throughout).
>
> - **PART 1 — MULTI-PARENT (AF-2): NEGATIVE RESULT, recorded as a result.** No descent from any parent, therefore *a fortiori* none from more than one. **AF-2 gets no second demonstrating case; INV-0016 (Manichaeism) remains its only one and the deferral stands (ADR-GOV-0010 D4).** The family that looked most likely on its face to produce a multi-parent descent case produced the program's first **zero-parent** case instead. **One observation, explicitly not a hedge on the negative:** the multi-parent *shape* recurs at the **influence** layer (two traditions, assessed independently), which is a **design constraint on Part 2's candidate** — any `influenced_by` type must support multiple targets from birth.
> - **PART 2 — EDGE-TYPE ADEQUACY: FIRES. The bar is cleared in one step.** INV-0011 is the **pre-existing FIRST case** of a graded influence relation the timeline cannot render; **INV-0018 is the SECOND**, and a stronger one — here the unrenderable influence relation *is* the investigation's central finding, on a node with no other edge at all. A candidate **`influenced_by`** type is **specified and recommended only**: asymmetric and never auto-reciprocated; **ENT → ENT**; **multi-target from birth**; a **minimal, explicitly provisional two-value qualifier list** (`documented` / `contested`) rather than a speculative taxonomy — the direct lesson of ADR-GOV-0010; warrant-by-graded-claim **plus a REQUIRED not-descent determination on the warranting claim** (the discipline this circuit executed, generalised — without it the type becomes the soft option that hollows out the edge-restraint rule); and a render style **visually subordinate to descent connectors**, under the hard constraint that **a node whose only edges are `influenced_by` must still read as a ROOT, never as a branch**. **Load-bearing caveat:** creating the type would **not** by itself let this finding be drawn, because the honest entity targets do not exist — **the edge-type question and the entity-resolution question must be governed together.** Cost of continuing without it: two closed investigations' graded findings stay structurally invisible on a public-facing view that currently implies *no relation* where the record says *graded influence*. **NOT CREATED.**
> - **PART 3 — RESTORATIONIST SELF-UNDERSTANDING vs THE VOCABULARY: OBSERVATION ONLY.** Islam's self-account is structurally ***claimed descent from something not continuously transmitted*** — named by **none** of the six qualifiers (four presuppose a continuous parent; `syncretic-descent` presupposes multiple living parents; `disputed` concerns **historical** descent). Kin to the anticipated **REVIVAL** case (a tradition developing from the recovered teachings of a tradition no longer living). **But the two are not the same kind of thing:** revival would be a *historical* finding, whereas this is a *self-understanding* structure, and under the dual-track rule **a self-account may NEVER be encoded as a lineage edge.** Islam is therefore a **PRESSURE case, not a demonstrating case** — the shape is named in advance and logged as a possible future second-use input, and **no vocabulary action is recommended**. **CLM-0098's grade did not move on account of this Part, and the Part rests on nothing in that grade.**
> - **Also recorded:** qualifier-list fit **did not fire** (no edge, no qualifier, and no qualifier-fit component anywhere). The **§2.3 distinctness threshold was NOT ASSESSED** — recorded as not-assessed rather than as assessed-and-clear, since the sub-streams that would have pressed it sit inside the deferred Sunni/Shia scope (§2.4). **`tradition_type` vocabulary strain FIRED twice** (no `restorationist` value; late-crystallisation pressure toward `emergent`) — reported, not force-fit. **A FOURTH, UNANTICIPATED OBSERVATION ROUTED: ENTITY RESOLUTION** — both entity gaps are instances of one structural fact, that the tradition-entity layer has a single resolution and can represent neither a regional community formation nor a sub-tradition body that a documented relationship actually attaches to. The reviewer records this as **the most transferable finding in the circuit**, because it blocks edge-drawing independently of whether any new edge type exists.

> **Reserved framing retained below for the record.** Per **ADR-GOV-0007 §3** every finding recorded here is a **RECOMMENDATION routed to GB-2026-041 / the review queue — never a self-applied structural change.** This investigation amends **no** standard, template, or tool, and **creates no new relationship type.**

**PART 1 — MULTI-PARENT (the deferred AF-2 recommendation).**
`branches_from` is currently a single-parent edge in practice; **AF-2** (multi-parent lineage) was raised by the Iranian family and **deferred** by ADR-GOV-0010 D4 as a candidate awaiting a second demonstrating case. **If the evidence here supports descent from more than one parent** (Judaism *and* Christianity), this family is that **SECOND demonstrating case**, and the circuit **says so explicitly** — naming INV-0016 as the first and this as the second, and stating what the two cases jointly demonstrate. **If the evidence does not support multi-parent descent, the circuit says that too** — a negative result on AF-2 is a real result and is recorded as one, not omitted.

**PART 2 — EDGE-TYPE ADEQUACY (`branches_from` is descent-only).**
The vault **already holds graded influence findings that the timeline cannot render.** **INV-0011 — *Zoroastrian Eschatology and Second Temple Jewish Apocalypticism — Influence Pathways*** established influence relations between two families that appear as **disconnected clusters** in `views/relatio-timeline.html`: the relation is real, graded, and closed — and structurally invisible, because the only lineage edge the vocabulary offers means *descent*.

- **If Islam's relationship to Judaism and/or Christianity proves influence-shaped rather than descent-shaped**, then **INV-0011 is the PRE-EXISTING FIRST CASE and Islam is the SECOND** for a possible **`influenced_by`** edge type — **which would clear the defer-to-second-use bar in one step** (the ADR-GOV-0005 §3 pattern: a candidate matures on its second independent firing).
- The circuit **assesses and recommends**: what the missing edge would have to express (asymmetric? qualifier-carrying? warrant-by-graded-claim like `branches_from`? renderable distinctly from descent on the timeline?), what it must **not** collapse into, and what the cost of continuing without it is.
- **It does NOT create the edge type, does NOT draw such an edge, and does NOT self-apply the recommendation.** The recommendation is routed; the owner governs (ADR-GOV-0007 §3 — the ADR-GOV-0010 precedent, where the system's own finding informed and the owner decided).

**Also recorded here if they fire:** qualifier-list fit for any edge actually drawn; §2.3 threshold strain from any sub-stream (§2.3); and any `tradition_type` vocabulary strain for a tradition whose self-account is *restoration* rather than founding or emergence — a genuinely novel case for the four-value list, to be **reported, not force-fit**.

---

# 7. Acceptance Criteria for Closing

INV-0018 may close only when all of the following hold (modelled on INV-0017 §7, adapted):

1. [x] **MET.** Four claims — **CLM-0095** (A emergence/dating) · **CLM-0096** (B Judaism) · **CLM-0097** (C Christianity) · **CLM-0098** (D self-understanding). Each carries `# Element (i)` / `# Element (ii)` / `# Element (iii)` as **discrete headed sections**, not diffused prose; CLM-0096 and CLM-0097 further subdivide element (ii) into (a) bar / (b) evidence / (c) entity-precision / (d) edge decision. **Reviewer-confirmed** at Critical Review – RQ-0018 §6 ("structural separation beyond the requirement, and the reason the entity-precision work is auditable at all").
2. [x] **MET.** **ENT-0015 Islam**, one entity only, born conformant to TPL-0006 v1.1 / STD-0002 v1.10+v1.11: review and `attribution` fields present, `tradition_type: founded`, `dating_claims: CLM-0095`, `display_range` render-only, **no `origin_date` field**, and the render-only bounds `range_start_year: 610` / `range_end_year: present` / `range_uncertainty: moderate` **derived confidence-inheriting from CLM-0095's weakest emergence-dating component**, with the non-temporal exclusion documented and reviewer-adjudicated (Critical Review §6). **No Sunni/Shia or other sub-tradition entity** — confirmed, the Entities folder gained exactly one file. `validate.py` shape-checks all of it at error level (§6b).
3. [x] **MET on the SECOND limb.** **No `branches_from` edge was drawn, and the reasoning is recorded** — in CLM-0096 §(ii), CLM-0097 §(ii), ENT-0015 §4, and FND-0018 §1. **The reviewer verified the refusal is REASONED, not merely absent**, against six explicit tests (Critical Review §2): the descent bar was stated before the evidence was measured; the strongest descent candidate was engaged rather than dodged; the refusal rests on positive counter-indications, not silence; no disclosed absence was converted into support; **`disputed` was not used to hedge for influence** (verified on every object; no `qualifier:` key exists in the subgraph); and the disconnected node was not treated as a defect. Two candidate qualifiers were additionally considered and refused with reasons. **`graph_integrity.py`: 0 branch errors** (§6b).
4. [x] **MET.** All three guards held and **reviewer-checked in both directions on every object** (Critical Review §4). Dual-track: slide 1 verified **structurally** (CLM-0098 carries no typed edge to the historical claims, in either direction) and substantively (the historical refusals rest on historical reasoning that would stand unchanged if the self-account said the opposite); slide 2 verified (the account is steelmanned in register and explicitly not characterised as late, apologetic, or constructed). **The convergence trap — both tracks agreeing that Islam does not descend — was named and explicitly denied evidential weight**, which the reviewer records as the best evidence the rule was operative rather than decorative. No confessional or supersessionist framing in any direction; the Byzantine heresy reading was **refused on historical evidence rather than on register**; the `founded`/`emergent` asymmetry against ENT-0013 was verified as evidenced, not a covert ranking.
5. [x] **MET.** Four rival readings steelmanned in CLM-0095 §(iii) (traditional chronology; Wansbrough's late crystallisation; the *Hagarism* reconstruction; Donner's Believers movement), and three more in each relationship claim, **including the opposite-slide rivals** (back-projection / no-relation). **The field's lopsidedness is reported as lopsidedness and EVIDENCED from the source records' own logged reception** — SRC-0145 and SRC-0146 each state on-record that their theses are non-consensus, SRC-0146 additionally records authorial distancing, and the four mainstream works proceed without adopting either reconstruction. **Neither pole is caricatured or adopted**; the revisionist current's methodological legacy is credited as absorbed into mainstream practice, and the record's own adjudicative reach is graded **Low** rather than claiming the question settled. "Institutional authority is credential, not evidence of correctness" is applied **symmetrically to the mainstream works**.
6. [x] **MET.** CLM-0095 separates the movement's origin from the crystallisation point and grades them apart; the traditional chronology is reported **as the tradition's chronology**, and a single-point founding date is explicitly rejected (Alternative 1). `display_range` is render-only and authoritative; **there is no `origin_date` field and none was invented**; the sourced, graded, epistemic-fielded dates live in CLM-0095. The render bound uses the **earliest defensible** value (610) with the firmer alternative (622) recorded, and the contestedness is carried by `range_uncertainty` and by the claim, never by a false-precision point. Reviewer-verified (Critical Review §6).
7. [x] **MET.** SRC-0143…0151 **cited and unmodified** (working-tree verified, §6b); **all nine interiors parametric/unread and disclosed on every claim**; **no page-level claim asserted from any interior**, and reported positions/criticisms are traceable to the source records' own §1/§3 sections. **No passage of the primary text was quoted or paraphrased and no *sūra*:*āya* was cited anywhere** — stricter than required, and the right call on an unread interior. **The residual §2.5 gaps are reported, not papered over** — the Arabian-Judaism gap is carried as an explicit **Low** component, and the absent Syriac-substratum literature is disclosed as absent and treated as a **limit on the determination rather than as support for it**. **No new source was created.** Closed records (INV-0011/0013/0014/0016/0017) were **neither cited-as-re-derived nor edited**. Two determinate source-discipline flags were raised by the reviewer and **remediated in-session** (parametric general-reference disclosures now on all three historical claims).
8. [x] **MET.** Native `Level N (Label)` only; **scale-discipline grep clean** — no `★`/`☆` and no H-band token in any frontmatter or grading field on any INV-0018 object, the only occurrences being prose statements of the rule itself (§6b).
9. [x] **MET.** Full OPS-0003 circuit ran: **Specialist (ROLE-0002)** → **Critical Reviewer (ROLE-0004)**, verdict **Conformant with Flags**, [[Critical Review - RQ-0018]] → **Knowledge Architect (ROLE-0001)**. **Verification strength is disclosed by BOTH** — every claim carries a §Verification section, FND-0018 §5 carries the synthesis disclosure with the two named base holes, and the Critical Review §9 discloses the reviewer's own posture (read every object, cross-checked the entity fields and typed-relationship blocks directly; read **no** source interior, consulted **no** Arabic and **no** second translation; **same model family, therefore no independence of kind**). **ROLE-0001 structural validation is evidenced IN-RECORD at §6b** (ADR-GOV-0005 §2 satisfied without an out-of-record citation): `validate.py` **391 files, 0 errors, 0 warnings, exit 0**; `graph_integrity.py` **0 dangling, 0 branch errors, exit 0**, advisory counts unchanged.
10. [x] **MET, and in THREE parts.** Completed and routed to **GB-2026-041**: **Part 1 NEGATIVE and recorded as a result** (AF-2 gets no second demonstrating case; the deferral stands; the negative was not softened into a partial positive — the multi-parent-at-the-influence-layer observation is framed as a design constraint on Part 2); **Part 2 FIRES** with INV-0011 as first case and Islam as second, fully specified and **not created**, including the required not-descent determination and the load-bearing entity-resolution caveat; **Part 3 OBSERVATION ONLY**, with the pressure-case/demonstrating-case distinction that keeps a self-account out of the lineage vocabulary. Qualifier-list fit recorded as **did not fire**; §2.3 recorded as **not assessed** rather than assessed-and-clear; `tradition_type` strain recorded as fired; a **fourth, unanticipated observation (entity resolution)** routed. **Nothing self-applied.** Standards, templates, tools, ADRs, the Architecture Baseline, prior investigations, and the existing source bases are **unmodified** (§6b).

**Verification & reliance (§7.5 analog).** This investigation is **externally consequential** (public-facing timeline; a living tradition of ~2 billion adherents) **and verification-light-expected** (parametric interiors). **Findings are NOT cleared for external reliance regardless of closure** — a verification-light review may issue verdicts but may not clear findings for external use; genuinely independent re-verification is the gate-lift. Everything lands **R0**. Anchor Fit output is additionally **§7.6-reflexively-gated**.

---

# 8. Relationships (STD-0004)

- `part_of` the Knowledge Base — a **classification** statement, not a typed graph edge ("Knowledge Base" is not a resolvable object; no `part_of` target declared in frontmatter — matching INV-0009…INV-0017).
- **Frontmatter edges at opening: none.** Per **ADR-GOV-0004 D4**, frontmatter references are graph claims and may name only existing objects. At scaffold, **no accurate typed edge to an existing object exists at the INV level:** the catalogued sources attach to **child claims** created at circuit, not to INV-0018 itself, and those children do not yet exist. Declaring any child, source, or inheritance edge now would assert a relationship the record does not yet have. The planned subgraph is declared in prose here and edged at execution.
- **Planned subgraph (populated at execution; existing STD-0004 types only, none invented):** INV-0018 is the **hub**.
  - **Four claims (CLM, identifiers assigned at execution; expected range beginning CLM-0095):** each `part_of` INV-0018, `supports` the finding, and `derived_from` its cited source(s). **CLM D** `derived_from` the primary text (SRC-0151) **only in the self-understanding register.**
  - **One tradition entity (ENT, identifier assigned at execution; expected ENT-0015):** created on demand (D2), carrying `tradition_type` / `dating_claims` / `display_range` and the v1.11 positioning fields.
  - **`branches_from` edges: UNDETERMINED.** **Whether ANY `branches_from` edge exists is the circuit's FINDING, not a scaffold assumption** (§2.2). Under the edge-restraint rule (§3.1), the honest outcomes include **zero edges** — Islam rendering as an **unconnected node** on the timeline — and that outcome requires **no** repair. If an edge is warranted, it is ENT→ENT, qualifier-carrying from the six-value provisional list, and warrant-paired with a graded claim.
  - **Finding (FND, expected FND-0018):** `derived_from` the four claims, `part_of` INV-0018.
  - **Source-to-source edges among SRC-0143…SRC-0151 already exist** (catalogued this session, §2.5) and record the **literature's real tension as a tension** — explicitly **NOT** an INV-0018 verdict. They are not modified at circuit.
  - **Cross-family relations:** any relation to the Iranian family or to traditions outside this family is **prose only**; no typed cross-family edge is drawn.
- **Entity creation is deferred to circuit** (ADR-GOV-0009 D2); this scaffold creates **no claim, entity, edge, or finding.**

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-23|Draft|Opened as scaffold per owner-ratified brief (brief 1 of 2). **FAMILY 3 of the ADR-GOV-0009 world-religions timeline program (D5) — Islam.** Scope: **ONE tradition entity**; **Sunni/Shia DEFERRED** to a later separate investigation (§2.4). **The modeling question is held OPEN with three named hypotheses, none pre-adopted** (multi-parent descent / separate root with influence and no descent edge / a mix) — §1, §2.2. **EDGE-RESTRAINT RULE stated as operative discipline** (§3.1): influence is not descent, and a disconnected timeline node is an honest rendering. Four-claim decomposition (A emergence-and-dating · B relationship to Judaism · C relationship to Christianity · D self-understanding), each with separable (i)/(ii)/(iii) elements. **Acute neutrality requirement** recorded as three reviewer-checked guards: dual-track (both slides), revisionist-as-scholarship with reception disclosed, consensus-asymmetry; no confessional or supersessionist framing in any direction; all three traditions' metaphysical claims bracketed. **Anchor Fit Assessment RESERVED in two parts** (§ Anchor Fit): PART 1 multi-parent = the possible second demonstrating case for the deferred AF-2; PART 2 edge-type adequacy = if the relationship proves influence-shaped, **INV-0011 is the pre-existing first case and Islam the second** for a possible `influenced_by` edge type — assess and recommend only, never self-applied. **Islamic-studies source base catalogued this session (SRC-0143…SRC-0151, nine records, ADR-GOV-0003 pattern: catalog only, grade nothing)**; residual gaps reported (Arabian Jewish communities; documentary/epigraphic evidence; Arabic/Syriac-language scholarship). **Zero claims/entities/edges/findings — awaiting circuit under brief 2.** Native `Level N` only; everything R0; §7.5-analog gate declared at opening, findings not cleared for external reliance; Anchor Fit additionally §7.6-gated. No frontmatter relationship edges (D4); no new edge type; no source-base, closed-record, Standard, template, tool, Baseline, or ADR modification.|
|0.2|2026-07-23|Draft|**FULL OPS-0003 CIRCUIT EXECUTED AND RECORD CLOSED** (brief 2 of 2, under the owner's conditional pre-authorization; ADR-GOV-0004 D1). **THE MODELLING QUESTION RESOLVED TO HYPOTHESIS (b): a separate root with influence relationships and NO descent edge** — (a) multi-parent descent and (c) a mix unsupported on this base. Created **CLM-0095** (emergence and dating: seventh-century CE Arabian emergence **Level 4/High**, earned on the mainstream/revisionist cross-pole convergence test; confessional crystallisation Moderate; revisionist re-dating adjudication Low; `tradition_type` fit Moderate), **CLM-0096** (relationship to Judaism: **influence, not descent**, Moderate; Arabian Jewish community character **Low**), **CLM-0097** (relationship to Christianity: **influence, not descent**, Moderate, reasoned independently by a different route; transmission mechanism Low), **CLM-0098** (self-understanding: restorationist account Moderate as a reported fact, terminology **Low** for the translation limit), **ENT-0015 Islam** (`tradition_type: founded`; bounds 610 → present, `range_uncertainty: moderate`), and **FND-0018** (seven components; one Level 4, no Level 5, one Low). **THE EDGE DECISION: ZERO `branches_from` edges — Islam is the program's FIRST DELIBERATELY UNCONNECTED TRADITION NODE.** The refusal is recorded and reviewer-verified against six explicit tests; the descent bar was stated before the evidence was measured; the base's one descent-shaped reading (*Hagarism*) was weighed and failed on its own recorded reception rather than being dismissed; **`disputed` was not used to hedge for influence**, and `heterodox-offshoot` / `syncretic-descent` were refused with reasons. **THE ENTITY-PRECISION REQUIREMENT (owner ruling) WORKED IN FULL AND PRODUCED TWO RECORDED ENTITY GAPS OF DIFFERENT SHAPES:** ENT-0012 Second Temple Judaism **fails the chronological-coherence check** (`range_end_year: 70`); ENT-0014 Rabbinic Judaism passes chronologically but **over-specifies**; ENT-0013 Christianity passes chronologically but is **too coarse**. **No entity created; no edge forced onto an approximate target;** both gaps routed to Anchor Fit and kept structurally independent of the edge refusal. **Anchor Fit completed and routed in THREE parts: PART 1 NEGATIVE** (AF-2 gets no second demonstrating case; deferral stands), **PART 2 FIRES** (INV-0011 first case, Islam second, bar cleared in one step; candidate `influenced_by` fully specified — direction, ENT→ENT, multi-target, minimal provisional qualifier list, warrant-plus-required-not-descent-determination, subordinate render — **and NOT created**, with the caveat that the edge-type and entity-resolution questions must be governed together), **PART 3 OBSERVATION ONLY** (restorationist self-account is claimed descent across a discontinuity, named by no qualifier, kin to the anticipated revival case, but a **pressure** case not a demonstrating one, since a self-account may never be encoded as a lineage edge; CLM-0098's grade unmoved). Fourth observation routed: **entity resolution** as a first-class anchor question. **Critical Review – RQ-0018: CONFORMANT WITH FLAGS** — three determinate flags **all remediated in-session** (parametric-disclosure on the Syriac-substratum mention; uniform parametric general-reference disclosures on the three historical claims; the "three families" wording in FND-0018), three advisory non-blocking; **no confidence level raised and none lowered.** **ROLE-0001 validation in-record (§6b): `validate.py` 391 files 0 errors / 0 warnings exit 0; `graph_integrity.py` 0 dangling / 0 branch errors exit 0, advisory counts unchanged; scale-discipline grep clean; subgraph matches §8.** All ten §7 criteria re-assessed and ticked with in-record evidence (criterion 3 on its second limb). Verification-light throughout with two named base holes (no dedicated Arabian-Judaism source; no Syriac-language scholarship); four framing anchors live-verified at general-reference level; **no Qur'anic passage quoted, paraphrased, or cited at verse level**; everything **R0**, **findings NOT cleared for external reliance regardless of closure**, Anchor Fit additionally §7.6-gated. Frontmatter `status` untouched (ADR-GOV-0005 §1). No standard, template, tool, ADR, Baseline, prior investigation, or source base modified.|

# End INV-0018
