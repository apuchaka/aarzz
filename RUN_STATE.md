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
