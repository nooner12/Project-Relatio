---
title: ENT-9206 - Fixture Tradition (influenced_by edge cases)
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
display_range: "7th c. CE (fixture)"
relationships:
  - type: influenced_by
    target: ENT-9202          # VALID — ENT->ENT, qualifier, resolvable warrant + not_descent
    qualifier: documented
    warrant:
      - CLM-9101
    not_descent: CLM-9101
  - type: influenced_by
    target: ENT-9203          # VALID — the second qualifier value
    qualifier: contested
    warrant:
      - CLM-9102
    not_descent: CLM-9102
  - type: influenced_by
    target: ENT-9204          # INVALID QUALIFIER — not in documented/contested
    qualifier: thematic
    warrant:
      - CLM-9101
    not_descent: CLM-9101
  - type: influenced_by
    target: ENT-9205          # MISSING QUALIFIER
    warrant:
      - CLM-9101
    not_descent: CLM-9101
  - type: influenced_by
    target: ENT-9100          # MISSING WARRANT
    qualifier: documented
    not_descent: CLM-9101
  - type: influenced_by
    target: ENT-9101          # DANGLING WARRANT
    qualifier: documented
    warrant:
      - CLM-9999
    not_descent: CLM-9101
  - type: influenced_by
    target: ENT-9102          # MISSING NOT_DESCENT — the constitutive failure
    qualifier: documented
    warrant:
      - CLM-9101
  - type: influenced_by
    target: CLM-9101          # NON-ENT TARGET
    qualifier: documented
    warrant:
      - CLM-9101
    not_descent: CLM-9101
---

# ENT-9206

Eight `influenced_by` entries: two valid (one per qualifier value) and six
defective in the six distinct ways STD-0004 §7.3 names. The MISSING NOT_DESCENT
case is the load-bearing one — ADR-GOV-0012 D6 makes the not-descent
determination constitutive, so an edge without one must be rejected by the tool
rather than left to a reviewer to notice. Without that check `influenced_by` is
the soft option that empties the edge-restraint rule of force.
