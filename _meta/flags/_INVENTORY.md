---
type: completeness audit
scope: every decision-bearing item in _meta/flags/, by whatever structure each file uses
status: enumeration only — no rulings made, nothing moved
---

# Complete inventory of `_meta/flags/` — 707 decision-bearing items

**Built because my own extraction was incomplete.** The 275-row pass that produced
`_BY_DESTINATION.md` read **only markdown tables with an ID in the first cell**. It therefore
missed, silently:

- **`_Clinical_Process_set.md` entirely** — its 10 file-combination proposals are `### C1 ·` …
  `### C10 ·` **headings**, and its reverse-flag table is keyed on *destination*, not on an ID.
  **Zero of its items were in the 275.**
- **59 `KEEP + IN-TEXT FLAG` bullets** across the system files, which sit outside the move tables.
- **`GI_merged.md`'s 28 groupings**, which are written as **run-on prose** (`G1 … · G2 … · G3 …`)
  rather than as bullets or rows.

**Three grouping formats coexist and no single parser sees all three:** run-on prose (GI),
bullets (Cardio and 16 others), `###` headings (Psychiatry). This is the same class as
CLAUDE.md rule 9's silent false skip — *"a file missing from a scan looks identical to a file
that came back clean"* — except the unit skipped was a whole file and a whole structure.

## Totals

| | |
|---|---:|
| **decision-bearing items** | **707** |
| written as a bullet | 361 |
| written as a table row | 278 |
| written as a `###` heading | 25 |
| written as run-on prose | 1 section (GI's 28 groups) |

## By category, and whether it needs a ruling from you

| Category | n | Needs your ruling? |
|---|---:|---|
| **GROUPINGS** | **350** | **No.** *"Groupings need no ruling from me. Grouping is not merging."* Nothing here proposes a discard. |
| **MOVES** | **260** | **Partly — see the split below.** |
| **KEEP + FLAG / POINTER** | **59** | **No.** Resolved by A3: *"All in-text flags… No ruling needed from me on any of these."* 80 flags applied, `90dc93f`. |
| **FILE COMBINATIONS** (`C1`–`C10`) | **10** | **YES — none has been ruled on.** |
| **NARRATIVE FINDING** | 20 | No — findings, not proposals. |
| **RECORDED (no action)** | 4 | No — the disposition *is* "recorded". |
| **OPEN QUESTION** | 2 | **YES** — the drug axis and the procedure axis. |
| **DONE (recorded)** | 2 | No. |
| *REVERSE FLAGS* | *(7 rows)* | *Not counted — a destination-keyed index of moves already counted under MOVES.* |

## The 260 MOVES, split

| | n | Status |
|---|---:|---|
| **✅ executed** | **61** | Investigation-Interpretation (`ac620de`), Examination + History-Taking (`c5df174`), A1 (`f5e49c9`) |
| pending, **named destination** | **104** | needs approval by destination |
| pending, **flag only — no destination proposed** | **63** | needs a home, or a ruling that none exists |
| pending, **arguable / decide-with** | **32** | two or three defensible homes, no discriminator |

**197 pending.** The 63 with no destination are the ones a pattern *cannot* resolve — they are
the residue where the analysis found a real problem and could not name where the content goes.

## Per file

| File | Items | Moves | Groupings | Keep | Other |
|---|---:|---:|---:|---:|---:|
| `MSK_merged.md` | **54** | 16 | 23 | 3 | 12 |
| `GI_merged.md` | **51** | 12 | 28 | 5 | 6 |
| `OBGYN_merged.md` | 50 | 20 | 27 | 3 | — |
| `Derm_merged.md` | 46 | 16 | 26 | 4 | — |
| `Neuro_merged.md` | 45 | 23 | 19 | 3 | — |
| `Heme Onc_merged.md` | 43 | 20 | 22 | — | 1 |
| `Infectious Disease_merged.md` | 43 | 20 | 19 | 4 | — |
| `Cardio_merged.md` | 42 | 13 | 24 | 4 | 1 |
| `Endocrine and metabolics_merged.md` | 38 | 14 | 21 | 3 | — |
| `Renal and Urology_merged.md` | 38 | 13 | 18 | 3 | 4 |
| `Resp_merged.md` | 35 | 14 | 17 | 4 | — |
| `Pediatrics_merged.md` | 34 | 7 | 22 | 5 | — |
| `Emergency and Crit Care_merged.md` | 31 | 16 | 12 | 3 | — |
| `ENT_merged.md` | 29 | 10 | 16 | 3 | — |
| `Psychiatry_merged.md` | 25 | 9 | 13 | 3 | — |
| `Geriatrics_merged.md` | 25 | 9 | 14 | — | 2 |
| `Opthalm_merged.md` | 24 | 7 | 14 | 3 | — |
| `GP_merged.md` | 22 | 11 | 8 | 3 | — |
| `Anaes_merged.md` | 20 | 10 | 7 | 3 | — |
| **`_Clinical_Process_set.md`** | **12** | — | — | — | **10 combinations + 2 open questions** |

`_BY_DESTINATION.md`, `_CONSOLIDATED.md`, `_RULE5_FIGURES.md`, `_TRAUMA.md`, `_PAIRED_BLOCKS.md`
and `_INVENTORY.md` carry **no independent decisions** — they are indexes and reports over the
19 per-file files plus the Clinical Process set.

## Also present, and not previously counted anywhere

**"UNGROUPED — stays put, listed for visibility"** blocks. GI's names **23 sections**; Cardio 8,
MSK 6, Heme 3, OBGYN 3, Endocrine 2, ID 2, Pediatrics 1, Renal 1. **These are deliberate
non-decisions** — content the analysis looked at and left — and they were in no count until now.
They need no ruling, but they are the record that those sections were examined rather than
skipped, which is the distinction rule 9 says is invisible.

## Reconciliation against the ledger's 280 and 291

**The flag files are the artefact; `_CONSOLIDATED.md` is an index over them, and it was built
from the incomplete extraction.**

| Ledger claim | Actual | Difference |
|---|---:|---:|
| "moves and flags **280**" | **319** (260 moves + 59 keep) | **+39** |
| "groupings **291** (214 high · 77 medium)" | **350** | **+59** |

**Where the 39 went.** The ledger's 280 counted move-table rows and the flags it had already
identified, from the table-only parser. It missed the 59 `KEEP + IN-TEXT FLAG` bullets as a
category — 80 flags were later applied from them under A3, so the *work* was done, but the
*count* never included them; and it double-counted some rows that appear in both a per-file
table and `_BY_DESTINATION.md`. Net +39.

**Where the 59 went.** 291 was the sum of the per-file grouping counts as reported at the time.
It omitted **GI's 28 run-on-prose groups** almost entirely and **Psychiatry's 12**, which did not
exist when the ledger was written (they were deliberately deferred until A1 made the file whole).
28 + 12 = 40 of the 59; the remainder is groups added or split during the later per-file passes
and never re-totalled.

> [!warning] **This is the sixth sampled-not-counted figure in this project**, after "Corpus C
> states no doses", "65 backticked references", "42 wikilinks in C", "167 placeholder links" and
> "191 unbuilt targets". Same cause every time: **a number correct for the thing it was measured
> against, then quoted as a fact about the whole.** 280 and 291 were correct counts *of the
> table-shaped items the parser could see.*

**`_CONSOLIDATED.md` has been corrected to 707 / 319 / 350 and now names its own scope.**

## What actually needs a ruling from you

| | n | |
|---|---:|---|
| **File combinations `C1`–`C10`** | **10** | none ruled on; `C3` is already partly executed by the Investigation-Interpretation move |
| **The two axis questions** | **2** | drug axis · procedure axis |
| **Pending moves with a named destination** | **104** | approve by destination, as you have been |
| **Pending moves, arguable** | **32** | two or three homes, no discriminator |
| **Pending moves, no destination proposed** | **63** | needs a home or a ruling that none exists |
| **TOTAL** | ~~211~~ **161** | corrected — see below |

> [!warning] **211 was wrong and 161 is the measured number.** 41 rows were already executed but
> unmarked, because the `✅ EXECUTED` marking had been keyed on **exact heading text** and the
> flag rows are paraphrases; 9 more were `keep, flag` rows A3 had already settled. Re-marked by
> **row ID against the execution manifests**. **The full list is `THE_161.md`.**

Everything else — 350 groupings, 59 keep-and-flag, **61 executed moves**, **12 paired-block rows
resolved as Option 1**, 20 narrative findings, 4 recorded, 2 done, and the ungrouped "stays put"
lists — **is resolved by a pattern you have already set. 546 items.**

---

## SHOCK — an unflagged duplication, found 2026-09-01

**14 headings contain "shock". None moved — the count is identical to the initial upload.**
But two parallel breakdowns exist and **no flag row in any of the 25 files ever covered them:**

| File | Structure |
|---|---|
| `Emergency and Crit Care_merged.md` 01_Cardiovascular `§0.20 Shock` (co-located out of `Cardio_merged.md` 2026-09-01) | `§0.20.1` Cardiogenic · `§0.20.2` Hypovolaemic · `§0.20.3` Distributive · `§0.20.4` Obstructive |
| `Emergency and Crit Care_merged.md F0-3` | `§0.1` Recognition and Phenotype Framework · `§0.2` Hypovolaemic · `§0.3` Cardiogenic · `§0.4` Obstructive (tamponade) · `§0.5` Obstructive (PE) · `§0.6` Distributive (Addisonian) |

Plus `Emergency §0.2 SIRS, Sepsis and Septic Shock`, `§0.10 Urosepsis and Gram-Negative Septic
Shock`, and `Infectious Disease ### Toxic shock syndrome`.

**The same four-phenotype framework, taught twice, in two files, with different subdivisions.**
It is the shape the whole exercise was looking for and the analysis did not find it — because
every flag row was generated per source file, and neither file *declares* the other.

**`Cardio §0.20.3 Distributive shock` also holds a full ASCIA adrenaline box** including the
`<7.5 kg` infant row — a fifth anaphylaxis copy, and the second of only two places carrying that
row. See `_RULE5_FIGURES.md`, which had missed it.
