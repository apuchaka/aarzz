# Consolidated report — corpus reorganisation

**Navigable version:** https://claude.ai/code/artifact/47915732-d749-41d4-beee-6c21b2ee4e26
**Per-file detail:** `_meta/flags/<file>.md` — 20 files, 2,333 lines.
**Status: NOTHING MOVED.** Only two content commits exist, both pointer repairs.

| | |
|---|---:|
| outputs written | 20 |
| moves and flags | 280 |
| groupings | 291 (214 high · 77 medium) |
| approved by user, **not yet executed** | 11 |
| cross-references repaired | 23 |
| structural findings | 4 |

## THE FOUR STRUCTURAL FINDINGS — settle these before section-level moves
1. **`Neuro_merged.md:3829–5452` holds `N1`–`N8`, the entire Corpus B psychiatry set** — 1,624 lines,
   28% of the file. `Psychiatry_merged.md` has none of it. 8-for-8 mapping onto Psychiatry's Corpus A
   files. `N8_Eating_Disorders`: 17 inbound, **2 from Neuro**.
2. **`GER4_Safeguarding_and_Forensic` (37 inbound, 14 from Paediatrics, 1 internal) and
   `GER3_Preventive_and_Occupational_Health` (31 inbound) are not geriatrics** — filed under
   Geriatrics because of the `GER` prefix.
3. **Investigation interpretation has no home.** 60+ sections across 12 files; 9 duplicate a section
   `Investigation-Interpretation.md` already has. **ECG interpretation is absent from the entire
   Clinical Process set** — its only two section-level homes in the vault are inside `Cardio_merged`.
4. **Safeguarding is a four-way split whose pieces do not overlap**, and the largest piece is in
   Geriatrics.

## DESTINATIONS RANKED BY WHAT THEY GAIN
| Destination | Gains | Note |
|---|---:|---|
| `Investigation-Interpretation.md` (+`GER7`) | **60+ sections, 12 files** | grows several-fold |
| `Examination.md` (+`NEW_Exam_Manoeuvres` Part 1) | 22 named + ~60 blocks | |
| `History-Taking.md` | 20 named + ~60 blocks | sexual history from **three** files |
| `Psychiatry_merged.md` | **8 whole sources** + 4 | the single largest move |
| `Emergency and Crit Care` | 11 | 3 already approved |
| `Pediatrics_merged.md` | 9 | **all duplications, no gaps** |
| **New: Procedures** | 5 sources | `GER8`'s real parent |
| **New: Safeguarding** | 4 sources | |
| **New: Preventive health** | 6 sources | also settles the 4th Austroads home |
| **New: Palliative care** | 2 sources, 31 inbound | none from haematology |
| GI · OBGYN · Heme · Opthalm · ENT · Neuro · MSK · Derm · Endocrine · ID · Renal · Resp · Cardio | 37 total | see the artifact or per-file flags |

## CONFLICTS WITH ALREADY-APPROVED DECISIONS — need a ruling
- **`M-1` CSF Studies → Neuro.** Neuro already has `### CSF Interpretation`;
  `Investigation-Interpretation §1.13` also exists; ENT has CSF rhinorrhoea with β-transferrin.
  Moving it makes CSF **four-way**. **Recommend redirecting to Investigation-Interpretation.**
- **`M-2` Coombs/DAT → Heme Onc.** The fuller entry it points at should itself go to
  Investigation-Interpretation. **Recommend both land there.**
- **`M-6` Abdominal trauma → Emergency.** **MSK already holds two copies**; Neuro holds head injury;
  Emergency holds `F0-5 §0.7/§0.8`. **Recommend deciding trauma as one question across four files.**

## TWO-WAY DISAGREEMENTS — each file points at the other
urticaria/angioedema (Derm ↔ ID) · carcinoid (GI / Derm / Endocrine) ·
genetic cancer predisposition (Heme ↔ GP)

## COUNTING NOTE
The brief says 20 system files. There are **19** merged system files plus 16 Clinical Process files.
After GI there were **18** remaining, not 19.

## LIMITATIONS THAT TRAVEL WITH THIS REPORT
- HIGH confidence = "same topic", **not** "one is a subset of the other". No claim-level testing;
  **no discard verdicts implied** (CLAUDE.md rule 12 not applied).
- **Absence of inbound references is weak evidence** — only 0.9% of numeric pointers can be validated.
- **Rule 5 territory:** anaphylaxis, paediatric life support, paediatric DKA carry weight-based
  figures. No merge without checking every per-kg figure and injector band survives.
- **Psychiatry's section groupings were deliberately not produced** — half its corpus is in Neuro.
- Clean against everything currently known to check for — not complete.
