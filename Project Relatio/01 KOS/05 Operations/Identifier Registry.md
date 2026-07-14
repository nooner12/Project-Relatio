---
title: Identifier Registry
document_type: Navigation Document
version: 1.13
status: Adopted
operational_status: Active
created: 2026-07-09
parent_documents:
  - STD-0001 Naming & Identification Standard
  - KOS-0011 Governance, Stewardship & Evolution Framework
related_documents:
  - OPS-0001 Knowledge Base Organization
  - OPS-0002 Relationship Integrity & Graph Maintenance
tags:
  - ProjectRelatio
  - Operations
  - Registry
  - Identifiers
---

# Identifier Registry

## Version 1.13

## Active Navigation Document

---

# 1. Purpose

The authoritative inventory of every assigned identifier in Project Relatio. It fulfils the registry promised by STD-0001 §18, and serves two operational functions:

- **Collision prevention** — the single place to check the next free number before assigning an identifier (Pressure Test F-9).
- **Graph source of truth** — the canonical list of what exists, so relationship integrity (OPS-0002) can flag references to non-existent objects.

This is a living record; update it whenever an identifier is assigned, retired, or superseded.

---

# 2. Registry (as of 2026-07-09)

## CON — Constitution
CON-0001, CON-0002, CON-0003, CON-0004. — **Next: CON-0005.**

## KOS — Kernel Operating System
KOS-0001, KOS-0003, KOS-0004, KOS-0005, KOS-0006, KOS-0007, KOS-0008, KOS-0009, KOS-0010, KOS-0011, KOS-0012.
- KOS-0002 — **Superseded** by KOS-0004 (archived).
- KOS-0100 — **Retired**; migrated to ROLE-0001.
- KOS-0200 — **Superseded / Archived** (2026-07-11, GB-2026-007). "Standards Framework" Draft, never adopted; its role is fulfilled by STD-0001…0007 + the Standards Index/Manifest. Moved to `07 Archive`.
- KOS-0013 … KOS-0016 — **Reserved** (deferred candidates: Human Development, Communication, Ethical Reasoning, Reality Integration — see Kernel Status §8).
- **Next free: KOS-0017.**

## STD — Standards
STD-0001, STD-0002, STD-0003, STD-0004, STD-0005, STD-0006, STD-0007. — **Next: STD-0008.**

## ADR — Architecture Decision Records
- **ADR-GOV-0001** (Governance and Role Reconciliation) — Adopted. First ADR; inaugurates the practice.
- **ADR-GOV-0002** (Guardrail and Scope Reframe) — Adopted 2026-07-11. Reframes the over-architecture guardrail (fear → merit principle) and clarifies the health/education scope.
- ADR-KOS-0001 … ADR-KOS-0010 — the former phantom references (Retrospective C-9) were **removed 2026-07-10** (GB-2026-005 resolved); these identifiers are now unused/available.
- Format: `ADR-[CATEGORY]-NNNN` (GOV, KOS, …). — **Next: ADR-GOV-0003.**

## ROLE — Roles
- ROLE-0001 (Knowledge Architect) — **Adopted v1.1**. Implements ST-001.
- ROLE-0002 (Research Specialist) — **Adopted v1.0**. Implements ST-002.
- ROLE-0003 (Research Council Coordinator) — **RETIRED** 2026-07-09 (`07 Archive/`; no warrant; ADR-GOV-0001).
- ROLE-0004 (Critical Reviewer) — **Adopted v1.0**. Implements ST-004; epistemic validation (STD-0006 §8).
- ROLE-0005 (Vision Steward) — **Adopted v1.0**. Implements CON-0003 §4.1; owner authority (with constitutional limits).
— **Next: ROLE-0006.** (See the **Roles Index** for the canonical Function → ST-role → ROLE mapping.)

## TPL — Templates
TPL-0001 (Claim), TPL-0002 (Source), TPL-0003 (Investigation), TPL-0004 (Finding), TPL-0005 (ADR). — **Next: TPL-0006** (candidate: Entity template, if entities recur).

## OPS — Operations
OPS-0001 (KB Organization), OPS-0002 (Relationship Integrity), OPS-0003 (Research Workflow). — **Next: OPS-0004.**
Unnumbered Operations records: Identifier Registry, Governance Backlog, Standing Authorizations, Architecture Baseline.

## INV — Investigations
INV-0001 (Jesus & Daoism), INV-0002 (Phantom Traffic Jams), INV-0003 (Wu Wei), INV-0004 (Metformin Discontinuation & T2D Remission), INV-0005 (Chronic Stress Interventions), INV-0006 (Wellness Intervention Adherence & Maintenance), INV-0007 (Formal Constraints in Knowledge Systems), INV-0008 (Skills-Based Child Development Programming — **health/high-stakes class; gated STD-0006 §7.5**). — **Next: INV-0009.**

## CLM — Claims
CLM-0001, CLM-0002 (INV-0001); CLM-0003, CLM-0004 (INV-0002); CLM-0005, CLM-0006 (INV-0003); CLM-0007 … CLM-0012 (INV-0004); CLM-0013 … CLM-0018 (INV-0005); CLM-0019 … CLM-0026 (INV-0006); CLM-0027 … CLM-0033 (INV-0007); CLM-0034 … CLM-0040 (INV-0008). — **Next: CLM-0041.**

## SRC — Sources
SRC-0001 (Gospels), SRC-0002 (Daoist Corpus), SRC-0003 (Sugiyama 2008), SRC-0004 (Jamiton Modeling), SRC-0005 (Slingerland), SRC-0006 (DiRECT Trial Programme), SRC-0007 (Taylor Twin-Cycle Mechanism), SRC-0008 (Virta Health Trial), SRC-0009 (STAMPEDE Surgery Trial), SRC-0010 (ADA/EASD Remission Consensus), SRC-0011 (Diet & Exercise Literature), SRC-0012 (Khoury 2015 MBSR Meta-Analysis), SRC-0013 (de Vibe 2017 Campbell MBSR Review), SRC-0014 (Goyal 2014 JAMA Meditation Meta-Analysis), SRC-0015 (Goessl 2017 HRV Biofeedback Meta-Analysis), SRC-0016 (Cochrane Individual-Level Occupational Stress — Tamminga 2023), SRC-0017 (Cochrane Organizational-Level Occupational Stress), SRC-0018 (CBT-I Long-Term Meta-Analysis), SRC-0019 (Holt-Lunstad 2010 Social Relationships & Mortality), SRC-0020 (Physical Activity, Cortisol & Stress Literature), SRC-0021 (Nature Exposure & Stress Literature), SRC-0022 (Coping Theory & Problem-Focused Coping Literature), SRC-0023 (McEwen Allostatic Load Literature), SRC-0024 (Kwasnicka 2016 Maintenance Theories), SRC-0025 (Rhodes & de Bruijn 2013 Intention-Behaviour Gap), SRC-0026 (Michie 2009 Effective Techniques Meta-Regression), SRC-0027 (Harkin 2016 Progress Monitoring), SRC-0028 (Gollwitzer & Sheeran 2006 Implementation Intentions), SRC-0029 (Lally 2010 Habit Formation), SRC-0030 (Teixeira 2012 Exercise & SDT), SRC-0031 (Mantzari 2015 Financial Incentives), SRC-0032 (Eysenbach 2005 Law of Attrition), SRC-0033 (Ashford 2010 Self-Efficacy & Physical Activity), SRC-0034 (Baumel 2019 Objective Engagement with Mental Health Apps), SRC-0035 (Adler & Borys 1996 Enabling vs Coercive Bureaucracy), SRC-0036 (Hansen, Nohria & Tierney 1999 Codification vs Personalization), SRC-0037 (Simmons, Nelson & Simonsohn 2011 False-Positive Psychology), SRC-0038 (Szollosi et al. 2020 Is Preregistration Worthwhile), SRC-0039 (Meyer & Rowan 1977 Myth & Ceremony / Decoupling), SRC-0040 (Campbell 1979 Campbell's Law), SRC-0041 (March 1991 Exploration & Exploitation), SRC-0042 (Ostrom 1990 Governing the Commons), SRC-0043 (Merton 1940 Bureaucratic Structure & Personality / Goal Displacement), SRC-0044 (Polanyi 1966 The Tacit Dimension), SRC-0045 (Timmermans & Epstein 2010 A World of Standards), SRC-0046 (Brussoni et al. 2015 Risky Outdoor Play — GRADE review), SRC-0047 (Kaleta et al. 2025 Nature-Based Interventions Review of Reviews), SRC-0048 (DuBois et al. 2011 Mentoring Meta-Analysis — d ≈ 0.21), SRC-0049 (Tierney, Grossman & Resch 1995 Big Brothers Big Sisters RCT), SRC-0050 (Multon, Brown & Lent 1991 Self-Efficacy & Academic Outcomes), SRC-0051 (Rosanbalm & Murray 2017 Co-Regulation Practice Brief, OPRE 2017-79), SRC-0052 (Fiese et al. 2002 Family Routines & Rituals Review), SRC-0053 (Bandura 1997 Self-Efficacy: The Exercise of Control — catalogued in RQ-0008 remediation). — **Next: SRC-0054.**

## ENT — Entities
ENT-0001 (Wu Wei), ENT-0002 (Ziran), ENT-0003 (Allostatic Load), ENT-0004 (Intention-Behaviour Gap), ENT-0005 (Enabling vs Coercive Formalization), ENT-0006 (Co-Regulation). — **Next: ENT-0007.**

## FND — Findings
FND-0001 (Resonant Ethic, Opposed Ultimates), FND-0002 (Jams as Emergent Instability), FND-0003 (Wu Wei as Non-Forcing Action), FND-0004 (Evidence-Based Pathways to T2D Remission & Safe De-prescribing), FND-0005 (Durable Chronic-Stress Relief Requires Stressor Reduction Plus Response Regulation), FND-0006 (What Best Supports Sustained Wellness Behaviour — best-evidenced levers of maintenance; renamed from the longer "…Built by…" title 2026-07-11), FND-0007 (Value and Failure of Formal Constraints), FND-0008 (Skills Programming Evidence — ingredients individually supported unevenly; compound untested). — **Next: FND-0009.**

---

# 3. Unnumbered Meta-Documents

These are authoritative navigational/architectural documents that intentionally carry **no** `TYPE-NNNN` identifier (precedent: indexes and status records):

- KOS Architecture Manifest; Kernel Index; KOS Dependency Map; Kernel Status.
- Standards Index; Standards Dependency Map; Standards Status; Standards Architecture Retrospective.
- Roles Index.
- Per-run review/assessment reports: Pressure Test Report – RQ-0001; Second-Run Friction Assessment – RQ-0002; Third-Run Assessment – RQ-0003; Critical Review – RQ-0004 (ROLE-0004); Fourth-Run Assessment – RQ-0004 (coordinator); Critical Review – RQ-0005; Critical Review – RQ-0006 (ROLE-0004); Sixth-Run Assessment – RQ-0006 (coordinator); Critical Review – RQ-0007 (ROLE-0004); Seventh-Run Assessment – RQ-0007 (coordinator, pre-registered — filing imminent); Critical Review – RQ-0008 (ROLE-0004, health/high-stakes — Conformant with Flags).
- Identifier Registry (this document); Governance Backlog; Standing Authorizations; Architecture Baseline.

---

# 4. Maintenance

Per OPS-0002 and STD-0006: before assigning a new identifier, consult this registry and use the listed "Next" value; after assigning, update it. Retirements and supersessions are recorded here as well as on the object (STD-0005).

---

# 5. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Active|Initial registry; fulfils STD-0001 §18. Inventories all identifiers assigned through the third research workflow.|
|1.1|2026-07-09|Active|Roles layer authored: ROLE-0001 Adopted; ROLE-0002/0003 Draft; ROLE-0004 (Critical Reviewer) added as a new proposed role. OPS-0003 (Research Workflow) registered.|
|1.2|2026-07-09|Active|Governance assessment: ROLE-0003 retired; ROLE-0005 (Vision Steward) added; ADR class opened (ADR-GOV-0001); TPL-0005 (ADR template) added; Governance Backlog and Standing Authorizations registered.|
|1.3|2026-07-09|Active|ROLE-0002/0004/0005 ratified to Adopted v1.0.|
|1.4|2026-07-10|Active|Fourth research workflow (INV-0004, RQ-0004, T2D remission / metformin): registered INV-0004; CLM-0007…CLM-0012; SRC-0006…SRC-0011; FND-0004. Objects Draft, pending ROLE-0004 review and ROLE-0001 conformance.|
|1.5|2026-07-10|Active|Fifth research workflow (INV-0005, RQ-0005, chronic-stress interventions & durability): registered INV-0005; CLM-0013…CLM-0018; SRC-0012…SRC-0023; ENT-0003 (Allostatic Load); FND-0005. Objects Draft, pending ROLE-0004 review and ROLE-0001 conformance.|
|1.6|2026-07-11|Active|Registered the **Architecture Baseline** (unnumbered Operations governance record, Phase II M1). Vault-wide lifecycle & relationship migrations (GB-2026-006 / GB-2026-001) added `operational_status` and typed `relationships` frontmatter — no new identifiers assigned.|
|1.7|2026-07-11|Active|Sixth research workflow (INV-0006, RQ-0006, wellness-intervention adherence & maintenance): registered INV-0006; CLM-0019…CLM-0026; SRC-0024…SRC-0032; ENT-0004 (Intention-Behaviour Gap); FND-0006. First KB objects authored with the new two-lifecycle-field + typed-`relationships` metadata. Objects Draft, pending ROLE-0004 epistemic review and ROLE-0001 conformance.|
|1.8|2026-07-11|Active|INV-0006 circuit completed: registered Critical Review – RQ-0006 (Conformant with Flags) and Sixth-Run Assessment – RQ-0006 in §3; back-filled the previously-unlisted Critical Review – RQ-0005. Reconciled the frontmatter version / `## Version` heading drift (→1.8) during ROLE-0001 validation.|
|1.9|2026-07-11|Active|RQ-0006 remediation pass (ROLE-0002, owner-approved): registered **SRC-0033** (Ashford 2010 self-efficacy → CLM-0020) and **SRC-0034** (Baumel 2019 app attrition → CLM-0022), closing two evidentiary gaps flagged by ROLE-0004. **FND-0006 renamed** "…Is Built by…" → "What Best Supports Sustained Wellness Behaviour" (title softened to match the Level-3 body; filename shortened to clear the Windows MAX_PATH limit). Old-named FND-0006 file left as a redirect stub pending ROLE-0001 `git rm`. Next SRC → SRC-0035.|
|1.10|2026-07-11|Active|Registered **ADR-GOV-0002** (Guardrail and Scope Reframe). Next ADR → ADR-GOV-0003.|
|1.11|2026-07-12|Active|Seventh research workflow (INV-0007, RQ-0007, formal constraints in knowledge systems): registered INV-0007; CLM-0027…CLM-0033 (three value, three failure-mode, one synthesis); SRC-0035…SRC-0042; ENT-0005 (Enabling vs Coercive Formalization); FND-0007 (Value and Failure of Formal Constraints). Next values advanced (INV-0008, CLM-0034, SRC-0043, ENT-0006, FND-0008). Objects Draft, in the ROLE-0004 / ROLE-0001 review circuit. Registered during ROLE-0001 structural validation (SA-001).|
|1.12|2026-07-12|Active|INV-0007 post-review remediation (Critical Review – RQ-0007 + ROLE-0001 structural flags): registered **SRC-0043** (Merton 1940 → CLM-0031 goal-displacement anchor), **SRC-0044** (Polanyi 1966 → CLM-0029 tacit-loss anchor), **SRC-0045** (Timmermans & Epstein 2010 → CLM-0033 steelman, `contrasts_with`) — converting previously-invoked companions into catalogued sources; Next SRC → SRC-0046. Registered Critical Review – RQ-0007 in §3 and pre-registered Seventh-Run Assessment – RQ-0007. Re-validated during ROLE-0001 SA-001 pass (validate.py + graph_integrity.py clean; no new advisories involve INV-0007).|
|1.13|2026-07-14|Active|Eighth research workflow (INV-0008, RQ-0008, skills-based child-development programming — **health/high-stakes class, gated STD-0006 §7.5**): registered INV-0008; CLM-0034…CLM-0040 (six evidence domains + one integrative evidence-gap claim); SRC-0046…SRC-0052 (seven live-verified sources); ENT-0006 (Co-Regulation); FND-0008. Circuit completed: **Critical Review – RQ-0008 Conformant with Flags** (no fabrication; DuBois d ≈ 0.21, Multon, Bandura independently re-verified) — remediation catalogued **SRC-0053** (Bandura 1997) to anchor CLM-0036's "strongest source" half. Next values advanced (INV-0009, CLM-0041, SRC-0054, ENT-0007, FND-0009). Registered/validated during ROLE-0001 pass (validate.py PASS 182 files 0/0; graph_integrity.py exit 0 — no dangling refs; only pre-existing vault-wide symmetric-link advisories). Findings remain Draft and **externally gated pending independent re-verification.**|

---

# End Identifier Registry
