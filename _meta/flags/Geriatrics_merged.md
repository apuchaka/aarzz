# Geriatrics_merged.md — grouping and misplacement flags

Status: **ANALYSED. NOTHING MOVED.**
Sources: 6 · lines 1347 · numbering drift: **none** · **no self-declared misfiles.**
Zero inbound: `NEW_Geriatrics` (which has no clinical content — only a skipped-topics table).

## THE HEADLINE: two of the five sources are not geriatrics
They are filed here because of the `GER` prefix, not because of their subject.

| Source | Inbound | Where the referrers are | Actually about |
|---|---:|---|---|
| `GER3_Preventive_and_Occupational_Health` | **31** | Endocrine ×5, Paediatrics, OBGYN, GP, AU1, Cardio… | **preventive health, screening, immunisation, lifestyle, occupational health, driving** |
| `GER4_Safeguarding_and_Forensic` | **37** | **Paediatrics ×14**, Neuro ×6, OBGYN, ID… | **child protection, family violence, sexual assault, elder abuse** |
| `GER1_Comprehensive_Geriatric_Assessment` | 10 | Neuro ×5, GI ×2 | genuinely geriatric |
| `GER2_Geriatric_Syndromes_and_End_of_Life_Care` | 7 | GI ×2, Neuro | genuinely geriatric |
| `18_Geriatrics_and_Older_Persons_Health` | 47 | GP ×8, Emergency… | genuinely geriatric |

**`GER4`'s single largest referrer is Paediatrics, at 14.** Only **one** of its 37 inbound
references is internal. It is a safeguarding file that no geriatrics content points at.

| ID | Source | L | → | Note |
|---|---|---|---|---|
| **R-1** | `GER4_Safeguarding_and_Forensic` — `§0.1 Safeguarding Mindset and Mandatory Reporting` · `§0.2 Recognising Child Abuse and Neglect` · `§0.3 Responding to a Child Protection Concern` · `§0.4 Family and Domestic Violence` · `§0.5 Sexual Assault` · `§0.6 Elder Abuse and Adults at Risk` | 1116–1330 | **`NEW_Safeguarding_and_Forensic`** | ⚠️ **A standalone Clinical Process file of that exact name already exists.** Safeguarding is currently split **three ways**: GER4 · `NEW_Safeguarding_and_Forensic` · `Pediatrics 15_24a Non-Accidental Injury and Sexual Abuse` (**Paediatrics P-5**). **Only `§0.6 Elder Abuse` has a geriatric claim**, and `18_ ## Abuse of Older People (Elder Abuse) and Carer Stress` (199) is its partner |
| **R-2** | `GER3_Preventive_and_Occupational_Health` — `§0.1 The Preventive Consultation` · `§0.2 Cardiovascular and Metabolic Risk` · `§0.3 Cancer Screening in Practice` · `§0.4 Immunisation` · `§0.5 Lifestyle Risk and Behaviour Change` · `§0.6 Occupational Health, Certification and Driving` | 919–1115 | **`PH1_Population_Health_and_Research_Literacy` or GP** | preventive health and screening. Pairs with **ID I-10** (vaccination schedule) and **Heme G-B18/G-P17**. ⚠️ **`§0.6` is the FOURTH Austroads driving home** — with `Cardio §0.35.5`, `Endocrine §0.15.8`, `Neuro ### Austroads Driving Standards (Neurological)` |

## PROPOSED MOVES — history / examination (standing rule)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| R-3 | `**History:**` + `**Examination:**` blocks under `## Falls in Older People` | 51, 55 | **History-Taking.md / Examination.md** | *"the circumstances of each fall (what they were doing…)"* — a history schema |
| R-4 | `### Distinguishing a fall from a collapse — do this first` | 18 | **History-Taking.md** | the discriminating question. ⚠️ **Cross-file: `Cardio B4 §0.4 Conscious Collapse and the Unwitnessed Fall` is the same discriminator** |
| R-5 | `### Communication and follow-up` (discharge planning) | 278 | **arguable — Communication.md** | flag only |

## PROPOSED MOVES — topic overlap
| ID | Section | L | → | Note |
|---|---|---|---|---|
| R-6 | `## 0.6 Osteoporosis and Fracture Prevention` (GER1) | 550 | **flag — MSK owns it** | `MSK 11_08b ## Osteoporosis` + `## Bisphosphonates`, `L7 §0.6 Fragility Fractures`, `Endocrine NEW_Drugs_10 §0.1`. **Five homes** — see MSK G-K17 |
| R-7 | `## 0.1 Continence` (GER2) | 613 | **flag** | with `Renal 07 §0.13`, `H2 §0.6`, `OBGYN 17_08 ## Urinary incontinence`, `O5 §0.6`, and `GI §0.42 Faecal Incontinence`. **Six homes across four files** |
| R-8 | `## 0.2 Pressure Injury` (GER2) | 658 | **flag** | with `Derm G2 §0.6 Wounds, Pressure Injury and Leg Ulcers` (D-11) and `Examination.md §1.28 Wound Management` |
| R-9 | `## 0.4 Immobility, Deconditioning and Hospital-Associated Decline` (GER2) | 760 | **flag** | ⚠️ **the destination of MSK K-27** (`L6 §0.6 Immobility, Mobility Aids and Functional Assessment`) |
| R-10 | `## 0.5 End-of-Life Care and Recognising Dying` · `## 0.6 Advance Care Planning in Practice` (GER2) | 794, 852 | **flag — decide with Heme H-21** | `Heme 10_11c Palliative Care Prescribing` and `J5 §0.4`–`§0.6`. **Palliative and end-of-life care is currently in Heme Onc and Geriatrics with no owner.** `GI C3 §0.6.3` and `C7 §0.6.3` also push advance care planning |
| R-11 | `## 0.3 Malnutrition and Nutrition` (GER2) | 707 | **flag** | with `GI C2 §0.6 Appetite Change, Early Satiety and Anorexia`, `Endocrine I5 §0.2 Unintentional Weight Loss`, `Cardio B6 §0.5 Fatigue` |

## GROUPINGS
**HIGH** — `18_` and `GER1` duplicate each other almost section for section.
- **G-R1 Falls** — `18_ ## Falls in Older People` +`### distinguishing fall from collapse`
  +`### risk factors` +`### assessment` +`### Mx` (10–91) · `GER1 §0.5 Falls` (507).
  (+ `Cardio B4 §0.4`, `Neuro D5 §0.5 Gait Disorders`)
- **G-R2 Frailty** — `18_ ## Frailty` +`### assessment` +`### why it changes management` +`### Mx`
  (92–149) · `GER1 §0.2 Frailty` (357)
- **G-R3 Polypharmacy and deprescribing** — `18_ ## Polypharmacy and Deprescribing`
  +`### anticholinergic burden` +`### tools` +`### Mx` (150–198) · `GER1 §0.4` (440) ·
  `GER6_Drug_Class_Addendum` (a Clinical Process file)
- **G-R4 Comprehensive geriatric assessment and function** — `GER1 §0.1 CGA` (308) ·
  `§0.3 Functional Assessment and the Australian Aged Care System` (394) ·
  `18_ ## Discharge Planning and Home Safety Assessment` +5 subsections (246–306)
- **G-R5 Elder abuse** — `18_ ## Abuse of Older People and Carer Stress` (199) ·
  `GER4 §0.6 Elder Abuse and Adults at Risk` (1284). **The one part of GER4 that belongs here**
- **G-R6 Geriatric syndromes** — `GER2 §0.1 Continence` (613) · `§0.2 Pressure Injury` (658) ·
  `§0.3 Malnutrition` (707) · `§0.4 Immobility` (760). See R-7 – R-11
- **G-R7 End of life** — `GER2 §0.5` (794) · `§0.6` (852). See R-10
- **G-R8 Preventive health** — `GER3 §0.1`–`§0.6` (920–1115). See R-2
- **G-R9 Safeguarding** — `GER4 §0.1`–`§0.5` (1117–1283). See R-1

**MEDIUM**
- **G-R10 Delirium and cognition in older people** — **no section here**, though
  `Neuro ## Delirium vs Dementia vs Depression — the "3 Ds" in Older People` (320) **self-declares
  it came from the Geriatrics category** (Neuro N-19). **A genuine gap in this file**, and the
  reason `GER1` is referenced by Neuro ×5

## LIMITATIONS
- R-1 and R-2 are **the largest structural items after the psychiatry block**, and both are
  cross-file. Neither is decided here.
- The **fourth Austroads home** (R-2) means driving standards now appear in Cardio, Endocrine,
  Neuro and Geriatrics, with `Clinical-Process-EBM:102` pointing at two. **Recommend one home,
  decided at the Clinical Process pass.**
