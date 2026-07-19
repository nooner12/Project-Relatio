---
title: CLM-0031 - Constraints as Targets Get Gamed
document_type: Claim Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-12
category:
  - Knowledge Base
  - Claim
  - Measurement and Incentives
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0007 Formal Constraints in Knowledge Systems
related_documents:
  - SRC-0040 Campbell 1979 Assessing the Impact of Planned Social Change
  - SRC-0043 Merton 1940 Bureaucratic Structure and Personality
  - FND-0007 Value and Failure of Formal Constraints
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - CampbellsLaw
  - GoalDisplacement
relationships:
  - type: derived_from
    target: SRC-0040
  - type: derived_from
    target: SRC-0043
  - type: supports
    target: FND-0007
  - type: part_of
    target: INV-0007
---

# CLM-0031

# When a Formal Constraint or Metric Becomes a Target, It Is Gamed and Displaces the Goal It Was Meant to Serve

## Draft Claim Record

---

# Claim
> A characteristic **failure mode** of formal constraints is **metric gaming / goal displacement**: when a quantitative indicator or formal rule is turned into a **target for control or high-stakes decisions**, actors optimise the measured proxy rather than the underlying goal, **corrupting both the measure's validity and the process it was meant to improve** (Campbell's Law; Merton's "goal displacement"). The more consequential the metric, the stronger the corruption pressure.

---

# Claim Type (KOS-0003 §3)
**Causal** (making a metric a high-stakes target → gaming/goal displacement), stated as a **descriptive regularity**.

---

# Evidence (KOS-0003 §4)
Type: **Historical/observational (illustrative) + theoretical**, broadly corroborated across domains.
- **SRC-0040 (Campbell 1979):** "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor" — illustrated with test scores, crime statistics, etc.
- **SRC-0043 (Merton 1940, "Bureaucratic Structure and Personality"):** **goal displacement** — rule-following becomes an end in itself, displacing the organization's objectives — plus **trained incapacity** (disciplined routines become blind spots under changed conditions). Catalogued in remediation as the anchor for the goal-displacement half of the claim.
- Cross-domain corroboration (widely reported; not separately catalogued): high-stakes educational testing, healthcare wait-time targets, policing quotas — repeatedly show the pattern.

---

# Evidence Evaluation (KOS-0003 §5, 0–5)
- **Reliability: 4** — Campbell is authoritative; the regularity is broadly corroborated across sectors.
- **Relevance: 5** — directly names a core failure mode of formal metrics/rules.
- **Independence: 3** — two catalogued anchors (Campbell for gaming, Merton for goal displacement), but they are **complementary halves of the claim**, not independent confirmation of one proposition; cross-domain corroboration remains uncatalogued. Level 3 holds.
- **Quality: 3** — the 1979 anchor is illustrative, not a quantified measurement of gaming rates; corroboration is distributed across many later studies not individually verified here.
- **Limitations:** Establishes a **tendency**, not a deterministic law or an effect size; strongest for **high-stakes** metrics — low-stakes formal measures are less affected.

---

# Consensus (KOS-0003 §9)
- Evidence strength: **Moderate-to-High** (a robust, repeatedly observed regularity).
- Consensus strength: **High** — Campbell's Law / Goodhart's Law / goal displacement are widely accepted across the social sciences and management.
- Relationship: strongly supported as a tendency; contested only at the edges (magnitude, boundary conditions).

---

# Source Evaluation
SRC-0040: high authority, high transparency, academic. Campbell's Law formulation and citation verified this session. Merton's goal-displacement companion is invoked from the standard literature, not separately catalogued (recorded limitation).

---

# Assumptions (KOS-0003 §10)
- **Ontological:** actors respond to incentives created by measurement — strongly supported.
- **Methodological:** the social-indicator finding extends to knowledge-system metrics (e.g., counts of objects, link density, "coverage") — an explicit analogical assumption.

---

# Reasoning (KOS-0003 §7)
**Inductive from converging cases.** Across independent domains, making a proxy a high-stakes target produces gaming; the regularity generalises. **Risks checked:** *overgeneralisation to a deterministic law* (named — it is a tendency, strongest at high stakes); *false precision* (no effect size asserted); *confirmation bias* (guarded — this is an inconvenient failure mode for any metric-driven system and is retained).

---

# Confidence (KOS-0003 §8)
**Level 3 (Moderate)** that formal metrics/rules used as high-stakes targets are gamed and displace their goals. Graded Moderate rather than High because the catalogued anchor is illustrative (not a quantified study), boundary conditions matter (stakes-dependent), and the strong cross-domain corroboration is invoked rather than individually catalogued here. The *directional* pattern is close to consensus; the grade reflects evidential cataloguing and magnitude uncertainty, not doubt about the tendency.

---

# Limitations
- A tendency, not a deterministic law; magnitude unquantified.
- Strongest for high-stakes metrics; weaker for low-stakes/diagnostic ones.
- Single catalogued primary source; cross-domain support invoked.

---

# Alternative Interpretations
1. **"Better-designed metrics (baskets, hard-to-game indicators) avoid this."** Steelmanned and partly conceded — design mitigates gaming — but does not eliminate the pressure; feeds CLM-0033 (design/governance) rather than refuting the failure mode.
2. **"Gaming reflects bad actors, not the metric."** Rejected as primary — Campbell's point is that the *pressure* is created by the high-stakes use itself, largely independent of actor virtue.

---

# Relationships (STD-0004)
- `derived_from` SRC-0040 (gaming / Campbell's Law), SRC-0043 (goal displacement / Merton).
- `supports` FND-0007.
- *(Conceptually adjacent to CLM-0030 on decoupling — a sibling appearance-vs-reality distortion; left as prose only, not asserted as a typed `related_to` edge, per "use related_to sparingly," STD-0004.)*
- `part_of` INV-0007.

---

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-12|Draft|Created for RQ-0007. Campbell's Law formulation verified this session; Merton goal-displacement companion invoked not catalogued. Level 3 — robust directional tendency, illustrative anchor, stakes-dependent boundary condition.|
|0.2|2026-07-12|Draft|Post-review remediation (Critical Review - RQ-0007, #6): catalogued Merton 1940 (SRC-0043) as the goal-displacement anchor (previously an uncatalogued invocation); noted Campbell and Merton are complementary halves, not independent confirmation, so Independence 3 holds. #9: de-asserted the prose-only `related_to CLM-0030`. Title shortened (STD-0001 §10). No confidence change — remains Level 3.|

# End CLM-0031
