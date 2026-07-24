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
# Attribution shape check (STD-0002 §6/§6.1 v1.12 / ADR-GOV-0011 Decisions B+C)
#
# Every formal Knowledge Object carries `attribution`: provenance, with
# AI-assistance disclosure. This helper checks *shape* only -- whether a
# disclosed degree is *honest* is not a machine question, and is deliberately
# left to the permanent-record principle (ADR-GOV-0011 §4).
#
# **ALWAYS A LIST**, minimum one entry. At Stage 1 the vault writes exactly one
# entry (`event: created`), but the check does NOT cap the list length: Stage 2
# (per-event attribution, deferred per ADR-GOV-0011 §8) extends the same list
# additively, and a Stage-1 checker that rejected a second entry would make that
# extension a migration -- precisely the outcome the list shape exists to avoid.
# tests/test_attribution.py pins this with a two-entry additivity case.
#
# `event` is likewise NOT vocabulary-checked. `created` is the only value Stage 1
# writes, but the Stage 2 vocabulary (reviewed / verified / ratified / …) is not
# yet decided, and hard-coding a one-value enum here would have to be unwound.
#
# **No metric may be computed from this field** (ADR-GOV-0011 Decision E): any
# tool computing contributor standing, ranking, or gating absent its own
# governance ADR is nonconformant by definition. This checker counts problems,
# never contributors.
# ----------------------------------------------------------------------------

AI_DEGREES = ("unassisted", "ai-assisted", "ai-delegated")

ATTRIBUTION_KEYS = ("actor", "role", "event", "date", "ai_degree",
                    "ai_model_family")


def attribution_problems(meta):
    """Shape-check the STD-0002 §6 `attribution` field of a frontmatter dict.

    Returns a list of problem strings; empty means well-formed.
    """
    problems = []
    attribution = meta.get("attribution")

    if attribution is None:
        problems.append(
            "missing `attribution` (STD-0002 §6 v1.12: required list, "
            "minimum one entry)"
        )
        return problems

    if not isinstance(attribution, list) or not attribution:
        problems.append(
            "`attribution` must be a non-empty list -- a single entry is a "
            "one-item list, never a scalar block (STD-0002 §6; the list shape "
            "is what makes ADR-GOV-0011 Stage 2 additive)"
        )
        return problems

    for i, entry in enumerate(attribution):
        if not isinstance(entry, dict):
            problems.append(
                f"attribution[{i}] must be a mapping with "
                f"{'/'.join(ATTRIBUTION_KEYS)}"
            )
            continue

        for key in ATTRIBUTION_KEYS:
            if entry.get(key) is None:
                problems.append(f"attribution[{i}].{key} is required")

        for key in ("actor", "role", "event"):
            value = entry.get(key)
            if value is not None and (
                not isinstance(value, str) or not value.strip()
            ):
                problems.append(
                    f"attribution[{i}].{key} must be a non-empty string "
                    f"(got {value!r})"
                )

        date = entry.get("date")
        if date is not None and _parse_date(date) is None:
            problems.append(
                f"attribution[{i}].date must be YYYY-MM-DD (§10) (got {date!r})"
            )

        degree = entry.get("ai_degree")
        if degree is not None and degree not in AI_DEGREES:
            problems.append(
                f"attribution[{i}].ai_degree must be one of "
                f"{list(AI_DEGREES)} (got {degree!r})"
            )

        family = entry.get("ai_model_family")
        if family is not None and (
            not isinstance(family, str) or not family.strip()
        ):
            problems.append(
                f"attribution[{i}].ai_model_family must be a non-empty string "
                f"(a vendor/family, or the literal `none`) (got {family!r})"
            )
        elif degree in AI_DEGREES and isinstance(family, str):
            # The pairing rule, enforced as a biconditional (STD-0002 §6):
            # `none` iff `unassisted`. Implemented at ERROR, not warning -- an
            # `unassisted` entry naming a model family, or an AI-assisted entry
            # naming none, is self-contradictory on its face, and neither has a
            # legitimate use the free-string field would otherwise permit.
            is_none = family.strip().lower() == "none"
            if degree == "unassisted" and not is_none:
                problems.append(
                    f"attribution[{i}].ai_model_family must be `none` when "
                    f"ai_degree is `unassisted` (got {family!r})"
                )
            elif degree != "unassisted" and is_none:
                problems.append(
                    f"attribution[{i}].ai_model_family must name a model "
                    f"family when ai_degree is {degree!r} (got `none`)"
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
    "continuation",  # ADR-GOV-0010 D1 (STD-0004 v1.3) — main-line carry-forward
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


RANGE_UNCERTAINTIES = ("low", "moderate", "high")

# The render-only positioning fields (STD-0002 §11 v1.11). OPTIONAL; when any is
# present, range_start_year + range_uncertainty are co-required, range_end_year
# optional (an integer year or the literal token `present`).
RANGE_FIELDS = ("range_start_year", "range_end_year", "range_uncertainty")


def tradition_range_problems(meta):
    """Shape-check the OPTIONAL render-only positioning fields (STD-0002 §11 v1.11).

    Returns a list of problem strings; empty means well-formed OR none present.
    These are NON-EVIDENTIAL rendering hints — this checks shape only (integer
    years or the `present` token; the uncertainty vocabulary; start+uncertainty
    co-presence). Whether a bound is *correctly derived* from the dating claim is
    a review question, not a shape question. `range_end_year` accepts the literal
    string `present` (a living tradition) or an integer; a bare integer year may
    be negative (BCE). PyYAML parses an unquoted `present` to the string, and a
    signed integer to int, so both arrive typed.
    """
    problems = []
    present = {f: meta.get(f) for f in RANGE_FIELDS if meta.get(f) is not None}
    if not present:
        return problems  # no positioning fields: nothing to check

    start = meta.get("range_start_year")
    if start is not None and (isinstance(start, bool) or not isinstance(start, int)):
        problems.append(
            f"`range_start_year` must be an integer year (BCE negative) (got {start!r})"
        )

    end = meta.get("range_end_year")
    if end is not None:
        if isinstance(end, str):
            if end.strip() != "present":
                problems.append(
                    f"`range_end_year` string must be the literal `present` (got {end!r})"
                )
        elif isinstance(end, bool) or not isinstance(end, int):
            problems.append(
                f"`range_end_year` must be an integer year or the token `present` (got {end!r})"
            )

    unc = meta.get("range_uncertainty")
    if unc is not None and unc not in RANGE_UNCERTAINTIES:
        problems.append(
            f"`range_uncertainty` must be one of {list(RANGE_UNCERTAINTIES)} (got {unc!r})"
        )

    # Co-presence: any positioning field present requires start + uncertainty
    # (range_end_year stays optional — absent = terminus not claim-dated).
    if meta.get("range_start_year") is None:
        problems.append(
            "positioning fields present but `range_start_year` missing "
            "(STD-0002 §11 v1.11: start + uncertainty are co-required)"
        )
    if meta.get("range_uncertainty") is None:
        problems.append(
            "positioning fields present but `range_uncertainty` missing "
            "(STD-0002 §11 v1.11: start + uncertainty are co-required)"
        )

    return problems


# ----------------------------------------------------------------------------
# Entity rendering class + community-class fields (ADR-GOV-0012 D2/D3/D4 /
# STD-0002 §11 v1.13).
#
# The entity layer is multi-granularity. `rendering_class` declares which
# resolution an entity occupies and is REQUIRED AT MINT on every entity carrying
# a class field set. Concept entities (ENT-0001…0007) are outside the timeline
# program: they carry no class field set and no `rendering_class`, and must never
# be flagged.
#
# The `substrate` class is ESTABLISHED but has NO FIELD SET (ADR-GOV-0012 D7
# defers substrate rendering and no substrate entity is minted). Both field sets
# are therefore forbidden on it — the value exists so the class is reachable
# later without reopening governance, not so a session can improvise one.
# ----------------------------------------------------------------------------

RENDERING_CLASSES = ("tradition", "substrate", "community")

# The three co-required community-class fields (STD-0002 §11 v1.13).
COMMUNITY_FIELDS = ("attestation_claims", "attestation_window",
                    "attestation_uncertainty")


def rendering_class_problems(meta):
    """Check `rendering_class` presence, vocabulary, and class/field-set fit.

    Returns (missing, problems):
      * `missing` is the single "required at mint" problem string, or None. It is
        returned SEPARATELY so the caller can warning-gate it during the
        define -> backfill -> enforce migration window (the EPISTEMIC_FIELDS
        precedent); every other problem is an error from introduction because it
        guards births rather than describing migration debt.
      * `problems` is everything else: an out-of-vocabulary value, a class
        declared without its field set, and any field set forbidden on the
        declared class.

    A concept entity (no rendering_class, no class fields) yields (None, []).
    """
    problems = []
    trad = [f for f in TRADITION_FIELDS if meta.get(f) is not None]
    comm = [f for f in COMMUNITY_FIELDS if meta.get(f) is not None]
    rng = [f for f in RANGE_FIELDS if meta.get(f) is not None]
    rc = meta.get("rendering_class")

    if rc is None:
        if trad or comm:
            return (
                "missing `rendering_class` (STD-0002 §11 v1.13 / ADR-GOV-0012 "
                f"D3: REQUIRED AT MINT; class fields present {sorted(trad + comm)})",
                problems,
            )
        return None, problems  # concept entity: outside the timeline program

    if rc not in RENDERING_CLASSES:
        problems.append(
            f"`rendering_class` must be one of {list(RENDERING_CLASSES)} (got {rc!r})"
        )
        return None, problems

    if rc == "tradition":
        if not trad:
            problems.append(
                "`rendering_class: tradition` requires the tradition-class field "
                f"set {list(TRADITION_FIELDS)} (none present)"
            )
        if comm:
            problems.append(
                f"community-class fields {sorted(comm)} are forbidden on "
                "`rendering_class: tradition`"
            )
    elif rc == "community":
        if not comm:
            problems.append(
                "`rendering_class: community` requires the community-class field "
                f"set {list(COMMUNITY_FIELDS)} (none present)"
            )
        if trad:
            problems.append(
                f"tradition-class fields {sorted(trad)} are forbidden on "
                "`rendering_class: community` (a community entity carries an "
                "ATTESTATION WINDOW, never a founding date — ADR-GOV-0012 D4)"
            )
        if rng:
            problems.append(
                f"render-only positioning bounds {sorted(rng)} are forbidden on "
                "`rendering_class: community` — a community entity has no numeric "
                "geometry and no founding-date-style bar (ADR-GOV-0012 D4)"
            )
    else:  # substrate
        if trad or comm or rng:
            problems.append(
                "`rendering_class: substrate` has NO field set — substrate "
                "rendering is deferred (ADR-GOV-0012 D7) and no substrate entity "
                f"is minted; remove {sorted(trad + comm + rng)}"
            )

    return None, problems


def community_entity_problems(meta):
    """Shape-check the community-class entity fields (STD-0002 §11 v1.13).

    Returns (problems, attestation_claims). The three fields are **co-required**:
    presence of ANY one requires ALL three, exactly as the tradition trio. Shape
    only -- whether a window is *correctly derived* from its warranting records
    is a review question. Resolution of `attestation_claims` targets is
    graph_integrity's job (they are graph claims, §12.1), so this returns them
    rather than resolving.
    """
    problems = []
    present = {f: meta.get(f) for f in COMMUNITY_FIELDS if meta.get(f) is not None}

    if not present:
        return problems, []  # not a community entity: nothing to check

    missing = [f for f in COMMUNITY_FIELDS if meta.get(f) is None]
    if missing:
        problems.append(
            "community-class entity fields are co-required (STD-0002 §11 v1.13): "
            f"present {sorted(present)}, missing {missing}"
        )

    claims = meta.get("attestation_claims")
    claim_list = []
    if claims is not None:
        if not isinstance(claims, list) or not claims:
            problems.append(
                "`attestation_claims` must be a non-empty list of graded-record "
                "identifiers (Claim or Finding Records)"
            )
        else:
            for i, entry in enumerate(claims):
                ident = extract_identifier(str(entry).strip())
                if ident is None:
                    problems.append(
                        f"attestation_claims[{i}] must be a record identifier "
                        f"(got {entry!r})"
                    )
                else:
                    claim_list.append(str(entry).strip())

    window = meta.get("attestation_window")
    if window is not None and (not isinstance(window, str) or not window.strip()):
        problems.append(
            "`attestation_window` must be a non-empty string (render-only; a "
            "WINDOW, never a founding date)"
        )

    unc = meta.get("attestation_uncertainty")
    if unc is not None and unc not in RANGE_UNCERTAINTIES:
        problems.append(
            f"`attestation_uncertainty` must be one of "
            f"{list(RANGE_UNCERTAINTIES)} (got {unc!r})"
        )

    return problems, claim_list


# ----------------------------------------------------------------------------
# projects_to + influenced_by edge integrity (ADR-GOV-0012 D5/D6 / STD-0004 v1.5
# §7 and §7.3).
#
# Two new relationship types with opposite characters, deliberately checked in
# one place so the difference cannot blur:
#
#   * `projects_to` is NON-EVIDENTIAL. It says "for rendering, re-anchor here"
#     and asserts nothing about the world. It takes NO qualifier, NO warrant, and
#     NO confidence component, and any of them present is an ERROR -- the
#     enforcement is what keeps it out of the evidential vocabulary, rather than
#     trusting it to stay there. It IS machine-traversable (roll-up rendering
#     will traverse it), so a dangling target is an error like any graph claim.
#
#   * `influenced_by` is evidential and its warrant rule is CONSTITUTIVE: a
#     graded warrant PLUS a recorded not-descent determination. Unlike
#     `branches_from` (whose warrant is prose and therefore review-checked), both
#     are structured resolvable pointers here, precisely because ADR-GOV-0012 D6
#     makes "no instance without a not-descent determination" a rule a tool can
#     hold. Without it the type becomes the soft option that empties the
#     edge-restraint rule of force.
# ----------------------------------------------------------------------------

INFLUENCE_QUALIFIERS = ("documented", "contested")

# Keys that make a projects_to entry malformed (STD-0004 §7.3). `confidence` is
# listed because a graded projection would be an evidential edge by another name.
PROJECTS_TO_FORBIDDEN = ("qualifier", "warrant", "not_descent", "confidence")


def relationship_raw(meta):
    """Every typed relationship as its RAW dict (type/target present).

    `relationship_entries` normalizes to type/target/qualifier and drops
    everything else, which is exactly wrong for a check whose job is to notice an
    extra key. This returns the entries as authored so
    `projects_to_problems` can see a forbidden `confidence`/`qualifier`.
    """
    return [r for r in (meta.get("relationships") or [])
            if isinstance(r, dict) and r.get("type") and r.get("target")]


def projects_to_problems(source_id, entries, class_of):
    """Integrity-check a source object's projects_to edges (STD-0004 §7.3).

    `entries` is the list of RAW relationship dicts whose type is projects_to;
    `class_of` maps a target identifier to (object_type, rendering_class), with
    object_type None when the target does not resolve (the dangling pass owns
    that case). Returns a list of (target, reason) problems.

    Enforced as errors: source is an ENT; source is NOT tradition-class (a
    tradition does not project); target resolves to a tradition-class ENT; and
    the entry carries none of the forbidden evidential keys.
    """
    problems = []
    src_type, src_class = class_of(source_id) if source_id else (None, None)
    for entry in entries:
        target = str(entry.get("target")).strip()
        if src_type != "ENT":
            problems.append(
                (target, f"source is not an ENT (got {src_type or 'unidentified'})")
            )
        elif src_class == "tradition":
            problems.append(
                (target, "source is tradition-class — projects_to runs "
                         "non-tradition -> tradition (ADR-GOV-0012 D5)")
            )
        elif src_class is None:
            problems.append(
                (target, "source carries no `rendering_class` (required at mint)")
            )
        tgt_type, tgt_class = class_of(target)
        if tgt_type is not None:
            if tgt_type != "ENT":
                problems.append((target, f"target is not an ENT (got {tgt_type})"))
            elif tgt_class != "tradition":
                problems.append(
                    (target, f"target must be tradition-class (got "
                             f"{tgt_class!r}) — projects_to re-anchors to the "
                             f"tradition layer")
                )
        for key in PROJECTS_TO_FORBIDDEN:
            if entry.get(key) is not None:
                problems.append(
                    (target, f"`{key}` is forbidden on projects_to — the relation "
                             f"is NON-EVIDENTIAL (STD-0004 §7.3 / ADR-GOV-0012 D5)")
                )
    return problems


def influenced_by_problems(source_id, entries, type_of, resolves):
    """Integrity-check a source object's influenced_by edges (STD-0004 §7.3).

    `entries` is the list of RAW relationship dicts whose type is influenced_by;
    `type_of` maps a target identifier to its object type (None if unresolved);
    `resolves` is a predicate saying whether an identifier resolves to an
    existing object. Returns a list of (target, reason) problems.

    Enforced as errors: ENT -> ENT; a REQUIRED qualifier from
    INFLUENCE_QUALIFIERS; a non-empty, fully resolvable `warrant` list; and a
    present, resolvable `not_descent` pointer. The last is the constitutive one
    (ADR-GOV-0012 D6) -- an edge without a recorded not-descent determination may
    not exist, and that is checked here rather than left to review.
    """
    problems = []
    src_type = source_id.split("-")[0] if source_id else None
    for entry in entries:
        target = str(entry.get("target")).strip()
        if src_type != "ENT":
            problems.append(
                (target, f"source is not an ENT (got {src_type or 'unidentified'})")
            )
        tgt_type = type_of(target)
        if tgt_type is not None and tgt_type != "ENT":
            problems.append((target, f"target is not an ENT (got {tgt_type})"))

        qual = entry.get("qualifier")
        if qual is None:
            problems.append((target, "missing REQUIRED qualifier"))
        elif str(qual).strip() not in INFLUENCE_QUALIFIERS:
            problems.append(
                (target, f"invalid qualifier {qual!r} "
                         f"(one of {list(INFLUENCE_QUALIFIERS)})")
            )

        warrant = entry.get("warrant")
        if warrant is None:
            problems.append(
                (target, "missing REQUIRED `warrant` (graded claim(s) — the edge "
                         "renders, the claim warrants)")
            )
        elif not isinstance(warrant, list) or not warrant:
            problems.append(
                (target, f"`warrant` must be a non-empty list of graded-record "
                         f"identifiers (got {warrant!r})")
            )
        else:
            for w in warrant:
                w = str(w).strip()
                if not resolves(w):
                    problems.append(
                        (target, f"`warrant` entry {w!r} does not resolve")
                    )

        nd = entry.get("not_descent")
        if nd is None:
            problems.append(
                (target, "missing REQUIRED `not_descent` determination — "
                         "CONSTITUTIVE (ADR-GOV-0012 D6): no influenced_by edge "
                         "may exist without a recorded statement of why "
                         "branches_from was refused")
            )
        elif not resolves(str(nd).strip()):
            problems.append(
                (target, f"`not_descent` pointer {str(nd).strip()!r} does not resolve")
            )
    return problems


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