# RELATIO — TRANSFER BRIEF STANDARD
### Working convention for the claude.ai support surface

**Status.** This is a DESCRIPTIVE working convention, not a governed vault
object. It has no identifier, no version in the Registry, and no authority over
the vault. It captures the brief-writing practice developed across ~15 briefs
(2026-07-20 → 2026-07-23) so a new support-surface chat can write briefs to the
same standard instead of re-deriving it. Adjust it freely; it describes craft,
not law.

---

## 1. WHERE A BRIEF SITS IN THE WORKFLOW

```
claude.ai support surface (design + governance)
        │  drafts a TRANSFER BRIEF as a .txt in /mnt/user-data/outputs/
        ▼
owner pastes it into a FRESH Claude Code session
        │  Claude Code executes against the vault, commits, pushes
        ▼
owner pastes the EXECUTION REPORT back to the support surface
        │  support surface reviews, updates memory pointers, drafts the next brief
        ▼
                        (repeat)
```

Two hard boundaries this workflow assumes:

- **The vault is truth.** The support surface may clone the public repo
  read-only to verify state, but never writes to it. All vault writes go through
  Claude Code.
- **Owner-reserved territory.** ADRs and CON documents are HAND-AUTHORED by the
  owner. A brief may CITE them; it may never write in the Architectural
  Decisions directory. For an ADR-dependent job, the owner authors the ADR and
  pushes it FIRST; the brief then verifies its existence at Task 0.

---

## 2. NON-NEGOTIABLE SKELETON

Every brief has these parts, in this order:

```
RELATIO — CLAUDE CODE TRANSFER (SUBJECT — JOB TYPE)
Integrity rule: this brief ends with an explicit === END OF BRIEF === marker.
If absent, the transfer was truncated — stop and request a re-send.

CONTEXT (settled — do not relitigate)
  ...owner rulings, prior state, standing disciplines...

TASK 0 — Pull and preconditions
TASK 1..N — the work
OUTPUT
DO NOT
=== END OF BRIEF ===
```

The integrity marker exists because long briefs get truncated in transit. The
`DO NOT` block exists because it is where most of the real safety lives — see §6.

---

## 3. TASK 0 — THE STANDARD PRECONDITION BLOCK

Nearly identical every time. Adapt the specifics; keep the shape.

```
TASK 0 — Pull and preconditions
git pull. Tree clean (the benign .claude/settings.json may remain uncommitted;
do not commit it). validate.py PASS at error level; graph_integrity.py 0
dangling, 0 branch errors. [Job-specific state checks.] Verify against the
Identifier Registry: [expected next identifiers] — the REGISTRY WINS; report the
values used. If any check fails, STOP.
```

Rules embedded there, each learned the hard way:

- **The Registry wins over the brief's figures.** Always state expected values
  AND instruct verification. A brief's numbers are a convenience, never an
  authority.
- **STOP on precondition failure.** Never let an agent proceed past a failed
  precondition "to be helpful."
- **The benign `settings.json`** is a permanent uncommitted local file. Name it
  every time or an agent will try to tidy it.
- **Known-vs-discovered.** If a number is known (e.g. an owner-authored ADR just
  pushed), say so explicitly: "number KNOWN = 0011 — verification, not
  discovery." This closes the failure mode where an agent finds *some* ADR and
  proceeds with the wrong one.

---

## 4. STANDING DISCIPLINES TO RESTATE IN EVERY RELEVANT BRIEF

These do not live in the agent's head. If a brief needs one, it states it.

**Provenance and derivation**
- DERIVE FROM THE RECORD, NOT FROM THE BRIEF. Where a brief offers guidance
  values (dates, bounds, grades), instruct the agent to derive them from the
  authoritative record and state: *the record wins on any discrepancy; report
  it.* This has caught real errors (Manichaeism's end date).
- Do not assert a source from model memory without disclosing that; do not
  invent authors, titles, or editions — verify and disclose, or record the gap.
- Do not paraphrase untranslated material from model knowledge.

**Commit hygiene (the graph must validate at every boundary)**
- Backfill BEFORE flipping enforcement on. Never leave the vault red between
  commits.
- Entities and their warranting claims land in the SAME commit — no edge ever
  precedes its warrant in history.
- Interactive/long jobs commit in small batches so an interruption leaves a
  clean, resumable state.

**Testing**
- PROVE THE POSITIVE (house convention): every new check gets a fixture proving
  it FIRES, not merely that the vault passes. This convention has caught at
  least three real bugs (YAML float coercion, PyYAML date parsing, a
  false-positive in the coherence checker).

**Scale and epistemics**
- Native Level N (Label) is the ONLY on-record confidence vocabulary. No H-band,
  no ★ in any frontmatter or grading field (prose only, where permitted).
- Split confidence is a LIST and is NEVER averaged.
- Everything lands R0 unless a verification pass says otherwise; findings are
  NOT cleared for external reliance regardless of closure.
- No grade is RAISED without explicit Critical Reviewer justification.

**Tooling**
- Extended-length path handling (STD-0001 §8) is mandatory for all vault tooling.
- Views must never render attribution (ADR-GOV-0011 selective-visibility).

**Currency**
- Run the D3 / CLAUDE.md currency check at close-out. Name the specific stale
  assertions you expect (closure-state bullets, counts, "next" pointers).
- The Registry's "Next: ADR-GOV-####" pointer goes stale every time the owner
  hand-authors an ADR. Instruct the agent to check and close it.

**Ambiguity**
- Always end DO NOT with: *If ambiguous, execute the unambiguous tasks and
  report the ambiguity.* Never let an agent guess silently, and never let it
  stall entirely on one unclear item.

---

## 5. BRIEF TYPES AND THEIR SHAPES

**A. Investigation scaffold (brief 1 of 2)**
Opens the INV record only. Creates NO claim, entity, edge, or finding
(STD-0006 §7.6 independence: the session that opens a scaffold does not fill
it). Contains: the primary RQ verbatim (marked *authoritative pending owner
freeze*), the claim decomposition mandate with per-claim required elements,
§2 scope/disambiguation disciplines, §3 method with any operative rule stated
as a blockquote, §7 acceptance criteria, §8 relationships (prose only — D4
forbids frontmatter references to non-existent objects), §9 revision row.
**The RQ freeze happens at the owner's review of the scaffold report**, before
the circuit brief is drafted.

**B. Circuit + conditional closure (brief 2 of 2)**
Runs the full OPS-0003 circuit: Specialist (ROLE-0002) → Critical Reviewer
(ROLE-0004) → Knowledge Architect (ROLE-0001) → record update → conditional
closure → registry/backlog/currency/views. Closure is pre-authorized on FOUR
conditions, stated every time:

> (a) all acceptance criteria genuinely met; (b) verdict Conformant, or
> Conformant with Flags with all flags remediated in-session; (c) no confidence
> level raised without reviewer justification; (d) both validators clean.
> If ANY condition fails: do not close; precise STATUS note; report.
> **Non-closure is legitimate.**

**C. Prep brief** — source cataloguing (ADR-GOV-0003 pattern: catalog only,
grade nothing), template refresh, small schema work. Keep source bases TIGHT
(~6–9 records); over-cataloguing is scope creep.

**D. ADR enactment brief** — the owner hand-authors the ADR first; the brief
verifies it exists and Adopted, then enacts its decisions mechanically across
standards, tooling, records, registry, backlog.

**E. Tooling build** — read-only-over-the-vault generators, validators, queue
tools. State what it may read, what it may never write, and the fixtures that
must prove each new behaviour.

**F. Migration** — schema change plus corpus backfill. Sequence is always:
define → backfill → THEN enforce. Warning-gate the check until the backfill
lands, or the vault goes red on records that are merely awaiting migration.

**G. Interactive brief** — for work needing per-record human judgment. Split it:
auto-fill the mechanical majority in one committed batch, then walk the owner
through the genuine judgment cases one at a time, committing every ~5. Include
an ESCALATION VALVE: if an auto-fill record turns out to need judgment, the
agent adds it to the interactive queue rather than guessing. (This caught 17
records the pre-classification missed.)

---

## 6. WRITING PRINCIPLES (the judgment, not the format)

**Fence the failure modes you can predict.** Before writing DO NOT, ask: what is
the most plausible wrong thing a capable agent might do here, in good faith?
Name it. Examples that earned their place:
- "Do not draw a `branches_from` edge to make the timeline connect."
- "Do not use `disputed` to hedge for influence."
- "Do not let self-understanding settle the historical question, or dismiss it."
- "Do not enforce the check before the backfill commit lands."

**Pre-authorize honest negative outcomes.** An agent under implicit pressure to
produce a positive result will produce one. So state plainly, where applicable:
a thin base is legitimate; UNSOURCED is recordable; a no-edge outcome is a
completed finding; non-closure is legitimate; a negative result on a stress-test
is a real result and is recorded as one.

**Owner rulings go in CONTEXT, marked "settled — do not relitigate."** This
prevents an agent re-opening decided questions and burning a session on them.

**State operative rules as blockquotes in §3.** Rules that must govern
judgment (edge-restraint, classification-evidence, warrant, layer-inheritance)
read better and survive better as a quoted rule than as prose.

**Reserve a section for reflexive findings** on any job that could produce
recommendations about Relatio's own structure. Recommendations route to the
Governance Backlog per ADR-GOV-0007 §3; they are NEVER self-applied in session.

**Ask for the report you need to review.** The OUTPUT block should enumerate
exactly what you will check: per-edge warrant verdicts, the exception list, the
counts that must reconcile, the specific judgment calls you want surfaced.

**Never put a placeholder inside a code block.** If a value is unknown, ask for
it or give a discovery command first (standing owner rule).

---

## 7. SKELETON TO ADAPT

```
RELATIO — CLAUDE CODE TRANSFER (SUBJECT — JOB TYPE)
Integrity rule: this brief ends with an explicit === END OF BRIEF === marker.
If absent, the transfer was truncated — stop and request a re-send.

CONTEXT (settled — do not relitigate)
[Prior state + commit refs. Owner rulings. Standing disciplines this job needs.
 What is explicitly OUT of scope and why. Date all rows with the ACTUAL
 execution date.]

TASK 0 — Pull and preconditions
[Standard block per §3, plus job-specific state checks and identifier
 verification. STOP on failure.]

TASK 1..N — [the work, one coherent unit each]

TASK N+1 — Verification and close-out
[validate.py at error level; graph_integrity.py; test suites; view regeneration
 if relevant; D3 + CLAUDE.md currency with the specific stale items named;
 Registry version bump + history row; Backlog only if genuinely affected.]

OUTPUT
One report: [enumerate exactly what must be reported, including the judgment
 calls you intend to review]. Commit logically ([ordering constraint]), push —
 standing authorization covers this session. Then STOP.

DO NOT
- [predicted failure modes, named specifically]
- Do not write in the Architectural Decisions directory (owner-reserved).
- Do not touch the Architecture Baseline or closed research content.
- If ambiguous, execute the unambiguous tasks and report the ambiguity.
=== END OF BRIEF ===
```

---

## 8. ANTI-PATTERNS (each of these actually happened)

- **Trusting the brief's identifier figures.** Always instruct Registry
  verification. Numbers move between sessions.
- **Transcribing values through the support surface.** Values that inherit
  confidence from a vault record must be derived AT EXECUTION from that record,
  never copied into the brief by the drafter.
- **Referencing an artifact that does not exist.** A precondition once cited
  "in-repo verification-channel evidence" that lived only on the support
  surface. The agent correctly searched, found nothing, and flagged it. Check
  that every referenced artifact is actually in the vault.
- **Asserting a backlog pointer an ADR promised but nobody created.** If an ADR
  says "Inline pointer: Governance Backlog," some session must create the entry.
- **Enforcing before backfilling.** Turns the vault red mid-sequence.
- **Sweep-editing pinned version citations.** Fixing a citation bumps the citing
  record, which re-invalidates the citation. Use the going-forward convention
  instead (cite standards without a version unless load-bearing).
- **Assuming a scaffold's working hypotheses are conclusions.** State that
  hypotheses are TESTED, not assumed. Two have now been overturned by evidence.

---

## 9. THE POSTURE THAT MAKES THIS WORK

A brief is not a script; it is a contract with a capable agent about what
counts as done, what counts as honest, and what must never happen. Write the
constraints that protect the vault's integrity, state the outcomes you are
willing to accept including the disappointing ones, ask for the evidence you
intend to check — and leave the judgment inside those bounds to the agent.
Every genuinely good result in this project came from an agent exercising
judgment inside well-drawn fences, including the results that overturned what
the brief expected.

---
**END — TRANSFER BRIEF STANDARD**
