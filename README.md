# Project Relatio

**A knowledge architecture for conducting thorough, disciplined, evidence-graded research — not a note-taking system.**

Project Relatio treats knowledge as *a structured network of meaningful relationships, not a collection of stored information*. Its purpose is concrete: to answer real research questions rigorously, with every claim graded for evidence, every conclusion independently challenged, and nothing fabricated.

This repository is the **Relatio Reference Implementation (RRI)** — the [Obsidian](https://obsidian.md) vault that implements the platform-independent **Relatio Knowledge Architecture (RKA)**.

---

## What makes it unusual

- **Knowledge Objects, not notes.** Every unit — an Investigation (INV), Source (SRC), Claim (CLM), Entity (ENT), or Finding (FND) — is a typed object with structured metadata and a defined lifecycle.
- **Relationships carry meaning.** Objects connect through a controlled vocabulary (`derived_from`, `supports`, `contrasts_with`, `part_of`, …), not bare links. The graph *is* the knowledge; the folders are only classification.
- **Evidence is graded, honestly.** Every claim is scored on a canonical confidence scale — `Level N (Label)`, from 0 (Unsupported) to 5 — and a synthesis is never more confident than its weakest necessary claim. **Level 5 is reserved.**
- **An adversarial research circuit.** No conclusion is self-certified. Each investigation runs:

  > **Research Specialist** (builds it) → **Critical Reviewer** (independently attacks it) → **Knowledge Architect** (validates its structure)

  The reviewer issues a Conformant / Flagged / Blocked verdict, checks for motivated reasoning in *both* directions, and gates health/high-stakes findings from external reliance until independently re-verified.
- **Anti-fabrication is a first principle.** Inventing a source, citation, statistic, or DOI is the one unrecoverable failure. Figures are asserted only at the precision actually verified.
- **Governed evolution.** The architecture changes only through recorded governance decisions — never spontaneous restructuring — and its core concepts are deliberately *frozen* (see the Architecture Baseline) against over-design.

---

## What's in here

The vault lives under [`Project Relatio/`](./Project%20Relatio) and is organised in layers (folders are classification only — the real structure is the relationship graph):

| Layer | Folder | What it holds |
|---|---|---|
| **Constitution** | `00 Constitution/` | Vision, principles, governance & epistemic charters (CON-0001…0004) |
| **Kernel** | `01 KOS/01 Kernel/` | The conceptual foundation — epistemology, ontology, relationship & systems modelling, the Knowledge Object Model (KOS-0001…0012) |
| **Standards** | `01 KOS/02 Standards/` | The 7 operating standards — naming, metadata, classification, relationships, lifecycle, review, terminology (STD-0001…0007) |
| **Roles** | `01 KOS/03 Roles/` | The four active roles of the research circuit (ROLE-0001/0002/0004/0005) |
| **Templates** | `01 KOS/04 Templates/` | Object templates (Claim, Source, Investigation, Finding, ADR) |
| **Operations** | `01 KOS/05 Operations/` | The research workflow, identifier registry, governance backlog, standing authorizations, architecture baseline |
| **Knowledge Base** | `01 KOS/06 Knowledge Base/` | The actual research — investigations and their sources, claims, entities, findings |

### The research so far

Six investigations have been run end-to-end through the full circuit, spanning very different domains — a deliberate stress test of the architecture:

1. **INV-0001** — Convergence and divergence between the teachings of Jesus and Daoism
2. **INV-0002** — Phantom traffic jams (emergent instability, not bottlenecks)
3. **INV-0003** — *Wu wei* (non-forcing action)
4. **INV-0004** — Type-2-diabetes remission and safe metformin de-prescribing
5. **INV-0005** — Durable interventions for chronic stress
6. **INV-0006** — Why people abandon wellness interventions, and what best sustains them

> The clinical and behavioural investigations (INV-0004/0005/0006) are **educational evidence reviews, not medical advice**, and are gated from external/client-facing reliance pending genuine independent and clinician review.

---

## Repository layout

```
Research OS/                 ← git repository root
├── README.md                ← you are here
├── Project Relatio/         ← the RRI vault (the knowledge system itself, ~140 Markdown objects)
│   ├── 00 Constitution/
│   ├── 01 KOS/              ← Kernel · Standards · Roles · Templates · Operations · Knowledge Base · Archive
│   └── CLAUDE.md            ← orientation for AI coding sessions working in the vault
└── tools/                   ← RRI implementation tooling (not architecture)
    ├── validate.py          ← structural conformance (identifiers, metadata, uniqueness)
    ├── graph_integrity.py   ← relationship-graph integrity (dangling refs, typed reciprocity)
    └── README.md
```

**Where to start reading:** [`KOS-0001`](./Project%20Relatio/01%20KOS/01%20Kernel/00%20Foundational%20Documents) (the charter), then the **Architecture Baseline** and **Identifier Registry** under `01 KOS/05 Operations/`.

---

## Tools

The Python tooling under [`tools/`](./tools) enforces the standards (it does not define them). It requires only PyYAML:

```bash
pip install -r tools/requirements.txt
cd tools
python validate.py          # structural conformance — identifiers, metadata, uniqueness
python graph_integrity.py   # graph integrity — dangling references + typed reciprocity
```

---

## Status & nature

Project Relatio is an **evolving, single-owner research system** — a working reference implementation, not a finished product. Its standing risk is *over-architecture* (building meta-structure faster than real use can validate it), and it is deliberately steered against that: every addition must make the *research* better, not the architecture more complete. Knowledge Objects are versioned and carry a two-dimensional lifecycle (maturity × operational state); superseded and archived material is preserved, never erased.

## Rights

© 2026 Brian Noon. All rights reserved. This repository is public
for reference; see [LICENSE.md](./LICENSE.md). An open licensing model may be
considered in the future — it has not been adopted.
