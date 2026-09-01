

<!-- ===== SOURCE: 19_General_Practice_and_Preventive_Medicine.md ===== -->


> [!note] Why this file exists. The CSV category "General Practice, Preventive Med, Ethics & Communication" (29 rows) was found by Step 23 to be the **second-largest gap in this project**, and it was never "(NEW)"-tagged, which is why Step 21's first pass missed it. An audit of all 29 rows before building classified them as **7 adequately covered, 6 partially present, 16 genuinely absent** — not the "roughly half covered" previously assumed.
>
> **Placement rule applied to all 29 rows, in this order** — a new file was the last resort, not the default:
> 1. **Consultation skill → [[Communication]]** (the task-led station file): breaking bad news, DNACPR and goals of care, domestic and family violence, motivational interviewing, clinical handover, open disclosure, complaints, angry patients, professional boundaries, explaining a safeguarding referral.
> 2. **Clinical process / ethics / legal → [[Clinical-Process-EBM-Consent-Capacity]]**: documenting in the medical notes, mandatory reporting as a general duty.
> 3. **Preventive and screening *content* → the relevant organ-system file**, where it already lives and is already source-verified: bowel screening in [[03_Gastrointestinal]] Colorectal Cancer, cervical in [[17_09_Cervical__Vaginal_and_Endometrial_Cancer]] Cervical cancer screening, cardiovascular risk in [[01_Cardiovascular]], diabetes risk in [[06_Metabolic_Medicine_and_Endocrinology]]. **This file does not restate any of it** — those entries remain authoritative.
> 4. **This file, only for what fits none of the above:** general practice as a discipline and preventive care as a *system* — the consolidating framework that no single organ file can hold, continuity of care, the features that distinguish general practice, hospital avoidance, and behavioural risk factors spanning all four SNAP domains. Same justification as the five orphan topics in [[18_Geriatrics_and_Older_Persons_Health]]: a genuine cluster that no existing file owns, not a convenient container.
>
> Rows confirmed already covered and deliberately **not** duplicated here: breaking bad news, discussing end-of-life care, polypharmacy (see [[18_Geriatrics_and_Older_Persons_Health]] Polypharmacy and Deprescribing), ICE (applied throughout [[History-Taking]]), fitness to drive (Austroads-verified across [[01_Cardiovascular]], [[04_Neurology]] and others), and palliative care (see [[10_11c_Oncology_-_Palliative_Care_Prescribing]]).

> [!note] **Moved to `[[Preventive-Health]]` on 2026-09-01:** `0.1 Preventive Medicine and Screening in Australian General Practice` — reproduced there verbatim under a `SOURCE:` divider naming this file.

> [!note] **Moved to `[[Preventive-Health]]` on 2026-09-01:** `0.2 Lifestyle Risk Factors (SNAP) and Smoking Cessation` — reproduced there verbatim under a `SOURCE:` divider naming this file.

## 0.3 Hospital Avoidance and Potentially Preventable Hospitalisations

> [!note] Gap-filled from CSV ("Hospital avoidance," Medium yield). Verified absent: the only corpus-wide hit was this file's own placement-rule line listing it as a row to build. Placed here rather than in a disease file because it is a **property of how care is organised** rather than of any one condition — the same test that put continuity of care in this file. Verified against the AIHW *Atlas of avoidable hospitalisations in Australia: ambulatory care-sensitive conditions* and Victorian and NSW health department ACSC work, Aug 2026.

**D:** an **ambulatory care-sensitive condition (ACSC)** is one for which hospitalisation is considered **potentially avoidable through timely and effective care in the community**. Admissions for these are counted as **potentially preventable hospitalisations**, and the rate is used in Australia as a health-system performance measure — which is why the term appears in service planning as well as clinically.

> [!info] **The concept is a measure of the *system*, not a judgement about the patient or the admitting doctor — and this distinction matters clinically.** A "potentially preventable" admission does not mean the admission was wrong at the point it happened. It means that somewhere upstream — access, follow-up, medication supply, education, or a review that did not occur — there was a modifiable opportunity. **Admitting a patient who needs admitting is always correct**; the question the measure asks is what happened in the weeks before.

**The conditions this applies to** fall into three groups:
- **Chronic** — diabetes complications, COPD, congestive heart failure, angina, hypertension, asthma. These dominate the numbers, and the modifiable factor is usually **continuity, medication access and early review** (see Continuity of Care, and What Makes General Practice Different below).
- **Acute** — urinary tract and other infections, dehydration, cellulitis: conditions where earlier community treatment could have prevented deterioration.
- **Vaccine-preventable** — influenza, pneumococcal disease (see Preventive Medicine and Screening in Australian General Practice above, not repeated here).

### 0.3.1 What an intern can actually do

The temptation is to read this as policy. It is not — several of the levers sit with the person doing the discharge:

- **Ask why this admission happened now**, not only what to treat. Ran out of medicine? Could not get a GP appointment? Did not understand the sick-day plan? Nobody at home? Each has a different fix, and none is addressed by treating the presenting problem alone.
- **Make the discharge do the preventive work** — accurate medication list, a follow-up appointment that actually exists, a written action plan for the chronic condition, and a discharge summary the GP receives promptly. This is the single largest lever an inpatient team holds (see [[18_Geriatrics_and_Older_Persons_Health]] Discharge Planning and Home Safety Assessment, not repeated here).
- **Know the alternatives to admission** your service has: **Hospital in the Home (HITH)** for conditions treatable with community-delivered IV therapy or monitoring, ambulatory or rapid-access clinics, outreach and post-acute services, and — for older patients — the aged care pathways in [[18_Geriatrics_and_Older_Persons_Health]] Discharge Planning and Home Safety Assessment.
- **In residential aged care**, transfer decisions turn on whether the facility can deliver the care and on the resident's **advance care directive and ceiling of care** — an admission that contradicts a documented plan is a failure of communication rather than of medicine (see [[Communication]] Goals of Care and Ceiling of Care (Treatment Escalation Planning)).

> [!danger] **Aboriginal and Torres Strait Islander Australians experience substantially higher rates of potentially preventable hospitalisation**, including frequent avoidable admissions for chronic conditions — and the drivers identified in Australian research are **access and continuity**, not disease severity alone. The clinical consequence sits with the discharging team: **the generic discharge plan is the one most likely to fail here.** Ask specifically whether the patient can get the medicine (see [[Clinical-Process-EBM-Consent-Capacity]] Choosing a Medicine — Quality Use of Medicines for the Closing the Gap PBS Co-payment Program, not repeated here), whether follow-up is with a service they will actually attend — an **Aboriginal Community Controlled Health Organisation** may be that service — and whether the discharge summary is going to the clinician who will see them. Verified against Australian cohort research on frequent avoidable admissions among Aboriginal people with chronic conditions in NSW, Aug 2026.

---

## 0.4 Continuity of Care, and What Makes General Practice Different

> [!warning] FLAG 2026-09-01 — structural observation about this file
> **Every other section in `GP_merged.md` has a stronger home elsewhere**: the preventive-medicine half
> belongs with `Preventive-Health.md`, and `NEW_Investigations_General_and_Preventive` is sixteen
> general laboratory tests that belong with `Investigation-Interpretation.md`
> (`§0.1 Inflammatory Markers` duplicates its `§1.21` outright).
> **This section is the one with a genuine claim to be "general practice".**
> ⚠️ **Whether General Practice is a system or a setting is a decision for you, not a finding.**
> Recorded, not acted on.

> [!note] Gap-filled from CSV ("Continuity of care," High yield, and "Unique features of General practice," Medium — built together because the second is largely an explanation of why the first matters). Genuinely absent: **zero corpus-wide hits** for "continuity of care". Placed here rather than in [[Communication]] because this is a property of the *system and the therapeutic relationship over time*, not a consultation skill performed within a single station. Verified against RACGP position and advocacy material on the role of specialist GPs and continuity, the MJA analysis of patient enrolment and continuity in Australian general practice, and RACGP-reported NSW Health linked-data findings on post-discharge follow-up, Aug 2026.

**D:** the extent to which a patient experiences care as **connected and coherent over time**. Conventionally three components, which are genuinely different things and can come apart:
- **Relational** — seeing the *same clinician* over time, so accumulated knowledge of the person does not have to be rebuilt each visit.
- **Informational** — the *record* travels even when the clinician changes: results, medication changes, what has already been tried and failed.
- **Management** — different clinicians deliver a *consistent plan* rather than contradicting one another.

> [!info] Why the distinction matters practically: a patient can have excellent informational continuity (a complete shared record) and no relational continuity at all, and the two are not interchangeable. A locum with the full notes still does not know that this patient always minimises symptoms, or that the last three presentations were really about a deteriorating home situation.

**The evidence — this is not merely a nice principle:** continuity of care is associated with **greater patient satisfaction and better chronic disease self-management, fewer hospitalisations, and lower mortality**. An Australian-specific finding worth knowing: linked NSW Health and general practice data show patients **promptly followed up by their GP after a hospital admission are substantially less likely to be readmitted**, and aged care residents who keep seeing their regular GP after entering a facility have around **8% fewer emergency department presentations**.

> [!tip] The direct implication for an intern working in hospital, which is where this content is most immediately actionable: **the discharge summary and the follow-up appointment are the continuity mechanism.** They are not paperwork — they are the intervention that connects the admission to the rest of the patient's care, and the evidence above is the reason they matter (see [[18_Geriatrics_and_Older_Persons_Health]] Discharge Planning and Home Safety Assessment for how to do them well, and [[Communication]] Clinical Handover (ISBAR) and Prioritisation of Jobs for the in-hospital equivalent).

**Australian context:** patient enrolment with a single practice has historically **not** been a feature of Australian general practice, unlike several comparable systems — patients may attend multiple practices, which fragments both relational and informational continuity. Voluntary registration arrangements have been introduced to address this. Check current arrangements rather than relying on this description, as the policy is actively changing.

### 0.4.1 What actually distinguishes general practice as a discipline

Worth understanding because it explains why GP reasoning differs from hospital reasoning, and why an intern rotating into general practice finds their hospital habits do not transfer cleanly:

- **Undifferentiated presentations.** Patients arrive with symptoms, not diagnoses, and often very early in the illness when discriminating features have not yet appeared. Much of the skill is tolerating diagnostic uncertainty safely rather than resolving it immediately.
- **Very different pre-test probabilities.** The same symptom carries a far lower probability of serious disease in general practice than in an emergency department, because the population is different. **A test with good characteristics in a hospital population performs much worse in a low-prevalence one**, generating more false positives than true — which is why reflexively investigating everything is not the safer option it appears to be (see [[Clinical-Process-EBM-Consent-Capacity]] Diagnostic Test Characteristics — Sensitivity, Specificity, PPV and NPV).
- **Time as a diagnostic tool.** Reviewing in a defined interval — "watchful waiting" with an explicit plan — is a legitimate and often superior strategy to immediate investigation, provided the safety net is real.
- **Safety-netting is the core skill this depends on.** Tell the patient specifically **what should improve and by when, what would mean they need to be seen sooner, and exactly how to get seen**. Vague advice to "come back if it gets worse" is not a safety net.
- **Whole-person and longitudinal care** — comorbidity, family and social context, and the same clinician seeing the consequences of their own decisions over years, which is a genuinely different accountability from an episode of hospital care.
- **The gatekeeping and coordinating role** — managing the interface with specialist services rather than being one, and holding the whole picture when several specialists each hold part of it (see [[Communication]] Management of Patients with Multiple Chronic Medical Problems).


<!-- ===== SOURCE: NEW_Investigations_General_and_Preventive.md ===== -->


# NEW — Investigations: General and Preventive

> [!danger] **Sourcing limitation applying to this whole file.** Australian primary guideline domains are **egress-blocked** (verified 2026-08-30); AMH and Therapeutic Guidelines are subscription-gated. Entries are **snippet-sourced**. Numerics appear only on three-source agreement; assay- and laboratory-dependent reference intervals are **omitted with the omission stated in place**.

> [!note] **Two build-list rows collapse into other entries.** `Albumin` and `Serum Albumin` are the same test and are built once (0.2). `Prenatal Screening` duplicates `Prenatal Screening Panel`, already built as 0.5 of `NEW_Investigations_Obstetrics_and_Gynaecology.md`, and is not rebuilt here. Both are recorded in the build status table.

---

> [!note] **Moved to `[[Investigation-Interpretation]]` Part 2 on 2026-09-01 — 11 sections from this source block.**
>
> `0.1 Inflammatory Markers (CRP, ESR, Procalcitonin)` · `0.2 Albumin (Serum Albumin)` · `0.3 Alkaline Phosphatase (ALP)` · `0.4 Lactate Dehydrogenase (LDH)` · `0.5 Uric Acid (Serum Urate)` · `0.6 Ammonia (Ammonium)` · `0.7 Serum Ceruloplasmin` · `0.8 Calcitonin` · `0.9 Gallium Scan` · `0.10 Incisional Biopsy` · `0.11 Stains (Histochemical Special Stains and Immunohistochemistry)`
>
> Moved under the standing rule as extended to investigation interpretation: **how to read the
> test** is owned by `[[Investigation-Interpretation]]`; **what the result means in this disease**
> stays here, in each condition's own `Ix:` entry. The sections are reproduced there **verbatim and
> unrenumbered**, under a `SOURCE:` divider naming this file, so a pointer written by heading name
> still resolves.

> [!note] **Moved to `[[Preventive-Health]]` on 2026-09-01:** `0.12 Health Screening (Australian Population Screening Programs)` — reproduced there verbatim under a `SOURCE:` divider naming this file.

> [!note] **Moved to `[[Preventive-Health]]` on 2026-09-01:** `0.13 Low-Dose CT Screening (National Lung Cancer Screening Program)` — reproduced there verbatim under a `SOURCE:` divider naming this file.

## Build status

| # | Item | Built | Notes |
|---|---|---|---|
| 0.1 | Inflammatory Markers | yes | |
| 0.2 | Albumin | yes | |
| 0.2 | Serum Albumin | yes | **Same test as `Albumin`** — the build list carries both; built once. Calcium correction formula omitted (laboratory-specific coefficients). |
| 0.3 | ALP | yes | |
| 0.4 | Lactate Dehydrogenase | yes | |
| 0.5 | Uric Acid | yes | mg/dL↔mmol/L conversion refused, per the standing policy on presenting own arithmetic as a sourced threshold. |
| 0.6 | Ammonium | yes | Built as serum ammonia. Action thresholds omitted — age- and assay-dependent. |
| 0.7 | Serum Ceruloplasmin | yes | |
| 0.8 | Calcitonin | yes | Reference intervals and referral cut-offs omitted — assay- and sex-specific. |
| 0.9 | Gallium Scan | yes | Ga-67 (largely historical) distinguished explicitly from the Ga-68 PET tracers. |
| 0.10 | Incisional Biopsy | yes | |
| 0.11 | Stains | yes | Built as histochemical special stains plus immunohistochemistry. |
| 0.12 | Health Screening | yes | |
| 0.13 | Low-Dose CT Screening | yes | |
| 0.14 | Genetic Risk Assessment | yes | Commencement date of the Australian life-insurance genetic discrimination ban **omitted** — sources conflicted and it did not meet the three-source bar; the ban's existence and scope are stated. |
| 0.15 | Genetics & Molecular Testing | yes | |
| 0.16 | Pharmacogenomic Assessment | yes | Gene-specific dose-reduction percentages omitted — must come from the report and current guideline. |
| — | Prenatal Screening | **already built** | Duplicate of `Prenatal Screening Panel`, built as 0.5 of `NEW_Investigations_Obstetrics_and_Gynaecology.md`. Not rebuilt. |

**Items in file: 16 entries covering 17 of the 18 build-list rows; the 18th (`Prenatal Screening`) is a duplicate already built in the O&G file.**
