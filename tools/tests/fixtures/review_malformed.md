---
title: CLM-9002 - Review Fields Malformed Fixture
document_type: Claim Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-07-21
confidence:
  - component: overall
    level: 2
    label: Low
reliance_tier: R0
review_cycle: 0
review_date: 2027-01-20
last_reviewed: "2026-07-40"
---

# CLM-9002

Fixture body: review_cycle non-positive; last_reviewed not a real date;
review_date fails the arithmetic (checked only when the other two are well-formed,
so here the bad cycle and bad last_reviewed are what surface).
