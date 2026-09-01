# The 16 Clinical Process files — FILE-COMBINATION output

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
Per the brief: these are **not** grouped by topic and their content is **not** flagged for system
files. This output answers *which files should combine*, plus the reverse flags collected from all
19 system passes.

## FIRST — two corrections to the starting hypothesis
Both come from the files' own scope declarations, which I read before grouping.

**1. `EBM1` has no research-literacy half to merge into `PH1`.** Its scope note says so explicitly:
> *"**SCOPE NOTE:** study design, bias, confounding, diagnostic test statistics, measures of effect
> and screening are built in **[[PH1]]** and are NOT repeated here. This file covers **applying**…"*

**The duplicate is `Clinical-Process-EBM-Consent-Capacity`, not `EBM1`.** Its second half —
`## Diagnostic Test Characteristics` (168) · `## Interpreting Treatment Effects` (202) ·
`## Study Design and Bias` (230) · `## Statistical Significance` (268) · `## Screening` (290) —
**duplicates `PH1 §0.1`–`§0.5` almost section for section**, while `EBM1` deliberately does not.
So: **`PH1` + the second half of `Clinical-Process-EBM`**, and `EBM1` stays separate.

**2. `GER8`'s parent is not `Examination.md`.** Its scope line names procedures —
*"gastroscopy · oesophagoscopy · gastrografin…"* — which is `NEW_Exam_Manoeuvres_and_Procedures`
**Part 2**, not the examination file.

## THE GER ADDENDA — parents confirmed from each file's own scope line
| File | Its own words | Parent |
|---|---|---|
| `GER7_Investigation_and_Lab_Addendum` | *"a **CROSSWALK ADDENDUM** covering the investigations … that did not fit a clinical cluster"* | **`Investigation-Interpretation.md`** ✅ as hypothesised |
| `GER8_Procedure_Addendum` | *"a **CROSSWALK ADDENDUM** covering the procedures …"* | **`NEW_Exam_Manoeuvres_and_Procedures` Part 2** — *not* `Examination.md` |
| `GER6_Drug_Class_Addendum` | *"a **CROSSWALK ADDENDUM** … drug classes … that did not fit any clinical cluster"* | **the `NEW_Drugs_NN` set** — and **it was not in the brief's candidate list** |
| `GER5_Communication_and_Consultation_Skills` | **not an addendum** — a full file that defers outward: *"Open disclosure and handover are built in [[EBM1]] 0.5–0.6, cultural safety in [[AU1]] 0.3, goals of care in [[GER2]] 0.6"* | **`Communication.md`** ✅ as hypothesised |
**All three addenda are residual crosswalks — content that fitted nowhere else.** That is why each
is thin and each has a different parent. **Do not treat them as one class.**

## RECOMMENDED COMBINATIONS

### C1 · Communication — **MERGE** `Communication.md` + `GER5`
Confirmed. Direct duplicates: `Communication §1.2 Breaking Bad News` ↔ `GER5 §0.2 Breaking Bad
News`; `§1.8 Angry Patients and Complaints` ↔ `GER5 §0.3 Difficult Conversations`.
`GER5` adds what `Communication` lacks — `§0.1 The Consultation — Structure and Core Skills`,
`§0.4 Interpreters and Communicating Across Difference`, `§0.5 Shared Decision-Making and Health
Literacy`, `§0.6 Telehealth, Phone and Written Communication`.
**`GER5` is written in actual forms of words** — its own note says *"the difference is whether you
can say the sentence"*. **Preserve that; it is the OSCE-usable half.**
⚠️ **Open disclosure and handover must be resolved at the same time — they are three-way:**
`Communication §1.13 Open Disclosure` + `EBM1 §0.6 Error, Incident Reporting and Open Disclosure`;
`Communication §1.7 Clinical Handover (ISBAR)` + `EBM1 §0.5 Handover and Transitions of Care`.
**`GER5` defers to `EBM1` for both — so `EBM1` is the declared owner and `Communication` is the
duplicate.**

### C2 · Examination and Procedures — **SPLIT, then merge along the axis**
**Do not merge all three.** They are two different things:
- **Examination** → `Examination.md` §1.1–§1.7, §1.9–§1.10, §1.12–§1.27 · `NEW_Exam_Manoeuvres`
  **Part 1** (15 sections, **every one an MSK test** — Lachman, drawer, pivot shift, Thompson,
  Finkelstein, grind, FABER, Trendelenburg, Adam's, SLR, femoral stretch, Schober, Spurling,
  distraction).
- **Procedures** → a **separate file**: `Examination.md §1.8 Pleural Aspiration` and
  `§1.11 Abdominal Paracentesis` (procedures currently inside the examination file) ·
  `NEW_Exam_Manoeuvres` **Part 2** (cardioversion, ICD, carotid endarterectomy, external fixation) ·
  **all six of `GER8`** · `Emergency F0-4 §0.7 Mechanical Ventilation`, `§0.8 Procedural Sedation`,
  `§0.11 Fascia Iliaca Block` (X-4) · `Anaes 03a §0.2 Airway Adjuncts`, `§0.3 Regional Anaesthesia`
  (A-3, A-4).
⚠️ **`GER8 §0.3 Gastrografin and Contrast Studies` duplicates `GI NEW_Inv_Gastro §0.36 Gastrografin`
(M-18)** — which you have already flagged for a heading rewrite. **Same content, two files.**
⚠️ **`GER8 §0.5 Arthrocentesis` duplicates `MSK L1 §0.6 Joint Aspiration and Synovial Fluid
Interpretation` (K-13) and `Investigation-Interpretation §1.15 Joint Aspirate`. Three files.**

### C3 · Investigation interpretation — **MERGE** `Investigation-Interpretation.md` + `GER7`
Confirmed, **and this is now the largest destination in the whole project.**
`GER7` adds `§0.1 Interpreting Any Investigation` (a general method the parent lacks),
`§0.2 Haematinics and Red Cell Folate`, `§0.3 Rheumatoid Factor and Lupus Serology`,
`§0.6 Pre-Analytical Error`.
⚠️ **Two `GER7` sections belong elsewhere:**
`§0.4 Troponins and Cardiac Biomarkers` is the **fourth** troponin home (Cardio ×2, Inv-Interp §1.12);
`§0.5 Fetal Scalp Blood Sampling and Intrapartum Assessment` is obstetric — **and is where approved
Cardio C-1 (CTG/NST) and OBGYN B-9 (biophysical profile) should land.**

> **The scale of what the system passes send here — 60+ sections across 12 files:**
> ECG interpretation and its 12 subsections (Cardio C-2/C-3, **absent from the whole Clinical
> Process set**) · 8 respiratory investigations (R-1–R-9) · 7 renal (RU-5–RU-11) · 6 endocrine
> (E-1–E-6) · 25 haematology (H-2–H-9) · 23 infectious disease (I-2–I-9) · 12 obstetric (B-5–B-9) ·
> 16 general (GP P-1–P-6) · 12 from the MSK grab-bag (K-1–K-12) · joint aspirate, autoantibodies,
> fracture description, growth charts, paediatric bloods.
> **Nine of these duplicate a section `Investigation-Interpretation.md` already has**
> (§1.5 ABG ×3, §1.7 fracture description, §1.11 FBC ×2, §1.14 urinalysis, §1.15 joint aspirate ×2,
> §1.16 autoimmune markers ×4, §1.17 coagulation ×2, §1.19 growth charts, §1.21 CRP/ESR).
> **This file grows several-fold. It is the single biggest consequence of the extended standing rule.**

### C4 · Ethics, consent and capacity — **MERGE THREE, but only the consent half of one**
`A10` + **the first half of** `Clinical-Process-EBM` (`## General principles of informed consent`
through `## Notifiable conduct`, L10–126) + the consent/goals-of-care sections of `Communication`.
Consent and capacity is currently in **three** Clinical Process files:
| File | Sections |
|---|---|
| `A10` | `§0.1 Capacity Assessment` · `§0.2 Consent and Treatment Refusal` · `§0.3 Substitute Decision-Making and ACDs` |
| `Clinical-Process-EBM` | `## General principles of informed consent` · `## Capacity assessment — the general framework` · `## Consent to Medical Treatment and Palliative Care Act 1995 (SA)` · `## Right to refuse treatment` · `## Consent and children` |
| `Communication` | `§1.1 Consent for Blood Transfusion` · `§1.3 DNACPR` · `§1.4 Goals of Care and Ceiling of Care` |
**Plus inbound:** `Psychiatry Y-4` (guardianship) · `Psychiatry Y-5` (Mental Health Act) ·
`Paediatrics P-3` (mature minor) · `Geriatrics GER2 §0.6 Advance Care Planning`.
⚠️ **Mandatory reporting is a separate three-way**: `Clinical-Process-EBM ## Mandatory Reporting`
+ `## Notifiable conduct` · `A10 §0.5 Professional Practice Concern` ·
`GER4 §0.1 The Safeguarding Mindset and Mandatory Reporting` (**now `Safeguarding.md`, `16a9386`**) ·
plus `ID I-11` (notifiable **diseases**, twice in one file — a different duty, easily conflated).

### C5 · Research literacy — **MERGE** `PH1` + the second half of `Clinical-Process-EBM`
Per correction 1. `EBM1` stays separate as the **application** file (critical appraisal in practice,
using guidelines, clinical reasoning and diagnostic error, documentation, handover, open disclosure).
⚠️ **`PH1 §0.6 Public Health Practice` and `§0.5 Screening` belong with the preventive-health
question below, not with research literacy.**

### C6 · Safeguarding — **A FOUR-WAY SPLIT, and the pieces do not overlap**
| File | Covers | Does **not** cover |
|---|---|---|
| `NEW_Safeguarding_and_Forensic` (standalone, 81 lines) | neglect · emotional abuse · fabricated illness · safe sleep — **all paediatric** | elder abuse · family violence · sexual assault |
| `GER4` — **now `Safeguarding.md` (`16a9386`)** (**37 inbound, 14 from Paediatrics, 1 internal**) | safeguarding mindset · child abuse recognition · responding to a concern · family violence · sexual assault · elder abuse | the four topics above |
| `Pediatrics 15_24a` (14 inbound) | non-accidental injury · sexual abuse | |
| `Communication §1.9` | explaining a safeguarding referral to a family | |
**The brief lists `NEW_Safeguarding_and_Forensic` as standalone. It is not — it is one quarter of a
topic**, and the largest quarter (`GER4`) **was** filed under Geriatrics **and is now `Safeguarding.md` (`16a9386`)**. **Recommend one safeguarding
file**, built from all four, with `Communication §1.9` staying as the conversation.

### C7 · Preventive health — **SIX SOURCES, FOUR FILES, no owner**
`GER3 §0.1`–`§0.5` — **now `Preventive-Health.md` (`16a9386`)** (31 inbound) · `GP 19_ §0.1`–`§0.2` · `GP NEW_Inv_General §0.12`,`§0.13` ·
`PH1 §0.5 Screening`, `§0.6 Public Health Practice` · `ID 08_01-03 ## Vaccination Schedule` +
`## Passive Immunisation` (I-10) · `NEW_Drugs_20 Vaccines` · `Pediatrics 15_24b`.
**Recommend one preventive-health file.** `GER3` is the largest and best-referenced candidate.
⚠️ **`GER3 §0.6 Occupational Health, Certification and Driving` is the FOURTH Austroads home**
(Cardio §0.35.5 · Endocrine §0.15.8 · Neuro `### Austroads Driving Standards (Neurological)`),
and `Clinical-Process-EBM:102` has a *"Fitness to drive"* row pointing at two of them.
**One Austroads home, wherever preventive health lands.**

### C8 · `NEW_Drugs_21_Miscellaneous` — **belongs with the drug files, and that is the point**
42 lines, one content section (AMH section 21: enzyme replacement, rare metabolic disease, contrast
agents, dantrolene, sugammadex, glucarpidase). **20 of the 21 `NEW_Drugs_NN` files are already
inside system files; this is the only one left standalone** — because its content is
system-agnostic by construction.
**Recommend: keep it with whatever home the drug-class axis gets** (see the axis question below).
Its nearest clinical relatives are `Pediatrics 15_17a/15_17b` (inherited metabolic disease) and
`Endocrine E-8`. Its `> [!danger]` block — *"NEVER OMIT, INTERRUPT OR SUBSTITUTE A SPECIALISED DRUG
WITHOUT CONTACTING THE TREATING CENTRE"* — is genuinely cross-cutting intern advice and should
survive wherever it goes.

### C9 · `AU1_Australian_Health_Context_and_ATSI_Health` — **STANDALONE, confirmed**
The brief's guess holds. But its `§0.4 Conditions With Disproportionate Burden` is a **hub for
equity blocks scattered through the system files**: `Resp §0.4 Lung Cancers` · `Neuro ## Strokes` ·
`Heme 10_11a ## Cancer Outcomes in ATSI Australians` (H-18) · `Cardio §0.23 RHD`.
**These are a deliberate pattern, not duplicates. Flag them as a set; do not consolidate** — the
point of each is that it sits in the disease entry where a reader meets the disease.

### C10 · `History-Taking.md` — **STANDALONE, and the destination of the most reverse flags**
Not in the brief's candidate list, and it should stay separate. **But note it already contains
`§1.25 Adolescent Psychosocial Assessment (HEADSS/HEEADSSS)` — which is where `Paediatrics P-1`
(`M7 §0.2 The HEEADSSS Psychosocial Assessment`) lands. The destination already exists.**

## REVERSE FLAGS — the standing rule's harvest across all 19 system files
| Destination | What arrives | Count |
|---|---|---|
| **`History-Taking.md`** | `**Focused Hx:**` blocks from every `NEW_*` presentation source (Cardio 14, Neuro 8, MSK 8, Derm 6, OBGYN 6, ID, Resp 3, Renal 2, Opthalm 4, ENT 4, Endocrine, Psychiatry, Paeds) · **the sexual history, from three files** (ID I-1, OBGYN B-1, MSK K-10) · HEEADSSS (P-1) · occupational history (R-10, R-11) · collateral history in syncope (C-8) · falls history (R-3, R-4) | **~60 blocks** |
| **`Examination.md`** | matching `**Examination:**` blocks · GI M-7 (approved) · abdominal exam signs · murmur dynamic manoeuvres (C-4) · heart sounds and pulses (C-5) · Valsalva ×2 (C-6) · fundoscopy (C-7) · MSE (N-4) · HINTS (N-5) · lesion localisation (N-6, N-7) · GCS (N-3) · dermatomes and myotomes (K-16) · Tinel/Phalen (K-18) · rash description (D-12, D-13, D-14) · nails (D-16) · triple assessment (B-2) · ear examination (T-1) · A–E (X-1, X-2) · pre-anaesthetic assessment (A-1, A-2) · paediatric approach (P-4) | **~60 blocks** |
| **`Investigation-Interpretation.md` (+`GER7`)** | see C3 | **60+ sections** |
| **`Communication.md` (+`GER5`)** | adolescent consultation (P-2) · the 5As (P-9) · discharge communication (R-5) · pre-pregnancy counselling (B-3, arguable) | ~5 |
| **`A10` / consent file** | mature minor (P-3) · guardianship (Y-4) · Mental Health Act (Y-5) | 3 |
| **safeguarding file** | Paediatrics NAI (P-5) · FGM (B-13) | 2 |
| **preventive health file** | vaccination schedule (I-10) · ATSI cancer outcomes (H-18, arguable) | 2 |

## THE UNRESOLVED AXIS QUESTION (deferred from GI G17/G28, now answerable in principle)
**Two axes cut across every system file and neither has a home:**
- **Drug classes** — 21 `NEW_Drugs_NN` files, 20 inside system files, 1 standalone, **plus `GER6`
  as their crosswalk addendum**, plus per-system drug sections (`Cardio §0.35`, `Psychiatry 14_06a`,
  `Neuro ## Anticonvulsants`, `Renal`…). ⚠️ **`NEW_Drugs_07` is byte-identical in two system files.**
- **Procedures** — see C2.
**My reading:** the drug axis is already coherent *as a set* (`NEW_Drugs_01`–`21` + `GER6`) and is
only incoherent in *where it is stored*. The procedure axis is genuinely fragmented across five
files and needs building. **Both are your decisions; I have not made either.**

## LIMITATIONS
- `Clinical-Process-EBM-Consent-Capacity` is **two unrelated files in one** (consent/reporting, then
  research literacy). C4 and C5 both cut it. **Splitting it is a prerequisite for both.**
- `GER6_Drug_Class_Addendum` was absent from the brief's candidate list; I have proposed a parent
  from its own scope line, but that is inference from one sentence and should be checked.
- I have **not** proposed merging `History-Taking.md` with anything, and **not** treated
  `Examination.md` and `NEW_Exam_Manoeuvres` as a single merge. Both are deliberate departures from
  the starting hypothesis, argued above.
