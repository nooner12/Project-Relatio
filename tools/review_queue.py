#!/usr/bin/env python3
"""
review_queue.py — the Review & Revision queue for Project Relatio (STD-0009 §10).

Read-only. Runs the STD-0009 §4 trigger detections against the vault and emits
the current review queue — one row per surfaced item:

    object · trigger · resolved scope · prescribed act

exactly per the STD-0009 §4/§5 tables. The queue **PROPOSES**; it NEVER writes
to any record (ADR-GOV-0008 D6 / STD-0009 §10). Every act is executed by a
session under recorded governance, not by this tool.

v1 detections
-------------
  time_decay            review_date ≤ today                → whole record
                        → Light re-affirmation
  source_superseded     a Superseded object appears in a CLM/FND's derived_from,
                        or in a confidence component's bounded_by
                        → the affected components → Targeted re-grade
  upstream_grade_change an object in a component's bounded_by (or the record's
                        derived_from where bounded_by is absent) has a
                        confidence change in its history dated AFTER the
                        dependent record's last_reviewed
                        → the bounded components → Targeted re-grade
  contradiction         recorded flag (see MARKER CONVENTION) → the conflicting
                        claims → Full OPS-0003 circuit
  field_prose_divergence recorded flag → the divergent field → Reconciliation

The first three are computed from the graph; the last two are read from
recorded flags because a contradiction or a field/prose divergence is a
*judgment* a circuit session or reviewer makes, not something the graph shows.

MARKER CONVENTION (contradiction / field_prose_divergence)
----------------------------------------------------------
A flag is a line in the Governance Backlog of the form:

    REVIEW-FLAG | trigger=<contradiction|field_prose_divergence> | object=<ID> | scope=<free text>

(leading Markdown list/quote punctuation and surrounding whitespace are
ignored). One flag per line. The marker is deliberately explicit so that
ordinary Backlog prose mentioning a contradiction does NOT enter the queue —
e.g. the CLM-0043/0046/0050 borderline-split Backlog item is NOT a flag and
must NOT be written as one. Reflexive structural recommendations (ADR-GOV-0007)
enter the same queue via the same marker once the reflexive process graduates
(STD-0009 §10); v1 ships only the two review-flag triggers above so no act type
beyond the STD-0009 §5 table is invented.

Extended-length path handling per STD-0001 §8 (inherited from common.read_text).

Usage:
    python review_queue.py            # live run against the vault
    (importable: detect(records, objects, flags, today) is the pure core,
     exercised by tools/tests/test_review_queue.py)
"""

from datetime import date
from pathlib import Path
import re
import sys

import yaml

from common import (
    find_vault_root, markdown_files, parse_frontmatter, read_text,
    extract_identifier, version_elements, _parse_date, confidence_bounded_by,
)

# --- STD-0009 §5 trigger → scope → act table (the single source in code) -----
SCOPE_ACT = {
    "time_decay":            ("whole record",                 "Light re-affirmation"),
    "source_superseded":     ("affected components",          "Targeted re-grade"),
    "upstream_grade_change": ("bounded components",            "Targeted re-grade"),
    "contradiction":         ("the conflicting claims",       "Full OPS-0003 circuit"),
    "field_prose_divergence":("the divergent field",          "Reconciliation"),
}

KB_LEAF = ("CLM", "FND")

FLAG_RE = re.compile(
    r"REVIEW-FLAG\s*\|\s*trigger=(?P<trigger>[a-z_]+)\s*\|\s*"
    r"object=(?P<object>[A-Z]{2,5}-\d{4})\s*\|\s*scope=(?P<scope>.+?)\s*$"
)

# A history-row description that records an ACTUAL confidence-level change.
# Matches "Level 3→Level 2", "Level 3 -> 2", "lowered Level 3", "re-grade",
# but excludes rows that explicitly say no level changed (the remediation rows
# that pepper the vault: "no confidence level changed / not raised").
GRADE_CHANGE_RE = re.compile(
    r"(re-?grade|(?:lower|rais|chang)\w*\s+(?:to\s+)?level|level\s*\d\s*(?:→|->|to)\s*(?:level\s*)?\d)",
    re.I,
)
GRADE_NOCHANGE_RE = re.compile(r"no\s+confidence\s+level|level\s+(?:un)?changed|not\s+(?:raised|lowered|changed)", re.I)


def _as_tuple(d):
    """A (y,m,d) tuple for a date-ish value, or None."""
    return _parse_date(d)


def load_objects(vault):
    """Index every object: id → {operational_status, grade_change_dates}.

    grade_change_dates: the dates of that object's own Revision-History rows
    whose description records an actual confidence-level change (used by the
    upstream_grade_change detection).
    """
    objects = {}
    for f in markdown_files(vault):
        ident = extract_identifier(f.stem)
        if ident is None:
            continue
        text = read_text(f)
        fm, body = parse_frontmatter(text)
        meta = {}
        if fm is not None:
            try:
                loaded = yaml.safe_load(fm)
                if isinstance(loaded, dict):
                    meta = loaded
            except Exception:
                meta = {}

        grade_dates = []
        hist = version_elements(body if fm is not None else text, fm)
        # Re-scan history rows for dates + descriptions (version_elements gives
        # only versions); parse the table rows directly.
        for row in re.findall(r"^\|.*\|$", (body if fm is not None else text), re.M):
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) >= 4:
                dt = _parse_date(cells[1])
                desc = cells[-1]
                if dt and GRADE_CHANGE_RE.search(desc) and not GRADE_NOCHANGE_RE.search(desc):
                    grade_dates.append(dt)

        objects[ident] = {
            "operational_status": meta.get("operational_status"),
            "grade_change_dates": grade_dates,
        }
    return objects


def load_records(vault):
    """The CLM/FND records with their review fields, derived_from, and per-component bounded_by."""
    records = []
    for f in markdown_files(vault):
        ident = extract_identifier(f.stem)
        if ident is None or ident.split("-")[0] not in KB_LEAF:
            continue
        text = read_text(f)
        fm, _ = parse_frontmatter(text)
        if fm is None:
            continue
        try:
            meta = yaml.safe_load(fm)
        except Exception:
            continue
        if not isinstance(meta, dict):
            continue

        derived = []
        for r in (meta.get("relationships") or []):
            if isinstance(r, dict) and str(r.get("type", "")).strip() == "derived_from":
                derived.append(str(r.get("target")).strip())

        components = []
        for comp in (meta.get("confidence") or []):
            if isinstance(comp, dict):
                components.append({
                    "component": str(comp.get("component", "?")),
                    "bounded_by": [str(b).strip() for b in (comp.get("bounded_by") or [])],
                })

        records.append({
            "id": ident,
            "review_date": _parse_date(meta.get("review_date")),
            "last_reviewed": _parse_date(meta.get("last_reviewed")),
            "derived_from": derived,
            "components": components,
        })
    return records


def load_flags(vault):
    """Recorded contradiction / field_prose_divergence flags from the Governance Backlog."""
    flags = []
    for f in markdown_files(vault):
        if "Governance Backlog" not in f.name:
            continue
        for line in read_text(f).splitlines():
            m = FLAG_RE.search(line)
            if m:
                flags.append({
                    "trigger": m.group("trigger"),
                    "object": m.group("object"),
                    "scope": m.group("scope").strip(),
                })
    return flags


def detect(records, objects, flags, today):
    """Pure core: return queue items. today is a (y,m,d) tuple.

    Each item: {object, trigger, scope, act}. Deterministic ordering.
    """
    items = []

    for rec in records:
        rid = rec["id"]

        # time_decay -------------------------------------------------------
        rd = rec["review_date"]
        if rd is not None and tuple(rd) <= tuple(today):
            scope, act = SCOPE_ACT["time_decay"]
            items.append({"object": rid, "trigger": "time_decay", "scope": scope, "act": act})

        last = rec["last_reviewed"]

        # Per-component graph triggers. A component's resolution surface is its
        # bounded_by if present, else the record's derived_from edges (STD-0009 §5/§9).
        for comp in rec["components"]:
            surface = comp["bounded_by"] if comp["bounded_by"] else rec["derived_from"]
            cname = comp["component"]

            for up in surface:
                uo = objects.get(up)
                if uo is None:
                    continue

                # source_superseded -------------------------------------
                if uo.get("operational_status") == "Superseded":
                    scope, act = SCOPE_ACT["source_superseded"]
                    items.append({
                        "object": rid, "trigger": "source_superseded",
                        "scope": f"{scope}: {cname} (← {up})", "act": act,
                    })

                # upstream_grade_change ---------------------------------
                if last is not None:
                    for gd in uo.get("grade_change_dates", []):
                        if tuple(gd) > tuple(last):
                            scope, act = SCOPE_ACT["upstream_grade_change"]
                            items.append({
                                "object": rid, "trigger": "upstream_grade_change",
                                "scope": f"{scope}: {cname} (← {up} re-graded {gd[0]:04d}-{gd[1]:02d}-{gd[2]:02d})",
                                "act": act,
                            })
                            break

    # contradiction / field_prose_divergence (recorded flags) -------------
    for fl in flags:
        trig = fl["trigger"]
        if trig not in ("contradiction", "field_prose_divergence"):
            continue  # v1 ships only these two flag triggers
        _, act = SCOPE_ACT[trig]
        items.append({
            "object": fl["object"], "trigger": trig,
            "scope": fl["scope"], "act": act,
        })

    items.sort(key=lambda x: (x["object"], x["trigger"], x["scope"]))
    return items


def render(items):
    lines = []
    lines.append("# Review Queue — Project Relatio (STD-0009 §10)")
    lines.append("")
    lines.append(f"Items: {len(items)}")
    lines.append("")
    if not items:
        lines.append("Queue empty — nothing due. (All review_dates future-dated; "
                      "no supersessions; no upstream grade changes after last review; "
                      "no recorded flags.)")
        return "\n".join(lines) + "\n"
    lines.append("| Object | Trigger | Resolved scope | Prescribed act |")
    lines.append("|---|---|---|---|")
    for it in items:
        lines.append(f"| {it['object']} | `{it['trigger']}` | {it['scope']} | {it['act']} |")
    return "\n".join(lines) + "\n"


def main():
    tools = Path(__file__).parent
    vault = find_vault_root(tools)
    records = load_records(vault)
    objects = load_objects(vault)
    flags = load_flags(vault)
    today = date.today()
    items = detect(records, objects, flags, (today.year, today.month, today.day))
    report = render(items)
    print(report)
    out = tools / "output" / "review_queue.md"
    out.parent.mkdir(exist_ok=True)
    from common import write_text
    write_text(out, report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
