# Classification fixture — "Map of Content"

The CONTENT of this file is irrelevant: classification in validate.py is by
filename only (`validator_rules.yaml` `filename_contains`). This fixture exists
so test_classification.py can prove, from a real on-disk filename, that a file
named with the "Map of Content" fragment is classified as an infrastructure
document rather than falling through to `defaults`.
