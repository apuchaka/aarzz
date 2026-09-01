# ENT_merged.md — grouping and misplacement flags

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
Sources: 18 · lines 1858 · numbering drift: **none** · no self-declared misfiles.
Zero inbound: `13_06c Bell's Palsy`, `13_07b Salivary Gland Problems`, `NEW_Drugs_09_ENT`,
`NEW_ENT_and_Oral`. `F3_Throat__Voice_and_Oral` 12 inbound (Neuro ×3, GI ×2, Endocrine).

## ALREADY APPROVED — the move out of this file
| ID | Section | L | → |
|---|---|---|---|
| **M-R1** ✅approved | `## 0.3 Barrett's oesophagus` · `## 0.4 Oesophageal carcinoma` | 653, 666 | **GI** |
| **M-R1** ✅approved | `## 0.1 Dysphagia — approach` · `## 0.5 Pharyngeal pouch` · `## 0.6 Globus pharyngeus` | 629, 679, 687 | **STAY in ENT** |
⚠️ **`ENT:662` carries a stale pointer** — *"(See also 03.08 for GORD…)"*. **03.08 is not GORD;
GORD is `03_Gastrointestinal §0.28`.** This is a **numeric pointer with no `[[ ]]` and no file
name**, so neither `dangling.py` nor `misaimed.py` can see it. **Fix by hand when M-R1 executes.**

## INBOUND FLAGS — decisions needed here
| From | Item | Existing owner here |
|---|---|---|
| **Neuro N-13** | `D7 §0.4 Speech, Voice and Swallowing` | `## Dysphonia (hoarseness)` +`### Causes` (584, 590) · `F3 §0.3 Hoarseness and the Voice` (1321) · `F3 §0.4 Oropharyngeal Dysphagia` (1352) |
| **Neuro N-14** | `D7 §0.5 Smell and Taste` | `F2 §0.4 Rhinitis` (1158) — weak; **no dedicated smell/taste section here.** Counter-evidence for N-14 |
| **Neuro N-15** | `04_Neurology ### Vertigo` + `D5` cluster | `## Vertigo` +`### central` +`### peripheral` (158–188) · `## BPPV` (236) · `## Ménière's` (244) · `## Vestibular neuronitis` (260) · `## (Viral) labyrinthitis` (272) · `F1 §0.6 Vertigo, Trauma and Foreign Bodies` (1013). ⚠️ **`D5` has 21 inbound and ENT is the largest external referrer at ×6** |
| **ID I-16** | `### Acute epiglottitis` | `## Acute epiglottitis` (519) |
| **ID I-17** | `### Centor criteria` | `## Sore throat` +`### Management` (415, 438) · `F3 §0.1 Sore Throat` (1256). ⚠️ **`Cardio §0.22` already routes here and flags that Centor/FeverPAIN thresholds differ in Australia — preserve that caveat** |
| **ID I-18** | `K4 §0.5 Allergic Rhinitis and the Atopic March` | `## Allergic Rhinitis (Hay Fever)` (332) · `F2 §0.4 Rhinitis` (1158) · `NEW_Drugs_09 §0.4` (1691) |
| **Emergency X-10** | `F0-5 §0.10 Tonsillitis and Peritonsillar Abscess` | `### Complications of tonsillitis` (458) · `### DDx of unilateral tonsillar enlargement` (453) |
| **Emergency X-13** | `A8 §0.2 Aural` · `§0.3 Nasal` · `§0.5 Oropharyngeal FB` | `F1 §0.6` (1013) · `F2 §0.6 Nasal Trauma and Foreign Bodies` (1214) · `ENT:535` (the gap-fill note) |
| **Resp G-R15** | `NEW_Resp ## Acute Stridor` | `## Stridor — overview` (486) · `## Croup` (497) · `## Acute epiglottitis` (519) · `## Foreign body airway obstruction` (533) · `## Laryngomalacia` (549) · `Emergency A2 §0.5`,`§0.6`. **Five files** |
| **Endocrine G-E3** | thyroid nodule | `F4 §0.4 Thyroid Nodules` (1532) |

## PROPOSED MOVES OUT
| ID | Section | L | → | Why |
|---|---|---|---|---|
| T-1 | `## 0.1 Examining the Ear and Assessing Hearing` (F1) | 852 | **Examination.md §1.19/§1.20** | **§1.19 "Otoscopy" and §1.20 "Rinne and Weber Tests" already exist.** `13_02` and `13_03` have **Examination ×5 and ×4 inbound** **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| T-2 | 4 × `**Focused Hx:**` + 4 × `**Examination:**` in `NEW_ENT_and_Oral` | 1779–1819 | **History-Taking.md / Examination.md** | L1780 *"assess the airway before the throat"*; L1793 *"otoscopy of both ears"*; L1819 *"listen to the voice and characterise it"* |
| T-3 | `## 0.1 Lumps in the neck — approach` (13_07a) · `## 0.1 Approach to a Neck Lump` (F4) | 705, 1454 | **flag — same topic twice** | and **cross-file with `Cardio B6 §0.8 Undifferentiated Lump`** (19 inbound, none cardiac — Cardio C-10) |
| T-4 | `## 0.4 Thyroid Nodules` (F4) | 1532 | **flag — Endocrine** | `Endocrine 06 §0.3 Thyroid Cancers`, `§0.4 Goitre`, `I1 §0.5 Thyroid Nodule and Goitre`, `NEW_Inv_Endo §0.2 Thyroid Ultrasound`. **Five homes** |
| T-5 | `## Bell's palsy` (13_06c) | 697 | **keep as the stub it is** | **This is the model to follow elsewhere.** It is a deliberate stub that defers to `[[04_Neurology]]` and explains why. **Zero inbound and that is correct** — it exists to preserve one cross-reference. Do not delete it |
| T-6 | `## 0.5 Head and Neck Cancer` (F4) · `## HNSCC` +`### HPV-related` (13_06a) | 1563, 598, 618 | **flag** | with `Heme 10_11a ## Common cancers` and `## Tumour markers`. HPV ties to `OBGYN 17_07 ## Genital warts` and `O6` |
| T-7 | `## Dentistry for doctors` +`### Assessing tooth pain` · `## Trismus` · `## Facial swellings due to dental infection` · `## Systemic disease complicating dental infection` · `## Periodontal disease` +`### Vincent's angina` (13_07c) | 796–851 | **flag — arguable own home** | **1 inbound, internal.** Dental content in an ENT file; `F3 §0.6 Salivary Glands and Dental Problems` (1406) is the partner |
| T-8 | `## Obstructive sleep apnoea` · `## Primary (simple) snoring` (13_05b) | 570, 560 | **flag — Resp** | `Resp §0.18 Sleep Apnoea`, `RESP-X §0.5 Sleep-Disordered Breathing`, `NEW_Inv_Resp §0.4 Sleep Studies`, `Psychiatry N7 §0.5 Excessive Daytime Sleepiness` (**moved out of Neuro by A1, `f5e49c9`**). **Five homes** |
| T-9 | `## CSF rhinorrhoea` (13_04) | 361 | **flag** | ⚠️ **the destination of approved GI M-1** is CSF studies incl. **β-transferrin**, which is exactly this. `Neuro ### CSF Interpretation` and `Investigation-Interpretation §1.13` are the others. **Four-way — see Neuro N-1** |
| T-10 | `## Cancer of the paranasal sinuses` (324) · `## Nasopharyngeal cancer` (400) | | **keep, flag** | with T-6 |

## KEEP + IN-TEXT FLAG
- **Vertigo is the most duplicated topic in this file**: `13_02 ## Vertigo` +`### central`
  +`### peripheral` (158–188) · `13_03 ## BPPV` (236) · `## Ménière's` (244) ·
  `## Vestibular neuronitis` (260) · `## (Viral) labyrinthitis` (272) · `F1 §0.6` (1013) ·
  **plus `Neuro 04 ### Vertigo` and the whole of `Neuro D5`** (N-15). **Two files, eight sections.**
  `Examination.md §1.21` already owns Dix-Hallpike and HINTS.
- **`13_01`/`F1` and `13_04`/`F2` and `13_05a`+`13_05b`/`F3` and `13_07a`/`F4` are clean Corpus A ↔
  Corpus B pairs** — this file has the tidiest pairing after Derm.
- `NEW_Drugs_09_ENT` (**zero inbound**) — `§0.1 Drugs for Ear Infections`, `§0.2 Cerumenolytics`,
  `§0.3 Mouth and Throat`, `§0.4 Rhinitis and Sinusitis`, `§0.5 Intranasal Decongestants`,
  `§0.6 Other Nasal`.

## GROUPINGS
**HIGH**
- **G-T1 Otalgia and otitis** — `13_01 ## Otitis externa` +`### malignant OE` (6, 34) ·
  `## Causes of otalgia` (44) · `## Causes of a discharging ear` (54) · `## Otitis media (acute)`
  (62) · `## Glue ear` (80) · `## Chronic otitis media` (101) · `F1 §0.2 Otalgia` (888) ·
  `§0.3 Otitis Externa and Otitis Media` (908) · `NEW_Drugs_09 §0.1` (1646) ·
  `NEW_ENT_and_Oral ## Acute Ear Pain` (1787)
- **G-T2 Hearing loss** — `13_02 ## Hearing loss — DDx` (113) · `## Tinnitus — DDx` (133) ·
  `13_03 ## Childhood deafness` (189) · `## Deafness in adults` (204) · `## Otosclerosis` (212) ·
  `## Vestibular schwannoma` (222) · `F1 §0.4 Hearing Loss` (952) · `§0.5 Sudden SNHL and Tinnitus`
  (982) · `§0.1 Examining the Ear and Assessing Hearing` (852)
- **G-T3 Vertigo** — see the flag above
- **G-T4 Rhinosinusitis and rhinitis** — `13_04 ## Rhinosinusitis` +`### acute` +`### Mx by
  severity` +`### with polyps` +`### complications` (284–323) · `## Allergic Rhinitis` (332) ·
  `F2 §0.2 Acute Rhinosinusitis` (1097) · `§0.3 Chronic Rhinosinusitis and Nasal Polyps` (1127) ·
  `§0.4 Rhinitis` (1158) · `NEW_Drugs_09 §0.4` +`.1`+`.2` (1691–1715) · `§0.5`,`§0.6` (1716, 1733)
- **G-T5 Epistaxis** — `13_04 ## Epistaxis` +`### Management` +`### Post-bleeding advice`
  (370–399) · `F2 §0.1 Epistaxis` (1061) · `NEW_ENT_and_Oral ## Acute Epistaxis` (1798)
- **G-T6 Nasal trauma and obstruction** — `13_04 ## Nasal fractures` (353) · `## CSF rhinorrhoea`
  (361) · `F2 §0.5 Nasal Obstruction and the Unilateral Red Flags` (1184) · `§0.6 Nasal Trauma and
  Foreign Bodies` (1214)
- **G-T7 Sore throat and tonsillitis** — `13_05a ## Sore throat` +`### Management` +`### DDx of
  unilateral tonsillar enlargement` +`### Complications` +`### Tonsillectomy` (415–482) ·
  `F3 §0.1 Sore Throat` (1256) · `NEW_ENT_and_Oral ## Acute Sore Throat` (1773) ·
  `NEW_Drugs_09 §0.3` (1675). **Cross-file — ID I-17, Emergency X-10**
- **G-T8 Airway-threatening throat and stridor** — `13_05b ## Stridor — overview` (486) ·
  `## Croup` (497) · `## Acute epiglottitis` (519) · `## Foreign body airway obstruction` (533) ·
  `## Laryngomalacia` (549) · `F3 §0.2 The Airway-Threatening Throat` (1289). **Five files —
  see the inbound table**
- **G-T9 Sleep-disordered breathing** — `13_05b ## Primary snoring` (560) · `## OSA` (570). See T-8
- **G-T10 Dysphonia and head/neck cancer** — `13_06a ## Dysphonia` +`### Causes` (584, 590) ·
  `## HNSCC` +`### HPV-related` (598, 618) · `F3 §0.3 Hoarseness and the Voice` (1321) ·
  `F4 §0.5 Head and Neck Cancer` (1563) · `NEW_ENT_and_Oral ## Acute Hoarseness` (1810)
- **G-T11 Dysphagia and oesophageal** — `13_06b §0.1`–`§0.6` (629–692) ·
  `F3 §0.4 Oropharyngeal Dysphagia` (1352). **See M-R1**
- **G-T12 Neck lumps** — `13_07a §0.1 approach` +`§0.2 DDx by anatomical location` (705, 715) ·
  `F4 §0.1 Approach` (1454) · `§0.2 Cervical Lymphadenopathy` (1482) · `§0.3 Congenital and
  Midline Lumps` (1508) · `§0.4 Thyroid Nodules` (1532)
- **G-T13 Salivary glands and xerostomia** — `13_07b §0.1 Sialadenitis` +`§0.2 Sialolithiasis`
  +`§0.3 Salivary gland tumours` +`§0.3.1` +`§0.4 Xerostomia` (746–795) ·
  `F3 §0.6 Salivary Glands and Dental Problems` (1406). **`13_07b` has zero inbound**
- **G-T14 Oral lesions** — `F3 §0.5 Oral Lesions and Oral Cancer` (1380) ·
  `13_07c` dental cluster (796–851)
- **G-T15 Facial pain** — `F4 §0.6 Facial Pain and Swelling` (1597) · `13_07c ## Trismus` (811) ·
  `## Facial swellings due to dental infection` (821). **Cross-file: `Neuro ## Trigeminal
  Neuralgia`, `D7 §0.6`**

**MEDIUM**
- **G-T16 Bell's palsy** — `13_06c ## Bell's palsy` (697), a deliberate stub. See T-5

## LIMITATIONS
- N-14 (smell and taste) is the one inbound flag this file gives **counter-evidence** against —
  there is no smell/taste section here to receive it. Recorded as a finding.
- T-9 (CSF rhinorrhoea) makes the CSF question **four-way**. Flagged with Neuro N-1.
