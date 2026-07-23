---
title: INV-0016 - Iranian Religious Family Origins and Branching
document_type: Investigation Record
version: 0.5
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
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-21
    ai_degree: ai-delegated
    ai_model_family: Claude
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

> **Provisional-anchor note (ADR-GOV-0007 §2 / STD-0004 v1.2).** `branches_from` is PROVISIONAL. At scaffold (v0.1) no tradition entity, dating claim, or `branches_from` edge existed; the **circuit (v0.2, brief 2 of 2) populated them for the first time in the vault** — every lineage edge is warranted by a graded claim and reviewer-verified (the warrant rule). The anchors remain provisional and reflexively gated (see the Anchor Fit Assessment).

> **CLOSED 2026-07-21 — formal closure under ADR-GOV-0004 §2 D1, per the owner's conditional pre-authorization (INV-0016 circuit brief, brief 2 of 2).** All four pre-authorization conditions were evaluated and met: **(a)** all eight §7 acceptance criteria genuinely met and ticked with in-record evidence — five tradition claims with separable (i)/(ii)/(iii) elements; four born-conformant tradition entities (the vault's first) with three warrant-paired, reviewer-verified `branches_from` edges; **Zurvanism modelled as a current, not forced into an entity** (criterion 2's own provision); Anchor Fit Assessment completed, §7.6-reflexively-gated, and routed as recommendations; **(b)** reviewer verdict **Conformant with Flags with both determinate flags remediated in-session** (Critical Review – RQ-0016 v1.0); **(c)** **no confidence level raised** — none changed at all, reviewer-confirmed; **(d)** validate.py PASS (357/0/0) and graph_integrity.py clean (0 dangling; 0 branch errors; advisory delta 0). Maturity `status` remains `Draft` and `operational_status` remains `Active` per **ADR-GOV-0005 §1** (closure lives in this banner and the history row, not a frontmatter field; model INV-0010/INV-0013/INV-0014/INV-0015). Closure is **not** a maturity promotion. **The three Low tradition components and the "disputed" Yazidism verdict are completed findings, not deficiencies** — the honest thin-base outcome the brief pre-authorized. **Per the §7.5-analog note this rests on a verification-light, same-model (procedurally-independent) circuit — findings are NOT cleared for external reliance (timeline-publication or any outward use) regardless of closure**; genuinely independent, blinded re-verification is the gate-lift, and the Anchor Fit findings are additionally §7.6-gated from promoting the lineage anchors provisional→durable.

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

**Executed by the Research Specialist (ROLE-0002), 2026-07-21; pending ROLE-0004 review and ROLE-0001 validation.**

Primary synthesis: **[[FND-0016 - Origins and Branching of the Iranian Religious Family]]** — a **layered verdict by tradition**. The family resolves into **one root, one internal current, and three branching traditions**:

- **CLM-0087 — Zoroastrianism (root):** emergence contested (traditional 6th-c.-BCE date a late construct; early linguistic dating c. 1500–1000 BCE indirect; inherited from INV-0011 CLM-0056, not re-derived); **Level 3 (Moderate)**; `tradition_type: founded`; **no `branches_from`** (root).
- **CLM-0088 — Zurvanism:** ideas attested (5th c., Eznik) **Level 3**, but distinct-tradition status disputed **Level 2** — on §2.3 it does **not** clear the distinctness threshold (no attested separate community/sect); **modelled as a heterodox current of Zoroastrianism — NO entity, NO edge.** The decisive anchor-stress result.
- **CLM-0089 — Manichaeism:** founded 3rd c. CE (best-dated in the family) **Level 3**, deliberately syncretic **Level 3**, but multi-parent with the primary (Elchasaite) matrix out-of-family so the in-family Zoroastrian parent is **Level 2**; `branches_from` ENT-0008 `syncretic-descent`.
- **CLM-0090 — Mazdakism:** Kavad-era (late 5th–early 6th c. CE) heterodox offshoot, **Level 2 throughout** — hostile/late Perso-Arabic base (Crone); the family's thinnest case; `branches_from` ENT-0008 `heterodox-offshoot`.
- **CLM-0091 — Yazidism:** 12th-c. crystallisation (Sheikh ʿAdī/Lalish) **Level 3**; deeper descent **genuinely disputed** (Iranian-substrate advocacy vs Sufi-origin) **Level 3** — the disputedness is the finding; `branches_from` ENT-0008 `disputed`.

**No verdict exceeds Moderate; three of five tradition components are Low** — the honest thin-base outcome for a family built around extinction, contested dating, and hostile-source-only attestation.

---

# 5. Confidence Summary (KOS-0003 §8)

**Assigned at execution (2026-07-21), native `Level N` only; pending circuit review.** Every grade is bounded by §3.1 (layer-inheritance) and by the strength of the actual catalog sources per tradition.

- **Moderate (Level 3):** Zoroastrian dating + root status (CLM-0087, bounded by CLM-0056); Zurvanite ideas attested (CLM-0088-i); Manichaean founding date + syncretic character (CLM-0089-i/ii); Yazidi crystallisation + the disputedness of its descent (CLM-0091).
- **Low (Level 2) — the honest thin points (§2.2), recorded not papered over:** Zurvanism's distinct-tradition status (CLM-0088-ii — disputed, threshold not cleared); Manichaeism's Zoroastrian-as-in-family-parent (CLM-0089 — partial, multi-parent); Mazdakism throughout (CLM-0090 — hostile/late base).
- **No Level 4 or 5 anywhere** — verification-light throughout (catalog largely parametric; extinct traditions; hostile/late sources). Splits split, never averaged.
- **Reliance:** everything **R0**; **not cleared for external reliance** regardless of closure (§7.5-analog, FND-0016 §4).

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

**Populated at circuit execution (2026-07-21).** The first pressure test of the lineage anchors (ADR-GOV-0009 §7(a)). **Per ADR-GOV-0007 §3, every finding below is a RECOMMENDATION routed to the review queue — never a self-applied structural change. This investigation amended no standard, template, or tool.** Four substantive findings:

> **Reflexive-finding gate (STD-0006 §7.6; added at ROLE-0004 remediation, Flag 1).** These are **reflexive findings** — they bear on Project Relatio's own anchor design (the `branches_from` edge, the §2.3 distinctness threshold, the qualifier list, `tradition_type`) and some reach partly *vindicating* conclusions. Per STD-0006 §7.6 they are **gated for reflexive use: they may NOT be cited to promote `branches_from`, the §2.3 threshold, the qualifier vocabulary, or `tradition_type` from provisional toward durable until genuinely independent, blinded review** (a different model, or a human specialist, without the vault's framing). The Specialist and the ROLE-0004 reviewer are the **same underlying model** (independence procedural only) — same-model assessment **flags, it does not certify**; a shared blind spot cannot be ruled out from inside it. This gate is load-bearing for a public-facing timeline.

**AF-1 — The distinctness threshold discriminated on a split-leg case (Zurvanism).** The §2.3 tradition-vs-current criterion did real work: Zurvanism **cleared the distinguishing-doctrine leg (b)** (the Zurvan cosmogony) but **failed the separate-community leg (a)** (no attested Zurvanite sect) **and the named-tradition-not-current leg (c)** (the sources frame it as a current *within* Zoroastrianism), so — on the conjunctive bar — it was modelled as a **current, not a distinct tradition: no entity, no edge.** The criterion split the case rather than passing or failing it wholesale, which is the discriminating behaviour §2.3 was meant to have. *Recommendation:* the three-leg conjunctive form (community/lineage · distinguishing core · named-tradition-not-current) is a workable criterion; **whether to promote it toward a durable rule is deferred to the reflexive gate above and a second family's exercise of it.** **Routed as a review-queue recommendation (not actioned).**

**AF-2 — `branches_from` cannot represent MULTI-PARENT descent (Manichaeism).** The edge is single-target (ENT→one ENT), but Manichaeism has several parents, its *primary* one (Elchasaite Jewish-Christian) out-of-family. Edging Manichaeism→Zoroastrianism alone captures a real but partial descent and risks implying a Zoroastrian primacy the evidence denies. The `syncretic-descent` qualifier flags incorporation but not *plurality* or *primacy*. *Recommendation:* consider whether multi-parent syncretic descent needs (a) multiple `branches_from` edges permitted with a "primary/secondary" marker, or (b) an explicit convention that out-of-family parents are prose-only and the in-family edge is understood as partial. **Routed as a review-queue recommendation.**

**AF-3 — Edge TARGET can be broader than the named parent (Yazidism; Manichaeism).** For Yazidism the disputed Iranian antecedent is *ancient Western Iranian religion broadly*, not specifically Zoroastrianism; ENT-0008 stands in as the family-root representative — a target stretch. The `disputed` qualifier carried the contestation well (the strongest alternative, Sufi origin, is out-of-family and unedgeable), which is a **success** for that qualifier. *Recommendation:* consider whether the family root should be an explicit "ancient Iranian religion" node distinct from Zoroastrianism, so descent-from-substrate is not conflated with descent-from-the-root-tradition. **Routed as a review-queue recommendation.**

**AF-4 — `tradition_type` vocabulary strains where categories co-apply.** `founded` and `syncretic` both fit Manichaeism; `founded` and `emergent` both arguably fit Zoroastrianism; `reform` (tradition_type) sat adjacent to `heterodox-offshoot` (qualifier) for Mazdakism. The single-valued field forced a least-wrong choice each time (tensions recorded on each entity). The `founded/reform/emergent/syncretic` set is workable but not cleanly exclusive. *Recommendation:* consider either a controlled multi-value `tradition_type` or explicit precedence guidance (e.g., "the defining act wins: a founded-and-syncretic tradition is `founded`"). **Routed as a review-queue recommendation.**

**Qualifier-list fit (overall):** the five-qualifier list (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed`) **fit every edge actually drawn** — `syncretic-descent` (Manichaeism), `heterodox-offshoot` (Mazdakism), `disputed` (Yazidism); `schism` and the qualifier-`reform` were not needed this family (Mazdakism's `reform` near-miss recorded at AF-4/CLM-0090). No case fell *outside* the list. The strains are about edge *cardinality* and *target* (AF-2/AF-3), not the qualifier vocabulary.

**Routing:** these are prose recommendations surfaced to the owner and the review queue; none is a `contradiction`/`field_prose_divergence` trigger, so no `REVIEW-FLAG` marker line is lodged (the Governance Backlog carries a single pointer entry — see Task 6). No structural change applied in-session (ADR-GOV-0007 §3).

---

# 7. Acceptance Criteria for Closing

INV-0016 may close only when all of the following hold (modelled on INV-0015 §7, adapted):

1. [x] The question is decomposed into the **five tradition claims** (§1), each separately gradable, with elements **(i) emergence dating / (ii) descent relationship / (iii) rival reading** answered **explicitly and separably** in the claim record — discrete sections, not diffused prose. — *Met: CLM-0087…CLM-0091, each carrying discrete `# Element (i)/(ii)/(iii)` sections; Critical Review – RQ-0016 duty (a) PASS.*
2. [x] **Tradition entities** are born conformant to **TPL-0006 / STD-0002 v1.10** (`tradition_type` from the controlled vocabulary; co-required `dating_claims` and `display_range`; no `origin_date`), **created only as their claims warrant them** (ADR-GOV-0009 D2). A tradition that fails the §2.3 distinctness threshold is recorded as a current of its parent, not forced into an entity. — *Met: **four** entities ENT-0008…ENT-0011 born conformant (validate.py tradition-field check PASS at error level); **Zurvanism deliberately NOT made an entity** — recorded as a heterodox current of Zoroastrianism on ENT-0008 (CLM-0088; §2.3 threshold not cleared). Five-claim/four-entity divergence is exactly the criterion-2 provision, reviewer-confirmed sound (per-edge table, PASS on the Zurvanism negative).*
3. [x] **Every `branches_from` edge is qualifier-carrying and warrant-paired with a graded claim, reviewer-verified per the warrant rule** (§3.1). No unwarranted edge; no edge with a missing or off-vocabulary qualifier; no ENT→non-ENT edge. — *Met: three edges (ENT-0009 `syncretic-descent`/CLM-0089; ENT-0010 `heterodox-offshoot`/CLM-0090; ENT-0011 `disputed`/CLM-0091), **each warrant-verified individually** by Critical Review – RQ-0016 §3 (all PASS); ENT-0008 correctly edgeless; `graph_integrity.py` 0 branch errors (ENT→ENT + controlled qualifier confirmed, edges parsed not skipped).*
4. [x] **Contested dating is reported as contested; no false precision;** `display_range` is render-only and the sourced/graded date lives in the claim (dates-as-claims, D3). — *Met: every `display_range` hedged ("(contested)", "(earlier substrate disputed)", "(fl. under Kavad I)"); each entity §3 states the field is render-only with the graded date in the CLM; Critical Review duty (e) PASS.*
5. [x] **Source discipline held:** the catalog SRC-0104…SRC-0123 is **cited and unmodified**; INV-0011 is **inherited, not re-derived**; **UNSOURCED / thin-base outcomes are recorded honestly** where the base is thin (no thin-sourcing). — *Met: git diff touches no SRC-0104…0123 file and no INV-0011 file (verified at validation); CLM-0087 inherits CLM-0056 via `depends_on`, bounded (L3 ≤ L4); Mazdakism graded Low throughout, three of five components Low — honest thin base; Critical Review duty (c) PASS with Flag 2 (over-specification) remediated.*
6. [x] **Native `Level N` only** — no H-band and no ★ in any frontmatter or grading field; the **metaphysical bracket held** in both directions on every object. — *Met: grep-verified no ★/H-band in any frontmatter or grading field (only rule-text mentions); no Level 4/5 anywhere; Critical Review duty (d) PASS (bracket both directions).*
7. [x] The **full OPS-0003 circuit** has run, with **verification-strength disclosure** by Specialist and Critical Reviewer; **ROLE-0001 structural validation evidenced in-record** (or via in-record citation naming document and version, per ADR-GOV-0005 §2). — *Met: Specialist v0.2 (verification-light, disclosed §5/FND-0016 §4); **Critical Review – RQ-0016 v1.0 — CONFORMANT WITH FLAGS**, verification-light disclosed, both determinate flags remediated in-session; **ROLE-0001 structural validation recorded in this record's v0.3 history row** — validate.py PASS 357/0/0, graph_integrity.py 0 dangling / 0 branch errors, advisories 39/2 unchanged.*
8. [x] The **Anchor Fit Assessment is completed and routed as recommendations** (ADR-GOV-0007 §3); **Standards, the Architecture Baseline, the Iranian catalog, and the Architecture are unmodified.** — *Met: AF-1…AF-4 + qualifier-list-fit completed, §7.6 reflexive-gated (Flag 1 remediated), routed as review-queue recommendations (Backlog pointer GB-2026-041); git diff confirms no Standard, template, tool, Architecture Baseline, Architectural Decisions, or catalog file modified.*

**Verification & reliance (§7.5 analog).** This investigation is **externally consequential** (the world-religions timeline is public-facing in ambition) **and verification-light-expected.** **Findings are NOT cleared for external reliance regardless of closure** — a verification-light review may issue verdicts but may not clear findings for external use; genuinely independent re-verification is the gate-lift. Everything lands **R0**.

---

# 8. Relationships (STD-0004)

- `part_of` the Knowledge Base — a **classification** statement, not a typed graph edge ("Knowledge Base" is not a resolvable object; no `part_of` target declared in frontmatter — matching INV-0009…INV-0015).
- **Frontmatter edges at opening: none.** Per **ADR-GOV-0004 D4**, frontmatter references are graph claims and may name only existing objects. At scaffold, **no accurate typed edge to an existing object exists at the INV level:** the INV-0011 inheritance and the catalog citations attach to **child claims** created at circuit, not to INV-0016 itself, and those children do not yet exist. Declaring any child or inheritance edge now would assert a relationship the record does not yet have. The planned subgraph is declared in prose here and edged at execution.
- **Built subgraph (populated at execution 2026-07-21; existing STD-0004 types only, none invented):** INV-0016 is the **hub**.
  - **Five tradition claims (CLM-0087…CLM-0091):** each `part_of` INV-0016, `supports` FND-0016, and `derived_from` its cited catalog source(s) in SRC-0104…SRC-0123. Because the **catalog is unmodified**, these `derived_from` edges into the catalog are **one-directional by necessity** — accepted OPS-0002 §5 advisories, not reciprocated (the INV-0014 CLM-0075→SRC-0101 pattern).
  - **Zoroastrian dating claim (CLM-0087):** inherits INV-0011 **CLM-0056** via a **one-directional `depends_on`** edge into the closed INV-0011 claim (the INV-0014 CLM-0074 precedent) — INV-0011 unmodified; a bounded advisory.
  - **FOUR tradition entities (ENT-0008…ENT-0011), NOT five:** created on demand (D2). ENT-0008 Zoroastrianism (root, **no `branches_from`**); ENT-0009 Manichaeism (`branches_from` ENT-0008, `syncretic-descent`); ENT-0010 Mazdakism (`branches_from` ENT-0008, `heterodox-offshoot`); ENT-0011 Yazidism (`branches_from` ENT-0008, `disputed`). Each carries `tradition_type` / `dating_claims` / `display_range`; each edge is warranted by its tradition's claim element (ii). **Zurvanism receives NO entity** — modelled as a heterodox current of Zoroastrianism (CLM-0088; §2.3 threshold not cleared), recorded on ENT-0008. This is a **hypothesis overturned**: the scaffold's working table had Zurvanism as a `heterodox-offshoot` branch; the evidence made it a current.
  - **Finding (FND-0016):** `derived_from` CLM-0087…CLM-0091, `part_of` INV-0016.
  - **No cross-family edges.** Manichaeism's Christian/Buddhist parents and Yazidism's Sufi-Islamic parent are **noted in prose, not edged** (§2.4).
- **Divergence from the scaffold plan (honest report):** five claims but **four entities and three edges** (not five/four) — Zurvanism dissolved to a current. Conformant with acceptance criterion 2 ("created only as their claims warrant them; a tradition that fails §2.3 is recorded as a current, not forced into an entity").

---

# 9. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|0.4|2026-07-21|Draft|**Formally CLOSED under ADR-GOV-0004 §2 D1, per the owner's conditional pre-authorization (circuit brief 2 of 2).** All four conditions evaluated and met (dated closure banner added, citing the pre-authorization): (a) all eight §7 criteria met and ticked with in-record evidence; (b) Critical Review – RQ-0016 **Conformant with Flags, both determinate flags remediated in-session**; (c) no confidence level raised (none changed); (d) validate.py PASS 357/0/0, graph_integrity.py 0 dangling / 0 branch errors, advisory delta 0. **Per ADR-GOV-0005 §1 closure state is carried by the banner and this row, not frontmatter** — `status: Draft` / `operational_status: Active` deliberately unchanged. Closure is not a maturity promotion and **not a clearance for external reliance** (verification-light, same-model circuit; §7.5-analog gate stands; Anchor Fit findings additionally §7.6-gated). The three Low components and "disputed" Yazidism are completed findings, not deficiencies. No research content altered by this closure; additive only.|
|0.3|2026-07-21|Draft|**Circuit review + remediation + ROLE-0001 structural validation (recorded in-record here per §7 criterion 7).** **Critical Review – RQ-0016 (v1.0): CONFORMANT WITH FLAGS** — verification-light (six of twelve sources read in full, quoted phrases verbatim-matched; same-model, procedural independence only); **per-edge warrant rule verified individually — all three edges PASS + both negatives (Zoroastrianism root, Zurvanism-as-current) PASS**; five flags (two determinate, three non-determinate). **Both determinate flags remediated in-session:** Flag 1 (reflexive AF findings ungated) → §7.6 reflexive-gating disclosure added to the Anchor Fit Assessment; Flag 2 (CLM-0090/ENT-0010 over-specification — "Zaradusht of Fasa", property/women program, mis-sourced skepticism) → hedged parametric + misattribution corrected (CLM-0090 v0.2, ENT-0010 v0.2). Three non-determinate adopted/acknowledged (AF-1 split-leg rewording; ENT-0010 tradition_type base-thinness note; Yazidism target-stretch acknowledged). **No confidence level raised or lowered anywhere.** **ROLE-0001 structural validation (this row is the in-record evidence): validate.py PASS 357 files / 0 errors / 0 warnings** (version coherence at error level; epistemic + review fields well-formed on all six CLM/FND; tradition-entity fields on all four ENT); **graph_integrity.py 0 dangling / 0 branch errors** (three `branches_from` ENT→ENT + controlled qualifier confirmed parsed, not skipped; `dating_claims` resolve; CLM-0087→CLM-0056 `depends_on` into closed INV-0011); advisory delta **0** (39 symmetric / 2 untyped, unchanged — new edges all asymmetric types); scale-discipline grep clean; §8 declared subgraph matches the built graph.|
|0.2|2026-07-21|Draft|**Executed by the Research Specialist (ROLE-0002)** — owner froze the scaffold as authored (RQ, five-claim decomposition, §2.3 threshold all stand). Created **five tradition claims CLM-0087…CLM-0091** (each with separable (i) dating / (ii) descent+qualifier / (iii) rival elements), **four tradition entities ENT-0008…ENT-0011** (the vault's first tradition-class entities; ENT-0008 Zoroastrianism root, ENT-0009/0010/0011 with `branches_from` ENT-0008 qualified `syncretic-descent`/`heterodox-offshoot`/`disputed`), and **FND-0016** (layered verdict by tradition). **Zurvanism dissolved to a heterodox current of Zoroastrianism — no entity, no edge (hypothesis overturned; §2.3 threshold not cleared)** — five claims, four entities, three edges. Zoroastrian dating inherited from INV-0011 CLM-0056 via one-directional `depends_on` (INV-0011 unmodified). **Anchor Fit Assessment populated (AF-1…AF-4)** and routed as review-queue recommendations (ADR-GOV-0007 §3; no structural change applied). Populated §4/§5/§8 actuals. Native `Level N` only, no Level 4/5 (verification-light); everything R0, not cleared for external reliance. Catalog SRC-0104…0123 cited, unmodified. Pending ROLE-0004 review and ROLE-0001 validation.|
|0.1|2026-07-21|Draft|Opened as scaffold per owner-ratified brief. First family investigation of the ADR-GOV-0009 timeline program; first consumer of the Iranian standing source base (SRC-0104…SRC-0123) and the lineage anchors (STD-0004 v1.2 `branches_from`, STD-0002 v1.10 tradition-entity fields, TPL-0006). Zero claims/entities/edges — awaiting circuit under brief 2. Five-claim (one-per-tradition) decomposition with separable (i) emergence dating / (ii) descent relationship / (iii) rival reading elements; working `branches_from` hypotheses stated as tests, not conclusions; distinctness threshold (§2.3) and Anchor Fit Assessment (§7(a)) reserved as the stress-test deliverables; source discipline, thin-base authorization, metaphysical bracket, native-Level-N, and R0 §7.5-analog gate declared at opening. No frontmatter relationship edges (D4); no catalog, INV-0011, closed-record, Standard, Baseline, or Architectural Decisions modification.|
|0.5|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

# End INV-0016
