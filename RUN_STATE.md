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
- [ ] Cardio_merged.md            <-- RESUME HERE
- [ ] Resp_merged.md
- [ ] Renal and Urology_merged.md
- [ ] Endocrine and metabolics_merged.md
- [ ] Neuro_merged.md
- [ ] Heme Onc_merged.md
- [ ] Infectious Disease_merged.md
- [ ] MSK_merged.md
- [ ] Derm_merged.md
- [ ] OBGYN_merged.md
- [ ] Pediatrics_merged.md
- [ ] Psychiatry_merged.md
- [ ] Geriatrics_merged.md
- [ ] Anaes_merged.md
- [ ] Emergency and Crit Care_merged.md
- [ ] ENT_merged.md
- [ ] Opthalm_merged.md
- [ ] GP_merged.md
- [ ] **Clinical Process set (16 files)** — file-combination output, separate
- [ ] **Consolidated report** — moves by destination file · all in-text flags · groupings by
      confidence · anything unplaceable

## Cross-file items already open (must survive to the consolidated report)
- ENT → GI: Barrett's + oesophageal carcinoma (M-R1). ENT_merged L662 stale pointer `03.08`.
- GI → Emergency: paracetamol (M-8) and ascending cholangitis (M-9) as **deliberate duplicates**.
- Carcinoid split GI §0.15 / Derm L2084–2100 / Endocrine (M-13).
- Alcohol withdrawal split GI §0.6.1 / Neuro §0.1 L4077 + L804 / Psychiatry L917 + L1268 (M-5).
