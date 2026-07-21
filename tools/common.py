from pathlib import Path
import os
import sys
import re


def _extended(path) -> str:
    """Return an OS path safe for Windows MAX_PATH (260) limits.

    Deep vault folders plus long object titles can push a file's absolute path
    past 260 chars, which makes the default Windows file APIs raise
    FileNotFoundError. Prefixing an absolute path with `\\\\?\\` opts into the
    extended-length path form. No-op on non-Windows.
    """
    p = os.path.abspath(str(path))
    if sys.platform == "win32" and not p.startswith("\\\\?\\"):
        p = "\\\\?\\" + p
    return p


def read_text(path, encoding="utf-8") -> str:
    """Long-path-safe replacement for Path.read_text()."""
    with open(_extended(path), "r", encoding=encoding) as f:
        return f.read()


def write_text(path, data, encoding="utf-8") -> None:
    """Long-path-safe replacement for Path.write_text()."""
    with open(_extended(path), "w", encoding=encoding) as f:
        f.write(data)

# Whole-string identifier (e.g. "KOS-0004"). Kept for backward compatibility.
ID_PATTERN = re.compile(r"^[A-Z]{2,5}-\d{4}$")

# Leading identifier, matched at the start of a filename or `title:` string.
# Handles both TYPE-NNNN (KOS-0004, CLM-0007) and ADR-CAT-NNNN (ADR-GOV-0001).
# Mirrors the convention used by graph_integrity.py.
IDENTIFIER_RE = re.compile(r"^(ADR-[A-Z]{2,5}-\d{4}|[A-Z]{2,5}-\d{4})")

WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)")

# ----------------------------------------------------------------------------
# Version coherence (GB-2026-035)
#
# A document can carry its version in up to three places: the `version:`
# frontmatter field, a `## Version N.N` body heading, and the newest row of its
# own `# Revision History` table. When two of these disagree the record is
# internally inconsistent -- the drift class that produced 39 instances in the
# 2026-07-20 sweep, invisible to the validator because nothing compared them.
# ----------------------------------------------------------------------------

VERSION_HEADING_RE = re.compile(r"^##\s*Version\s+([0-9]+(?:\.[0-9]+)*)\s*$", re.M)

# Tolerates both "# Revision History" and numbered "# 22. Revision History".
REVISION_HISTORY_RE = re.compile(r"^#+\s*(?:\d+\.\s*)?Revision History\s*$", re.M | re.I)

# A history row's leading cell, e.g. "|1.27|2026-07-20|Active|...". Tolerates a
# leading "v" and any dotted depth.
VERSION_ROW_RE = re.compile(r"^\|\s*v?([0-9]+(?:\.[0-9]+)+)\s*\|", re.M)

# The `version:` frontmatter line, read from the RAW frontmatter text.
#
# This must not go through yaml.safe_load: an unquoted `version: 1.10` is valid
# YAML for the *float* 1.1, which silently drops the trailing zero and makes a
# coherent 1.10 document look like 1.1 against its own 1.10 history row. Reading
# the literal characters avoids inventing that drift. (Caught by the fixture
# tests, which is why they exist.)
FRONTMATTER_VERSION_RE = re.compile(r"^version:\s*(.+?)\s*$", re.M)


def parse_version(text):
    """Return a version string as a comparable tuple of ints, or None.

    Tuple comparison is required, not float: as floats 1.9 > 1.27, but as
    versions 1.27 > 1.9. The Identifier Registry is the live proof -- it has
    reached 1.23, and a float-max over its rows returns 1.9.
    """
    if text is None:
        return None
    s = str(text).strip().lstrip("vV")
    if not s:
        return None
    parts = s.split(".")
    if not all(p.isdigit() for p in parts):
        return None
    return tuple(int(p) for p in parts)


def version_elements(text, frontmatter=None):
    """Extract the (frontmatter, heading, newest history row) version strings.

    `text` is the document body; `frontmatter` is the raw frontmatter block as
    text (not a parsed dict -- see FRONTMATTER_VERSION_RE for why).

    Returns a dict with keys 'frontmatter', 'heading', 'history' mapping to the
    raw version strings found (or None), plus 'rows' listing every history row
    version in document order.

    The newest history row is chosen by **parse-and-max, never by position**
    (GB-2026-029): the Identifier Registry's rows are not in numeric order, so
    the last line of the table is not the latest version.
    """
    found = {"frontmatter": None, "heading": None, "history": None, "rows": []}

    if frontmatter:
        line = FRONTMATTER_VERSION_RE.search(frontmatter)
        if line:
            value = line.group(1).strip().strip("'\"")
            if value:
                found["frontmatter"] = value

    heading = VERSION_HEADING_RE.search(text)
    if heading:
        found["heading"] = heading.group(1)

    history = REVISION_HISTORY_RE.search(text)
    if history:
        rows = VERSION_ROW_RE.findall(text[history.end():])
        found["rows"] = rows
        parsed = [r for r in rows if parse_version(r) is not None]
        if parsed:
            found["history"] = max(parsed, key=parse_version)

    return found


# ----------------------------------------------------------------------------
# Epistemic-field shape check (STD-0008 / STD-0002 s.11 v1.8)
#
# Claim Records and Finding Records carry the epistemic-axis fields:
# `confidence` (always a list; each component pairs an integer level 1-5 with
# the matching KOS-0003 s.8 label) and `reliance_tier` (R0/R1/R2, the
# ADR-GOV-0006 vocabulary). This helper checks *shape* only -- whether a grade
# is correct is epistemic review (ROLE-0004), not validation.
# ----------------------------------------------------------------------------

EPISTEMIC_LEVEL_LABELS = {
    5: "Very High",
    4: "High",
    3: "Moderate",
    2: "Low",
    1: "Very Low",
}

RELIANCE_TIERS = ("R0", "R1", "R2")


def epistemic_field_problems(meta):
    """Shape-check the STD-0008 epistemic fields of a parsed frontmatter dict.

    Returns a list of problem strings; empty means well-formed. Level 0
    (Unsupported) is deliberately not a valid field value: KOS-0003 s.12
    excludes Unsupported conclusions from the permanent Knowledge Base, so the
    field range is 1-5 (STD-0008 s.5.1).
    """
    problems = []
    confidence = meta.get("confidence")
    tier = meta.get("reliance_tier")

    if confidence is None:
        problems.append("missing `confidence` (STD-0002 s.11: required list)")
    elif not isinstance(confidence, list) or not confidence:
        problems.append(
            "`confidence` must be a non-empty list -- a single grade is a "
            "one-item list with component `overall`, never a scalar"
        )
    else:
        for i, comp in enumerate(confidence):
            if not isinstance(comp, dict):
                problems.append(
                    f"confidence[{i}] must be a mapping with component/level/label"
                )
                continue
            name = comp.get("component")
            level = comp.get("level")
            label = comp.get("label")
            if not isinstance(name, str) or not name.strip():
                problems.append(
                    f"confidence[{i}].component must be a non-empty string"
                )
            if isinstance(level, bool) or not isinstance(level, int) \
                    or not 1 <= level <= 5:
                problems.append(
                    f"confidence[{i}].level must be an integer 1-5 (got {level!r})"
                )
            elif label != EPISTEMIC_LEVEL_LABELS[level]:
                problems.append(
                    f"confidence[{i}].label must be "
                    f"{EPISTEMIC_LEVEL_LABELS[level]!r} for level {level} "
                    f"(got {label!r})"
                )

    if tier is None:
        problems.append(
            "missing `reliance_tier` (STD-0002 s.11: required, R0/R1/R2)"
        )
    elif tier not in RELIANCE_TIERS:
        problems.append(
            f"`reliance_tier` must be one of R0/R1/R2 (got {tier!r})"
        )

    return problems


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