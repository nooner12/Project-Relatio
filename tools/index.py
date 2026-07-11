#!/usr/bin/env python3

from pathlib import Path
import json
import yaml
from datetime import datetime

from common import (
    find_vault_root,
    markdown_files,
    parse_frontmatter,
    wikilinks,
)

ROOT = Path(__file__).parent
OUTPUT = ROOT / "output"
OUTPUT.mkdir(exist_ok=True)

vault = find_vault_root(ROOT)

records = []

for file in markdown_files(vault):

    text = file.read_text(encoding="utf-8")

    frontmatter, body = parse_frontmatter(text)

    metadata = {}

    if frontmatter:

        try:
            metadata = yaml.safe_load(frontmatter) or {}

        except Exception:
            metadata = {}

    records.append(
        {
            "path": str(file.relative_to(vault)),
            "name": file.stem,
            "id": metadata.get("id"),
            "title": metadata.get("title"),
            "links": sorted(set(wikilinks(text))),
        }
    )

records.sort(key=lambda r: r["path"])

output = {
    "generated": datetime.utcnow().isoformat() + "Z",
    "count": len(records),
    "files": records,
}

with open(
    OUTPUT / "repository_index.json",
    "w",
    encoding="utf-8",
) as f:

    json.dump(output, f, indent=2)

print(f"Indexed {len(records)} markdown files.")
print("Output:")
print(OUTPUT / "repository_index.json")