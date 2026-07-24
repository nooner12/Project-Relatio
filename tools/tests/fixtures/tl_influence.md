---
title: ENT-9109 - Fixture Tradition (influence-only; must render as a ROOT)
document_type: Entity Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-24
category:
  - Knowledge Base
  - Entity
  - Tradition
rendering_class: tradition
tradition_type: founded
dating_claims:
  - CLM-9101
display_range: "8th c. CE (fixture)"
range_start_year: 700
range_end_year: 800
range_uncertainty: moderate
relationships:
  - type: influenced_by
    target: ENT-9108
    qualifier: documented
    warrant:
      - CLM-9101
    not_descent: CLM-9101
  - type: influenced_by
    target: ENT-9100
    qualifier: contested
    warrant:
      - CLM-9102
    not_descent: CLM-9102
---

# ENT-9109

The Islam-shaped fixture: a tradition whose ONLY edges are `influenced_by` and
which carries NO `branches_from`. Under ADR-GOV-0012 D7 neither influence edge
renders on the default timeline, so this node must render as a **ROOT** — an
unconnected node is an honest rendering of "no descent," and an influence
connector that could make it read as a branch is the failure the filter prevents.

It also proves the filter is edge-TYPE-based, not target-based: one of its
influence targets (ENT-9100) is itself an on-axis tradition, so a filter keyed on
"is the target renderable" rather than "is this a descent edge" would leak.
