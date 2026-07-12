---
title: Governance Backlog
document_type: Governance Record
version: 1.10
status: Adopted
operational_status: Active
created: 2026-07-09
parent_documents:
  - KOS-0011 Governance, Stewardship & Evolution Framework
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - Standards Architecture Retrospective
  - Pressure Test Report - RQ-0001
  - Second-Run Friction Assessment - RQ-0002
  - Third-Run Assessment - RQ-0003
  - Identifier Registry
tags:
  - ProjectRelatio
  - Governance
  - Backlog
---

# Governance Backlog

## Version 1.10

## Active Governance Record

---

# 1. Purpose

The single, authoritative list of **unresolved decisions, improvement opportunities, architectural questions, and future revisions** — as mandated by **KOS-0011 §9 (GB-001)**, which required a governance backlog that was never built.

Before this document existed, open items were scattered across five places: the Standards Architecture Retrospective's migration register, CLAUDE.md's deferred list, and three research assessment reports. Consolidating them is the point.

**Entry format (GB-001):** Issue → Context → Impact → Priority → Potential Solutions → Decision Status.

**Discipline:** an item on this list is *not* a commitment to build. Per the scope guardrail, nothing is actioned without **demonstrated need** or Vision Steward approval. Deferral is a legitimate, recorded outcome.

---

# 2. Open Items

---

## GB-2026-001 — Typed relationships in frontmatter
- **Issue:** STD-0004 defines a relationship vocabulary (`supports`, `derived_from`, `contrasts_with`…) but STD-0002 frontmatter carries only untyped `related_documents`. Types live in object bodies.
- **Context:** Pressure Test F-4; recurred in every investigation.
- **Impact:** Medium. Tooling (Dataview) can see links but not their meaning; graph queries are weaker than the architecture promises.
- **Solutions:** (a) extend STD-0002 to carry typed relations; (b) formally rule that types live in the body only.
- **Status:** **RESOLVED 2026-07-11 — owner-directed (option a).** STD-0002 §7 (v1.6) adds an optional typed **`relationships`** block (`type` + `target`, STD-0004 vocabulary); STD-0004 §7.1 (v1.1) records the machine encoding — no vocabulary change. The flat `parent_documents`/`related_documents` lists are retained for tooling. **All 52 KB objects back-encoded** (222 typed edges, transcribed from their stated body §Relationships). `graph_integrity.py` made **type-aware**: symmetric types (`related_to`/`contrasts_with`) are checked for reciprocity, directional types are not (43 crude one-directional flags → 32 genuine symmetric-asymmetry advisories). Templates TPL-0001…0004 carry the block. Verified: validate.py 115/0, graph 0 dangling. Moved to §3.

## GB-2026-002 — Quantitative evidence fields
- **Issue:** KOS-0003 §5 grades evidence 0–5 but has no field for sample size, effect size, replication count, or numeric results.
- **Context:** Second-Run Friction Assessment F-10 (surfaced by an empirical investigation; absent from interpretive ones).
- **Impact:** Medium, domain-specific. Partly mitigated by KOS-0003 §9 (Consensus Evaluation).
- **Solutions:** add optional quantitative-evidence fields to the Claim structure (KOS-0003 minor revision).
- **Status:** **Deferred by decision.** Threshold: act only if a *third* empirical investigation strains against it. One instance is not demonstrated need.

## GB-2026-003 — Entity template (TPL)
- **Issue:** No template for Entity records; ENT-0001/0002 were hand-authored from KOS-0012 §5.5.
- **Context:** Third-Run Assessment F-13.
- **Impact:** Low.
- **Solutions:** create an Entity template.
- **Status:** **Deferred.** Threshold: entities recur in a future investigation.

## GB-2026-004 — Graph-integrity automation
- **Issue:** Relationship reciprocity and dangling-reference checks were manual (OPS-0002 §6).
- **Context:** Third-Run Assessment F-12; the fourth run (agent circuit) confirmed the manual check is real per-run work.
- **Status:** **RESOLVED 2026-07-10.** Built `tools/graph_integrity.py` (dangling-reference + one-directional-link report over the actual `related_documents`/`parent_documents` convention). The Knowledge Architect and agent now run it instead of tracing by hand. OPS-0002 §6 rewritten. Moved to §3.

## GB-2026-005 — Phantom ADR references
- **Issue:** `ADR-KOS-0001` … `ADR-KOS-0010` are cited in KOS-0003 and KOS-0011 but do not exist.
- **Context:** Retrospective C-9 / migration M-3.
- **Impact:** Medium. Dangling references in Adopted Kernel documents; a standing STD-0006 non-conformance.
- **Solutions:** (a) remove/reword the references; (b) write the ADRs (rejected — over-architecture).
- **Status:** **RESOLVED 2026-07-10.** `graph_integrity.py` surfaced the 9 phantom references as dangling failures on every run, making the deferral's cost concrete. Resolved by replacing the dead pointers with genuine relationships (verify-then-remove; verified non-existent): KOS-0003's 8 `ADR-KOS-0001…0008` → `STD-0006` (which operationalizes §12.1); KOS-0011's `ADR-KOS-0010` → the real `ADR-GOV-0001`. Tool now exits clean (0 dangling). KOS-0003 → v1.2, KOS-0011 → v1.2. Moved to §3.

## GB-2026-006 — Two-dimensional lifecycle field
- **Issue:** STD-0005 and CLAUDE.md mandate independent Maturity and Operational states; documents carry a single `status`.
- **Context:** Retrospective M-1.
- **Impact:** Low today.
- **Solutions:** add `operational_status` across ~24 documents.
- **Status:** **RESOLVED 2026-07-11 — owner-directed.** The deferral trigger (a real supersession/archival event) fired: KOS-0200 superseded/archived and ROLE-0003 retired. Implemented per STD-0005's two-dimensional model: STD-0002 v1.5 narrows `status` to **maturity** and adds the required **`operational_status`** (Active/Superseded/Archived); STD-0005 §24 → v1.1 names the two fields. **Migrated 109 governed objects** (the 8 that held an operational value in `status` had it moved to the new field: 6 Active governance/nav records → maturity Adopted; KOS-0002 → Draft/Superseded; KOS-0200, ROLE-0003 → Draft/Archived). Templates updated. Verified: validate.py 115/0. Moved to §3.

## GB-2026-007 — KOS-0200 fate
- **Issue:** KOS-0200 "Standards Framework" (Draft, v0.1) appears to duplicate the purpose of the Standards Index and Manifest.
- **Context:** Retrospective M-5 / C-11. Still carries an unapproved `document_type` ("Operational Framework").
- **Impact:** Low. Confusing but inert.
- **Solutions:** supersede and archive it, or adopt and retype it.
- **Status:** **RESOLVED 2026-07-11 — owner-directed: superseded & archived.** KOS-0200 was never adopted and its role is fulfilled by the adopted STD-0001…0007 series + the Standards Index/Manifest/Dependency Map (its §4 six-category taxonomy was a *non-adopted* proposal). Moved to `07 Archive` as "KOS-0200 - Standards Framework (Superseded).md" with `status: Archived` and a supersession banner. Live references updated (Identifier Registry, Standards Status, Retrospective M-5, CLAUDE.md). Verified: validate.py clean, graph 0 dangling. Moved to §3.

## GB-2026-008 — ST-003 Domain Specialist unimplemented
- **Issue:** KOS-0011 §10 defines ST-003 Domain Specialist; no ROLE implements it.
- **Context:** Governance assessment. Three investigations (religion, physics, Chinese philosophy) showed no need — the Research Specialist handled all domains.
- **Impact:** Low.
- **Solutions:** implement as ROLE-NNNN if domain depth becomes a bottleneck.
- **Status:** **Deferred.** Do not implement speculatively.

## GB-2026-009 — Source metadata for non-modern sources
- **Issue:** STD-0002 §11 (`source_author`, `source_url`, `publication_date`) assumes a modern, single-author, dated source.
- **Context:** Pressure Test F-3. **Confirmed domain-specific** — modern scientific sources (SRC-0003/0004) fit cleanly; ancient/composite texts did not.
- **Impact:** Low. Honest prose qualification in the fields is an adequate interim.
- **Solutions:** add optional fields/guidance for composite and ancient sources.
- **Status:** Open, low priority.

## GB-2026-010 — ADR practice adopted, not backfilled
- **Issue:** CON-0003 §7 states significant decisions **shall** be preserved as ADRs. None existed; many significant decisions were made.
- **Context:** Governance assessment R8.
- **Impact:** Medium — institutional memory of *why* decisions were made.
- **Solutions:** adopt ADRs going forward (done: TPL-0005, ADR-GOV-0001); do **not** backfill.
- **Status:** **Resolved going forward.** Backfill explicitly declined as bureaucracy.

## GB-2026-011 — Role authority ratification outstanding
- **Issue:** ROLE-0002, ROLE-0004, and ROLE-0005 carried **PROPOSED** Authority (§4) and Boundaries (§5). Only ROLE-0001 was ratified.
- **Context:** Authority definition is Vision-Steward-reserved (ROLE-0001 §4.2).
- **Impact:** High while open — the research circuit ran on Draft definitions.
- **Status:** **RESOLVED 2026-07-09.** The Vision Steward ratified all three to **Adopted v1.0**, with two refinements applied at ratification: (1) ROLE-0002 §4.2a scope boundary (disambiguation vs. material redirection); (2) ROLE-0004 §5 procedural-independence limit. ROLE-0005's constitutional limits were accepted as binding on the owner. SA-002/SA-003 made non-provisional. Moved to §3.

## GB-2026-012 — Layer-stack vs governance-level mismatch
- **Issue:** The Manifest §12 layer stack (Kernel→Standards→Roles→Templates→Operations→Research) does not align with KOS-0011 §8 governance levels (Constitution→Kernel→Standards→Procedures→Experiments). Roles appear in one, not the other.
- **Context:** Governance assessment.
- **Impact:** Low. Cosmetic inconsistency; no operational effect.
- **Solutions:** reconcile the two hierarchies in a future Kernel review.
- **Status:** Open, low priority.

## GB-2026-013 — Circuit cost / tiered workflow
- **Issue:** The full Specialist→Reviewer→Architect circuit is resource-intensive (RQ-0004, Fourth-Run Assessment F-14); the reviewer was interrupted by a session limit. May be disproportionate for low-stakes questions.
- **Impact:** Medium. Efficiency/usability.
- **Status:** **Partially addressed 2026-07-10.** The *proportionality rule* is now in OPS-0003 §2.1 (full circuit for high-stakes, lean path for low; default-to-full when uncertain), plus §3.1 efficiency refinements (review-targeting handoff, parallel Reviewer∥Architect, automated structural check). A fuller build-out of the lean path (its own defined sub-procedure) remains **trigger-gated**: act only if a *fifth*, routine question reproduces the cost friction. Not to be over-built on one data point.

## GB-2026-016 — validate.py aligned to title-embedded identifiers
- **Issue:** The older `tools/validate.py` checks for an `id:` frontmatter field and `[[wikilinks]]`, neither of which the adopted STD-0001/0002 convention uses (identifier is title-embedded; graph is in `related_documents`). Its `id` check is disabled for now (`requires_id: false`).
- **Impact:** Low. It still does useful checks (empty files, YAML validity, duplicate filenames, broken wikilinks); graph_integrity.py covers the graph.
- **Solutions:** update validate.py to validate the title-embedded identifier and filename/title parity instead of an `id` field.
- **Status:** **RESOLVED 2026-07-11.** `validate.py` rebuilt: `requires_id`/`id:` replaced with `requires_identifier`, which checks that the **filename carries a valid identifier, the `title:` carries the same one, and the identifier is unique** across the vault (handles both `TYPE-NNNN` and `ADR-CAT-NNNN`). Added `extract_identifier()` to `common.py`. Removed the stale broken-`[[wikilink]]` pass (not the adopted convention; it false-flagged prose). Verified: **114 files, 0 errors, 0 warnings.** README updated. Moved to §3.

## GB-2026-017 — Propagate ontological-humility + relationalism from CON-0004 §2
- **Issue:** The foundational audit (2026-07-11) revised CON-0004 §2 from a critical-realist orientation to **ontological humility + relationalism** (owner-directed). Other documents may still carry the older critical-realist framing.
- **Impact:** Medium — foundational coherence.
- **Solutions:** review KOS-0003 (Epistemic Framework) and KOS-0004 (Ontology) for residual "critical realism" language and reconcile to the new stance; consider whether CON-0001 Axiom 1 / §6 and KOS-0004's ontology should foreground relationalism explicitly. Owner-reserved (Constitution/Kernel).
- **Status:** **Largely RESOLVED 2026-07-11.** A Kernel-wide search for "critical realis*/realist/realism" returned **zero** matches — the framing existed only in CON-0004 §2 (now amended). Residual (optional): decide whether KOS-0004's ontology and CON-0001's axioms should *foreground* relationalism affirmatively (not merely lack the old term) — fold into GB-2026-018.

## GB-2026-018 — Foundational (Kernel) audit — continue
- **Issue:** The 2026-07-11 audit covered the **Constitution** (CON-0001/0002/0004) fully; the **Kernel** document bodies (KOS-0001, 0004–0010 — ChatGPT-era authorship) were not yet audited for coherence, over-claims, and alignment.
- **Impact:** Medium.
- **Solutions:** audit the Kernel in a fresh session, priority order **KOS-0005 (Relationship Modeling)** then **KOS-0004 (Ontology)** — the two most central to the project's relational aim — then KOS-0001, 0003, 0006–0010. Fold in GB-2026-017.
- **Status:** In progress. **KOS-0005 (Relationship Modeling) audited AND revised → v1.1 (2026-07-11):** A (two-vocabulary distinction), B (§6A descriptive/normative separation — owner ratified the value-is-standpoint-relative principle), C (Transcendent softened), D (relationalism cross-ref) all applied. **KOS-0004 (Ontology) audited AND revised → v1.1 (2026-07-11):** fixed `version` field (`1`→`1.1`); §2 aligned to CON-0004 §2 (minimal realism under humility+relationalism); RM-003 relationship list deferred to KOS-0005 as authoritative + distinguished from STD-0004 graph relations. KOS-0004 was already descriptively clean (no normative baking-in). **Deep question resolved (GB-2026-019): co-primary decided and applied (as a working lens under humility) — KOS-0004 → v1.3, KOS-0005 → v1.3.** **Remaining Kernel audited AND revised (2026-07-11):** **KOS-0001 → v1.1** (§7 stale "currently consists of" list corrected → defers to Kernel Index); **KOS-0003 → v1.3** (stale "Version 1.0" reference fixed; co-primacy propagated into §10 Assumption Mapping); **KOS-0006 → v1.1** (§10 Flourishing Assessment scoped as a normative overlay per KOS-0005 §6A); **KOS-0009 → v1.1** (four competing-authority deference notes — §5→KOS-0012, §6→STD-0005, §7→STD-0002, §10→STD-0004/KOS-0005); **KOS-0010 → v1.1** (empty RS-004 filled; RS-003 numbering gap closed; "Research Architect"→ROLE-0001 reconciliation note). KOS-0007 and KOS-0008 audited — clean; minor items flagged (below). **Judgment calls spun out:** GB-2026-020 (Research Architect rename), GB-2026-021 (confidence-scale reconciliation KOS-0003 vs KOS-0008), GB-2026-022 (CON-0001/KOS-0001 "creation" wording). STD-0004 reciprocal cross-ref for the two-vocabulary distinction remains a small pending follow-up. **Status: Kernel audit substantially COMPLETE** — Constitution + all Kernel document bodies now audited.

## GB-2026-019 — Relationalism: ontological primacy vs. entity-first (Vision-Steward decision)
- **Issue:** CON-0004 §2 now adopts relationalism, but KOS-0004's ontology is still **entity-first** — RM-001 Entities is the lead dimension; relationships are one of five dimensions (RM-003) and one principle (OP-003). Strong relationalism holds that **relations are ontologically primary** — entities are partly *constituted by* their relationships, not merely connected after the fact.
- **Impact:** Medium–High (philosophical identity of a project named *Relatio*).
- **Options:** (a) keep entity-first, relationalism as interpretive lens (current); (b) elevate relations to *co-primary* with entities; (c) full relationalism — relations primary, entities as relational nodes. Each has trade-offs for how research is structured.
- **Status:** **RESOLVED 2026-07-11 — Vision-Steward decision: option (b), co-primary — adopted as a *working lens*, not a metaphysical verdict.** Implemented in **KOS-0004 → v1.3**: §2 *Entity–Relationship Co-Primacy* statement; §4 names RM-001 Entities and RM-003 Relationships as the two co-foundational dimensions; OP-003 retitled and rewritten. Coherence cross-ref in **KOS-0005 → v1.3** (§3). **Refinement (owner-directed, same session):** consistent with the project's own OP-006 (Ontological Humility) and OP-008 (Tension Preservation), co-primacy is the **default modeling lens** — entity-first and strong/eliminative relationalism are held as **viable perspectives** (evaluated comparatively, OP-007; tension preserved, OP-008), **not rejected**, until substantiated evidence settles a case. CON-0004 §2 already supported the stance — no change needed. Moved to §3.

## GB-2026-020 — "Research Architect" legacy name vs adopted "Knowledge Architect"
- **Issue:** KOS-0010 §17 defines a "Research Architect Role" (integrate specialist research, connect specialists). No role by that exact name was adopted; the function is fulfilled by the **Knowledge Architect (ROLE-0001)** (with Vision-Steward coordination, ROLE-0005).
- **Context:** Kernel audit (GB-2026-018), 2026-07-11. A reconciliation note was added to KOS-0010 §17 pointing to ROLE-0001; the *rename* itself was not made (roles/terminology are owner-reserved — STD-0007, ROLE-0001 §4.2).
- **Impact:** Low–Medium. Terminology drift; a reader could infer a role that doesn't exist.
- **Options:** (a) rename §17 to "Knowledge Architect Function" and reword; (b) keep the legacy name with the clarifying note (current); (c) leave for a broader terminology pass.
- **Status:** **RESOLVED 2026-07-11 — owner-directed: option (a).** KOS-0010 §17 renamed "Research Architect Function/Role" → **"Knowledge Architect Function,"** pointing to **ROLE-0001**; the legacy name is retained only as a noted historical alias. KOS-0010 → v1.2. Rename confined to §17 (verified by vault search — no other substantive occurrences). Moved to §3.

## GB-2026-021 — Two confidence scales in the Kernel
- **Issue:** KOS-0003 §8 defines confidence as **numeric Level 0–5** (six tiers, incl. Level 0 Unsupported); KOS-0008 §8 defines it as **labels Very High → Very Low** (five tiers). They map roughly but are not identical, and both are Adopted Kernel.
- **Context:** Kernel audit (GB-2026-018), 2026-07-11.
- **Impact:** Medium. Two scales risk inconsistent confidence ratings across investigations.
- **Options:** (a) make KOS-0003's 0–5 canonical and have KOS-0008 defer to it; (b) publish an explicit mapping table; (c) reconcile to a single scale in a Kernel review.
- **Status:** **RESOLVED 2026-07-11 — owner-directed: a single canonical *hybrid* scale.** Confidence is one scale written as **"Level N (Label)"** — numeric level 0–5 paired with a qualitative label (Very High → Very Low, plus an Unsupported Level-0 floor). The descriptive label carries the meaning (relational, non-quantitative emphasis per owner); the number is an ordinal marker only. KOS-0003 §8 restated as the canonical definition; KOS-0008 §8 aligned (Level column added); TPL-0001/TPL-0004 confidence lines updated (→ v1.1). **No Knowledge Base migration needed** — existing CLM/FND objects already use "Level N (Label)." KOS-0003 → v1.4, KOS-0008 → v1.1. Moved to §3.

## GB-2026-022 — "Creation" wording under ontological humility
- **Issue:** KOS-0001 §2 ("humanity's relationship with ultimate reality and **creation**") and similar phrasings mildly presuppose a creator, which sits slightly awkwardly with CON-0004 §2 ontological humility (no commitment to what reality ultimately is).
- **Context:** Kernel audit (GB-2026-018), 2026-07-11.
- **Impact:** Low. Aspirational-charter language, not an operative claim.
- **Options:** soften "creation" → "origins" / "claimed creation," or leave as a listed domain of inquiry.
- **Status:** **RESOLVED 2026-07-11 — owner-directed: softened, held open.** KOS-0001 §2 → "ultimate reality and the question of origins (including creation claims)," plus a note framing origin/ultimate-reality as **open questions** under ontological humility — no account (creator-based, naturalistic, or other) presumed; all open to evidence and revision. Survey confirmed this was the only occurrence in the project's own voice (other "creation"/"creator" hits correctly attribute the concept to specific traditions and were left unchanged). KOS-0001 → v1.2. Moved to §3.

## GB-2026-014 — Verification-light reviews must gate reliance
- **Issue:** The strongest anti-fabrication check (live citation re-location, STD-0006 §5.7) depends on web tools that can be rate-limited (RQ-0004, F-15). The reviewer voluntarily marked its review verification-light and gated reliance.
- **Impact:** Medium, safety-relevant.
- **Status:** **RESOLVED 2026-07-10.** Owner-adopted as STD-0006 §7.5 (Verification Integrity); a review must disclose its verification strength, and a verification-light review may not clear an object for external reliance. Codified in the `critical-reviewer` agent. Moved to §3.

## GB-2026-015 — Mid-session agent definitions not invokable
- **Issue:** Agents created mid-session aren't registered as invokable types until reload (RQ-0004, F-16, RRI/platform).
- **Impact:** Low, platform-specific.
- **Solutions:** note in the agent-implementation docs; no architectural change.
- **Status:** Open, low priority.

## GB-2026-023 — Independent-review pathway for reflexive findings
- **Issue:** RQ-0007 (the first **reflexive** question — research whose conclusion bears on Project Relatio's own design) demonstrated that procedural independence (ROLE-0004 §5, same underlying model) is **structurally insufficient** for reflexive findings: the Specialist's synthesis imported the vault's own merit-principle vocabulary and claimed the literature "independently supports" it; the Reviewer caught the leak but correctly ruled a same-model reviewer cannot certify it caught *all* of a bias it plausibly shares (Critical Review - RQ-0007 §3.6, §6, §10).
- **Context:** Seventh-Run Assessment F-22, 2026-07-12. The STD-0006 §7.5 gate machinery absorbed the case — the reliance gate was applied to the *reflexive use* (FND-0007 may not be cited as vindication of the vault's governance), extending §7.5's logic from verification *strength* to independence *kind*. No new structure was needed to contain it; what is needed is a **decision**.
- **Impact:** Medium. Any future finding that touches the system's own design carries the same hazard; FND-0007 is gated until resolved.
- **Solutions:** (a) owner engages a genuinely independent reviewer (different model, or a human organizational-theory/KM specialist) for FND-0007 and adopts that as the standing rule for reflexive findings — candidate one-line addition to STD-0006 §7.5; (b) accept the standing gate and simply never rely on reflexive findings for self-assessment; (c) defer.
- **Status:** Open. Vision-Steward decision required.

## GB-2026-024 — validate.py descriptive filename/title parity
- **Issue:** `validate.py` (as rebuilt under GB-2026-016) checks that filename and `title:` carry the same **identifier**, not the same **descriptive text** — six INV-0007 claims shipped with long titles over short filenames and passed the validator; ROLE-0001 caught the STD-0001 §10 divergence manually (Seventh-Run Assessment F-21; recurrence context F-18/F-23).
- **Impact:** Low. Manual review catches it; two runs' data.
- **Solutions:** extend the parity check to the full descriptive text (exact match after the identifier), with the fix direction being title-shortening per the FND-0006 precedent. Pairs with the F-18/F-23 candidate STD-0001 guidance (title = filename; bound length).
- **Status:** Open, low priority — do with the next tooling touch.

---

# 3. Resolved (retained for institutional memory)

| Item | Resolution |
|---|---|
| Anti-fabrication rule lived only in `.claude/agents` (RRI) | Elevated to KOS-0003 §12.1; enforced by STD-0006 §5.7/§7.3 |
| Verification-light reviews could clear reliance (GB-2026-014) | STD-0006 §7.5 (v1.2): reviews disclose verification strength; verification-light reviews cannot clear external reliance |
| Graph-integrity checks were manual (GB-2026-004) | Built `tools/graph_integrity.py`; Architect + agent run it; OPS-0002 §6 rewritten |
| Phantom ADR references in KOS-0003/0011 (GB-2026-005/M-3) | Replaced with genuine relationships (STD-0006; ADR-GOV-0001); tool exits clean |
| Three competing role vocabularies (Functions / ST-roles / ROLE) | Reconciled; Roles Index is canonical; KOS-0011 §10 note added |
| ROLE-0003 had no architectural warrant | Retired to `07 Archive`; function absorbed by ROLE-0005 |
| Owner authority undocumented | ROLE-0005 Vision Steward created, with constitutional limits |
| STD-0006 §8 validation authority unassigned | Split: structural → ROLE-0001; epistemic → ROLE-0004 |
| No appeal path; dissent could be erased | STD-0006 §7.4 (GP-004); CR-001/2/3 taxonomy wired in |
| Identifier Registry missing (STD-0001 §18) | Created |
| KB organization / graph maintenance undefined | OPS-0001, OPS-0002 |
| No governance backlog (KOS-0011 §9) | *This document* |
| Role authority unratified (GB-2026-011) | Vision Steward ratified ROLE-0002/0004/0005 to Adopted (2026-07-09), with two refinements applied |
| Relationalism: ontological primacy vs. entity-first (GB-2026-019) | Vision-Steward decision: **co-primary as a working lens** (option b, held under ontological humility — rivals not rejected). KOS-0004 → v1.3 (§2/§4/OP-003); KOS-0005 → v1.3 coherence note |
| Kernel audit (GB-2026-018) | Constitution + all Kernel bodies audited; KOS-0001/0003/0006/0009/0010 revised; three judgment calls (GB-020/021/022) resolved below |
| "Research Architect" legacy name (GB-2026-020) | Renamed to **Knowledge Architect (ROLE-0001)** in KOS-0010 §17 → v1.2 |
| Two confidence scales in the Kernel (GB-2026-021) | Unified into one canonical **hybrid** "Level N (Label)" scale (KOS-0003 §8 v1.4, KOS-0008 §8 v1.1, TPL-0001/0004 v1.1) |
| "Creation" presumed in KOS-0001 §2 (GB-2026-022) | Softened to "the question of origins (including creation claims)," framed as open under ontological humility → v1.2 |
| validate.py used non-convention id/wikilink checks (GB-2026-016) | Rebuilt to validate the title-embedded identifier + filename/title parity + uniqueness (STD-0001/0002); wikilink pass removed; 114 files clean |
| KOS-0200 duplicative Draft (GB-2026-007) | Superseded & archived to `07 Archive`; role fulfilled by STD-0001…0007 + Standards Index; references updated |
| Single `status` conflated maturity + operational (GB-2026-006) | Two-dimensional lifecycle implemented: STD-0002 v1.5 (`status`=maturity, new `operational_status`), STD-0005 §24 v1.1; 109 objects migrated; templates updated |
| Frontmatter could not carry typed relationships (GB-2026-001 / F-4) | STD-0002 §7 v1.6 typed `relationships` block + STD-0004 §7.1 v1.1; 52 KB objects back-encoded (222 edges); graph_integrity.py made type-aware |

---

# 4. Maintenance

Any role may **add** an item. Only the Vision Steward may mark an item **Decided** or **Deferred by decision**. Items resolved move to §3 rather than being deleted (CON-0003 §9.4: historical preservation).

---

# 5. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Active|Created per KOS-0011 §9 (GB-001), consolidating open items previously scattered across the Retrospective, CLAUDE.md, and three assessment reports.|
|1.1|2026-07-09|Active|GB-2026-011 resolved: ROLE-0002/0004/0005 ratified to Adopted with two refinements. Moved to §3.|
|1.2|2026-07-10|Active|Circuit-efficiency work (owner-authorized, ADR waived): GB-2026-014 resolved (STD-0006 §7.5 verification rule); GB-2026-004 resolved (graph_integrity.py built); GB-2026-013 partially addressed (OPS-0003 §2.1 tiering rule + §3.1 refinements, fuller build trigger-gated); GB-2026-016 added (validate.py alignment); GB-2026-005 phantom-ADR cost now tool-surfaced, cleanup recommended pending owner go-ahead.|
|1.3|2026-07-11|Active|GB-2026-019 resolved — Vision-Steward decision **co-primary (option b)**; implemented in KOS-0004 v1.2 (Entity–Relationship Co-Primacy) and KOS-0005 v1.2 coherence note. GB-2026-018 advanced (deep question closed; KOS-0001/0003/0006–0010 audit still open).|
|1.4|2026-07-11|Active|**GB-2026-018 Kernel audit substantially complete.** Remaining Kernel docs audited and revised: KOS-0001 v1.1, KOS-0003 v1.3, KOS-0006 v1.1, KOS-0009 v1.1, KOS-0010 v1.1 (KOS-0007/0008 clean). Three judgment calls spun out as new items: **GB-2026-020** (Research Architect rename), **GB-2026-021** (confidence-scale reconciliation), **GB-2026-022** ("creation" wording).|
|1.5|2026-07-11|Active|**GB-2026-019 co-primacy framing refined** (owner-directed): co-primary adopted as the project's **default working lens** rather than a metaphysical verdict — entity-first and strong/eliminative relationalism held as viable perspectives under ontological humility (OP-006/OP-008), not rejected, pending substantiated evidence. KOS-0004 → v1.3, KOS-0005 → v1.3.|
|1.6|2026-07-11|Active|**Three audit judgment calls resolved (owner-directed).** GB-2026-020: "Research Architect" renamed to Knowledge Architect (ROLE-0001), KOS-0010 → v1.2. GB-2026-021: two confidence scales unified into one canonical **hybrid "Level N (Label)"** scale — KOS-0003 §8 → v1.4, KOS-0008 §8 → v1.1, TPL-0001/0004 → v1.1 (no KB migration needed). GB-2026-022: KOS-0001 §2 "creation" softened to an open "question of origins," KOS-0001 → v1.2. All three moved to §3.|
|1.7|2026-07-11|Active|**GB-2026-016 resolved:** `validate.py` rebuilt to check the title-embedded identifier + filename/title parity + uniqueness (STD-0001/0002); stale `id`/`[[wikilink]]` checks removed; 114 files validate clean. Session work committed and pushed to GitHub (public repo). Repo hygiene: `.gitignore` added; build artifacts / local settings / Obsidian UI state untracked.|
|1.8|2026-07-11|Active|**GB-2026-007 resolved (owner-directed): KOS-0200 superseded & archived.** Never-adopted "Standards Framework" Draft moved to `07 Archive` (status → Archived, supersession banner); role fulfilled by STD-0001…0007 + Standards Index. References updated (Identifier Registry, Standards Status, Retrospective M-5, CLAUDE.md). **Remaining open items (GB-001/009/012/015) intentionally left deferred** — no demonstrated need; actioning them would be over-architecture (per the CLAUDE.md scope guardrail). Backlog now at a healthy resting state.|
|1.9|2026-07-11|Active|**Phase II re-scope (owner-directed "action now").** Created the **Architecture Baseline v1.0** freeze record (Phase II brief M1). **GB-2026-006 resolved** — two-dimensional lifecycle field implemented (STD-0002 v1.5, STD-0005 §24 v1.1; 109 objects migrated); its deferral trigger (KOS-0200/ROLE-0003 supersession) had fired. **GB-2026-001 resolved** — typed `relationships` frontmatter (STD-0002 §7 v1.6, STD-0004 §7.1 v1.1; 52 KB objects / 222 edges back-encoded; graph_integrity.py type-aware; templates updated). Both moved to §3. Verified: validate.py 115/0, graph 0 dangling.|
|1.10|2026-07-12|Active|Seventh run (RQ-0007, formal constraints — first reflexive question). Added **GB-2026-023** (independent-review pathway for reflexive findings — same-model independence structurally insufficient; F-22) and **GB-2026-024** (validate.py descriptive filename/title parity blind spot; F-21). Also fixed the stale `## Version` heading (read 1.0; drift noted at ROLE-0001-style reconciliation).|

---

# End Governance Backlog
