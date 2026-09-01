# OBGYN_merged.md — grouping and misplacement flags

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
Sources: 24 · lines 5714 (2nd largest) · numbering drift: **none**.
Zero inbound: `NEW_Gynaecology_and_Reproductive`, `NEW_Obstetrics`.
`O2_Later_Pregnancy_and_Fetal` has **42 inbound — the highest of any Corpus B source in the vault**
(Heme ×8, OBGYN ×6, MSK ×5, Neuro ×5).

## THE HEADLINE: sexual history is now in three files
| Where | Section | L |
|---|---|---|
| **OBGYN** | `## 0.1 The Sexual History and STI Assessment` (O6) — carries the **"five Ps"** and the normalising script *"I ask everyone these questions…"* | 5185 **✅ EXECUTED 2026-09-01 → `History-Taking.md` (c5df174)** |
| **Infectious Disease** | `## The STI Check — Sexual History, What to Test, and When` + `### Taking a sexual history` (ID I-1) | 870 **✅ EXECUTED 2026-09-01 → `History-Taking.md` (c5df174)** |
| **MSK** | `## 0.18 STI Screening (asymptomatic sexual health check)` (MSK K-10) | 4497 |

**Three sources, three files, one OSCE station.** `O6` has **23 inbound and only 2 internal** —
GI ×6, ID ×5, Neuro ×4, Paediatrics — i.e. it is already the de facto owner.
**→ `History-Taking.md`**, with the disease content staying in ID and OBGYN.

## PROPOSED MOVES

### History-taking / examination (standing rule)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| B-1 | `## 0.1 The Sexual History and STI Assessment` (O6) | 5185 | **History-Taking.md** | see above. Merge with ID I-1 and MSK K-10 **✅ EXECUTED 2026-09-01 → `History-Taking.md` (c5df174)** |
| B-2 | `## 0.1 Triple Assessment` (O7) | 5499 | **Examination.md §1.17** | **§1.17 "Breast Examination" already exists.** Triple assessment is the examination-plus-imaging-plus-biopsy method **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| B-3 | `## 0.1 Pre-pregnancy counselling` (16_01-05) | 12 | **arguable — Communication.md** | a counselling consultation. Counter: it is heavily clinical (folate, rubella, medication review). **Flag, do not move** |
| B-4 | **6** × `**Focused Hx:**` + **6** × `**Examination:**` *(count corrected 2026-09-01 — measured, not re-estimated)* in `NEW_Obstetrics` and `NEW_Gynaecology_and_Reproductive` | 4000–3628 | **History-Taking.md / Examination.md** | both sources have zero inbound **✅ RESOLVED 2026-09-01 — Option 1: left in place, indexed in `Examination.md` §3 and `History-Taking.md` §2 (`bcf7515`/`fab04f5`)** |

### Investigation interpretation (standing rule, as extended)
`NEW_Investigations_Obstetrics_and_Gynaecology` — 12 entries, 4 inbound (GP ×2, MSK, NEW_Exam).
| ID | Section | L | → | Note |
|---|---|---|---|---|
| B-5 | `## 0.1 Cervical Screening Test and Abnormality (Australian NCSP)` · `## 0.2 Liquid-Based Cytology` | 3666, 3696 | **Investigation-Interpretation.md** | **duplicates `17_09 ## Cervical cancer screening`** (3034). `GP_merged` and `Clinical-Process-EBM` both cite `17_09` **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |
| B-6 | `## 0.3 Genital / Cervical Swab Panel` | 3718 | **Investigation-Interpretation.md** | overlaps `17_08 ## Vaginal discharge — DDx` and `ID 08_08` **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| B-7 | `## 0.4 Hormone Panel (Gynaecological / Reproductive)` | 3744 | **Investigation-Interpretation.md** | serves amenorrhoea, PCOS, menopause **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| B-8 | `## 0.5 Prenatal Screening Panel` · `## 0.6 CVS` · `## 0.7 Amniocentesis` · `## 0.8 Cordocentesis` | 3769–3858 | **Investigation-Interpretation.md** | ⚠️ **§0.6 and §0.7 duplicate `16_01-05 §0.6.1 Chorionic villus sampling` and `§0.6.2 Amniocentesis`** (203, 209), and `§0.5` duplicates `§0.5.4`–`§0.5.6` (NIPT, combined and quadruple tests) **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| B-9 | `## 0.9 Kleihauer-Betke` · `## 0.10 Ferning and Nitrazine` · `## 0.11 Fetal Fibronectin` · `## 0.12 Biophysical Profile` | 3859–3964 | **Investigation-Interpretation.md** | ⚠️ **the BPP and CTG cluster is where approved Cardio C-1 (`Non-Stress Test / CTG`) should land**, alongside `GER7 §0.5 Fetal Scalp Blood Sampling`. **Three CTG/fetal-monitoring homes** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |

### Topic in the wrong system
| ID | Section | L | → | Why |
|---|---|---|---|---|
| B-10 | `## Puerperal psychosis` (16_10-13) | 1481 | **Psychiatry** | `O3 §0.6 Perinatal Mental Health` (4634) is the Corpus B partner and would move with it. `Psychiatry_merged` owns mood and psychotic disorders |
| B-11 | `### 0.12.8 Psychiatric conditions — drugs in pregnancy` | 536 | **Psychiatry / drug files** | `NEW_Drugs_17_Psychotropic` is in Psychiatry |
| B-12 | `## Male subfertility` | 2492 | **misplaced within OBGYN** | it sits inside `17_05_PID__Endometriosis__Fibroids` — a source about none of those. Belongs with `17_06 Subfertility` (2623) at minimum, or **Renal/Urology**, which owns ED and vasectomy |
| B-13 | `## Female genital mutilation (FGM)` | 1956 | **arguable — `NEW_Safeguarding_and_Forensic`** | mandatory reporting and legal dimensions. Counter: the clinical management is gynaecological. **Flag** |
| B-14 | `## Ophthalmia neonatorum` | 825 | **Ophthalmology / Paediatrics** | neonatal conjunctivitis |
| B-15 | `## Birth injuries` | 1054 | **Paediatrics** | `Pediatrics 15_22b Neonatal Respiratory Distress and Jaundice`, `M3 Neonatal Problems` **✅ EXECUTED 2026-09-01 → `Pediatrics_merged.md` (block 5)** |
| B-16 | `## 0.5 Routine Postnatal and Newborn Care` (O3) | 4605 | **flag — Paediatrics** | `Examination.md §1.24 Newborn Examination` already exists |
| B-17 | `## Urinary incontinence` (17_08) + `## 0.6 Prolapse and Urinary Incontinence` (O5) | 2967, 5123 | **flag — Renal owns it** | `Renal 07 §0.13 Incontinence`, `H2 §0.6 Incontinence`. **Four homes.** Prolapse legitimately stays in OBGYN |
| B-18 | `## 0.6 Gender Diversity and Puberty` (O6) | 5435 | **flag** | with `NEW_Drugs_16 §0.13.3 Gender-Affirming Hormone Care` (3523) and `16_16-17 ### Transgender and non-binary people` (1937). **Three places** |
| B-19 | `16_06-07 Ante-Perinatal Infections` (15 sections) | 654–876 | **flag — decide with ID** | **8 inbound, 6 from Infectious Disease.** Every section duplicates an ID or Derm entry (CMV, toxoplasmosis, syphilis, parvovirus, listeria, HBV, HSV, VZV, chlamydia, gonorrhoea, TB, GBS). **The pregnancy-specific management is the part that belongs here** |
| B-20 | `## Sepsis in the puerperium` (16_14-15) | 1499 | **flag** | **destination of approved Heme H-10** (`## Postpartum Infection and Thromboembolism`, Heme L782). Confirm they merge rather than duplicate |

## KEEP + IN-TEXT FLAG
- **`### 0.12.1`–`### 0.12.13 Pre-existing problems in pregnancy`** (416–652) is **13 subsections,
  each a one-paragraph version of a disease owned by another file** — anaemia, diabetes,
  hypertension, hyperthyroidism, jaundice, malaria, renal disease, psychiatric drugs, epilepsy,
  connective tissue disease, HIV, rubella, measles. `O2 §0.6 Medical Problems and Infection in
  Pregnancy` (4418) is the Corpus B version of the same list. **Do not disperse these** — the
  pregnancy-specific modification is the content. **Flag as a set for cross-checking**, since each
  system file also has a "in pregnancy" note (`Endocrine I1 §0.6`, `I2 §0.7`, `Cardio B5 §0.3`,
  `Neuro D6 §0.3` valproate, `Resp` asthma).
- **Breast is in four files**: `NEW_Breast` (3255) and `O7_Breast_Disease` (5498) here ·
  `Heme 10_12 Oncology — Breast` (H-19) · `MSK NEW_Inv_Ortho §0.13 Breast MRI` (K-6).
  Plus `Examination.md §1.17` and `ID 08_09 ## Mastitis and Breast Abscess` (I-12).
  **`NEW_Breast` and `O7` are both in this file and cover the same three topics** (lump, pain,
  nipple discharge/galactorrhoea).
- ⚠️ **`OBGYN_merged.md:4264` cites `[[B2]] 0.5`, which does not exist** (`B2_Hypertension_Spectrum`
  has §0.1–§0.4). **Deliberately not fixed** — the intended target cannot be determined. This is the
  one dangling pointer left in the vault after commit `48a870f`.

## GROUPINGS
**HIGH**
- **G-B1 Early pregnancy bleeding and pain** — `17_03 ## TOP` +3 (2273–2336) · `## Miscarriage`
  +`### Mx` (2337, 2366) · `## Recurrent miscarriage` (2382) · `17_04 ## Ectopic` +`### PUL`
  (2403, 2444) · `## GTD` (2451) · `O1 §0.1 Assessing Bleeding and Pain` (4058) · `§0.2 Ectopic`
  (4086) · `§0.3 Miscarriage` (4118) · `§0.4 Molar Pregnancy and Hyperemesis` (4157) ·
  `§0.5 Unintended Pregnancy` (4184) · `§0.6 Early Pregnancy Care and Recurrent Loss` (4209) ·
  `NEW_Obstetrics ## First-Trimester Pain` (4000)
- **G-B2 Antenatal care and screening** — `16_01-05 §0.3` +`.1 booking` +`.2 later` (93–128) ·
  `§0.4 Structural abnormality screening` +`.1` (129, 150) · `§0.5 Aneuploidy` +`.1`–`.6` (162–200) ·
  `§0.6 Invasive testing` +`.1 CVS` +`.2 amniocentesis` (201–217) · `§0.8 Antenatal timetable` (253) ·
  `NEW_Inv_OG §0.5`–`§0.8` (3769–3858)
- **G-B3 Hypertensive disorders of pregnancy** — `16_08-09 ## Pre-eclampsia` (934) ·
  `## HELLP` (962) · `16_14-15 ## Eclampsia` (1528) · `16_01-05 §0.12.3` (459) ·
  `O2 §0.1 Hypertensive Disorders` (4251) · `§0.2 Pre-eclampsia and Eclampsia` (4281) ·
  `NEW_Drugs_16 §0.8` (3446). (+ `Cardio B2 §0.5` — the dangling pointer's intended target)
- **G-B4 Antepartum haemorrhage and placenta** — `16_10-13 ## Placenta problems` +`### praevia`
  +`### accreta` +`### vasa praevia` +`### other anomalies` +`### other APH causes` (1373–1449) ·
  `16_14-15 ## Placental abruption` (1560) · `O2 §0.3 Antepartum Haemorrhage` (4331)
- **G-B5 Labour and delivery** — `16_10-13 ## Normal labour` +`### stages 1–3` +`### monitoring`
  (1075–1114) · `## Induction` +`### Bishop` +`### methods` (1115–1160) · `## Pain relief in labour`
  (1161) · `## Instrumental delivery` (1299) · `## Caesarean` (1314) · `O3 §0.1 Normal Labour` (4480) ·
  `§0.2 Abnormal Labour and Intrapartum Emergencies` (4511) · `NEW_Drugs_16 §0.7` +`.1`+`.2`
  (3427–3445) · `§0.9 Drugs for Preterm Labour` (3462)
- **G-B6 Obstetric emergencies** — `16_14-15 ## Cord prolapse` (1591) · `## Shoulder dystocia` (1614) ·
  `## PPH` (1638) · `## Uterine rupture` (1668) · `## DIC` (1686) · `## Amniotic fluid embolism` (1709) ·
  `O3 §0.3 Postpartum Haemorrhage` (4550) · `§0.4 The Unwell Postpartum Woman` (4587)
- **G-B7 Fetal wellbeing and growth** — `16_08-09 ## SGA` (878) · `## LGA` (899) ·
  `## Oligohydramnios` (985) · `## Polyhydramnios` (995) · `## Prematurity` (1011) ·
  `## Postmaturity` (1038) · `16_10-13 ## Reduced fetal movements` (1259) · `## Stillbirth/IUFD`
  (1346) · `O2 §0.4 Preterm Labour and PROM` (4368) · `§0.5 Fetal Concerns` (4389) ·
  `NEW_Inv_OG §0.10`–`§0.12` (3882–3964)
- **G-B8 Perinatal infection** — `16_06-07` all 15 sections (654–876) · `16_01-05 §0.12.11 HIV`
  `§0.12.12 rubella` `§0.12.13 measles` `§0.12.6 malaria` (512–652) · `O2 §0.6` (4418).
  **Cross-file with ID and Derm — see B-19**
- **G-B9 Contraception** — `16_16-17` all 24 sections (1734–1954) · `O6 §0.3 Contraception` (5290) ·
  `§0.4 Emergency Contraception and Unintended Pregnancy` (5352) · `NEW_Drugs_16 §0.1` +`.1`–`.4`
  (3335–3369)
- **G-B10 Abnormal uterine bleeding** — `17_02 ## AUB — Approach and DDx` (2095) ·
  `## Menorrhagia` (2141) · `O4 §0.1 PALM-COEIN` (4694) · `§0.2 Heavy Menstrual Bleeding` (4721) ·
  `§0.3 Intermenstrual, Postcoital and Postmenopausal Bleeding` (4761) ·
  `NEW_Drugs_16 §0.3` (3389) · `NEW_Gynae ## Acute Vaginal Bleeding` (3585)
- **G-B11 Amenorrhoea and PCOS** — `17_01 ## Normal menstrual cycle` (1993) ·
  `## Primary amenorrhoea` (2004) · `## Secondary amenorrhoea` +`### causes` (2032, 2038) ·
  `## PCOS` (2060) · `O4 §0.4 Amenorrhoea` (4802) · `NEW_Inv_OG §0.4 Hormone Panel` (3744).
  (+ `Endocrine I4 §0.6 Androgen Excess, Hirsutism and Virilisation` — see Endocrine G-E18)
- **G-B12 Menopause and HRT** — `17_02 ## Menopause` (2202) · `## HRT` (2235) ·
  `O4 §0.6 Menopause and Hormone Therapy` (4871) · `NEW_Drugs_16 §0.2` +`.1`+`.2` (3370–3388).
  (+ `Derm G6 §0.3 Menopause, Drugs and the Common Causes` of flushing)
- **G-B13 Endometriosis, fibroids and pelvic pain** — `17_05 ## Endometriosis` (2536) ·
  `## Fibroids` (2563) · `## Chronic pelvic pain` +`### mittelschmerz` +`### dyspareunia`
  +`### adenomyosis` (2589–2621) · `O4 §0.5 Dysmenorrhoea and Endometriosis` (4838) ·
  `O5 §0.4 Chronic Pelvic Pain` (5055) · `NEW_Drugs_16 §0.5` +`.1` (3406, 3408)
- **G-B14 PID and acute pelvic pain** — `17_05 ## PID` (2511) · `O5 §0.1 Acute Pelvic Pain` (4938) ·
  `§0.2 PID` (4962) · `NEW_Gynae ## Acute Pelvic Pain` (3615). (+ `GI C1 §0.8 Suprapubic Pain`)
- **G-B15 Ovarian pathology** — `17_10 ## Ovarian cancer` (3151) · `## Ovarian cysts` +4 (3181–3227) ·
  `## Ovarian torsion` (3228) · `O5 §0.3 Ovarian Pathology` (4998)
- **G-B16 Vulval conditions** — `17_07` all 10 sections (2734–2883) · `O5 §0.5 Vulval Symptoms` (5084)
- **G-B17 Vaginal discharge** — `17_08 ## Vaginal discharge — DDx` +6 subtypes (2885–2966) ·
  `NEW_Inv_OG §0.3 Genital/Cervical Swab Panel` (3718) · `NEW_Drugs_16 §0.12` (3497).
  **Cross-file with `ID 08_08 ## Bacterial vaginosis`, `## Trichomonas`, `## Chlamydia` etc.**
- **G-B18 Gynaecological cancer and screening** — `17_09 ## Cervical screening` (3034) ·
  `## Cervical cancer` (3066) · `## Vaginal cancer` (3090) · `## Endometrial cancer` (3104) ·
  `## Endometrial hyperplasia` (3135) · `NEW_Inv_OG §0.1`,`§0.2` (3666, 3696)
- **G-B19 Subfertility** — `17_06 ## Subfertility` +`### medical` +`### surgical` (2623–2662) ·
  `## IVF` +`### other options` +`### semen analysis` (2663–2706) · `## OHSS` (2707) ·
  `17_05 ## Male subfertility` (2492) · `NEW_Drugs_16 §0.6` (3416)
- **G-B20 Breast** — `NEW_Breast ## Breast Lump` `## Breast Pain` `## Galactorrhoea` (3263–3309) ·
  `O7 §0.1`–`§0.6` (5499–5716) · `NEW_Drugs_16 §0.11 Drugs Affecting Lactation` (3486).
  **Cross-file — see the breast flag above**
- **G-B21 Anti-D and rhesus** — `16_01-05 §0.7 Use of anti-D` (218) ·
  `NEW_Drugs_16 §0.10.2 Anti-D Immunoglobulin` (3477) · `NEW_Inv_OG §0.9 Kleihauer-Betke` (3859).
  (+ `Heme NEW_Inv_Haem ## Immunohematology`)

**MEDIUM**
- **G-B22 Physiological change and minor symptoms** — `16_01-05 §0.2 Physiological changes` (54) ·
  `§0.9 Minor symptoms` (292) · `§0.10 Hyperemesis gravidarum` (313) ·
  `16_10-13 ## Postpartum physiological changes` (1472). (+ `GI C2` nausea and vomiting)
- **G-B23 VTE in pregnancy** — `16_01-05 §0.11` +`.1 risk stratification` (354, 362).
  **Cross-file with `Heme 10_06b ## Postpartum VTE` (H-10) and `Heme J3 §0.6`**
- **G-B24 Sexual dysfunction** — `O6 §0.5 Sexual Dysfunction` (5390). Cross-file with
  `Renal 07 §0.16 Erectile Dysfunction` and `NEW_Drugs_13 §0.3`
- **G-B25 Perineal trauma** — `16_10-13 ## Perineal tears + episiotomy` (1450) ·
  `## Retained placenta` (1279). `GI §0.42` cites the tear grading from here

**UNGROUPED — stays put**: `16_10-13 ## Multiple pregnancy` (1189) · `## Breech` (1219) ·
`## Meconium-related problems` (1238) · `17_01 ## FGM` (1956, pending B-13) ·
`NEW_Drugs_16 §0.13 Sex Hormones` +`.1`+`.2` (3507–3522) · 6 administrative blocks

## LIMITATIONS
- B-19 (perinatal infection) is the largest undecided item — it needs the ID conclusion, and
  splitting it wrongly would lose the pregnancy-specific management that is the whole point.
- B-9 bears on **approved Cardio C-1**; B-20 on **approved Heme H-10**. Both flagged, not resolved.
- The `[[B2]] 0.5` dangling pointer remains **deliberately unfixed** pending a user ruling.
