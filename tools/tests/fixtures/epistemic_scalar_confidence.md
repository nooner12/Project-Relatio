---
title: FIXTURE - scalar confidence, missing reliance tier
document_type: Claim Record
version: 0.1
status: Draft
operational_status: Active
created: 2026-07-20
confidence: 3
---

# Fixture

Two deliberate defects: `confidence` as a scalar (STD-0002 s.11: always a
list, never a scalar) and `reliance_tier` absent while `confidence` is
present -- a half-authored record, which is new-authoring breakage rather
than migration debt.
