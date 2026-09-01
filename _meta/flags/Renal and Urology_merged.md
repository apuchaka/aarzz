# Renal and Urology_merged.md — grouping and misplacement flags

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
Sources: 7 · lines 2103 · `07_Renal_Medicine_and_Urology` 36 inbound (Investigation-Interpretation ×10,
History-Taking ×4, MSK ×4). Numbering drift: **none**.

## LEAD: four self-declared misfiles, all in `NEW_Investigations_Renal_and_Urology`
The file states them itself at L1776 and again in its build status at L2014.
| ID | Section | L | → | Evidence |
|---|---|---|---|---|
| RU-1 | `## 0.9 Adrenal / Cortisol Testing` | 1921 | **Endocrine** | *"Mis-filed — an endocrine investigation listed under Renal & Urology"* |
| RU-2 | `## 0.10 Metanephrines` | 1940 | **Endocrine** | same wording. Endocrine already owns phaeochromocytoma (`[[B2]] 0.4` is cross-referenced from there ×6) |
| RU-3 | `## 0.13 Fecal Incontinence` | 1996 | **GI** | *"Mis-filed and mis-categorised — a symptom, not an investigation"*, carrying a live `UNRESOLVED — needs review`. **Destination confirmed from the other end:** `GI 03_Gastrointestinal §0.42 Faecal Incontinence (Adult)` says it was *"found under Renal & Urology in the source spreadsheet, but genuinely a GI/colorectal topic"*. **Two files independently agree.** |
| RU-4 | `## 0.4 Dark Urine` | 1840 | **Investigation-Interpretation** *or* a presentations home | *"A sign, not a test"*. Note `Renal:1848` is the pointer that cites `NEW_Investigations_Gastroenterology.md 0.31` (Pale Stools) — **the sign/test axis error is symmetrical across two files** |

## PROPOSED MOVES

### Investigation interpretation (standing rule, as extended)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| RU-5 | `## 0.1 Urinalysis Panel (Dipstick, pH, SG, Microscopy, Culture)` | 1780 | **Investigation-Interpretation.md §1.14** | **§1.14 "Urinalysis and Urine Microscopy, Culture & Sensitivity" already exists there.** Duplicate, not a gap **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`), then FOLDED INTO `Procedures.md` under C2/AXIS-2 (`98ceb40`) — a procedure, as this row said** |
| RU-6 | `## 0.3 Renal Function Panel (Urea, Creatinine, eGFR, Electrolytes)` | 1819 | **Investigation-Interpretation.md** | no equivalent there **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| RU-7 | `## 0.2 Urine ACR` | 1801 | **Investigation-Interpretation.md** | carries a deliberate refusal to convert mg/g→mg/mmol — **keep that note with it** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |
| RU-8 | `## 0.5 Elevated PSA` | 1858 | **Investigation-Interpretation.md** | *"prostate-specific, not prostate-cancer-specific, which is the entire interpretive problem"* — pure interpretation **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |
| RU-9 | `## 0.6 Urine Cytology` · `## 0.7 Uroflowmetry` · `## 0.8 Urodynamic Studies` | 1877, 1891, 1905 | **Investigation-Interpretation.md** | how to read the trace **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| RU-10 | `## 0.11 24-hour Urine Copper` | 1958 | **Investigation-Interpretation.md**; content serves `GI §0.7 Wilson's Disease` | flag the GI link **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| RU-11 | `## 0.12 Urine Protein Electrophoresis / Bence-Jones` | 1977 | **Investigation-Interpretation.md**; serves `Renal §0.8 Myeloma Kidney` and Heme Onc | 1 inbound (GP) **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (`ac620de`)** |

> RU-5 – RU-11 empty `NEW_Investigations_Renal_and_Urology` of everything except the four
> self-declared misfiles. Same shape as `NEW_Investigations_Respiratory`.

### Procedures
| ID | Section | L | → | Note |
|---|---|---|---|---|
| RU-12 | `## 0.5 Catheters` (H2) | 1122 | **`NEW_Exam_Manoeuvres_and_Procedures` / `GER8_Procedure_Addendum`** | *"The indications are narrow, and 'incontinence' is not one of them"* — procedure indications and technique. Axis question, flag |
| RU-13 | `## 0.6 Renal Biopsy` (H1) | 970 | **`GER8_Procedure_Addendum`** *or* Investigation-Interpretation | indications/complications of a procedure **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |

### History / examination (standing rule)
| ID | Section | L | → |
|---|---|---|---|
| RU-14 | 2 × `**Focused Hx:**` + 2 × `**Examination:**` in `NEW_Renal_and_Urology` | 2043–2072 | **History-Taking.md / Examination.md**. L2044 is explicit technique: *"examine the patient standing and lying, with consent and a chaperone"*; L2072 *"palpate and percuss for a distended bladder"* **✅ RESOLVED 2026-09-01 — Option 1: left in place, indexed in `Examination.md` §3 and `History-Taking.md` §2 (`bcf7515`/`fab04f5`)** |

### Cross-file
| ID | Section | L | → | Note |
|---|---|---|---|---|
| RU-15 | `## 0.5 Groin Lumps and Hernias` (H4) | 1545 | **arguable — GI** | GI owns `§0.21 Hernias` + `§0.21.1 Types`. H4's version is a groin-lump differential with the pubic-tubercle landmark. **Decide alongside GI G27** |
| RU-16 | `### 0.14.1 TURP Syndrome` | 500 | **arguable — Anaes** | glycine absorption → dilutional hyponatraemia; a perioperative complication. Decide with the Anaes pass |
| RU-17 | `### 0.2.3 CKD-Related Anaemia` | 107 | **keep, flag** | Heme Onc owns anaemia; this is the renal cause. Boundary is defensible — flag only |

## KEEP + IN-TEXT FLAG
- **`NEW_Drugs_13 §0.7 Drugs for Adrenal Insufficiency`** (1728) **self-declares a duplicate**:
  *"This subsection duplicates content built in AMH section 10 … written in full at
  `NEW_Drugs_10_Endocrine.md` 0.5.1 and 0.5.2."* Flag both.
- `NEW_Renal_and_Urology` has **zero inbound references** and its only two clinical sections
  (`## Acute Scrotal Pain`, `## Acute Urinary Retention`) duplicate `H4 §0.1` and `H2 §0.3`.
- `H4 §0.4` opens *"Rule out an abdominal aortic aneurysm before diagnosing first-episode renal
  colic over 50"* — the same must-not-miss as `GI C1 §0.1` and `Cardio §0.36.4`. Consistent, not a
  duplicate. No action; recorded so it is not mistaken for one later.

## GROUPINGS
**HIGH** — Corpus A and the H-files duplicate each other almost topic-for-topic.
- **G-U1 AKI** — `07_Renal §0.1` +`.1 RRT indications (AEIOU)` (6, 40) · `H3 §0.1 Definition and
  Approach` (1194) · `H3 §0.2 The Causes` (1214) · `H3 §0.3 Management and Dialysis Indications` (1260)
- **G-U2 CKD** — `07_Renal §0.2` +`.1 staging` +`.2 mineral bone disease` +`.3 anaemia`
  +`.4 RRT modalities` +`.5 rejection` +`.6 transplant complications` (49–163) · `H3 §0.4` (1293).
  **A stages by GFR alone; H3 stages on TWO axes (eGFR and albuminuria)** — H3 is the current framing.
- **G-U3 Glomerular disease** — `07_Renal §0.4 Nephritic vs Nephrotic` (189) · `§0.6 Lupus Nephritis`
  (224) · `§0.7 ANCA-Associated GN` (244) · `H1 §0.2 The Glomerular Syndromes` (847) ·
  `H1 §0.3 Nephritic Syndrome and GN` (871) · `H1 §0.4 Nephrotic Syndrome` (905)
- **G-U4 Haematuria / proteinuria** — `H1 §0.1 Haematuria` (799) · `H1 §0.5 Proteinuria` (940) ·
  `NEW_Inv_Renal §0.1 Urinalysis` (1780) · `§0.2 ACR` (1801)
- **G-U5 BPH and LUTS** — `07_Renal §0.14 BPH` (473) · `H2 §0.1 LUTS` (1003) · `H2 §0.2 BPH` (1032) ·
  `NEW_Drugs_13 §0.1` +`.1`–`.3` (1613–1646)
- **G-U6 Urinary retention** — `07_Renal §0.12` (418) · `H2 §0.3 Acute` (1070) ·
  `H2 §0.4 Chronic and Obstructive Uropathy` (1098) · `NEW_Renal ## Acute Urinary Retention` (2062).
  **Four copies.**
- **G-U7 Incontinence** — `07_Renal §0.13` (445) · `H2 §0.6` (1152) · `NEW_Drugs_13 §0.2` +`.1`+`.2`
  (1647–1670) · (+ `NEW_Inv_Renal §0.13 Fecal Incontinence`, which is the **GI** topic — see RU-3)
- **G-U8 Acute scrotum / torsion** — `07_Renal §0.20 Testicular Torsion` (722) · `H4 §0.1 The Acute
  Scrotum` (1409) · `NEW_Renal ## Acute Scrotal Pain` (2032). **Three copies.**
- **G-U9 Scrotal and testicular lumps** — `07_Renal §0.21 Testicular Cancer` (745) ·
  `§0.22 Testicular Lumps` (772) · `H4 §0.2 Scrotal Lumps` (1449)
- **G-U10 Urolithiasis** — `07_Renal §0.15` (514) · `H4 §0.4 Renal Colic and Urolithiasis` (1504) ·
  `NEW_Drugs_13 §0.4 Drugs for Kidney Stones` (1692) · `§0.5 Urinary Alkalinisers` (1706)
- **G-U11 UTI** — `07_Renal §0.11` +`.1 cystitis` +`.2 pyelonephritis` +`.3 chronic pyelonephritis`
  +`.4 prostatitis` +`.5 epididymitis` +`.6 balanoposthitis` (312–417)
- **G-U12 Penile and foreskin** — `07_Renal §0.11.6 Balanoposthitis` (393) ·
  `§0.18.1 Circumcision` (663) · `§0.18.3 Priapism` (681) · `H4 §0.3 Penile and Foreskin` (1479)
- **G-U13 Urological trauma** — `07_Renal §0.19 Urethral and Bladder Trauma` (698) ·
  `H4 §0.6 Urological Trauma` (1573)
- **G-U14 Erectile dysfunction** — `07_Renal §0.16` (557) · `NEW_Drugs_13 §0.3` +`.1`+`.2` (1671–1691)
- **G-U15 Urological cancers** — `07_Renal §0.17` +`.1 RCC` +`.2 bladder` +`.3 prostate` (587–660) ·
  `NEW_Inv_Renal §0.5 PSA` (1858) · `§0.6 Urine Cytology` (1877) · `NEW_Drugs_13 §0.6 Bladder
  Instillations` (1715)

**MEDIUM**
- **G-U16 Intrinsic renal / tubulointerstitial** — `§0.9 Acute Interstitial Nephritis` (276) ·
  `§0.10 ATN` (292) · `H3 §0.5 Drug and Contrast Nephropathy` (1348). H3 §0.5's *"the risk of
  contrast nephropathy has been substantially over-estimated"* is a **correction** to older teaching
  — do not let a merge lose it.
- **G-U17 Water handling** — `H3 §0.6 Polyuria, Oliguria and Water Handling` (1372). No A partner;
  check against Endocrine (diabetes insipidus).
- **G-U18 Renal disease in systemic illness** — `§0.5 Diabetic Nephropathy` (205) ·
  `§0.8 Myeloma Kidney` (261) · `§0.6 Lupus Nephritis` (224). Siblings, not one topic.

**UNGROUPED — stays put**: `§0.3 Polycystic Kidney Disease` (164) · `§0.18.2 Vasectomy` (671) ·
`### 0.14.1 TURP Syndrome` (500, pending RU-16) · 4 administrative blocks

## LIMITATIONS
- RU-15 (groin hernias) and RU-16 (TURP syndrome) deliberately undecided — both need inbound
  evidence from GI and Anaes respectively.
- `NEW_Inv_Renal §0.13`'s own `UNRESOLVED` marker asks whether the build list meant **anorectal
  manometry** rather than the symptom. That question is **not resolved here** and must not be
  silently answered by moving the section.
