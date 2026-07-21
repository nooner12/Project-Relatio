---
title: CLM-9004 - bounded_by Extraction Fixture
document_type: Claim Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-07-21
confidence:
  - component: placement
    level: 3
    label: Moderate
    bounded_by: [SRC-0129]
  - component: criteria_mechanics
    level: 2
    label: Low
    bounded_by: [SRC-9999, CLM-9998]
reliance_tier: R0
review_cycle: 6
review_date: 2027-01-21
last_reviewed: 2026-07-21
---

# CLM-9004

Fixture body: three bounded_by entries across two components. SRC-0129 exists in
the vault; SRC-9999 and CLM-9998 do not (synthetic dangling targets). Not a vault
object -- it lives outside the content dirs.
