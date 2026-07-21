from pathlib import Path
import datetime
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


# ----------------------------------------------------------------------------
# Review-field shape check (STD-0009 s.8 / STD-0002 s.11 v1.9)
#
# Claim Records and Finding Records carry the review-cycle fields: `review_cycle`
# (positive integer months), `last_reviewed` (YYYY-MM-DD, the most recent review
# act or initialization), and `review_date` (YYYY-MM-DD, = last_reviewed +
# review_cycle months). This helper checks *shape* only -- whether a cadence is
# the *right* one for the record's epistemic state is a review-act question
# (STD-0009 s.7), not validation. Enforced at error level from initialization
# onward (ADR-GOV-0008 Task 5 makes every record conformant same-session).
# ----------------------------------------------------------------------------

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _parse_date(value):
    """Return (y, m, d) for a YYYY-MM-DD date, or None if malformed.

    Accepts both a `datetime.date` (PyYAML parses an unquoted `2027-04-20`
    into one, exactly as it does the `created:` field) and a YYYY-MM-DD string
    (a quoted value, or a malformed one PyYAML left as text).
    """
    if isinstance(value, datetime.datetime):
        value = value.date()
    if isinstance(value, datetime.date):
        return (value.year, value.month, value.day)
    if not isinstance(value, str) or not _DATE_RE.match(value):
        return None
    y, m, d = (int(p) for p in value.split("-"))
    if not (1 <= m <= 12 and 1 <= d <= 31):
        return None
    return (y, m, d)


def add_months(date_tuple, months):
    """Add whole calendar months to a (y, m, d) tuple, clamping the day."""
    y, m, d = date_tuple
    m += months
    y += (m - 1) // 12
    m = (m - 1) % 12 + 1
    leap = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    days_in = [31, 29 if leap else 28, 31, 30, 31, 30,
               31, 31, 30, 31, 30, 31][m - 1]
    return (y, m, min(d, days_in))


def confidence_bounded_by(meta):
    """Extract (component_name, target) pairs from confidence `bounded_by` lists.

    `bounded_by` is an optional list on a confidence component (STD-0002 §11
    v1.9 / STD-0009 §9) naming the objects that bound that component's grade.
    Each entry is a graph claim, so graph_integrity.py resolves it for dangling
    detection exactly like a relationships target. Shared here so the check and
    its test exercise the same extraction. Usually returns [] (optional field).
    """
    pairs = []
    for comp in (meta.get("confidence") or []):
        if isinstance(comp, dict):
            cname = str(comp.get("component", "?"))
            for b in (comp.get("bounded_by") or []):
                pairs.append((cname, str(b).strip()))
    return pairs


def review_field_problems(meta):
    """Shape-check the STD-0009 review fields of a parsed frontmatter dict.

    Returns a list of problem strings; empty means well-formed. Checks: all
    three fields present; dates are YYYY-MM-DD (STD-0002 s.10); `review_cycle`
    a positive integer; and review_date == last_reviewed + review_cycle months
    (the arithmetic STD-0009 s.8 defines -- a divergence means one of the three
    is stale, the review-field analogue of version incoherence).
    """
    problems = []
    cycle = meta.get("review_cycle")
    review_date = meta.get("review_date")
    last_reviewed = meta.get("last_reviewed")

    if cycle is None:
        problems.append("missing `review_cycle` (STD-0002 s.11: required, positive integer months)")
    elif isinstance(cycle, bool) or not isinstance(cycle, int) or cycle <= 0:
        problems.append(f"`review_cycle` must be a positive integer (months) (got {cycle!r})")

    ld = None
    if last_reviewed is None:
        problems.append("missing `last_reviewed` (STD-0002 s.11: required, YYYY-MM-DD)")
    else:
        ld = _parse_date(last_reviewed)
        if ld is None:
            problems.append(f"`last_reviewed` must be YYYY-MM-DD (got {last_reviewed!r})")

    rd = None
    if review_date is None:
        problems.append("missing `review_date` (STD-0002 s.11: required, YYYY-MM-DD)")
    else:
        rd = _parse_date(review_date)
        if rd is None:
            problems.append(f"`review_date` must be YYYY-MM-DD (got {review_date!r})")

    # Arithmetic coherence -- only when all three are individually well-formed.
    if ld is not None and rd is not None and isinstance(cycle, int) \
            and not isinstance(cycle, bool) and cycle > 0:
        expected = add_months(ld, cycle)
        if tuple(rd) != tuple(expected):
            exp_s = f"{expected[0]:04d}-{expected[1]:02d}-{expected[2]:02d}"
            problems.append(
                f"`review_date` must equal last_reviewed + review_cycle months "
                f"({last_reviewed} + {cycle}m = {exp_s}; got {review_date})"
            )

    return problems


# ----------------------------------------------------------------------------
# Tradition-entity fields + branches_from lineage edge (ADR-GOV-0009 / STD-0002
# v1.10 §11 / STD-0004 v1.2 §7.2).
#
# Two controlled vocabularies, defined once here so validate.py (field shape)
# and graph_integrity.py (edge integrity) read the same source of truth:
#   * TRADITION_TYPES — values for a tradition-class entity's `tradition_type`.
#   * BRANCH_QUALIFIERS — values for a `branches_from` edge's REQUIRED qualifier.
# ----------------------------------------------------------------------------

TRADITION_TYPES = ("founded", "emergent", "reform", "syncretic")

BRANCH_QUALIFIERS = (
    "schism", "reform", "syncretic-descent", "heterodox-offshoot", "disputed",
)

# The three co-required tradition-class fields (STD-0002 §11 v1.10).
TRADITION_FIELDS = ("tradition_type", "dating_claims", "display_range")


def tradition_entity_problems(meta):
    """Shape-check the tradition-class entity fields of a parsed frontmatter dict.

    Returns (problems, dating_claims): `problems` is a list of problem strings
    (empty means well-formed OR not a tradition entity); `dating_claims` is the
    list of raw dating_claims entries for the caller's dangling resolution.

    The three fields (`tradition_type`, `dating_claims`, `display_range`) are
    **co-required**: presence of ANY one requires ALL three (STD-0002 §11 v1.10 /
    ADR-GOV-0009 D3). A concept entity carries none of them and yields no
    problems. Shape only -- whether a date is *correct* is research, not
    validation; resolution of `dating_claims` targets is graph_integrity's job
    (they are graph claims, §12.1), so this returns them rather than resolving.
    """
    problems = []
    present = {f: meta.get(f) for f in TRADITION_FIELDS if meta.get(f) is not None}

    if not present:
        return problems, []  # concept entity (or non-entity): nothing to check

    # Co-presence: any one requires all three.
    missing = [f for f in TRADITION_FIELDS if meta.get(f) is None]
    if missing:
        problems.append(
            "tradition-class entity fields are co-required (STD-0002 §11 v1.10): "
            f"present {sorted(present)}, missing {missing}"
        )

    ttype = meta.get("tradition_type")
    if ttype is not None and ttype not in TRADITION_TYPES:
        problems.append(
            f"`tradition_type` must be one of {list(TRADITION_TYPES)} (got {ttype!r})"
        )

    dating = meta.get("dating_claims")
    dating_list = []
    if dating is not None:
        if not isinstance(dating, list) or not dating:
            problems.append("`dating_claims` must be a non-empty list of claim identifiers")
        else:
            for i, entry in enumerate(dating):
                ident = extract_identifier(str(entry).strip())
                if ident is None:
                    problems.append(
                        f"dating_claims[{i}] must be a claim identifier (got {entry!r})"
                    )
                else:
                    dating_list.append(str(entry).strip())

    disp = meta.get("display_range")
    if disp is not None and (not isinstance(disp, str) or not disp.strip()):
        problems.append("`display_range` must be a non-empty string (render-only)")

    return problems, dating_list


def branches_from_problems(source_id, edges, type_of):
    """Integrity-check a source object's branches_from edges (STD-0004 v1.2 §7.2).

    `source_id` is the edge source's identifier (or None if unidentified);
    `edges` is a list of (target, qualifier) pairs; `type_of` is a callable
    mapping a target identifier to its object type ("ENT", "CLM", …) or None if
    the target does not resolve. Returns a list of (target, reason) problems.

    Enforced (each an error): source is an ENT; target resolves to an ENT; the
    qualifier is present and drawn from BRANCH_QUALIFIERS. A dangling target is
    NOT reported here (Check 1's dangling pass owns that) -- an unresolved target
    yields type None and is skipped for the ENT-target check. The WARRANT rule
    (every edge backed by a graded claim) is deliberately NOT here: it is
    review-checked, not tool-checked (a warrant is a claim about lineage, not a
    structured pointer). Shared so graph_integrity.py and its test agree.
    """
    problems = []
    src_type = source_id.split("-")[0] if source_id else None
    for target, qual in edges:
        if src_type != "ENT":
            problems.append(
                (target, f"source is not an ENT (got {src_type or 'unidentified'})")
            )
        tgt_type = type_of(target)
        if tgt_type is not None and tgt_type != "ENT":
            problems.append((target, f"target is not an ENT (got {tgt_type})"))
        if qual is None:
            problems.append((target, "missing REQUIRED qualifier"))
        elif qual not in BRANCH_QUALIFIERS:
            problems.append(
                (target, f"invalid qualifier {qual!r} (one of {list(BRANCH_QUALIFIERS)})")
            )
    return problems


def relationship_entries(meta):
    """Every typed relationship as a dict with type/target/qualifier.

    Shared by graph_integrity.py (edge integrity) and build_view.py (chip
    rendering) so the qualifier is read the same way. Returns a list of
    {"type", "target", "qualifier"} (qualifier is None when absent).
    """
    out = []
    for r in (meta.get("relationships") or []):
        if isinstance(r, dict) and r.get("type") and r.get("target"):
            q = r.get("qualifier")
            out.append({
                "type": str(r["type"]).strip(),
                "target": str(r["target"]).strip(),
                "qualifier": (str(q).strip() if q is not None else None),
            })
    return out


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