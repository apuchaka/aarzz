# Neuro_merged.md — grouping and misplacement flags

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
Sources: 18 · lines 5867 (largest file) · `04_Neurology` **143 inbound — the most-referenced source
in the vault** (Examination ×21, Opthalm ×16, Investigation-Interpretation ×15, Paediatrics ×13).
Numbering drift: **none**.

## THE HEADLINE: eight whole psychiatry sources are filed under Neurology
`Neuro_merged.md` lines **3829–5452** contain **N1–N8 in full — 1,624 lines, 28% of the file**.
`Psychiatry_merged.md` contains the Corpus A psychiatry files and **none of N1–N8**.
**The two halves of psychiatry are in different merged documents.** Every grouping the brief asks
for in Psychiatry is currently split across two files.

| Corpus B source, currently in **Neuro** | L | Corpus A partner, in **Psychiatry** |
|---|---|---|
| `N1_Mental_State_Examination_and_Risk` | 3829 | `14_06b Mental Health Act and Sectioning` (+ `Examination.md §1.22 MSE`) |
| `N2_Acute_Behavioural_Disturbance_and_Substance_Use` | 4067 | `14a-1 Substance Misuse` · `14a-2 Overdose and Poisoning` |
| `N3_Psychosis_and_Antipsychotics` | 4251 | `14_03 Psychotic Disorders and Antipsychotics` |
| `N4_Mood_Disorders` | 4472 | `14_01 Mood Disorders (Depression, Suicide, Bipolar)` |
| `N5_Anxiety__OCD_and_Trauma` | 4714 | `14_02 Anxiety and Related Disorders` |
| `N6_Functional__Dissociative_and_Personality_Disorders` | 4904 | `14_04 Personality Disorders` · `14_05c Unexplained Symptoms` |
| `N7_Sleep_Disorders` | 5080 | `14_05b Insomnia` |
| `N8_Eating_Disorders` | 5264 | `14_05a Eating Disorders` |

**Eight for eight.** Corroborating evidence from the reference index: **`N8_Eating_Disorders` has 17
inbound and only 2 are from Neuro** — GI ×5, Endocrine ×4, MSK ×2, OBGYN ×2, Paediatrics, Neuro ×2.
It is referenced from everywhere except neurology.

**Recommended as one move of eight whole sources, not 47 section moves.** Nothing else in this
report should be actioned before this one, because it changes what "the Psychiatry file" contains.

## PROPOSED MOVES — investigation interpretation & examination (standing rule)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| N-1 | `### CSF Interpretation` (table: normal/bacterial/viral/TB/fungal) | 707 | **Investigation-Interpretation.md §1.13** | **§1.13 "CSF Interpretation" already exists.** ⚠️ **And you approved GI M-1 (`## 0.32 CSF Studies`) → Neuro.** With this, CSF would have **three** homes. **Recommend redirecting M-1 to Investigation-Interpretation instead** — please confirm **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| N-2 | `### Who gets a CT head for head injury?` | 1452 | **Investigation-Interpretation.md §1.2** | §1.2 "CT Head — Systematic Approach" already exists. Carries a live note that AU pathways use the **Canadian CT Head Rule**, not NICE — **keep that caveat with it** **✅ EXECUTED 2026-09-01 → `Investigation-Interpretation.md` (ac620de)** |
| N-3 | `### Glasgow Coma Scale (GCS)` | 719 | **Examination.md** | a scoring scale applied at the bedside **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| N-4 | `## 0.1 Psychiatric Assessment and the Mental State Examination` (N1) | 3841 | **Examination.md §1.22** | opens *"The MSE is an EXAMINATION, not a history"* — the file argues the move itself. §1.22 MSE already exists **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| N-5 | `## 0.2 Acute Vestibular Syndrome and the HINTS Examination` (D5) | 3016 | **Examination.md §1.21.2** | §1.21.2 "HINTS exam" already exists there **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| N-6 | `## 0.1 Localising the Lesion` (D4) | 2700 | **Examination.md** | *"from cortex to muscle"* — the neurological examination's organising method **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| N-7 | `## Brain Lesion Localisation` | 952 | **Examination.md** | lobe-by-lobe sign lists **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| N-8 | 8 × `**Focused Hx:**` + 8 × `**Examination:**` in `NEW_Neurology` | 5695–5830 | **History-Taking.md / Examination.md** | L5786 *"test the forehead first and explicitly — ask the patient to raise their eyebrows"* is pure technique |

## PROPOSED MOVES — topic in the wrong system
| ID | Section | L | → | Why a reader would look there |
|---|---|---|---|---|
| N-9 | `## Syncope` + `### Cardiac syncope` + `### Non-cardiac syncope` | 879–919 | **Cardio** | `Cardio B4` is an entire syncope/collapse source (`§0.1 TLoC Framework`, `§0.2 Syncope`, `§0.3 Presyncope`). Syncope is taught cardiac-first |
| N-10 | `### Seizures vs Syncope` (comparison table) | 823 | **keep, flag** | the discriminator legitimately belongs to whoever owns both. Flag against N-9 |
| N-11 | `## 0.3 Diplopia and Disorders of Eye Movement` (D7) | 3646 | **Ophthalmology** | **D7 has 8 inbound and 6 are from Opthalm_merged** |
| N-12 | `### Horner's Syndrome` | 1001 | **Ophthalmology** | ptosis/miosis/anhidrosis; `Derm:2242` already routes *"Horner syndrome and carotid dissection → [[E3]] and [[D5]]"* |
| N-13 | `## 0.4 Speech, Voice and Swallowing` (D7) | 3704 | **ENT** | dysphonia and dysphagia; ENT owns `## Dysphonia (hoarseness)` and `## 0.4 Oropharyngeal Dysphagia` |
| N-14 | `## 0.5 Smell and Taste` (D7) | 3752 | **arguable — ENT** | ENT owns nose and sinus. Counter-argument in its own text: *"hyposmia is an early feature of neurodegenerative disease"* |
| N-15 | `### Vertigo (Peripheral vs Central, BPPV, Vestibular Neuritis)` | 1016 | **decide with ENT** | ENT owns BPPV, Ménière's, vestibular neuronitis, labyrinthitis as full entries. **D5 has 21 inbound, ENT ×6 — the largest external referrer** |
| N-16 | `## Serotonin Syndrome and NMS` | 356 | **Emergency** | Emergency owns `A6 §0.3 Hyperthermia versus Fever, and the Drug-Induced Hyperthermias` and the toxidrome framework |
| N-17 | `## Opioid Toxicity` | 376 | **Emergency** | Emergency owns `F0-1 §0.5 Opioid-Induced Respiratory Depression` |
| N-18 | `### Febrile Convulsions` | 794 | **Paediatrics** | Paediatrics owns `15_12a Epilepsy Syndromes and Status Epilepticus` |
| N-19 | `## Delirium vs Dementia vs Depression — the "3 Ds" in Older People` | 320 | **Geriatrics** | **self-declares** it was gap-filled from the *"Older Persons Health / Geriatrics category"* |
| N-20 | `### Cauda Equina Syndrome` · `### Malignant Spinal Cord Compression` | 1559, 1582 | **arguable — MSK/spinal** | MSK owns `11_06 Spinal Orthopaedics`; both present as back pain. **Counter: both are neurosurgical emergencies.** Decide with MSK |
| N-21 | `### Neurofibromatosis` · `### Tuberous Sclerosis` | 1691, 1709 | **arguable — Derm/genetics** | neurocutaneous; Paediatrics owns the microdeletion/genetic syndromes |
| N-22 | `### Subacute Combined Degeneration of the Spinal Cord` | 1614 | **flag only** | B₁₂ deficiency; Heme Onc owns pernicious anaemia. Neurological presentation justifies staying |
| N-23 | `### Austroads Driving Standards (Neurological Conditions)` | 1764 | **flag, do not move** | **third Austroads table** — with `Cardio §0.35.5` and `Endocrine §0.15.8`. `Clinical-Process-EBM:102` points at two. Decide at the Clinical Process pass |

## KEEP + IN-TEXT FLAG
- **Alcohol withdrawal is now in four places across three files**: `GI §0.6.1` (the AU-verified core,
  5 inbound) · `N2 §0.1 Alcohol Withdrawal and Delirium Tremens` (**moved to `Psychiatry_merged.md` by A1, `f5e49c9`; was Neuro:4077**) ·
  `04_Neurology ### Alcohol Withdrawal Seizures` (804) · `Psychiatry 14a-1`. **GI M-5 flagged this
  with three; it is four.** The N2 copy moves with the psychiatry block.
- `### Wernicke's Encephalopathy` (1799) also appears as `GI C2 §0.7 Complications of Vomiting`.
- `NEW_Neurology` has only 2 inbound (GI, Renal), both backticked.

## GROUPINGS (neurology proper — the psychiatry groupings belong with the Psychiatry pass)
**HIGH**
- **G-N1 Headache** — `04 ## Migraine` (6) · `## Tension Headache` (77) · `## Trigeminal Neuralgia`
  (33) · `## Trigeminal Autonomic Cephalalgias` + `### Cluster Headache` (53, 57) ·
  `## Medication Overuse Headache` (111) · `## Other Headache Causes` (125) ·
  `## Temporal Arteritis` (97) · `D1 §0.1 Framework and Red Flags` (1840) · `D1 §0.3 Primary Headache
  Disorders` (1934) · `D1 §0.4 Secondary Headaches` (1998)
- **G-N2 Thunderclap headache / SAH** — `04 ### Subarachnoid Haemorrhage` (1144) · `D1 §0.2` (1883)
- **G-N3 Meningitis and CNS infection** — `04 ### Bacterial Meningitis` (498) · `### Viral Meningitis`
  (529) · `### Encephalitis` (547) · `### Brain Abscess` (572) · `### Spinal Epidural Abscess` (596) ·
  `D1 §0.5 Meningism, Meningitis and Encephalitis` (2053) · `D1 §0.6 Neck Stiffness` (2110) ·
  `04 ### CSF Interpretation` (707)
- **G-N4 Stroke and TIA** — `04 ## Strokes` +`### TIA` +`### Ischaemic` +`### Haemorrhagic`
  +`### Arterial Territory Syndromes` +`### Bamford-Oxford` (1040–1139) ·
  `D3 §0.1 Hyperacute Management` (2419) · `§0.2 Syndromes and Localisation` (2479) ·
  `§0.3 TIA and Secondary Prevention` (2516) · `§0.4 Intracerebral Haemorrhage` (2565) ·
  `§0.5 Stroke Mimics and Chameleons` (2601) · `§0.6 The Paresis Patterns` (2625)
- **G-N5 Intracranial bleeds and ICP** — `04 ### Subdural` (1175) · `### Extradural` (1194) ·
  `### Cerebral Aneurysm` (1209) · `### Intracranial Pressure` / `### Low ICP` / `### Raised ICP`
  (1467–1499) · `### Hydrocephalus` (1500) · `### Idiopathic Intracranial Hypertension` (1524) ·
  `### Head Injury` (1536)
- **G-N6 Delirium, dementia and cognition** — `04 ## Dementias` +`### MCI` +`### Vascular`
  +`### Alzheimer's` +`### Lewy Body` +`### FTLD` +`### Cognitive-enhancing drugs` +`### NPH`
  (146–296) · `04 ## Delirium` (297) · `04 ## Delirium vs Dementia vs Depression` (320) ·
  `D2 §0.1 Reduced Consciousness` (2150) · `§0.2 Delirium` (2205) · `§0.3 Dementia` (2260) ·
  `§0.4 The Distinction` (2312) · `§0.5 Amnesia` (2340) · `§0.6 MCI and the "Worried About My
  Memory" Consultation` (2375) · `NEW_Drugs_15 §0.3` (5563) · `NEW_Neurology ## Acute Confusion`
  (5685) · `## Reduced Consciousness` (5701)
- **G-N7 Seizures and epilepsy** — `04 ## Seizures and Epilepsy` +6 subsections (749–834) ·
  `04 ## Anticonvulsants` (835) · `04 ## PNES` (861) · `D6 §0.1 Classification and First Seizure`
  (3232) · `§0.2 Status Epilepticus` (3290) · `§0.3 Epilepsy Management` (3333) ·
  `NEW_Drugs_15 §0.1` +`.1`–`.3` (5466–5513)
- **G-N8 Parkinsonism and movement disorders** — `04 ### Parkinson's Disease` (394) ·
  `### PD drug classes` (419) · `### Parkinson-Plus` (436) · `### Huntington` (474) ·
  `### Abnormal Involuntary Movements` (1747) · `### Restless Legs Syndrome` (1731) ·
  `D6 §0.4 Tremor` (3377) · `§0.5 Parkinsonism` (3420) · `§0.6 Chorea, Dystonia, Tics, Myoclonus`
  (3472) · `§0.7 Rigidity` (3517) · `NEW_Drugs_15 §0.2` +`.1`–`.5` (5514–5562)
- **G-N9 Neuropathy and weakness** — `04 ## Weakness — DDx` +`### No objective weakness`
  +`### With objective weakness` (1227–1275) · `04 ### Diabetic Neuropathy` (1276) ·
  `04 ### Charcot-Marie-Tooth` (1815) · `D4 §0.2 Peripheral Neuropathy` (2733) ·
  `§0.3 Radiculopathy` (2782) · `§0.4 Mononeuropathies and Entrapment` (2828) ·
  `§0.6 Myopathy` (2911) · `§0.7 Sensory Disturbance` (2944)
- **G-N10 Neuromuscular junction** — `04 ### Myasthenia Gravis` (1401) · `D4 §0.5` (2867) ·
  `NEW_Drugs_15 §0.5` (5601)
- **G-N11 Demyelinating disease** — `04 ### Multiple Sclerosis` (1311) · `### Neuromyelitis Optica`
  (1430) · `### GBS` (1345) · `### CIDP` (1379) · `NEW_Drugs_15 §0.4` (5590)
- **G-N12 Dizziness and vertigo** — `04 ### Vertigo` (1016) · `D5 §0.1 Disambiguating the Complaint`
  (2992) · `§0.2 AVS and HINTS` (3016) · `§0.3 Episodic Vertigo` (3074) · `§0.4 Disequilibrium`
  (3114) · `§0.6 Nystagmus` (3185) · `NEW_Drugs_15 §0.7 Drugs for Vestibular Disorders` (5632)
- **G-N13 Cranial nerves and facial palsy** — `04 ## Cranial Nerve Disorders and Vertigo` +
  `### Bell's Palsy` (969, 973) · `D7 §0.1 Cranial Nerve Localisation` (3563) · `§0.2 Facial Palsy`
  (3590) · `§0.6 Other Cranial Nerve Syndromes` (3789). (**ENT carries a Bell's palsy stub that
  already defers here** — that pointer is correct and should be preserved)
- **G-N14 Spinal cord syndromes** — `04 ### Brown-Séquard` (1605) · `### Subacute Combined
  Degeneration` (1614) · `### Anterior Spinal Artery Occlusion` (1645) · `### Syringomyelia` (1662) ·
  `### Tabes Dorsalis` (1677) · `### Friedreich's Ataxia` (1635)
- **G-N15 Motor neuron disease** — `04 ### MND` (446) · `### ALS` (454)
- **G-N16 Brain tumours** — `04 ## Brain Tumours` (920) · `04 ### Primary CNS Lymphoma` (649)

**MEDIUM**
- **G-N17 Gait** — `D5 §0.5 Gait Disorders` (3155). Overlaps `Examination.md §1.26 Trendelenburg's
  Sign and Gait` and MSK. Flag
- **G-N18 Aphasia** — `04 ### Aphasia` (1790). Ties to G-N4 localisation and N-13
- **G-N19 Immunosuppression-associated CNS infection** — `04 ### Toxoplasmosis` (624) ·
  `### Cryptococcosis` (667) · `### PML` (688). ID owns HIV staging; ID:676 already defers here

**UNGROUPED — stays put**: `04 ### Normal Pressure Hydrocephalus` (277) · `NEW_Drugs_15 §0.6` (5613) ·
2 administrative blocks

## LIMITATIONS
- **The psychiatry block (N1–N8) is NOT grouped here.** Its groupings belong with `Psychiatry_merged`
  and will be produced there, once it is clear which file will hold them.
- N-15 (vertigo), N-20 (cauda equina), N-13/N-14 (ENT) and N-11 (diplopia) are deliberately
  undecided pending the ENT, MSK and Ophthalmology passes.
- N-1 raises a **conflict with an already-approved decision** (GI M-1). Flagged, not resolved.
