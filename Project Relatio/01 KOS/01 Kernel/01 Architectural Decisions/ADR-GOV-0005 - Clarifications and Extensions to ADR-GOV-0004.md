---
title: ADR-GOV-0005 - Clarifications and Extensions to ADR-GOV-0004
document_type: Architecture Decision Record
version: 1.0
status: Adopted
operational_status: Active
created: 2026-07-20
decision_status: Accepted
decision_date: 2026-07-20
category:
  - Knowledge Operating System
  - Architecture Decision
parent_documents:
  - CON-0003 Project Relatio Governance & Stewardship Framework
related_documents:
  - Governance Backlog
  - ADR-GOV-0004 - Governance Hygiene Closure Decision Tiering and Reference Integrity
tags:
  - ProjectRelatio
  - ADR
  - Governance
  - Clarification
  - PathIntegrity
---

## §1 — D1(d) clarified: closure state lives in banner + history, not frontmatter

Ratified as authored-intent: closure state is carried by (i) the dated closure banner and (ii) the revision-history row. STD-0005's status vocabulary is UNCHANGED and defines no "closed" value; INV-0010 (maturity deliberately held at Draft) remains the model instance. D1(d)'s phrase "frontmatter status fields updated to the closed state" is void where the field vocabulary defines no such state — the 2026-07-20 execution's reading is confirmed correct. A frontmatter-queryable closure field is DEFERRED to second use (trigger: any tooling or query that needs closure state machine-readable).

## §2 — Evidence-provenance rule for acceptance criteria

An acceptance criterion may be satisfied by evidence outside the record if and only if the tick carries an in-record citation naming the external document and its specific version. Registry entries qualify.

Operative one-line rule:

> Out-of-record evidence may satisfy an acceptance criterion only via an in-record citation to the evidencing document and version.

Application note: ROLE-0001 structural validation of INV-0011/0012/0013 is evidenced at Identifier Registry v1.17/v1.18/v1.20; criterion #7 on those records may be ticked citing those versions. This rule does NOT relax substantive criteria: INV-0011 criterion #2 (three sub-questions per doctrine claim) is research structure, not formality, and remains open until the work exists.

## §3 — D3 home: deferred to second use

Per the recorded defer-to-second-use pattern (GB-2026-026): D3 receives no document home now. ADR-GOV-0004 §2 D3, as extended by §4 below, is the operative text. Re-open trigger: a second session-procedure rule requiring a home creates OPS-0004 and both rules move there together.

## §4 — D3 extended: CLAUDE.md currency check

Session close-out includes a CLAUDE.md currency check: scan for assertions superseded by the session or by prior sessions. CLAUDE.md sits outside the KOS lifecycle — corrections are direct edits with a commit message citing D3, no version machinery. Tier weight: CLAUDE.md corrections are tier-1 (fix in-session) under this extension; the 2026-07-20 report's judgment that they were heavier is superseded by this explicit authorization.

## §5 — Path-length constraint (standing infrastructure record)

(a) HAZARD RECORD: Vault files whose absolute Windows paths exceed MAX_PATH (260 chars) are invisible to naive scanners. Four such files existed as of 2026-07-20; one carried drift. ANY tool that enumerates the vault MUST use extended-length path handling (\?\ prefix or equivalent); a scan without it is non-conforming and its results are invalid regardless of what it reports.

(b) PREVENTIVE RULE: Vault root sits at ~75 absolute characters (`C:\Users\Uncle Brian\Desktop\Research OS Obsidian\Research OS\Project Relatio\`), leaving ~185 of headroom under the 260 ceiling. Budget: relative path from vault root ≤ 180 characters. (buffer against drive-prefix + sync-client overhead below the 260 ceiling). Existing violators are grandfathered — renames touch graph references and are owner-decision only.

(c) PLACEMENT: operative rule text for (a) and (b) is to be amended into the document owning file-naming/path conventions, per the D5/D6 locate-or-report procedure. If no document owns it, report the gap with candidates — do not create.