---
title: OPS-0003 - Research Workflow
document_type: Operations Document
version: 1.4
status: Adopted
operational_status: Active
created: 2026-07-09
parent_documents:
  - KOS-0008 Research Methodology & Investigation Framework
  - KOS-0012 Knowledge Object Model
  - STD-0006 Review & Validation Standard
related_documents:
  - ROLE-0001 Knowledge Architect
  - ROLE-0002 Research Specialist
  - ROLE-0004 Critical Reviewer
  - ROLE-0005 Vision Steward
  - OPS-0001 Knowledge Base Organization
  - OPS-0002 Relationship Integrity & Graph Maintenance
tags:
  - ProjectRelatio
  - Operations
  - ResearchWorkflow
  - Roles
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-09
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# OPS-0003

# Research Workflow

## Version 1.4
## Adopted Operations Document

---

# 1. Purpose

This is the **operating procedure of Project Relatio's actual purpose**: turning a research question into thorough, disciplined, evidenced knowledge.

It is not theory. It is the distilled procedure of three completed investigations (INV-0001 Jesus/Daoism, INV-0002 phantom traffic jams, INV-0003 wu wei), formalised so the next question runs the same disciplined circuit.

---

# 2. Scope Guardrail (reframed — ADR-GOV-0002)

> Project Relatio's purpose is to conduct thorough and disciplined research on the owner's questions, **and** to become an excellent knowledge architecture in the process — both are legitimate aims, the research primary.

Every step below **earns its place on its merits** — by making research **better** or improving the system's ability to produce good answers — judged by *use*, not by symmetry or completeness, and **by merit regardless of which contributor proposes it**. A step that adds ceremony without catching a real failure is removed; but a step that genuinely improves the work is not suppressed to stay minimal. *(This replaces the earlier framing that treated architecture-building as a risk to defend against; see ADR-GOV-0002.)*

---

# 2.1 Proportionality — Tier by Stakes

The full circuit is rigorous but resource-intensive (Fourth-Run Assessment F-14). Not every question needs it. The coordinator triages by stakes:

- **Full circuit** — Specialist → *independent* Critical Reviewer → Knowledge Architect → external-verification gate — for **high-stakes / externally-consequential** questions: health, safety, financial, public-facing, or anything a person will act on. (RQ-0004 was correctly full-circuit.)
- **Lean path** — Specialist + a structured **self-red-team** + the **automated structural check** — for exploratory, internal, or low-consequence questions.

**Rule: default to the full circuit whenever the stakes are uncertain.** Triage is cheap; under-reviewing a consequential question is not. **Independence is never waived on high-stakes work** — the Specialist never certifies its own high-stakes conclusions, and STD-0006 §7.5 still gates reliance on verification strength.

*(The lean path is used on demand. A fuller build-out of tiering awaits demonstrated need — GB-2026-013 — and is deliberately not over-built on a single data point.)*

---

# 3. The Workflow

```
[Vision Steward ROLE-0005 / Owner]  poses a research question
   │
   ▼
[Vision Steward + main session]  intake, triage, assign INV-NNNN from the Identifier Registry
   │
   ▼
[Specialist ROLE-0002]
   1. Refine & scope the question  (disambiguate terms, corpora; state the rationale)
   2. Sources        → SRC records   (KOS-0003 §6 evaluation; state what each does NOT establish)
   3. Claims         → CLM records   (type, evidence, 0–5 grading, assumptions, reasoning, confidence,
                                      limitations, alternatives — KOS-0003 §12)
   4. Entities       → ENT records   (where a concept is load-bearing or cross-investigation)
   5. Synthesis      → FND records   (integrate claims; never exceed the weakest necessary link)
   │
   ▼
[Critical Reviewer ROLE-0004]  independent epistemic challenge
   reasoning risks → evidence grading → confidence calibration
   → assumptions → steelmanned alternatives → motivated-reasoning check
   Verdict: Conformant | Flagged | Blocked   (STD-0006 §7)
   │
   ├── Flagged/Blocked ──► back to Specialist: revise, defend with evidence, or LOWER confidence
   │                        (disputes → Coordinator arbitrates process, or escalates to Owner)
   ▼
[Knowledge Architect ROLE-0001]  structural validation
   conformance (STD-0001/0002/0003/0005/0007) + graph integrity (OPS-0002) + placement (OPS-0001)
   │
   ▼
[Coordinator]  completeness check → friction/convergence assessment → Owner
```

---

# 3.1 Workflow Refinements (v1.2)

- **Review-targeting handoff.** The Specialist ends by naming its weakest claims, what it could not verify, and its most contestable calls (as it did in RQ-0004). The Critical Reviewer uses this brief to focus its expensive verification on the genuinely uncertain points instead of re-deriving everything — sharper *and* cheaper, without reducing coverage.
- **Reviewer and Architect run in parallel.** Epistemic review (ROLE-0004) and structural/graph validation (ROLE-0001) are independent — they check different things — so they run concurrently after the Specialist finishes, shortening the critical path and reducing the risk of an interrupted run.
- **Structural validation is automated.** The Knowledge Architect runs `tools/graph_integrity.py` (OPS-0002 §6) for dangling-reference and reciprocity checks and adjudicates its output, rather than tracing links by hand. Mechanical validation no longer costs manual effort — an agent's judgment is spent only on what the tool flags.

---

# 4. Non-Negotiables

1. **No conclusion bypasses the epistemic pipeline** (KOS-0003 §2).
2. **The Specialist does not certify its own work.** Independent review is structural, not optional.
3. **Confidence only moves down under review.** Raising it requires new evidence.
4. **A synthesis is never more confident than its weakest necessary claim.**
5. **No investigation completes with an unresolved Blocked verdict.**
6. **Alternatives are steelmanned before rejection.**
7. **What cannot be settled is bracketed and said so** (historicity, metaphysics, contested scholarship).

---

# 5. Artefacts Produced

| Step | Object | Template | Placement (OPS-0001) |
|---|---|---|---|
| Investigation | INV | TPL-0003 | `06 Knowledge Base/INV-NNNN - …/` |
| Sources | SRC | TPL-0002 | `06 Knowledge Base/Sources/` |
| Claims | CLM | TPL-0001 | investigation folder |
| Entities | ENT | *(none yet — hand-author from KOS-0012 §5.5)* | `06 Knowledge Base/Entities/` |
| Findings | FND | TPL-0004 | investigation folder |
| Assessment | Review Report | — | investigation folder |

Identifiers are drawn from and recorded in the **Identifier Registry**.

---

# 6. Implementation (RRI) — Roles as Claude Code Agents

The Roles layer is **platform-independent architecture (RKA)**. In this Obsidian/Claude Code reference implementation (RRI), three roles are implemented as Claude Code subagents in `.claude/agents/`:

| Role (RKA) | Agent (RRI) |
|---|---|
| ROLE-0002 Research Specialist | `research-specialist` |
| ROLE-0004 Critical Reviewer | `critical-reviewer` |
| ROLE-0001 Knowledge Architect | `knowledge-architect` |

Coordination (intake, sequencing, completeness) is performed by the **Vision Steward (ROLE-0005) and the main session** orchestrating the agents — not by a separate agent or role. The former ROLE-0003 Coordinator was retired for adding ceremony without warrant (ADR-GOV-0001).

**The separation matters:** the role definitions govern *what the function is and may decide*; the agent files govern *how it is invoked on this platform*. Changing agents does not change the architecture; changing a role's authority requires owner ratification (ROLE-0001 §4.2).

---

# 7. Relationship to Other Documents

Roles: ROLE-0001…0004. Object model: KOS-0012. Epistemics: KOS-0003. Methodology: KOS-0008. Validation: STD-0006. Placement: OPS-0001. Graph: OPS-0002.

---

# 8. Revision History

|Version|Date|Status|Description|
|---|---|---|---|
|1.0|2026-07-09|Adopted|Initial research workflow, distilled from three completed investigations; defines the role circuit and the RKA→RRI agent mapping|
|1.1|2026-07-09|Adopted|Governance assessment: rerouted coordination from the retired ROLE-0003 to the Vision Steward (ROLE-0005) and the main session (ADR-GOV-0001)|
|1.2|2026-07-10|Adopted|Efficiency refinements from the first agent-circuit run (RQ-0004): §2.1 proportionality/tiering by stakes; §3.1 review-targeting handoff, parallel Reviewer∥Architect, and automated structural check (`tools/graph_integrity.py`). Owner-authorized; ADR waived by owner. Full tiering build remains trigger-gated (GB-2026-013).|
|1.3|2026-07-11|Adopted|§2 Scope Guardrail reframed per **ADR-GOV-0002**: architecture-building is a legitimate concurrent aim (not a risk to defend against); additions judged by merit/use regardless of source; warranted work is not suppressed to stay minimal. (Also fixed a stale `## Version` heading that read 1.1.)|
|1.4|2026-07-22|Adopted|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

---

# End OPS-0003
