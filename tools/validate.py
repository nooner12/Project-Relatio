#!/usr/bin/env python3

from pathlib import Path
import sys
import yaml

from common import (
    find_vault_root,
    markdown_files,
    parse_frontmatter,
    note_name,
    extract_identifier,
    read_text,
    version_elements,
    parse_version,
)

ROOT = Path(__file__).parent

RULES = yaml.safe_load(
    (ROOT / "validator_rules.yaml").read_text(encoding="utf-8")
)

errors = []
warnings = []

ids = {}
names = {}

vault = find_vault_root(ROOT)

files = list(markdown_files(vault))


def classify(filename):

    for rule in RULES["document_types"].values():

        for prefix in rule.get("filename_prefix", []):

            if filename.startswith(prefix):
                return rule

        for fragment in rule.get("filename_contains", []):

            if fragment in filename:
                return rule

    return RULES["defaults"]


# ----------------------------
# First pass
# ----------------------------

for file in files:

    rule = classify(file.name)

    text = read_text(file)

    if not text.strip():
        errors.append(f"Empty file: {file}")
        continue

    frontmatter, body = parse_frontmatter(text)

    if rule["requires_yaml"]:

        if frontmatter is None:
            errors.append(f"Missing YAML: {file}")
            continue

        try:
            meta = yaml.safe_load(frontmatter)

        except Exception as ex:

            errors.append(
                f"Invalid YAML: {file}\n{ex}"
            )
            continue

        if not isinstance(meta, dict):

            errors.append(f"Invalid metadata object: {file}")
            continue

        if rule.get("requires_identifier"):

            # Per STD-0001/STD-0002 the identifier is embedded in the filename and
            # the `title:` field (e.g. "KOS-0004 …"), not a separate `id:` field.
            # Check: filename carries a valid identifier, title carries one, they
            # agree, and the identifier is unique across the vault.

            filename_id = extract_identifier(file.stem)
            title = meta.get("title")
            title_id = extract_identifier(title)

            if filename_id is None:

                errors.append(f"Filename has no valid identifier: {file.name}")

            elif title is None:

                errors.append(
                    f"Missing title (identifier lives in the title): {file.name}"
                )

            elif title_id is None:

                errors.append(
                    f"Title has no valid identifier: {file.name}\n"
                    f"  title: {title!r}"
                )

            elif title_id != filename_id:

                errors.append(
                    f"Identifier mismatch (filename vs title): {file.name}\n"
                    f"  filename: {filename_id}\n"
                    f"  title:    {title_id}"
                )

            if filename_id is not None:

                if filename_id in ids:

                    errors.append(
                        f"Duplicate identifier:\n"
                        f"  {filename_id}\n"
                        f"  {ids[filename_id]}\n"
                        f"  {file}"
                    )

                else:

                    ids[filename_id] = file

    stem = note_name(file)

    if stem in names:

        warnings.append(f"Duplicate filename: {stem}")

    else:

        names[stem] = file

# ----------------------------
# Version coherence pass (GB-2026-035)
#
# Checks that a document's `version:` frontmatter, its `## Version` body heading,
# and the newest row of its own `# Revision History` table agree. This is the
# durable countermeasure for the drift class GB-2026-028 recorded: the
# 2026-07-20 sweep found 39 instances, and the validator passed clean through
# every one of them because nothing compared the three.
#
# Scope: **self-scoping, deliberately NOT gated by validator_rules.yaml.** The
# check runs wherever at least two of the three elements exist, and is silent
# where fewer do (a document with only a `version:` field has nothing to
# disagree with). Gating by document_types would have been wrong: 17 versioned
# files -- including the Architecture Baseline and every Critical Review report
# -- match neither the identified_documents prefixes nor the
# infrastructure_documents fragments, and GB-2026-028 records that the drift
# class had already reached two review reports.
#
# Severity: **error** (owner ruling, 2026-07-21). Built at warning level per the
# GB-2026-035 build notes -- the reasoning being that the content of a drifted
# record is not wrong, only its summary field is stale. The owner promoted it on
# three grounds: a stale version field is a record lying about itself, which is
# the defect ADR-GOV-0004 §4's trust-without-re-derivation principle exists to
# prevent; the class produced 40 known instances, one of which manual sweeping
# structurally could not see; and a zero-warning baseline erodes, whereas an
# error cannot be deferred without a deliberate act.
#
# Run as its own pass rather than inside the first loop because that loop
# short-circuits on empty/invalid-YAML files, and because the infrastructure
# documents that drifted most (Identifier Registry, Governance Backlog) are
# `requires_yaml: false` and so never have their frontmatter parsed above.
# ----------------------------

for file in files:

    text = read_text(file)

    if not text.strip():
        continue

    frontmatter, body = parse_frontmatter(text)

    found = version_elements(
        body if frontmatter is not None else text,
        frontmatter,
    )

    present = {
        label: found[label]
        for label in ("frontmatter", "heading", "history")
        if found[label] is not None
    }

    if len(present) < 2:
        continue

    distinct = {parse_version(v) for v in present.values()}

    if len(distinct) > 1:

        detail = ", ".join(
            f"{label}={value}" for label, value in sorted(present.items())
        )

        # The history table is authoritative when present (2026-07-20 sweep
        # convention): its rows are the accurate record; the summary fields lag.
        if found["history"] is not None:
            fix = f"authoritative = newest history row {found['history']}"
        else:
            fix = "no history table; reconcile against the intended version"

        errors.append(
            f"Version incoherence: {file.name}\n"
            f"  {detail}\n"
            f"  {fix}"
        )

# ----------------------------
# NOTE: The adopted STD-0001/STD-0002 convention does not use [[wikilinks]] for the
# knowledge graph — relationships live in `related_documents`/`parent_documents` and
# are validated by graph_integrity.py. The old broken-[[wikilink]] pass was removed
# here (GB-2026-016): it did not match the convention and false-flagged prose that
# merely mentioned "[[wikilinks]]".
# ----------------------------

print()

print("=" * 60)
print("PROJECT RELATIO VALIDATION REPORT")
print("=" * 60)

print()

print(f"Files scanned : {len(files)}")
print(f"Errors        : {len(errors)}")
print(f"Warnings      : {len(warnings)}")

print()

if errors:

    print("ERRORS")
    print("-" * 60)

    for e in errors:
        print(e)

    print()

if warnings:

    print("WARNINGS")
    print("-" * 60)

    for w in warnings:
        print(w)

print()

if errors:

    print("STATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS")
sys.exit(0)