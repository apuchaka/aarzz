# Endocrine and metabolics_merged.md — grouping and misplacement flags

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


Status: **ANALYSED. NOTHING MOVED.**
Sources: 9 · lines 3667 · `06_Metabolic_Medicine_and_Endocrinology` 37 inbound.
Numbering drift: **none**. Zero inbound: `NEW_Acid-Base_Fluids_and_Electrolytes`, `NEW_Investigations_Endocrine`.

> **Indexer correction made during this file's pass.** `F0-2_Acid-Base__DKA_and_Fluid_States` was
> initially reported as **zero inbound**. It has **55+**. The prose writes `[[F0.2]]` with a dot
> where the filename uses a hyphen — the exact trap CLAUDE.md §1.10 documents. Fixed; all four
> earlier zero-inbound verdicts re-verified and unchanged.

## THE HEADLINE: this file shares a whole source with Heme Onc
`NEW_Drugs_07_Blood_and_Electrolytes.md` is **byte-identical, 240 lines**, in
`Endocrine and metabolics_merged.md:2889` **and** `Heme Onc_merged.md:2774`. **The only source file
in the vault (1 of 295) concatenated into two merged docs.** Needs a single home, not a move.

## PROPOSED MOVES

### Investigation interpretation (standing rule, as extended)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| E-1 | `## 0.1 Thyroid Panel (TSH, fT4, fT3, antibodies)` | 3468 | **Investigation-Interpretation.md** | **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |
| E-2 | `## 0.2 Thyroid Ultrasound` · `## 0.3 Radioactive Iodine Uptake and Scintigraphy` | 3497, 3516 | **Investigation-Interpretation.md** | TIRADS reporting; uptake patterns **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| E-3 | `## 0.4 Glucose / Diabetes Testing (glucose, HbA1c, OGTT)` | 3536 | **Investigation-Interpretation.md** | **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |
| E-4 | `## 0.5 Prolactin` · `## 0.6 Renin–Aldosterone (ARR)` | 3558, 3575 | **Investigation-Interpretation.md** | macroprolactin; ARR interference **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| E-5 | `### 0.20.6 Arterial Blood Gas Reference Values` | 768 | **Investigation-Interpretation.md §1.5** | **§1.5 "ABG / VBG Interpretation" already exists there** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| E-6 | `## 0.1 Acid-Base Interpretation — Framework` (F0-2) | 1077 | **Investigation-Interpretation.md §1.5** | *"a structured method for converting a blood gas plus electrolytes into a named disorder"* — that is §1.5's job description **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |

### Misplaced investigations (not self-declared — found by reading)
| ID | Section | L | → | Why |
|---|---|---|---|---|
| E-7 | `## 0.7 G6PD Assay` | 3597 | **Heme Onc** | a red-cell enzyme assay in an endocrine investigations file. `Derm_merged G6 §0.6 Cyanosis and Abnormal Skin Colour` already routes *"G6PD deficiency and methylene blue → [[J2]] 0.2"*, i.e. to haematology **✅ EXECUTED 2026-09-01 → `Heme Onc_merged.md` (block 5)** |
| E-8 | `## 0.8 Carnitine Levels` · `## 0.9 Plasma Amino Acid Screen` | 3615, 3632 | **Paediatrics** | inherited metabolic disease. `Pediatrics_merged` owns `## 15_17a Approach to Inherited Metabolic Disease` and `## 15_17b Glycogen Storage Disorders, PKU, Lysosomal Storage Diseases` **✅ EXECUTED 2026-09-01 → `Pediatrics_merged.md` (block 5)** |
| E-9 | `## 0.4 Paediatric Diabetic Ketoacidosis` (F0-2) | 1173 | **arguable — Paediatrics** | `Pediatrics_merged §15_16b Diabetes Mellitus, MODY, DKA` exists. **CLAUDE.md rule 5 territory** — this is where paediatric absolute quantities live. **Do not move without checking the fluid figures survive** |

### Cross-file
| ID | Section | L | → | Note |
|---|---|---|---|---|
| E-10 | `## 0.22 Hypercholesterolaemia` | 802 | **decide with Cardio** | lipids currently occupy **five** sections across two files: here, `I5 §0.3 Lipid Disorders` (2664), `Cardio §0.40 Dyslipidaemia`, `NEW_Drugs_06 §0.9`, `NEW_Inv_Card §0.3`. Cardio G-C13 is the other half |
| E-11 | `### 0.15.7 Perioperative Diabetes Management` | 531 | **arguable — Anaes** | verified against the **ADS-ANZCA** perioperative guideline — an anaesthetic co-authored source. Decide with the Anaes pass |
| E-12 | `## 0.23 Principles of Fluid and Electrolyte Management in Surgical Patients` | 838 | **arguable — Anaes / surgical** | self-describes as a *"general principles entry"* for surgical patients |
| E-13 | `### 0.15.8 Austroads Driving Standards for Diabetes` | 546 | **flag, do not move yet** | **Austroads standards are now in three system files** — here, `Cardio §0.35.5`, and Neuro. `Clinical-Process-EBM-Consent-Capacity:102` has a *"Fitness to drive"* row pointing at two of them. Candidate for one home; decide at the Clinical Process pass |

### History (standing rule)
| ID | Section | L | → |
|---|---|---|---|
| E-14 | `**Focused Hx:**` + `**Examination:**` in `NEW_Acid-Base_Fluids_and_Electrolytes ## Dehydration` | 2852–2853 | **History-Taking.md / Examination.md** **✅ RESOLVED 2026-09-01 — Option 1: left in place, indexed in `Examination.md` §3 and `History-Taking.md` §2 (`bcf7515`/`fab04f5`)** |

## KEEP + IN-TEXT FLAG
- `## 0.27 Weight Change — Differential Approach` (1048) self-describes as *"absent as a unifying
  differential despite the individual causes being scattered across this file … and others"*. It is
  a **presentation-level differential in a disease file** — flag alongside `I5 §0.2`.
- `NEW_Drugs_13 §0.7` (in **Renal**) self-declares that it duplicates `NEW_Drugs_10_Endocrine
  §0.5.1/§0.5.2` — **the other half of that flag lives here.** Cross-reference the two.
- `NEW_Acid-Base_Fluids_and_Electrolytes` has **one clinical section** (`## Dehydration`) and zero
  inbound. Smallest orphan found so far.

## GROUPINGS
**HIGH** — Corpus A (`06_Metabolic…`) and the I-files duplicate each other almost entirely.
- **G-E1 Thyroid function and hypothyroidism** — `06 §0.1` +`.1 subclinical` +`.2 sick euthyroid`
  +`.3 myxoedema coma` (6–69) · `I1 §0.1 TFT Interpretation` (1387) · `I1 §0.2 Hypothyroidism` (1426) ·
  `NEW_Drugs_10 §0.4.1` (3313) · `NEW_Inv_Endo §0.1` (3468)
- **G-E2 Hyperthyroidism** — `06 §0.2` +`.1 Graves` +`.2 toxic MNG` +`.3 thyroid storm` (70–131) ·
  `I1 §0.3` (1469) · `I1 §0.4 Thyroid Emergencies` (1527) · `NEW_Drugs_10 §0.4.2`,`.3` (3328, 3342)
- **G-E3 Goitre, nodule and thyroid cancer** — `06 §0.3 Thyroid Cancers` (132) · `06 §0.4 Goitre`
  (145) · `I1 §0.5 Thyroid Nodule and Goitre` (1565) · `NEW_Inv_Endo §0.2`,`§0.3` (3497, 3516).
  (+ `ENT §0.4 Thyroid Nodules` — cross-file, flag for the ENT pass)
- **G-E4 Diabetes — diagnosis and management** — `06 §0.15` +`.1 T1DM` +`.2 T2DM` +`.5 stepwise`
  +`.9 insulin types` +`.10 drugs` (417–586) · `I2 §0.1 Diagnosis` (1678) · `I2 §0.2 T2DM Mx` (1715) ·
  `I2 §0.3 T1DM Mx` (1755) · `NEW_Drugs_10 §0.2` +`.1`–`.10` (3201–3294) · `NEW_Inv_Endo §0.4` (3536)
- **G-E5 Diabetes complications** — `06 §0.15.3` (460) · `06 §0.15.4 Diabetic Foot` (472) ·
  `I2 §0.5 Microvascular` (1853) · `I2 §0.6 Macrovascular and the Diabetic Foot` (1878)
- **G-E6 Hypoglycaemia** — `06 §0.18` (651) · `I2 §0.4` (1793) · `NEW_Drugs_10 §0.3.1 Glucagon` (3297)
- **G-E7 DKA / HHS** — `06 §0.16 DKA` (587) · `06 §0.17 HHS` (620) · `F0-2 §0.2 HAGMA — DKA` (1118) ·
  `F0-2 §0.3 Adult DKA Management` (1145) · `F0-2 §0.4 Paediatric DKA` (1173). **Four copies**
- **G-E8 Acid-base** — `06 §0.20` +`.1`–`.6` (707–786) · `F0-2 §0.1` (1077) · `§0.5 Lactic acidosis`
  (1200) · `§0.6 NAGMA` (1228) · `§0.7 Metabolic alkalosis` (1255) · `§0.8 Salicylate` (1287).
  (+ `Investigation-Interpretation §1.5` — see E-5/E-6)
- **G-E9 Sodium and water** — `06 §0.25 Hyponatraemia` +`.1`–`.5` (968–1025) · `06 §0.26
  Hypernatraemia` (1026) · `06 §0.19 Diabetes Insipidus` (674) · `I5 §0.5 Sodium and Water Balance`
  (2738) · `NEW_Drugs_10 §0.5.6 Tolvaptan` (3400) · `NEW_Drugs_07 §0.3.5` (3049)
- **G-E10 Potassium** — `06 §0.24.1 Hyperkalaemia` (864) · `§0.24.2 Hypokalaemia` (890) ·
  `I5 §0.6 Potassium Disorders` (2790) · `NEW_Drugs_07 §0.3.1` (3003)
- **G-E11 Calcium, PTH and bone** — `06 §0.10` +`.1`–`.3` (286–316) · `06 §0.11` +`.1`+`.2` (317–338) ·
  `06 §0.12 Vitamin D Deficiency` (339) · `06 §0.24.3 Hypercalcaemia` (913) · `§0.24.4 Hypocalcaemia`
  (930) · `I3 §0.1`–`§0.5` (1964–2170) · `NEW_Drugs_10 §0.1` +`.1`–`.7` (3141–3200)
- **G-E12 Magnesium and phosphate** — `06 §0.24.5 Hypomagnesaemia` (951) · `I3 §0.6` (2171) ·
  `NEW_Drugs_07 §0.3.3 Phosphate Binders` (3030) · `§0.3.4 Essential Minerals` (3040)
- **G-E13 Adrenal** — `06 §0.5 Cushing's` (159) · `06 §0.6 Addison's` +`.1 crisis` (191–230) ·
  `06 §0.7 Hyperaldosteronism` (231) · `I4 §0.3 Adrenal Insufficiency` (2334) · `I4 §0.4 Cushing`
  (2386) · `I4 §0.5 Mineralocorticoid Excess and Phaeochromocytoma` (2431) · `I4 §0.7 Incidentalomas`
  (2514) · `NEW_Drugs_10 §0.5.1`,`.2` (3353, 3370) · `NEW_Inv_Endo §0.6 ARR` (3575).
  **Both I4 §0.3 and §0.4 open with the same correction — *"the commonest cause is prescribed
  glucocorticoid"* — which Corpus A does not lead with.**
- **G-E14 Pituitary** — `06 §0.8 Acromegaly` (249) · `06 §0.13 Prolactinoma` (354) ·
  `06 §0.14 Hypopituitarism` +`.1 apoplexy` (379–416) · `I4 §0.1` (2230) · `I4 §0.2 Pituitary Tumours`
  (2285) · `NEW_Drugs_10 §0.5.3 Dopamine agonists` (3378) · `§0.5.4`,`§0.5.5` (3386, 3393) ·
  `NEW_Inv_Endo §0.5 Prolactin` (3558)
- **G-E15 Obesity, weight and metabolic syndrome** — `06 §0.21 Metabolic Syndrome` (787) ·
  `06 §0.27 Weight Change` (1048) · `I5 §0.1 Obesity` (2574) · `I5 §0.2 Unintentional Weight Loss`
  (2625) · `I5 §0.4 Metabolic Syndrome and Integrated Risk` (2717)
- **G-E16 Lipids** — `06 §0.22` (802) · `I5 §0.3` (2664). See E-10 for the Cardio half
- **G-E17 Fluid states** — `F0-2 §0.9 Isotonic Dehydration` (1314) · `§0.10 Third-Spacing` (1345) ·
  `NEW_Acid-Base ## Dehydration` (2844) · `06 §0.23` (838)

**MEDIUM**
- **G-E18 Androgen excess** — `I4 §0.6 Androgen Excess, Hirsutism and Virilisation` (2469).
  **No `06` partner**; overlaps OBGYN (PCOS) — flag for the OBGYN pass
- **G-E19 MEN** — `06 §0.9` (269). Ties G-E3, G-E11, G-E13 together; keep as its own entry
- **G-E20 Blood products and anaemia drugs** — `NEW_Drugs_07 §0.1 Blood Products` (2902) ·
  `§0.2` +`.1`–`.4` (2935–3000). **This whole block reads as haematology, not endocrine** — and it
  is the duplicated file. Decide with Heme Onc
- **G-E21 Vitamins** — `NEW_Drugs_07 §0.4` +`.1`–`.3` (3060–3102) · `06 §0.12 Vitamin D` (339)

**UNGROUPED — stays put**: `06 §0.15.6 DM Sick Day Rules` (518) · `§0.20.5 Renal Tubular Acidosis`
(752) · `I2 §0.7 Diabetes in Special Situations` (1908) · `I1 §0.6 Thyroid Disease in Pregnancy`
(1613) · 5 administrative blocks

## LIMITATIONS
- E-9 (paediatric DKA), E-11 and E-12 (Anaes), E-10 (lipids/Cardio), E-13 (Austroads),
  G-E18 (androgen excess/OBGYN), G-E20 (blood products/Heme) are **deliberately undecided** —
  each needs inbound evidence from a file not yet analysed.
- `F0-2` is shared conceptually with Emergency (`F0-1`, `F0-3`, `F0-4`, `F0-5` all live there).
  **Its home is a question for the Emergency pass, not this one.**
