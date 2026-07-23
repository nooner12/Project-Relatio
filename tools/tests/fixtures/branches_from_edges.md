---
title: ENT-9010 - Fixture Tradition (branches_from edge cases)
document_type: Entity Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-21
category:
  - Knowledge Base
  - Entity
  - Tradition
tradition_type: syncretic
dating_claims:
  - CLM-9001
display_range: "19th c. CE"
relationships:
  - type: branches_from
    target: ENT-9000
    qualifier: schism
  - type: branches_from
    target: ENT-9006
    qualifier: bogus-qualifier
  - type: branches_from
    target: ENT-9007
  - type: branches_from
    target: CLM-9099
    qualifier: reform
  - type: branches_from
    target: ENT-9008
    qualifier: continuation
  - type: derived_from
    target: SRC-9001
---

# ENT-9010

Edge cases for the branches_from integrity check:
- ENT-9000 / schism — VALID.
- ENT-9006 / bogus-qualifier — invalid qualifier.
- ENT-9007 / (none) — missing required qualifier.
- CLM-9099 / reform — target is not an ENT.
- ENT-9008 / continuation — VALID (ADR-GOV-0010 D1; the sixth qualifier).
