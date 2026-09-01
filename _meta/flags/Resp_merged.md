# Resp_merged.md — grouping and misplacement flags

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
Sources: 5 · lines 1578 · `02_Respiratory` 63 inbound — **Investigation-Interpretation ×22**, the
heaviest test-file dependency of any system file so far (History-Taking ×9, Examination ×7).
Numbering drift: **none** (`drift.py` clean).

## THE HEADLINE: `RESP-X` is a second copy of five topics `02_Respiratory` already owns
`RESP-X_Occupational_and_Chronic_Lung_Disease` has **zero inbound references in any form**, and
**five of its six sections duplicate `02_Respiratory`:**
| RESP-X | L | duplicates `02_Respiratory` | L |
|---|---|---|---|
| `## 0.1 Interstitial Lung Disease` | 1310 | `## 0.7 IPF` + `### 0.7.1 Pulmonary fibrosis — zonal distribution` | 276, 297 |
| `## 0.2 Occupational Lung Disease` | 1372 | `## 0.20 Pneumoconioses (Occupational Lung Disease — brief overview)` | 767 |
| `## 0.3 Asbestos-Related Disease` | 1414 | `## 0.5 Mesothelioma` + `### 0.5.1 Pleural plaques` + `### 0.5.2 Asbestosis` | 210, 230, 233 |
| `## 0.4 Bronchiectasis` | 1453 | `## 0.6 Bronchiectasis` | 241 |
| `## 0.5 Sleep-Disordered Breathing` | 1497 | `## 0.18 Sleep Apnoea (OSA)` | 704 |
| `## 0.6 Chronic Respiratory Failure and Long-Term Management` | 1537 | `## 0.3 Respiratory Failure` (partial — A is acute-focused) | 147 |
**Not a move — a merge decision.** `02_Respiratory §0.20` even calls itself a *"brief overview"*
while RESP-X §0.2 is the full treatment. RESP-X is richer on occupational history and Australian
asbestos exposure; `02_Respiratory` is richer on mesothelioma staging.

## PROPOSED MOVES

### Investigation interpretation (standing rule, as extended by the user)
| ID | Section | L | → | Why |
|---|---|---|---|---|
| R-1 | `## 0.2 Pulmonary Function Tests (Spirometry, Lung Volumes, DLCO)` | 1013 | **Investigation-Interpretation.md §1.3** | §1.3 *"Spirometry and Peak Flow"* already exists there. This entry is **richer** — adds lung volumes, TLC/RV, DLCO. *How to read the test.* **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| R-2 | `## 0.3 Pulse Oximetry (SpO₂)` | 1041 | **Investigation-Interpretation.md** | functional vs fractional saturation, the failure modes. No equivalent exists there. 2 inbound (MSK, internal) **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| R-3 | `## 0.4 Sleep Studies (Polysomnography, HSAT)` | 1064 | **Investigation-Interpretation.md** | level 1 vs home testing, channels. 1 inbound (Anaes) |
| R-4 | `## 0.5 Sputum Culture` | 1087 | **Investigation-Interpretation.md** | sits beside §1.18 Blood Cultures and Microbiology Basics |
| R-5 | `## 0.6 Sweat Chloride Test` | 1109 | **Investigation-Interpretation.md** | how the test works **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| R-6 | `## 0.7 TB Screening (TST/Mantoux and IGRA)` | 1134 | **Investigation-Interpretation.md** | *how to read the induration*. **The disease content stays** — see R-13. 2 inbound (Heme, ID) |
| R-7 | `## 0.8 V/Q Scan` | 1159 | **Investigation-Interpretation.md** | mismatched-defect reading |
| R-8 | `## 0.1 Nasopharyngeal Swab` | 992 | **Investigation-Interpretation.md** *or* `NEW_Exam_Manoeuvres_and_Procedures` | it is a **procedure description** (*"floor of the nose, parallel to the palate, not angled upwards"*) — axis question, flag |
| R-9 | `### 0.9.1 Diagnosis of latent TB — Mantoux test` | 440 | **Investigation-Interpretation.md**, with R-6 | *"0.1 mL of 1:1,000 PPD injected intradermally; read 2–3 days later"* is technique, not disease **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |

> **R-1 – R-9 empty `NEW_Investigations_Respiratory` almost entirely.** That is the expected shape:
> it is an investigations file that was filed under a system.

### History-taking (standing rule)
| ID | Section | L | → | Why |
|---|---|---|---|---|
| R-10 | `> [!danger] Ask the occupational history — it is systematically not taken` | 1374 | **History-Taking.md** | a history schema, not a disease fact |
| R-11 | `> [!warning] Hypersensitivity pneumonitis — take the exposure history properly` | 1334 | **History-Taking.md** | ditto; leave the disease content in Resp |
| R-12 | **2** × `**Focused Hx:**` + **3** × `**Examination:**` *(count corrected 2026-09-01 — measured, not re-estimated)* in `NEW_Respiratory` | 1221–1264 | **History-Taking.md / Examination.md** | acute dyspnoea, acute cough, acute stridor. `L1264` opens *"this is where the greatest harm is done, so the first rule is what not to do"* — examination technique |

### Cross-file topic ownership
| ID | Section | L | → | Note |
|---|---|---|---|---|
| R-13 | `## 0.9 Tuberculosis` + `.2`–`.6` | 423–485 | **arguable — Infectious Disease** | `Infectious Disease_merged §0.3 Tuberculosis — Latent Infection, Contacts and Active Disease` (ID:2031) is a **fuller entry**. TB currently has three homes: Resp, ID, and the screening entry at Resp:1134. **Decide with the ID pass** |
| R-14 | `## 0.21 Upper Respiratory Tract Infection (URTI)` | 791 | **arguable — ENT or GP** | ENT owns sore throat, rhinosinusitis; `NEW_ENT_and_Oral ## Acute Sore Throat` exists. Borderline |

## KEEP + IN-TEXT FLAG
- **`## 0.22 Cross-references to avoid duplication`** (L812) is an **administrative section inside
  clinical content**. It also carried one of the broken pointers (fixed, `48a870f`). Flag: this is
  metadata, not notes — candidate for `_meta/`.
- **Its own text flags two topics as homeless**: *"Diphtheria — … flagged for whichever of those
  files comes up next in the rotation"* and the paediatric respiratory rows (bronchiolitis, croup,
  pertussis, viral-induced wheeze). **Check both land somewhere in the Paediatrics and ID passes.**
- `Light's criteria` appears in **three** files — `Investigation-Interpretation:102`,
  `GP_merged:278`, and the Resp pleural effusion entry (562). Inv-Interp already draws the boundary
  correctly (*"see [[02_Respiratory]] Pleural Effusions"*); **GP's copy is the odd one.**
- `## 0.13 Oxygen Therapy` +`.1 Delivery devices` +`.2 NIV` (571–594) — **not** investigation
  interpretation (nothing is being read), so the standing rule does not reach it. Flag as a
  candidate for a procedures home; leave for now.

## GROUPINGS
**HIGH**
- **G-R1 Asthma / COPD** — `02_Resp §0.1` +`.1 acute exacerbation` (6, 41) · `§0.2 COPD` +`.1
  phenotypes` +`.3 exacerbation` (64, 94, 133) · `NEW_Drugs_18 §0.1` +`.1`–`.5` (830–878).
  The `> [!danger] SABA-ONLY TREATMENT IS NO LONGER ADEQUATE` block (832) is management, in the drug file.
- **G-R2 Pneumonia** — `§0.8` +`.1 CAP` +`.2 HAP` +`.3 atypical` +`.4 immunocompromised`
  +`.5 viral/COVID` (307–422) · `§0.17 Aspiration Pneumonia and Pneumonitis` (681) ·
  `§0.16 Acute Bronchitis` (660, adjacent) · `NEW_Inv_Resp §0.5 Sputum Culture` (1087)
- **G-R3 Interstitial / fibrotic lung disease** — `§0.7 IPF` +`.1 zonal distribution` (276, 297) ·
  `RESP-X §0.1 ILD` (1310) · `NEW_Drugs_18 §0.6` antifibrotics (945)
- **G-R4 Occupational and asbestos disease** — `§0.5 Mesothelioma` +`.1`+`.2` (210–240) ·
  `§0.20 Pneumoconioses` (767) · `RESP-X §0.2` (1372) · `RESP-X §0.3` (1414)
- **G-R5 Bronchiectasis** — `§0.6` (241) · `RESP-X §0.4` (1453)
- **G-R6 Sleep-disordered breathing** — `§0.18 OSA` (704) · `RESP-X §0.5` (1497) ·
  `NEW_Inv_Resp §0.4 Sleep Studies` (1064). **Three copies.**
- **G-R7 Respiratory failure and oxygen** — `§0.3` (147) · `§0.13` +`.1`+`.2` (571–594) ·
  `RESP-X §0.6` (1537) · `NEW_Inv_Resp §0.3 Pulse Oximetry` (1041)
- **G-R8 Tuberculosis** — `§0.9` +`.1`–`.6` (423–485) · `NEW_Inv_Resp §0.7` (1134) ·
  (+ `Infectious Disease §0.3`, outside this file)
- **G-R9 Cystic fibrosis** — `§0.14` (595) · `NEW_Drugs_18 §0.4 CFTR modulators` (928) ·
  `NEW_Inv_Resp §0.6 Sweat Chloride` (1109)
- **G-R10 Lung cancer** — `§0.4` +`.1 SCLC` +`.2 NSCLC` (158–209)
- **G-R11 Pleural disease** — `§0.11 Pneumothorax` (513) · `§0.12 Pleural Effusions` (550) ·
  `§0.19 Empyema and Haemothorax` (731)
- **G-R12 Cough** — `NEW_Drugs_18 §0.2` +`.1`–`.3` (879–901) · `NEW_Resp ## Acute Cough` (1244)
- **G-R13 Dyspnoea** — `NEW_Resp ## Acute Dyspnoea` (1212). **No `02_Respiratory` partner** —
  and `Emergency and Crit Care §0.1 Acute Dyspnoea` (756) is a second copy. Cross-file.
- **G-R14 Pulmonary hypertension** — `NEW_Drugs_18 §0.3` +`.1`–`.3` (902–927). **No Resp partner**;
  the disease entry is `Cardio §0.37 Pulmonary Hypertension`. Cross-file.

**MEDIUM**
- **G-R15 Stridor** — `NEW_Resp ## Acute Stridor` (1254). Its own note says the bare topic *Stridor*
  was **skipped on a header match** and asks for the existing coverage to be checked. It is in
  **ENT** (`## 0.5 Acute Stridor`, `## Stridor — overview`) and **Emergency** (`§0.5 Acute Stridor`).
  **Three files.** Flag for the ENT and Emergency passes.
- **G-R16 Sarcoidosis** — `§0.10` (486). Ungrouped within Resp; check against Derm and Opthalm.
- **G-R17 ARDS** — `§0.15` (636). Check against Emergency/Anaes.

**UNGROUPED — stays put**: `§0.21 URTI` (791) · `NEW_Drugs_18 §0.5 Pulmonary Surfactants` (937,
neonatal — check against Paediatrics) · 4 administrative `Build status` / `Topics skipped` blocks

## LIMITATIONS
- R-13 (TB) and R-14 (URTI) are **deliberately not decided here** — both depend on inbound evidence
  from files not yet analysed. Same reason M-15 was left in GI.
- `RESP-X`'s zero inbound count is a genuine measurement, but per the trust-map caveat, **absence of
  inbound references is weak evidence** on its own; it is strong here only because it coincides with
  five demonstrated content duplicates.
