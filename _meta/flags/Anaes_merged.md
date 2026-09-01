# Anaes_merged.md — grouping and misplacement flags

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
Sources: 4 · lines 1068 · numbering drift: **none** · no self-declared misfiles.
`03a_Anaesthetics_Primer` 9 inbound (**Clinical-Process-EBM ×3, Examination**);
`AN1_Perioperative_Care` 8 inbound, **0 internal** (MSK ×5, Resp ×2, GER8).

## THE SHAPE: this file is mostly *procedure* and *drug* content, and it is small
Only two sources are clinical (`03a`, `AN1`) and **they duplicate each other section for section.**
The other two are drug files. `AN1` is referenced only from outside anaesthetics.

## PROPOSED MOVES
| ID | Section | L | → | Why |
|---|---|---|---|---|
| A-1 | `## 0.5 Pre-Operative Assessment` + its `**History:**` and `**Examination:**` blocks | 197–231 | **Examination.md §1.12** | **§1.12 "Pre-Anaesthetic Assessment (Airway + Fitness for Anaesthesia)" already exists** — and `Anaes:23` **already points at it**: *"See [[Examination]] Pre-Anaesthetic Assessment"*. **The file itself has made this move once and not the second time** **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| A-2 | `## 0.1 Preoperative Assessment` (AN1) · `## 0.2 Airway Assessment and Anaesthetic Technique` (AN1) | 344, 388 | **Examination.md §1.12** | the Corpus B partner of A-1 **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| A-3 | `## 0.2 Airway Adjuncts` +`.1 OPA` +`.2 NPA` +`.3 supraglottic` +`.4 BVM` +`.5 ETT` +`.6 laryngoscope` +`.7 tracheostomies` | 64–113 | **`NEW_Exam_Manoeuvres_and_Procedures` / `GER8_Procedure_Addendum`** | equipment and technique. **Cross-file: `Emergency A2 §0.8 Tracheostomy and Laryngectomy Emergency`, `F0-4 §0.6 Intubation and RSI`** |
| A-4 | `## 0.3 Regional / Local Anaesthesia` +`.1 nerve blocks` +`.2 risks` +`.3 neuraxial` +`.4 epidural` +`.5 spinal` | 114–171 | **flag — procedures** | `GER8_Procedure_Addendum` is the natural home. **`OBGYN 16_10-13 ## Pain relief in labour` (1161) duplicates the epidural content** |
| A-5 | `## 0.6 Group & Hold / Crossmatch` | 232 | **Heme Onc / Investigation-Interpretation** | `Heme 10_08 ## ABO and Rh Compatibility`, `NEW_Inv_Haem ## Immunohematology`. **Three homes** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| A-6 | `## 0.4 Post-Operative Nausea and Vomiting (PONV)` | 172 | **flag — GI owns antiemetics** | `GI C2 §0.5 Antiemetic Selection by Mechanism` (**16 inbound, Anaes ×2**) and `NEW_Drugs_12 §0.2`. **The mechanism table is in GI; the perioperative application is here** — that split is defensible. Flag only |
| A-7 | `## 0.7 Assessment and Basic Management of Pain` +`.1 assessment` +`.2 management` | 248–300 | **flag** | with `AN1 §0.6 Postoperative Analgesia` (520), `NEW_Drugs_03 §0.4 Drugs for Pain Relief` (942), `Heme 10_11c ## Conversion between opioids` (H-21). **Opioid conversion is in two files** |
| A-8 | `## 0.1 Drugs for Gout` +`.1 xanthine oxidase inhibitors` +`.2 other` (NEW_Drugs_03) | 820–862 | **MSK** | gout is `MSK 12_02 §0.2`; **nothing to do with analgesia or anaesthesia** beyond the AMH chapter it came from |
| A-9 | `## 0.2 Drugs for Migraine` +`.1 triptans` +`.2 ergots` +`.3 CGRP` +`.4 prevention` | 863–923 | **Neuro** | migraine is `Neuro ## Migraine` and `D1 §0.3` |
| A-10 | `## 0.3 Drugs for Opioid Dependence` | 924 | **Psychiatry** | `Psychiatry 14a-1 ## Opioid misuse` +`### acute` +`### long-term` (998–1020) |

## KEEP + IN-TEXT FLAG
- **Inbound flags landing here, from other files' passes:**
  `Endocrine E-11` (`### 0.15.7 Perioperative Diabetes Management`, verified against the **ADS-ANZCA**
  guideline) · `Endocrine E-12` (`## 0.23 Principles of Fluid and Electrolyte Management in Surgical
  Patients`) · `Renal RU-16` (`### 0.14.1 TURP Syndrome`).
  **`AN1 §0.3 Perioperative Medication Management` (429) and `§0.7 Specific Perioperative
  Situations` (557) are where all three would land** — check for duplication first.
- `## 0.8 Postoperative Care and Complications` +`.1 by timing` (301–342) and
  `AN1 §0.5 Postoperative Complications` (482) are the same topic twice.
  **Cross-file: `Emergency A1 §0.5 Post-Procedural Deterioration`, `§0.6 Failure to Wake
  Post-Sedation`, and `ID K1 §0.6 Post-Operative and Drug Fever`.**
- `NEW_Drugs_03_Analgesics` is **an AMH chapter, not a clinical grouping** — it contains gout,
  migraine and opioid dependence alongside analgesics because AMH section 3 does. **A-8/A-9/A-10
  are all the same observation.**

## GROUPINGS
**HIGH**
- **G-A1 Preoperative assessment** — `03a §0.1.1 Pre-op checks` (12) · `§0.1.3 Pre-op instructions`
  (38) · `§0.5 Pre-Operative Assessment` (197) · `AN1 §0.1` (344) · `§0.2 Airway Assessment` (388) ·
  `§0.4 Fasting, Fluids and Enhanced Recovery` (457). (+ `Examination.md §1.12`)
- **G-A2 General anaesthesia** — `03a §0.1` +`.2 induction` +`.4 maintenance` +`.5 reversal`
  (8–63) · `NEW_Drugs_02 §0.2` +`.1`–`.4` (659–711) · `§0.3 Neuromuscular Blockers` +`.1`–`.3`
  (712–749) · `§0.4` +`.1`+`.2` (750–776)
- **G-A3 Local and regional anaesthesia** — `03a §0.3` +`.1`–`.5` (114–171) ·
  `NEW_Drugs_02 §0.1` +`.1`–`.5` (598–658)
- **G-A4 Postoperative complications** — `03a §0.8` +`.1` (301–342) · `AN1 §0.5` (482)
- **G-A5 Perioperative analgesia** — `03a §0.7` +`.1`+`.2` (248–300) · `AN1 §0.6` (520) ·
  `NEW_Drugs_03 §0.4` +`.1`–`.6` (942–1038)
- **G-A6 PONV** — `03a §0.4` (172). Cross-file with GI C2 §0.5 — see A-6

**MEDIUM**
- **G-A7 Perioperative medication and special situations** — `AN1 §0.3` (429) · `§0.7` (557).
  The landing zone for E-11, E-12, RU-16

**UNGROUPED — stays put**: `03a §0.6 Group & Hold` (232, pending A-5) · administrative blocks

## LIMITATIONS
- `AN1_Perioperative_Care` has **zero internal inbound references** — nothing in anaesthetics points
  at it. Per the trust-map caveat that is weak evidence alone, but it coincides with `03a`
  duplicating all seven of its sections.
