---
type: analysis
scope: all proposed moves, grouped by destination
status: PROPOSALS ONLY — nothing in this file has been executed
---

# All moves, by destination

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


**248 move rows · 15 destination blocks · 0 executed.**

The per-file flag files list moves **by source**, which answers *"what does this file lose?"*
This answers *"what does each destination gain?"* — the question you have to answer to approve
a destination.

**Every row here is a proposal.** The only content moves executed in this run are A1's
(`N1`–`N8` → Psychiatry, `GER3`/`GER4` → the new files), and they are not in this table
because they are done.

## How to read the Evidence column

You said: *"You said only 0.9% of numeric pointers can be validated, so absence of inbound
references is weak evidence — mark it per row rather than letting it read as measured."*
That is what this column does.

| Value | Meaning | Count |
|---|---|---:|
| `content` | The argument is what the section says. No inbound figure is cited. | **217** |
| `inbound-corrob.` | An inbound count is quoted alongside a content argument. Remove the count and the row still stands. | **19** |
| **`inbound-PRIMARY`** | **The inbound distribution IS the argument.** Remove it and little is left. | **12** |

**Only 31 of 248 rows cite inbound-reference evidence at all**, and only **12** lean on it.
That is the honest scope of the weak evidence — it is not diffused through the analysis, it
is concentrated in twelve rows, every one of which is named in a block narrative below.

> [!warning] **The first version of this column mis-marked three rows, and the cause is
> CLAUDE.md rule 9 in its exact documented form.** I keyed the classification on the row ID
> alone. **`P-5`, `P-6` and `P-7` each exist in TWO flag files** (GP and Paediatrics), as do
> **`R-2`, `R-3` and `R-6`** (Resp and Geriatrics) — so `Pediatrics P-6` (growth charts) was
> silently marked with `GP P-6`'s evidence class, and `Geriatrics R-6` (osteoporosis) with
> `Resp R-6`'s. Found by counting the emitted column and getting **13 / 213 / 22** where I
> had asserted 12 / 205 / 31. **Re-keyed on `(file, id)`; the counts above are the corrected
> output, quoted from the run.**

> [!warning] **The 0.9% figure, restated so it travels with the rows.**
> Of **2,416** numeric wikilink pointers in the vault, only **21** carry a topic name that
> allows validation. Of those 21, **35% were wrong** — 7 misaimed pointers found by
> `misaimed.py` after `dangling.py` had called them clean. **So an inbound count tells you how
> many links exist, not how many are correct, and a zero tells you nothing at all.**
> Twelve rows in this file rest on that. They are marked, not removed.


---

## Investigation-Interpretation.md

**59 rows** · 1 rest primarily on inbound-reference distribution · 4 cite it as corroboration · 54 rest on content reasoning alone.

**Gains: 59 rows from 12 system files** — the largest single destination in the corpus, and
the one that changes character rather than merely growing.

**What it gains, by axis:**
- **Haematology** (`H-2`–`H-9`, 8 rows) — the full blood count, coagulation screen, iron
  studies, anaemia by MCV and reticulocyte index, immunohaematology, plus the remaining 20
  entries of `NEW_Investigations_Haematology` and `_Part2`.
- **Biochemistry and general** (`P-1`–`P-6`, 6 rows) — inflammatory markers, albumin, ALP,
  LDH, urate, ammonia, caeruloplasmin, calcitonin, plus genetics and molecular testing.
- **Renal and urinary** (`RU-5`–`RU-13`, 7 rows) — urinalysis, ACR, renal function panel,
  PSA, cytology, uroflowmetry, urodynamics, 24-hour copper, Bence-Jones.
- **Respiratory** (`R-1`–`R-9`, 9 rows) — PFTs, oximetry, sleep studies, sputum, sweat
  chloride, TB screening, V/Q, nasopharyngeal swab.
- **Serology and micro** (`I-2`–`I-8`, 7 rows) — autoimmune, vasculitis, coeliac, gram
  stain, HIV, syphilis, monospot.
- **Obstetric and gynaecological** (`B-5`–`B-9`, 5 rows) — cervical screening, swabs,
  hormone panel, prenatal screening, CVS, amniocentesis, Kleihauer-Betke, fetal fibronectin.
- **Endocrine** (`E-1`–`E-6`, 6 rows) — thyroid panel and imaging, glucose/HbA1c/OGTT,
  prolactin, ARR, ABG reference values, acid-base framework.
- **Cardiology** (`C-2`, `C-3`) — **ECG interpretation and its twelve subsections**, plus
  the cardiac-territory table.
- Singles from MSK (`K-13`–`K-15`), Neuro (`N-1`, `N-2`), Paediatrics (`P-6`, `P-7`),
  Anaes (`A-5`).

> [!danger] **This block contains nine known duplications and they must be marked, not merged.**
> Your PART B ruling already covers it: *"where a move would land content next to an existing
> copy — the nine Investigation-Interpretation duplicates — move it and mark the pair, never
> merge."* The destination already holds sections at `§1.2`, `§1.3`, `§1.5`, `§1.7`, `§1.11`,
> `§1.13`–`§1.21` that the incoming rows name explicitly. Every such row carries the
> destination section number in the table below so the pairing is pre-identified.

> [!warning] **`C-2` is structural finding 3 and it is the reason this block is not routine.**
> **ECG interpretation is absent from the entire Clinical Process set.** Its only two
> section-level homes in the vault are inside `Cardio_merged.md`. Moving it does not
> reorganise an existing section — it creates the corpus's first general ECG entry.

**Evidence quality: 54 of 59 rows rest on content reasoning alone**, i.e. the section
describes how to read a test rather than what a result means in one disease — the standing
rule applied directly. **One** rests primarily on inbound distribution: **`GP P-6`**, and it
does so because `## 0.14 Genetic Risk Assessment` overlaps `Heme 10_11b Genetic Cancer **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)**
Predisposition Syndromes`, **which has 3 inbound, ALL from GP** — one of the three two-way
disagreements under A4. **No row in this block argues from an absence of pointers.**

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `A-5` | Anaes | `## 0.6 Group & Hold / Crossmatch` | 232 | **Heme Onc / Investigation-Interpretation** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `C-2` | Cardio | `## 0.12 ECG Interpretation` + `.1`–`.12` (P wave, PR, AV blocks, QRS, BBB, axis, ST, T wave, chamber hypertrophy, athlete variants, hypothermia, digoxin effect) | 474–546 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `C-3` | Cardio | `### 0.1.1 ECG cardiac territories` | 33 | **Investigation-Interpretation.md**, with C-2 | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `E-1` | Endocrine | `## 0.1 Thyroid Panel (TSH, fT4, fT3, antibodies)` | 3468 | **Investigation-Interpretation.md** | content |
| `E-2` | Endocrine | `## 0.2 Thyroid Ultrasound` · `## 0.3 Radioactive Iodine Uptake and Scintigraphy` | 3497, 3516 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `E-3` | Endocrine | `## 0.4 Glucose / Diabetes Testing (glucose, HbA1c, OGTT)` | 3536 | **Investigation-Interpretation.md** | content |
| `E-4` | Endocrine | `## 0.5 Prolactin` · `## 0.6 Renin–Aldosterone (ARR)` | 3558, 3575 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `E-5` | Endocrine | `### 0.20.6 Arterial Blood Gas Reference Values` | 768 | **Investigation-Interpretation.md §1.5** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `E-6` | Endocrine | `## 0.1 Acid-Base Interpretation — Framework` (F0-2) | 1077 | **Investigation-Interpretation.md §1.5** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `P-1` | GP | `## 0.1 Inflammatory Markers (CRP, ESR, Procalcitonin)` | 186 | **Investigation-Interpretation.md §1.21** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `P-2` | GP | `## 0.2 Albumin` · `## 0.3 ALP` · `## 0.4 LDH` · `## 0.5 Uric Acid` · `## 0.6 Ammonia` | 209–337 | **Investigation-Interpretation.md** | content |
| `P-3` | GP | `## 0.7 Serum Ceruloplasmin` | 338 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `P-4` | GP | `## 0.8 Calcitonin` | 364 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `P-5` | GP | `## 0.9 Gallium Scan` · `## 0.10 Incisional Biopsy` · `## 0.11 Stains (histochemical and immunohistochemistry)` | 387–465 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `P-6` | GP | `## 0.14 Genetic Risk Assessment` · `## 0.15 Genetics and Molecular Testing` · `## 0.16 Pharmacogenomic Assessment` | 519–597 | **Investigation-Interpretation.md** | **inbound-PRIMARY** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `H-2` | Heme | `## CBC & Peripheral Blood` | 3240 | **Investigation-Interpretation.md §1.11** | content |
| `H-3` | Heme | `## 0.11 Coagulation Profile (PT/INR, APTT, Fibrinogen, D-dimer)` | 3366 | **Investigation-Interpretation.md §1.17** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `H-4` | Heme | `## 0.1 Interpreting the Coagulation Screen` (J3) | 2160 | **Investigation-Interpretation.md §1.17** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `H-5` | Heme | `## 0.9 How to interpret blood results — a quick approach` | 117 | **Investigation-Interpretation.md §1.11** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `H-6` | Heme | `## Iron studies interpretation` | 426 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `H-7` | Heme | `## Anaemia — DDx by MCV and reticulocyte index` | 408 | **Investigation-Interpretation.md** | content |
| `H-8` | Heme | `## Immunohematology (Blood Group & Rh, DAT)` | 3305 | **Investigation-Interpretation.md** | content |
| `H-9` | Heme | remaining 20 entries of `NEW_Investigations_Haematology` + `_Part2` (B12, MMA, homocysteine, anti-IF, APCA, haptoglobin, Hb electrophoresis, EPO, factor VIII, vWF, ADAMTS13, HIT ELISA, SRA, flow cytometry, marrow/node biopsy, SPEP/SFLC, β2-microglobulin, osmotic fragility, sickle solubility, Schilling, lymphoscintigraphy) | 3251–3686 | **Investigation-Interpretation.md** | content |
| `I-2` | Infectious | `## 0.19 Autoimmune / Rheumatological Serology (ANA, anti-La/SSB, Scl-70, histone, myositis)` | 3464 | **Investigation-Interpretation.md §1.16** | content |
| `I-3` | Infectious | `## 0.20 Positive Autoimmune Serology (approach to an unexpected positive)` | 3490 | **Investigation-Interpretation.md §1.16** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `I-4` | Infectious | `## 0.21 Vasculitis Serology (ANCA, PR3, MPO, anti-GBM)` | 3511 | **Investigation-Interpretation.md §1.16** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `I-5` | Infectious | `## 0.18 Coeliac Serology (anti-tTG IgA, DGP)` | 3444 | **Investigation-Interpretation.md**; serves **GI §0.17 Coeliac Disease** | content |
| `I-6` | Infectious | `## 0.1 Gram Stain` · `## 0.2 Microbiology Panel (Wound C&S)` · `## 0.3 Viral Culture` | 3104–3158 | **Investigation-Interpretation.md §1.18** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `I-7` | Infectious | `## 0.9 Stool & Fecal Studies` (culture, multiplex PCR, O/C/P, **faecal calprotectin, FOBT/FIT**) | 3253 | **Investigation-Interpretation.md**; calprotectin and FIT serve **GI** (IBD, bowel screening) | content |
| `I-8` | Infectious | `## 0.12 HIV Panel` · `## 0.13 Western Blot` · `## 0.14 Syphilis Panel` · `## 0.15 Monospot` · `## 0.16 Parvovirus Serology` · `## 0.17 ASOT / anti-DNase B` | 3308–3443 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `K-13` | MSK | `## 0.6 Joint Aspiration and Synovial Fluid Interpretation` (L1) | 2161 | **Investigation-Interpretation.md §1.15** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `K-14` | MSK | `## 0.6 Autoantibody and Serology Interpretation` (L2) | 2471 | **Investigation-Interpretation.md §1.16** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `K-15` | MSK | `## 0.1 Describing a Fracture` (L7) | 3505 | **Investigation-Interpretation.md §1.7** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `N-1` | Neuro | `### CSF Interpretation` (table: normal/bacterial/viral/TB/fungal) | 707 | **Investigation-Interpretation.md §1.13** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `N-2` | Neuro | `### Who gets a CT head for head injury?` | 1452 | **Investigation-Interpretation.md §1.2** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `B-5` | OBGYN | `## 0.1 Cervical Screening Test and Abnormality (Australian NCSP)` · `## 0.2 Liquid-Based Cytology` | 3666, 3696 | **Investigation-Interpretation.md** | content |
| `B-6` | OBGYN | `## 0.3 Genital / Cervical Swab Panel` | 3718 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `B-7` | OBGYN | `## 0.4 Hormone Panel (Gynaecological / Reproductive)` | 3744 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `B-8` | OBGYN | `## 0.5 Prenatal Screening Panel` · `## 0.6 CVS` · `## 0.7 Amniocentesis` · `## 0.8 Cordocentesis` | 3769–3858 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `B-9` | OBGYN | `## 0.9 Kleihauer-Betke` · `## 0.10 Ferning and Nitrazine` · `## 0.11 Fetal Fibronectin` · `## 0.12 Biophysical Profile` | 3859–3964 | **Investigation-Interpretation.md** | content |
| `P-6` | Pediatrics | `## 0.1 Measuring and Plotting Growth` (M4) | 3281 | **Investigation-Interpretation.md §1.19** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `P-7` | Pediatrics | `## Anaemia in children — approach` + `### Approach to haemolysis` (15_14) | 1528, 1542 | **Investigation-Interpretation.md §1.20** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `RU-5` | Renal | `## 0.1 Urinalysis Panel (Dipstick, pH, SG, Microscopy, Culture)` | 1780 | **Investigation-Interpretation.md §1.14** | content |
| `RU-6` | Renal | `## 0.3 Renal Function Panel (Urea, Creatinine, eGFR, Electrolytes)` | 1819 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `RU-7` | Renal | `## 0.2 Urine ACR` | 1801 | **Investigation-Interpretation.md** | content |
| `RU-8` | Renal | `## 0.5 Elevated PSA` | 1858 | **Investigation-Interpretation.md** | content |
| `RU-9` | Renal | `## 0.6 Urine Cytology` · `## 0.7 Uroflowmetry` · `## 0.8 Urodynamic Studies` | 1877, 1891, 1905 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `RU-10` | Renal | `## 0.11 24-hour Urine Copper` | 1958 | **Investigation-Interpretation.md**; content serves `GI §0.7 Wilson's Disease` | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `RU-11` | Renal | `## 0.12 Urine Protein Electrophoresis / Bence-Jones` | 1977 | **Investigation-Interpretation.md**; serves `Renal §0.8 Myeloma Kidney` and Heme Onc | inbound-corrob. |
| `RU-13` | Renal | `## 0.6 Renal Biopsy` (H1) | 970 | **`GER8_Procedure_Addendum`** *or* Investigation-Interpretation | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `R-1` | Resp | `## 0.2 Pulmonary Function Tests (Spirometry, Lung Volumes, DLCO)` | 1013 | **Investigation-Interpretation.md §1.3** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `R-2` | Resp | `## 0.3 Pulse Oximetry (SpO₂)` | 1041 | **Investigation-Interpretation.md** | inbound-corrob. **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `R-3` | Resp | `## 0.4 Sleep Studies (Polysomnography, HSAT)` | 1064 | **Investigation-Interpretation.md** | inbound-corrob. |
| `R-4` | Resp | `## 0.5 Sputum Culture` | 1087 | **Investigation-Interpretation.md** | content |
| `R-5` | Resp | `## 0.6 Sweat Chloride Test` | 1109 | **Investigation-Interpretation.md** | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| `R-6` | Resp | `## 0.7 TB Screening (TST/Mantoux and IGRA)` | 1134 | **Investigation-Interpretation.md** | inbound-corrob. |
| `R-7` | Resp | `## 0.8 V/Q Scan` | 1159 | **Investigation-Interpretation.md** | content |
| `R-8` | Resp | `## 0.1 Nasopharyngeal Swab` | 992 | **Investigation-Interpretation.md** *or* `NEW_Exam_Manoeuvres_and_Procedures` | content |
| `R-9` | Resp | `### 0.9.1 Diagnosis of latent TB — Mantoux test` | 440 | **Investigation-Interpretation.md**, with R-6 | content **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |


---

## Examination.md

**24 rows** · 1 rest primarily on inbound-reference distribution · 2 cite it as corroboration · 21 rest on content reasoning alone.

**Gains: 24 rows** — 22 named sections plus roughly 60 `**Examination:**` blocks embedded
inside disease entries.

The standing rule from `M-16` is doing all the work here: *how to elicit a sign* goes to
`Examination.md`; *this sign is positive in this disease* stays. Several rows name the
destination section that already exists — `§1.1`, `§1.2`, `§1.5`, `§1.12`, `§1.15`, `§1.17`,
`§1.18`, `§1.19`, `§1.20`, `§1.21.2`, `§1.22` — which makes them duplicate-pair rows under
your PART B ruling, not fresh additions.

> [!note] **`T-1` is the clearest case in the corpus.** `Examination.md` already has
> **§1.19 "Otoscopy"** and **§1.20 "Rinne and Weber Tests"**; `ENT F1 §0.1 Examining the Ear
> and Assessing Hearing` is the same procedure written a second time in a system file. The
> ENT sources `13_02` and `13_03` carry Examination ×5 and ×4 inbound, so the Clinical
> Process set is already the dominant referrer.

**`D-14` rests primarily on inbound distribution** — `09_02` has 10 inbound and **the entire
referrer profile is the Clinical Process set** (Examination ×4, Communication ×2,
History-Taking). Marked in the table. It is the strongest inbound argument in the corpus and
it is still only 10 pointers, of which the 0.9% validation rate applies.

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `A-1` | Anaes | `## 0.5 Pre-Operative Assessment` + its `**History:**` and `**Examination:**` blocks | 197–231 | **Examination.md §1.12** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `A-2` | Anaes | `## 0.1 Preoperative Assessment` (AN1) · `## 0.2 Airway Assessment and Anaesthetic Technique` (AN1) | 344, 388 | **Examination.md §1.12** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `C-4` | Cardio | `> [!info] Dynamic manoeuvres` (RILE; Valsalva/standing; squatting/handgrip; the HOCM and MVP exceptions) | 2483 | **Examination.md** | content |
| `C-5` | Cardio | `### 0.21.2 Heart sounds`, `### 0.21.4 Pulses` | 790, 800 | **Examination.md §1.5** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `C-6` | Cardio | `> [!tip] Valsalva manoeuvre` (L438) and `> [!info] Vagal manoeuvres — do them properly` (L2051) | 438, 2051 | **Examination.md** | content |
| `C-7` | Cardio | `> [!danger] Fundoscopy is the examination that most often makes the diagnosis` | 1927 | **Examination.md §1.18** (Fundoscopy already exists there) | content |
| `D-12` | Derm | `## Skin lesion morphology — reference terms` | 942 | **Examination.md §1.15** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `D-13` | Derm | `## 0.1 Describing a Rash` (G1) | 1048 | **Examination.md §1.15** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `D-14` | Derm | `## 0.1 Assessing a Pigmented Lesion` (G5) | 1873 | **Examination.md §1.15** | **inbound-PRIMARY** **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `D-16` | Derm | `## 0.5 Nails` (G5) | 1985 | **flag — Examination** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `T-1` | ENT | `## 0.1 Examining the Ear and Assessing Hearing` (F1) | 852 | **Examination.md §1.19/§1.20** | inbound-corrob. **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `X-1` | Emergency | `## 0.1 The A–E Approach` (F0-4) | 3042 | **Examination.md §1.1** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `X-2` | Emergency | `## 0.1 The Deteriorating Patient — Recognition` (A1) · `## 0.2 Vital Signs and Early Warning Scores` (Examination §1.2's topic) | 11 | **flag — Examination.md §1.2** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `K-16` | MSK | `## Dermatomes — quick reference` + the 5 nerve-root/peripheral-nerve tables + `## Brachial Plexus Injury` (11_07a) | 797–891 | **Examination.md** | inbound-corrob. **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `K-18` | MSK | `> Tinel's sign` · `> Phalen's sign` (11_03) | 395, 396 | **Examination.md** | content |
| `N-3` | Neuro | `### Glasgow Coma Scale (GCS)` | 719 | **Examination.md** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `N-4` | **Psychiatry** (was Neuro; A1 `f5e49c9`) | `## 0.1 Psychiatric Assessment and the Mental State Examination` (N1) | 3841 | **Examination.md §1.22** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `N-5` | Neuro | `## 0.2 Acute Vestibular Syndrome and the HINTS Examination` (D5) | 3016 | **Examination.md §1.21.2** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `N-6` | Neuro | `## 0.1 Localising the Lesion` (D4) | 2700 | **Examination.md** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `N-7` | Neuro | `## Brain Lesion Localisation` | 952 | **Examination.md** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `B-2` | OBGYN | `## 0.1 Triple Assessment` (O7) | 5499 | **Examination.md §1.17** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `E-1` | Opthalm | `## 0.2 Drugs for Eye Examinations and Procedures` (NEW_Drugs_11) | 1506 | **Examination.md §1.18** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `E-3` | Opthalm | `## Eye Anatomy Reference` | 6 | **flag — Examination.md** | content **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| `P-4` | Pediatrics | `> Get down to the child's level, introduce yourself to THEM…` (M1 §0.6 Practical Paediatrics) | 2806–2851 | **Examination.md / Communication.md** | content |


---

## History-Taking.md

**7 rows** · 0 rest primarily on inbound-reference distribution · 0 cite it as corroboration · 7 rest on content reasoning alone.

**Gains: 7 named rows**, plus its share of the ~60 paired blocks in the next block.

Sexual history arrives from **three separate files** — that is the finding, not the volume.
The rows are pure standing-rule applications: a history schema in a system file, with a
pointer left behind. **No row here rests on inbound evidence at all.**

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `C-8` | Cardio | `> [!danger] The collateral history is the investigation` | 2268 | **History-Taking.md** | content |
| `R-4` | Geriatrics | `### Distinguishing a fall from a collapse — do this first` | 18 | **History-Taking.md** | content **✅ EXECUTED 2026-09-01 → `History-Taking.md` (c5df174)** |
| `I-1` | Infectious | `## The STI Check — Sexual History, What to Test, and When` + `### Taking a sexual history` + `### What a standard asymptomatic check consists of` + `### Window periods` + `### After the result` | 870–923 | **History-Taking.md** | content **✅ EXECUTED 2026-09-01 → `History-Taking.md` (c5df174)** |
| `B-1` | OBGYN | `## 0.1 The Sexual History and STI Assessment` (O6) | 5185 | **History-Taking.md** | content **✅ EXECUTED 2026-09-01 → `History-Taking.md` (c5df174)** |
| `P-1` | Pediatrics | `## 0.2 The HEEADSSS Psychosocial Assessment` (M7) | 3970 | **History-Taking.md** | content **✅ EXECUTED 2026-09-01 → `History-Taking.md` (c5df174)** |
| `R-10` | Resp | `> [!danger] Ask the occupational history — it is systematically not taken` | 1374 | **History-Taking.md** | content |
| `R-11` | Resp | `> [!warning] Hypersensitivity pneumonitis — take the exposure history properly` | 1334 | **History-Taking.md** | content |


---

## Examination.md + History-Taking.md — paired blocks

**12 rows** · 0 rest primarily on inbound-reference distribution · 1 cite it as corroboration · 11 rest on content reasoning alone.

**Gains: 12 rows, each naming both destinations** — a `**Focused Hx:**` and an
`**Examination:**` block sitting adjacent inside one disease entry, which the standing rule
splits in two directions at once.

These are the rows most likely to be mis-executed: the two halves must go to different files
and **the pointer left behind has to name both**. `OBGYN B-4` alone is twelve such pairs in
`NEW_Obstetrics`.

> [!note] **`B-4`'s "both sources have zero inbound" is cited but is not the argument.**
> The argument is the standing rule. I have marked it `inbound-corrob.` rather than
> `inbound-PRIMARY` for that reason — flagging it here because at a glance the row reads as
> if absence of references were the case for moving it, and it is not.

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `C-9` | Cardio | **14 `**Focused Hx:**` + 14 `**Examination:**` blocks**, all in `NEW_Cardiology_and_Vascular` | 3375–3541 | **History-Taking.md / Examination.md** | content |
| `D-15` | Derm | **5** × `**Focused Hx:**` + **5** × `**Examination:**` in `NEW_Dermatology` *(count corrected 2026-09-01; the row said 6+6)* | 2264–2318 | **History-Taking.md / Examination.md** | content |
| `T-2` | ENT | 4 × `**Focused Hx:**` + 4 × `**Examination:**` in `NEW_ENT_and_Oral` | 1779–1819 | **History-Taking.md / Examination.md** | content |
| `E-14` | Endocrine | `**Focused Hx:**` + `**Examination:**` in `NEW_Acid-Base_Fluids_and_Electrolytes ## Dehydration` | 2852–2853 | **History-Taking.md / Examination.md** | content |
| `R-3` | Geriatrics | `**History:**` + `**Examination:**` blocks under `## Falls in Older People` | 51, 55 | **History-Taking.md / Examination.md** | content |
| `K-17` | MSK | **6** × `**Focused Hx:**` + **6** × `**Examination:**` in `NEW_Orthopaedics_and_Trauma` *(count corrected 2026-09-01; the row said 8+8)* and `NEW_Rheumatology_and_Immunology` | 4889–5021 | **History-Taking.md / Examination.md** | content |
| `N-8` | Neuro | 8 × `**Focused Hx:**` + 8 × `**Examination:**` in `NEW_Neurology` | 5695–5830 | **History-Taking.md / Examination.md** | content |
| `B-4` | OBGYN | **6** × `**Focused Hx:**` + **6** × `**Examination:**` in `NEW_Obstetrics` *(count corrected 2026-09-01; the row said 12 blocks)* and `NEW_Gynaecology_and_Reproductive` | 4000–3628 | **History-Taking.md / Examination.md** | inbound-corrob. |
| `E-2` | Opthalm | 4 × `**Focused Hx:**` + 4 × `**Examination:**` in `NEW_Ophthalmology` | 1632–1692 | **History-Taking.md / Examination.md** | content |
| `Y-9` | Psychiatry | `**Focused Hx:** / **Examination:**` in `NEW_Psychiatry ## Acute Behavioural Disturbance` | **3019–3020** | **History-Taking.md / Examination.md** | content |
| `RU-14` | Renal | 2 × `**Focused Hx:**` + 2 × `**Examination:**` in `NEW_Renal_and_Urology` | 2043–2072 | **History-Taking.md / Examination.md**. L2044 is explicit technique: *"examine the patient standing and lying, with consent and a chaperone"*; L2072 *"palpate and percuss for a distended bladder"* | content |
| `R-12` | Resp | **2** × `**Focused Hx:**` + **3** × `**Examination:**` in `NEW_Respiratory` *(count corrected 2026-09-01; the row said 3+3)* | 1221–1264 | **History-Taking.md / Examination.md** | content |


---

## Communication.md

**3 rows** · 0 rest primarily on inbound-reference distribution · 0 cite it as corroboration · 3 rest on content reasoning alone.

**Gains: 3 rows.** Small, and two of the three are `arguable` rather than confident —
breaking-bad-news and consent-conversation content that could equally stay with its disease.
**No inbound evidence cited for any of the three.**

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `R-5` | Geriatrics | `### Communication and follow-up` (discharge planning) | 278 | **arguable — Communication.md** | content |
| `B-3` | OBGYN | `## 0.1 Pre-pregnancy counselling` (16_01-05) | 12 | **arguable — Communication.md** | content |
| `P-2` | Pediatrics | `## 0.1 Adolescent Development and the Consultation` (M7) | 3944 | **Communication.md** | content |


---

## NEW — Procedures.md

**5 rows** · 0 rest primarily on inbound-reference distribution · 1 cite it as corroboration · 4 rest on content reasoning alone.

**Gains: 5 sources.** `Procedures.md` was created empty under A2 with a manifest; this is
what the manifest names.

**`GER8_Procedure_Addendum` is the load-bearing one** — it is currently filed under
Geriatrics for the same reason `GER3` and `GER4` were, the `GER` prefix, and it has no
geriatric content. `NEW_Exam_Manoeuvres_and_Procedures` Part 2 is its natural partner.
`Psychiatry Y-8` (ECT — consent, workup, complications) and `Renal RU-13` (renal biopsy)
are procedure entries currently sitting in disease files.

> [!warning] **`RU-13` is listed in two blocks on purpose** — the flag reads
> *"`GER8_Procedure_Addendum` **or** Investigation-Interpretation"*, because a renal biopsy
> is both a procedure and a source of a result to interpret. **Unresolved, deliberately.**

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `A-3` | Anaes | `## 0.2 Airway Adjuncts` +`.1 OPA` +`.2 NPA` +`.3 supraglottic` +`.4 BVM` +`.5 ETT` +`.6 laryngoscope` +`.7 tracheostomies` | 64–113 | **`NEW_Exam_Manoeuvres_and_Procedures` / `GER8_Procedure_Addendum`** | content |
| `A-4` | Anaes | `## 0.3 Regional / Local Anaesthesia` +`.1 nerve blocks` +`.2 risks` +`.3 neuraxial` +`.4 epidural` +`.5 spinal` | 114–171 | **flag — procedures** | content |
| `X-4` | Emergency | `## 0.7 Mechanical Ventilation` · `## 0.8 Procedural Sedation` · `## 0.11 Fascia Iliaca Block` (F0-4) | 3241, 3270, 3359 | **`GER8_Procedure_Addendum` / `NEW_Exam_Manoeuvres_and_Procedures`** | content |
| `Y-8` | Psychiatry | `14_05d Electroconvulsive Therapy` | **738–758** | **flag — procedures** | inbound-corrob. |
| `RU-12` | Renal | `## 0.5 Catheters` (H2) | 1122 | **`NEW_Exam_Manoeuvres_and_Procedures` / `GER8_Procedure_Addendum`** | content |


---

## NEW — Safeguarding.md

**2 rows** · 0 rest primarily on inbound-reference distribution · 1 cite it as corroboration · 1 rest on content reasoning alone.

**Gains: 2 move rows — but that count understates it, and this is structural finding 4.**

**Safeguarding is a four-way split whose pieces do not overlap**, and the largest piece was
in Geriatrics as `GER4` (37 inbound, **14 from Paediatrics, 1 internal**). `GER4` has already
moved under A1/A2 and now *is* `Safeguarding.md`'s founding content. The two rows below are
what would join it: **`Pediatrics P-5` (`15_24a` Non-Accidental Injury and Sexual Abuse,
whole source, 14 inbound with Communication ×4)** and **`OBGYN B-13` (FGM)**.

The four pieces: elder abuse (`GER4`), child protection (`15_24a`), FGM (`OBGYN`), and
domestic/family violence. **None duplicates another** — which is why this is a new file
rather than a consolidation.

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `B-13` | OBGYN | `## Female genital mutilation (FGM)` | 1956 | **arguable — `NEW_Safeguarding_and_Forensic`** | content |
| `P-5` | Pediatrics | `15_24a Non-Accidental Injury and Sexual Abuse` (whole source) | 2541–2581 | **`NEW_Safeguarding_and_Forensic`** | inbound-corrob. |


---

## NEW — Preventive-Health.md

**2 rows** · 0 rest primarily on inbound-reference distribution · 1 cite it as corroboration · 1 rest on content reasoning alone.

**Gains: 2 move rows on top of `GER3`, which has already moved under A1/A2** (31 inbound).

The finding this file settles is `GP P-7`: **preventive health and screening is in six
sources** — `GP 12_01`, `GER3 §0.1`–`§0.5`, `PH1_Population_Health_and_Research_Literacy`,
`ID 08_01-03 ## Vaccination Schedule`, `Pediatrics 15_24b`, and `NEW_Drugs_20`. It also
settles the **fourth Austroads driving-fitness home**, which had no owner.

**Nothing is merged by creating the file.** `Preventive-Health.md` currently holds `GER3`
whole plus a rationale header; the other five sources are flagged, not moved.

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `P-7` | GP | `## 0.1 Preventive Medicine and Screening in Australian GP` +`.1 the three national cancer screening programs` +`.2 CV, diabetes and kidney risk` +`.3 immunisation across the lifespan` +`.4 other preventive domains` | 16–79 | **decide as one with GER3 / PH1** | inbound-corrob. |
| `I-10` | Infectious | `## Vaccination Schedule (Australia — NIP)` + `### Influenza vaccination` + `## Passive Immunisation — Immunoglobulin After an Exposure` | 332–404 | **preventive health** — `GER3_Preventive_and_Occupational_Health` (per CLAUDE.md §1.10's mapping) or `PH1` | content |


---

## A10 Ethics, Capacity, Consent and Certification

**4 rows** · 0 rest primarily on inbound-reference distribution · 0 cite it as corroboration · 4 rest on content reasoning alone.

**Gains: 4 rows.** `A10` is an existing Corpus B file, not a new one.

The clearest is **`Psychiatry Y-4` — `## Guardianship — a related but distinct framework`**,
which the section's own first paragraph identifies as the **Guardianship and Administration
Act 1993 (SA)** operating *"instead of or alongside the Mental Health Act"*. It is a capacity
framework filed inside mental health law.

**`Psychiatry Y-5` (the SA Mental Health Act, 9 sections) is listed as `A10` or keep** and is
deliberately unresolved — see the A5 note below, because both copies now carry a verification
warning.

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `I-11` | Infectious | `## Notifiable Diseases (Australia)` **and** `## Notifiable Diseases in Australia — What "Notifiable" Actually Means` | 327, 1313 | **`A10_Ethics__Capacity__Consent_and_Certification` or `PH1`** | content |
| `P-3` | Pediatrics | `## 0.3 Confidentiality, Consent and the Mature Minor` (M7) | 3992 | **`A10_Ethics__Capacity__Consent_and_Certification`** | content |
| `Y-4` | Psychiatry | `## Guardianship — a related but distinct framework` | **900** | **`A10_Ethics__Capacity__Consent_and_Certification`** | content |
| `Y-5` | Psychiatry | `14_06b Mental Health Act and Sectioning` (9 sections: involuntary treatment, CTOs, ITOs, SACAT, interstate transfer, safeguards, police, voluntary inpatients) | **855–904** | **flag — `A10` or keep** | content |


---

## PH1 / AU1 — population health and Australian context

**4 rows** · 0 rest primarily on inbound-reference distribution · 0 cite it as corroboration · 4 rest on content reasoning alone.

**Gains: 4 rows**, all marked `arguable` in their source flag files. `PH1` and `AU1` are
existing Corpus B files.

This block overlaps the Preventive-Health block by design: `P-7` names `PH1` as one of the
six preventive-health sources. **Deciding Preventive-Health.md's scope decides this block**,
which is why the rows are listed rather than recommended.

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `P-10` | GP | `## 0.3 Hospital Avoidance and Potentially Preventable Hospitalisations` +`.1 what an intern can actually do` | 120–145 | **arguable — `PH1`** | content |
| `P-11` | GP | `## 0.4 Continuity of Care, and What Makes General Practice Different` +`.1` | 146–176 | **arguable — `PH1` or keep** | content |
| `H-18` | Heme | `## Cancer Outcomes in Aboriginal and Torres Strait Islander Australians` | 1487 | **arguable — `AU1_Australian_Health_Context_and_ATSI_Health`** | content |
| `Y-7` | Psychiatry | `## Gambling disorder (gambling-related harms)` | **1045** | **arguable — GP / PH1** | content |


---

## Emergency and Crit Care

**8 rows** · 0 rest primarily on inbound-reference distribution · 1 cite it as corroboration · 7 rest on content reasoning alone.

**Gains: 8 rows**, three of which you approved in message 2 (`M-8` paracetamol overdose and
King's College criteria, `M-9` ascending cholangitis, `M-6` abdominal trauma) and **one of
which you have since withdrawn** (`M-6`).

> [!danger] **`M-8` and `M-9` create duplicates on purpose, per your own instruction:**
> *"Move GI's copy in alongside. Do NOT merge or reconcile them. I will do that by hand and
> I want both versions in front of me."* Recorded here so the instruction travels with the
> destination rather than living only in the GI flag file.

**`Psychiatry Y-1` is the largest new row** — `14a-2 Overdose and Poisoning Management`
(`§0.1` by-agent table, `§0.2` digoxin, `§0.3` salicylate, `§0.4` TCA). Emergency already
holds `A5 §0.1 The Poisoned Patient`, `§0.2 TCA Overdose`, `F0-1 §0.1`–`§0.8` and
`NEW_Drugs_04 Antidotes and Antivenoms`. **Salicylate additionally duplicates
`Endocrine F0-2 §0.8`** — so this row is a three-way duplication, not a two-way.

**`M-6` is now in the trauma report instead**, which recommends deciding trauma as one
question across four files rather than executing this row.

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `D-1` | Derm | `## Anaphylaxis` | 6 | **Emergency / ID(K4)** | content |
| `H-13` | Heme | `## Lead poisoning` | 457 | **Emergency / toxicology** | content |
| `H-14` | Heme | `## Methaemoglobinaemia` | 718 | **Emergency / toxicology** | content |
| `I-13` | Infectious | `## Sepsis` | 1242 | **flag — Emergency owns it** | content |
| `K-19` | MSK | `## Burns and Scalds` + `### First aid` + `### Assessment — depth and TBSA` + `### Mx` (11_09b) | 1183–1263 | **Emergency** | content |
| `N-16` | Neuro | `## Serotonin Syndrome and NMS` | 356 | **Emergency** | content |
| `N-17` | Neuro | `## Opioid Toxicity` | 376 | **Emergency** | content |
| `Y-1` | Psychiatry | `14a-2 Overdose and Poisoning Management` — `§0.1 by agent` · `§0.2 Digoxin` · `§0.3 Salicylate` · `§0.4 TCA` | **1079–1120** | **Emergency** | inbound-corrob. |


---

## Paediatrics

**11 rows** · 2 rest primarily on inbound-reference distribution · 1 cite it as corroboration · 8 rest on content reasoning alone.

**Gains: 11 rows — and all eleven are duplications, none is a gap.**

That is the finding for this destination and it is unusual: every proposed move lands beside
content Paediatrics already has. Under your PART B ruling each becomes a marked pair.

**Two rows rest primarily on inbound distribution and they point in opposite directions:**
- **`Heme H-12`** — `## Primary Immunodeficiencies` (whole source, 15 sections) has
  **3 inbound: Paediatrics ×2, ID ×1, none from haematology.** `Pediatrics 15_15b` is
  *"Primary Immunodeficiencies and SCID"*. The inbound argument supports moving it out of Heme.
- **`MSK K-26`** — `11_10 Paediatric Orthopaedics` (12 sections) has **8 inbound: MSK ×3,
  Examination ×2, History-Taking, NEW_Exam_Manoeuvres.** Here the inbound argument runs
  **against** the proposed destination: the dominant referrer is MSK itself. The flag records
  the counter-argument (*"they are orthopaedic conditions"*) rather than suppressing it.

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `E-8` | Endocrine | `## 0.8 Carnitine Levels` · `## 0.9 Plasma Amino Acid Screen` | 3615, 3632 | **Paediatrics** | content |
| `E-9` | Endocrine | `## 0.4 Paediatric Diabetic Ketoacidosis` (F0-2) | 1173 | **arguable — Paediatrics** | content |
| `H-11` | Heme | `### Haemolytic uraemic syndrome (HUS)` | 630 | **decide with Paediatrics** | content |
| `H-12` | Heme | `## Primary Immunodeficiencies` (whole source, 15 sections) | 251–372 | **decide with Paediatrics / ID** | **inbound-PRIMARY** |
| `K-24` | MSK | `## Henoch-Schönlein purpura` (12_04) | 1918 | **flag — Paediatrics** | content |
| `K-26` | MSK | `## 11_10 Paediatric Orthopaedics` (12 sections: JIA, transient synovitis, DDH, Perthes, SCFE, postural variants, rickets, Osgood-Schlatter, paediatric/Salter-Harris fractures) | 1316–1461 | **arguable — Paediatrics** | inbound-corrob. |
| `N-18` | Neuro | `### Febrile Convulsions` | 794 | **Paediatrics** | content |
| `B-14` | OBGYN | `## Ophthalmia neonatorum` | 825 | **Ophthalmology / Paediatrics** | content |
| `B-15` | OBGYN | `## Birth injuries` | 1054 | **Paediatrics** | content |
| `B-16` | OBGYN | `## 0.5 Routine Postnatal and Newborn Care` (O3) | 4605 | **flag — Paediatrics** | content |
| `Y-6` | Psychiatry | `14_07 Attention Deficit Hyperactivity Disorder` | **908–930** | **decide with Paediatrics** | **inbound-PRIMARY** |


---

## Psychiatry

**3 rows** · 0 rest primarily on inbound-reference distribution · 0 cite it as corroboration · 3 rest on content reasoning alone.

**Gains: 3 rows on top of the eight whole sources delivered by A1.**

A1 is not in this table because it is executed, not proposed. With `N1`–`N8` in place
Psychiatry went from 15 sources to 23 and from 1,405 lines to 3,036. The three remaining rows
are small: content in other files whose subject is psychiatric.

**None rests on inbound evidence.**

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `A-10` | Anaes | `## 0.3 Drugs for Opioid Dependence` | 924 | **Psychiatry** | content |
| `B-10` | OBGYN | `## Puerperal psychosis` (16_10-13) | 1481 | **Psychiatry** | content |
| `B-11` | OBGYN | `### 0.12.8 Psychiatric conditions — drugs in pregnancy` | 536 | **Psychiatry / drug files** | content |


---

## System file → system file

**65 rows** · 7 rest primarily on inbound-reference distribution · 5 cite it as corroboration · 53 rest on content reasoning alone.

**Gains: 65 rows spread across 19 destinations** — no single system file gains more than
about eight. Presented as one block because splitting it into nineteen would bury the pattern.

**Three sub-patterns account for most of it:**

1. **`Emergency A8` foreign bodies fan out by anatomy** (`X-12`–`X-16`, plus `X-11`): ocular
   to Ophthalmology, aural/nasal/oropharyngeal to ENT, rectal to GI, vaginal to OBGYN,
   swallowed to GI *or* ENT. Six rows, one source section, six destinations. **This is a
   presentation-organised section meeting a system-organised corpus**, and it is the cleanest
   example of that collision in the vault.
2. **`Emergency F0-5` organ-specific emergencies return to their systems** (`X-3`, `X-6`–`X-10`):
   BLS/ALS to Cardio, respiratory failure to Resp, pulmonary oedema to Cardio, headache and
   head injury to Neuro, renal colic to Renal, quinsy to ENT. **All flagged as duplicates**,
   not gaps.
3. **`Neuro D7` cranial-nerve content redistributes** (`N-11`, `N-13`, `N-14`): diplopia to
   Ophthalmology, speech/voice/swallowing to ENT, smell and taste to ENT.

> [!danger] **`Cardio B6 §0.4`–`§0.8` is the block you specifically ruled on — "flag §0.4-0.8
> for whichever file each belongs to individually, not as a block" — and doing so exposed a
> problem the block-level view hid.**
> These five rows (`C-10`–`C-14`) are the **only** cluster in the corpus where the inbound
> distribution is the primary argument, and their evidence quality varies sharply:
>
> | Row | Section | Inbound | Reads as |
> |---|---|---|---|
> | `C-10` | Undifferentiated Lump | **19, ZERO from cardiology** (MSK×7, ID×3, ENT×2, Heme×2, Paeds×2, Renal×2, Derm×1) | **decisive that it is not cardiac; silent on where it goes** |
> | `C-13` | Fatigue, Lethargy, Malaise | 8 (MSK×3, Endo×2, Neuro×2, GI×1) | diffuse — supports "general", not a system |
> | `C-14` | Eyelid and Facial Swelling | 7 (Derm×2, Endo×2, Heme×2, Neuro×1) | **no majority at all** — genuinely undecidable on this evidence |
> | `C-12` | Generalised Weakness | 4 (**Endocrine×3**, Neuro×1) | **the evidence contradicts the proposed destination (Neuro)** |
> | `C-11` | Generalised Pain | 2 (both Neuro) | too few to mean anything; the content argument (musculoskeletal) is carrying it |
>
> **`C-12` is the one to look at.** I proposed Neuro on content grounds and the inbound
> distribution points at Endocrine three-to-one. **I have not changed the proposal** — the
> content argument stands and the pointer evidence is weak — but a row where my two lines of
> evidence disagree should not be presented as though they agreed.

**Also in this block: two of the three two-way disagreements.** `Derm D-2` (urticaria and
angioedema) says *decide with ID* while `Infectious I-19` says *flag — Derm*; `Derm D-7`
(carcinoid) says *decide with GI/Endocrine*. Both ends are flagged under A4 and **neither is
resolved**, per your ruling that each file pointing at the other means neither owns it.

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `A-6` | Anaes | `## 0.4 Post-Operative Nausea and Vomiting (PONV)` | 172 | **flag — GI owns antiemetics** | inbound-corrob. |
| `A-8` | Anaes | `## 0.1 Drugs for Gout` +`.1 xanthine oxidase inhibitors` +`.2 other` (NEW_Drugs_03) | 820–862 | **MSK** | content |
| `A-9` | Anaes | `## 0.2 Drugs for Migraine` +`.1 triptans` +`.2 ergots` +`.3 CGRP` +`.4 prevention` | 863–923 | **Neuro** | content |
| `C-10` | Cardio | `## 0.8 Undifferentiated Lump` (B6) | 2995 | **general / MSK or a lump-and-mass home** | **inbound-PRIMARY** |
| `C-11` | Cardio | `## 0.7 Generalised Pain` (B6) | 2959 | **MSK** | **inbound-PRIMARY** |
| `C-12` | Cardio | `## 0.6 Generalised Weakness` (B6) | 2916 | **Neuro** | **inbound-PRIMARY** |
| `C-13` | Cardio | `## 0.5 Fatigue, Lethargy and Malaise` (B6) | 2872 | **GP / general** | **inbound-PRIMARY** |
| `C-14` | Cardio | `## 0.4 Eyelid and Facial Swelling` (B6) | 2833 | **arguable — Ophthalm / ENT / Derm** | **inbound-PRIMARY** |
| `D-2` | Derm | `## Acute urticaria and angioedema` | 38 | **decide with ID** | content |
| `D-5` | Derm | `## Varicella zoster virus / chickenpox` + `### PEP` + `### VZV in pregnancy` + `## Herpes zoster / shingles` | 729–792 | **flag — ID/OBGYN** | content |
| `D-7` | Derm | `## 0.2 The Endocrine and Neoplastic Causes` (G6) — the **carcinoid syndrome** block | 2082–2119 | **decide with GI/Endocrine** | content |
| `D-8` | Derm | `## 0.4 The Systemic Vasculitides` (G3) | 1540 | **flag — MSK owns it** | content |
| `D-9` | Derm | `## 0.6 Cyanosis and Abnormal Skin Colour` (G6) | 2204 | **arguable — Resp/Cardio** | content |
| `T-4` | ENT | `## 0.4 Thyroid Nodules` (F4) | 1532 | **flag — Endocrine** | content |
| `T-8` | ENT | `## Obstructive sleep apnoea` · `## Primary (simple) snoring` (13_05b) | 570, 560 | **flag — Resp** | content |
| `X-3` | Emergency | `## 0.2 Basic Life Support` · `## 0.3 Advanced Life Support — Adult` (F0-4) | 3076, 3110 | **flag — Cardio duplicate** | content |
| `X-6` | Emergency | `## 0.1 Acute Asthma` · `## 0.2 Acute Exacerbation of COPD` · `## 0.4 Severe CAP and ARDS` · `## 0.5 Neuromuscular Respiratory Failure` (F0-5) | 3399–3559 | **flag — Resp** | content |
| `X-7` | Emergency | `## 0.3 Acute Pulmonary Oedema` (F0-5) | 3468 | **flag — Cardio** | content |
| `X-8` | Emergency | `## 0.6 Acute Severe Headache` · `## 0.7 Major Head Injury` · `## 0.8 Minor Head Injury` (F0-5) | 3560–3653 | **flag — Neuro** | content |
| `X-9` | Emergency | `## 0.9 Acute Renal Colic` (F0-5) | 3654 | **flag — Renal** | content |
| `X-10` | Emergency | `## 0.10 Tonsillitis and Peritonsillar Abscess (Quinsy)` (F0-5) | 3689 | **flag — ENT** | content |
| `X-11` | Emergency | `## 0.2 Drugs for Allergic and Inflammatory Eye Conditions` · `## 0.3 Other Drugs for Allergic Eye Conditions` (NEW_Drugs_01) | 3776, 3806 | **Ophthalmology** | content |
| `X-12` | Emergency | `## 0.4 Corneal and Ocular Foreign Body` (A8) · `## 0.4 Chemical Eye Injury` (A7) | 1938, 1723 | **flag — Ophthalmology** | content |
| `X-13` | Emergency | `## 0.2 Aural Foreign Body` · `## 0.3 Nasal Foreign Body` · `## 0.5 Oropharyngeal Foreign Body` (A8) | 1872–1997 | **flag — ENT** | content |
| `X-14` | Emergency | `## 0.7 Rectal Foreign Body` (A8) | 2032 | **flag — GI** | content |
| `X-15` | Emergency | `## 0.8 Vaginal Foreign Body` (A8) | 2064 | **flag — OBGYN** | content |
| `X-16` | Emergency | `## 0.6 Swallowed Foreign Body` (A8) | 1998 | **flag — GI / ENT** | content |
| `E-7` | Endocrine | `## 0.7 G6PD Assay` | 3597 | **Heme Onc** | content |
| `E-10` | Endocrine | `## 0.22 Hypercholesterolaemia` | 802 | **decide with Cardio** | content |
| `E-11` | Endocrine | `### 0.15.7 Perioperative Diabetes Management` | 531 | **arguable — Anaes** | content |
| `E-12` | Endocrine | `## 0.23 Principles of Fluid and Electrolyte Management in Surgical Patients` | 838 | **arguable — Anaes / surgical** | content |
| `R-6` | Geriatrics | `## 0.6 Osteoporosis and Fracture Prevention` (GER1) | 550 | **flag — MSK owns it** | content |
| `R-10` | Geriatrics | `## 0.5 End-of-Life Care and Recognising Dying` · `## 0.6 Advance Care Planning in Practice` (GER2) | 794, 852 | **flag — decide with Heme H-21** | content |
| `H-10` | Heme | `## Postpartum Infection and Thromboembolism` + `### Postpartum (puerperal) infection` + `### Postpartum VTE` | 782–808 | **OBGYN** | content |
| `H-15` | Heme | `## Hereditary angioedema` | 1137 | **Immunology / ID** | content |
| `H-17` | Heme | `## 0.2 Organ transplant` +`.1 matching` +`.2 rejection types` | 1323–1351 | **flag — overlaps Renal** | **inbound-PRIMARY** |
| `H-19` | Heme | `## 10_12 Oncology — Breast` (breast cancer + 8 benign breast conditions) | 1612–1735 | **arguable — OBGYN or a breast home** | inbound-corrob. |
| `H-21` | Heme | `10_11c ## General principles` · `## Conversion between opioids` · `## Symptom management in palliative care` (1563–1611) **and** `J5 §0.4 Palliative Care Principles` (2658) · `§0.5 Symptom Control` (2687) · `§0.6 The Last Days of Life` (2724) |  | **flag — candidate for its own home or Geriatrics/GP.** 11 + 20 inbound, **Anaes ×4, GP, MSK, Geriatrics** — referenced from across the vault, not from haematology. Decide after Geriatrics and GP | content |
| `I-12` | Infectious | `## Mastitis and Breast Abscess` | 1133 | **OBGYN** | content |
| `I-16` | Infectious | `### Acute epiglottitis` | 112 | **flag — ENT owns it** | content |
| `I-17` | Infectious | `### Centor criteria (sore throat)` | 290 | **flag — ENT owns it** | content |
| `I-18` | Infectious | `## 0.5 Allergic Rhinitis and the Atopic March` (K4) | 2379 | **flag — ENT owns it** | content |
| `I-19` | Infectious | `## 0.6 Urticaria, Angioedema and Mast Cell Disorders` (K4) | 2412 | **flag — Derm** | content |
| `I-20` | Infectious | `## Diarrhoea — differential diagnosis` + `## Gastroenteritis — causes by incubation time` | 1331, 1353 | **flag — GI owns it** | inbound-corrob. |
| `K-21` | MSK | `## Ocular trauma` (11_09b) | 1304 | **Ophthalmology** | content |
| `K-23` | MSK | `## Autonomic dysreflexia` (11_06) | 694 | **arguable — Neuro** | content |
| `K-27` | MSK | `## 0.6 Immobility, Mobility Aids and Functional Assessment` (L6) | 3435 | **arguable — Geriatrics** | content |
| `N-9` | Neuro | `## Syncope` + `### Cardiac syncope` + `### Non-cardiac syncope` | 879–919 | **Cardio** | content |
| `N-11` | Neuro | `## 0.3 Diplopia and Disorders of Eye Movement` (D7) | 3646 | **Ophthalmology** | **inbound-PRIMARY** |
| `N-12` | Neuro | `### Horner's Syndrome` | 1001 | **Ophthalmology** | content |
| `N-13` | Neuro | `## 0.4 Speech, Voice and Swallowing` (D7) | 3704 | **ENT** | content |
| `N-14` | Neuro | `## 0.5 Smell and Taste` (D7) | 3752 | **arguable — ENT** | content |
| `N-15` | Neuro | `### Vertigo (Peripheral vs Central, BPPV, Vestibular Neuritis)` | 1016 | **decide with ENT** | inbound-corrob. |
| `N-19` | Neuro | `## Delirium vs Dementia vs Depression — the "3 Ds" in Older People` | 320 | **Geriatrics** | content |
| `N-20` | Neuro | `### Cauda Equina Syndrome` · `### Malignant Spinal Cord Compression` | 1559, 1582 | **arguable — MSK/spinal** | content |
| `N-21` | Neuro | `### Neurofibromatosis` · `### Tuberous Sclerosis` | 1691, 1709 | **arguable — Derm/genetics** | content |
| `B-12` | OBGYN | `## Male subfertility` | 2492 | **misplaced within OBGYN** | content |
| `B-17` | OBGYN | `## Urinary incontinence` (17_08) + `## 0.6 Prolapse and Urinary Incontinence` (O5) | 2967, 5123 | **flag — Renal owns it** | content |
| `B-19` | OBGYN | `16_06-07 Ante-Perinatal Infections` (15 sections) | 654–876 | **flag — decide with ID** | inbound-corrob. |
| `E-5` | Opthalm | `## Tropical Eye Diseases` — `### Xerophthalmia` · `### Trachoma` · `### Onchocerciasis` | 828–872 | **arguable — Infectious Disease** | content |
| `Y-2` | Psychiatry | `## 0.5 Postpartum (Puerperal) Psychosis` | **362** | **OBGYN** | content |
| `RU-15` | Renal | `## 0.5 Groin Lumps and Hernias` (H4) | 1545 | **arguable — GI** | content |
| `RU-16` | Renal | `### 0.14.1 TURP Syndrome` | 500 | **arguable — Anaes** | content |
| `R-13` | Resp | `## 0.9 Tuberculosis` + `.2`–`.6` | 423–485 | **arguable — Infectious Disease** | content |
| `R-14` | Resp | `## 0.21 Upper Respiratory Tract Infection (URTI)` | 791 | **arguable — ENT or GP** | content |


---

## NO DESTINATION PROPOSED — in-text flag only

**39 rows** · 1 rest primarily on inbound-reference distribution · 2 cite it as corroboration · 36 rest on content reasoning alone.

**39 rows with no destination.** These are the rows where the analysis found a real problem
and could not name where the content should go — recorded so the gap is visible rather than
absorbed.

They fall into three kinds:
- **`flag — X owns it`** (about 20 rows) — the content duplicates a section in a named file
  but the correct disposition is a pointer, not a move. `I-16` acute epiglottitis, `I-17`
  Centor criteria, `I-18` allergic rhinitis, `D-8` systemic vasculitides, `R-6` osteoporosis,
  `B-17` urinary incontinence.
- **`arguable — …`** (about 12 rows) — two or three defensible homes and no discriminator.
  `E-5` tropical eye disease (Ophthalm ↔ ID), `K-23` autonomic dysreflexia (MSK ↔ Neuro),
  `N-21` neurofibromatosis and tuberous sclerosis (Neuro ↔ Derm ↔ genetics).
- **`keep, flag`** (about 7 rows) — content that is correctly placed but misleading as
  written, including GI's `M-10`, `M-17` and `M-18`, all three of which you named and all
  three of which are **already applied in the corpus** under A3.

> [!note] **`ENT T-5` is here and it is the model, not a problem.**
> `## Bell's palsy` in `13_06c` is a deliberate stub that defers to `[[04_Neurology]]` and
> explains why it defers. **Zero inbound — and that is correct**, because it exists to
> preserve one cross-reference. It is the only row in 248 where zero inbound is cited as
> evidence *for* leaving something alone. **Do not delete it.** Reach for this shape wherever
> the overlap is obvious.

| ID | From | Section | L | Proposed destination | Evidence |
|---|---|---|---|---|---|
| `A-7` | Anaes | `## 0.7 Assessment and Basic Management of Pain` +`.1 assessment` +`.2 management` | 248–300 | **flag** | content |
| `D-3` | Derm | `## Necrotising fasciitis` | 135 | **flag** | content |
| `D-4` | Derm | `## Cellulitis & erysipelas` | 575 | **flag** | content |
| `D-6` | Derm | `## Head lice` · `## Scabies` | 579, 599 | **flag** | content |
| `D-10` | Derm | `## Pyoderma gangrenosum` | 248 | **keep, flag** | content |
| `D-11` | Derm | `## 0.6 Wounds, Pressure Injury and Leg Ulcers` (G2) | 1385 | **flag** | content |
| `T-3` | ENT | `## 0.1 Lumps in the neck — approach` (13_07a) · `## 0.1 Approach to a Neck Lump` (F4) | 705, 1454 | **flag — same topic twice** | inbound-corrob. |
| `T-5` | ENT | `## Bell's palsy` (13_06c) | 697 | **keep as the stub it is** | inbound-corrob. |
| `T-6` | ENT | `## 0.5 Head and Neck Cancer` (F4) · `## HNSCC` +`### HPV-related` (13_06a) | 1563, 598, 618 | **flag** | content |
| `T-7` | ENT | `## Dentistry for doctors` +`### Assessing tooth pain` · `## Trismus` · `## Facial swellings due to dental infection` · `## Systemic disease complicating dental infection` · `## Periodontal disease` +`### Vincent's angina` (13_07c) | 796–851 | **flag — arguable own home** | **inbound-PRIMARY** |
| `T-9` | ENT | `## CSF rhinorrhoea` (13_04) | 361 | **flag** | content |
| `T-10` | ENT | `## Cancer of the paranasal sinuses` (324) · `## Nasopharyngeal cancer` (400) |  | **keep, flag** | content |
| `X-5` | Emergency | `## 0.9 Adult Analgesia` · `## 0.10 Paediatric Analgesia` (F0-4) | 3298, 3330 | **flag** | content |
| `E-13` | Endocrine | `### 0.15.8 Austroads Driving Standards for Diabetes` | 546 | **flag, do not move yet** | content |
| `P-8` | GP | `## 0.12 Health Screening (Australian Population Screening Programs)` · `## 0.13 Low-Dose CT Screening (National Lung Cancer Screening Program)` | 466, 498 | **with P-7** | content |
| `P-9` | GP | `## 0.2 Lifestyle Risk Factors (SNAP) and Smoking Cessation` +`.1 the 5As` +`.2 smoking` +`.3 nutrition, alcohol, activity` | 80–119 | **with P-7** | content |
| `R-7` | Geriatrics | `## 0.1 Continence` (GER2) | 613 | **flag** | content |
| `R-8` | Geriatrics | `## 0.2 Pressure Injury` (GER2) | 658 | **flag** | content |
| `R-9` | Geriatrics | `## 0.4 Immobility, Deconditioning and Hospital-Associated Decline` (GER2) | 760 | **flag** | content |
| `R-11` | Geriatrics | `## 0.3 Malnutrition and Nutrition` (GER2) | 707 | **flag** | content |
| `H-16` | Heme | `## Anaemia of chronic kidney disease` | 508 | **flag only** | content |
| `H-20` | Heme | `## Thymoma` | 1169 | **flag only** | content |
| `I-9` | Infectious | organism entries `## 0.4 Bacteroides` · `0.5 Fusobacterium` · `0.6 Enterococcus` · `0.7 CPE` · `0.8 Candida` · `0.10 Cryptosporidium` · `0.11 Giardia` · `0.22 Campylobacter` · `0.23 C. perfringens` | 3159–3576 | **flag — axis question** | content |
| `I-14` | Infectious | `## Spinal epidural abscess` | 1268 | **flag** | content |
| `I-15` | Infectious | `## Post-splenectomy sepsis` | 1184 | **flag** | content |
| `K-20` | MSK | `## 0.3 Rhabdomyolysis` (11_01) | 58 | **flag** | content |
| `K-22` | MSK | `## Lower genitourinary tract trauma` · `## Splenic trauma` · `## Liver trauma` · `## Head injuries` (11_09b) | 1277–1303 | **flag** | content |
| `K-25` | MSK | `### Lupus nephritis` (12_03) | 1751 | **flag** | content |
| `K-28` | MSK | `## Rickets` (11_10) | 1422 | **flag** | content |
| `N-10` | Neuro | `### Seizures vs Syncope` (comparison table) | 823 | **keep, flag** | content |
| `N-22` | Neuro | `### Subacute Combined Degeneration of the Spinal Cord` | 1614 | **flag only** | content |
| `N-23` | Neuro | `### Austroads Driving Standards (Neurological Conditions)` | 1764 | **flag, do not move** | content |
| `B-18` | OBGYN | `## 0.6 Gender Diversity and Puberty` (O6) | 5435 | **flag** | content |
| `B-20` | OBGYN | `## Sepsis in the puerperium` (16_14-15) | 1499 | **flag** | content |
| `E-4` | Opthalm | `## Ocular Manifestations of Systemic Disease — Consolidated Reference` | 873 | **keep, flag** | content |
| `E-6` | Opthalm | `## Thyroid Eye Disease` | 804 | **flag** | content |
| `E-7` | Opthalm | `## Diabetic Retinopathy` (615) · `## Hypertensive Retinopathy` (644) |  | **keep, flag** | content |
| `Y-3` | Psychiatry | `## Perinatal depression` | 158 | **flag — with Y-2** | content |
| `RU-17` | Renal | `### 0.2.3 CKD-Related Anaemia` | 107 | **keep, flag** | content |

## RECONCILIATION

```
move rows extracted from the 19 system-file flag files   248
assigned to a destination block                          248
unassigned                                                 0
```

Extracted mechanically from every `## PROPOSED MOVES*` table in `_meta/flags/*.md`
(`scratchpad/mkdest.py`); block 09 (`Palliative-and-End-of-Life-Care.md`) has **no move rows**
and is therefore absent — its content case comes from the Clinical Process file-combination
output (`_Clinical_Process_set.md`), not from a system-file move. `Heme H-21` is the row that
would populate it and is currently filed under the system-to-system block as
*"flag — decide with Heme H-21"*.

## WHAT IS NOT IN THIS FILE

- **The 11 rows you approved in message 2 and which remain unexecuted** are listed here as
  ordinary proposals. Three (`M-1`, `M-2`, `M-6`) you have since withdrawn; they are still in
  their blocks, marked in the source flag files, because withdrawing an approval does not
  delete the finding.
- **Groupings.** They are in the per-file flag files and need no ruling.
- **In-text flags.** All 80 are applied in the corpus; they are recorded in the per-file flag
  files, not here.

## LIMITATIONS

1. **A destination block is not a merge plan.** Several blocks contain rows that would land
   beside an existing copy — the nine in Investigation-Interpretation, `M-8`'s paracetamol
   pair, `M-9`'s cholangitis pair. Your ruling stands: **move and mark the pair, never merge.**
2. **The Evidence column is my classification of my own reasoning**, made by reading each
   row's justification. It is not derived from the corpus and cannot be re-derived
   mechanically. A second reader might class three or four rows differently at the
   `corroborating` / `primary` boundary.
3. **Row counts are of flag rows, not of sections.** A single row can name a dozen sections
   (`OBGYN B-19` is 15; `Heme H-9` is 20 entries). **Do not read 248 as a section count.**
4. Clean against everything currently known to check for — not complete.
