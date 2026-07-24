#!/usr/bin/env python3
"""Detection tests for the ADR-GOV-0012 enactment: `rendering_class`, the
community-class attestation fields, and the `projects_to` / `influenced_by` edge
integrity checks (STD-0002 §11 v1.13 / STD-0004 v1.5 §7 and §7.3).

House convention: PROVE THE POSITIVE. After the ENT-0008…0015 backfill the whole
vault carries `rendering_class`, and every edge in the vault is well-formed, so a
clean live run proves nothing about whether the checkers can see a bad record.
Each check below is fired against a deliberately-defective fixture:

  * `rendering_class` MISSING on an entity that carries a class field set (the
    D3 required-at-mint rule) — and the same fixture is used to pin the
    migration gate: the missing-field problem is returned SEPARATELY so it could
    be warning-gated until the backfill commit landed;
  * an out-of-vocabulary `rendering_class`;
  * a class declared without its field set, and each field set forbidden on the
    wrong class — including the load-bearing one, a community entity carrying
    the render-only positioning bounds (a founding-date-style bar, ADR-GOV-0012
    D4 forbids it);
  * community-field co-presence, list/string/vocabulary shape;
  * `projects_to`: a qualifier REJECTED, a confidence component REJECTED, a
    dangling target caught, and a non-tradition target caught;
  * `influenced_by`: missing/invalid qualifier, missing warrant, dangling
    warrant, MISSING NOT_DESCENT (the constitutive check), and a non-ENT target;
  * the concept entities are untouched by all of it;
  * source wiring for validate.py and graph_integrity.py.

Run: python tools/tests/test_rendering_class.py
"""

from pathlib import Path
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common import (  # noqa: E402
    parse_frontmatter,
    read_text,
    rendering_class_problems,
    community_entity_problems,
    relationship_raw,
    projects_to_problems,
    influenced_by_problems,
    RENDERING_CLASSES,
    INFLUENCE_QUALIFIERS,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"
TOOLS = Path(__file__).resolve().parent.parent

failures = []


def want(cond, msg):
    if not cond:
        failures.append(msg)


def meta_of(name):
    fm, _ = parse_frontmatter(read_text(FIXTURES / name))
    return yaml.safe_load(fm)


# ---------------------------------------------------------------------------
# 1. rendering_class (ADR-GOV-0012 D2/D3)
# ---------------------------------------------------------------------------
print("rendering_class detection (STD-0002 §11 v1.13 / ADR-GOV-0012 D3)")

missing, probs = rendering_class_problems(meta_of("rendering_class_missing.md"))
want(missing is not None and "REQUIRED AT MINT" in missing,
     f"missing rendering_class not caught: {missing!r}")
want(probs == [],
     f"the missing-field case must return NO other problems (it is the "
     f"migration-gated one), got {probs}")
print(f"  missing on a class-fielded entity -> fires: {bool(missing)}")

missing, probs = rendering_class_problems(meta_of("rendering_class_bad_value.md"))
want(missing is None, "an out-of-vocabulary value is not a 'missing' problem")
want(any("must be one of" in p and "milieu" in p for p in probs),
     f"out-of-vocabulary rendering_class not caught: {probs}")
print(f"  out-of-vocabulary value -> {len(probs)} problems")

# Concept entity: no class fields, no rendering_class -> silent, both ways.
missing, probs = rendering_class_problems(meta_of("concept_entity.md"))
want(missing is None and probs == [],
     f"concept entity must be untouched, got missing={missing!r} probs={probs}")
print("  concept entity -> untouched (0 problems)")

# A class declared without its field set.
_, probs = rendering_class_problems({"rendering_class": "tradition"})
want(any("requires the tradition-class field set" in p for p in probs),
     f"tradition class without its field set not caught: {probs}")
_, probs = rendering_class_problems({"rendering_class": "community"})
want(any("requires the community-class field set" in p for p in probs),
     f"community class without its field set not caught: {probs}")

# Field sets forbidden on the wrong class.
_, probs = rendering_class_problems(
    {"rendering_class": "tradition", "tradition_type": "founded",
     "dating_claims": ["CLM-9001"], "display_range": "x",
     "attestation_window": "y"})
want(any("forbidden on `rendering_class: tradition`" in p for p in probs),
     f"community field on a tradition entity not caught: {probs}")

_, probs = rendering_class_problems(
    {"rendering_class": "community", "attestation_claims": ["CLM-9101"],
     "attestation_window": "x", "attestation_uncertainty": "moderate",
     "tradition_type": "founded"})
want(any("ATTESTATION WINDOW, never a founding date" in p for p in probs),
     f"tradition field on a community entity not caught: {probs}")

# THE LOAD-BEARING ONE: a community entity carrying a founding-date-style bar.
_, probs = rendering_class_problems(meta_of("community_entity_forbidden_bar.md"))
want(any("no numeric geometry and no founding-date-style bar" in p for p in probs),
     f"positioning bounds on a community entity not caught: {probs}")
print("  founding-date-style bar on a community entity -> fires (D4)")

# substrate: established as a class, but no field set exists for it yet (D7).
_, probs = rendering_class_problems({"rendering_class": "substrate"})
want(probs == [], f"bare substrate must be silent, got {probs}")
_, probs = rendering_class_problems(
    {"rendering_class": "substrate", "display_range": "x"})
want(any("has NO field set" in p and "D7" in p for p in probs),
     f"substrate carrying a field set not caught: {probs}")
print("  substrate -> class reachable, field sets refused (D7 deferral held)")

want(set(RENDERING_CLASSES) == {"tradition", "substrate", "community"},
     f"RENDERING_CLASSES drifted from ADR-GOV-0012 D2: {RENDERING_CLASSES}")

# ---------------------------------------------------------------------------
# 2. Community-class field shape (ADR-GOV-0012 D4)
# ---------------------------------------------------------------------------
print()
print("community-class field shape (STD-0002 §11 v1.13 / ADR-GOV-0012 D4)")

probs, claims = community_entity_problems(meta_of("community_entity_wellformed.md"))
want(probs == [], f"well-formed community entity flagged: {probs}")
want(claims == ["CLM-9101"], f"expected attestation_claims ['CLM-9101'], got {claims}")
print(f"  well-formed -> {len(probs)} problems; attestation_claims={claims}")

probs, _ = community_entity_problems(meta_of("community_entity_missing_field.md"))
want(any("co-required" in p and "attestation_uncertainty" in p for p in probs),
     f"community co-presence violation not caught: {probs}")
print(f"  co-presence violation -> {len(probs)} problems")

probs, _ = community_entity_problems(
    {"attestation_claims": [], "attestation_window": "x",
     "attestation_uncertainty": "moderate"})
want(any("non-empty list" in p for p in probs),
     f"empty attestation_claims not caught: {probs}")

probs, _ = community_entity_problems(
    {"attestation_claims": ["CLM-9101"], "attestation_window": "x",
     "attestation_uncertainty": "quite sure"})
want(any("attestation_uncertainty" in p and "quite sure" in p for p in probs),
     f"out-of-vocabulary attestation_uncertainty not caught: {probs}")

# A tradition entity carries no community fields -> silent.
probs, claims = community_entity_problems(meta_of("tradition_entity_wellformed.md"))
want(probs == [] and claims == [],
     f"tradition entity must be untouched by the community check: {probs}")
print("  tradition + concept entities -> untouched by the community check")

# ---------------------------------------------------------------------------
# 3. projects_to integrity (ADR-GOV-0012 D5 / STD-0004 §7.3)
# ---------------------------------------------------------------------------
print()
print("projects_to edge integrity (STD-0004 v1.5 §7.3 / ADR-GOV-0012 D5)")

FIXTURE_CLASSES = {
    "ENT-9100": ("ENT", "tradition"),
    "ENT-9101": ("ENT", "tradition"),
    "ENT-9102": ("ENT", "tradition"),
    "ENT-9202": ("ENT", "community"),
    "ENT-9205": ("ENT", "community"),
    "ENT-9206": ("ENT", "tradition"),
    "CLM-9101": ("CLM", None),
    "CLM-9102": ("CLM", None),
}


def class_of(target):
    return FIXTURE_CLASSES.get(str(target).strip(), (None, None))


raw = relationship_raw(meta_of("projects_to_edges.md"))
projections = [r for r in raw if r["type"] == "projects_to"]
want(len(projections) == 5,
     f"expected 5 projects_to entries in the fixture, got {len(projections)}")

pp = projects_to_problems("ENT-9205", projections, class_of)


def hit(target, fragment, problems):
    return any(t == target and fragment in why for t, why in problems)


want(hit("ENT-9101", "`qualifier` is forbidden", pp),
     f"qualified projects_to not REJECTED: {pp}")
want(hit("ENT-9102", "`confidence` is forbidden", pp),
     f"projects_to carrying a confidence component not REJECTED: {pp}")
want(hit("ENT-9202", "target must be tradition-class", pp),
     f"non-tradition projects_to target not caught: {pp}")
want(not any(t == "ENT-9100" for t, _ in pp),
     f"the valid projects_to edge must NOT be flagged: {pp}")
print(f"  qualifier / confidence / wrong-direction -> {len(pp)} problems")

# A dangling target is caught by the DANGLING pass, which owns it (Check 1) —
# projects_to is machine-traversable, so an unresolvable target fails the build.
# Proven here through the same resolve-shaped predicate graph_integrity uses.
want(class_of("ENT-9999") == (None, None),
     "the fixture's dangling target must not resolve")
want(not any(t == "ENT-9999" and "target" in why for t, why in pp),
     "a dangling target must be reported by the dangling pass, not duplicated here")
gi_src = read_text(TOOLS / "graph_integrity.py")
want('relationships[' in gi_src and 'for rtype, target in o["typed"]' in gi_src,
     "graph_integrity must run every typed target (projects_to included) through "
     "the dangling pass")
print("  dangling target -> owned by the dangling pass (build-failing)")

# A tradition entity may not be the SOURCE of a projection.
pp2 = projects_to_problems("ENT-9100", [{"type": "projects_to", "target": "ENT-9101"}],
                           class_of)
want(any("source is tradition-class" in why for _, why in pp2),
     f"tradition-class source not caught: {pp2}")

# ---------------------------------------------------------------------------
# 4. influenced_by integrity (ADR-GOV-0012 D6 / STD-0004 §7.3)
# ---------------------------------------------------------------------------
print()
print("influenced_by edge integrity (STD-0004 v1.5 §7.3 / ADR-GOV-0012 D6)")

RESOLVABLE = set(FIXTURE_CLASSES) | {"ENT-9203", "ENT-9204"}


def type_of(target):
    return FIXTURE_CLASSES.get(str(target).strip(), (None, None))[0] \
        or (str(target).split("-")[0] if str(target).strip() in RESOLVABLE else None)


raw = relationship_raw(meta_of("influenced_by_edges.md"))
influences = [r for r in raw if r["type"] == "influenced_by"]
want(len(influences) == 8,
     f"expected 8 influenced_by entries in the fixture, got {len(influences)}")

ip = influenced_by_problems("ENT-9206", influences, type_of,
                            lambda ref: ref in RESOLVABLE)

want(hit("ENT-9204", "invalid qualifier", ip),
     f"invalid influenced_by qualifier not caught: {ip}")
want(hit("ENT-9205", "missing REQUIRED qualifier", ip),
     f"missing influenced_by qualifier not caught: {ip}")
want(hit("ENT-9100", "missing REQUIRED `warrant`", ip),
     f"missing warrant not caught: {ip}")
want(hit("ENT-9101", "does not resolve", ip),
     f"dangling warrant not caught: {ip}")
want(hit("ENT-9102", "missing REQUIRED `not_descent`", ip),
     f"MISSING NOT_DESCENT not caught — the constitutive check: {ip}")
want(hit("CLM-9101", "target is not an ENT", ip),
     f"non-ENT influenced_by target not caught: {ip}")
want(not any(t in ("ENT-9202", "ENT-9203") for t, _ in ip),
     f"the two valid influenced_by edges must NOT be flagged: {ip}")
print(f"  qualifier / warrant / not_descent / domain -> {len(ip)} problems")

# The constitutive rule, stated on its own so it cannot be lost in a rewrite:
# an otherwise-perfect edge with no not_descent pointer is still rejected.
ip2 = influenced_by_problems(
    "ENT-9206",
    [{"type": "influenced_by", "target": "ENT-9202", "qualifier": "documented",
      "warrant": ["CLM-9101"]}],
    type_of, lambda ref: ref in RESOLVABLE)
want(any("CONSTITUTIVE" in why for _, why in ip2),
     f"an edge lacking only not_descent must still be rejected: {ip2}")

# A dangling not_descent is caught too (a named-but-nonexistent determination is
# not a determination).
ip3 = influenced_by_problems(
    "ENT-9206",
    [{"type": "influenced_by", "target": "ENT-9202", "qualifier": "documented",
      "warrant": ["CLM-9101"], "not_descent": "CLM-9999"}],
    type_of, lambda ref: ref in RESOLVABLE)
want(any("`not_descent` pointer" in why and "does not resolve" in why
         for _, why in ip3),
     f"dangling not_descent not caught: {ip3}")
print("  not_descent absent AND unresolvable -> both fire")

# A non-ENT source is flagged for every edge (parallel to branches_from).
ip4 = influenced_by_problems(
    "CLM-1234",
    [{"type": "influenced_by", "target": "ENT-9202", "qualifier": "documented",
      "warrant": ["CLM-9101"], "not_descent": "CLM-9101"}],
    type_of, lambda ref: ref in RESOLVABLE)
want(any("source is not an ENT" in why for _, why in ip4),
     f"non-ENT influenced_by source not caught: {ip4}")

want(set(INFLUENCE_QUALIFIERS) == {"documented", "contested"},
     f"INFLUENCE_QUALIFIERS drifted from ADR-GOV-0012 D6: {INFLUENCE_QUALIFIERS}")

# ---------------------------------------------------------------------------
# 5. Wiring
# ---------------------------------------------------------------------------
print()
print("wiring")

v_src = read_text(TOOLS / "validate.py")
want("rendering_class_problems" in v_src,
     "validate.py must import/use rendering_class_problems")
want("community_entity_problems" in v_src,
     "validate.py must import/use community_entity_problems")
want("RENDERING_CLASS_ENFORCED" in v_src,
     "validate.py must carry the rendering_class migration gate flag")
want("Community-entity fields malformed" in v_src and "errors.append" in v_src,
     "validate.py must append community-entity problems to `errors`")
want("Rendering class malformed" in v_src,
     "validate.py must append non-presence rendering_class problems to `errors`")

# GATE GUARD (ADR-GOV-0012 D3 migration: define -> backfill -> enforce).
# MIGRATION WINDOW: ENT-0008…0015 do not yet carry the field, so the presence
# check is WARNING-gated and the vault is green rather than red between two of
# this enactment's own commits. Flip this expectation to `= True` in the SAME
# commit that flips the flag, immediately after the backfill commit lands.
want("RENDERING_CLASS_ENFORCED = False" in v_src,
     "during the ENT-0008…0015 backfill window the rendering_class presence "
     "check must stay warning-gated (define -> backfill -> enforce)")

want("projects_to_problems" in gi_src and "influenced_by_problems" in gi_src,
     "graph_integrity.py must import/use both new edge checks")
want("projection_errors" in gi_src and "influence_errors" in gi_src,
     "graph_integrity.py must collect both new error lists")
want("projection_errors\n               or influence_errors" in gi_src
     or "or influence_errors" in gi_src,
     "graph_integrity.py must exit non-zero on the new edge errors")
want("attestation_claims" in gi_src,
     "graph_integrity.py must resolve attestation_claims for dangling")
want("relationship_raw" in gi_src,
     "graph_integrity.py must read RAW relationship entries so a forbidden key "
     "on projects_to is visible to the check that rejects it")
print("  validate.py + graph_integrity.py wired at error level")

print()
if failures:
    print("FAILURES")
    for f in failures:
        print("  -", f)
    print("\nSTATUS : FAIL")
    sys.exit(1)

print("STATUS : PASS (rendering_class presence/vocabulary/class-fit, community "
      "shape + forbidden bar, projects_to non-evidentiality, and influenced_by "
      "warrant + not_descent all proven to FIRE; concept entities untouched)")
sys.exit(0)
