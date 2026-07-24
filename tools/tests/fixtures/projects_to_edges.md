---
title: ENT-9205 - Fixture Community (projects_to edge cases)
document_type: Entity Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-24
category:
  - Knowledge Base
  - Entity
  - Community
rendering_class: community
attestation_claims:
  - CLM-9101
attestation_window: "7th c. CE (fixture)"
attestation_uncertainty: moderate
relationships:
  - type: projects_to
    target: ENT-9100          # VALID — community -> tradition, bare entry
  - type: projects_to
    target: ENT-9101
    qualifier: documented     # FORBIDDEN — projects_to takes no qualifier
  - type: projects_to
    target: ENT-9102
    confidence:               # FORBIDDEN — a graded projection is an evidential edge
      - component: overall
        level: 3
        label: Moderate
  - type: projects_to
    target: ENT-9999          # DANGLING — resolves to nothing
  - type: projects_to
    target: ENT-9202          # WRONG DIRECTION — target is community, not tradition
---

# ENT-9205

Five `projects_to` entries, one valid and four defective in the four distinct
ways STD-0004 §7.3 names: a qualifier (forbidden), a confidence component
(forbidden — this is the one that would silently turn a rendering instruction
into a graded historical claim), a dangling target (machine-traversable means
resolvable), and a non-tradition target (projection re-anchors UP to the
tradition layer, never sideways).
