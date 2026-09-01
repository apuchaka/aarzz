# Pediatrics_merged.md — grouping and misplacement flags

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
Sources: 43 (most in the vault) · lines 4132 · numbering drift: **none** ·
**no self-declared misfiles — the only system file with none.**
Zero inbound: `15_09a Congenital Abdominal Wall and GI Anomalies`, `15_13a Neural Tube Defects`,
`15_18a Precocious and Delayed Puberty, CAH`, `15_18b Genetic Disorders Inheritance Summary`,
`15_22a Neonatal Sepsis and Seizures`.

## THE SHAPE OF THIS FILE IS DIFFERENT
Paediatrics is **the destination of more cross-file flags than any other file** — nine raised so far
point here. It is also the file whose Corpus B set (M1–M7) is **most heavily referenced by other
systems**: `M5 Paediatric GI, GU and Limb` has **36 inbound** (MSK ×10, GI ×6, Renal), `M6` 22,
`M7` 22 (**Neuro ×9**). **Recommend resolving Paediatrics' boundary before the system files that
point at it**, not after.

## INBOUND FLAGS ALREADY RAISED — decisions needed here
| From | Item | Their line | Paediatrics' existing owner |
|---|---|---|---|
| **GI M-10** | neonatal/infant two-thirds of `C2 §0.3 Bilious vs Non-Bilious Vomiting` | GI 1948 | `## Mid-gut malrotation` (972) · `## Pyloric stenosis` (894) · `## Hirschsprung` (910) · `M3 §0.4 Neonatal Vomiting` (3168) · `M5 §0.2 Vomiting and Gastroenteritis` (3549) |
| **Endocrine E-8** | `## 0.8 Carnitine Levels` · `## 0.9 Plasma Amino Acid Screen` | Endo 3615, 3632 | `## Inherited metabolic disease` (1869) · `15_17b Glycogen Storage, PKU, Lysosomal` |
| **Endocrine E-9** | `F0-2 §0.4 Paediatric Diabetic Ketoacidosis` | Endo 1173 | `15_16b Diabetes Mellitus, MODY, DKA` (1730) |
| **Neuro N-18** | `### Febrile Convulsions` | Neuro 794 | `M6 §0.5 Seizures and Febrile Convulsions` (3850) · `15_12a Epilepsy Syndromes` |
| **Heme H-11** | `### Haemolytic uraemic syndrome` | Heme 630 | `15_11 Urological and Renal Anomalies, Wilms, **HUS**` (1200) |
| **Heme H-12** | `## Primary Immunodeficiencies` (15 sections) | Heme 251 | `15_15b Primary Immunodeficiencies and SCID` (1635) |
| **MSK K-24** | `## Henoch-Schönlein purpura` | MSK 1918 | `15_14 Anaemia, Sickle Cell, HS, **HSP**` (1525) |
| **MSK K-26** | `11_10 Paediatric Orthopaedics` (12 sections) | MSK 1316 | `M5 §0.5 The Limping Child` (3650) · `§0.6 Bone Pain and Paediatric Orthopaedic Conditions` (3690) |
| **MSK K-9** | `## 0.17 Newborn Bloodspot Screening` | MSK 4473 | `15_24b Screening, SIDS, Vaccination Schedule` (2582) |
| **OBGYN B-14/B-15/B-16** | ophthalmia neonatorum · birth injuries · routine newborn care | OBGYN 825, 1054, 4605 | `M3 Neonatal Problems` · `15_22b`, `15_23a`, `15_23b` |
| **ID G-I10** | childhood exanthems and diphtheria | ID 558–728 | `15_03a Childhood Viral Exanthems` (283) |
| **Resp §0.22** | paediatric respiratory rows parked *"for whichever file comes up next"* | Resp 812 | `M6 §0.2 Stridor` (3759) · `§0.3 Bronchiolitis and Preschool Wheeze` (3784) · `§0.4 Asthma in Children` (3816) · `15_04a`, `15_04b` |

**Every one has an existing owner here.** None of these is a gap; all are duplications.

## PROPOSED MOVES OUT

### History-taking / communication (standing rule)
| ID | Section | L | → | Why |
|---|---|---|---|---|
| P-1 | `## 0.2 The HEEADSSS Psychosocial Assessment` (M7) | 3970 | **History-Taking.md** | **a named history-taking framework.** The single clearest standing-rule item in this file **✅ EXECUTED 2026-09-01 → `History-Taking.md` (c5df174)** |
| P-2 | `## 0.1 Adolescent Development and the Consultation` (M7) | 3944 | **Communication.md** | how to run the consultation, incl. seeing the young person alone |
| P-3 | `## 0.3 Confidentiality, Consent and the Mature Minor` (M7) | 3992 | **`A10_Ethics__Capacity__Consent_and_Certification`** | Gillick/mature minor is a **consent and capacity** topic. `A10` is the owner |
| P-4 | `> Get down to the child's level, introduce yourself to THEM…` (M1 §0.6 Practical Paediatrics) | 2806–2851 | **Examination.md / Communication.md** | **`Examination.md §1.23 Approach to Paediatric Examination` already exists** **✅ EXECUTED 2026-09-01 → `Examination.md` (`c5df174`)** |
| P-5 | `15_24a Non-Accidental Injury and Sexual Abuse` (whole source) | 2541–2581 | **`NEW_Safeguarding_and_Forensic`** | **14 inbound, Communication ×4.** Safeguarding is that file's stated subject. Pairs with **OBGYN B-13 (FGM)** **✅ EXECUTED 2026-09-01 → `Safeguarding.md` (`98ceb40`)** |

### Investigation interpretation (standing rule, as extended)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| P-6 | `## 0.1 Measuring and Plotting Growth` (M4) | 3281 | **Investigation-Interpretation.md §1.19** | **§1.19 "Growth Charts and Percentile Interpretation" already exists** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| P-7 | `## Anaemia in children — approach` + `### Approach to haemolysis` (15_14) | 1528, 1542 | **Investigation-Interpretation.md §1.20** | **§1.20 "Paediatric Bloods and Imaging — How Interpretation Differs from Adults" already exists.** Serves Heme G-H1/G-H4 **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |

## KEEP + IN-TEXT FLAG
- **`15_01a Paediatric and Newborn Life Support` has 1 inbound (Examination) and duplicates
  `Emergency F0-4 §0.4 Paediatric Resuscitation` and `§0.5 Neonatal Resuscitation`.**
  ⚠️ **CLAUDE.md rule 5 territory** — this is where weight-based resuscitation figures live.
  **Flag; do not merge without checking every per-kg figure survives.**
- `15_01b Anaphylaxis` (143) has **7 inbound, none internal** (Emergency ×3, Derm ×2, Cardio).
  With `Derm D-1`, `Emergency F0-1 §0.9` and `NEW_Drugs_01`, anaphylaxis is in **five** places.
  **Rule 5 again: the ASCIA adrenaline bands are the figures at risk.**
- `## 0.6 ADHD` (M7, 4086) duplicates `Psychiatry 14_07 Attention Deficit Hyperactivity Disorder`.
  **M7 has 22 inbound with Neuro ×9** — and Neuro is where the psychiatry Corpus B set currently
  sits. **Decide M7's adolescent-mental-health half with the psychiatry block.**
- `M5 §0.4 Urinary Tract Infection and Enuresis` (3620) and `15_10 UTI, Nephrotic Syndrome,
  Glomerulonephritis` (1040) vs `Renal 07 §0.11 UTIs`. Enuresis has no adult partner.
- `15_09b Infant Feeding Problems` (1005) and `M3 §0.3 Feeding, Weight and Hypoglycaemia` (3137)
  vs `OBGYN NEW_Drugs_16 §0.11 Drugs Affecting Lactation` and `O3 §0.5`.

## GROUPINGS
**HIGH** — Corpus A (15_*) and the M-files map cleanly; the M-files are presentation-organised.
- **G-P1 The seriously unwell child** — `15_01a Life Support` (3–142) · `15_02 Ill and Feverish
  Child` (179) · `M1 §0.1 Recognising` (2659) · `§0.2 Why Children Compensate and Then Crash` (2692) ·
  `§0.3 Resuscitation and the Sick Child Pathway` (2720) · `§0.4 The Unwell Infant` (2753) ·
  `§0.5 The Irritable, Lethargic or Pale Child` (2774).
  (+ `Emergency F0-3 §0.8 Paediatric Sepsis`, `F0-4 §0.4`)
- **G-P2 Fever in children** — `15_02` (179–282) · `M2 §0.1 Approach to the Febrile Child` (2853) ·
  `§0.2 Fever in the Young Infant` (2876) · `§0.3 Fever Without Source` (2899) ·
  `§0.4 The Serious Bacterial Infections` (2934) · `§0.5 Rash in a Febrile Child` (2958) ·
  `§0.6 Specific Infections and the Australian Context` (3003).
  (+ `ID K1 Fever Workup` — cross-file, ID G-I1)
- **G-P3 Childhood exanthems** — `15_03a` (283–360) · `M2 §0.5` (2958).
  **Cross-file with `ID 08_05-06` — see ID G-I10**
- **G-P4 Paediatric respiratory** — `15_04a URTI and LRTI` (396) · `15_04b Asthma in Children` (494) ·
  `M6 §0.1 Assessing Respiratory Distress` (3737) · `§0.2 Stridor and Upper Airway Obstruction`
  (3759) · `§0.3 Bronchiolitis and Preschool Wheeze` (3784) · `§0.4 Asthma in Children` (3816).
  **Cross-file with `Resp §0.22`'s parked rows, `ENT ## Croup`/`## Laryngomalacia`, `Emergency A2`**
- **G-P5 Congenital heart disease** — `15_05 Acyanotic CHD` (580) · `15_06 Cyanotic CHD, Kawasaki,
  Murmurs` (659) · `M3 §0.2 The Cyanosed or Collapsed Neonate` (3096).
  **Cross-file with `Cardio §0.38 Congenital Heart Disease incl. Coarctation`** (Cardio's own
  limitation note defers this here)
- **G-P6 Paediatric abdomen** — `15_07 Abdominal Pain, Neuroblastoma, Coeliac, Malnutrition,
  Diarrhoea and Vomiting` (747) · `15_08 Surgical Abdomen` (855) · `15_09a Congenital Abdominal Wall
  and GI Anomalies` (935) · `M5 §0.1 Acute Abdominal Pain in Children` (3512) ·
  `§0.2 Vomiting and Gastroenteritis` (3549) · `§0.3 Constipation and Soiling` (3584).
  **Cross-file with `GI C2 §0.3` (M-10), `GI C5 §0.2 Constipation` (the load-bearing orphan)**
- **G-P7 Neonatal problems** — `15_22a Neonatal Sepsis and Seizures` (2309) ·
  `15_22b Neonatal Respiratory Distress and Jaundice` (2359) · `15_23a NEC, Neonatal Hypoglycaemia,
  Hypotonia` (2421) · `15_23b Minor Neonatal Problems` (2459) · `M3 §0.1 Neonatal Jaundice` (3048) ·
  `§0.5 Apnoea and BRUE` (3204) · `§0.6 Common and Minor Neonatal Problems` (3236).
  ⚠️ **`## Neonatal jaundice` appears at 2383 AND `M3 §0.1` at 3048 — plus `### Jaundice <24h`,
  `### 24h–2 weeks`, `### >2 weeks` (2389–2404).** Cross-file with `GI C3 Jaundice`
- **G-P8 Growth and development** — `15_19a Developmental Milestones and Delay` (2035) ·
  `15_19b Cerebral Palsy and Muscular Dystrophies` (2104) · `M4 §0.1 Measuring and Plotting Growth`
  (3281) · `§0.2 Growth Faltering` (3308) · `§0.3 Short Stature` (3348) · `§0.4 Tall Stature,
  Obesity and Puberty` (3386) · `§0.5 Developmental Milestones and Surveillance` (3411) ·
  `§0.6 Developmental Delay and Neurodevelopmental Conditions` (3449) ·
  `15_13b Autism Spectrum Disorder and Cleft Lip/Palate` (1485)
- **G-P9 Paediatric renal** — `15_10 UTI, Nephrotic Syndrome, Glomerulonephritis` (1040) ·
  `15_11 Urological and Renal Anomalies, Wilms, HUS` (1200) · `M5 §0.4 UTI and Enuresis` (3620)
- **G-P10 Paediatric neurology** — `15_12a Epilepsy Syndromes and Status Epilepticus` (1279) ·
  `15_12b Brain Tumours` (1391) · `15_13a Neural Tube Defects` (1439) ·
  `M6 §0.5 Seizures and Febrile Convulsions` (3850) · `§0.6 Epilepsy and Paediatric Neurology` (3897)
- **G-P11 Paediatric haematology and oncology** — `15_14 Anaemia, Sickle Cell, HS, HSP` (1525) ·
  `15_15a ITP and ALL` (1623) · `15_15b Primary Immunodeficiencies and SCID` (1635) ·
  `15_12b Brain Tumours` (1391) · `15_11` Wilms. **Cross-file with Heme — H-11, H-12**
- **G-P12 Paediatric endocrine** — `15_16a Hypothyroidism` (1695) · `15_16b Diabetes, MODY, DKA`
  (1730) · `15_17a Hyperthyroidism and Inherited Metabolic Disease` (1848) ·
  `15_17b Glycogen Storage, PKU, Lysosomal` (1897) · `15_18a Precocious and Delayed Puberty, CAH`
  (1949) · `M4 §0.4 Tall Stature, Obesity and Puberty` (3386). **Cross-file with Endocrine E-8, E-9**
- **G-P13 Genetics** — `15_18b Inheritance Summary` (2006) · `15_20a Trisomies and Sex Chromosome
  Disorders` (2148) · `15_20b Imprinting Disorders` (2212) · `15_21a Microdeletion Syndromes` (2229) ·
  `15_21b Fragile X, Achondroplasia, Noonan, Marfan` (2261).
  (+ `Neuro N-21 Neurofibromatosis / Tuberous Sclerosis`, `Heme 10_11b Genetic Cancer Predisposition`)
- **G-P14 Paediatric MSK** — `M5 §0.5 The Limping Child` (3650) · `§0.6 Bone Pain and Paediatric
  Orthopaedic Conditions` (3690). **Cross-file — MSK K-26**
- **G-P15 Adolescent health** — `M7 §0.1`–`§0.6` (3944–4130). See the ADHD flag
- **G-P16 Safeguarding** — `15_24a Non-Accidental Injury and Sexual Abuse` (2541). See P-5
- **G-P17 Screening and immunisation** — `15_24b Screening, SIDS, Vaccination Schedule` (2582).
  **Cross-file with `ID 08_01-03 ## Vaccination Schedule` (I-10) and `NEW_Drugs_20`**

**MEDIUM**
- **G-P18 HIV in children** — `15_03b` (361). 1 inbound (ID). Cross-file with ID G-I3
- **G-P19 Infant feeding** — `15_09b` (1005) · `M3 §0.3` (3137)

**UNGROUPED — stays put**: `15_01b Anaphylaxis` (143, pending the five-way flag) ·
`M1 §0.6 Practical Paediatrics` (2806, pending P-4)

## LIMITATIONS
- **This file has no self-declared misfiles**, so the lead-with-self-declared step produced nothing
  and every flag here rests on reading plus the inbound index.
- Nine cross-file flags land here. **I have not decided any of them** — each needs the two files
  compared side by side, and several (anaphylaxis, paediatric life support, paediatric DKA) carry
  weight-based figures that CLAUDE.md rule 5 says must be checked before anything moves.
