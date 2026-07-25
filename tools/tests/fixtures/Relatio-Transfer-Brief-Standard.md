# Classification fixture — "Transfer-Brief"

The CONTENT of this file is irrelevant: classification in validate.py is by
filename only (`validator_rules.yaml` `filename_contains`). This fixture carries
the EXACT filename of the owner-placed Transfer Brief Standard at the repo root,
so test_classification.py can prove the "Transfer-Brief" fragment (hyphenated —
a space would silently fail the literal substring match) classifies it as an
infrastructure document rather than falling through to `defaults`.
