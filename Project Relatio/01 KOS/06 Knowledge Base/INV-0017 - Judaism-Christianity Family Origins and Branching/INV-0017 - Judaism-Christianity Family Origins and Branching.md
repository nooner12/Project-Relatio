---
title: INV-0017 - Judaism-Christianity Family Origins and Branching
document_type: Investigation Record
version: 0.4
status: Draft
operational_status: Active
created: 2026-07-22
category:
  - Knowledge Base
  - Religious Studies
  - Judaism and Christianity
  - Investigation
parent_documents:
  - KOS-0008 Research Methodology & Investigation Framework
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - KOS-0007 Comparative Analysis Framework
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Investigation
  - JudaismChristianity
  - WorldReligionsTimeline
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-22
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# INV-0017

# Judaism–Christianity Family Origins and Branching — The Second Temple Root and the Descent of Christianity and Rabbinic Judaism (the "Parting of the Ways")

## Draft Investigation Record

> ## ✅ CLOSED — 2026-07-22 (full OPS-0003 circuit complete)
> **This investigation is formally CLOSED per ADR-GOV-0004 D1, under the owner's conditional pre-authorization in the circuit brief (brief 2 of 2).** The full adversarial circuit ran: Research Specialist (ROLE-0002) → Critical Reviewer (ROLE-0004, verdict **Conformant with Flags**, [[Critical Review - RQ-0017]]) → Knowledge Architect (ROLE-0001, structural validation clean, §6b). All eight §7 acceptance criteria are met with in-record evidence (§7). Closure conditions verified: **(a)** all criteria met — both `branches_from` edge-warrant pairs reviewer-verified per-edge, the single-hub §2.3 justification recorded, the Anchor Fit Assessment completed and routed; **(b)** verdict Conformant with Flags with **zero determinate flags** (three advisory, non-blocking, reported); **(c)** **no confidence level raised**; **(d)** both validators clean (`validate.py` 371 files 0/0; `graph_integrity.py` 0 dangling / 0 branch errors).
>
> **This is FAMILY 2 of the ADR-GOV-0009 world-religions timeline program — the second population of the timeline anchors** (the first fork: one hub, Second Temple Judaism, branching into BOTH Christianity and Rabbinic Judaism). Created: **CLM-0092/0093/0094**, **ENT-0012/0013/0014**, **FND-0017**, and the two `branches_from` edges.
>
> **"Closed" is NOT a maturity promotion** — the frontmatter `status` stays **Draft** (ADR-GOV-0005 §1: closure state lives in this banner and the history row, not in frontmatter). **"Closed" is NOT a clearance for external reliance:** everything lands **R0** and the **findings are NOT cleared for external reliance regardless of closure** (STD-0006 §7.5-analog — verification-light for the Jewish-tradition dating; the world-religions timeline is public-facing in ambition; genuinely independent re-verification is the gate-lift). The **Anchor Fit recommendations are additionally §7.6-reflexively-gated** (GB-2026-041) — they may not promote the provisional `branches_from` / qualifier / §2.3 anchors from provisional toward durable absent blinded independent review.

> Authored using **TPL-0003**. Seventeenth research workflow (RQ-0017). **Opened as a scaffold**; to be executed and closed through the full adversarial circuit (OPS-0003: Research Specialist → Critical Reviewer → Knowledge Architect; Vision Steward/owner closes). The opening/closing split is structural (**STD-0006 §7.6** independence principle): the session that authored this scaffold does not itself generate and certify the findings that fill it. The circuit runs under a separate brief (brief 2 of 2) after owner review. **The RQ freeze checkpoint is the owner's review of this scaffold report** — the §1 primary wording is authoritative pending that freeze.

> **Program context — this is FAMILY 2 of the world-religions timeline program (ADR-GOV-0009 D1),** the first successor to INV-0016 (the Iranian family). Its subject is the **Judaism–Christianity "parting of the ways."** The family is modelled as **one fork**: a single parent — **Second Temple Judaism** — branching into **BOTH** Christianity **and** Rabbinic Judaism. Modelling the fork *as a fork* is deliberate and load-bearing (see §2.2): showing only the Christian branch would falsely imply Second Temple Judaism "became" Christianity, when its main line continued as Rabbinic Judaism. Nothing here creates any entity, claim, or edge; the circuit does.

> **Source posture — REPORT THE GAP, DO NOT AUTO-CATALOG (owner-ratified).** Unlike the Iranian family, this family has **no dedicated standing source base.** Existing coverage is **partial and asymmetric**: the Christianity side is served well by the New Testament corpus already in the vault (**SRC-0091…SRC-0103**, catalogued for INV-0013/INV-0014), and the descent question is partly served by inheritance (**INV-0011 CLM-0058**; INV-0013/INV-0014). **Dating Second Temple Judaism and Rabbinic Judaism *as traditions* may require a few Jewish-studies sources the vault does not yet hold.** This scaffold's job is to **identify** that coverage need (see §2.4) — it **creates no source and assumes none exists.** If a catalog extension is warranted, that is a **SEPARATE owner-approved step** (the precedent is the Iranian catalog authorised under **ADR-GOV-0003**), decided at or after RQ-freeze, not here.

> **Cross-investigation inheritance (owner-ratified).** Three closed records seed this family and are **CITED by layer inheritance, never re-derived or edited**: (a) **CLM-0058 — Nazarene Inheritance from Second Temple Apocalypticism (INV-0011)** is the **seed warrant for the Christianity descent edge**; (b) **INV-0013 / INV-0014** supply **first-century dating anchors** for Christianity's emergence; (c) INV-0011's Second-Temple-apocalypticism material is **context** for the Second Temple Judaism hub. **Identifiers are VERIFIED at execution; on any discrepancy the cited claim wins over this brief's label.** INV-0011, INV-0013, INV-0014 and every other closed record are cited, never re-opened.

> **Anchor stress-test duty (ADR-GOV-0009 §7(a)).** This family is the **sharpest test yet** of the `branches_from` qualifier list. **Christianity is a schism-class case** (a movement that separated from its parent). **Rabbinic Judaism is a CONTINUATION / main-line case** — the parent tradition's own line reconstituting after 70 CE — and the current controlled list (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed`) **may not contain a right word for it.** Whether `reform` is the least-wrong fit, or the vocabulary needs a new qualifier for main-line continuation, is exactly the **Anchor Fit Assessment** deliverable (reserved below). Per **ADR-GOV-0007 §3** the finding is a **RECOMMENDATION routed to GB-2026-041 / the review queue — NEVER a self-applied structural change.** Nothing in this investigation amends STD-0004, STD-0002, TPL-0006, or any standard.

> **Metaphysical neutrality — acute for this family.** The truth claims of all three traditions are **bracketed entirely**, in a **neutral historical register**. This matters with particular force here: the circuit adopts **neither a supersessionist frame** (Christianity as the fulfilment/replacement of Judaism) **nor a polemical frame** in any direction. See §2.1 and the DO-NOT list.

> **Verification & reliance note (STD-0006 §7.5 analog).** Historical religious-studies investigation — **not health/high-stakes, not child-facing** — no health gate. It is, however, **externally consequential** (the world-religions timeline is public-facing in ambition) **and verification-light-expected** for the Jewish-tradition dating (where vault coverage is thin). The Specialist and the Critical Reviewer **must each disclose their verification strength**, and **everything lands R0 — the findings are NOT cleared for external reliance regardless of closure.** Genuinely independent re-verification is the gate-lift.

> **Scale discipline.** Every on-record confidence rating — frontmatter and every grading field — is native **`Level N (Label)`** (KOS-0003 §8), the only authorized on-record confidence vocabulary. No H-band in any frontmatter or grading field; no ★-glyphs anywhere in any Knowledge Object. The optional H-band typology may appear in prose only.

> **Provisional-anchor note (ADR-GOV-0007 §2 / STD-0004 v1.2 / STD-0002 v1.11).** `branches_from` is PROVISIONAL. **No tradition entity, dating claim, or `branches_from` edge is created by this scaffold** — entities are created on demand at circuit (ADR-GOV-0009 D2), and every lineage edge is warranted by a graded claim and reviewer-verified (the warrant rule). At circuit the three entities are **born timeline-ready**, carrying the render-only STD-0002 v1.11 positioning fields (`range_start_year` / `range_end_year` / `range_uncertainty`) **derived from and bounded by each tradition's dating claim** (confidence-inheriting; `display_range` stays authoritative) — noted here as a circuit deliverable so **no backfill is ever needed**. *(Template note: TPL-0006 v1.0 predates STD-0002 v1.11 and its tradition-class skeleton does not yet list the three render-only positioning fields; they are optional/additive at validation, so the circuit adds them per STD-0002 §11 v1.11 directly — flagged to the owner in the scaffold report as a possible TPL-0006 refresh, which is an owner-reserved template change and is NOT made here.)* This session lays no anchors of its own and populates none; it frames the work that brief 2 executes.

---

# 1. Research Question

**Primary (authoritative wording pending owner freeze at scaffold review):**

> What can be established, and at what evidential grade, about the origins and historical branching of the Judaism–Christianity family — the emergence and dating of Second Temple Judaism, and the descent of both Christianity and Rabbinic Judaism from it (the "parting of the ways") — including the nature of each descent relationship?

**Decomposition mandate (owner-ratified): THREE claims, one per tradition** (identifiers assigned at execution, not here), **each answering three explicitly separable elements** — the lesson encoded from INV-0011 criterion #2 that "treated in prose" is not "answered separably", and applied throughout INV-0016:

- **CLM (Second Temple Judaism — the HUB/root for this family):**
  - **(i) EMERGENCE / DATING BOUNDS.** What the sources establish about the emergence and bounds of Second Temple Judaism *as a tradition* — the Second Temple period framing (roughly the post-exilic return through the destruction of the Second Temple in 70 CE), reported at grade, with contested bounds reported as contested (dates are claims — ADR-GOV-0009 D3; no false precision).
  - **(ii) ROOT POSITION FOR THIS FAMILY.** Its position as the family **root** — with the explicit statement that its **own upstream descent (from Israelite/Yahwistic religion) is DEFERRED to a later "family 2-deep" investigation (§2.5)** and is **not asserted here**; hence **no `branches_from` on Second Temple Judaism** in this family.
  - **(iii) RIVAL READING.** The strongest counter-reading of its **periodization or coherence as a single "tradition"** — e.g., whether "Second Temple Judaism" names one tradition or a **period containing several distinct sects/Judaisms** (Pharisaic, Sadducean, Essene, apocalyptic, Hellenistic) — steelmanned, with its survival and its cost to confidence stated. (This is also the §2.3 distinctness-threshold case for this family.)

- **CLM (Christianity):**
  - **(i) EMERGENCE DATING.** First-century-CE emergence, **inheriting the INV-0013 / INV-0014 first-century dating anchors** (cited, not re-derived), at grade.
  - **(ii) DESCENT + QUALIFIER.** Descent from Second Temple Judaism, and the **`branches_from` qualifier the evidence supports** (working expectation: schism-class), stated with the justification that will warrant the edge at circuit — **warrant seeded by CLM-0058** (the Nazarene inheritance). The qualifier is a **test, not a conclusion.**
  - **(iii) RIVAL READING.** The strongest counter-reading — e.g., Christianity as a **fully new religion** versus an **intra-Jewish movement that only later separated**; and the "parting" as **early and sharp** versus **late and gradual** (the Boyarin-style "ways that never parted" reading) — steelmanned, with its cost to confidence stated.

- **CLM (Rabbinic Judaism):**
  - **(i) EMERGENCE DATING.** Post-70-CE emergence (the rabbinic movement consolidating after the Temple's destruction; the Mishnah c. 200 CE as a dating anchor), at grade, contested bounds reported as contested.
  - **(ii) DESCENT + QUALIFIER — THE ANCHOR STRESS-TEST.** Descent from Second Temple Judaism **as the CONTINUATION / main line**, and its qualifier. **If no listed qualifier (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed`) cleanly fits the main-line-continuation case, the circuit SAYS SO, records it as Anchor Fit material, and chooses the LEAST-WRONG value with the tension explicitly stated** — it does not silently force a fit.
  - **(iii) RIVAL READING.** The **rupture-versus-continuity** debate — how much Rabbinic Judaism is a **continuation** of Second Temple Judaism versus its own **reconstitution / reinvention** after the Temple's destruction — steelmanned, with its cost to confidence stated.

**Working hypotheses — to be TESTED at circuit, NOT assumed** (the evidence may overturn any of these; the qualifier column especially is the anchor stress-test, not a conclusion):

| Tradition | Root/descent working hypothesis | Working `branches_from` qualifier (to test) |
|---|---|---|
| Second Temple Judaism | Family **root** (for this family; own upstream descent deferred) | — (no edge; root) |
| Christianity | Schism-class branch from Second Temple Judaism | `schism` |
| Rabbinic Judaism | **Continuation / main line** of Second Temple Judaism | **no listed qualifier clearly fits** — least-wrong candidate `reform`; **Anchor Fit material** (§7(a)) |

These are hypotheses under test. Whether the qualifier list contains a right word for **main-line continuation** is itself the sharpest anchor-stress question of the program to date (see the reserved Anchor Fit Assessment); the circuit must not treat `reform` as settled.

---

# 2. Scope & Disambiguation

## 2.1 Metaphysical neutrality (acute for this family)

The three traditions' truth claims are **bracketed entirely.** This is **historical dating and descent**, in a **neutral religious-studies register** — no confessional framing in any direction, and no theological adjudication of any tradition's self-account. For this family the neutrality discipline is **load-bearing and explicit**: the circuit adopts **neither a supersessionist frame** (treating Christianity as the fulfilment or replacement of Judaism, or Rabbinic Judaism as a mere residue) **nor a polemical frame** against any tradition. Both branches descend from a shared parent; neither is the "true" continuation in any normative sense the record asserts.

## 2.2 The fork model (one parent, two edges — load-bearing)

The "parting of the ways" is modelled as **ONE fork**: a **shared parent** (Second Temple Judaism) with **two `branches_from` edges**, one to Christianity and one to Rabbinic Judaism. The two branches are investigated **together**, because **each branch's descent question bounds the other**: what one inherits from the parent, and when it separates, is defined partly by contrast with the other. Modelling only the Christian branch would falsely imply Second Temple Judaism *became* Christianity; in fact its main line continued as Rabbinic Judaism. The fork is therefore not a presentational choice but a **claim about the history**, and the two-edge structure is required to state it honestly.

## 2.3 Distinctness threshold — what counts as a TRADITION vs. a period/current (the Iranian §2.3 criterion applies)

The Iranian family's **§2.3 distinctness threshold applies unchanged**: a formation warrants its own **tradition-class Entity Record** (and a place in the branching graph) when the source base treats it as a **distinct religious tradition** — evidenced by (a) an identifiable community, adherents, or transmission lineage of its own; (b) a distinguishing doctrinal or organizational core; and (c) recognition in the literature as a *named tradition* rather than a *period, tendency, or current*.

**Its sharpest case here is the hub itself: is "Second Temple Judaism" one tradition, or a *period* containing several distinct Judaisms (Pharisaic, Sadducean, Essene, apocalyptic, Hellenistic)?** This is a real scholarly question, and it is **flagged, not pre-decided.** The circuit applies the working criterion, records where it strains (this hub case in particular — it is the §1(iii) rival reading for the Second Temple Judaism claim), and reports the strain to the Anchor Fit Assessment; it does not force a verdict to protect the criterion. The program treats "Second Temple Judaism" as the operative root **for this family**, while recording honestly whatever internal plurality the sources show.

## 2.4 Source posture and coverage assessment (report-the-gap; no source creation)

- **No source record is created at scaffold, and none is assumed.** Anti-fabrication (KOS-0003 §12.1) is absolute; no claim is thin-sourced into a grade it has not earned; UNSOURCED / insufficient-base outcomes are legitimate and recordable.
- **Coverage that EXISTS in the vault:**
  - *Christianity side (well covered):* the **New Testament corpus SRC-0091…SRC-0103** (Metzger & Ehrman, Ehrman, Brown, Sanders, Meier, the primary NT texts, the non-Christian testimonia, etc.), catalogued for INV-0013/INV-0014, serves Christianity's emergence dating and its Second-Temple-Jewish matrix.
  - *Descent question (partly covered by inheritance):* **INV-0011 CLM-0058** (Nazarene inheritance from Second Temple apocalypticism — the seed warrant for the Christianity edge); **INV-0013 / INV-0014** (first-century dating anchors); INV-0011's Second-Temple-apocalypticism material (context for the hub).
- **Coverage that is likely MISSING (the gap this scaffold reports):** dedicated **Jewish-studies sources for dating the two Jewish traditions *as traditions*** — (a) **Second Temple Judaism** as a period/tradition (its bounds, its internal plurality) and (b) **Rabbinic Judaism** (post-70-CE emergence; the Mishnah c. 200 CE; the rupture-vs-continuity scholarship; the "parting of the ways" literature, e.g. the Dunn / Boyarin / Schäfer strands). The existing NT-corpus sources touch the Second-Temple-Jewish *matrix of Christianity* but were **not** catalogued to date **Rabbinic Judaism** or to bound **Second Temple Judaism as a tradition in its own right.**
- **Whether a catalog extension is needed:** on the coverage assessment above, the circuit is **likely to need a small Jewish-studies source extension** to grade the two Jewish-tradition dating claims at anything above a thin base. **That extension, if warranted, is a SEPARATE owner-approved step** (the ADR-GOV-0003 Iranian-catalog precedent) — **decided by the owner at or after RQ-freeze, not created or assumed here.** If the owner declines the extension, the circuit grades those claims honestly on the available base (a thin-base / lower-grade outcome is pre-authorized, not a failure).

## 2.5 Boundaries

- **Deeper Jewish roots are OUT OF SCOPE (deferred to a later "family 2-deep").** The upstream descent of Second Temple Judaism — from **Israelite / Yahwistic religion** and the **Canaanite substrate** — is a **separate later investigation.** Second Temple Judaism is treated as the **root for this family**; its own upstream descent is **not asserted**, and **no `branches_from` is placed on Second Temple Judaism** in this investigation.
- **With INV-0011 / INV-0013 / INV-0014 (cite, never re-derive).** CLM-0058 and the first-century dating anchors are **inherited under the layer-inheritance rule (§3.1)**; those investigations are not edited, re-opened, or re-derived. Their identifiers are verified at execution and the cited claim wins on any discrepancy.
- **With the NT corpus (consume, never modify).** SRC-0091…SRC-0103 are cited only; no catalogued source record is touched.
- **With future families (no cross-family edges).** No `branches_from` edge or any typed edge is drawn to a tradition **outside** this family (e.g., no edge to Islam, and none up into the deferred Israelite-religion root). Cross-family relations, if noted, are prose only.

## 2.6 Scale posture

Native **`Level N`** only in every frontmatter and grading field. The H-band typology may be used in **prose only** (optional), and carries no grading authority. No ★-glyphs anywhere.

## 2.7 Reliance posture

**Everything lands R0.** Verification-light close is expected for the Jewish-tradition dating where vault coverage is thin (§2.4). Findings are **NOT cleared for external reliance regardless of closure** — the §7.5-analog gate is declared here, at opening, before any evidence.

## 2.8 Terminology

- **"Judaism–Christianity family"** denotes, for this investigation, the fork rooted in **Second Temple Judaism** and branching into **Christianity** and **Rabbinic Judaism**. The **deeper Israelite/Yahwistic root is excluded** (§2.5).
- **"Parting of the ways"** is the scholarly shorthand for the historical separation of Christianity and Rabbinic Judaism from their shared Second-Temple matrix; its timing and sharpness are **contested** and are part of the §1(iii) rival readings, not presupposed.
- **`branches_from` qualifiers** (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed`, STD-0004 §7.2) are **distinct from** `tradition_type` **values** (`founded` / `emergent` / `reform` / `syncretic`, STD-0002 §11) — the two vocabularies are not interchangeable and are not conflated in any record. Note that `reform` appears in **both** vocabularies with different meanings; the circuit must keep them distinct (a `tradition_type: reform` entity is not automatically a `qualifier: reform` edge, and vice versa).

---

# 3. Method / Protocol

Execution follows the KOS-0003 pipeline (Question → Claims → Assumptions → Evidence → Confidence) through the **full OPS-0003 circuit**. Claims via **TPL-0001**; the three tradition entities via **TPL-0006 tradition-class skeleton** (born conformant — `tradition_type`, `dating_claims`, `display_range`, and any qualified `branches_from` edges present from birth, STD-0002 v1.10 — **and the render-only STD-0002 v1.11 positioning fields `range_start_year` / `range_end_year` / `range_uncertainty`**, derived from each tradition's dating claim, confidence-inheriting, `display_range` authoritative — the honesty keystone, so no backfill is needed); the synthesis via **TPL-0004**. Sources are **cited** from what the vault holds (SRC-0091…SRC-0103 and the inherited claims), and **no new source is created at circuit without a separate owner-approved catalog extension** (§2.4). All identifiers registered in the Identifier Registry at execution.

## 3.1 Operative disciplines (bind at circuit)

> **WARRANT RULE (review-checked, not tool-checked).** Every `branches_from` edge written at circuit **MUST be warranted by a graded claim** asserting the descent (the edge renders; the claim warrants). `graph_integrity.py` enforces only the *structural* constraints (ENT→ENT, required/controlled qualifier) — it **cannot** verify the warrant, because a warrant is a claim about lineage, not a structured pointer. **The Critical Reviewer therefore verifies each of the two edge-warrant pairs explicitly.** An unwarranted edge is a defect the reviewer must catch. The Christianity edge's warrant is **seeded by CLM-0058** (verified at execution); the Rabbinic Judaism edge's warrant is authored fresh from the continuation/rupture evidence.

> **LAYER-INHERITANCE.** A dating or descent claim that **cites a closed investigation** (CLM-0058 in INV-0011; the first-century anchors in INV-0013/INV-0014) is **bounded by the cited claims' grades** — the inheriting claim may not exceed the cited claim's grade on the shared question. A claim resting on **thin or absent vault coverage** (the two Jewish-tradition dating claims, absent a catalog extension) is **bounded by that thin base** — which is why lower grades are anticipated there (§2.4).

## 3.2 Per-claim structure

Each of the three tradition claims answers elements **(i) emergence/dating**, **(ii) descent (or root) relationship**, and **(iii) rival reading** in **explicit, separable sections** of the claim record — not diffused through prose (§1; acceptance criterion 1). The Rabbinic Judaism claim's element (ii) additionally carries the **least-wrong-qualifier-with-stated-tension** treatment (§1; the anchor stress-test).

## 3.3 Entity-on-demand, dates-as-claims, and born-timeline-ready positioning

- Tradition entities are created **only as their claims warrant them** (ADR-GOV-0009 D2) — no pre-populated gazetteer.
- **Dates are claims** (D3): the entity carries `dating_claims` pointers and a render-only `display_range`; the sourced, graded, epistemic-fielded date lives in the CLM, and **there is no `origin_date` field.** Contested dating is carried as contestedness in the claim, never flattened into a false-precision range on the entity.
- **Born timeline-ready (STD-0002 v1.11):** each entity additionally carries the render-only positioning fields `range_start_year` / `range_end_year` / `range_uncertainty`, **derived from and bounded by its dating claim** (`range_uncertainty` mapping from the dating component's confidence; a bar never renders more certain than the claim behind it; `display_range` stays authoritative and is shown verbatim). Populating these at birth is a **circuit deliverable**, so the timeline renders proportionally with no later backfill. (TPL-0006 v1.0 does not yet list these optional fields — the circuit adds them per STD-0002 §11 v1.11 directly; see the scaffold-report flag.)

---

# 4. Findings / Synthesis

*Populated at circuit execution (Specialist pass, 2026-07-22); pending ROLE-0004 review and ROLE-0001 validation.*

Primary synthesis is **FND-0017 — Origins and Branching of the Judaism-Christianity Family**, a **layered verdict by tradition** (native `Level N`, per-component, never averaged):

- **Second Temple Judaism — family root** (root + single-tradition status **Moderate**; emergence dating **Moderate**). The shared Jewish matrix (Temple, Torah, covenant God), bounded by the Second Temple period c. 516 BCE – 70 CE (period bounds live-verified; tradition-emergence contested). Modelled as **one internally-plural tradition** (Pharisees, Sadducees, Essenes, apocalyptic, Hellenistic = parties within, not distinct traditions) — a reasoned finding against the §2.3 threshold via the common-Judaism substrate, plural-Judaisms rival costed in. **No `branches_from` edge** (upstream Israelite/Yahwistic descent deferred to a later family 2-deep). Claim **CLM-0092**; entity **ENT-0012**.
- **Christianity — 1st-c.-CE schism-class branch** (emergence + descent **High**, inherited; `schism` qualifier fit **Moderate**). Earliest Jesus movement a Second-Temple Jewish sect (seed warrant **CLM-0058**, High), anchored by the closed first-century results (**CLM-0075/0076/0068**, inherited not re-derived). `branches_from` Second Temple Judaism, qualifier **`schism`** — least-wrong for "separated to become distinct," with a load-bearing caveat that the parting was gradual/late/uneven (Boyarin, Becker & Reed, against Dunn). Claim **CLM-0093**; entity **ENT-0013**.
- **Rabbinic Judaism — post-70-CE continuation / main line** (emergence + descent **Moderate**; continuation-qualifier fit **Low** — the anchor stress-test). Consolidated after 70 CE (Yavneh; Mishnah c. 200 CE, SRC-0142), continuing the Pharisaic stream. `branches_from` Second Temple Judaism, qualifier **`reform`** — the controlled list has **no** value for main-line continuation; `reform` is least-wrong under protest, `reform_qualifier_fit` graded **Low** to encode the vocabulary strain, with a recommendation for a new `continuation`/`main-line` qualifier routed to Anchor Fit. Claim **CLM-0094**; entity **ENT-0014**.

**The fork** (two `branches_from` edges, **both on the children**, none on the hub) is stated as a finding: Second Temple Judaism did not "become" Christianity — its main line continued as Rabbinic Judaism. **Neither branch is the normatively "true" continuation; the register is neutral throughout.** The full layered verdict, brackets, and the Anchor Fit Assessment live in **FND-0017**.

---

# 5. Confidence Summary (KOS-0003 §8)

*Assigned at circuit execution, native `Level N` only; pending circuit review.* Per-component, never averaged (FND-0017 §2):
- **second_temple_root_and_single_tradition — Level 3 (Moderate).**
- **christianity_emergence_and_descent — Level 4 (High)** — the one High component, **inherited** from the closed CLM-0058/0068/0075/0076 spine (bounded at those grades per §3.1; not re-derived).
- **christianity_schism_qualifier — Level 3 (Moderate)** — the gradual/late parting complicates the `schism` label.
- **rabbinic_emergence_and_descent — Level 3 (Moderate)** — post-70 / c. 200 CE framing firm; continuity-vs-rupture contested; interiors parametric.
- **rabbinic_continuation_qualifier — Level 2 (Low)** — no listed qualifier fits main-line continuation; `reform` least-wrong under protest (Anchor Fit).

**No Level 5 anywhere; exactly one Level 4 (the inherited Christianity spine), the rest Moderate or Low** — the honest outcome, as anticipated at opening: the Christianity emergence rests on inherited High-graded closed records, while the two Jewish-tradition datings rest on a **parametric/unread** Jewish-studies base (SRC-0137…0142) and are graded Moderate accordingly, and the Rabbinic continuation qualifier is bounded by the anchor-fit vocabulary strain, not by evidence strength alone. Everything R0; not cleared for external reliance.

---

# 6. Assumptions & Bracketing (KOS-0003 §10)

*Expanded at circuit execution (Specialist pass, 2026-07-22). The actuals held at circuit:*
- **Single-tradition modelling of the hub** was applied (not merely assumed): Second Temple Judaism modelled as one internally-plural tradition via the common-Judaism substrate, with the plural-Judaisms rival steelmanned and costed into the Moderate grade (CLM-0092 (iii)).
- **Inheritance held:** CLM-0058 (seed warrant) and CLM-0068/0075/0076 (first-century anchors) were inherited at their grades and cited, not re-derived; the closed INV-0011/0013/0014 records were not modified.
- **Source posture held:** the Jewish-studies base SRC-0137…0142 was cited from its bibliographically-verified but **parametric/unread interiors**; no page-level claim was drawn from any of them; no source was created or modified; period-frame facts were live-verified at general-reference level and disclosed as such (§ Verification-strength disclosure below).
- **Qualifier vocabulary treated as possibly-inadequate** for the Rabbinic case, not force-fit: `reform` used as least-wrong under protest with the tension recorded and a routed recommendation.

*The standing brackets and disciplines below bind from opening:*

- **Metaphysical bracket, acute (§2.1).** Every tradition's truth claims are bracketed; the register is neutral historical religious studies, in no direction — **neither supersessionist nor polemical.**
- **The fork is a claim, not a layout (§2.2).** Two edges from one parent; each branch's descent bounds the other; neither branch is the normatively "true" continuation.
- **Deeper roots deferred (§2.5).** Second Temple Judaism is the root **for this family only**; its own upstream descent is not asserted and carries no edge.
- **No directional premise on descent or qualifier.** Each working hypothesis in §1 is **tested, not assumed** — the Christianity qualifier and especially the Rabbinic Judaism continuation-qualifier are open questions; a "least-wrong with stated tension" or an Anchor-Fit-routed vocabulary gap is a legitimate result.
- **Inheritance not re-derivation (§2.5, §3.1).** CLM-0058 and the first-century anchors are inherited, bounded by their grades; the closed investigations are not re-opened.
- **Source posture holds (§2.4).** No source is created or assumed; a catalog extension is an owner decision; thin-base outcomes are pre-authorized.

---

# Anchor Fit Assessment (ADR-GOV-0009 §7(a) stress-test deliverable)

> **Completed at circuit execution (Specialist pass, 2026-07-22). The full Anchor Fit Assessment lives in FND-0017 §4 (four routed recommendations); it is summarised here.** Per **ADR-GOV-0007 §3** every finding is a **RECOMMENDATION routed to GB-2026-041 / the review queue — never self-applied.** This investigation amends no standard, template, or tool.
>
> 1. **Continuation qualifier (CENTERPIECE) — the list lacks a right word for main-line continuation.** For Rabbinic Judaism each listed value is wrong (`schism` = a break away; `heterodox-offshoot` = deviant/mildly polemical; `syncretic-descent` = multi-parent; `disputed` = uncertain descent). `reform` is **least-wrong** but understates the least-departed line as a departure; the rupture and continuity rivals squeeze it off-centre in opposite directions. **RECOMMENDATION:** add a **`continuation`/`main-line`** qualifier to STD-0004 §7.2. Until then `reform` stands, `reform_qualifier_fit` graded Low.
> 2. **Christianity `schism` fit.** Least-wrong for "separated to become distinct" but connotes a sharp break where the parting was gradual/late. **RECOMMENDATION:** consider distinguishing sharp vs. gradual separation; for now `schism` with the caveat, `christianity_schism_qualifier` Moderate.
> 3. **Fork semantics.** The two-edge fork (both edges on the children, none on the hub; hub `range_end_year: 70`) honestly prevents "Second Temple Judaism became Christianity"; the only strain is that `branches_from` reads as "departs from," misdescribing a continuation — resolved by (1). No change to the ENT→ENT fork structure needed.
> 4. **§2.3 threshold — internally-plural root.** Discriminated under strain: internal parties are currents within one tradition, not distinct traditions (nearest pressure the extinct Essene/Qumran *sect*, which does not clear the bar). **RECOMMENDATION:** note "internally-plural root" as a recurring pattern in the threshold guidance; no structural change. Also flagged: the double-`reform` coincidence (`tradition_type` vs. `branches_from` qualifier, §2.8, same word / different vocabularies).

*Original reserved framing (retained for context):* Under the anchor stress-test duty (ADR-GOV-0009 §7(a)), this family is the **sharpest test yet** of the lineage anchors, and this section's **centerpiece is the continuation-qualifier question.** At circuit the Specialist and Critical Reviewer record findings on:

1. **Qualifier-list fit — THE CENTERPIECE.** Does the controlled list (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed`) contain a right word for **main-line continuation** (Rabbinic Judaism), or does the case fall **outside** the list? If no listed qualifier fits, the circuit states so, chooses the **least-wrong** value with the **tension explicitly recorded**, and routes a recommendation — possibly for a **new qualifier** (e.g., a `continuation` / `main-line` value) — to the review queue. Christianity's **schism-class** fit is also assessed (does `schism` capture a gradual/late separation, or does it imply an over-sharp break?).
2. **Edge semantics — the fork.** Does `branches_from`'s ENT→ENT, asymmetric, warrant-by-graded-claim semantics represent a **fork** (one parent, two edges) honestly — in particular, can it represent a **main-line continuation** without implying the parent merely "became" the other branch? Does modelling the continuation as a `branches_from` edge (which reads as "derives from / departs from") misdescribe a tradition that is the **least-departed** line?
3. **Distinctness threshold (§2.3) — the hub.** Does the tradition-vs-period criterion discriminate cleanly on **"Second Temple Judaism as one tradition versus a period of several Judaisms"**, or does it need refinement for a **root that is internally plural**?

**Per ADR-GOV-0007 §3, every finding recorded here is a RECOMMENDATION routed to the review queue / GB-2026-041 — never a self-applied structural change.** This investigation amends no standard, template, or tool. Contradiction / field-prose-divergence style items, if any, enter the Governance Backlog as explicit `REVIEW-FLAG` marker lines (tools/README.md convention); ordinary prose recommendations are carried here and surfaced to the owner at close.

---

# 6a. Verification-strength disclosure (Specialist pass, 2026-07-22)

**Asymmetric, as anticipated.**
- **Live-verified this session (strong, general-reference level — not source-interior claims):** the Second Temple period bounds (c. 516 BCE completion of the rebuilt Temple – 70 CE destruction); the post-70 rabbinic consolidation (Yavneh / Yohanan ben Zakkai); the Mishnah's redaction c. 200 CE under Judah ha-Nasi. Searched and confirmed against standard reference scholarship.
- **Inherited from closed, previously-reviewed records (not re-derived):** the Christianity emergence/descent spine — CLM-0058 (Nazarene apocalyptic inheritance, High), CLM-0068 (undisputed Pauline dating, High), CLM-0075 (Jesus existence, High), CLM-0076 (crucifixion, High / under-Pilate Moderate). Cited one-directionally; INV-0011/0013/0014 unmodified.
- **Parametric / unread (bibliographically live-verified only — the grade ceiling):** the Jewish-studies base SRC-0137 (Sanders), SRC-0138 (Cohen), SRC-0139 (Boyarin), SRC-0140 (Dunn), SRC-0141 (Becker & Reed), SRC-0142 (Strack–Stemberger). **No page-level citation is asserted from any of them.** The two Jewish-tradition dating claims are graded Moderate at this ceiling; the parting-of-the-ways positions are recorded as scholarly poles, not adjudicated from interiors this circuit did not read.
- **Not verified / bracketed:** the internal-plurality debate, the parting timing/sharpness, and the continuity-vs-rupture question are steelmanned and costed into grades, not resolved. Everything R0; nothing cleared for external reliance.

---

# 6b. Circuit outcome — Critical Review & ROLE-0001 validation (2026-07-22)

**Critical Review — RQ-0017 (ROLE-0004): verdict CONFORMANT WITH FLAGS.** Full record: [[Critical Review - RQ-0017]] (this folder). Zero determinate flags; three advisory (non-blocking) flags; **no confidence level raised**; no fabrication found. Highlights the reviewer verified independently:

- **Per-edge warrant verification (the tool cannot check this):**
  - **Christianity edge** (ENT-0013 → ENT-0012, `schism`, warrant CLM-0093 seeded by CLM-0058): edge **warranted** (descent High rests on CLM-0058 L4, does not exceed it) and qualifier **warranted** as least-wrong with the gradual/late-parting caveat encoded at Moderate. ✔
  - **Rabbinic edge** (ENT-0014 → ENT-0012, `reform`, warrant CLM-0094): edge **warranted** (descent Moderate via the Pharisaic stream) and qualifier **warranted** as an openly-declared least-wrong stand-in — the sanctioned "least-wrong with stated tension" outcome, `reform_qualifier_fit` graded Low to encode the vocabulary strain. ✔
- **Neutral register held in both directions** on every object — no supersessionist and no polemical drift (the no-"residue" / no-"fulfilment" framings do real work, not boilerplate).
- **Single-hub §2.3 justification genuinely made, not assumed** (common-Judaism substrate; interpretive-not-traditional difference); the **Essene/Qumran door-open provision honored** (nearest sub-stream flagged as a future-investigation candidate, not forced into an entity).
- **Four Specialist-flagged calibration points adjudicated:** all confirmed (CLM-0094 Low-on-vocabulary correct; CLM-0093 emergence High confirmed as scoped to the movement's 1st-c. origin; CLM-0092 Moderate confirmed; Christianity `emergent` confirmed as the neutral least-wrong `tradition_type`). No level lowered or raised.
- **Advisory flags (carried forward, not applied to the reviewed records — the body prose already disambiguates, so the review boundary is preserved):** A1 (CLM-0092 consider splitting the conjunction component at a future pass), A2 (CLM-0093 consider a "movement origin, 1st c." scoping gloss on the `emergence_dating` component), A3 (reliance_note pre-declaration — tidiness only). A1/A2 routed forward as minor recommendations (GB-2026-041 close-out note).

**ROLE-0001 structural validation (this session, 2026-07-22): CLEAN.**
- `validate.py` — **PASS**, 371 files scanned, **0 errors / 0 warnings** (epistemic + review + v1.11 range fields well-formed at birth on all seven new objects; version coherence intact).
- `graph_integrity.py` — **0 dangling references, 0 `branches_from` edge errors** (both edges ENT→ENT with controlled qualifiers `schism`/`reform`; both from ENT-0012; **none on the hub**; `dating_claims` resolve; the CLM-0058 inheritance edge one-directional into the unmodified closed record).
- **Scale-discipline grep:** no ★-glyph and no H-band token in any frontmatter or grading field of the seven new objects (the only ★/"H-band" strings in the vault subgraph are this record's rule statements).
- **Subgraph confirmed against §8:** three claims `part_of` INV-0017 + `supports` FND-0017 + `derived_from` their sources; the Christianity claim `depends_on` CLM-0058/0068/0075/0076 (inheritance) and `derived_from` the NT/Jewish-studies base; three entities on demand (ENT-0012 root/no edge; ENT-0013 `schism`; ENT-0014 `reform`); FND-0017 `derived_from` the three claims. Matches the planned subgraph exactly.

# 7. Acceptance Criteria for Closing

INV-0017 may close only when all of the following hold (modelled on INV-0016 §7, adapted):

1. [x] **MET.** Decomposed into three tradition claims — **CLM-0092** (Second Temple Judaism), **CLM-0093** (Christianity), **CLM-0094** (Rabbinic Judaism) — each with discrete `# Element (i) — Emergence Dating`, `# Element (ii) — Descent Relationship`, `# Element (iii) — Rival Reading` sections (reviewer confirmed real structural separation, not diffused prose — §6b).
2. [x] **MET.** Three tradition entities born conformant to TPL-0006 v1.1 / STD-0002 v1.11 — **ENT-0012** (`tradition_type: emergent`, no lineage edge), **ENT-0013** (`emergent`, `branches_from` `schism`), **ENT-0014** (`reform`, `branches_from` `reform`); each with co-required `dating_claims`/`display_range`, no `origin_date`, and the v1.11 positioning fields derived confidence-inheriting from its dating claim (validators clean, §6b). The internal parties (Pharisees/Sadducees/Essenes/…) are recorded as currents within ENT-0012, **not forced into entities**; the extinct Essene/Qumran sub-stream is flagged as a future candidate, not entified (§2.3).
3. [x] **MET.** Two `branches_from` edges, **both from ENT-0012** (→ ENT-0013 `schism`, → ENT-0014 `reform`), each **warrant-paired with a graded claim and reviewer-verified per-edge** (§6b: both edge- and qualifier-warrants confirmed YES). No unwarranted/off-vocabulary/ENT→non-ENT edge; **no `branches_from` on ENT-0012** (upstream descent deferred). `graph_integrity.py`: 0 branch errors.
4. [x] **MET.** Contested dating reported as contested (the 538/516 BCE spread; the tradition-emergence points; the parting timing) with no false precision; `display_range` render-only and authoritative on all three entities; the sourced/graded dates live in the claims (dates-as-claims); the v1.11 numeric bounds are confidence-inheriting (reviewer confirmed a bar never renders more certain than its claim — §6b).
5. [x] **MET.** Coverage gap reported (§2.4; the Jewish-studies extension was the owner-approved SRC-0137…0142 step, already catalogued in prep); **no new source created at circuit**; the NT corpus and SRC-0137…0142 **cited and unmodified**; CLM-0058 and the INV-0013/0014 anchors **inherited, not re-derived** (one-directional edges into unmodified closed records); thin-base outcomes graded honestly (the two Jewish-tradition datings at Moderate, the continuation qualifier at Low — no thin-sourcing).
6. [x] **MET.** Native `Level N` only — scale-discipline grep clean (no H-band/★ in any field, §6b); the **metaphysical bracket held in both directions on every object** (reviewer neutral-register check both directions: no supersessionist and no polemical drift — §6b).
7. [x] **MET.** The full OPS-0003 circuit ran (Specialist → Critical Reviewer → ROLE-0001); **verification-strength disclosure** by both Specialist (§6a) and Critical Reviewer ([[Critical Review - RQ-0017]] §9); **ROLE-0001 structural validation evidenced in-record** (§6b).
8. [x] **MET.** Anchor Fit Assessment completed and **routed as recommendations** (FND-0017 §4; INV Anchor Fit summary; GB-2026-041), never self-applied; the **continuation-qualifier question resolved to a least-wrong (`reform`)-with-stated-tension outcome plus a routed recommendation for a new `continuation`/`main-line` qualifier**; Standards, the Architecture Baseline, the prior investigations, and the Iranian source base are **unmodified** (validators + grep confirm).

**Verification & reliance (§7.5 analog).** This investigation is **externally consequential** (the world-religions timeline is public-facing in ambition) **and verification-light-expected** for the Jewish-tradition dating. **Findings are NOT cleared for external reliance regardless of closure** — a verification-light review may issue verdicts but may not clear findings for external use; genuinely independent re-verification is the gate-lift. Everything lands **R0**.

---

# 8. Relationships (STD-0004)

- `part_of` the Knowledge Base — a **classification** statement, not a typed graph edge ("Knowledge Base" is not a resolvable object; no `part_of` target declared in frontmatter — matching INV-0009…INV-0016).
- **Frontmatter edges at opening: none.** Per **ADR-GOV-0004 D4**, frontmatter references are graph claims and may name only existing objects. At scaffold, **no accurate typed edge to an existing object exists at the INV level:** the INV-0011/INV-0013/INV-0014 inheritance and the NT-corpus citations attach to **child claims** created at circuit, not to INV-0017 itself, and those children do not yet exist. Declaring any child or inheritance edge now would assert a relationship the record does not yet have. The planned subgraph is declared in prose here and edged at execution.
- **Planned built subgraph (populated at execution; existing STD-0004 types only, none invented):** INV-0017 is the **hub**.
  - **Three tradition claims (CLM, identifiers assigned at execution; expected range beginning CLM-0092):** each `part_of` INV-0017, `supports` FND-0017, and `derived_from` its cited source(s). The **Christianity claim** additionally `derived_from` / `depends_on` the NT corpus (SRC-0091…SRC-0103, one-directional into the unmodified catalogued sources — the accepted OPS-0002 §5 advisory, the INV-0014 CLM-0075→SRC-0101 pattern).
  - **Inheritance edges (one-directional into closed records):** the **Christianity claim** inherits **CLM-0058** (INV-0011) as the descent seed-warrant, and the **INV-0013 / INV-0014 first-century dating anchors**, via one-directional `depends_on` edges into those closed claims (the INV-0014 CLM-0074 precedent) — the closed investigations are **not modified**; bounded advisories.
  - **Three tradition entities (ENT, identifiers assigned at execution; expected range beginning ENT-0012):** created on demand (D2), each carrying `tradition_type` / `dating_claims` / `display_range` and the v1.11 positioning fields.
    - **Second Temple Judaism** — family **root**; **no `branches_from`** (upstream descent deferred, §2.5).
    - **Christianity** — `branches_from` **Second Temple Judaism**, qualifier per the evidence (working: `schism`), warranted by the Christianity claim (seed CLM-0058).
    - **Rabbinic Judaism** — `branches_from` **Second Temple Judaism**, qualifier per the evidence (the anchor stress-test; least-wrong with stated tension), warranted by the Rabbinic Judaism claim.
  - **Two `branches_from` edges, BOTH from Second Temple Judaism** (→ Christianity, → Rabbinic Judaism) — the fork (§2.2). No third lineage edge; **none on the parent.**
  - **Finding (FND-0017):** `derived_from` the three tradition claims, `part_of` INV-0017.
  - **No cross-family edges** (§2.5): no edge to Islam, to the deferred Israelite-religion root, or to any tradition outside this family; any such relation is prose only.
- **Entity/source creation is deferred to circuit** (ADR-GOV-0009 D2); this scaffold creates none. **Any Jewish-studies source needed to grade the two Jewish-tradition dating claims is subject to a separate owner-approved catalog extension** (§2.4) — not assumed here.

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.3|2026-07-22|Draft|**Circuit closed (Critical Review + ROLE-0001 validation + conditional closure), brief 2 of 2.** Critical Review — RQ-0017 verdict **CONFORMANT WITH FLAGS** ([[Critical Review - RQ-0017]]): zero determinate flags, three advisory (non-blocking), **no confidence level raised**, no fabrication; both `branches_from` edge-warrant pairs verified per-edge (Christianity `schism` and Rabbinic `reform` each edge- and qualifier-warranted); neutral register held both directions; single-hub §2.3 justification confirmed genuinely made (Essene/Qumran door-open honored); Anchor Fit substantive. ROLE-0001 structural validation clean (`validate.py` 371 files 0/0; `graph_integrity.py` 0 dangling / 0 branch errors; scale-discipline grep clean; subgraph matches §8) — recorded in §6b. Added the RQ-0017 review record; added §6b circuit-outcome; ticked all eight §7 criteria with in-record evidence; added the CLOSED banner. **Formally CLOSED per ADR-GOV-0004 D1 under owner pre-authorization** (all four closure conditions met). Frontmatter `status` untouched (Draft, ADR-GOV-0005 §1); everything R0, findings NOT cleared for external reliance; Anchor Fit recommendations §7.6-gated (GB-2026-041). No Standard, template, tool, Baseline, closed-record, or Iranian-base modification.|
|0.2|2026-07-22|Draft|**Circuit executed (Specialist pass, brief 2 of 2).** Created the three tradition claims (**CLM-0092** Second Temple Judaism root / **CLM-0093** Christianity / **CLM-0094** Rabbinic Judaism), the three tradition entities born timeline-ready (**ENT-0012**/**ENT-0013**/**ENT-0014**, TPL-0006 v1.1 / STD-0002 v1.11), and the synthesis **FND-0017**. **The fork:** two `branches_from` edges, both on the children — ENT-0013 → ENT-0012 (`schism`, warrant CLM-0093, seed CLM-0058) and ENT-0014 → ENT-0012 (`reform`, warrant CLM-0094); **no edge on the hub** (upstream Israelite/Yahwistic descent deferred). Layered verdict: Christianity emergence/descent High (inherited CLM-0058/0068/0075/0076), `schism` qualifier Moderate (sharpness caveat); Second Temple root/dating Moderate (single-tradition modelling via common-Judaism substrate, §2.3); Rabbinic emergence/descent Moderate, `reform` continuation-qualifier **Low** — the anchor stress-test, list lacks a word for main-line continuation, `continuation`/`main-line` recommendation routed to Anchor Fit (never self-applied). Populated §4/§5/§6/§6a and the Anchor Fit Assessment with actuals. Metaphysical/neutrality bracket held both directions; native `Level N` only; everything R0, not cleared for external reliance. Sources SRC-0137…0142 cited from parametric interiors (no page-level claim); closed records, Standards, Baseline, templates, tools unmodified. Pending Critical Review (ROLE-0004) and structural validation (ROLE-0001).|
|0.1|2026-07-22|Draft|Opened as scaffold per owner-ratified brief (brief 1 of 2). **Family 2 of the ADR-GOV-0009 world-religions timeline program (the Judaism–Christianity "parting of the ways").** Modelled as one fork: **three tradition claims / three entities / two `branches_from` edges** — both edges from the hub **Second Temple Judaism** (→ Christianity, → Rabbinic Judaism); deeper Israelite/Yahwistic roots **deferred** to a later "family 2-deep" investigation (no edge on the hub). **Zero claims/entities/edges — awaiting circuit under brief 2.** Three-claim decomposition (Second Temple Judaism / Christianity / Rabbinic Judaism), each with separable (i) emergence-dating / (ii) descent-or-root / (iii) rival-reading elements; working qualifiers stated as tests, not conclusions, with the **Rabbinic Judaism continuation-qualifier as the reserved Anchor Fit centerpiece** (the list may lack a right word for main-line continuation). **Source-coverage assessment included (§2.4): Christianity side covered by NT corpus SRC-0091…SRC-0103; descent partly by inheritance CLM-0058 / INV-0013 / INV-0014; dating the two Jewish traditions as traditions likely needs a Jewish-studies source extension — a SEPARATE owner-approved step (ADR-GOV-0003 precedent), not created or assumed here.** Metaphysical bracket declared acute (neither supersessionist nor polemical); native `Level N` only; everything R0, §7.5-analog gate, findings not cleared for external reliance. No frontmatter relationship edges (D4); no source, closed-record, Standard, template, tool, Baseline, Iranian-base, or Architectural-Decisions modification.|
|0.4|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

# End INV-0017
