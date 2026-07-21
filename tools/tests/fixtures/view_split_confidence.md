---
title: CLM-9002 - Split Confidence And Past Due
document_type: Claim Record
version: 0.3
status: Draft
operational_status: Active
created: 2026-07-21
parent_documents:
  - INV-9001 Fixture Investigation Root
relationships:
  - type: part_of
    target: INV-9001
  - type: derived_from
    target: SRC-9001
confidence:
  - component: strand_a
    level: 3
    label: Moderate
  - component: strand_b
    level: 2
    label: Low
  - component: strand_c
    level: 4
    label: High
reliance_tier: R0
reliance_note: "unassessed floor; predates verification pass."
review_cycle: 6
review_date: 2020-01-01
last_reviewed: 2019-07-01
---

# CLM-9002

Split-confidence fixture claim with a deliberately past-due review_date.
