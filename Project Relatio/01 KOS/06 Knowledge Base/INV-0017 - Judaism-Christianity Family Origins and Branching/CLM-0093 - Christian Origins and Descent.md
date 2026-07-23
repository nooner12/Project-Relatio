---
title: CLM-0093 - Christian Origins and Descent
document_type: Claim Record
version: 0.2
status: Draft
operational_status: Active
created: 2026-07-22
category:
  - Knowledge Base
  - Claim
  - Judaism and Christianity
parent_documents:
  - KOS-0003 Epistemic Framework & Knowledge Validation System
  - INV-0017 Judaism-Christianity Family Origins and Branching
related_documents:
  - SRC-0140 Dunn The Partings of the Ways
  - SRC-0139 Boyarin 2004 Border Lines
  - SRC-0141 Becker Reed The Ways That Never Parted
  - SRC-0103 New Testament Primary Texts Pauline Letters and Gospels
  - CLM-0058 Nazarene Inheritance from Second Temple Apocalypticism
  - CLM-0068 Dating of the Undisputed Pauline Letters
  - CLM-0075 Existence of Jesus as a Historical Figure
  - CLM-0076 Crucifixion under Pontius Pilate
  - FND-0017 Origins and Branching of the Judaism-Christianity Family
tags:
  - ProjectRelatio
  - KnowledgeBase
  - Claim
  - Christianity
  - JudaismChristianity
relationships:
  - type: derived_from
    target: SRC-0140
  - type: derived_from
    target: SRC-0139
  - type: derived_from
    target: SRC-0141
  - type: derived_from
    target: SRC-0103
  - type: depends_on
    target: CLM-0058
  - type: depends_on
    target: CLM-0068
  - type: depends_on
    target: CLM-0075
  - type: depends_on
    target: CLM-0076
  - type: supports
    target: FND-0017
  - type: part_of
    target: INV-0017
confidence:
  - component: emergence_dating
    level: 4
    label: High
  - component: descent_from_second_temple_judaism
    level: 4
    label: High
  - component: schism_qualifier_fit
    level: 3
    label: Moderate
reliance_tier: R0
reliance_note: "verification-light review; not cleared for external reliance"
review_cycle: 9
review_date: 2027-04-22
last_reviewed: 2026-07-22
attribution:
  - actor: Brian Noon
    role: Vision Steward
    event: created
    date: 2026-07-22
    ai_degree: ai-delegated
    ai_model_family: Claude
---

# CLM-0093

# Christian Origins and Descent

## Draft Claim Record

---

# Claim
> **Christianity emerged as a movement within Second Temple Judaism in the first century CE** and descends from that shared Jewish matrix. Its earliest layer — the Jesus movement (the Nazarenes) — inherited its whole apocalyptic frame from Second Temple Jewish apocalypticism (**CLM-0058**, inherited, High), and its emergence is anchored by the closed first-century results: the historical Jesus's existence and execution (**CLM-0075** / **CLM-0076**, c. 30 CE) and the undisputed Pauline letters as the earliest datable Christian documents (**CLM-0068**, c. 50–60 CE). Within this family it **`branches_from` Second Temple Judaism**, qualifier **`schism`** — chosen as least-wrong for a movement that separated from its parent to become a distinct tradition — **with an explicit caveat that `schism` must not be read as a single sharp early break**: the separation ("the parting of the ways") was **gradual, late, uneven, and locally variable** (the Boyarin / Becker–Reed reading). This claim takes **no supersessionist position**: Christianity is a branch of the shared parent, not its fulfilment or replacement.

---

# Element (i) — Emergence Dating
- **First-century CE emergence, inherited (not re-derived).** The movement originates around the historical Jesus, a first-century Galilean Jew executed under Pontius Pilate c. 30 CE — **CLM-0075** (existence, Level 4/High) and **CLM-0076** (crucifixion Level 4/High; under-Pilate specification Level 3/Moderate), inherited from INV-0014. The earliest datable Christian *documents* are the seven undisputed Pauline letters, c. 50–60 CE — **CLM-0068** (Level 4/High), inherited from INV-0013, anchored externally by the Gallio synchronism. These grades are **inherited under the layer-inheritance rule (§3.1) and cited, not re-derived**; on any discrepancy the cited claim wins.
- **What "emergence" means here.** The claim dates the *movement's origin* (1st c. CE) — firmly, on inherited High-graded anchors. The *separation into a distinct tradition* (when Christianity became non-Jewish/distinct) is a **different, more contested question**, handled in elements (ii)/(iii) and not conflated with the movement's origin.
- **Disposition:** `display_range` on ENT-0013 reads "1st c. CE." The render-only `range_start_year` uses 30 (the movement's origin at the crucifixion, per CLM-0075/0076) rather than 50 (earliest documents), because the movement — not the first surviving letter — is what the tradition dates from; both anchors are inherited High. Graded **High** (Level 4): this is the one component the inherited closed anchors carry above Moderate; the parametric Jewish-studies interiors do not govern it.

# Element (ii) — Descent Relationship (+ qualifier; warrant seeded by CLM-0058)
- **Descent from Second Temple Judaism is exceptionally well-attested (High).** The earliest Jesus movement was a **Second Temple Jewish sect** that inherited its entire frame — bodily resurrection, imminent judgment, two-age periodization, angel/demon cosmology, an eschatological deliverer — **from Second Temple Jewish apocalypticism (CLM-0058, Level 4/High)**. This is a **Jewish-stream→sect inheritance**, and it is the **seed warrant** for the `branches_from` edge. That Christianity descends from Second Temple Judaism is among the most secure facts in the field; graded **High**.
- **In-family edge:** `branches_from` **ENT-0012 (Second Temple Judaism)**, qualifier **`schism`** — warranted by this claim (seed CLM-0058). The edge renders; the claim warrants.
- **Qualifier test — `schism` is least-wrong, with a sharpness caveat that is load-bearing.** Against the controlled list (`schism` / `reform` / `syncretic-descent` / `heterodox-offshoot` / `disputed`), `schism` best captures **a movement that separated from its parent to become a distinct tradition** — as opposed to `reform` (which would imply Christianity reformed/continued Judaism, false), `heterodox-offshoot` (understates that Christianity became a separate religion, not a heresy-current within Judaism), `syncretic-descent` (its later Hellenistic development is real but not its defining descent), or `disputed` (the *fact* of descent is not disputed). **But `schism` connotes a formal, datable split, and the historical separation was not that.** The "parting of the ways" was **gradual, late, uneven, and locally variable** (SRC-0139 Boyarin's "border lines drawn late from above"; SRC-0141 Becker & Reed's "ways that never [cleanly] parted"), against the classic earlier-partings model (SRC-0140 Dunn). The qualifier is retained **because it is the least-wrong available value for "separated to become distinct," with the sharpness caveat explicitly recorded** — routed to Anchor Fit as the Christianity-side note. Because of this, `schism_qualifier_fit` is graded **Moderate**, not High.
- **`tradition_type` on ENT-0013 is `emergent`.** Christianity is modelled as an emergent movement (it grew from the Jesus movement and its gradual separation), not `founded` — asserting Jesus *founded a new religion* is a contested, confession-adjacent claim that the metaphysical bracket forbids the record to assert; historically the tradition emerged. **Anchor Fit note:** a `founded` reading (Jesus, or Paul, as founder) is defensible in other framings; `emergent` chosen as least-wrong and most neutral, tension recorded.

# Element (iii) — Rival Reading (steelmanned)
- **Rival A — Christianity as a fully new religion from early on (sharp, early parting).** Steelmanned: distinctive Christology, the Gentile mission, and the abrogation of Torah-observance mark Christianity as a *new religion* almost from the start, so `schism` (a clean break) is apt and even the 1st century sees two religions. **Survives, partially** — the theological distinctives are real and early. **Cost:** the earliest movement is transparently a Second-Temple *Jewish* sect (CLM-0058), Torah-observant Jewish Christianity persisted for generations, and the "clean early break" is exactly what the revisionist literature (SRC-0139/0141) shows to be overdrawn; so this rival cannot lift the `schism` fit above Moderate — it is one pole, not the settled reading.
- **Rival B — an intra-Jewish movement that only later (and never cleanly) separated (late, gradual parting).** Steelmanned (Boyarin, Becker & Reed): the border between "Judaism" and "Christianity" was **constructed late**, largely through heresiology and rabbinic/Christian self-definition, with continued interaction into late antiquity — so `branches_from ... schism` misdescribes a boundary that was drawn from above, well after the first century. **Survives** — this is why the sharpness caveat is recorded and why `schism_qualifier_fit` is only Moderate. **Cost:** even on this reading a separation *did* occur (two traditions exist today), and `branches_from` with a recorded "gradual/late" caveat is not a claim of a datable rupture; the edge represents descent-with-eventual-separation, not a clean split. **Net:** the two rivals bracket the qualifier from opposite sides (too-sharp vs. too-late), and both costs land on the same Moderate `schism_qualifier_fit` grade.

---

# Claim Type (KOS-0003 §3)
**Descriptive / historical** — emergence and genealogical descent of a tradition; no theological claim about Jesus or Christianity is made or implied (bracketed).

# Evidence (KOS-0003 §4)
Type: **Historical.**
- Inherited (cited, not re-derived): CLM-0058 (Nazarene apocalyptic inheritance, L4), CLM-0068 (undisputed Pauline dating, L4), CLM-0075 (Jesus existence, L4), CLM-0076 (crucifixion, L4 / under-Pilate L3).
- SRC-0103 (NT primary texts): the earliest documentary layer (cited via the inherited claims; unmodified).
- SRC-0140 (Dunn), SRC-0139 (Boyarin), SRC-0141 (Becker & Reed): the parting-of-the-ways debate — the two poles (earlier-partings vs. late/gradual/constructed) that bound the qualifier's sharpness (parametric interiors; live-verified bibliographically — weak content-verification, disclosed).

# Consensus (KOS-0003 §9)
- Evidence strength: **High** for the 1st-c. emergence and the descent from Second Temple Judaism; **Moderate** for the qualifier's fit (the timing/sharpness of the parting is actively contested).
- Consensus strength: **High** that Christianity began as a Second-Temple Jewish movement and descends from that matrix; **contested** on when/how sharply it became a distinct religion — which is the qualifier tension, not a doubt about descent.

# Assumptions (KOS-0003 §10)
- **Inheritance not re-derivation:** the first-century anchors and the apocalyptic-inheritance warrant are inherited from closed records at their grades (§3.1); those investigations are not re-opened or edited.
- **Single-target edge:** the in-family parent (Second Temple Judaism) is the one modelled parent; later Hellenistic/Greco-Roman inputs are prose-only, not edged.
- **Metaphysical bracket, acute:** no supersessionist frame (Christianity is not modelled as the fulfilment/replacement of Judaism), no polemical frame; the truth of Christian claims is not at issue.

# Confidence (KOS-0003 §8)
- **emergence_dating — Level 4 (High):** 1st-c. CE origin, on inherited High-graded closed anchors (CLM-0068/0075/0076). **Not Level 5** (reserved; the under-Pilate specification is Moderate, and the tradition-separation point is contested).
- **descent_from_second_temple_judaism — Level 4 (High):** the Jewish-stream→sect inheritance is among the field's most secure results (seed CLM-0058, L4). **Not Level 5.**
- **schism_qualifier_fit — Level 3 (Moderate):** `schism` is the least-wrong value for "separated to become distinct," but the gradual/late/uneven character of the parting (SRC-0139/0141) complicates a label that connotes a sharp break; the tension is routed to Anchor Fit. **No Level 4/5.** R0.

# Limitations
- Establishes a 1st-c. CE emergence and a well-attested descent from Second Temple Judaism, with a least-wrong-with-caveat `schism` qualifier; does **not** fix a date for the separation, does **not** endorse the sharp-early *or* the late-gradual pole (both are steelmanned; the qualifier carries the tension), and asserts **nothing** about Christianity's truth.

# Relationships (STD-0004)
- `derived_from` SRC-0140, SRC-0139, SRC-0141, SRC-0103.
- `depends_on` CLM-0058 (seed warrant), CLM-0068, CLM-0075, CLM-0076 — one-directional layer-inheritance edges into closed records (INV-0011/0013/0014 **unmodified**).
- `supports` FND-0017; **warrants the ENT-0013 → ENT-0012 `branches_from` (`schism`) edge**.
- `part_of` INV-0017.

# Revision History
|Version|Date|Status|Description|
|---|---|---|---|
|0.1|2026-07-22|Draft|Created for RQ-0017 (Specialist pass). 1st-c. CE emergence (inherited CLM-0068/0075/0076, High) and descent from Second Temple Judaism (seed warrant CLM-0058, High) — both High. `branches_from` Second Temple Judaism qualifier `schism` (scaffold working hypothesis retained) chosen as least-wrong for "separated to become distinct," with a load-bearing sharpness caveat: the parting was gradual/late/uneven (Boyarin SRC-0139; Becker & Reed SRC-0141) against the earlier-partings pole (Dunn SRC-0140); `schism_qualifier_fit` graded Moderate to encode the tension, routed to Anchor Fit. `tradition_type: emergent` (founded tension flagged). Both rivals (sharp-early / late-gradual) steelmanned. Metaphysical bracket acute — no supersessionist framing. Inherited grades cited not re-derived; parting-source interiors parametric; verification-light; R0; not cleared for external reliance. Pending Critical Review and structural validation.|
|0.2|2026-07-22|Draft|attribution backfill (Stage 1, record-level, best-effort) per ADR-GOV-0011 Decision B|

# End CLM-0093
