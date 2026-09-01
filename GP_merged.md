

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

<!-- ===== SOURCE: NEW_Investigations_General_and_Preventive.md ===== -->


# NEW — Investigations: General and Preventive

> [!danger] **Sourcing limitation applying to this whole file.** Australian primary guideline domains are **egress-blocked** (verified 2026-08-30); AMH and Therapeutic Guidelines are subscription-gated. Entries are **snippet-sourced**. Numerics appear only on three-source agreement; assay- and laboratory-dependent reference intervals are **omitted with the omission stated in place**.

> [!note] **Two build-list rows collapse into other entries.** `Albumin` and `Serum Albumin` are the same test and are built once (0.2). `Prenatal Screening` duplicates `Prenatal Screening Panel`, already built as 0.5 of `NEW_Investigations_Obstetrics_and_Gynaecology.md`, and is not rebuilt here. Both are recorded in the build status table.

---

## 0.1 Inflammatory Markers (CRP, ESR, Procalcitonin)

**D:** Three different measurements of the acute-phase response. **CRP** — a hepatic acute-phase protein measured directly. **ESR** — the rate at which red cells sediment in a column, an *indirect* measure driven largely by fibrinogen and immunoglobulins. **Procalcitonin** — a precursor peptide released systemically in bacterial infection.

**Ind:** Suspected infection or inflammation; monitoring response to treatment; suspected inflammatory arthritis, vasculitis or polymyalgia rheumatica; suspected myeloma or chronic inflammatory disease; part of the work-up of pyrexia of unknown origin.

**Role:** **Trend and magnitude, not diagnosis.** They tell you whether an inflammatory process is present and whether it is getting better or worse. They do not tell you where it is or what caused it.

> [!info] **The kinetics are the reason to choose one over another**
> Sources agree on the ordering: **procalcitonin rises within about 4–6 hours** of bacterial insult and peaks at **12–24 hours**, with a half-life around **24 hours**. **CRP begins rising at 12–24 hours** and peaks at **2–3 days**, with a half-life of roughly **19 hours**. **ESR is the slowest to rise and the slowest to fall** — it lags the clinical picture by days and can stay elevated for weeks after recovery.
> **Practical consequence:** a normal CRP very early in an acute illness means little; an ESR that is still high in a recovering patient does not mean treatment has failed.

> [!danger] **Do not ignore**
> - **A normal CRP does not exclude serious infection**, particularly in the **first hours** of illness, in the **immunosuppressed**, in **neutropenia**, and in **the elderly**, whose inflammatory response is blunted. Sources note explicitly that older patients mount a less pronounced response, putting them at risk of both under- and over-treatment.
> - **A raised CRP is not a reason to start antibiotics** on its own, and a falling CRP is not a reason to stop them if the patient is unwell. These are markers, not decisions.
> - **ESR is raised by anything that raises fibrinogen or immunoglobulins** — **anaemia, pregnancy, older age, female sex, obesity, renal failure, and paraproteinaemia**. A very high ESR with a modest CRP should raise the question of **myeloma or another paraprotein**, and is a distinctive pattern worth knowing. See [[10_02_Haemonc_-_Lymphomas_and_Multiple_Myeloma]].
> - **A markedly raised ESR with a compatible clinical picture in a patient over 50 raises giant cell arteritis** — but a normal ESR does **not** exclude it, and suspected GCA with visual symptoms is treated immediately, not investigated first. See [[12_04_Rheum_-_Vasculitis]].
> - **Procalcitonin is a stewardship tool, not a rule-in test.** Sources support its use to **shorten** antibiotic courses safely; they also state plainly that its sensitivity and specificity are suboptimal and it must be interpreted in clinical context. It is raised in non-infective states — major surgery, trauma, burns, cardiac arrest, severe renal impairment.

**Normal/abnormal:** Laboratory-specific reference intervals; **ESR ranges vary with age and sex** and must be read against an age-appropriate range rather than a single cut-off.

**Alt:** **Full blood count and film** (neutrophilia, left shift, lymphopenia); **blood cultures and site-specific cultures — the tests that actually identify the pathogen**; lactate; imaging; ferritin (an acute-phase reactant itself, which is why it is unreliable for iron deficiency in inflammation).

## 0.2 Albumin (Serum Albumin)

**D:** The principal plasma protein, synthesised by the liver. It carries drugs, hormones, bilirubin and calcium, and generates most of the plasma oncotic pressure.

**Ind:** Part of liver function tests; assessment of **nutritional and inflammatory state**; oedema and ascites; nephrotic syndrome; chronic disease and frailty assessment; needed to **correct serum calcium**; needed to calculate the **serum-ascites albumin gradient** and pleural fluid Light's criteria; component of prognostic scores (Child-Pugh, and others).

**Role:** A general marker of **hepatic synthetic function, protein loss and systemic illness** — and one of the more misinterpreted numbers on a routine panel.

> [!danger] **Hypoalbuminaemia is much more often a marker of inflammation than of malnutrition.** Albumin is a **negative acute-phase reactant**: it falls in any significant inflammatory illness because synthesis is downregulated and capillary leak redistributes it. A low albumin in an acutely unwell patient is a **severity marker**, not a prescription for nutritional supplementation, and treating it as "malnutrition" is the classic error.

> [!info] **Work through the causes by mechanism**
> - **Reduced synthesis** — chronic liver disease, and any acute inflammatory illness.
> - **Increased loss** — **renal** (nephrotic syndrome — check a urine protein:creatinine ratio), **gastrointestinal** (protein-losing enteropathy, coeliac disease, inflammatory bowel disease), **skin** (extensive burns).
> - **Redistribution and dilution** — sepsis and capillary leak, fluid overload, pregnancy.
> - **Genuine malnutrition** — real, but a late and slow change (albumin's half-life is long, around 20 days), which is why it is a poor short-term nutritional marker.

> [!warning] **Correcting calcium.** Roughly half of serum calcium is albumin-bound, so **total calcium falls with albumin while ionised (physiologically active) calcium is unchanged.** Use your laboratory's **corrected/adjusted calcium**, or measure ionised calcium directly where accuracy matters (critical illness, acid–base disturbance, massive transfusion). **A correction formula is deliberately not reproduced here** — the coefficients differ between laboratories and assays, and applying the wrong one is worse than reading the laboratory's own adjusted value.

> [!danger] **Do not ignore**
> - **Albumin also binds drugs.** Hypoalbuminaemia raises the free fraction of highly protein-bound drugs — **phenytoin** is the classic example, where a "normal" total level can conceal a toxic free level.
> - **Nephrotic syndrome** in a patient with oedema and hypoalbuminaemia requires urine protein quantification, not just a repeat albumin.
> - Albumin infusion is **not** a treatment for a low albumin figure; it has specific indications (large-volume paracentesis, spontaneous bacterial peritonitis, hepatorenal syndrome) and is otherwise not indicated.

**Normal/abnormal:** Laboratory reference interval; interpret **alongside CRP** — the two together distinguish an inflammatory fall from a loss or synthetic problem.

**Alt:** **Total protein and protein electrophoresis** (paraprotein, globulin fraction); **urine protein:creatinine ratio or albumin:creatinine ratio**; prealbumin (shorter half-life, still confounded by inflammation); INR as the more responsive measure of hepatic synthetic function; faecal alpha-1 antitrypsin for protein-losing enteropathy; formal dietetic assessment for nutrition.

## 0.3 Alkaline Phosphatase (ALP)

**D:** A family of isoenzymes from **liver (biliary canalicular membrane), bone (osteoblasts), placenta and intestine**, reported as a single total activity on routine biochemistry.

**Ind:** Part of every liver function panel; investigation of jaundice, cholestasis and abnormal LFTs; bone pain, pathological fracture and suspected metabolic bone disease; suspected malignancy with bone or liver metastases; unexplained raised ALP found incidentally.

**Role:** **The cholestatic marker.** A **cholestatic pattern** (ALP and GGT raised disproportionately to ALT/AST) points to biliary obstruction or infiltration; a **hepatitic pattern** (ALT/AST raised disproportionately) points to hepatocellular injury. Distinguishing the two is the first step in every abnormal LFT.

> [!info] **A raised ALP has one essential next question: liver or bone? GGT answers it.**
> - **ALP raised + GGT raised** → **hepatobiliary** origin.
> - **ALP raised + GGT normal** → **bone** (or placenta, or intestine) — think **Paget disease, osteomalacia, healing fracture, bone metastases, hyperparathyroidism, growing children**.
> This single pairing resolves most raised ALPs at the bedside and is high-yield.

> [!warning] **Physiological elevations are common and must not be investigated as disease**
> - **Children and adolescents** have a much higher ALP from bone growth — a value that would be markedly abnormal in an adult can be normal in a growing child. Always read paediatric ALP against an **age-specific** range.
> - **Pregnancy**, particularly the third trimester, raises ALP because of the **placental** isoenzyme.
> - Both are ordinary findings; treating them as pathology generates needless imaging.

> [!danger] **Do not ignore**
> - **An isolated raised ALP with a normal GGT in an older adult** — consider **Paget disease** (usually asymptomatic, often incidental) and **osteomalacia/vitamin D deficiency** (check calcium, phosphate, vitamin D and PTH).
> - **A cholestatic picture with pain, fever and jaundice is ascending cholangitis** — an emergency needing antibiotics and biliary drainage, not an outpatient ultrasound. See [[03_Gastrointestinal]].
> - **Painless obstructive jaundice with weight loss** is pancreatic or biliary malignancy until proven otherwise.
> - **Very low ALP** is unusual and is a clue to **hypophosphatasia**, malnutrition, zinc deficiency, hypothyroidism or Wilson disease.

**Normal/abnormal:** Laboratory- and **age-specific** reference intervals; **ALP isoenzyme fractionation** is available where GGT does not settle the question.

**Alt:** **GGT** (the discriminator); full LFTs including bilirubin, ALT, AST and albumin; **abdominal ultrasound** as the first imaging test in cholestasis; MRCP; calcium, phosphate, vitamin D and PTH for the bone pathway; bone scan and skeletal imaging.

## 0.4 Lactate Dehydrogenase (LDH)

**D:** A ubiquitous intracellular enzyme released whenever cells are damaged or turn over rapidly. Present in essentially every tissue, which is both its use and its limitation.

**Ind:** Suspected **haemolysis** (with the rest of the haemolysis screen); **tumour lysis syndrome**; staging and prognosis in **lymphoma, myeloma, germ cell tumours and melanoma**; suspected **PJP** in the immunosuppressed; assessment of pleural fluid (Light's criteria); suspected bowel or other tissue infarction.

**Role:** A **non-specific marker of cell turnover or destruction** that is genuinely useful only within a defined clinical question.

> [!warning] **LDH on its own answers nothing.** It is raised in myocardial infarction, muscle injury, liver disease, renal infarction, pulmonary embolism, haemolysis, malignancy, severe infection and after seizures. **Ordering it "to see" produces an uninterpretable result.**

> [!info] **Where LDH earns its place**
> - **Haemolysis screen:** **raised LDH + raised unconjugated bilirubin + reticulocytosis + LOW haptoglobin**. LDH is one leg of that quartet and is not interpreted alone. See [[10_05_Haemonc_-_Normocytic_Anaemia_and_Sickle_Cell_Disease]].
> - **Tumour lysis syndrome:** rising LDH with **hyperkalaemia, hyperphosphataemia, hyperuricaemia and hypocalcaemia** after starting chemotherapy — an oncological emergency. See [[10_10a_Haemonc_-_Haematological_and_Oncological_Emergencies]].
> - **Lymphoma and germ cell tumours:** LDH is part of formal **prognostic indices**, so it is measured at diagnosis and tracked.
> - **Pleural fluid:** pleural:serum LDH ratio and absolute pleural LDH form two of the three **Light's criteria** separating exudate from transudate.
> - **PJP pneumonia:** a raised LDH in a breathless immunosuppressed patient with a relatively clear chest X-ray is a recognised supporting feature, not a diagnosis.

> [!danger] **Do not ignore**
> - **A haemolysed specimen produces a spuriously raised LDH** (and a raised potassium) from red cells lysed in the tube. **A high LDH with a high potassium and a "haemolysed" comment is a sampling artefact** — repeat before acting.
> - **Thrombotic microangiopathy** — a very high LDH with **thrombocytopenia, fragments on the film and renal impairment** — is TTP/HUS and is an emergency requiring immediate haematology involvement.

**Normal/abnormal:** Laboratory reference interval; the **trend** in an oncology patient is usually more informative than any single value.

**Alt:** For haemolysis — **haptoglobin, reticulocytes, bilirubin, blood film, direct antiglobulin test**; troponin for myocardial injury; CK for muscle; disease-specific tumour markers; imaging for suspected infarction.

## 0.5 Uric Acid (Serum Urate)

**D:** The end product of purine metabolism, renally excreted. Measured as **serum urate**, reported in Australia in **mmol/L**.

**Ind:** Suspected or established **gout** — for long-term monitoring rather than acute diagnosis; monitoring **urate-lowering therapy**; suspected or established **tumour lysis syndrome**; **pre-eclampsia** assessment; investigation of urate nephrolithiasis and of chronic kidney disease.

**Role:** In gout, urate is the **treatment target**, not the diagnostic test.

> [!danger] **A normal serum urate during an acute attack does NOT exclude gout, and this is the single most-tested point.**
> Urate falls during acute inflammation. Sources report that during acute attacks a substantial minority of patients have a genuinely normal serum urate. **Measure urate 2–4 weeks after the attack has settled**, when it reflects the patient's true steady state. Diagnosing or excluding gout on an acute-phase urate is a recognised error in both directions.

> [!info] **The diagnostic test for gout is joint aspiration.**
> **Negatively birefringent, needle-shaped monosodium urate crystals** under polarised light. This matters because the differential is **septic arthritis**, which is limb- and life-threatening and can coexist with crystal arthritis. See [[12_02_Rheum_-_Ankylosing_Spondylitis__Gout__Pseudogout__Reactive_Arthritis__Fibromyalgia__PMR__CFS]].

> [!info] **The treat-to-target figure.** Sources agree on a serum urate target of **<0.36 mmol/L** on urate-lowering therapy, with a lower target (commonly quoted as <0.30 mmol/L) where there are tophi or frequent flares. Allopurinol is started at a low dose and titrated to that target with repeat urate measurement, not fixed at a starting dose.

> [!danger] **Do not ignore**
> - **A hot, swollen joint is septic arthritis until proven otherwise** — aspirate, culture, and do not let a raised urate or a history of gout persuade you otherwise. This mistake destroys joints.
> - **Do not stop established allopurinol during an acute flare**, and starting urate-lowering therapy can itself precipitate a flare — which is why flare prophylaxis is co-prescribed.
> - **Allopurinol hypersensitivity syndrome** is rare and potentially fatal, with a recognised association with **HLA-B\*58:01** (see 0.16) and with renal impairment and higher starting doses.
> - **Asymptomatic hyperuricaemia is generally not treated** — most people with a raised urate never develop gout.
> - **In tumour lysis syndrome**, urate rises with potassium and phosphate; **rasburicase** (contraindicated in **G6PD deficiency**) and allopurinol have different roles and are not interchangeable.

**Normal/abnormal:** Laboratory reference interval (**mmol/L in Australia** — beware US sources quoting **mg/dL**; **the conversion is not performed here**, since presenting my own arithmetic as a sourced threshold is exactly the trap this file avoids).

**Alt:** **Joint aspiration with polarised microscopy and culture — the diagnostic test**; renal function and eGFR; **ultrasound (double contour sign)** and **dual-energy CT** for urate deposition; 24-hour urinary urate in selected cases; screening for the metabolic comorbidities that travel with gout.

## 0.6 Ammonia (Ammonium)

**D:** Plasma ammonia, a nitrogenous product of protein metabolism and gut bacterial activity, normally detoxified to urea by the liver.

**Ind:** **Encephalopathy of unclear cause**, particularly where the history does not fit; suspected **inborn error of metabolism** in a neonate or child with encephalopathy, vomiting or unexplained deterioration; **valproate**-associated encephalopathy; suspected urea cycle disorder in an adult; unexplained coma.

**Role:** **Narrow and frequently misused.** In an adult with known cirrhosis, ammonia adds little; in a child or an undifferentiated patient, a markedly raised ammonia can point to a treatable metabolic emergency.

> [!danger] **Hepatic encephalopathy is a CLINICAL diagnosis and ammonia does not grade it.**
> Sources are explicit that serum ammonia **does not correlate with the severity of overt hepatic encephalopathy**, is heavily affected by sample handling and processing, and should not be used to diagnose, exclude or monitor it. **Do not withhold lactulose because the ammonia is normal, and do not diagnose encephalopathy because it is high.** Look for the precipitant instead — infection (including SBP), gastrointestinal bleeding, constipation, dehydration, electrolyte disturbance, sedatives.

> [!warning] **The result is only as good as the specimen, and this is where most spurious results come from.** Sources agree on: a **free-flowing sample without a tourniquet** (venous stasis and muscle activity raise it), **transported on ice**, and **analysed rapidly** — one source specifies within about 20 minutes. Delay, a difficult draw, or a clenched fist can produce a high value in a well patient and send a whole work-up in the wrong direction. **Call the laboratory before taking the sample.**

> [!danger] **Do not ignore**
> - **In a neonate or infant, a markedly raised ammonia with encephalopathy is a metabolic emergency** — urea cycle defects and organic acidaemias. Stop protein intake, give intravenous dextrose to suppress catabolism, and involve the metabolic service immediately; treatment cannot wait for the diagnosis. See [[15_17a_Paeds_-_Hyperthyroidism_and_Approach_to_Inherited_Metabolic_Disease]].
> - **A very high ammonia in a patient without liver disease demands an explanation** — valproate, urea cycle disorder presenting in adulthood, urease-producing organism with urinary stasis, portosystemic shunt, or salicylate toxicity.
> - **Hyperammonaemic encephalopathy from valproate can occur with normal LFTs and a therapeutic valproate level.**

**Normal/abnormal:** Laboratory- and **age-specific** intervals (neonatal values are higher). **Numeric thresholds for action are deliberately not stated** — they are age- and assay-dependent, and the clinical context, not the number, drives management.

**Alt:** LFTs, INR, glucose, electrolytes, septic screen and cultures; **blood gas** (metabolic acidosis with a raised anion gap in organic acidaemia); plasma amino acids and urine organic acids in suspected metabolic disease; CT head and EEG to exclude alternatives; drug levels.

## 0.7 Serum Ceruloplasmin

**D:** The copper-carrying alpha-2 glycoprotein made by the liver, carrying the majority of circulating copper. Measured as part of the work-up for **Wilson disease**.

**Ind:** **Unexplained liver disease in a young person** — the classic indication, and the one an intern must know; unexplained **movement disorder, dysarthria, dystonia or tremor** in a young person; **new psychiatric presentation with neurological signs** in someone under 40; unexplained **Coombs-negative haemolytic anaemia** with liver disease; screening of **first-degree relatives** of a person with Wilson disease.

**Role:** A **screening test only**. Wilson disease is diagnosed on a combination of findings, never on ceruloplasmin alone.

> [!danger] **A normal ceruloplasmin does not exclude Wilson disease — it is an ACUTE-PHASE REACTANT.**
> Sources state that levels **rise into the normal range with concurrent inflammation, active hepatitis, pregnancy and oestrogen therapy** (including the combined oral contraceptive). This is the failure mode that matters, because the patients being tested frequently have active hepatitis. A convincing clinical picture with a normal ceruloplasmin still requires **24-hour urinary copper, slit-lamp examination and specialist referral**.

> [!warning] **A low ceruloplasmin is not specific either.** Sources report its positive predictive value used alone in patients with liver dysfunction can be **very low** — it falls in any cause of impaired hepatic synthesis, in protein-losing states, and in heterozygous carriers who will never develop the disease. It performs as a screen (high sensitivity at a low cut-off) and fails as a diagnosis.

> [!info] **What the diagnosis actually rests on**
> **Low ceruloplasmin** + **raised 24-hour urinary copper** (sources give normal as roughly ≤30 µg/day and Wilson disease as typically >100 µg/day **in adults**; **the paediatric threshold is lower — sources give above roughly 40 µg/day in children** — see [[NEW_Investigations_Renal_and_Urology]] 0.11, which states both. Treat both as orientation: sources describe these biochemical thresholds as imperfect) + **Kayser-Fleischer rings on slit-lamp examination** — the combination of KF rings with a clearly low ceruloplasmin is described as sufficient to establish the diagnosis. Where doubt remains: **hepatic copper on liver biopsy** and **ATP7B genetic testing**.

> [!danger] **Do not ignore**
> - **Wilson disease is treatable and untreated it is fatal** — this is why it is screened for in young people with unexplained liver or neuropsychiatric disease, despite being rare. Missing it is a permanent loss.
> - **Kayser-Fleischer rings need a slit lamp** — they are not reliably seen on bedside inspection, and their absence does not exclude hepatic Wilson disease (they are more consistently present in the neurological form).
> - **Acute liver failure in a young person with Coombs-negative haemolysis and a disproportionately low ALP** is a described Wilsonian pattern and is a transplant emergency.
> - **Screen the siblings.** It is autosomal recessive, and a presymptomatic sibling can be treated before any damage occurs.

**Normal/abnormal:** Laboratory reference interval; sources use a screening threshold around **<0.2 g/L**, with **<0.1 g/L** carrying much greater weight. Interpret with CRP and the clinical picture, never alone.

**Alt:** **24-hour urinary copper** (with and without penicillamine challenge in children); **slit-lamp examination**; serum copper (frequently misleading and not a substitute); **liver biopsy for hepatic copper quantification**; **ATP7B mutation analysis**; MRI brain in the neurological form.

## 0.8 Calcitonin

**D:** A peptide hormone secreted by thyroid **parafollicular C cells**. Its physiological role in calcium homeostasis in humans is minor; its clinical role is entirely as a **tumour marker for medullary thyroid carcinoma (MTC)**.

**Ind:** **Suspected or confirmed medullary thyroid carcinoma** — pre-operative assessment, post-operative surveillance for residual or recurrent disease; **MEN2 kindreds** and **RET** mutation carriers; a thyroid nodule with **suspicious or indeterminate cytology**, or a family history of MTC or MEN2. **Not for the routine assessment of calcium disorders** — it is not a test for hypercalcaemia.

**Role:** The **most specific marker for MTC**, and the basis of both diagnosis and lifelong follow-up in those who have it.

> [!warning] **Routine calcitonin in every thyroid nodule is contested, and the sources say so.** They describe the practice as **controversial with no definite recommendation for or against** and insufficient evidence for universal testing. The argument against is the volume of **mildly raised, non-specific results** it generates; the argument for is that MTC is otherwise found late. Follow your endocrine unit's policy rather than assuming either position.

> [!danger] **A mildly raised calcitonin is usually NOT medullary thyroid carcinoma.**
> Sources list recognised causes of non-MTC elevation: **proton pump inhibitors** (via raised gastrin, which stimulates C cells — a very common and easily missed confounder), **autoimmune thyroid disease**, renal impairment, neuroendocrine tumours of other origin, smoking, and hypercalcaemia. **Ask about the PPI before referring.** By contrast, a **markedly** raised calcitonin in a patient with a thyroid nodule is strongly suggestive and warrants urgent specialist assessment.

> [!danger] **Do not ignore**
> - **A diagnosis of MTC obliges you to look for the syndrome.** **Exclude phaeochromocytoma before any thyroid surgery** — operating on an unrecognised phaeochromocytoma can be fatal. Also check calcium and PTH for hyperparathyroidism. See [[10_11b_Oncology_-_Genetic_Cancer_Predisposition_Syndromes]].
> - **Offer RET germline testing** to everyone with MTC, and **cascade testing to relatives** — gene carriers can have prophylactic thyroidectomy before cancer develops, which is one of the clearest examples in medicine of genetic testing changing an outcome.
> - **MTC does not take up radioiodine** and is not followed with thyroglobulin — the surveillance markers are **calcitonin and CEA**.
> - **Fine-needle aspiration cytology can miss MTC**; a raised calcitonin overrides a reassuring cytology result.

**Normal/abnormal:** **Assay-specific reference intervals, with different ranges for males and females** (men have higher values), and **numeric thresholds are deliberately not stated here** — they vary between assays, and the appropriate cut-off for referral is set locally. Stimulated testing is a specialist procedure.

**Alt:** **CEA** (co-secreted, tracked alongside calcitonin); thyroid **ultrasound** and **FNA cytology** with calcitonin measured in the needle washout; **RET** germline and somatic testing; plasma metanephrines and calcium/PTH for the MEN2 components; neck and staging imaging.

## 0.10 Incisional Biopsy

**D:** Surgical removal of a **representative portion** of a lesion, leaving the remainder in situ. Distinguished from **excisional** biopsy (the whole lesion removed), **punch** biopsy (a small full-thickness cylinder), **core** biopsy (a needle core), and **fine-needle aspiration** (cells only, no architecture).

**Ind:** A lesion **too large to excise without first knowing the diagnosis**, or where excision would be disfiguring or mutilating; suspected **soft tissue sarcoma** or **bone tumour**; large or deep lesions where the treatment plan depends on histological type and grade; ulcerated or infiltrative lesions of the mouth, vulva or skin.

**Role:** Obtains **architecture as well as cytology** — it shows how cells relate to surrounding tissue, which cytology cannot, and so distinguishes invasion from in-situ disease.

> [!danger] **In suspected sarcoma, the biopsy must be planned by the team that will perform the definitive resection.**
> A badly sited biopsy tract **contaminates tissue planes and compartments** and can convert a limb-sparing operation into an amputation, because the tract must be excised with the specimen. **Refer suspected sarcoma to a specialist sarcoma centre before biopsying it.** This is the highest-consequence point in this entry and applies to any deep or enlarging soft-tissue mass, particularly one **larger than about 5 cm, deep to fascia, or growing**. See [[11_09a_Ortho_-_Orthopaedic_and_Bone_Malignancies]].

> [!warning] **Sampling error is the characteristic failure.** A partial biopsy samples part of a heterogeneous lesion: it can **under-grade** a tumour, miss a focus of invasion, or return "benign" from the benign edge of a malignant lesion. **A negative biopsy that does not fit the clinical picture must be repeated or escalated, not accepted.**

> [!info] **Choosing the biopsy type**
> - **Pigmented skin lesion suspicious for melanoma** → **excisional biopsy with a narrow margin** is preferred, because **Breslow thickness** determines staging and management and a partial biopsy can under-measure it. Incisional or punch biopsy is reserved for lesions too large or in sites where excision is not feasible (face, acral, subungual) — and the limitation must be flagged to the pathologist.
> - **Deep soft tissue mass** → imaging **before** biopsy, and biopsy planned by the treating unit.
> - **Lymph node suspicious for lymphoma** → **whole-node excision** where possible; core biopsy is often adequate but FNA alone is usually **not**, because lymphoma classification needs architecture.

> [!danger] **Do not ignore**
> - **Send the specimen in the right medium.** Formalin for histology, but **fresh or saline** if microbiology culture or lymphoma flow cytometry is needed, and **fresh/frozen** for some molecular studies. Formalin makes culture impossible — a specimen sent wrongly usually cannot be retaken without another procedure.
> - **Label laterality and site precisely**, and orient the specimen if margins matter.
> - **Give the pathologist the clinical information.** A histology request that says only "lesion" invites a non-committal report.
> - Check **anticoagulation, bleeding risk and infection risk** before any biopsy.

**Normal/abnormal:** A histopathology report giving tissue type, benign or malignant, grade, and — where the specimen allows — depth, margins and molecular markers.

**Alt:** **Excisional biopsy**; **core needle biopsy** (often image-guided — the standard for breast and many deep lesions, and less invasive); **punch biopsy** for skin; **FNA cytology** (fast, low morbidity, no architecture); **imaging-guided biopsy**; **frozen section** for intraoperative decisions.

## 0.11 Stains (Histochemical Special Stains and Immunohistochemistry)

**D:** Additional stains applied to tissue beyond the routine **haematoxylin and eosin (H&E)**. **Histochemical "special" stains** exploit chemical reactions with tissue components; **immunohistochemistry (IHC)** uses labelled antibodies against specific proteins, conventionally read as **brown positive staining** against a blue counterstain.

**Ind:** Requested by the pathologist to answer a specific question raised by the H&E — identifying an organism, a deposit, or the lineage of an undifferentiated tumour. Occasionally requested by the clinician when a particular diagnosis is suspected, which is why an intern should know that **the clinical question on the request form determines which stains get done**.

**Role:** Turns a descriptive H&E into a specific diagnosis.

> [!info] **The special stains worth knowing by name**
> - **PAS (periodic acid-Schiff)** — glycogen, mucin, **basement membranes** (hence its use in renal biopsy); **PAS-D** (with diastase, which digests glycogen) is a **fungal** stain.
> - **Ziehl-Neelsen** — **acid-fast bacilli**: *Mycobacterium tuberculosis* and other mycobacteria.
> - **Congo red** — **amyloid**, staining orange-red on light microscopy with the characteristic **apple-green birefringence under polarised light**.
> - **Perls Prussian blue** — **iron/haemosiderin**: haemochromatosis, haemosiderosis, and marrow iron stores.
> - **Gram** — bacteria in tissue. **Silver stains** (e.g. Grocott) — fungi and *Pneumocystis*. **Trichrome and reticulin** — fibrosis and architecture, used in liver biopsy staging.

> [!info] **Immunohistochemistry answers "what lineage is this?" and "is it treatable?"**
> Broad lineage markers (cytokeratins for epithelial, CD45/LCA for lymphoid, S100 and melanocytic markers for melanoma) sort an undifferentiated tumour; then **predictive markers** direct therapy — **ER, PR and HER2** in breast cancer, **mismatch repair proteins** in colorectal and endometrial cancer (which also screens for **Lynch syndrome**), and a growing list of others.

> [!danger] **Do not ignore**
> - **A stain is only as good as the tissue it is applied to.** Formalin fixation prevents culture; **if infection is a possibility, send fresh tissue for microbiology as well** — histology stains show organisms but give **no susceptibilities**, and a Ziehl-Neelsen positive result still needs culture or molecular testing for speciation and drug sensitivity.
> - **Negative stains do not exclude.** Acid-fast bacilli are notoriously sparse; a negative ZN on tissue does not exclude tuberculosis, and **culture and PCR** are required.
> - **Tell the pathologist what you suspect.** "Query amyloid", "query TB", "immunosuppressed" changes which stains are run and can save a repeat procedure.
> - Immunohistochemistry has **false positives and negatives**, and results are interpreted as a panel in context, never as a single positive stain.

**Normal/abnormal:** Descriptive, integrated into the histopathology report rather than reported as a value.

**Alt:** **Microbiological culture and susceptibility testing**; **PCR / nucleic acid amplification** on tissue; **flow cytometry** (needs fresh tissue) for haematological malignancy; **molecular and cytogenetic testing** including FISH and next-generation sequencing; electron microscopy in selected renal and neuromuscular pathology.

> [!note] **Moved to `[[Preventive-Health]]` on 2026-09-01:** `0.12 Health Screening (Australian Population Screening Programs)` — reproduced there verbatim under a `SOURCE:` divider naming this file.

> [!note] **Moved to `[[Preventive-Health]]` on 2026-09-01:** `0.13 Low-Dose CT Screening (National Lung Cancer Screening Program)` — reproduced there verbatim under a `SOURCE:` divider naming this file.

## 0.9 Gallium Scan

**D:** **Gallium-67 citrate scintigraphy** — a SPECT nuclear medicine study in which Ga-67, an iron analogue that binds transferrin and lactoferrin, localises to sites of infection, inflammation and some tumours. Imaging is delayed, typically **48–72 hours** after injection.

**Ind:** Historically: **pyrexia of unknown origin**, occult infection and abscess, osteomyelitis and discitis, **sarcoidosis** disease activity, interstitial lung disease, and lymphoma staging.

**Role:** **Largely historical.** Sources state plainly that **Ga-67 has been largely replaced by 18F-FDG PET/CT**, which gives earlier imaging, better resolution and quantification (SUV). An intern needs to recognise the name, understand why it was used, and know what has superseded it.

> [!warning] **Do not confuse gallium-67 with the gallium-68 PET tracers, which are contemporary and completely different tests.** Sources distinguish them clearly: **Ga-67 is a SPECT agent**; **Ga-68 is a PET isotope** used to label targeting molecules —
> - **Ga-68 DOTATATE** targets **somatostatin receptors** — the imaging standard for well-differentiated **neuroendocrine tumours**;
> - **Ga-68 PSMA** targets prostate-specific membrane antigen — **prostate cancer** staging and detection of recurrence.
> These share only the element. Reading "gallium scan" on a request and assuming a 1970s infection study when the patient is being staged for prostate cancer is a real and avoidable error.

> [!danger] **Do not ignore**
> - **Delayed imaging means a delayed answer** — Ga-67 requires the patient to return at 48–72 hours, which is why it is impractical in acute illness.
> - **Radiation dose is significant** and higher than most alternatives.
> - **Physiological bowel and hepatic uptake** limits abdominal interpretation; normal uptake occurs in liver, spleen, bone marrow, bowel and lacrimal glands.
> - **Sarcoidosis** patterns (lambda and panda signs) are classic teaching but are not specific, and **serial CT and lung function** now drive management.

**Normal/abnormal:** Reported qualitatively as abnormal focal uptake against the known physiological distribution.

**Alt:** **18F-FDG PET/CT** — the modern replacement for essentially all the historical indications; **labelled white cell scan** for infection where PET is unsuitable; **CT and MRI**; **Tc-99m bone scan** for osteomyelitis; echocardiography and blood cultures for endocarditis; the **Ga-68 PET tracers** above for their specific tumour indications.

## 0.14 Genetic Risk Assessment

> [!warning] FLAG 2026-09-01 — TWO-WAY DISAGREEMENT: neither file owns this
> **`Heme Onc_merged 10_11b_Oncology_-_Genetic_Cancer_Predisposition_Syndromes` — Li-Fraumeni, BRCA1/2,
> Lynch, FAP, von Hippel-Lindau — has 3 inbound references and ALL THREE ARE FROM THIS FILE.**
> This entry and `§0.15 Genetics and Molecular Testing` point there; it does not point back.
> ⚠️ **Neither end is authoritative. Content left where it is; both ends flagged; NOT resolved.**

**D:** Structured assessment of an individual's risk of a heritable condition, built from a **three-generation family pedigree** — who is affected, with what, at what age, and how they are related — combined with personal and ethnic factors, and used to decide whether genetic testing, surveillance or referral is warranted. **It precedes testing and often replaces it.**

**Ind:** A family history of **cancer** suggesting a predisposition syndrome (multiple affected relatives on one side, young ages at diagnosis, multiple primaries in one person, characteristic tumour combinations, or a known familial variant); familial **cardiac** disease (cardiomyopathy, long QT, sudden unexplained death under 50); familial neurological or neuromuscular disease; recurrent pregnancy loss or a child with congenital anomalies; **consanguinity**; preconception carrier screening.

**Role:** Determines who needs testing, **which test**, and — crucially — **who should be tested first**.

> [!danger] **Test the affected relative first, not the worried well one.**
> Testing an **affected** family member establishes whether a pathogenic variant exists in that family and identifies it. Only then can testing an unaffected relative give a meaningful answer. **An uninformative negative in an unaffected person, when no family variant has been identified, means nothing at all** — and is routinely misread as reassurance. This is the single most important operational point in genetic risk assessment.

> [!info] **What the pedigree is looking for**
> Age at diagnosis younger than usual; **multiple affected relatives on the same side**; **bilateral or multiple primary tumours**; characteristic combinations (breast + ovarian; colorectal + endometrial; medullary thyroid + phaeochromocytoma); **male breast cancer**; and ethnicity carrying founder variants (for example, Ashkenazi Jewish ancestry and *BRCA1/2*).

> [!warning] **A strong family history changes management even without a genetic diagnosis.** Where no pathogenic variant is found, **family-history-based surveillance** still applies — earlier and more frequent colonoscopy, earlier breast imaging, cardiac screening of relatives. A negative test does not cancel the family history.

> [!danger] **Do not ignore**
> - **Genetic information is inherently shared.** A result affects relatives who have not consented and may not want to know. Consent, confidentiality and the process of **cascade testing** are handled by genetic counselling services, not opportunistically in a ward round.
> - **The result may be untreatable knowledge** (Huntington disease is the paradigm), and predictive testing for such conditions follows a formal counselling protocol with a deliberate delay. Never order it casually.
> - **Insurance.** Australia has **legislated a ban on life insurers using adverse genetic test results**, replacing the earlier industry moratorium — the legislation covers not only test results but information about whether a test was taken or recommended, and extends to relatives' results. **The precise commencement date is not asserted here** (retrieved sources gave conflicting dates and it was not established to the three-source standard); confirm the current position before advising a patient, because it is a genuine and reasonable reason patients decline testing.
> - **Reproductive implications** — carrier status affects reproductive choices and may warrant preconception or prenatal counselling.

**Normal/abnormal:** Expressed as a **risk category** (population / moderately increased / high risk) that determines surveillance intensity and eligibility for genetic testing — not as a number.

**Alt:** Validated risk assessment tools and referral criteria used by familial cancer services; formal **genetic counselling**; **genetic and molecular testing** (0.15); risk-based surveillance without testing; risk-reducing surgery and chemoprevention in defined high-risk groups. See [[10_11b_Oncology_-_Genetic_Cancer_Predisposition_Syndromes]].

## 0.15 Genetics and Molecular Testing

**D:** A spectrum of laboratory tests, not one test. **Karyotype** (whole-chromosome, detects aneuploidy and large structural rearrangements). **Chromosomal microarray** (detects submicroscopic copy-number changes; first-line for developmental delay and congenital anomaly). **FISH** (targeted, rapid, for a known locus). **Targeted single-gene or variant testing**. **Gene panels**. **Exome and genome sequencing**. Separately, **somatic (tumour) molecular testing**, which examines the cancer rather than the person.

**Ind:** Diagnosis of a suspected genetic condition; developmental delay, intellectual disability, dysmorphism or multiple congenital anomalies; a family history identified on risk assessment (0.14); carrier and preconception screening; prenatal diagnosis; and, in oncology, **selecting targeted therapy** on the tumour's molecular profile.

**Role:** Confirms a diagnosis, enables **cascade testing** of relatives, guides surveillance and reproductive decisions, and in cancer increasingly determines treatment.

> [!danger] **Germline and somatic testing answer different questions and must not be confused.**
> **Germline** testing examines the **inherited** genome — the result applies to the patient for life and to their relatives. **Somatic** testing examines **acquired changes in the tumour** — it guides treatment for that cancer and is generally not heritable. A somatic panel can, however, **incidentally reveal a germline variant**, which then requires germline confirmation and genetic counselling. Reporting a tumour result as an inherited risk, or vice versa, misdirects an entire family.

> [!warning] **The variant of uncertain significance (VUS) is the commonest difficult result.** A VUS is **not** a positive result and **must not** drive surgery, surveillance changes or reassurance. It may be reclassified — in either direction — as evidence accumulates, which is why patients under specialist genetic follow-up are periodically re-contacted. **Acting on a VUS is a recognised source of harm**, and it is more frequent in people of non-European ancestry because reference databases are less representative.

> [!danger] **Do not ignore**
> - **A negative result rarely means "no genetic condition."** It means the variants tested for were not found. Coverage differs enormously between a targeted test, a panel and a genome, and the family history still stands.
> - **Consent must cover incidental and secondary findings** before the sample is taken, not after the report arrives.
> - **Direct-to-consumer testing is not clinical testing.** Results carry significant false-positive and false-negative rates and require confirmation in an accredited diagnostic laboratory before anything is acted on — a genuinely common presentation in general practice.
> - **Turnaround time varies from days (FISH, QF-PCR) to months (exome/genome)** and must be matched to the clinical urgency — an urgent prenatal or acutely unwell neonatal question needs a rapid test, not a comprehensive one.
> - **Funding.** Medicare covers some tests under specific criteria; many are self-funded or restricted to specialist request. Check before promising a patient a test.

**Normal/abnormal:** Variants are reported on the standard five-tier scale — **pathogenic, likely pathogenic, variant of uncertain significance, likely benign, benign** — with an interpretive report. **The report's interpretation, not the raw variant, is the clinical result.**

**Alt:** Clinical diagnosis on phenotype alone; biochemical and enzyme testing for metabolic disease; imaging and functional studies; family-history-based surveillance without testing; specialist referral to clinical genetics.

## 0.16 Pharmacogenomic Assessment

**D:** Testing for inherited variation that alters drug response — either **pharmacokinetic** (how the drug is metabolised, mainly cytochrome P450 and specific enzymes) or **immunological** (HLA alleles that predispose to severe hypersensitivity).

**Ind:** **Before specific drugs where a defined test prevents a defined severe harm** — this is where the evidence is strongest and where an intern will actually encounter it. Also: unexplained toxicity at standard doses, or repeated non-response.

**Role:** A small number of pharmacogenomic tests are established, mandated-in-practice and genuinely life-saving. Broad "pharmacogenomic panels" marketed for psychotropic prescribing are a much weaker proposition and should not be confused with them.

> [!danger] **The four an intern must know**
> - **HLA-B\*57:01 before abacavir.** Strongly associated with abacavir hypersensitivity. Sources report a **negative predictive value of ~100%** — testing effectively excludes the reaction, which is why it became standard of care. **Never start abacavir without it.**
> - **HLA-B\*15:02 before carbamazepine** in patients of **Asian ancestry** — strongly associated with carbamazepine-induced **Stevens-Johnson syndrome and toxic epidermal necrolysis**. The allele is most prevalent in Oceanian, East Asian and South/Central Asian populations; the association (and hence the testing recommendation) is ancestry-specific.
> - **TPMT and NUDT15 before thiopurines** (azathioprine, mercaptopurine). Sources state that **nearly all patients with two inactive TPMT alleles suffer severe or life-threatening myelosuppression at standard doses**, and 30–60% of those with intermediate activity have moderate-to-severe myelosuppression. **NUDT15** deficiency is much commoner in **East Asian, South Asian and Native American** populations, and is the reason TPMT testing alone is insufficient in those groups.
> - **DPYD before fluoropyrimidines** (5-fluorouracil, capecitabine) — DPD deficiency causes severe, sometimes fatal, toxicity, and pre-treatment genotyping is increasingly standard oncology practice.
> - Also worth knowing: **HLA-B\*58:01 and allopurinol** hypersensitivity (see 0.5).

> [!warning] **A normal genotype does not license inattention.** TPMT/NUDT15 testing **does not replace FBC monitoring** on thiopurines — myelosuppression occurs in patients with normal genotypes, from other mechanisms and from interactions (notably **allopurinol with azathioprine**, which is a dangerous and well-described combination). Genotype adjusts the starting dose; monitoring still catches what genotype misses.

> [!danger] **Do not ignore**
> - **Ancestry determines which test is worth doing**, and self-reported ancestry is imperfect. Where the population risk is meaningful, test rather than assume.
> - **A hypersensitivity reaction to abacavir means the drug is never rechallenged** — rechallenge can be fatal, regardless of genotype.
> - **Document the result prominently as an allergy/alert**, not buried in a pathology result. A pharmacogenomic finding that nobody sees at the next prescribing decision has achieved nothing.
> - **Broad commercial pharmacogenomic panels for antidepressant selection have far weaker evidence** than the drug-specific tests above and are not a substitute for clinical review, adherence assessment and adequate trial duration.

**Normal/abnormal:** Reported as **allele present/absent** for HLA tests, and as a **metaboliser phenotype** (poor / intermediate / normal / rapid / ultrarapid) for enzyme genes, usually with an explicit dosing recommendation. **Specific dose-reduction percentages are not reproduced here** — they are gene-, variant- and drug-specific and must be taken from the report and the current guideline, not from memory.

**Alt:** **Phenotypic enzyme activity assays** (e.g. TPMT enzyme activity, an alternative to genotyping with different failure modes — recent transfusion invalidates it); **therapeutic drug monitoring**; **thiopurine metabolite levels** (6-TGN, 6-MMP); careful clinical monitoring with dose titration; choosing a different drug altogether.

---

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
