---
title: INV-0016 - Iranian Religious Family Origins and Branching
document_type: Investigation Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-21
category:
  - Knowledge Base
  - Religious Studies
  - Iranian Religions
  - Investigation
parent_documents:
  - KOS-0008 Research Methodology & Investigation Framework
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - KOS-0007 Comparative Analysis Framework
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Investigation
  - IranianReligions
  - WorldReligionsTimeline
---

# INV-0016

# Iranian Religious Family Origins and Branching — Emergence Dating and Historical Descent of Zoroastrianism, Zurvanism, Manichaeism, Mazdakism, and Yazidism

## Draft Investigation Record

> Authored using **TPL-0003**. Sixteenth research workflow (RQ-0016). **Opened as a scaffold**; to be executed and closed through the full adversarial circuit (OPS-0003: Research Specialist → Critical Reviewer → Knowledge Architect; Vision Steward/owner closes). The opening/closing split is structural (**STD-0006 §7.6** independence principle): the session that authored this scaffold does not itself generate and certify the findings that fill it. The circuit runs under a separate brief (brief 2 of 2) after owner review. **The RQ freeze checkpoint is the owner's review of this scaffold report** — the §1 primary wording is authoritative pending that freeze.

> **Program context — this is the FIRST family investigation of the world-religions timeline program (ADR-GOV-0009 D1).** It is also the first consumer of two structures that have existed only as anchors until now: the **Iranian standing source base (SRC-0104…SRC-0123)**, catalogued but unconsumed since ADR-GOV-0003; and the **lineage anchors** laid this same day — the provisional `branches_from` edge (STD-0004 v1.2), the tradition-entity fields `tradition_type`/`dating_claims`/`display_range` (STD-0002 v1.10), and the Entity Record template TPL-0006. Nothing here creates those objects; the circuit does.

> **Source discipline (owner-ratified).** The investigation is **confined to the Iranian catalog SRC-0104…SRC-0123 — READ AND CITE ONLY.** The catalog itself is **never modified** in any way: its hybrid stopping rule and ADR-GOV-0003 standing-source-base status are untouched. The catalog was deliberately built around extinction, contested dating, and hostile-source-only attestation, so **LOW GRADES ARE THE EXPECTED HONEST OUTCOME for several traditions — Mazdakism especially** (its record survives largely through hostile sources; it is graded down honestly, never worked around). **UNSOURCED and thin-base outcomes are pre-authorized;** nothing is thin-sourced to manufacture a grade. Anti-fabrication (KOS-0003 §12.1) is absolute.

> **Cross-investigation inheritance (owner-ratified).** Zoroastrian **dating** analysis already exists at graded confidence in INV-0011's claims (**CLM-0056 — The Dating Problem Is Load-Bearing**, and its neighbours). INV-0016 **CITES those claims by layer inheritance (R0 reliance carried), it does not re-derive them.** INV-0011 and every other closed record are cited, never edited.

> **Anchor stress-test duty (ADR-GOV-0009 §7(a)).** This investigation is the **first pressure test** of the `branches_from` qualifier list and edge semantics, and of the tradition/current distinctness threshold. A dedicated deliverable section (**Anchor Fit Assessment**, reserved below) records findings on anchor fit. Per **ADR-GOV-0007 §3**, those findings are **RECOMMENDATIONS routed to the review queue — never self-applied structural change.** Nothing in this investigation amends STD-0004, STD-0002, TPL-0006, or any standard.

> **Verification & reliance note (STD-0006 §7.5 analog).** Historical religious-studies investigation — **not health/high-stakes, not child-facing** — no health gate. It is, however, **externally consequential** (the world-religions timeline is public-facing in ambition) **and verification-light-expected** (extinct traditions, contested dating, paywalled and hostile-source-only attestation). The Specialist and the Critical Reviewer **must each disclose their verification strength**, and **everything lands R0 — the findings are NOT cleared for external reliance regardless of closure.** Genuinely independent re-verification is the gate-lift.

> **Scale discipline.** Every on-record confidence rating — frontmatter and every grading field — is native **`Level N (Label)`** (KOS-0003 §8), the only authorized on-record confidence vocabulary. No H-band in any frontmatter or grading field; no ★-glyphs anywhere in any Knowledge Object. The optional H-band typology may appear in prose only.

> **Provisional-anchor note (ADR-GOV-0007 §2 / STD-0004 v1.2).** `branches_from` is PROVISIONAL. **No tradition entity, dating claim, or `branches_from` edge is created by this scaffold** — entities are created on demand at circuit (ADR-GOV-0009 D2), and every lineage edge is warranted by a graded claim and reviewer-verified (the warrant rule). This session lays no anchors of its own and populates none; it frames the work that brief 2 executes.

---

# 1. Research Question

**Primary (authoritative wording pending owner freeze at scaffold review):**

> What can be established, and at what evidential grade, about the origins and historical branching of the Iranian religious family — Zoroastrianism, Zurvanism, Manichaeism, Mazdakism, and Yazidism — including the dating of each tradition's emergence and the nature of each descent relationship?

**Decomposition mandate (owner-ratified): FIVE claims, one per tradition** (identifiers assigned at execution, not here), **each answering three explicitly separable elements** — the lesson encoded from INV-0011 criterion #2 that "treated in prose" is not "answered separably":

- **(i) EMERGENCE DATING.** What the source base establishes about *when* the tradition emerged, at what grade; **contested ranges reported as contested** (dates are claims — ADR-GOV-0009 D3; no false precision). **Zoroastrianism's dating cites INV-0011's graded analysis by inheritance** (CLM-0056 and neighbours), it is not re-derived.
- **(ii) DESCENT RELATIONSHIP.** The tradition's lineage position, and — for the four non-root traditions — the **`branches_from` qualifier the evidence supports** (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed`), stated with the justification that will warrant the edge at circuit. **Zoroastrianism is the family root: no `branches_from`;** its (ii) states the root status and what bounds it.
- **(iii) RIVAL READING.** The strongest counter-reading of that tradition's dating or descent — steelmanned — with its survival and its cost to confidence stated.

**Working hypotheses — to be TESTED at circuit, NOT assumed** (the evidence may overturn any of these):

| Tradition | Root/descent working hypothesis | Working `branches_from` qualifier (to test) |
|---|---|---|
| Zoroastrianism | Family **root** | — (no edge; root) |
| Zurvanism | Offshoot / theological current of Zoroastrianism | `heterodox-offshoot` |
| Manichaeism | Founded syncretic tradition drawing on Iranian (and Christian/Buddhist) sources | `syncretic-descent` |
| Mazdakism | Offshoot or reform movement of Zoroastrianism | `heterodox-offshoot` **or** `reform` |
| Yazidism | Descent contested (Iranian-derivation readings vs. others) | `disputed` |

These are hypotheses under test. In particular, whether Zurvanism is a *distinct tradition* at all (versus a theological current within Zoroastrianism) is itself part of the distinctness-threshold test (§2.3), and Yazidism's non-Iranian-derivation readings are live (§1(iii) for that claim).

---

# 2. Scope & Disambiguation

## 2.1 Metaphysical neutrality

The five traditions' truth claims are **bracketed entirely.** This is **historical dating and descent**, in a **neutral religious-studies register** — no confessional framing in any direction, for or against any tradition, and no theological adjudication of any tradition's self-account.

## 2.2 Source discipline and thin-base authorization

- **Confined to SRC-0104…SRC-0123 — read and cite only; the catalog is never modified** (its stopping rule and ADR-GOV-0003 status are out of scope for this INV). No new source record is created — the source base *is* the base.
- **Hostile-source problems are graded down honestly, never worked around.** Mazdakism's record survives largely through its opponents (e.g., the Crone 1991 / Zaehner / Eznik material in the catalog); the grade reflects that evidential class rather than papering over it.
- **UNSOURCED / insufficient base to grade is a legitimate, recordable outcome.** No claim is thin-sourced into a grade it has not earned. Anti-fabrication (KOS-0003 §12.1) is absolute.

## 2.3 Distinctness threshold — what counts as a TRADITION vs. a current (working criterion; expected anchor-stress material)

A formation warrants its own **tradition-class Entity Record** (and thus a place in the branching graph) when the source base treats it as a **distinct religious tradition** — evidenced by (a) an identifiable community, adherents, or transmission lineage of its own; (b) a distinguishing doctrinal or organizational core; and (c) recognition in the literature as a *named tradition* rather than a *tendency, emphasis, or current within* another tradition. A formation that fails (a)+(b) — a doctrinal emphasis without a separable community or lineage — is a **current**, modelled as content of its parent tradition, not as a distinct entity.

**This threshold is under test, not settled.** Its sharpest case is **Zurvanism**: the literature is genuinely divided on whether it was a distinct tradition or a theological current within Zoroastrianism (the §1(iii) rival reading for that claim). The circuit applies this working criterion, records where it strains, and reports the strain to the Anchor Fit Assessment — it does not force a verdict to protect the criterion.

## 2.4 Boundaries

- **With INV-0011 (cite, never re-derive).** Zoroastrian dating is inherited from INV-0011's graded claims (CLM-0056 and neighbours) under the layer-inheritance rule (§3); INV-0011 is not edited, re-opened, or re-derived.
- **With the catalog (consume, never modify).** SRC-0104…SRC-0123 are cited only; no catalog record is touched.
- **With future families (no cross-family edges).** No `branches_from` edge or any typed edge is drawn to a tradition **outside** the Iranian family. Manichaeism's **Christian and Buddhist syncretic inputs are NOTED in prose, not edged** — those entities do not exist, and creating cross-family edges is out of scope (and would violate the family boundary the timeline program builds one family at a time).

## 2.5 Scale posture

Native **`Level N`** only in every frontmatter and grading field. The H-band typology may be used in **prose only** (optional), and carries no grading authority. No ★-glyphs anywhere.

## 2.6 Reliance posture

**Everything lands R0.** Verification-light close is expected (extinct traditions; contested dating; paywalled and hostile-source-only attestation). Findings are **NOT cleared for external reliance regardless of closure** — the §7.5-analog gate is declared here, at opening, before any evidence.

## 2.7 Terminology

"Iranian religious family" denotes the family of traditions rooted in or descended from ancient Iranian religion as the literature bounds it; the five in scope are Zoroastrianism, Zurvanism, Manichaeism, Mazdakism, and Yazidism. "Tradition" vs. "current" is governed by §2.3. `branches_from` **qualifiers** (`schism`/`reform`/`syncretic-descent`/`heterodox-offshoot`/`disputed`, STD-0004 §7.2) are **distinct from** `tradition_type` **values** (`founded`/`emergent`/`reform`/`syncretic`, STD-0002 §11) — the two vocabularies are not interchangeable and are not conflated in any record.

---

# 3. Method / Protocol

Execution follows the KOS-0003 pipeline (Question → Claims → Assumptions → Evidence → Confidence) through the **full OPS-0003 circuit**. Claims via **TPL-0001**; the five tradition entities via **TPL-0006 tradition-class skeleton** (born conformant — `tradition_type`, `dating_claims`, `display_range`, and any qualified `branches_from` edges present from birth, STD-0002 v1.10); the synthesis via **TPL-0004**. Sources are **cited from SRC-0104…SRC-0123**, not created. All identifiers registered in the Identifier Registry at execution.

## 3.1 Operative disciplines (bind at circuit)

> **WARRANT RULE (review-checked, not tool-checked).** Every `branches_from` edge written at circuit **MUST be warranted by a graded claim** asserting the descent (the edge renders; the claim warrants). `graph_integrity.py` enforces only the *structural* constraints (ENT→ENT, required/controlled qualifier) — it **cannot** verify the warrant, because a warrant is a claim about lineage, not a structured pointer. **The Critical Reviewer therefore verifies each edge-warrant pair explicitly.** An unwarranted edge is a defect the reviewer must catch.

> **LAYER-INHERITANCE.** A dating or descent claim that **cites INV-0011** is **bounded by the cited claims' grades** (the inheriting claim may not exceed CLM-0056's grade on the shared question). A **catalog-only** claim is **bounded by the catalog's source quality for that tradition** — which, for the hostile-source and extinct-tradition cases, is the reason low grades are expected (§2.2).

## 3.2 Per-claim structure

Each of the five tradition claims answers elements **(i) emergence dating**, **(ii) descent relationship**, and **(iii) rival reading** in **explicit, separable sections** of the claim record — not diffused through prose (§1; acceptance criterion 1).

## 3.3 Entity-on-demand and dates-as-claims

Tradition entities are created **only as their claims warrant them** (ADR-GOV-0009 D2) — no pre-populated gazetteer. **Dates are claims** (D3): the entity carries `dating_claims` pointers and a render-only `display_range`; the sourced, graded, epistemic-fielded date lives in the CLM, and **there is no `origin_date` field.** Contested dating is carried as contestedness in the claim, never flattened into a false-precision range on the entity.

---

# 4. Findings / Synthesis

*Stub — populated at circuit execution by the Research Specialist (ROLE-0002); pending ROLE-0004 review and ROLE-0001 validation.*

Primary synthesis will be **FND-0016** (identifier reserved; assigned at execution) — an expected **layered verdict by tradition**, with each tradition's emergence dating and descent relationship graded separately, contested cases reported as contested, and the hostile-source / extinct-tradition cases (Mazdakism especially) graded down honestly rather than papered over. No verdict is written here.

---

# 5. Confidence Summary (KOS-0003 §8)

*Stub — assigned at circuit execution, native `Level N` only; pending circuit review.* Every grade will be bounded by §3.1 (layer-inheritance) and by the accessibility and strength of the actual catalog sources for each tradition. **Low and Very Low grades are anticipated and pre-authorized** where the base is thin, extinct-tradition, or hostile-source-only — they are the honest outcome, not a deficiency (§2.2).

---

# 6. Assumptions & Bracketing (KOS-0003 §10)

*Stub — expanded at circuit execution. The standing brackets and disciplines below bind from opening:*

- **Metaphysical bracket (§2.1).** Every tradition's truth claims are bracketed; the register is neutral historical religious studies, in no direction.
- **Low grades are the honest expected outcome (§2.2).** The source base was built around extinction, contested dating, and hostile-source-only attestation; UNSOURCED and thin-base outcomes are pre-authorized and are not failures.
- **No directional premise on descent.** Each working hypothesis in §1 is **tested, not assumed** — the qualifier the evidence supports may differ from the working hypothesis, and a "disputed" outcome (or a distinctness-threshold failure that dissolves an entity into a current) is a legitimate result.
- **Inheritance not re-derivation (§2.4).** Zoroastrian dating is bounded by INV-0011's grades; INV-0011 is not re-opened.
- **Catalog and family boundaries hold.** The catalog is cited, never modified; no cross-family edges (§2.4).

---

# Anchor Fit Assessment — RESERVED (ADR-GOV-0009 §7(a) stress-test deliverable)

*Reserved section (per TPL convention), placed between the bracketing section and the acceptance criteria. **Populated at circuit execution; empty at scaffold.*** Under the anchor stress-test duty (ADR-GOV-0009 §7(a)), this investigation is the first pressure test of the lineage anchors. At circuit the Specialist and Critical Reviewer record findings on:

1. **Qualifier-list fit** — does the controlled list (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed`) fit the five descent relationships the evidence actually supports, or does a case fall between/outside the list?
2. **Edge semantics** — does `branches_from`'s ENT→ENT, asymmetric, warrant-by-graded-claim semantics hold under real use, or does a case strain it (e.g., a tradition with two plausible parents, or descent from a *current* rather than a tradition)?
3. **Distinctness threshold (§2.3)** — does the tradition-vs-current working criterion discriminate cleanly (the Zurvanism test case in particular), or does it need refinement?

**Per ADR-GOV-0007 §3, every finding recorded here is a RECOMMENDATION routed to the review queue — never a self-applied structural change.** This investigation amends no standard, template, or tool. Contradiction / field-prose-divergence style items, if any, enter the Governance Backlog as explicit `REVIEW-FLAG` marker lines (tools/README.md convention); ordinary prose recommendations are carried here and surfaced to the owner at close.

---

# 7. Acceptance Criteria for Closing

INV-0016 may close only when all of the following hold (modelled on INV-0015 §7, adapted):

1. [ ] The question is decomposed into the **five tradition claims** (§1), each separately gradable, with elements **(i) emergence dating / (ii) descent relationship / (iii) rival reading** answered **explicitly and separably** in the claim record — discrete sections, not diffused prose.
2. [ ] **Five tradition entities** are born conformant to **TPL-0006 / STD-0002 v1.10** (`tradition_type` from the controlled vocabulary; co-required `dating_claims` and `display_range`; no `origin_date`), **created only as their claims warrant them** (ADR-GOV-0009 D2). A tradition that fails the §2.3 distinctness threshold is recorded as a current of its parent, not forced into an entity.
3. [ ] **Every `branches_from` edge is qualifier-carrying and warrant-paired with a graded claim, reviewer-verified per the warrant rule** (§3.1). No unwarranted edge; no edge with a missing or off-vocabulary qualifier; no ENT→non-ENT edge.
4. [ ] **Contested dating is reported as contested; no false precision;** `display_range` is render-only and the sourced/graded date lives in the claim (dates-as-claims, D3).
5. [ ] **Source discipline held:** the catalog SRC-0104…SRC-0123 is **cited and unmodified**; INV-0011 is **inherited, not re-derived**; **UNSOURCED / thin-base outcomes are recorded honestly** where the base is thin (no thin-sourcing).
6. [ ] **Native `Level N` only** — no H-band and no ★ in any frontmatter or grading field; the **metaphysical bracket held** in both directions on every object.
7. [ ] The **full OPS-0003 circuit** has run, with **verification-strength disclosure** by Specialist and Critical Reviewer; **ROLE-0001 structural validation evidenced in-record** (or via in-record citation naming document and version, per ADR-GOV-0005 §2).
8. [ ] The **Anchor Fit Assessment is completed and routed as recommendations** (ADR-GOV-0007 §3); **Standards, the Architecture Baseline, the Iranian catalog, and the Architecture are unmodified.**

**Verification & reliance (§7.5 analog).** This investigation is **externally consequential** (the world-religions timeline is public-facing in ambition) **and verification-light-expected.** **Findings are NOT cleared for external reliance regardless of closure** — a verification-light review may issue verdicts but may not clear findings for external use; genuinely independent re-verification is the gate-lift. Everything lands **R0**.

---

# 8. Relationships (STD-0004)

- `part_of` the Knowledge Base — a **classification** statement, not a typed graph edge ("Knowledge Base" is not a resolvable object; no `part_of` target declared in frontmatter — matching INV-0009…INV-0015).
- **Frontmatter edges at opening: none.** Per **ADR-GOV-0004 D4**, frontmatter references are graph claims and may name only existing objects. At scaffold, **no accurate typed edge to an existing object exists at the INV level:** the INV-0011 inheritance and the catalog citations attach to **child claims** created at circuit, not to INV-0016 itself, and those children do not yet exist. Declaring any child or inheritance edge now would assert a relationship the record does not yet have. The planned subgraph is declared in prose here and edged at execution.
- **Planned built subgraph (populated at execution; existing STD-0004 types only, none invented):** INV-0016 is the **hub**.
  - **Five tradition claims (CLM, identifiers assigned at execution):** each `part_of` INV-0016, `supports` FND-0016, and `derived_from` its cited catalog source(s) in SRC-0104…SRC-0123. Because the **catalog is unmodified**, these `derived_from` edges into the catalog are **one-directional by necessity** — an accepted OPS-0002 §5 advisory, not reciprocated (the same pattern as INV-0014's one-directional CLM-0075→SRC-0101 citation into a closed source).
  - **Zoroastrian dating claim:** inherits INV-0011 **CLM-0056** under the layer-inheritance rule. Whether this is edged as a one-directional `depends_on` into the closed INV-0011 claim (the INV-0014 CLM-0074 precedent) or carried as a prose citation only is a circuit decision; either way INV-0011 is not modified.
  - **Five tradition entities (ENT, identifiers assigned at execution; expected range beginning ENT-0008):** created on demand (D2); each carries `dating_claims` pointing to its dating CLM and, for the non-root traditions, a qualified `branches_from` edge to its parent **entity within this family**, warranted by a graded descent claim (§3.1). Root Zoroastrianism carries **no** `branches_from`.
  - **Finding (FND-0016):** `derived_from` the five tradition claims, `part_of` INV-0016.
  - **No cross-family edges.** Manichaeism's Christian/Buddhist syncretic inputs are **noted in prose, not edged** (§2.4); no edge to any tradition outside the Iranian family.
- **Entity/source creation is deferred to circuit** (ADR-GOV-0009 D2); this scaffold creates none.

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-21|Draft|Opened as scaffold per owner-ratified brief. First family investigation of the ADR-GOV-0009 timeline program; first consumer of the Iranian standing source base (SRC-0104…SRC-0123) and the lineage anchors (STD-0004 v1.2 `branches_from`, STD-0002 v1.10 tradition-entity fields, TPL-0006). Zero claims/entities/edges — awaiting circuit under brief 2. Five-claim (one-per-tradition) decomposition with separable (i) emergence dating / (ii) descent relationship / (iii) rival reading elements; working `branches_from` hypotheses stated as tests, not conclusions; distinctness threshold (§2.3) and Anchor Fit Assessment (§7(a)) reserved as the stress-test deliverables; source discipline, thin-base authorization, metaphysical bracket, native-Level-N, and R0 §7.5-analog gate declared at opening. No frontmatter relationship edges (D4); no catalog, INV-0011, closed-record, Standard, Baseline, or Architectural Decisions modification.|

# End INV-0016
