#!/usr/bin/env python3

from pathlib import Path
import sys
import yaml

from common import (
    find_vault_root,
    markdown_files,
    parse_frontmatter,
    wikilinks,
    note_name,
    ID_PATTERN,
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

        if rule["requires_id"]:

            identifier = meta.get("id")

            if identifier is None:

                errors.append(f"Missing id: {file}")

            else:

                if not ID_PATTERN.match(identifier):

                    errors.append(
                        f"Invalid id: {identifier}"
                    )

                if identifier in ids:

                    errors.append(
                        f"Duplicate id:\n"
                        f"  {identifier}\n"
                        f"  {ids[identifier]}\n"
                        f"  {file}"
                    )

                ids[identifier] = file

    stem = note_name(file)

    if stem in names:

        warnings.append(f"Duplicate filename: {stem}")

    else:

        names[stem] = file

# ----------------------------
# Second pass
# ----------------------------

known = set(names.keys())

for file in files:

    text = file.read_text(encoding="utf-8")

    for link in wikilinks(text):

        if link not in known:

            warnings.append(
                f"Broken link: [[{link}]] in {file.name}"
            )

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