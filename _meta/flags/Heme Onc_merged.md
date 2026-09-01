# Heme Onc_merged.md — grouping and misplacement flags

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
Sources: 22 (most of any file) · lines 3730 · numbering drift: **none**.
Zero inbound: `10_10b_Haemonc_-_Transplant_Medicine`.

## LEAD: self-declared
| ID | Section | L | Note |
|---|---|---|---|
| H-1 | `## 0.25 Petechiae — **UNRESOLVED: not an investigation**` | 3686 | self-flagged, live marker. **A sign, not a test** — same shape as Renal RU-4 (Dark Urine) and GI M-17 (Pale Stools). **Three files have now independently produced this error class** |

## PROPOSED MOVES

### Investigation interpretation (standing rule, as extended)
`NEW_Investigations_Haematology` + `_Part2` are **25 investigation entries filed under a system**.
| ID | Section | L | → | Note |
|---|---|---|---|---|
| H-2 | `## CBC & Peripheral Blood` | 3240 | **Investigation-Interpretation.md §1.11** | **§1.11 "Full Blood Count and Blood Film" already exists** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |
| H-3 | `## 0.11 Coagulation Profile (PT/INR, APTT, Fibrinogen, D-dimer)` | 3366 | **Investigation-Interpretation.md §1.17** | **§1.17 "Coagulation Screen and D-dimer Interpretation" already exists** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| H-4 | `## 0.1 Interpreting the Coagulation Screen` (J3) | 2160 | **Investigation-Interpretation.md §1.17** | **a third copy of the same topic** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| H-5 | `## 0.9 How to interpret blood results — a quick approach` | 117 | **Investigation-Interpretation.md §1.11** | fourth interpretation entry **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| H-6 | `## Iron studies interpretation` | 426 | **Investigation-Interpretation.md** | **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| H-7 | `## Anaemia — DDx by MCV and reticulocyte index` | 408 | **Investigation-Interpretation.md** | the index table; the disease entries stay **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |
| H-8 | `## Immunohematology (Blood Group & Rh, DAT)` | 3305 | **Investigation-Interpretation.md** | ⚠️ **destination of approved GI M-2** (`## 0.33 Coombs / DAT-IAT` → Heme Onc). This is the fuller entry M-2's own text points at. **Recommend both land in Investigation-Interpretation, not Heme Onc — needs a ruling**, same shape as the Neuro N-1/CSF conflict **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |
| H-9 | remaining 20 entries of `NEW_Investigations_Haematology` + `_Part2` (B12, MMA, homocysteine, anti-IF, APCA, haptoglobin, Hb electrophoresis, EPO, factor VIII, vWF, ADAMTS13, HIT ELISA, SRA, flow cytometry, marrow/node biopsy, SPEP/SFLC, β2-microglobulin, osmotic fragility, sickle solubility, Schilling, lymphoscintigraphy) | 3251–3686 | **Investigation-Interpretation.md** | `## 0.18 Biopsy and Procedures` may belong with procedures instead — axis question **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |

### Topic in the wrong system
| ID | Section | L | → | Why |
|---|---|---|---|---|
| H-10 | `## Postpartum Infection and Thromboembolism` + `### Postpartum (puerperal) infection` + `### Postpartum VTE` | 782–808 | **OBGYN** | **puerperal sepsis is obstetric.** It sits inside `10_06b Thrombophilia, APS, Thrombocytosis, Methaemoglobinaemia` — a file about none of those things |
| H-11 | `### Haemolytic uraemic syndrome (HUS)` | 630 | **decide with Paediatrics** | `Pediatrics_merged 15_11` is titled *"Urological and Renal Anomalies, Wilms Tumour, **HUS**"* |
| H-12 | `## Primary Immunodeficiencies` (whole source, 15 sections) | 251–372 | **decide with Paediatrics / ID** | `Pediatrics_merged 15_15b` is *"Primary Immunodeficiencies and SCID"*. **3 inbound: Paediatrics ×2, ID ×1 — none from haematology** |
| H-13 | `## Lead poisoning` | 457 | **Emergency / toxicology** | sits under microcytic anaemia as a cause; the poisoning itself is tox |
| H-14 | `## Methaemoglobinaemia` | 718 | **Emergency / toxicology** | `Derm:2237` routes co-oximetry and methylene blue with the toxidromes |
| H-15 | `## Hereditary angioedema` | 1137 | **Immunology / ID** | `ENT:1252` already routes *"anaphylaxis and angioedema in [[K4]] 0.2"* |
| H-16 | `## Anaemia of chronic kidney disease` | 508 | **flag only** | duplicates `Renal §0.2.3 CKD-Related Anaemia`. Renal RU-17 is the other half |
| H-17 | `## 0.2 Organ transplant` +`.1 matching` +`.2 rejection types` | 1323–1351 | **flag — overlaps Renal** | `Renal §0.2.4 RRT Modalities`, `§0.2.5 Rejection`, `§0.2.6 Transplant complications`. **`10_10b` has zero inbound**; Renal's copy is referenced |
| H-18 | `## Cancer Outcomes in Aboriginal and Torres Strait Islander Australians` | 1487 | **arguable — `AU1_Australian_Health_Context_and_ATSI_Health`** | decide at the Clinical Process pass. Note `Resp §0.4` and `Neuro ## Strokes` carry parallel ATSI equity blocks — **a pattern, not a one-off** |
| H-19 | `## 10_12 Oncology — Breast` (breast cancer + 8 benign breast conditions) | 1612–1735 | **arguable — OBGYN or a breast home** | **12 inbound, Examination ×6** (i.e. from `Examination.md §1.17 Breast Examination`). Currently under oncology; the benign lumps are not oncology |
| H-20 | `## Thymoma` | 1169 | **flag only** | myasthenia association ties it to Neuro `D4 §0.5` |

### Palliative care — a whole topic without a home
| ID | Section | L | → |
|---|---|---|---|
| H-21 | `10_11c ## General principles` · `## Conversion between opioids` · `## Symptom management in palliative care` (1563–1611) **and** `J5 §0.4 Palliative Care Principles` (2658) · `§0.5 Symptom Control` (2687) · `§0.6 The Last Days of Life` (2724) | | **flag — candidate for its own home or Geriatrics/GP.** 11 + 20 inbound, **Anaes ×4, GP, MSK, Geriatrics** — referenced from across the vault, not from haematology. Decide after Geriatrics and GP |

## GROUPINGS
**HIGH** — Corpus A (10_*) and the J-files duplicate each other topic-for-topic.
- **G-H1 Approach to anaemia** — `10_04 ## Anaemia — DDx by MCV` (408) · `## Iron studies` (426) ·
  `J1 §0.1 Approach to Anaemia` (1737)
- **G-H2 Microcytic anaemia** — `10_04 ## Anaemia of chronic disease` (438) · `## Iron deficiency`
  (444) · `## β-thalassaemia` (463) · `## α-thalassaemia` (475) · `## Sideroblastic` (489) ·
  `J1 §0.2` (1761) · `J2 §0.6 Thalassaemia` (2107)
- **G-H3 Macrocytic anaemia** — `10_06a ## B12 deficiency` (668) · `## Folate deficiency` (682) ·
  `## Other causes` +`### liver` +`### alcohol` +`### hypothyroidism` (695–716) · `J1 §0.3` (1803) ·
  `NEW_Inv_Haem ## B12` `## MMA` `## Homocysteine` `## Anti-IF` `## APCA` (3251–3295) **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)**
- **G-H4 Normocytic and haemolytic anaemia** — `10_05 ## Normocytic haemolytic — intrinsic`
  +`### spherocytosis` +`### G6PD` +`### PNH` +`### HbC` (564–606) · `## extrinsic` +`### AIHA`
  +`### TTP` +`### HUS` +`### DIC` +`### macroangiopathic` +`### infections` (607–666) ·
  `J1 §0.4` (1838) · `J2 §0.1 Recognising Haemolysis` (1957) · `§0.2 Inherited` (1996) ·
  `§0.3 AIHA` (2021) · `§0.4 Microangiopathic and Mechanical` (2045)
- **G-H5 Sickle cell** — `10_05 ## Sickle cell disease` +`### acute crises` +`### crisis types`
  +`### long-term` (518–563) · `J2 §0.5` (2073) · `NEW_Inv_Haem_P2 §0.22 Sickle Solubility` (3612)
- **G-H6 Aplastic anaemia and marrow failure** — `10_04 ## Aplastic anaemia` (496) ·
  `10_06a ## Fanconi anaemia` (689) · `J1 §0.6 Platelet Disorders and Pancytopenia` (1888)
- **G-H7 Platelet and bleeding disorders** — `10_07 ## ITP` (810) · `## Thrombocytopaenia by
  severity` (825) · `## vWD` (841) · `### Other platelet disorders` (859) · `## Haemophilia` (864) ·
  `J3 §0.2 Inherited Bleeding` (2194) · `§0.3 Acquired Bleeding` (2228) ·
  `NEW_Inv_Haem_P2 §0.12 Factor VIII` `§0.13 vWF` `§0.14 ADAMTS13` (3393–3462)
- **G-H8 Thrombophilia and VTE** — `10_06b ## APS` (730) · `## Thrombophilia` +`### Factor V Leiden`
  (764–781) · `J3 §0.4 VTE Diagnosis` (2257) · `§0.5 Management and Anticoagulant Choice` (2283) ·
  `§0.6 Thrombophilia and Special Situations` (2324) · `NEW_Inv_Card §0.1 Antiphospholipid Panel`
  (**in Cardio** — cross-file)
- **G-H9 Anticoagulants and reversal** — `10_09a ## Anticoagulants` +`### DOACs` +`### Warfarin`
  +`### UFH` +`### LMWH` (1055–1108) · `## Antiplatelets` +`### Aspirin` +`### P2Y12` (1109–1126) ·
  `## Tranexamic acid` (1127) · `10_08 ## Warfarin — management of high INR` (911) ·
  `NEW_Inv_Haem_P2 §0.15 HIT ELISA` `§0.16 SRA` (3463–3501).
  **Cross-file: `Cardio NEW_Drugs_06 §0.1`–`§0.5` is a full second treatment of this class**
- **G-H10 Transfusion** — `10_08 ## ABO and Rh Compatibility` (925) · `## Blood products` +6
  subsections (943–1019) · `## MTP` (1020) · `## Transfusion complications` (1037) ·
  `NEW_Drugs_07 §0.1 Blood Products` (2787) · `NEW_Inv_Haem ## Immunohematology` (3305).
  **`10_08` has 15 inbound, Communication ×4** — consent-for-transfusion conversations
- **G-H11 Leukaemia** — `10_01 §0.1 ALL` `§0.2 CLL` `§0.3 Hairy cell` `§0.4 AML` `§0.5 CML` (8–78) ·
  `J4 §0.5 Leukaemia` (2521) · `NEW_Inv_Haem_P2 §0.17 Flow Cytometry` (3502)
- **G-H12 Myeloproliferative and MDS** — `10_01 §0.6 Myelofibrosis` (79) · `§0.7 MDS` (91) ·
  `§0.8 Polycythaemia vera` +`.1 DDx` (99, 109) · `10_06b ## Thrombocytosis` +`### Essential`
  (748, 757) · `J4 §0.6 Myeloproliferative Neoplasms` (2545) · `NEW_Inv_Haem ## EPO` (3324)
- **G-H13 Lymphoma** — `10_02 §0.1 NHL` +`.1 B cell` +`.2 T cell` (129–179) · `§0.2 Hodgkin` (180) ·
  `J4 §0.4 Lymphoma` (2481) · `10_09b ## Lymphadenopathy` (1180) ·
  `NEW_Inv_Haem_P2 §0.18 Biopsy` (3524)
- **G-H14 Myeloma and paraproteins** — `10_02 §0.3 Multiple myeloma` +`.1 other plasma cell
  disorders` (202, 232) · `J4 §0.1 Paraproteins and MGUS` (2383) · `§0.2 Multiple Myeloma` (2411) ·
  `§0.3 The Other Paraprotein Disorders` (2459) · `NEW_Inv_Haem_P2 §0.19 SPEP/SFLC` (3546) ·
  `§0.20 β2-microglobulin` (3570). (+ `Renal §0.8 Myeloma Kidney`, `NEW_Inv_Renal §0.12 UPEP`)
- **G-H15 Oncological emergencies** — `10_10a ## Neutropenic sepsis` (1226) · `## Tumour lysis`
  (1246) · `## SVCO` (1261) · `J5 §0.1 The Oncological Emergencies` (2580) ·
  `§0.2 Neutropenic Sepsis and Treatment Toxicity` (2595) · `§0.3 Metabolic and Structural` (2626)
- **G-H16 General oncology principles** — `10_11a ## Common cancers — AU incidence` (1353) ·
  `## Metastatic Disease` +`### bone mets` +`### CUP` (1378–1399) · `## Carcinogens` (1400) ·
  `## Tumour markers` (1410) · `## TNM Staging` (1426) · `## ECOG` (1449) ·
  `## Treatment Intent` (1473)
- **G-H17 Antineoplastic and immunomodulator pharmacology** — the whole of
  `NEW_Drugs_14` §0.1–§0.6 (3029–3195)
- **G-H18 Neutropenia** — `10_07 ## Neutropaenia` (887) · `J1 §0.5 White Cell Disorders` (1862) ·
  `NEW_Drugs_07 §0.2.3 Colony Stimulating Factors` (2861). ⚠️ **§0.2.3 self-declares it
  *"resolves the `G-CSF` row miscategorised onto the investigations build list"* — i.e. it is the
  destination for approved GI M-3.** Confirmed from both ends; note the file is the duplicated one
- **G-H19 Spleen** — `10_09b ## Hyposplenism` (1147) · `## Splenomegaly` (1159).
  (+ `GI C1 §0.5` post-splenectomy prophylaxis, `GI C3 §0.7 Hepatomegaly, Splenomegaly`)

**MEDIUM**
- **G-H20 Genetic cancer predisposition** — `10_11b §0.1`–`§0.5` (1500–1561). **3 inbound, all GP** —
  screening-driven. Flag against GP
- **G-H21 Fatigue and pallor** — `10_09b ## Fatigue and Pallor` (1194). **Cross-file duplicate of
  `Cardio B6 §0.5 Fatigue, Lethargy and Malaise`** (which C-13 already flags as non-cardiac)
- **G-H22 Porphyria** — `10_03b ## Acute intermittent porphyria` (374). 1 inbound (Anaes).
  Appears in the abdominal-pain "medical causes" list in `GI §0.41.2` and `C1 §0.1`

**UNGROUPED — stays put**: `10_03a ## Haematopoiesis — lineage overview` (364) ·
`NEW_Inv_Haem_P2 §0.21 Osmotic Fragility` (3586) · `§0.23 Schilling Test` (3638) ·
`§0.24 Lymphoscintigraphy` (3663) · 5 administrative blocks

## LIMITATIONS
- H-8 conflicts with approved **GI M-2** the same way Neuro N-1 conflicts with **M-1**. Both are the
  same pattern: a topic the Clinical Process set already owns, being moved between two system files.
  **Neither resolved here.**
- H-11, H-12, H-18, H-19, H-21 deliberately undecided pending Paediatrics, ID, OBGYN, GP.
- `NEW_Drugs_07_Blood_and_Electrolytes` is the **duplicated source** (also at
  `Endocrine and metabolics_merged.md:2889`). Its groupings are listed in both files' flags.
