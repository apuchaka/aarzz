# Cardio_merged.md — grouping and misplacement flags

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


Status: **ANALYSED. NOTHING MOVED.** Awaiting user decisions.
Sources: 10 · lines 4279 · most-referenced file in the vault (**92 inbound to `01_Cardiovascular`
alone**, of which **44 come from the Clinical Process set**: History-Taking ×19, Examination ×13,
Investigation-Interpretation ×12)

> **THIS FILE PRODUCED A METHOD-LEVEL FINDING — see `RUN_STATE.md` § "Off-by-one pointers".**
> `01_Cardiovascular` is **the only source in the vault with real numbering drift** (171 of 172 are
> clean, per `drift.py`). Its 21 damaged inbound pointers are **fixed as of `48a870f`**, so the
> POINTED AT BY figures below are now sound.
>
> **C-2/C-3 CONFIRMED by the user:** the standing rule extends to investigation interpretation.

## LEAD: self-declaring misfile (free, per the method)
| ID | Section | L | From → To | Evidence |
|---|---|---|---|---|
| C-1 | `## 0.4 Non-Stress Test (NST / Cardiotocography — CTG)` | 4239 | Cardio → **OBGYN** | self-flagged: *"Mis-filed — an obstetric investigation listed under Cardiology & Vascular"*, repeated at L4275. **A home already exists**: `GER7_Investigation_and_Lab_Addendum.md §0.5 Fetal Scalp Blood Sampling and Intrapartum Assessment` (L119–145) already covers intrapartum CTG. Decide OBGYN vs GER7. |

## PROPOSED MOVES

### Investigation-interpretation content in a disease file
| ID | Section | L | → | Why | Inbound |
|---|---|---|---|---|---|
| C-2 | `## 0.12 ECG Interpretation` + `.1`–`.12` (P wave, PR, AV blocks, QRS, BBB, axis, ST, T wave, chamber hypertrophy, athlete variants, hypothermia, digoxin effect) | 474–546 | **Investigation-Interpretation.md** | **`Investigation-Interpretation.md` contains NO ECG content.** Tested: `ECG` appears there twice — once as a CXR artefact (L59), once as *"correlate with the ECG"* inside the troponin entry (L274). Across all 16 Clinical Process files there are 10 mentions, every one incidental. **ECG has exactly two section-level homes in the whole vault and both are inside Cardio_merged.** That file's own subtitle is *"Template G — test-led, not disease-led"*, which is precisely what §0.12 is. | 0 section-level **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| C-3 | `### 0.1.1 ECG cardiac territories` | 33 | **Investigation-Interpretation.md**, with C-2 | leads → territory → vessel table; interpretation, not disease | 0 **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |

> **Scope question for the user.** The standing rule from GI M-16 names *history-taking, examination
> and communication*. C-2/C-3 are **investigation interpretation** — the fourth Clinical Process
> axis, named in the original brief but not in the standing rule. **Confirm the rule extends to it.**

### Examination content (standing rule)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| C-4 | `> [!info] Dynamic manoeuvres` (RILE; Valsalva/standing; squatting/handgrip; the HOCM and MVP exceptions) | 2483 | **Examination.md** | pure technique — *"this pair of exceptions is examined repeatedly"* **✅ EXECUTED 2026-09-01 → `Examination.md` (`c5df174`)** |
| C-5 | `### 0.21.2 Heart sounds`, `### 0.21.4 Pulses` | 790, 800 | **Examination.md §1.5** | how to interpret what you hear/feel. **`### 0.21.1 Murmurs — DDx` STAYS** — that is disease-mapping **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| C-6 | `> [!tip] Valsalva manoeuvre` (L438) and `> [!info] Vagal manoeuvres — do them properly` (L2051) | 438, 2051 | **Examination.md** | **two copies of one technique in one file**; the modified-Valsalva detail is in the B3 copy **✅ EXECUTED 2026-09-01 → `Examination.md` (`c5df174`)** |
| C-7 | `> [!danger] Fundoscopy is the examination that most often makes the diagnosis` | 1927 | **Examination.md §1.18** (Fundoscopy already exists there) | leave a pointer from B2 §0.3 **✅ EXECUTED 2026-09-01 → `Examination.md` (`c5df174`)** |
| C-8 | `> [!danger] The collateral history is the investigation` | 2268 | **History-Taking.md** | syncope collateral history **✅ EXECUTED 2026-09-01 → `History-Taking.md` (`c5df174`)** |
| C-9 | **14 `**Focused Hx:**` + 14 `**Examination:**` blocks**, all in `NEW_Cardiology_and_Vascular` | 3375–3541 | **History-Taking.md / Examination.md** | one pair per presentation — the exact Corpus B shape predicted. Largest single OSCE cluster found so far **✅ RESOLVED 2026-09-01 — Option 1: left in place, indexed in `Examination.md` §3 and `History-Taking.md` §2 (`bcf7515`/`fab04f5`)** |

### Non-cardiac presentations sitting in the cardiac file
| ID | Section | L | → | Inbound — **note the origin** |
|---|---|---|---|---|
| C-10 | `## 0.8 Undifferentiated Lump` (B6) | 2995 | **general / MSK or a lump-and-mass home** | **19 inbound, ZERO from cardiology**: MSK×7, ID×3, ENT×2, Heme×2, Paeds×2, Renal×2, Derm×1. Content is site-agnostic mass characterisation. **This is the GI M-15 shape, stronger.** |
| C-11 | `## 0.7 Generalised Pain` (B6) | 2959 | **MSK** | 2 inbound, both Neuro. Widespread musculoskeletal pain |
| C-12 | `## 0.6 Generalised Weakness` (B6) | 2916 | **Neuro** | 4 inbound: Endocrine×3, Neuro×1 |
| C-13 | `## 0.5 Fatigue, Lethargy and Malaise` (B6) | 2872 | **GP / general** | 8 inbound: MSK×3, Endocrine×2, Neuro×2, GI×1 |
| C-14 | `## 0.4 Eyelid and Facial Swelling` (B6) | 2833 | **arguable — Ophthalm / ENT / Derm** | 7 inbound: Derm×2, Endocrine×2, Heme×2, Neuro×1 |

> **B6 is a general-presentations file that has been filed as cardiology.** Only §0.1–0.3 (oedema,
> bilateral oedema, unilateral limb swelling) are cardiovascular. §0.4–0.8 are undifferentiated
> presentations whose **entire inbound traffic comes from other systems**. Recommend treating B6 as
> a split, not a move.

## KEEP + IN-TEXT FLAG
- **Troponin has FOUR section-level homes** and no owner: `01_CV §0.11 Cardiac Enzymes` (L461) ·
  `B1 §0.5 Troponin and Cardiac Biomarkers` (L1781) · `Investigation-Interpretation §1.12 Cardiac
  Markers (Troponin) and Lactate` · `GER7 §0.4 Troponins and Cardiac Biomarkers`. Flag all four.
- **`## 0.23 0.22a Rheumatic Heart Disease (RHD)`** (L836) — heading carries **two numbers**. This is
  the renumbering fingerprint that caused the off-by-one pointer damage. Flag; do not renumber
  (CLAUDE.md §1.14).
- `CV-X_Chronic_Heart_Failure` and `NEW_Cardiology_and_Vascular` have **zero inbound references**
  in any form.
- Cardiac procedures already live in the Clinical Process set —
  `NEW_Exam_Manoeuvres_and_Procedures §0.16 Cardioversion`, `§0.17 ICD`, `§0.18 Carotid
  Endarterectomy`. `B3 §0.6 Cardiac Device Events` (L2200) overlaps §0.17. Axis question, flag only.

## BROKEN POINTERS — **FIXED, commit `48a870f`** (kept as the record of what was wrong)
All target `01_Cardiovascular`; all off by exactly one; **all in the same direction.**
| Where | Says | Actually is | True home |
|---|---|---|---|
| `Heme Onc:780`, `Heme Onc:798` | `0.28 Deep Vein Thrombosis (DVT)` | 0.28 = Chronic Heart Failure | **0.29** |
| `Infectious Disease:1397` | `0.30 Infective Endocarditis` | 0.30 = Pulmonary Embolism | **0.31** |
| `Clinical-Process-EBM:220`, `GP_merged:49` | `0.39 Dyslipidaemia` | 0.39 = Carotid Artery Stenosis | **0.40** |
| `Examination:32`, `MSK:1275` | `0.33 Cardiac Tamponade` | 0.33 = Constrictive Pericarditis | **0.34** |
| `History-Taking:143`, `:200` | `0.29` for PE | 0.29 = DVT | **0.30** |
| `History-Taking:102` | `0.40` for ventricular ectopics/PACs | 0.40 = Dyslipidaemia | **0.41** |
| `Cardio:113`, `History-Taking:67`, `:71`, `Neuro:1774` | `0.34.5` Austroads | **does not exist** | **0.35.5** |
| `History-Taking:139` | `0.34.1` ACEi cough | **does not exist** | **0.35.1** |
| `Examination:154` | `0.35.8` leg ulcers | **does not exist** | **0.36.8** |

## GROUPINGS
**HIGH**
- **G-C1 Chest pain** — `01_CV §0.3 IHD` (210) · `B1 §0.1 Acute Chest Pain` (1621) · `B1 §0.2 Chest
  Tightness and Chronic Chest Pain` (1674) · `B1 §0.3 Pleuritic Chest Pain` (1708) ·
  `NEW_Card ## Acute Chest Pain` (3366) · `## Chronic Chest Pain` (3387) · `## Chest Tightness`
  (3394) · `## Pleuritic Chest Pain` (3401). **Corpus B and NEW_Card duplicate each other
  presentation-for-presentation — four topics, twice each.**
- **G-C2 Hypertension** — `01_CV §0.2` +`.1`–`.5` (118) · `B2 §0.1 Elevated BP` (1836) ·
  `B2 §0.2 Hypertensive Urgency` (1879) · `B2 §0.3 Hypertensive Emergency` (1910) ·
  `B2 §0.4 Paroxysmal/Secondary` (1952) · `NEW_Card ## Elevated Blood Pressure` (3477) ·
  `## Hypertensive Urgency` (3490) · `## Paroxysmal Hypertension` (3504). **Three-way.**
- **G-C3 Heart failure** — `01_CV §0.28` +`.1`–`.4` (936) · **the whole of `CV-X_Chronic_Heart_Failure`
  §0.1–0.7** (3047–3313) · `NEW_Drugs_06 §0.10 Drugs for Heart Failure` (3996) ·
  `NEW_Inv_Card §0.2 BNP/NT-proBNP` (4194). **CV-X is a complete second heart-failure file with
  zero inbound references.** The four-pillars framing is in CV-X §0.3 and NEW_Drugs_06 §0.10 both.
- **G-C4 AF and flutter** — `01_CV §0.4` +`.1`,`.2` (241) · `01_CV §0.19 Atrial Flutter` (640) ·
  `B3 §0.4 AF and Flutter` (2118). CHA₂DS₂-VASc in `01_CV §0.4.1`.
- **G-C5 Tachyarrhythmia** — `01_CV §0.9 Tachycardia: Peri-arrest` (412) +`.1 SVT` (422) ·
  `01_CV §0.7 VT` (368) · `B3 §0.1 Approach` (2006) · `B3 §0.2 Narrow Complex` (2042) ·
  `B3 §0.3 Broad Complex` (2082) · `NEW_Card ## Tachycardia` (3426) ·
  `## Multifocal Atrial Tachycardia` (3439)
- **G-C6 Bradycardia** — `01_CV §0.8 Bradycardia: Peri-arrest` (386) · `B3 §0.5 Symptomatic
  Bradycardia` (2161) · `NEW_Card ## Bradycardia and Symptomatic Bradycardia` (3408)
- **G-C7 Syncope / collapse** — `B4 §0.1 TLoC Framework` (2259) · `§0.2 Syncope` (2306) ·
  `§0.3 Presyncope` (2355) · `§0.4 Conscious Collapse` (2386) · `NEW_Card ## Presyncope` (3448).
  **No Corpus A partner** — `01_Cardiovascular` has no syncope section.
- **G-C8 Hypotension / shock** — `01_CV §0.20 Shock` +`.1`–`.4` (657) · `B4 §0.5 Hypotension`
  (2417) · `NEW_Card ## Hypotension` (3462)
- **G-C9 Murmurs and valves** — `01_CV §0.21` +`.1`–`.4` (749) · `B5 §0.1 Heart Murmurs —
  Assessment` (2468) · `B5 §0.2 New and Changing Murmur` (2517)
- **G-C10 Peripheral arterial disease** — `01_CV §0.36.1 PAD` (1292) · `§0.36.2 ABPI` (1315) ·
  `§0.36.3 Leriche` (1322) · `B5 §0.5 Claudication and PAD` (2621) · `B5 §0.6 Rest Pain / CLTI /
  Acute Limb Ischaemia` (2667) · `NEW_Card ## Claudication` (3533) ·
  `NEW_Drugs_06 §0.11.6 Drugs for PVD` (4088)
- **G-C11 Pacemakers / devices** — `01_CV §0.10 Pacemakers` (442) · `B3 §0.6 Cardiac Device Events`
  (2200) · (+ `NEW_Exam_Manoeuvres §0.17 ICD`, outside this file)
- **G-C12 Pericardial disease** — `01_CV §0.32 Pericarditis` (1109) · `§0.33 Constrictive
  Pericarditis` (1144) · `§0.34 Cardiac Tamponade` (1165)
- **G-C13 Dyslipidaemia** — `01_CV §0.40` (1537) · `NEW_Drugs_06 §0.9` +`.1`–`.6` (3952) ·
  `NEW_Inv_Card §0.3 Lipid Profile` (4218)
- **G-C14 Antihypertensive pharmacology** — `01_CV §0.2.4 side effects` (176) · `§0.35.1 detailed
  profiles` (1199) · **the whole of `NEW_Drug_Classes_Cardiovascular_Antihypertensives`**
  (3583–3671). **Three treatments of one drug class in one file.** Note `NEW_Drugs_06 §0.7
  Beta-Blockers` states it was built there as a **gap fix** because the antihypertensives file
  omitted them — a self-declared split.
- **G-C15 Oedema** — `B6 §0.1 Mechanism` (2724) · `§0.2 Bilateral/Generalised` (2758) ·
  `§0.3 Unilateral Limb Swelling` (2797) · `01_CV §0.29 DVT` (997)
- **G-C16 Anticoagulation** — `NEW_Drugs_06 §0.1` +`.1`–`.5` (3715) · `§0.2 Reversal` (3776) ·
  `01_CV §0.4.1` (271) · `01_CV §0.29/0.30` (997, 1034)

**MEDIUM**
- **G-C17 ACS** — `01_CV §0.1` +`.1`,`.6`–`.9` (6) · `B1 §0.5 Troponin` (1781) ·
  `01_CV §0.11 Cardiac Enzymes` (461) · `NEW_Drugs_06 §0.6 Drugs for Angina and ACS` (3847) ·
  `01_CV §0.15 Wellens' Syndrome` (569)
- **G-C18 Coronary vasospasm** — `B1 §0.4 Coronary Vasospasm` (1747) · `01_CV §0.12.7` ST-elevation
  list naming Prinzmetal (523). Medium: A mentions it only inside an ECG list.
- **G-C19 Cardiomyopathies** — `01_CV §0.24 HOCM` (855) · `§0.25 ARVC` (886) · `§0.26 Dilated` (905) ·
  `§0.27 Takotsubo` (921) · `§0.42 Restrictive` (1587) · `B5 §0.3 Peripartum` (2553). A cluster of
  siblings, not one topic — and **§0.42 Restrictive is a gap-fill that sits 15 sections away from
  its four siblings.**
- **G-C20 Inherited channelopathies** — `01_CV §0.16 Long QT` (579) · `§0.17 Short QT` (609) ·
  `§0.18 Brugada` (621) · `§0.13 WPW` (547)
- **G-C21 Aortic disease** — `01_CV §0.36.4 Aortic Aneurysm` (1330) · `§0.36.5 Aortic Dissection`
  (1353) · `§0.36.9 Popliteal Artery Aneurysm` (1426)
- **G-C22 Venous disease** — `01_CV §0.36.6 Varicose Veins` (1378) · `§0.36.7 Chronic Venous
  Insufficiency` (1399) · `§0.36.8 Lower Leg Ulcers` (1410)
- **G-C23 Rheumatic fever / RHD** — `01_CV §0.22` (810) · `§0.23` (836)
- **G-C24 Resuscitation** — `01_CV §0.5 ALS (Adult)` (314) · `§0.6 VF` (345) · `§0.7 VT` (368).
  **Cross-file axis question**: `Emergency and Crit Care §0.3 Advanced Life Support — Adult` (3110)
  is a second ALS entry. Flag, decide with Emergency.

**UNGROUPED — stays put**: `01_CV §0.14 Junctional Escape Rhythm` (563) · `§0.31 Infective
Endocarditis` (1072) · `§0.35.3 Adenosine` (1242) · `§0.35.5 Austroads driving rules` (1267) ·
`§0.37 Pulmonary Hypertension` (1449) · `§0.38 Congenital Heart Disease / Coarctation` (1483) ·
`§0.39 Carotid Artery Stenosis` (1512) · `§0.41 Cardiac Ectopic Beats` (1564) ·
`B5 §0.4 Post-Catheterisation Vascular Complications` (2587) ·
`NEW_Inv_Card §0.1 Antiphospholipid Panel` (4172) · 5 administrative `Build status` blocks

## LIMITATIONS
- Every POINTED AT BY count here that rests on a bare section number is **provisional** — see the
  off-by-one finding. File-level counts are sound; section-level ones are not, for `01_Cardiovascular`.
- `01_CV §0.38 Congenital Heart Disease` vs `Pediatrics_merged` congenital heart sections not yet
  cross-checked; deferred to the Paediatrics pass.
