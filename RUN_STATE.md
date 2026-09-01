# RUN_STATE — file reorganisation pass

**Task:** two outputs per file — (1) grouping of sections covering the same topic,
(2) misplacement flags. Then the 16 Clinical Process files as a file-combination
question, not a section-grouping one. **NOTHING MOVES until the user approves.**

**Per-file findings go to `_meta/flags/<file>.md`.** This file is the resume point.

## Counting note for the user
The brief says "20 system files". There are **19** merged system files on disk, plus
**16** Clinical Process files (35 content files + CLAUDE.md + checklist.csv = 37 entries).
So after GI there are **18** system files remaining, not 19. Listed below.

## Method (established on GI, which was the calibration file)
1. `sections.py <file>` — heading + first paragraph for every section, `Mx –` triads skipped.
   Read the first paragraph, never the heading alone.
2. `xref.py <file>` — inbound reference index in **BOTH** forms: `[[Code]] 0.x` wikilink
   **and** `` `Filename.md` 0.x `` backticked. Wikilink-only was a **false negative** on GI's
   three `NEW_*` sources.
3. `osce.py <file>` — candidate generator for history/examination/communication content
   (standing rule). **NOT a verdict — see the warning below.**
4. Read full sections wherever heading and first paragraph disagree, and wherever a flag
   is being proposed.
Scripts live in the session scratchpad, not the repo.

## TWO TOOL DEFECTS FOUND BY VALIDATING AGAINST KNOWN ANSWERS (CLAUDE.md rule 11)
Both found by running the new tool on GI, where the answers were already established.
- **`xref.py` v1 counted wikilinks only** and reported GI's three `NEW_*` sources as having
  **zero** inbound references. They are cited by backticked filename instead
  (`NEW_Drugs_12_Gastrointestinal.md 0.2` etc.). A zero-inbound verdict is exactly what makes
  a move look free. Fixed: both forms indexed, section number optional.
- **`osce.py` v1 MISSED GI M-7 entirely** — the whole examination half of C1 §0.2 — because
  this corpus puts examination content in Obsidian callouts, one clause per line, and the
  pattern required two words on one line. **50% false-negative rate on the one file whose
  answers were known.** Fixed by matching callout titles and named signs. **The tool remains a
  candidate generator only; sections it does NOT flag are still read by eye.**

## OFF-BY-ONE POINTERS — the method-level finding from Cardio (2026-09-01)
**A cross-reference can point at a section number that EXISTS but is the WRONG SECTION.**
This is not the broken-link problem the user already named (a `[[file]]` link resolving to the
wrong file after a move). It is one level down and it is silent.

`01_Cardiovascular` was renumbered — the fingerprint is its heading
`## 0.23 0.22a Rheumatic Heart Disease (RHD)`, which still carries **both** numbers. Every section
below it shifted by one. Pointers written before that insertion were never updated.

Measured, not reasoned:
- **2,559** numeric section pointers in the vault.
- **9** point at a number that does not exist. Loud, and `dangling.py` catches them.
- **`misaimed.py` then caught 7 more that `dangling.py` reported as CLEAN**, because their numbers
  do exist. Each names its topic as well as its number, and the two disagree:
  `Infectious Disease:1397` says *"`0.30` Infective Endocarditis"* — 0.30 is Pulmonary Embolism.
  All 7 are off by exactly one, all in the same direction, all targeting `01_Cardiovascular`.
- **Of the 20 pointers that carry both a number and a name, 7 are wrong — 35%.**

**THE PART THAT CHANGES THE METHOD:** only **21 of 2,416** wikilink section pointers — **0.9%** —
carry a topic name at all. The other **99.1% are a bare number and cannot be validated by any
means available.** `GER1` has 85 numeric pointers and **not one** names its topic; `A10` 78 and none;
`A9` 69 and none.

Consequence for this task: **POINTED AT BY is the load-bearing evidence for every move**, and its
section-level resolution is only as good as numbering that has already proved unstable in at least
one file. File-level inbound counts remain sound. Section-level counts are provisional wherever the
target file has been renumbered, and **there is no way to tell from the pointer itself.**

## NUMBERING TRUST MAP (option 2, user-approved) — `drift.py`
Five signals per source: double-numbered heading (the renumber fingerprint), duplicate section
numbers, gaps in the 0.N sequence, dangling inbound pointers, number/name disagreements.

**171 of 172 sources show no drift.** Only three ever flagged:
- `01_Cardiovascular` — FINGERPRINT `## 0.23 0.22a Rheumatic Heart Disease (RHD)`. **The only file
  with real drift.** Its 21 damaged inbound pointers are fixed as of `48a870f`.
- `NEW_Investigations_Gastroenterology` — 6 gaps, **all benign**: combined headings such as
  `## 0.12 Colonoscopy · 0.13 Flexible Sigmoidoscopy · 0.14 Sigmoidoscopy · 0.15 Anoscopy`.
- `B2_Hypertension_Spectrum` — 1 dangling pointer, deliberately unfixed (see below).

**`drift.py` v1 produced a false positive** and it was worth having: it reported
`NEW_Drugs_07_Blood_and_Electrolytes` as having 4 duplicate section numbers. It has none — the
file is **physically concatenated into TWO merged docs** (`Endocrine and metabolics_merged.md:2889`
and `Heme Onc_merged.md:2774`), so its headings were counted twice. Guarded, re-run, clean.

**Caveat that must travel with this map: absence of signal is WEAK evidence.** Only 0.9% of numeric
pointers carry a topic name, so the number/name check can only ever see a sliver. A file with no
signal is *unrefuted*, not *verified*.

## NOT FIXED, deliberately
`OBGYN_merged.md:4264` cites `[[B2]] 0.5`. `B2_Hypertension_Spectrum` has only §0.1–0.4. The context
is antihypertensives in pregnancy; **which section was intended cannot be determined**, and CLAUDE.md
rule 1 forbids writing a plausible-sounding target. Flagged for the user.

## THIRD INDEXER DEFECT (found at Endocrine, fixed)
`xref.py` reported `F0-2_Acid-Base__DKA_and_Fluid_States` as **zero inbound**. It has **55+**.
Prose writes `[[F0.2]]` with a dot; the filename uses a hyphen — **the exact trap CLAUDE.md §1.10
documents**. Only hyphen-prefixed codes were affected (`F0-1`…`F0-5`, all in Emergency plus F0-2 in
Endocrine). Fixed by registering the dotted alias. **All four earlier zero-inbound verdicts re-run
and unchanged.** Three tool defects now, all caught by validating against a known answer.

## Residual limitation, not fixable mechanically
Anaphoric references carry no filename and no tool can index them.
`Renal and Urology_merged.md:2000` reads *"see 0.22–0.23 of the same file"*. Hand-caught.

## Standing rule (from GI M-16, user-issued)
Any `Focused Hx` block, `Examination` block, history schema or examination sequence found in a
system file is flagged for `History-Taking.md` or `Examination.md`, with a pointer left behind.
**The line:** disease-specific findings stay in the system file. *"Murphy's sign is positive in
cholecystitis"* is GI. *"How to elicit Murphy's sign"* is Examination.
Reason: the OSCE is 1 Nov and tests exactly this; Corpus B is presentation-organised so it
generated one of each per presentation.

## PROGRESS
- [x] **GI_merged.md** — done, decisions received, `_meta/flags/GI_merged.md`
- [x] **Cardio_merged.md** — done, `_meta/flags/Cardio_merged.md`. **PRODUCED A METHOD-LEVEL
      FINDING — run PAUSED here to report it (user standing instruction).**
- [x] **Off-by-one pointers FIXED** — commit `48a870f`, standalone, 21 instances. User ruled
      options 2+3. Dangling 9→1, number/name disagreements 7→0.
- [x] **Resp_merged.md** — done, `_meta/flags/Resp_merged.md`
- [x] **Renal and Urology_merged.md** — done
- [x] **Endocrine and metabolics_merged.md** — done
- [x] **Neuro_merged.md** — done. **Contains N1–N8, the whole Corpus B psychiatry set.**
- [x] **Heme Onc_merged.md** — done
- [x] **Infectious Disease_merged.md** — done
- [x] **MSK_merged.md** — done
- [x] **Derm_merged.md** — done
- [x] **OBGYN_merged.md** — done
- [x] **Pediatrics_merged.md** — done
- [x] **Psychiatry_merged.md** — done (groupings deferred: half the corpus is in Neuro)
- [x] **Geriatrics_merged.md** — done. **GER3 and GER4 are not geriatrics.**
- [x] **Anaes_merged.md** — done
- [x] **Opthalm_merged.md** — done
- [x] **GP_merged.md** — done
- [x] **Emergency and Crit Care_merged.md** — done
- [x] **ENT_merged.md** — done

**ALL 19 SYSTEM FILES DONE.**
- [x] **Clinical Process set (16 files)** — done, `_meta/flags/_Clinical_Process_set.md`
- [x] **Consolidated report** — `_meta/flags/_CONSOLIDATED.md` + artifact
      https://claude.ai/code/artifact/47915732-d749-41d4-beee-6c21b2ee4e26

**RUN COMPLETE. Awaiting user decisions. NOTHING MOVED.**
- [ ] Resp_merged.md
- [ ] **Consolidated report** — moves by destination file · all in-text flags · groupings by
      confidence · anything unplaceable

## Cross-file items already open (must survive to the consolidated report)
- ENT → GI: Barrett's + oesophageal carcinoma (M-R1). ENT_merged L662 stale pointer `03.08`.
- GI → Emergency: paracetamol (M-8) and ascending cholangitis (M-9) as **deliberate duplicates**.
- Carcinoid split GI §0.15 / Derm L2084–2100 / Endocrine (M-13).
- Cardio → OBGYN or GER7: CTG/NST self-declared misfile (C-1).
- Cardio → Investigation-Interpretation: **ECG interpretation, absent from the whole Clinical
  Process set** (C-2, C-3). Needs a user ruling on whether the standing rule extends to
  investigation interpretation.
- Cardio B6 §0.4–0.8 are general presentations filed as cardiology; §0.8 Undifferentiated Lump has
  **19 inbound, none cardiac** (C-10 – C-14).
- Troponin has four section-level homes; ALS has two (Cardio §0.5, Emergency §0.3).
- ~~broken pointers into `01_Cardiovascular`~~ **FIXED, commit `48a870f`.**
- **`NEW_Drugs_07_Blood_and_Electrolytes.md` is byte-identical in two merged files** — 240 lines,
  in `Endocrine and metabolics_merged.md:2889` and `Heme Onc_merged.md:2774`. The only source file
  in the vault (1 of 295) concatenated into more than one merged doc. Needs a home decision.
- **Standing rule EXTENDED by the user to investigation interpretation.** Same boundary: *how to
  read the test* → `Investigation-Interpretation.md`; *what the result means in this disease* →
  system file. "How to work through an ECG" is Investigation-Interpretation; "new AF on ECG in
  thyrotoxicosis" is Endocrine.
- Alcohol withdrawal is in **four** places across three files (GI M-5 said three): `GI §0.6.1` ·
  `N2 §0.1` (in Neuro) · `04_Neurology ### Alcohol Withdrawal Seizures` · `Psychiatry 14a-1`.
- **BIGGEST STRUCTURAL FINDING: `Neuro_merged.md:3829–5452` holds N1–N8, the entire Corpus B
  psychiatry set — 1,624 lines, 28% of the file. `Psychiatry_merged.md` has none of it.**
  8-for-8 mapping onto Psychiatry's Corpus A files. Recommend one move of eight whole sources,
  **before** any other move, since it changes what the Psychiatry file contains.
- **CSF would end up in three homes**: `Investigation-Interpretation §1.13` (exists) ·
  `04_Neurology ### CSF Interpretation` · plus GI M-1 (`## 0.32 CSF Studies`), which the user
  approved moving **to Neuro**. Recommend redirecting M-1 to Investigation-Interpretation.
  **Needs a user ruling.**

---

## PART A EXECUTED (2026-09-01) — A1 to A7

The user ruled on the ledger and authorised PART A only. **PART B is untouched** and needs
individual approval by destination.

| | What | Commit | Verified by |
|---|---|---|---|
| **A1** | `N1`–`N8` (8 whole sources, 1,624 lines) `Neuro_merged.md` → `Psychiatry_merged.md` | `f5e49c9` | block sha256 `b395c26c7c69a568` identical before/after · Neuro 5,867→4,243 · Psych 1,405→3,029 · 8 `SOURCE: N#_` dividers present in order, **0 left in Neuro** · duplicate-header counts unchanged vs `git show HEAD:` |
| **A1** | `GER3` (196 lines) and `GER4` (224 lines) out of `Geriatrics_merged.md` | `16a9386` | Geriatrics 1,347→928 · remainder byte-matching · content identical apart from trailing blanks |
| **A2** | Four new files created: `Procedures.md` · `Safeguarding.md` · `Preventive-Health.md` · `Palliative-and-End-of-Life-Care.md` | `16a9386` | vault grepped before creation (§1.14) · `Preventive-Health` holds `GER3` whole, `Safeguarding` holds `GER4` whole, the other two are scaffolds with manifests |
| **A3/A4/A5** | **80 in-text flags** across all 19 system files, incl. GI's `M-10`, `M-17`, `M-18`; both ends of the three two-way disagreements; the `CF-PAIR` markers and the `N1 §0.5` verification warning on both SA mental health law copies | `90dc93f` | `applyflags.py` refuses any anchor matching ≠1 time — **80 applied, 0 failed to anchor** |
| **A6** | Trauma report — **report only, nothing moved**, `M-6` NOT executed | `cfba800` | `_meta/flags/_TRAUMA.md` |
| **A7** | Rule 5 figure inventory — **report only** | `cfba800` | `_meta/flags/_RULE5_FIGURES.md` · 11 spans, 48 figure-bearing lines, line numbers re-verified post-A1/A3 |
| — | Psychiatry section groupings, produced now the file is whole | `cfba800` | 12 groups over 175 sections, 19 not-groupable, **0 unaccounted** (`scratchpad/recon.py`) |
| — | All 248 move rows grouped **by destination**, 15 blocks | this commit | `_meta/flags/_BY_DESTINATION.md` |

### The A1 retarget finding — measured, and it contradicts the instruction's premise

The ruling required retargeting every inbound pointer. **There was nothing to retarget.**
209 `[[N1]]`–`[[N8]]` references exist; **none broke**, because wikilinks in this corpus name
the **source** file, which the move did not rename. 84 `[[GER3]]`/`[[GER4]]` references
likewise. `dangling` still 1 (the deliberate `[[B2]] 0.5`), `misaimed` 0, drift map unchanged.

**What did change is reachability: 45 references flipped intra-file → cross-file** (9 `[[N#]]`
left in Neuro, 36 `[[D#]]` carried into Psychiatry). **Locator notes were added at all three
ends** instead of a retarget — that is the correct repair for a reachability change, and
rewriting 209 correct links would have been damage.

## FOURTH TOOL DEFECT (found while building `_BY_DESTINATION.md`, fixed) — CLAUDE.md rule 9

The evidence classifier keyed on the flag-row ID alone. **`P-5`, `P-6` and `P-7` each exist
in two different flag files** (GP and Paediatrics), as do **`R-2`, `R-3` and `R-6`** (Resp and
Geriatrics). Three rows were silently marked with another row's evidence class — the false-hit
direction of rule 9, on an identifier rather than a substring.

**Found by counting the emitted column**, which returned `13 / 213 / 22` where the header
asserted `12 / 205 / 31`. Re-keyed on `(file, id)`; corrected output `12 / 19 / 217`, quoted
verbatim in the report. **The check that caught it was running the count instead of trusting
the input set** — rule 11 in its ordinary form.

## RESUME POINT

**Everything the user asked for in the PART A message has been delivered.** Nothing is
half-done. The next action is the user's: **approve destinations**, not rows.

**Blocked on user ruling, in the order they matter:**
1. `Investigation-Interpretation.md` — 59 rows, the largest block, and it creates the corpus's
   first general ECG entry. **9 known duplicate pairs to be marked, never merged.**
2. Trauma as one question across four files (`_TRAUMA.md`) — `M-6` withdrawn pending this.
3. `M-1` (CSF) and `M-2` (Coombs/DAT) — approvals withdrawn, recommendations recorded.
4. The 39 rows with **no destination proposed**.
5. Clinical Process file combinations (`_Clinical_Process_set.md`) — none executed.

**Standing prohibitions until then:** no section moves beyond A1's · no moves to
Investigation-Interpretation, Examination, History-Taking, Emergency, Paediatrics or any
system file · no Clinical Process combinations · **no merging of any duplicate pair, anywhere**
· nothing from the 11 approved-but-unexecuted rows.

---

## INVESTIGATION-INTERPRETATION EXECUTED (2026-09-01, `ac620de`) — the first destination approval

**104 sections · 2,285 lines · 23 source blocks · 12 system files.**
`Investigation-Interpretation.md` 533 → **2,986 lines**.

**Structure chosen, and why.** Part 1 (§1.1–§1.22) is **not renumbered and not edited**, apart
from one `CF-PAIR` marker beneath each of the 14 paired headings — CLAUDE.md §1.14 forbids
renumbering, and renumbering Part 1 would have broken every inbound pointer to it. Part 2
reproduces every incoming heading **verbatim and unrenumbered** under a `SOURCE:` divider naming
its origin file, which is the convention the merged files already use, so a pointer written as
`[[NEW_Investigations_Renal_and_Urology]] 0.3` still resolves by name wherever the block lives.
Each source file keeps its divider and gains a stub naming what left and why — **30 stubs for 30
contiguous runs**.

**Nothing merged.** 24 incoming sections cover topics Part 1 already has; both copies kept in
full, each carrying a `CF-PAIR` marker naming the other. Two further pairs are
**incoming-to-incoming**: the Mantoux appears in both respiratory sections, and group-and-hold
pairs with immunohaematology.

> [!warning] **It is 14 destination sections receiving 24 incoming, not the "9 duplicates" every
> earlier report in this project stated.** The 9 came from the Clinical Process analysis, whose
> list omitted **§1.2, §1.3, §1.13, §1.18 and §1.20**. Determined this time by hand against all
> 104 incoming headings and all 22 Part 1 headings, because the automated pair scorer had a
> **high false-negative rate** — it missed ABG↔§1.5 (acronym versus expansion, rule 2's exact
> trap), autoantibody↔autoimmune (synonym), and two more that fell a hundredth under threshold.

### Verification, all against the pre-move `git HEAD`

| Check | Result |
|---|---|
| blocks arriving line-for-line identical | **104 of 104** |
| moved headings still present in a source file | **0** |
| duplicate-header counts, all 13 files | **unchanged**; destination has none |
| `SOURCE:` divider counts, all 12 source files | **unchanged** |
| dangling pointers | **1** — the deliberate `[[B2]] 0.5`, unchanged |
| misaimed pointers | **0** |
| `drift.py` output | **byte-identical before and after** |

## FIFTH, SIXTH AND SEVENTH TOOL DEFECTS — all three found executing this move

**5 · Every line number in every flag file is stale, and the flag files do not say so.**
50 of the 59 rows pointed at something that is not a heading. Cause: the **80 in-text flags
applied in `90dc93f` shifted every system file** *after* the flag files were written. The
`_BY_DESTINATION.md` limitation *"line numbers are valid at `90dc93f`; any move invalidates
them"* was true and insufficient — they were **already** invalid when written.
**Consequence for the remaining destinations: do not execute any block from its recorded line
numbers. Re-anchor on heading text first.**

**6 · The section names in the flag rows are paraphrases, not verbatim headings.**
`0.1 Thyroid Panel (TSH, fT4, fT3, antibodies)` against an actual heading of
`0.1 Thyroid Panel (TSH, Free T4, Free T3, Thyroid Antibodies)`. 20 rows failed an exact text
match. **This is CLAUDE.md rule 10's PARAPHRASE clause, committed in my own records** — I wrote
the concept, not the author's phrase, and then tried to search on it. Resolved by token overlap
with the section number weighted, and every hit read.

**7 · The first block verifier reported 4 mismatches that were its own bug** — it rebuilt each
block by stopping at the next heading, so any section with subheadings (`C-2` ECG and its twelve,
`E-6`, `K-13`, `P-7`) failed. **Loss rate 0%. Verifier false-negative rate 4 in 104.** Same shape
as the merge-verification defect already recorded under rule 11: *"a false MISSING says content
was destroyed, which invites a restore that re-adds a block already present."*

**Also, and it is worth its own line: the `SOURCE:` dividers were first written as
`SOURCE: file.md  (moved from X, date)`.** `dangling.py` parses `SOURCE: (.*?) =====` and took
the whole string as the filename, registering every moved section under a key nothing points at
— **60 broken pointers reported.** Normalising the dividers to the exact corpus convention
returned it to 1. **No pointer was ever broken.** A format that merely *looked* like the
convention was enough to make the checker report catastrophe.

### One figure corrected

`drift.py` reports **158 of 172** sources with no drift signal, not the **171 of 172** recorded
earlier in this file. The 13 extra were flagged **before any of my work** — confirmed by running
the checker against a clean `git archive HEAD` extract. The claim that matters is unchanged and
now stronger: **before and after are byte-identical.**

---

## ⚠️ `PENDING_GUIDELINE_CHECKS.md` — THE REPO COPY IS CANONICAL WHILE THIS WORK RUNS

**Read this before touching that file, and before any sync in either direction.**

The tracker was **not in this repository** until 2026-09-01 — 50 citations across 19 files
pointed at a file that had never been tracked on any branch. It lived only in the Obsidian
vault. **The owner uploaded the current vault copy and it is now at the repo root**, filename
`PENDING_GUIDELINE_CHECKS.md`, matching all 50 citations exactly.

> [!danger] **The repo copy is authoritative until the owner pulls it back into the vault.**
> **A later session must NOT treat the vault copy as the source of truth and overwrite the repo
> copy with it.** Doing so silently deletes `B66` and `B67` and any row added after them, and
> the loss leaves no trace — this file has an **append-never-delete** history, so a row that
> vanishes cannot be distinguished from a row that was never written. That is the §1.13 failure
> in its worst form: *"taking one side silently discards either a stamp or a merge and nothing
> detects the loss."*
>
> **The owner pulls the repo copy back into the vault at the end of this work.** Until they
> confirm that has happened, the direction of sync is **repo → vault only**.

**Rows added 2026-09-01 (`B66`, `B67`).** Sequence maximum was **measured, not assumed**:
65 `B` rows, max `B65`, **no gaps and no duplicate IDs**, so B65 was both floor and ceiling.
Inserted immediately before `B65` — the position every row from `B23` to `B65` was inserted at,
preserving the file's newest-first convention within Section B.

**Append verified three ways:** the uploaded file's 198 lines are preserved as an **exact
ordered subsequence** of the 200-line result; **+2 lines, 0 removed, 0 modified**; and the
existing row-ID order is **identical** before and after.

- **B66** — EZ-IO needle bands `<39kg` / `>40kg` do not meet; 39–40 kg has no needle length,
  and the top band (`"larger patients"`) is unquantified.
- **B67** — the **class row**: weight and age band sets that do not tile the axis they claim to
  cover. Two instances (the ASCIA adrenaline table's missing `<7.5 kg` row, and B66). Resolves
  against **no external guideline** — it is a method item that closes when a band-tiling check
  exists and has been run across every dose table.

`_meta/PENDING_ROWS_TO_ADD.md` is retained as the record of why the rows were staged rather than
filed at the time. **Do not paste from it again** — that would duplicate B66/B67.

---

## THE STALENESS SWEEP AND THE DRIFT ANALYSIS (2026-09-01)

### Is the drift growing? YES — and it is entirely caused by later work

**I was wrong earlier.** I said the flag files' line numbers "were already stale when written."
**They were not.** Measured on the 219 rows carrying both a line number and a cited heading:

| Tree | Line number lands on a heading | Cause of the change |
|---|---:|---|
| `73aebe0` last commit before ANY content moved | **213/219 · 97%** | — |
| `f5e49c9` after A1 (`N1`–`N8`, `GER3`/`GER4`) | 212/219 · 97% | **−1.** Whole-source-block moves cost almost nothing |
| `16a9386` after A2 (four new files) | 212/219 · 97% | 0 |
| `90dc93f` after the 80 in-text flags | **53/219 · 24%** | **−159 in ONE commit** |
| `ac620de` after Investigation-Interpretation | 42/219 · 19% | −11 |
| `c5df174` after the OSCE block | 35/219 · 16% | −7 |

**"Stale when written" is 3%. "Stale because of later work" is 81%.** Only the second is
accumulating, and it will keep accumulating with every approved block.

> [!danger] **The counter-intuitive result: INSERTIONS are far more destructive than MOVES.**
> The 80 in-text flags moved no content at all and destroyed **73%** of the line numbers in one
> commit. The Investigation-Interpretation move relocated **104 sections and 2,285 lines** and
> cost **11 rows**. An insertion near the top of a file shifts everything below it; a move
> removes and adds in different places, and the two partly cancel.
>
> **So the cheap-looking operation is the expensive one.** Any future round of in-text flagging
> will cost more line-number validity than the block moves it annotates.

### Re-anchor cost per future block — measured on the two already executed

| | Investigation-Interpretation | OSCE |
|---|---|---|
| rows in the block | 59 | 31 |
| anchors needed | 103 | 38 |
| resolved by `scripts/reanchor.py` | 100 | 35 |
| **needed a hand decision** | **3** | **3** |
| line numbers still valid at execution | 9 of 59 (15%) | not usable |

**Cost is one script run plus about three hand decisions per block**, regardless of block size —
the hand cases are structural (a tie, a row naming a destination rather than a source, a row
whose file changed under A1), not proportional to the number of rows. **It does not grow with
the size of the block, and it does not grow as the line numbers rot further**, because the
method already ignores them entirely.

**The forward rule: never execute a row from its recorded line number. Re-anchor on heading
text.** Every flag file now carries that as a banner.

### The sweep — 672 rows checked

| | |
|---|---:|
| rows checked across 25 flag files | **672** |
| stale filename assertions found and corrected | **8** |
| candidates rejected as false positives after reading them | **8** |
| lines marked `✅ EXECUTED` with destination and commit | **128** |
| flag files given the staleness banner | **25** |

**The 8 false positives matter as much as the 8 real ones.** A first pass using fuzzy heading
matching returned **214** candidates. Most were rows in a *destination's* flag file describing
*incoming* content (`GI M-R1` describes Barrett's oesophagus, which is in ENT and proposed to
move to GI — the row is correct), or lines I had written myself recording that a move was done.
**Re-run against the execution manifests — exact heading text, not fuzzy matching — the real
number was 8 filename assertions and 144 executed-section citations.** Same lesson as §1.10's
`SRC:` token: when an exact key exists, use it instead of a content search.

The 8 corrected: `ENT:41` (`Neuro N7`), `Neuro:65` (`N2 … currently in Neuro`), `GP:27`
(`Geriatrics GER3`), `_Clinical_Process_set` ×4 (`Geriatrics GER4` ×3, `Geriatrics GER3`),
`_BY_DESTINATION:208` (`N-4` From column).

## `scripts/` — TOOLS NOW COMMITTED, WITH KNOWN-ANSWER TESTS

**Answering the second question directly: before today, NO tool in this project was committed.**
Both defects were one-off corrections inside the runs that found them. The entire toolchain
lived in a session scratchpad that is destroyed when the session ends, so the next session began
with nothing and the next author would have hit both again.

**`gapcheck.py` — which CLAUDE.md §1.3 cites throughout as mandatory before any `ABSENT`
verdict, and describes as the tool that "cannot truncate" and "refuses to report zero as a
verdict" — is still not in this repository.** Same shape as `PENDING_GUIDELINE_CHECKS.md`: a
thing the rules require, that does not exist here.

Now committed and self-testing (`scripts/checkall.sh`, all self-tests passing):

- **`check_dividers.py`** — enforces the `SOURCE:` convention. Its self-test includes **the
  exact string that produced the 60 false dangling pointers** and asserts it is rejected. Run
  against the vault: **347 dividers, all conforming.** **The convention is now enforced rather
  than remembered.**
- **`verify_move.py`** — the fixed block verifier. Its self-test builds a section with
  subheadings, confirms the fixed rule keeps them, **and reproduces the old rule to show it
  truncates** — the bug is pinned by a test that fails if it returns.
- **`reanchor.py`** — resolves a paraphrased heading to its current file and line. Self-test
  uses the thyroid-panel paraphrase that defeated exact matching.
- `dangling.py`, `misaimed.py`, `drift.py`, `xref.py`, `sections.py` — as used throughout.

**What is still NOT automated:** nothing forces a row's line number to be re-checked before
execution. `reanchor.py` makes it cheap; only the banner makes it expected.
