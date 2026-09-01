# GP_merged.md — grouping and misplacement flags

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
Sources: 2 · lines 621 (**smallest system file**) · numbering drift: **none** ·
no self-declared misfiles · **no history/examination blocks at all** (the only system file with none).
`19_General_Practice_and_Preventive_Medicine` 16 inbound (Clinical-Process-EBM…).

## THE SHAPE: a two-source file whose halves belong in different places
`19_` is **preventive medicine and health-system content**; `NEW_Investigations_General_and_Preventive`
is **16 general laboratory tests**. Neither is disease content, and the file has no clinical sections.

## PROPOSED MOVES

### Investigation interpretation (standing rule, as extended)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| P-1 | `## 0.1 Inflammatory Markers (CRP, ESR, Procalcitonin)` | 186 | **Investigation-Interpretation.md §1.21** | **§1.21 "Inflammatory Markers (CRP and ESR)" already exists.** Direct duplicate **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| P-2 | `## 0.2 Albumin` · `## 0.3 ALP` · `## 0.4 LDH` · `## 0.5 Uric Acid` · `## 0.6 Ammonia` | 209–337 | **Investigation-Interpretation.md** | general biochemistry. **`## 0.3 ALP` serves `GI §0.1/§0.2` cholestasis and `MSK 11_08b Paget's`; `## 0.6 Ammonia` serves `GI §0.6.3 Hepatic encephalopathy` — where the corpus already says a normal level does not exclude it** |
| P-3 | `## 0.7 Serum Ceruloplasmin` | 338 | **Investigation-Interpretation.md** | serves `GI §0.7 Wilson's Disease`. **Pairs with `Renal NEW_Inv §0.11 24-hour Urine Copper` (RU-10)** — the two halves of one work-up are in two different system files **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| P-4 | `## 0.8 Calcitonin` | 364 | **Investigation-Interpretation.md** | serves medullary thyroid carcinoma. **`GP:375` carries the PPI-confounder warning** — *"Ask about the PPI before referring"* — keep it with the entry **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| P-5 | `## 0.9 Gallium Scan` · `## 0.10 Incisional Biopsy` · `## 0.11 Stains (histochemical and immunohistochemistry)` | 387–465 | **Investigation-Interpretation.md** | `## 0.11` overlaps `Heme NEW_Inv_Haem_P2 §0.17 Flow Cytometry` and `§0.18 Biopsy and Procedures` **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| P-6 | `## 0.14 Genetic Risk Assessment` · `## 0.15 Genetics and Molecular Testing` · `## 0.16 Pharmacogenomic Assessment` | 519–597 | **Investigation-Interpretation.md** | ⚠️ **`## 0.14` overlaps `Heme 10_11b Genetic Cancer Predisposition Syndromes` — which has 3 inbound, ALL from GP** (Heme G-B20). The two halves point at each other **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |

### Preventive health — the fourth file on one topic
| ID | Section | L | → | Note |
|---|---|---|---|---|
| P-7 | `## 0.1 Preventive Medicine and Screening in Australian GP` +`.1 the three national cancer screening programs` +`.2 CV, diabetes and kidney risk` +`.3 immunisation across the lifespan` +`.4 other preventive domains` | 16–79 | **decide as one with GER3 / PH1** | ⚠️ **Preventive health and screening is now in FOUR places**: here · `GER3 §0.1`–`§0.5` — **now `Preventive-Health.md`, moved out of Geriatrics by A1/A2 (`16a9386`)** (R-2, **31 inbound**) · `PH1_Population_Health_and_Research_Literacy` (standalone) · `ID 08_01-03 ## Vaccination Schedule` (I-10). Plus `Pediatrics 15_24b` and `NEW_Drugs_20`. **Six sources, one topic** |
| P-8 | `## 0.12 Health Screening (Australian Population Screening Programs)` · `## 0.13 Low-Dose CT Screening (National Lung Cancer Screening Program)` | 466, 498 | **with P-7** | **`## 0.12` duplicates `§0.1.1` in this same file** — the two sources overlap each other |
| P-9 | `## 0.2 Lifestyle Risk Factors (SNAP) and Smoking Cessation` +`.1 the 5As` +`.2 smoking` +`.3 nutrition, alcohol, activity` | 80–119 | **with P-7** | duplicates `GER3 §0.5 Lifestyle Risk and Behaviour Change`. **`§0.2.1 The 5As` is a consultation framework → `Communication.md`** |
| P-10 | `## 0.3 Hospital Avoidance and Potentially Preventable Hospitalisations` +`.1 what an intern can actually do` | 120–145 | **arguable — `PH1`** | health-system content, not clinical |
| P-11 | `## 0.4 Continuity of Care, and What Makes General Practice Different` +`.1` | 146–176 | **arguable — `PH1` or keep** | a disciplinary essay. **The only section in this file with a genuine claim to be "general practice"** |

## KEEP + IN-TEXT FLAG
- **This file may not survive as a system file.** Every section has a stronger home elsewhere except
  P-11. That is a structural observation, not a recommendation — **the user should decide whether
  "General Practice" is a system or a setting.**
- `GP:49` and `GP:11` were two of the off-by-one pointers fixed in `48a870f` — both pointed into
  `01_Cardiovascular` for absolute cardiovascular risk and colorectal screening.
- `GP:278` carries **Light's criteria**, a third copy alongside `Investigation-Interpretation:102`
  and `Resp §0.12` — see Resp's flags.

## GROUPINGS
**HIGH**
- **G-P1 Cancer screening** — `§0.1.1 the three national programs` (29) · `## 0.12 Health Screening`
  (466) · `## 0.13 Low-Dose CT Screening` (498). **Cross-file: `GER3 §0.3 Cancer Screening in
  Practice`, `OBGYN 17_09 ## Cervical cancer screening`, `GI §0.26 Colorectal Cancer`,
  `Heme 10_12 Breast`**
- **G-P2 Cardiovascular and metabolic risk** — `§0.1.2` (47). **Cross-file: `GER3 §0.2`,
  `Cardio §0.40 Dyslipidaemia`, `Endocrine 06 §0.22`, `I5 §0.3`**
- **G-P3 Immunisation** — `§0.1.3 immunisation across the lifespan` (54). **Cross-file:
  `GER3 §0.4`, `ID 08_01-03 ## Vaccination Schedule`, `NEW_Drugs_20`, `Pediatrics 15_24b`**
- **G-P4 Lifestyle and behaviour change** — `## 0.2` +`.1 the 5As` +`.2 smoking` +`.3` (80–119).
  **Cross-file: `GER3 §0.5`, `Psychiatry NEW_Drugs_17 §0.7 Nicotine Dependence`**
- **G-P5 General biochemistry** — `NEW_Inv_General §0.1`–`§0.8` (186–386)
- **G-P6 Tissue diagnosis** — `§0.9 Gallium Scan` · `§0.10 Incisional Biopsy` · `§0.11 Stains`
  (387–465)
- **G-P7 Genetics** — `§0.14`–`§0.16` (519–597). **Cross-file: `Heme 10_11b`,
  `Pediatrics 15_18b Inheritance Summary`, `15_20`–`15_21` syndromes**

**UNGROUPED — stays put**: `## 0.4 Continuity of Care` (146) · `## Build status` (598)

## LIMITATIONS
- **P-7 is the largest single grouping question in the vault by source count** — six sources across
  four files. It cannot be settled from GP alone and belongs with the Clinical Process output.
