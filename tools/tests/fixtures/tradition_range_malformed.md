---
title: ENT-9002 - Fixture Tradition (malformed positioning bounds)
document_type: Entity Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-22
category:
  - Knowledge Base
  - Entity
  - Tradition
tradition_type: founded
dating_claims:
  - CLM-9001
display_range: "3rd c. CE"
range_start_year: 200
range_end_year: "1200s"
range_uncertainty: severe
relationships:
  - type: derived_from
    target: SRC-9001
---

# ENT-9002

Malformed positioning-bounds fixture (STD-0002 §11 v1.11): `range_end_year` is
neither an integer nor the literal `present`, and `range_uncertainty` is outside
the controlled vocabulary. The shape check must flag BOTH.
