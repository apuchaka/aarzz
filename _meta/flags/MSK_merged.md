# MSK_merged.md — grouping and misplacement flags

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
Sources: 24 · lines 5052 · numbering drift: **none**.
Zero inbound: `NEW_Orthopaedics_and_Trauma`, `NEW_Rheumatology_and_Immunology`.

## THE HEADLINE: `NEW_Investigations_Orthopaedics_Neurology_and_Other` is a grab-bag
Its own title says *"and Other"*. **18 entries; 11 are neither orthopaedic nor neurological.**
| ID | Section | L | → | Note |
|---|---|---|---|---|
| K-1 | `## 0.1 Blood Gas and Acid-Base Analysis` | 4040 | **Investigation-Interpretation.md §1.5** | **§1.5 "ABG / VBG Interpretation" already exists.** Third copy, with `Endocrine §0.20.6` and `F0-2 §0.1` |
| K-2 | `## 0.2 Electrolytes and Minerals` · `## 0.3 Osmolality and the Osmolar Gap` | 4071, 4097 | **Investigation-Interpretation.md** | overlaps `Endocrine §0.24`–`§0.26`, `I5 §0.5`–`§0.6` |
| K-3 | `## 0.8 Protein and Immune Profile (electrophoresis, Ig, free light chains)` | 4234 | **Heme Onc / Investigation-Interpretation** | **duplicates `NEW_Inv_Haem_P2 §0.19 SPEP/SFLC`** |
| K-4 | `## 0.11 Tumour Markers` | 4315 | **Heme Onc** | **duplicates `10_11a ## Tumour markers`** (Heme, L1410) |
| K-5 | `## 0.12 FAMCARE-P16` | 4344 | **palliative care / EBM** | a **family satisfaction measure in palliative care** — not an investigation and not orthopaedic. Pairs with Heme H-21 |
| K-6 | `## 0.13 Breast MRI` | 4365 | **OBGYN / breast** | pairs with Heme H-19 |
| K-7 | `## 0.14 KOH Preparation` · `## 0.15 Wet Mount (saline microscopy)` | 4395, 4421 | **Derm / OBGYN** | fungal scraping and vaginal wet mount |
| K-8 | `## 0.16 Slit Skin Smear` | 4447 | **Derm / ID** | leprosy — `ID 08_01-03 ## Leprosy` (145) |
| K-9 | `## 0.17 Newborn Bloodspot Screening` | 4473 | **Paediatrics** | `Pediatrics 15_24b Screening, SIDS, Vaccination Schedule` |
| K-10 | `## 0.18 STI Screening (asymptomatic sexual health check)` | 4497 | **ID** | **duplicates `ID 08_08 ### What a standard asymptomatic check consists of`** — and ID I-1 sends that to History-Taking |
| K-11 | `## 0.9 EMG and Nerve Conduction Studies` · `## 0.10 ICP Monitoring` | 4260, 4290 | **Investigation-Interpretation / Neuro** | serve `Neuro D4` and `Neuro ### Raised ICP` |
| K-12 | `## 0.4 DEXA` · `## 0.5 Bone Scan` · `## 0.6 Pelvic X-Ray` · `## 0.7 C-Spine X-Ray` | 4122–4233 | **Investigation-Interpretation.md** | genuinely orthopaedic, but interpretation. **§1.7 "Limb X-Ray and Fracture Description" already exists** |

## PROPOSED MOVES — investigation interpretation (standing rule, as extended)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| K-13 | `## 0.6 Joint Aspiration and Synovial Fluid Interpretation` (L1) | 2161 | **Investigation-Interpretation.md §1.15** | **§1.15 "Joint Aspirate (Synovial Fluid) Analysis" already exists** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| K-14 | `## 0.6 Autoantibody and Serology Interpretation` (L2) | 2471 | **Investigation-Interpretation.md §1.16** | **§1.16 already exists.** With ID I-2/I-3/I-4 this makes **four** files sending autoantibody interpretation to §1.16 **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| K-15 | `## 0.1 Describing a Fracture` (L7) | 3505 | **Investigation-Interpretation.md §1.7** | **§1.7 is titled "Limb X-Ray and Fracture Description"** — the same job **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| K-16 | `## Dermatomes — quick reference` + the 5 nerve-root/peripheral-nerve tables + `## Brachial Plexus Injury` (11_07a) | 797–891 | **Examination.md** | **5 inbound: Examination ×2, NEW_Exam_Manoeuvres, internal ×2.** A pure reference for the neurological examination. `GI C1` already cites it as *"the anatomy is already tabulated in [[11_07a…]]"* **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |

## PROPOSED MOVES — examination (standing rule)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| K-17 | **6** × `**Focused Hx:**` + **6** × `**Examination:**` *(count corrected 2026-09-01 — measured, not re-estimated)* in `NEW_Orthopaedics_and_Trauma` and `NEW_Rheumatology_and_Immunology` | 4889–5021 | **History-Taking.md / Examination.md** | L5021 is the classic *"look, feel, move, and assess neurovascular status"* |
| K-18 | `> Tinel's sign` · `> Phalen's sign` (11_03) | 395, 396 | **Examination.md** | *how to elicit*. **The carpal tunnel disease entry stays.** `NEW_Exam_Manoeuvres` already owns the analogous tests |

> **Structural note for the Clinical Process output: `NEW_Exam_Manoeuvres_and_Procedures.md` Part 1
> is 15 sections and *every one* is an MSK test** — Lachman, anterior/posterior drawer, pivot shift,
> Thompson, Finkelstein, grind, FABER, Trendelenburg, Adam's, SLR, femoral stretch, Schober,
> Spurling, distraction. It references MSK sources 9 times. **That file is effectively the MSK
> examination file already.**

## PROPOSED MOVES — topic in the wrong system
| ID | Section | L | → | Why |
|---|---|---|---|---|
| K-19 | `## Burns and Scalds` + `### First aid` + `### Assessment — depth and TBSA` + `### Mx` (11_09b) | 1183–1263 | **Emergency** | `Emergency A7 §0.1 Burns — Assessment`, `§0.2 Burns — Resuscitation and Management`, `§0.3 Chemical Burns`. **Duplicate** |
| K-20 | `## 0.3 Rhabdomyolysis` (11_01) | 58 | **flag** | `Emergency A7 §0.6 Crush Injury and Rhabdomyolysis`. **Duplicate** |
| K-21 | `## Ocular trauma` (11_09b) | 1304 | **Ophthalmology** | `Emergency A7 §0.4 Chemical Eye Injury`, `A8 §0.4 Corneal and Ocular FB` also exist |
| K-22 | `## Lower genitourinary tract trauma` · `## Splenic trauma` · `## Liver trauma` · `## Head injuries` (11_09b) | 1277–1303 | **flag** | GU trauma duplicates `Renal §0.19` and `H4 §0.6`; head injury duplicates `Neuro ### Head Injury`; splenic/liver duplicate `L8 §0.4` and `GI C1 §0.10` |
| K-23 | `## Autonomic dysreflexia` (11_06) | 694 | **arguable — Neuro** | a spinal-cord-injury complication, filed under spinal orthopaedics |
| K-24 | `## Henoch-Schönlein purpura` (12_04) | 1918 | **flag — Paediatrics** | `Pediatrics 15_14` is titled *"Anaemia, Sickle Cell, Hereditary Spherocytosis, **HSP**"*. Also `Derm` (purpura) |
| K-25 | `### Lupus nephritis` (12_03) | 1751 | **flag** | duplicates `Renal §0.6 Lupus Nephritis` |
| K-26 | `## 11_10 Paediatric Orthopaedics` (12 sections: JIA, transient synovitis, DDH, Perthes, SCFE, postural variants, rickets, Osgood-Schlatter, paediatric/Salter-Harris fractures) | 1316–1461 | **arguable — Paediatrics** | **8 inbound: MSK ×3, Examination ×2, History-Taking, NEW_Exam_Manoeuvres.** Counter-argument: they are orthopaedic conditions. **Decide with Paediatrics** |
| K-27 | `## 0.6 Immobility, Mobility Aids and Functional Assessment` (L6) | 3435 | **arguable — Geriatrics** | functional assessment and aids. Decide with Geriatrics |
| K-28 | `## Rickets` (11_10) | 1422 | **flag** | with `Endocrine §0.12 Vitamin D Deficiency`, `I3 §0.5 Metabolic Bone Disease`, `11_07b ## Osteomalacia` (939). **Four places** |

## KEEP + IN-TEXT FLAG
- **Trauma is in three files and duplicated within this one.** `11_09b ## Major Trauma — Primary
  Survey` +7 subsections (1132–1182) **and** `L8 §0.1 The Primary Survey and Trauma Principles`
  (3748) are the same topic twice in MSK; `L8 §0.4 Abdominal Trauma` (3860) is a **third** copy of
  the topic **you approved moving from GI (M-6) to Emergency**. ⚠️ **M-6 should be decided knowing
  MSK already holds two copies.**
- `## Bisphosphonates` (11_08b, 1029) duplicates `NEW_Drugs_10 §0.1.1` (in Endocrine).
- `12_04 ## Giant cell arteritis` (1868), `L3 §0.3 GCA — The Overlap` (2600), `Neuro ## Temporal
  Arteritis` (97, which defers here), `Neuro D1 §0.4` — **four homes, one correct pointer.**

## GROUPINGS
**HIGH**
- **G-K1 Hot swollen joint / septic arthritis** — `11_01 §0.1` +`.1 replaced joint` (6, 26) ·
  `L1 §0.1 The Acutely Hot Swollen Joint` (1955) · `§0.2 Septic Arthritis` (1992) ·
  `§0.5 Wider Monoarthritis DDx` (2135) · `11_10 ### Septic arthritis vs transient synovitis` (1339)
- **G-K2 Crystal arthropathy** — `12_02 §0.2 Gout` +`.1 Mx` (1648, 1658) · `§0.3 Pseudogout` (1668) ·
  `L1 §0.3 Crystal Arthropathy` (2043)
- **G-K3 Rheumatoid arthritis** — `12_01 ## RA` +`### Management` +`### Complications` (1463–1537) ·
  `L2 §0.2 Rheumatoid Arthritis` (2270) · `NEW_Drugs_19 §0.1.1`,`.2` (3975, 3986)
- **G-K4 Spondyloarthritis** — `12_02 §0.1 Ankylosing spondylitis` (1628) · `§0.4 Reactive arthritis`
  (1676) · `12_01 ## Psoriatic arthritis` (1606) · `L2 §0.3 Spondyloarthritis` (2324)
- **G-K5 Connective tissue disease** — `12_03 ## SLE` +`### Lupus nephritis` (1730, 1751) ·
  `## Systemic sclerosis` (1765) · `## Dermatomyositis` (1783) · `## Polymyositis` (1795) ·
  `## Sjögren` (1801) · `L2 §0.4 Connective Tissue Disease` (2368)
- **G-K6 Vasculitis** — `12_04 ## overview` (1818) · GPA (1835) · EGPA (1848) · comparison (1855) ·
  GCA (1868) · Takayasu (1893) · PAN (1902) · microscopic polyangiitis (1911) · HSP (1918) ·
  Behçet (1927) · `L2 §0.5 Vasculitis` (2422) · `L3 §0.3 GCA — The Overlap` (2600)
- **G-K7 PMR, fibromyalgia and chronic widespread pain** — `12_02 §0.5 PMR` (1688) ·
  `§0.6 Fibromyalgia` (1697) · `§0.7 CFS/ME` (1713) · `L3 §0.1 Approach to Muscle Symptoms` (2511) ·
  `§0.2 PMR` (2545) · `§0.4 Myopathy and the Raised CK` (2629) · `§0.5 Fibromyalgia` (2648) ·
  `§0.6 Chronic Fatigue and the Overlap Syndromes` (2696).
  (+ `Cardio B6 §0.7 Generalised Pain` — cross-file, see Cardio C-11)
- **G-K8 Osteoarthritis** — `12_01 ## OA` +`### hip` +`### knee` +`### hand` +`### Ix` +`### Mx`
  (1538–1605) · `L5 §0.4 Hip` (3124) · `§0.5 Knee` (3163)
- **G-K9 Back and neck pain** — `11_01 §0.4 Spinal cord compression` +`.1 cauda equina`
  +`.2 red flags` +`.3 spinal tumours` (72–131) · `11_06 ## Cervical spondylosis` (700) ·
  `## Degenerative cervical myelopathy` (710) · `## Spinal stenosis` (722) · `## Discitis` (783) ·
  `L4 §0.1 Approach and Red Flags` (2740) · `§0.2 Cauda Equina` (2785) · `§0.3 MSCC` (2824) ·
  `§0.4 Spinal Infection` (2856) · `§0.5 Mechanical Back Pain and Radiculopathy` (2890) ·
  `§0.6 Spinal Stenosis` (2925) · `§0.7 Neck Pain` (2960).
  (+ `Neuro ### Cauda Equina Syndrome`, `### MSCC` — see Neuro N-20. **Three files**)
- **G-K10 Regional limb pain — shoulder** — `11_02 ## Shoulder` +9 subsections (184–290) ·
  `L5 §0.2 Shoulder` (3052)
- **G-K11 — elbow** — `11_02 ## Elbow` +5 subsections (291–332) · `L5 §0.3 Elbow` (3096)
- **G-K12 — wrist and hand** — `11_03 §0.1 Hand` +7 subsections (386–448) · `L5 §0.6` (3203) ·
  `11_07a` median nerve table (837)
- **G-K13 — knee and ankle** — `11_05 §0.1`–`§0.7` (575–692) · `L5 §0.5 Knee` (3163) ·
  `§0.7 Ankle and Foot` (3235) · `11_03 §0.2 Foot` (449)
- **G-K14 — hip** — `11_04` 9 sections (487–573) · `L5 §0.4 Hip` (3124)
- **G-K15 Fractures** — `11_02 ## Distal radius/forearm` +Colles/Smith/Barton/Monteggia/Galeazzi
  (333–384) · `11_08c ## Fracture types` +`## Pathological fractures` (1049–1083) ·
  `L7 §0.1 Describing` (3505) · `§0.2 Healing and Complications` (3525) · `§0.3 Upper Limb Eponyms`
  (3562) · `§0.4 Lower Limb Eponyms` (3595) · `§0.5 Paediatric` (3634) · `§0.6 Fragility` (3677) ·
  `§0.7 Open Fractures` (3697) · `11_01 §0.5 Open fractures` +`.1 closed` (132, 148)
- **G-K16 Soft tissue injury** — `L6 §0.1`–`§0.5` (3294–3434) · `11_05 §0.7 Achilles` (665) ·
  `11_02 ### Rotator cuff` (216)
- **G-K17 Metabolic bone disease** — `11_08b ## Paget's` (982) · `## Osteoporosis` (997) ·
  `## Bisphosphonates` (1029) · `11_07b ## Osteomalacia` (939) · `11_10 ## Rickets` (1422) ·
  `L7 §0.6 Fragility Fractures` (3677) · `NEW_Inv_Ortho §0.4 DEXA` (4122).
  **Cross-file: `Endocrine I3 §0.5`, `§0.12 Vitamin D`, `NEW_Drugs_10 §0.1`**
- **G-K18 Bone infection** — `11_07b ## Osteomyelitis` (893) · `11_01 §0.6 Infective myositis` (154) ·
  `§0.7 Tendon sheath infection` (168) · `L4 §0.4 Spinal Infection` (2856) · `11_06 ## Discitis` (783)
- **G-K19 Bone tumours** — `11_09a` 5 sections (1085–1130) · `L4 §0.3 MSCC` (2824) ·
  `NEW_Inv_Ortho §0.5 Bone Scan` (4150). (+ `Heme 10_11a ### Bone metastases`)
- **G-K20 Trauma** — `11_09b ## Major Trauma — Primary Survey` +7 (1132–1182) ·
  `L8 §0.1`–`§0.6` (3748–3958). See the trauma flag above

**MEDIUM**
- **G-K21 Compartment syndrome** — `11_01 §0.2` (37). Ties to K-20 rhabdomyolysis
- **G-K22 Joint replacement** — `11_08a` 5 sections (951–979). **1 inbound (Emergency)**;
  `11_01 §0.1.1 Septic arthritis of a replaced joint` (26) is its complication
- **G-K23 Paediatric orthopaedics** — `11_10` 12 sections. See K-26

**UNGROUPED — stays put**: `11_04 ## Meralgia paraesthetica` (538) · `## Pubic symphysis
dysfunction` (549) · `11_06 ## Scheuermann's kyphosis` (767) · `## Scoliosis` (775) ·
`11_07b ## Osteochondritis dissecans` (912) · `## Fat embolism` (920) · `## Charcot joint` (931) ·
`NEW_Drugs_19 §0.1.3 Muscle Relaxants` (4000) · 5 administrative blocks

## LIMITATIONS
- K-19 – K-22 (trauma/burns) all bear on **approved GI M-6**. Recommend deciding trauma as one
  question across GI, MSK, Emergency and Neuro rather than file by file.
- K-24, K-26 (Paediatrics), K-27 (Geriatrics), K-21 (Ophthalmology) deliberately undecided.
