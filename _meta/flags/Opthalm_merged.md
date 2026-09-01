# Opthalm_merged.md — grouping and misplacement flags

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
Sources: 6 · lines 1716 · numbering drift: **none**.
`05_Ophthalmology` 32 inbound (**History-Taking ×8, Examination ×6**);
`E1_Red_and_Painful_Eye` 27 inbound (**Paediatrics ×6, Emergency**). Zero inbound: `NEW_Drugs_11_Eye`.

## INBOUND FLAGS ALREADY RAISED — decisions needed here
| From | Item | Their L | Existing owner here |
|---|---|---|---|
| **Neuro N-11** | `D7 §0.3 Diplopia and Disorders of Eye Movement` | Neuro 3646 | `E2 §0.6 Field Defects and Diplopia` (1256) · `## Strabismus` +`### paralytic squint` (694, 720) |
| **Neuro N-12** | `### Horner's Syndrome` | Neuro 1001 | `### Horner Syndrome` (784) · `E3 §0.5 Ptosis and the Neuro-ophthalmic Patterns` (1418) |
| **MSK K-21** | `## Ocular trauma` | MSK 1304 | `E1 §0.5 Chemical Injury, Trauma and Foreign Bodies` (1018) · `## Corneal Abrasion` (64) |
| **OBGYN B-14** | `## Ophthalmia neonatorum` | OBGYN 825 | `## Conjunctivitis` (375) · `E1 §0.4` (996) |
**All four already have an owner here.** ⚠️ **`D7` has 8 inbound and 6 are from this file** — the
strongest single argument for N-11.

## PROPOSED MOVES
| ID | Section | L | → | Why |
|---|---|---|---|---|
| E-1 | `## 0.2 Drugs for Eye Examinations and Procedures` (NEW_Drugs_11) | 1506 | **Examination.md §1.18** | mydriatics and topical anaesthetic for fundoscopy. **§1.18 "Fundoscopy (Direct Ophthalmoscopy)" already exists** **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| E-2 | 4 × `**Focused Hx:**` + 4 × `**Examination:**` in `NEW_Ophthalmology` | 1632–1692 | **History-Taking.md / Examination.md** | L1662 *"visual acuity each eye separately — first, and always"*; L1679 *"pupils with the swinging-flashlight test"*; L1692 *"visual fields to confrontation"*. **Pure examination technique, and the RAPD test appears nowhere in `Examination.md`** **✅ RESOLVED 2026-09-01 — Option 1: left in place, indexed in `Examination.md` §3 and `History-Taking.md` §2 (`bcf7515`/`fab04f5`)** |
| E-3 | `## Eye Anatomy Reference` | 6 | **flag — Examination.md** | a reference diagram for the examination **✅ EXECUTED 2026-09-01 → `Examination.md` (c5df174)** |
| E-4 | `## Ocular Manifestations of Systemic Disease — Consolidated Reference` | 873 | **keep, flag** | a cross-system index — the eye findings of diabetes, hypertension, thyroid, MS, sarcoid, RA. **Preserve as a routing artefact**; several targets are contested |
| E-5 | `## Tropical Eye Diseases` — `### Xerophthalmia` · `### Trachoma` · `### Onchocerciasis` | 828–872 | **arguable — Infectious Disease** | `ID 08_07 §0.9.3 Filariasis` and the vector-borne cluster. Counter: they are blinding eye diseases. **Flag** |
| E-6 | `## Thyroid Eye Disease` | 804 | **flag** | `Endocrine 06 §0.2.1 Graves' Disease`, `I1 §0.3`. `E3 §0.3 Proptosis and Orbital Disease` (1360) is the local partner |
| E-7 | `## Diabetic Retinopathy` (615) · `## Hypertensive Retinopathy` (644) | | **keep, flag** | ⚠️ **`Cardio B2 §0.3` carries `> [!danger] Fundoscopy is the examination that most often makes the diagnosis` (Cardio C-7) and `Opthalm:1221` points back at `[[B2]] 0.3`.** The two files already cross-reference correctly — **do not break this pair** |

## KEEP + IN-TEXT FLAG
- ⚠️ **`## Stye (Hordeolum) and Chalazion` (425) and `## Hordeolum (Stye)` (461) are two sections on
  the same condition, 36 lines apart, in one source.** The clearest same-source duplicate found in
  the vault.
- **Glaucoma is split three ways within `05_Ophthalmology`**: `## Glaucoma` +`### Angle-Closure`
  (245, 249) · `## Glaucoma and Anti-Glaucoma Medications` (357) · `## Open-Angle Glaucoma` (499).
  Plus `E1 §0.3 Acute Angle-Closure Glaucoma` (974) and `NEW_Drugs_11 §0.4` (1536).
- `## Blepharospasm` (410) sits between two lid-disease sections but is a **movement disorder** —
  flag against `Neuro D6 §0.6 Chorea, Dystonia, Tics and Myoclonus`.

## GROUPINGS
**HIGH**
- **G-E1 The red eye** — `## The Red Eye — Regional Approach and DDx` (26) · `## Conjunctivitis`
  (375) · `## Anterior Uveitis` +`### other types` (277, 297) · `## Episcleritis and Scleritis`
  (308) · `## Keratitis` (329) · `## Subconjunctival Haemorrhage` (46) ·
  `E1 §0.1 Assessing the Red Eye` (899) · `§0.2 The Sight-Threatening Causes` (938) ·
  `§0.4 Conjunctivitis` (996) · `§0.6 Chronic and Recurrent Red Eye` (1051) ·
  `NEW_Ophth ## Acute Eye Pain` (1655)
- **G-E2 Acute angle-closure glaucoma** — `## Glaucoma` +`### Angle-Closure` (245, 249) ·
  `E1 §0.3` (974)
- **G-E3 Sudden vision loss** — `## Causes of Sudden, Sustained Vision Loss` (12) ·
  `## Retinal Detachment` (102) · `## Vitreous Haemorrhage` (125) · `## Retinal Vein Occlusion`
  (140) · `## Retinal Artery Occlusion` (157) · `## AION` (174) · `## Optic Neuritis` (215) ·
  `E2 §0.1 Approach to Vision Loss` (1098) · `§0.2 Sudden Painless Vision Loss — the Vascular
  Causes` (1125) · `§0.3 Retinal Detachment and the Other Sudden Causes` (1159) ·
  `NEW_Ophth ## Acute Visual Loss` (1615) · `## Acute Floaters` (1682)
- **G-E4 Gradual vision loss** — `## Cataracts` (591) · `## AMD` (521) · `## Open-Angle Glaucoma`
  (499) · `## Ametropia` (550) · `## Retinitis Pigmentosa` (571) · `E2 §0.4 Gradual Vision Loss` (1194)
- **G-E5 Transient visual disturbance** — `## Retinal Migraine` (189) ·
  `## Colour Vision and Blurred Vision — DDx` (231) · `E2 §0.5` (1232) ·
  `NEW_Ophth ## Acute Visual Disturbance` (1667)
- **G-E6 Lids and lacrimal** — `## Blepharitis` (396) · `## Stye and Chalazion` (425) ·
  `## Hordeolum (Stye)` (461) · `## Entropion and Ectropion` (443) · `## Pinguecula` (451) ·
  `## Other Issues with the External Eye` (485) · `E3 §0.1 Eyelid Disorders` (1311) ·
  `§0.2 The Watering Eye` (1338)
- **G-E7 Pupil** — `## Pupil Problems` +`### afferent` +`### efferent (CN III)` +`### tonic (Adie)`
  +`### Horner` +`### Argyll Robertson` +`### anisocoria` (766–803) · `E3 §0.4 The Abnormal Pupil`
  (1388) · `§0.5 Ptosis and the Neuro-ophthalmic Patterns` (1418)
- **G-E8 Orbit** — `## Orbital and Peri-Orbital Cellulitis` (669) · `## Thyroid Eye Disease` (804) ·
  `E3 §0.3 Proptosis and Orbital Disease` (1360)
- **G-E9 Optic disc and papilloedema** — `## Papilloedema` (201) · `## Optic Neuritis` (215) ·
  `E3 §0.6 The Optic Disc, Nystagmus and Visual Hallucinations` (1440).
  (+ `Neuro ### Idiopathic Intracranial Hypertension`, `D5 §0.6 Nystagmus`)
- **G-E10 Retinopathy of systemic disease** — `## Diabetic Retinopathy` (615) ·
  `## Hypertensive Retinopathy` (644) · `## Ocular Manifestations of Systemic Disease` (873)
- **G-E11 Squint and amblyopia** — `## Strabismus` +`### concomitant` +`### paralytic`
  +`### amblyopia` (694–765). **Paediatric — check against Paediatrics and `Examination.md §1.23`**
- **G-E12 Ocular trauma and foreign body** — `## Corneal Abrasion` (64) ·
  `E1 §0.5 Chemical Injury, Trauma and Foreign Bodies` (1018) · `## Endophthalmitis` (83).
  **Cross-file — MSK K-21, `Emergency A7 §0.4`, `A8 §0.4`**
- **G-E13 Ophthalmic drugs** — `## Glaucoma and Anti-Glaucoma Medications` (357) ·
  `## Contact Lens Care` (369) · `NEW_Drugs_11 §0.1`–`§0.5` (1490–1585)
- **G-E14 Ophthalmic shingles** — `## Ophthalmic Shingles` (469). Cross-file with
  `Derm 09_07 ## Herpes zoster / shingles` (D-5)

## LIMITATIONS
- E-5 (tropical eye disease) and E-6 (thyroid eye disease) are boundary calls I have deliberately
  not made; both are defensible either way.
