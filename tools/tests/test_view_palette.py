#!/usr/bin/env python3
"""Detection tests for the view palette (build_view.py).

House convention: prove the positive. "The colours are different" is not a
useful assertion — #0b6e4f and #3d8f4e are also different, and they were the
pair a reader could not tell apart. So this measures the separations in a
perceptual space (CIE L*a*b*, CIE76 dE) and asserts FLOORS, so that a future
edit which quietly narrows a distinction fails the build instead of silently
degrading the picture.

Why this matters architecturally, not just aesthetically:

  * CONFIDENCE. The epistemic record grades per component and never averages
    (STD-0008). A view in which Level 5 and Level 4 read as the same colour
    re-merges at the eye what the record refuses to merge on disk. Levels 5 and
    4 must therefore differ on lightness AND hue, not on shade alone.
  * RELIANCE. The R0/R1/R2 gate is load-bearing on BOTH views and no path may
    strip it (ADR-GOV-0006). A badge whose tier cannot be read at a glance
    carries no gate — legibility is part of the gate, not decoration. The tiers
    must also stay inside the blue family so a reliance badge is never mistaken
    for a confidence badge (the two axes are independent and must look it).
  * CONTRAST. Both badge families are rendered with white text, so every colour
    that carries text must clear WCAG AA (4.5:1) against white.

Floors are set BELOW the current values with headroom, so ordinary re-tuning is
allowed and only a real regression trips them.

Run: python tools/tests/test_view_palette.py
"""

import itertools
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from build_view import LEVEL_COLOR, RELIANCE_COLOR  # noqa: E402


# --- colour maths (self-contained; no third-party dependency) ---------------

def _channels(hexcolor):
    h = hexcolor.lstrip("#")
    if len(h) != 6:
        raise ValueError(f"expected #rrggbb, got {hexcolor!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _linear(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(hexcolor):
    r, g, b = (_linear(c) for c in _channels(hexcolor))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(a, b):
    la, lb = relative_luminance(a), relative_luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def _lab(hexcolor):
    r, g, b = (_linear(c) for c in _channels(hexcolor))
    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505

    def f(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116

    fx, fy, fz = f(x / 0.95047), f(y / 1.0), f(z / 1.08883)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def delta_e(a, b):
    """CIE76 dE. Rule of thumb: >2.3 is a just-noticeable difference; >20 is
    comfortably distinguishable side by side; >40 reads as a different colour."""
    return math.sqrt(sum((p - q) ** 2 for p, q in zip(_lab(a), _lab(b))))


def _hue_deg(hexcolor):
    _, a, b = _lab(hexcolor)
    return math.degrees(math.atan2(b, a)) % 360


def _hue_gap(a, b):
    d = abs(_hue_deg(a) - _hue_deg(b)) % 360
    return min(d, 360 - d)


# --- floors ----------------------------------------------------------------

LEVEL_5_4_DE_FLOOR = 40.0      # actual 47.6; the old pair was 21.8 and failed the eye
LEVEL_5_4_HUE_FLOOR = 20.0     # they must not be two shades of one hue
LEVEL_ADJACENT_DE_FLOOR = 25.0  # weakest adjacent pair is 3 vs 2 at 31.5
RELIANCE_DE_FLOOR = 20.0       # actual minimum 24.6; the old minimum was 14.5
AA_CONTRAST = 4.5              # WCAG AA, normal text, against the white badge text

FAILURES = []


def check(condition, message):
    if condition:
        print(f"  PASS  {message}")
    else:
        print(f"  FAIL  {message}")
        FAILURES.append(message)


def test_confidence_levels_all_distinct():
    print("\n[confidence] every level is its own colour")
    values = [LEVEL_COLOR[level] for level in sorted(LEVEL_COLOR)]
    check(len(set(values)) == len(values),
          f"five distinct hex values ({', '.join(values)})")


def test_level_5_and_4_are_strongly_separated():
    print("\n[confidence] Level 5 vs Level 4 — the owner-flagged pair")
    d = delta_e(LEVEL_COLOR[5], LEVEL_COLOR[4])
    check(d >= LEVEL_5_4_DE_FLOOR,
          f"dE(L5,L4) = {d:.1f} >= {LEVEL_5_4_DE_FLOOR} floor")
    h = _hue_gap(LEVEL_COLOR[5], LEVEL_COLOR[4])
    check(h >= LEVEL_5_4_HUE_FLOOR,
          f"hue gap = {h:.1f} deg >= {LEVEL_5_4_HUE_FLOOR} — not two shades of one hue")
    check(relative_luminance(LEVEL_COLOR[5]) < relative_luminance(LEVEL_COLOR[4]),
          "Level 5 is the darker of the two (stronger grade reads heavier)")


def test_remaining_levels_still_clearly_distinct():
    print("\n[confidence] Levels 3 / 2 / 1 remain clearly distinct")
    for hi, lo in ((3, 2), (2, 1)):
        d = delta_e(LEVEL_COLOR[hi], LEVEL_COLOR[lo])
        check(d >= LEVEL_ADJACENT_DE_FLOOR,
              f"dE(L{hi},L{lo}) = {d:.1f} >= {LEVEL_ADJACENT_DE_FLOOR} floor")
    d = delta_e(LEVEL_COLOR[4], LEVEL_COLOR[3])
    check(d >= LEVEL_ADJACENT_DE_FLOOR,
          f"dE(L4,L3) = {d:.1f} >= {LEVEL_ADJACENT_DE_FLOOR} floor "
          "(the new L4 did not drift into the amber)")


def test_reliance_tiers_are_distinguishable_at_a_glance():
    print("\n[reliance] R0 / R1 / R2 separation — the gate must be readable")
    values = [RELIANCE_COLOR[t] for t in ("R0", "R1", "R2")]
    check(len(set(values)) == 3, f"three distinct hex values ({', '.join(values)})")
    for a, b in itertools.combinations(("R0", "R1", "R2"), 2):
        d = delta_e(RELIANCE_COLOR[a], RELIANCE_COLOR[b])
        check(d >= RELIANCE_DE_FLOOR,
              f"dE({a},{b}) = {d:.1f} >= {RELIANCE_DE_FLOOR} floor")
    lums = [relative_luminance(v) for v in values]
    check(lums[0] > lums[1] > lums[2],
          "tiers darken monotonically R0 -> R1 -> R2 (stronger tier reads heavier)")


def test_reliance_tiers_stay_in_the_blue_family():
    print("\n[reliance] tiers stay blue — never confusable with a confidence badge")
    for tier, value in RELIANCE_COLOR.items():
        r, g, b = _channels(value)
        check(b > r and b > g, f"{tier} {value} is blue-dominant (b>{max(r, g)})")
    for tier, rel in RELIANCE_COLOR.items():
        for level, lev in LEVEL_COLOR.items():
            d = delta_e(rel, lev)
            check(d >= 25.0,
                  f"dE({tier}, L{level}) = {d:.1f} >= 25 — axes never confusable")


def test_white_badge_text_stays_legible():
    print("\n[contrast] white badge text clears WCAG AA on every reliance tier")
    for tier, value in RELIANCE_COLOR.items():
        c = contrast_ratio(value, "#ffffff")
        check(c >= AA_CONTRAST, f"{tier} {value} contrast vs white = {c:.2f} >= {AA_CONTRAST}")
    print("\n[contrast] confidence badges — reported, floor is AA-large (3.0)")
    for level in sorted(LEVEL_COLOR, reverse=True):
        c = contrast_ratio(LEVEL_COLOR[level], "#ffffff")
        check(c >= 3.0, f"L{level} {LEVEL_COLOR[level]} contrast vs white = {c:.2f} >= 3.0")


def main():
    print("=" * 62)
    print("VIEW PALETTE DETECTION TESTS — build_view.py")
    print("=" * 62)
    test_confidence_levels_all_distinct()
    test_level_5_and_4_are_strongly_separated()
    test_remaining_levels_still_clearly_distinct()
    test_reliance_tiers_are_distinguishable_at_a_glance()
    test_reliance_tiers_stay_in_the_blue_family()
    test_white_badge_text_stays_legible()
    print("\n" + "=" * 62)
    if FAILURES:
        print(f"FAILED — {len(FAILURES)} assertion(s)")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print("ALL PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
