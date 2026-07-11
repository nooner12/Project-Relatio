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

    text = file.read_text(encoding="utf-8")

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