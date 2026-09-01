---
type: analysis
scope: the 12 "Examination + History-Taking (paired blocks)" rows
status: NOT EXECUTED — measured, and the operation as specified would destroy content
---

# The 12 paired-block rows — why I stopped instead of moving them

> [!danger] **BOTH THE LINE NUMBERS AND THE FILE NAMES IN THIS FILE MAY BE STALE. RE-ANCHOR ON HEADING TEXT BEFORE EXECUTING ANY ROW.**
> **The line numbers were CORRECT when written and were invalidated afterwards — measured, and it
> corrects an earlier claim of mine that they were stale from the start.** On a 219-row sample,
> the recorded line number landed on a heading in **97%** of rows at `73aebe0`, the last commit
> before any content moved. **The 80 in-text flags (`90dc93f`) took that from 212/219 to 53/219
> in one commit** — 73% destroyed by insertions, not by moves. Each executed block since has cost
> a further 15–20% of what survived. **They are now valid in 16% of rows and still falling.**
>
> **File names go stale too, and a filename reads as authoritative in a way a line number does
> not.** A1 (`f5e49c9`) moved `N1`–`N8` from Neuro to Psychiatry and `GER3`/`GER4` out of
> Geriatrics; `ac620de` and `c5df174` moved 139 blocks into `Investigation-Interpretation.md`,
> `Examination.md` and `History-Taking.md`. A row still naming the old file is not a typo — it
> will send a reader to a file that no longer holds the content.
>
> **Rows already executed are marked `✅ EXECUTED` inline, with the destination and commit.**
> Everything else is a proposal.
>
> **The section names in these rows are PARAPHRASES, not verbatim headings.** `0.1 Thyroid Panel
> (TSH, fT4, fT3, antibodies)` against an actual `0.1 Thyroid Panel (TSH, Free T4, Free T3,
> Thyroid Antibodies)`. An exact-text search will miss about a third of them — match on the
> section number plus distinctive words, and **read every hit** before acting.
>
> Sweep of 2026-09-01: 672 rows checked, **8 stale filename assertions corrected**, **128 lines
> marked executed**. See `RUN_STATE.md` for the drift analysis.


**The other two OSCE destinations are done** (`c5df174`): 35 whole blocks, 23 pairs marked,
nothing merged. **These 12 rows are a different shape and I have not touched them.**

## What they actually are — measured

```
total Focused Hx / History / Examination bullets : 109   (53 Hx · 55 Exam · 1 History)
all single-line                                  : True
median words per bullet                          : 85
distinct parent sections they sit inside         : 55
distinct source files                            : 15
```

**They are not blocks.** Each is **one bullet** inside a presentation entry whose whole form is
a fixed skeleton:

```
- **D:**            what it is
- **DDx:**          the differential
- **Focused Hx:**   ← this
- **Examination:**  ← and this
- **First-line Ix:**
```

Removing the two middle bullets from 55 entries does not extract a block — it **puts a hole in
the middle of 55 entries** and produces 109 orphan fragments in two files with no organising
principle, since each is written for one presentation and reads as a non-sequitur away from it.

## The flag-row counts were wrong, in both directions

| Row | Flag said | Actually |
|---|---|---|
| `C-9` Cardio | 14 + 14 | **14 + 14** ✓ |
| `D-15` Derm | 6 + 6 | **5 + 5** |
| `K-17` MSK | 8 + 8 | **6 + 6** |
| `B-4` OBGYN | 12 blocks | **6 + 6** |
| `R-12` Resp | 3 + 3 | **2 + 3** |
| `N-8` Neuro | 8 + 8 | **8 + 8** ✓ |
| `T-2` ENT | 4 + 4 | **4 + 4** ✓ |
| `E-2` Opthalm | 4 + 4 | **4 + 4** ✓ |
| `RU-14` Renal | 2 + 2 | **2 + 2** ✓ |

## The real obstacle: the standing rule's own boundary runs *inside* each bullet

Your rule is *"how to elicit Murphy's sign is Examination; Murphy's sign is positive in
cholecystitis is GI."* Applied to these bullets:

```
bullets with EXAMINATION TECHNIQUE language      : 30
bullets with DIAGNOSTIC REASONING language       : 32
bullets with BOTH, in the same bullet            :  5
bullets with neither marker                      : 53
```

**The 5 are not the problem — they are the proof.** In every one, the two are interleaved
*within a single sentence*, so there is no seam to cut on:

> **ENT `## Acute Hoarseness` — Examination:** *"**listen to the voice and characterise it** —
> breathy suggests glottic incompetence or cord palsy; harsh or rough suggests a mass lesion; a
> **muffled "hot potato" voice suggests supraglottic pathology and an airway concern**."*

*Listen to the voice and characterise it* is technique → `Examination.md`.
*Breathy suggests cord palsy* is what the finding means in this presentation → **stays in ENT**.
**They are the same clause.**

> **Derm `## Chronic Rash` — Examination:** *"full skin examination **with the patient
> undressed** — including scalp, behind the ears, umbilicus, natal cleft, nails, palms, soles
> and web spaces… distribution pattern (**extensor versus flexural is one of the highest-yield
> discriminators — psoriasis extensor, atopic eczema flexural**)"*

The undressed-and-check-these-sites list is generic technique. The extensor/flexural
discriminator is dermatological diagnosis. One bullet.

And the 53 bullets matching **neither** marker are mostly pure presentation-specific reasoning,
which the standing rule places **in the system file**:

> **Cardio `## Presyncope` — Focused Hx:** *"**the circumstances are the diagnosis.** Position
> at onset (**during exertion or lying flat points to a cardiac cause; on standing points to
> orthostatic**)…"*

That is not how to take a history. It is what the answers mean in presyncope.

## What I recommend, and what it would cost

**Do not move the 109 bullets.** Three options, in the order I'd rank them:

1. **Leave them and point.** Add one line to each of `Examination.md` and `History-Taking.md`
   noting that presentation-specific focused histories and examinations live in the system
   files, with the list of the 55 entries. **Cost: one commit. Loses nothing.** This is the
   `ENT T-5` Bell's-palsy shape you already have as the model — a deliberate stub that defers
   and explains why.
2. **Extract only the generic technique, sentence by sentence, leaving the reasoning behind.**
   Honest but it is **109 hand judgements on clinical prose**, each one a rewrite rather than a
   move, and a rewrite cannot be verified line-for-line against pre-move `HEAD` the way all
   139 blocks moved so far have been. **I would not do this without you reading each one.**
3. **Move the bullets whole.** What the row as written asks for. It relocates the diagnostic
   reasoning too — against the standing rule — and holes 55 entries. **I recommend against it.**

**If you want option 3 anyway, say so and I will execute it exactly as specified.** The
disagreement is recorded here; it is your corpus and your exam.

## What is NOT in doubt

`RU-14`'s flag correctly spotted that one bullet is **explicit technique** —
*"examine the patient standing…"* for a varicocele. **That one is a genuine move.** A handful
of others like it exist. Option 2 is the way to find them, and option 1 does not preclude it
later.
