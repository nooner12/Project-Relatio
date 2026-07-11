from pathlib import Path
import re

# Whole-string identifier (e.g. "KOS-0004"). Kept for backward compatibility.
ID_PATTERN = re.compile(r"^[A-Z]{2,5}-\d{4}$")

# Leading identifier, matched at the start of a filename or `title:` string.
# Handles both TYPE-NNNN (KOS-0004, CLM-0007) and ADR-CAT-NNNN (ADR-GOV-0001).
# Mirrors the convention used by graph_integrity.py.
IDENTIFIER_RE = re.compile(r"^(ADR-[A-Z]{2,5}-\d{4}|[A-Z]{2,5}-\d{4})")

WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)")


def extract_identifier(text):
    """Return the leading TYPE-NNNN / ADR-CAT-NNNN identifier of a string, or None."""
    if not isinstance(text, str):
        return None
    match = IDENTIFIER_RE.match(text.strip())
    return match.group(0) if match else None

def find_vault_root(start: Path) -> Path:

    current = start.resolve()

    while current != current.parent:

        candidate = current / "Project Relatio"

        if candidate.exists():
            return candidate

        current = current.parent

    raise FileNotFoundError("Project Relatio not found.")

def markdown_files(vault):

    yield from vault.rglob("*.md")

def parse_frontmatter(text):

    if not text.startswith("---\n"):
        return None, text

    end = text.find("\n---", 4)

    if end == -1:
        return None, text

    return text[4:end], text[end + 4:]

def wikilinks(text):

    return WIKILINK_PATTERN.findall(text)

def note_name(path):

    return path.stem