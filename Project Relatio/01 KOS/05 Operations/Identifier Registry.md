---
title: Identifier Registry
document_type: Navigation Document
version: 1.10
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

## Version 1.10

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
INV-0001 (Jesus & Daoism), INV-0002 (Phantom Traffic Jams), INV-0003 (Wu Wei), INV-0004 (Metformin Discontinuation & T2D Remission), INV-0005 (Chronic Stress Interventions), INV-0006 (Wellness Intervention Adherence & Maintenance). — **Next: INV-0007.**

## CLM — Claims
CLM-0001, CLM-0002 (INV-0001); CLM-0003, CLM-0004 (INV-0002); CLM-0005, CLM-0006 (INV-0003); CLM-0007 … CLM-0012 (INV-0004); CLM-0013 … CLM-0018 (INV-0005); CLM-0019 … CLM-0026 (INV-0006). — **Next: CLM-0027.**

## SRC — Sources
SRC-0001 (Gospels), SRC-0002 (Daoist Corpus), SRC-0003 (Sugiyama 2008), SRC-0004 (Jamiton Modeling), SRC-0005 (Slingerland), SRC-0006 (DiRECT Trial Programme), SRC-0007 (Taylor Twin-Cycle Mechanism), SRC-0008 (Virta Health Trial), SRC-0009 (STAMPEDE Surgery Trial), SRC-0010 (ADA/EASD Remission Consensus), SRC-0011 (Diet & Exercise Literature), SRC-0012 (Khoury 2015 MBSR Meta-Analysis), SRC-0013 (de Vibe 2017 Campbell MBSR Review), SRC-0014 (Goyal 2014 JAMA Meditation Meta-Analysis), SRC-0015 (Goessl 2017 HRV Biofeedback Meta-Analysis), SRC-0016 (Cochrane Individual-Level Occupational Stress — Tamminga 2023), SRC-0017 (Cochrane Organizational-Level Occupational Stress), SRC-0018 (CBT-I Long-Term Meta-Analysis), SRC-0019 (Holt-Lunstad 2010 Social Relationships & Mortality), SRC-0020 (Physical Activity, Cortisol & Stress Literature), SRC-0021 (Nature Exposure & Stress Literature), SRC-0022 (Coping Theory & Problem-Focused Coping Literature), SRC-0023 (McEwen Allostatic Load Literature), SRC-0024 (Kwasnicka 2016 Maintenance Theories), SRC-0025 (Rhodes & de Bruijn 2013 Intention-Behaviour Gap), SRC-0026 (Michie 2009 Effective Techniques Meta-Regression), SRC-0027 (Harkin 2016 Progress Monitoring), SRC-0028 (Gollwitzer & Sheeran 2006 Implementation Intentions), SRC-0029 (Lally 2010 Habit Formation), SRC-0030 (Teixeira 2012 Exercise & SDT), SRC-0031 (Mantzari 2015 Financial Incentives), SRC-0032 (Eysenbach 2005 Law of Attrition), SRC-0033 (Ashford 2010 Self-Efficacy & Physical Activity), SRC-0034 (Baumel 2019 Objective Engagement with Mental Health Apps). — **Next: SRC-0035.**

## ENT — Entities
ENT-0001 (Wu Wei), ENT-0002 (Ziran), ENT-0003 (Allostatic Load), ENT-0004 (Intention-Behaviour Gap). — **Next: ENT-0005.**

## FND — Findings
FND-0001 (Resonant Ethic, Opposed Ultimates), FND-0002 (Jams as Emergent Instability), FND-0003 (Wu Wei as Non-Forcing Action), FND-0004 (Evidence-Based Pathways to T2D Remission & Safe De-prescribing), FND-0005 (Durable Chronic-Stress Relief Requires Stressor Reduction Plus Response Regulation), FND-0006 (What Best Supports Sustained Wellness Behaviour — best-evidenced levers of maintenance; renamed from the longer "…Built by…" title 2026-07-11). — **Next: FND-0007.**

---

# 3. Unnumbered Meta-Documents

These are authoritative navigational/architectural documents that intentionally carry **no** `TYPE-NNNN` identifier (precedent: indexes and status records):

- KOS Architecture Manifest; Kernel Index; KOS Dependency Map; Kernel Status.
- Standards Index; Standards Dependency Map; Standards Status; Standards Architecture Retrospective.
- Roles Index.
- Per-run review/assessment reports: Pressure Test Report – RQ-0001; Second-Run Friction Assessment – RQ-0002; Third-Run Assessment – RQ-0003; Critical Review – RQ-0004 (ROLE-0004); Fourth-Run Assessment – RQ-0004 (coordinator); Critical Review – RQ-0005; Critical Review – RQ-0006 (ROLE-0004); Sixth-Run Assessment – RQ-0006 (coordinator).
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

---

# End Identifier Registry
