# Emergency and Crit Care_merged.md — grouping and misplacement flags

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
Sources: 15 · lines 4034 · numbering drift: **none** · no self-declared misfiles.
`F0-4_Resuscitation_Algorithms` 15 inbound (**Paediatrics ×6**);
`A5_Toxicology_II` 14 (**Derm ×5**, Neuro).

## THE SHAPE: this is the destination file for the most approved moves so far
**Four already-approved GI moves land here** (M-6 abdominal trauma, M-8 paracetamol, M-9 ascending
cholangitis, plus the trauma question), and six more are proposed from other files. It is also the
file whose own content is **most duplicated elsewhere**.

## INBOUND FLAGS — decisions needed here
| From | Item | Existing owner here |
|---|---|---|
| **GI M-6** ✅approved | `C1 §0.10 Abdominal Trauma` | **none** — `FAST` appears once in the whole file; only trauma heading is `A7 §0.5 Minor Traumatic Wound`. ⚠️ **But `MSK 11_09b` and `MSK L8 §0.4` both hold abdominal trauma** (MSK K-22). **Decide trauma as one question** |
| **GI M-8** ✅approved | `## 0.10 Paracetamol Overdose` + King's College criteria | `F0-1 §0.6 Paracetamol Overdose` (2460) — **deliberate duplicate, do not merge** |
| **GI M-9** ✅approved | `## 0.4 Ascending Cholangitis` | `F0-3 §0.11 Biliary Sepsis — Ascending Cholangitis` (2996) — **deliberate duplicate, do not merge** |
| **Neuro N-16** | `## Serotonin Syndrome and NMS` | `A6 §0.3 Hyperthermia versus Fever, and the Drug-Induced Hyperthermias` (1383) |
| **Neuro N-17** | `## Opioid Toxicity` | `F0-1 §0.5 Opioid-Induced Respiratory Depression` (2429) |
| **Psychiatry Y-1** | `14a-2 Overdose and Poisoning Management` (4 sections) | `A5 §0.1 The Poisoned Patient` (1027) · `§0.2 TCA Overdose` (1077) · `§0.3 Benzodiazepine` (1115) · `F0-1 §0.1`–`§0.8` |
| **MSK K-19** | `## Burns and Scalds` (4 sections) | `A7 §0.1 Burns — Assessment` (1609) · `§0.2 Burns — Resuscitation and Management` (1657) · `§0.3 Chemical Burns` (1687) |
| **MSK K-20** | `## 0.3 Rhabdomyolysis` | `A7 §0.6 Crush Injury and Rhabdomyolysis` (1790) |
| **ID I-13** | `## Sepsis` | `A1 §0.2 SIRS, Sepsis and Septic Shock` (40) · `§0.3 Sepsis Phenotypes by Source` (73) · `F0-3 §0.7 Adult Sepsis` (2876) · `§0.8 Paediatric Sepsis` (2903) · `§0.9 Meningococcal Sepsis` (2931) · `§0.10 Urosepsis` (2965) — **six sepsis sections already here** |
| **Derm D-1** | `## Anaphylaxis` | `F0-1 §0.9 Anaphylaxis and Acute Allergic Reaction` (2557) · `NEW_Drugs_01_Allergy_and_Anaphylaxis` (whole source) · `§0.5 Sympathomimetics (Anaphylaxis) — Adrenaline` (3833) |
| **Anaes A-3** | airway adjuncts | `A2 §0.8 Tracheostomy and Laryngectomy Emergency` (429) · `F0-4 §0.6 Intubation and RSI` (3202) |

⚠️ **Rule 5 (CLAUDE.md): `NEW_Drugs_01 §0.5 Sympathomimetics (Anaphylaxis) — Adrenaline` (3833) and
`F0-4 §0.4 Paediatric Resuscitation` (3146) are where the weight-banded adrenaline figures live.**
`Pediatrics 15_01a` and `15_01b` hold the other copies. **No merge here without checking every
per-kg figure and every injector band survives.**

## PROPOSED MOVES OUT
| ID | Section | L | → | Why |
|---|---|---|---|---|
| X-1 | `## 0.1 The A–E Approach` (F0-4) | 3042 | **Examination.md §1.1** | **§1.1 "ABCDE Assessment (Acutely Unwell / Deteriorating Patient)" already exists.** `Examination:32` was one of the off-by-one pointers fixed in `48a870f` and points back into Cardio for Beck's triad **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| X-2 | `## 0.1 The Deteriorating Patient — Recognition` (A1) · `## 0.2 Vital Signs and Early Warning Scores` (Examination §1.2's topic) | 11 | **flag — Examination.md §1.2** | **§1.2 "Vital Signs and Early Warning Scores (Recognising the Deteriorating Patient)" already exists.** Same title, two files **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| X-3 | `## 0.2 Basic Life Support` · `## 0.3 Advanced Life Support — Adult` (F0-4) | 3076, 3110 | **flag — Cardio duplicate** | `Cardio §0.5 Advanced Life Support (Adult)` (314) carries an **ANZCOR verification box** with a correction: *"ANZCOR timing is NOT the same as the UK/ERC protocol — adrenaline timing genuinely differs by one shock"*. **Keep that box with whichever copy survives.** Cardio G-C24 is the other half |
| X-4 | `## 0.7 Mechanical Ventilation` · `## 0.8 Procedural Sedation` · `## 0.11 Fascia Iliaca Block` (F0-4) | 3241, 3270, 3359 | **`GER8_Procedure_Addendum` / `NEW_Exam_Manoeuvres_and_Procedures`** | procedures, not emergencies **✅ EXECUTED 2026-09-01 → `Procedures.md` (`98ceb40`)** |
| X-5 | `## 0.9 Adult Analgesia` · `## 0.10 Paediatric Analgesia` (F0-4) | 3298, 3330 | **flag** | with `Anaes 03a §0.7`, `AN1 §0.6`, `NEW_Drugs_03 §0.4`, `Heme 10_11c ## Conversion between opioids`. **Five analgesia homes** |
| X-6 | `## 0.1 Acute Asthma` · `## 0.2 Acute Exacerbation of COPD` · `## 0.4 Severe CAP and ARDS` · `## 0.5 Neuromuscular Respiratory Failure` (F0-5) | 3399–3559 | **flag — Resp** | `Resp §0.1.1 Acute exacerbation`, `§0.2.3 Exacerbation of COPD`, `§0.8.1 CAP`, `§0.15 ARDS`. **F0-5's acute-management framing is the delta** |
| X-7 | `## 0.3 Acute Pulmonary Oedema` (F0-5) | 3468 | **flag — Cardio** | `Cardio §0.28.1 Acute heart failure — Mx` and `CV-X §0.5 Decompensation` |
| X-8 | `## 0.6 Acute Severe Headache` · `## 0.7 Major Head Injury` · `## 0.8 Minor Head Injury` (F0-5) | 3560–3653 | **flag — Neuro** | `Neuro D1 §0.2 Thunderclap Headache and SAH`, `### Head Injury`, `### Who gets a CT head` (Neuro N-2) |
| X-9 | `## 0.9 Acute Renal Colic` (F0-5) | 3654 | **flag — Renal** | `Renal 07 §0.15 Urinary Tract Stones`, `H4 §0.4 Renal Colic and Urolithiasis` |
| X-10 | `## 0.10 Tonsillitis and Peritonsillar Abscess (Quinsy)` (F0-5) | 3689 | **flag — ENT** | `ENT ## Sore throat` +`### Complications of tonsillitis` +`### DDx of unilateral tonsillar enlargement` |
| X-11 | `## 0.2 Drugs for Allergic and Inflammatory Eye Conditions` · `## 0.3 Other Drugs for Allergic Eye Conditions` (NEW_Drugs_01) | 3776, 3806 | **Ophthalmology** | `Opthalm NEW_Drugs_11_Eye` is the eye-drug file |
| X-12 | `## 0.4 Corneal and Ocular Foreign Body` (A8) · `## 0.4 Chemical Eye Injury` (A7) | 1938, 1723 | **flag — Ophthalmology** | `Opthalm E1 §0.5 Chemical Injury, Trauma and Foreign Bodies` (1018). See MSK K-21 |
| X-13 | `## 0.2 Aural Foreign Body` · `## 0.3 Nasal Foreign Body` · `## 0.5 Oropharyngeal Foreign Body` (A8) | 1872–1997 | **flag — ENT** | `ENT:535` explicitly cites the FB content in `13_06b` and `13_02` |
| X-14 | `## 0.7 Rectal Foreign Body` (A8) | 2032 | **flag — GI** | |
| X-15 | `## 0.8 Vaginal Foreign Body` (A8) | 2064 | **flag — OBGYN** | |
| X-16 | `## 0.6 Swallowed Foreign Body` (A8) | 1998 | **flag — GI / ENT** | food bolus is `GI C6 §0.3.1` |

## KEEP + IN-TEXT FLAG
- **`A8_Foreign_Bodies_by_Site` is organised by site, so every one of its 8 sections belongs to a
  different system** (ear, nose, eye, oropharynx, oesophagus, rectum, vagina). **2 inbound, both
  GER8.** ⚠️ **This is the single clearest "one source, eight destinations" case in the vault** —
  and splitting it destroys the cross-site principles in `§0.1 Foreign Bodies — General Principles`.
  **Recommend keeping the source intact and pointing at it**, not splitting.
- `F0-1 §0.10 Australian Elapid Snakebite` (2592) · `§0.11 Spider Bites — Redback vs Funnel-Web`
  (2624) · `NEW_Drugs_04 §0.2 Antivenoms` (3956) are **distinctively Australian and referenced from
  nowhere else.** Preserve as a set.
- `A9_Transfusion, Coagulopathy and Anticoagulant Emergencies` (4 sections) has **5 inbound, 0
  internal** — Anaes ×3, Cardio. Cross-file with `Heme 10_08` and `10_09a` (Heme G-H9/G-H10).

## GROUPINGS
**HIGH**
- **G-X1 The deteriorating patient and resuscitation** — `A1 §0.1`–`§0.6` (11–207) ·
  `F0-4 §0.1 A–E` (3042) · `§0.2 BLS` (3076) · `§0.3 ALS Adult` (3110) · `§0.4 Paediatric
  Resuscitation` (3146) · `§0.5 Neonatal Resuscitation` (3174). **Cross-file: `Cardio §0.5`,
  `Pediatrics 15_01a`, `Examination.md §1.1`/`§1.2`**
- **G-X2 Sepsis and shock** — `A1 §0.2`,`§0.3` (40, 73) · `F0-3 §0.1 Shock Framework` (2679) ·
  `§0.2 Hypovolaemic` (2717) · `§0.3 Cardiogenic` (2746) · `§0.4 Tamponade` (2777) ·
  `§0.5 Massive PE` (2809) · `§0.6 Adrenal Crisis` (2843) · `§0.7`–`§0.11` (2876–3031).
  **Cross-file: `Cardio §0.20 Shock` +`.1`–`.4`, `ID 08_09 ## Sepsis`, `Endocrine §0.6.1
  Addisonian Crisis`**
- **G-X3 Airway** — `A2 §0.1`–`§0.8` (208–472) · `F0-4 §0.6 Intubation and RSI` (3202) ·
  `Anaes 03a §0.2 Airway Adjuncts`. **Cross-file: `ENT ## Stridor — overview`, `## Croup`,
  `## Acute epiglottitis`, `Resp NEW_Resp ## Acute Stridor`, `Pediatrics M6 §0.2`. Five files**
- **G-X4 Respiratory failure** — `A3 §0.1`–`§0.8` (473–745) · `F0-5 §0.1`,`§0.2`,`§0.4`,`§0.5`
  (3399–3559). **Cross-file: `Resp §0.3 Respiratory Failure`, `RESP-X §0.6`**
- **G-X5 Dyspnoea and cough** — `A4 §0.1`–`§0.7` (746–1016). **Cross-file: `Resp NEW_Resp ##
  Acute Dyspnoea`/`## Acute Cough`, `Cardio B6`, `NEW_Drugs_18 §0.2 Drugs for Cough`**
- **G-X6 Toxicology** — `A5 §0.1`–`§0.7` (1017–1303) · `F0-1 §0.1`–`§0.8` (2287–2556) ·
  `NEW_Drugs_04 §0.1 Antidotes` (3900) · `§0.3 Drugs That Chelate Iron` (3993).
  **Cross-file: `Psychiatry 14a-2` (Y-1), `GI §0.10 Paracetamol` (M-8), `Neuro ## Opioid Toxicity`
  (N-17), `Heme ## Lead poisoning`/`## Methaemoglobinaemia` (H-13/H-14)**
- **G-X7 Environmental and thermal injury** — `A6 §0.1`–`§0.8` (1304–1600) ·
  `A7 §0.1`–`§0.6` (1601–1825). **Cross-file: `MSK 11_09b ## Burns and Scalds` (K-19)**
- **G-X8 Allergy and anaphylaxis** — `F0-1 §0.9` (2557) · `NEW_Drugs_01 §0.1`–`§0.5` (3738–3862).
  **Cross-file: `Derm 09_01 ## Anaphylaxis` (D-1), `ID K4` (7 sections), `Pediatrics 15_01b`,
  `ENT ## Allergic Rhinitis`. Five files**
- **G-X9 Transfusion and anticoagulant emergencies** — `A9 §0.1`–`§0.4` (2098–2286).
  **Cross-file: `Heme 10_08`, `10_09a`, `Cardio NEW_Drugs_06 §0.2 Reversal`**
- **G-X10 Foreign bodies** — `A8 §0.1`–`§0.8` (1826–2097). See the A8 flag
- **G-X11 Envenomation** — `F0-1 §0.10`,`§0.11` (2592, 2624) · `NEW_Drugs_04 §0.2` (3956)
- **G-X12 Procedures** — `F0-4 §0.7 Mechanical Ventilation` (3241) · `§0.8 Procedural Sedation`
  (3270) · `§0.9`,`§0.10 Analgesia` (3298, 3330) · `§0.11 Fascia Iliaca Block` (3359)

## LIMITATIONS
- **Trauma is the single biggest unresolved cross-file question** — GI M-6 (approved),
  MSK `11_09b` + `L8`, `Neuro ### Head Injury`, `F0-5 §0.7`/`§0.8`. **Four files, and Emergency
  currently has the least of it.** Recommend one trauma decision covering all four.
- X-6 to X-10 are all the same shape: `F0-5` is an **acute-management layer over five other
  systems**. Splitting it would lose that layer; leaving it duplicates five files. **Not decided.**
