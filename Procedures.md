---
block: Shared — Procedures
source: created 2026-09-01 as the destination for procedure content currently split across five files; EMPTY pending approval by destination
---

# Procedures

> [!danger] This file is a scaffold. No content has been moved into it.
> It exists so the destination is named and recorded. Everything below is a manifest of what is
> **proposed** to arrive, not what is here.

> [!note] Why this file exists
> Procedures are currently in **five files**, and the axis has no home:
> `GER8_Procedure_Addendum` — its own scope line names procedures (*"gastroscopy · oesophagoscopy ·
> gastrografin…"*), so **its parent is this file, not `Examination.md`** ·
> `NEW_Exam_Manoeuvres_and_Procedures` **Part 2** — cardioversion, ICD, carotid endarterectomy,
> external fixation (**Part 1 is 15 MSK examination tests and belongs with `Examination.md`**) ·
> `Examination.md §1.8 Pleural Aspiration` and `§1.11 Abdominal Paracentesis` — procedures currently
> inside the examination file ·
> `Emergency F0-4 §0.7 Mechanical Ventilation`, `§0.8 Procedural Sedation`, `§0.11 Fascia Iliaca Block` ·
> `Anaes 03a §0.2 Airway Adjuncts`, `§0.3 Regional / Local Anaesthesia` ·
> `Renal H1 §0.6 Renal Biopsy`, `H2 §0.5 Catheters` · `Psychiatry 14_05d Electroconvulsive Therapy`.
>
> **Known duplicate pairs to place side by side, never merge:**
> `GER8 §0.3 Gastrografin` ↔ `GI NEW_Inv_Gastro §0.36 Gastrografin` ·
> `GER8 §0.5 Arthrocentesis` ↔ `MSK L1 §0.6 Joint Aspiration` ↔ `Investigation-Interpretation §1.15`.

---

# 1 Procedures merged in from five sources (2026-09-01)

> [!info] **C2 and AXIS-2 executed. This file was created empty under A2 with a manifest; this is that manifest, filled.**
> The procedure axis was *"genuinely fragmented across five files and needs building", unlike the drug
> axis, which is left distributed. **`GER8` gets its real parent here** instead of the `GER` prefix that
> filed it under Geriatrics.
>
> Every heading is verbatim and unrenumbered under a `SOURCE:` divider naming its origin file.
> **Nothing merged.** Two three-way duplications carry `CF-PAIR` markers.

<!-- ===== SOURCE: NEW_Exam_Manoeuvres_and_Procedures.md ===== -->
*Moved here from `NEW_Exam_Manoeuvres_and_Procedures.md` on 2026-09-01. Verbatim and unrenumbered.*

## 0.16 Cardioversion (Synchronised DC Cardioversion)

**D:** Delivery of a **synchronised** direct-current shock — timed to the **R wave** to avoid the vulnerable T-wave period — to terminate a tachyarrhythmia and restore sinus rhythm. Performed under **sedation or general anaesthesia** in the elective setting. **Chemical (pharmacological) cardioversion** is the drug alternative.

**Ind:** **Emergency:** any tachyarrhythmia with **adverse features** — shock, syncope, myocardial ischaemia, or heart failure. **Elective:** symptomatic persistent atrial fibrillation or flutter where a rhythm-control strategy is chosen; some other stable SVTs and VT.

**Role:** Restores sinus rhythm immediately where drugs would be too slow or have failed.

> [!danger] **Synchronisation is not a detail — it is the safety mechanism.**
> An **unsynchronised** shock delivered on the T wave can induce **ventricular fibrillation** ("R-on-T"). **Press the SYNC button and confirm the machine is marking the R waves** before every shock. **The exception is pulseless VF/pulseless VT, which is defibrillation — unsynchronised, and part of the cardiac arrest algorithm, not this procedure.** Also note that the machine **may drop out of sync mode after each shock** on many defibrillators; **re-check before the next one.**

> [!danger] **Anticoagulation and the timing rules — the highest-yield content**
> - **Atrial fibrillation of >48 hours' duration, or of uncertain duration:** cardioversion is **deferred until at least 3 weeks of therapeutic anticoagulation**, **or** a **transoesophageal echocardiogram** excludes left atrial appendage thrombus (sources give TOE sensitivity 93–100% and specificity 99–100% for excluding thrombus, and describe TOE-guided and conventional strategies as **equally effective**).
> - **After cardioversion, anticoagulate for at least 4 weeks regardless of the pre-procedure strategy** — because of **atrial stunning**. The atrium does not contract effectively for days to weeks after rhythm is restored, and sources note thromboembolic risk is **highest in the first 72 hours**, with most events within 10 days but some as late as 4 weeks. **This is the step most often forgotten, and it causes strokes.**
> - **Long-term anticoagulation is decided by stroke risk (CHA₂DS₂-VA/VASc), not by whether sinus rhythm was restored.** A successful cardioversion does not license stopping anticoagulation.
> - **A haemodynamically unstable patient is cardioverted immediately** — the arrhythmia is killing them now, and the thromboembolic risk is accepted.

> [!warning] **Practical points**
> - **Confirm fasting, consent, IV access, monitoring, oxygen and airway equipment**, and that someone competent in airway management is present — the sedation is usually the riskiest part.
> - **Check and correct potassium and magnesium** beforehand; electrolyte disturbance both promotes arrhythmia and reduces cardioversion success.
> - **Digoxin toxicity is a relative contraindication** — cardioversion in that setting can precipitate malignant ventricular arrhythmia.
> - **Pad position and energy**: use the manufacturer's recommended pad placement, and note that **flutter and SVT generally cardiovert at lower energies than AF**. **Specific energy settings are not stated here** — they are device-specific and set by the local resuscitation guideline, and quoting one number across all machines would be wrong.
> - Anticipate **post-shock bradycardia or asystole**, particularly in sinus node disease — have pacing available.
> - See [[01_Cardiovascular]].

**Alt:** **Chemical cardioversion** (agent choice depends on structural heart disease and is specialist-guided); **rate control** as an alternative strategy, which is non-inferior for many patients; **catheter ablation**; vagal manoeuvres and adenosine for regular narrow-complex SVT; treating the underlying precipitant (sepsis, thyrotoxicosis, alcohol, electrolytes, pulmonary embolism), without which the arrhythmia usually recurs.

## 0.17 Implantable Cardioverter Defibrillator (ICD)

**D:** An implanted device with one or more transvenous leads (or a **subcutaneous** lead in the S-ICD) that continuously monitors the rhythm and treats ventricular arrhythmia by **anti-tachycardia pacing** or an internal **shock**. Most devices also provide **bradycardia pacing**, and a **CRT-D** adds biventricular pacing for cardiac resynchronisation.

**Ind:** **Secondary prevention** — survivors of cardiac arrest from VF or haemodynamically unstable VT without a reversible cause, and sustained VT with structural heart disease. **Primary prevention** — sources agree on the core criteria: **LVEF ≤35% with NYHA class II–III symptoms on optimal guideline-directed medical therapy**, at least **40 days after myocardial infarction** and at least **90 days after revascularisation**, with an expected **meaningful survival of more than a year**. Also inherited arrhythmia syndromes (long QT, Brugada, ARVC, hypertrophic cardiomyopathy) on specialist risk assessment.

**Role:** It **prevents sudden arrhythmic death**. It does **not** treat heart failure, improve symptoms, or slow disease progression — and the distinction is central to counselling.

> [!danger] **The waiting periods are not bureaucratic delay — they exist because ejection fraction recovers.**
> Ventricular function frequently improves in the weeks after an infarct or revascularisation and after optimising medical therapy. Implanting early exposes patients to device complications without benefit, and trials showed no mortality advantage to early implantation. **Optimise medical therapy and reassess the ejection fraction before deciding.**

> [!danger] **An ICD shock is not a benign event, and neither is a device at the end of life**
> - **A shock is painful and frightening.** Recurrent shocks cause significant **anxiety, PTSD and depression**, and patients need to know this before implantation.
> - **An "electrical storm"** (three or more appropriate shocks in 24 hours) is an emergency requiring admission, antiarrhythmic therapy, sedation and a search for the precipitant (ischaemia, electrolytes, decompensated heart failure, drugs).
> - **Inappropriate shocks** — from atrial fibrillation with rapid conduction, supraventricular tachycardia, lead fracture or oversensing — are common and are a device problem, not an arrhythmia problem. Interrogate the device.
> - **Deactivation at end of life is essential care and is routinely neglected.** A dying patient being repeatedly shocked is a preventable harm. **Discuss deactivation as part of advance care planning**, and know that a **magnet placed over the device suspends shock therapy** as an immediate measure while the device team is contacted. See [[10_11c_Oncology_-_Palliative_Care_Prescribing]].

> [!warning] **Practical points an intern will actually meet**
> - **Driving restrictions apply after implantation and after any shock**, and differ for private and commercial licences. Tell the patient before they leave.
> - **MRI**: many modern systems are conditional, but this must be confirmed with the device card and the cardiac device service before any scan. Never assume.
> - **Diathermy in surgery** requires device management; involve the device team preoperatively.
> - **Device infection is serious** — a red, tender or discharging pocket, or bacteraemia (especially *Staphylococcus aureus*) in a patient with a device, requires urgent cardiology involvement, and usually means **system extraction**. Do not treat it as a superficial wound infection.
> - **Complications**: pneumothorax, haematoma, lead displacement and fracture, tricuspid regurgitation, venous occlusion, and battery depletion requiring generator change.
> - See [[01_Cardiovascular]].

**Alt:** **Optimal medical therapy for heart failure** — which itself reduces sudden death and must be maximised first; **wearable cardioverter defibrillator** during the waiting period in selected patients; **subcutaneous ICD** where pacing is not required; catheter ablation of VT; **CRT** where there is a broad QRS; and — a legitimate, informed choice — **declining a device**.

## 0.18 Carotid Endarterectomy

**D:** Surgical removal of atherosclerotic plaque from the **carotid bifurcation and proximal internal carotid artery**, usually with patch closure, performed under general or local/regional anaesthesia.

**Ind:** **Symptomatic** carotid stenosis — a **TIA, amaurosis fugax or non-disabling stroke** in the territory of the stenosed artery. Sources describe the **NASCET** evidence: surgery in addition to medical therapy significantly reduces ipsilateral and disabling stroke in **70–99%** symptomatic stenosis, with benefit also demonstrated in symptomatic moderate stenosis in the 50–69% range. **Asymptomatic** stenosis is a much weaker and increasingly contested indication, given how much better modern medical therapy has become.

**Role:** Secondary prevention of stroke — **it prevents the next stroke; it does not treat the one that has happened.**

> [!danger] **TIME IS THE WHOLE POINT: the risk of recurrent stroke is highest in the first days after the index event.**
> Benefit from endarterectomy falls sharply the longer surgery is delayed, and the standard target is **within 2 weeks** of the symptomatic event. **A TIA is a medical emergency**, not an outpatient referral: it needs immediate antiplatelet therapy, urgent carotid imaging, risk factor treatment and urgent vascular surgical assessment. Treating a TIA as reassuring — because the symptoms have resolved — is one of the most damaging errors in general medicine. See [[04_Neurology]].

> [!danger] **The side must match the symptoms.**
> Only a stenosis **ipsilateral to the symptomatic hemisphere or eye** is relevant. Right-hand weakness and expressive dysphasia means the **left** carotid; **amaurosis fugax means the carotid on the same side as the affected eye**. Operating on the wrong side does harm and no good, and a contralateral asymptomatic stenosis is a different (and much weaker) indication.

> [!warning] **The operation itself carries a stroke risk, which is why patient selection matters.** The benefit is the difference between the natural history and the peri-operative risk, so the procedure is only worthwhile in centres with audited low complication rates and in patients whose expected benefit exceeds it. **Degree of stenosis is measured by a defined method (the NASCET criteria), and different measurement conventions give different percentages** for the same artery — which matters when comparing an ultrasound report with an angiographic one.

> [!danger] **Do not ignore**
> - **Medical therapy is not optional and is not second-best**: antiplatelet therapy, high-intensity statin, blood pressure control, diabetes management, and **smoking cessation** — which is the single most effective thing the patient can do.
> - **Post-operative complications to look for**: **stroke**, **neck haematoma** (which can rapidly obstruct the airway and is a surgical emergency — do not wait), **cranial nerve injury** (hypoglossal, recurrent laryngeal, marginal mandibular — causing tongue deviation, hoarseness or facial asymmetry), **hyperperfusion syndrome** (severe headache, seizures, haemorrhage — driven by hypertension), myocardial infarction, and labile blood pressure from carotid sinus manipulation.
> - **A new neurological deficit after carotid surgery is an emergency** requiring immediate surgical review.
> - **Atrial fibrillation is a competing cause of stroke** and must be looked for; finding a carotid stenosis does not establish it as the mechanism.

**Alt:** **Carotid artery stenting** (an option in selected patients — anatomy, age, surgical risk and prior neck radiotherapy influence the choice); **best medical therapy alone**, which is the comparator and is increasingly favoured in asymptomatic disease; and, for the underlying vascular disease, comprehensive risk factor modification.

## 0.19 External Fixation

**D:** Stabilisation of a fracture with **pins or wires inserted into bone away from the injury zone**, connected to an external frame. Configurations range from a simple **spanning frame** across a joint to circular (Ilizarov) frames for deformity correction and bone transport.

**Ind:** **Damage control orthopaedics** in the physiologically unstable polytrauma patient; **open fractures** with significant soft tissue injury or contamination; fractures with **compartment syndrome** or vascular injury requiring access; **peri-articular fractures with severe swelling**, where definitive fixation must wait for the soft tissues; unstable **pelvic ring** injuries; infected non-union; limb lengthening and deformity correction; some fractures in the presence of burns.

**Role:** **Fast, minimally invasive, temporary skeletal stability** — controlling length, alignment and rotation, reducing bleeding and pain, and allowing the soft tissues (and the patient) to recover before definitive surgery.

> [!info] **Damage control orthopaedics — the concept behind the frame**
> The decision is driven by the **patient's physiology, not the fracture**. Sources describe the indication as relating to **haemodynamic instability, the severity of soft tissue injury, and high-energy open fractures needing repeated procedures**. Prolonged definitive surgery in a patient who is cold, coagulopathic and acidotic is a **"second hit"** that can be fatal. **Stabilise quickly, resuscitate, and return for definitive fixation when the patient can tolerate it** — "early total care" is for the physiologically stable patient.

> [!danger] **The soft tissues determine the timing of everything.**
> A closed tibial plateau or pilon fracture with severe swelling, fracture blisters or a compromised skin envelope must **not** have definitive internal fixation acutely — doing so causes wound breakdown, infection and catastrophic outcomes. A spanning external fixator holds the limb out to length while the swelling settles, typically over one to two weeks, and the wrinkle sign returns.

> [!danger] **Do not ignore**
> - **An open fracture needs the whole bundle, not just a frame**: **early intravenous antibiotics** (the single most important intervention, and the earlier the better), **tetanus prophylaxis**, photograph and cover the wound with a saline-soaked dressing, splint, and **urgent surgical debridement**. Repeated exposure of the wound on the ward increases infection.
> - **Compartment syndrome must be actively excluded and re-checked** — pain out of proportion, pain on passive stretch, and increasing analgesia requirement. **Pulses are present in compartment syndrome**; waiting for pulselessness means waiting for muscle death. See [[11_01_Ortho_-_Orthopaedic_Emergencies]].
> - **Pin site care is a daily nursing and medical responsibility.** **Pin site infection is the commonest complication**; look for redness, discharge and pin loosening at every review, and escalate rather than adding oral antibiotics indefinitely — a loose or infected pin needs surgical attention.
> - **Pin placement is not arbitrary**: sources note that although anatomical safe zones exist, **neurovascular structures are at risk** in the severely traumatised limb, and vascular injury after external fixation is a described complication.
> - **Timing of conversion to internal fixation matters** — converting through an infected pin tract risks deep infection and osteomyelitis; sources describe unicortical and carefully sited frames designed specifically to permit safe early conversion to intramedullary nailing.
> - Other complications: **malunion and non-union, joint stiffness, pin loosening, neurovascular injury, and the substantial burden the frame places on the patient's daily life** — dressing, sleeping, driving and psychological adjustment all need support.
> - See [[11_09b_Ortho_-_Trauma]] and [[11_08c_Ortho_-_Fracture_Types_and_Pathological_Fractures]].

**Alt:** **Definitive internal fixation** (intramedullary nail, plate and screws) where the patient and soft tissues allow; **plaster or splint immobilisation**; **traction** as a temporising measure; **pelvic binder** as the immediate step in a pelvic ring injury before any frame; amputation in a non-salvageable limb, which is sometimes the better reconstruction.

---

<!-- ===== SOURCE: GER8_Procedure_Addendum.md ===== -->
*Moved here from `GER8_Procedure_Addendum.md` on 2026-09-01. Verbatim and unrenumbered.*

## 0.1 Procedural Safety

> [!danger] The checklist exists because the errors happen
> **THE NEVER EVENTS: WRONG PATIENT · WRONG SITE · WRONG PROCEDURE · RETAINED FOREIGN OBJECT.**
> **These are called never events because they are entirely preventable by a system that is followed every time — and they occur when the checklist is treated as paperwork.**
> **THE SURGICAL SAFETY CHECKLIST / PROCEDURAL TIME-OUT, before every procedure including ward-based ones:**
> **· Correct PATIENT, identified actively.**
> **· Correct SITE, and MARKED before the patient is anaesthetised or draped — by the operator, with the patient participating.**
> **· Correct PROCEDURE, and correct consent.**
> **· ALLERGIES.**
> **· ANTICOAGULATION and antiplatelet status.**
> **· ANTIBIOTIC prophylaxis given if indicated.**
> **· Equipment available and working, and imaging displayed.**
> **· Anticipated problems stated aloud.**
> **The value is not the list itself — it is that it creates a moment where anyone in the room can speak up.** Cross-refer [[EBM1]] 0.6.

> [!warning] Consent, and knowing your limits
> **CONSENT FOR A PROCEDURE: the indication · what it involves · the ALTERNATIVES, including doing nothing · the MATERIAL RISKS (those a reasonable person in this patient's position would want to know, and those this particular patient would) · WHO will perform it, including whether a trainee will and under what supervision · and what happens afterwards.** Cross-refer [[A10]] 0.2.
> **AND THE RULE THAT MATTERS MOST FOR AN INTERN: DO NOT PERFORM A PROCEDURE YOU HAVE NOT BEEN TRAINED AND ASSESSED TO DO, WITHOUT SUPERVISION.**
> **"See one, do one, teach one" is not a standard of care. The pressure to be useful, and the reluctance to admit you have not done one before, are exactly how patients are harmed and how juniors end up in situations they cannot manage.** **Saying "I haven't done one of these — can you watch me?" is a mark of competence, not of weakness.**

> [!danger] Sedation and local anaesthetic — the two things that kill in minor procedures
> **PROCEDURAL SEDATION EXISTS ON A CONTINUUM, and the commonest cause of harm is REACHING A DEEPER LEVEL THAN INTENDED — losing airway reflexes in a patient who was meant to be lightly sedated, in a room set up for a minor procedure.**
> **REQUIREMENTS: appropriate FASTING · a trained person whose ONLY job is the sedation and the airway · continuous monitoring including oximetry and, where used, CAPNOGRAPHY (which detects hypoventilation well before desaturation) · oxygen, suction and airway equipment immediately available · REVERSAL AGENTS available (naloxone, flumazenil) · and recovery monitoring.** Cross-refer [[AN1]] 0.2.
> **LOCAL ANAESTHETIC SYSTEMIC TOXICITY (LAST) — from exceeding the maximum dose or from inadvertent intravascular injection.**
> **THE PROGRESSION: perioral TINGLING and numbness · a METALLIC TASTE · TINNITUS · visual disturbance · agitation and confusion · then SEIZURES · then cardiovascular collapse and cardiac arrest, which is refractory to standard resuscitation.**
> **THE TREATMENT IS INTRAVENOUS LIPID EMULSION ("INTRALIPID"), alongside standard resuscitation and prolonged CPR.**
> **KNOW THE MAXIMUM DOSE FOR THE AGENT AND THE PATIENT'S WEIGHT BEFORE YOU DRAW IT UP, ASPIRATE BEFORE INJECTING, AND KNOW WHERE THE LIPID EMULSION IS KEPT IN YOUR DEPARTMENT.** `UNVERIFIED — maximum doses and the lipid emulsion regimen.`

---

## 0.2 Gastroscopy and Oesophagoscopy

> [!tip] What they are for
> **GASTROSCOPY (oesophagogastroduodenoscopy) — flexible endoscopic examination of the oesophagus, stomach and duodenum, both diagnostic and therapeutic.**
> **DIAGNOSTIC INDICATIONS: dyspepsia with ALARM FEATURES · DYSPHAGIA · upper gastrointestinal BLEEDING · unexplained IRON DEFICIENCY ANAEMIA · suspected malignancy · DUODENAL BIOPSY for coeliac disease (which must be taken while the patient is still eating gluten — cross-refer [[C5]] 0.4) · and variceal surveillance in cirrhosis.**
> **THERAPEUTIC: haemostasis for bleeding ulcers and varices (banding, clips, injection) · dilatation of strictures · stenting · PEG insertion · and foreign body retrieval.** Cross-refer [[C4]] and [[C6]] 0.1.
> **OESOPHAGOSCOPY — may be flexible, or RIGID under general anaesthesia.**
> **RIGID oesophagoscopy is an ENT and upper gastrointestinal surgical procedure, and its particular role is IMPACTED FOREIGN BODIES — especially SHARP objects, food boluses with an underlying stricture, and BUTTON BATTERIES, where a secure airway and a large working channel matter.** Cross-refer [[F3]] 0.2 and [[A8]].

> [!danger] A patient in pain after an endoscopy has a complication until proven otherwise
> **THE COMPLICATIONS, in order of frequency:**
> **· SEDATION-RELATED CARDIORESPIRATORY EVENTS — the commonest, and the reason for the monitoring described in 0.1.**
> **· ASPIRATION — particularly in emergency endoscopy for haematemesis, where the stomach is full of blood. This is why some upper GI bleeds are intubated first.**
> **· BLEEDING — after biopsy, polypectomy or therapeutic intervention.**
> **· PERFORATION — uncommon but serious. Risk is higher with THERAPEUTIC procedures, DILATATION, rigid instruments, and in a diseased or radiated oesophagus.**
> **RECOGNISING PERFORATION: PAIN — cervical, chest, back or abdominal, and often severe and out of proportion · fever and tachycardia · SURGICAL EMPHYSEMA in the neck (feel for it) · pleural effusion · and rapid deterioration into mediastinitis or peritonitis.**
> **OESOPHAGEAL PERFORATION HAS HIGH MORTALITY AND THE OUTCOME DEPENDS ON HOW QUICKLY IT IS RECOGNISED.**
> **THE RULE: normal discomfort after gastroscopy is mild and settles. SIGNIFICANT OR PERSISTENT PAIN, FEVER OR TACHYCARDIA AFTER AN UPPER ENDOSCOPY IS A PERFORATION UNTIL IMAGING SAYS OTHERWISE — escalate rather than prescribing analgesia and reviewing later.**
> **AND THE IMAGING POINT THAT CONNECTS TO THE NEXT SECTION: INVESTIGATE A SUSPECTED PERFORATION WITH WATER-SOLUBLE CONTRAST, NEVER BARIUM.** See 0.3.

---

## 0.3 Gastrografin and Contrast Studies
`CF-PAIR` **THREE-WAY. `GI_merged.md §0.36 Gastrografin (Water-Soluble Contrast Study)` covers the same study — the duplication you flagged as `M-18`. Both kept in full, NOT reconciled.**

> [!danger] Barium versus water-soluble contrast — the decision rests on one question
> **THE QUESTION: IS THERE ANY POSSIBILITY OF A PERFORATION OR LEAK?**
> **· BARIUM gives superior mucosal detail and is the better diagnostic agent — BUT IF IT LEAKS OUTSIDE THE GASTROINTESTINAL LUMEN IT CAUSES SEVERE, PERSISTENT CHEMICAL MEDIASTINITIS OR PERITONITIS with dense fibrosis and granuloma formation, carrying high morbidity and mortality.**
> **· WATER-SOLUBLE CONTRAST (of which gastrografin is the archetype) is ABSORBED AND EXCRETED if it leaks, causing far less harm.**
> **THEREFORE: SUSPECTED PERFORATION, ANASTOMOTIC LEAK, POST-OPERATIVE ASSESSMENT, OR ANY PATIENT WHO MAY PROCEED TO SURGERY → WATER-SOLUBLE CONTRAST.**
> **This is the single most important principle in contrast selection and it is examinable.**

> [!danger] But gastrografin is hyperosmolar — and aspirating it can be fatal
> **GASTROGRAFIN IS A HIGH-OSMOLAR IONIC IODINATED AGENT, and its osmolarity creates two distinct dangers:**
> **1. ASPIRATION CAUSES SEVERE, POTENTIALLY FATAL PULMONARY OEDEMA AND CHEMICAL PNEUMONITIS.** **The hyperosmolar contrast draws large volumes of fluid into the alveoli.**
> **SO GASTROGRAFIN MUST NOT BE USED WHERE THERE IS AN ASPIRATION RISK — impaired swallow, reduced consciousness, suspected tracheo-oesophageal fistula, or high oesophageal obstruction.**
> **IN THOSE PATIENTS, A LOW-OSMOLAR NON-IONIC WATER-SOLUBLE AGENT IS USED INSTEAD — it retains the safety-if-it-leaks advantage without the pulmonary danger.**
> **"Water-soluble contrast" is therefore not one thing, and specifying which one matters when the patient cannot protect their airway.**
> **2. FLUID SHIFTS INTO THE BOWEL LUMEN — which can cause significant hypovolaemia and electrolyte disturbance in NEONATES, small children and dehydrated patients.** **Adequate hydration beforehand matters.**

> [!tip] The gastrografin challenge in adhesive small bowel obstruction
> **A genuinely elegant use of the hyperosmolarity: in ADHESIVE SMALL BOWEL OBSTRUCTION without signs of strangulation, gastrografin is administered and an abdominal radiograph taken at a defined interval.**
> **IT IS BOTH DIAGNOSTIC AND THERAPEUTIC:**
> **· DIAGNOSTIC — CONTRAST REACHING THE COLON within the defined time PREDICTS RESOLUTION WITHOUT SURGERY with good accuracy, and failure to reach the colon predicts the need for operation.** **It therefore triages who can be managed conservatively and shortens the period of watchful waiting.**
> **· THERAPEUTIC — the osmotic draw of fluid into the lumen reduces bowel wall oedema and increases the pressure gradient across the obstruction, and it appears to increase the rate of non-operative resolution and reduce length of stay.**
> **THE CAVEAT: it is for ADHESIVE obstruction WITHOUT features of strangulation, ischaemia or peritonism.** **A patient with signs of strangulation goes to theatre, not to radiology.** Cross-refer [[C5]] 0.3.
> **Water-soluble contrast enemas also have a therapeutic role in MECONIUM ILEUS.** Cross-refer [[M5]] 0.1.

> [!warning] Iodinated contrast generally — three persistent myths
> **1. "SHELLFISH ALLERGY" IS NOT A CONTRAINDICATION TO IODINATED CONTRAST.**
> **Shellfish allergy is to tropomyosin, a muscle protein — NOT to iodine. There is no cross-reactivity, and iodine itself is not an allergen (it is an essential element present throughout the body).** **The belief persists widely and delays necessary imaging.** **A previous reaction TO CONTRAST is what matters.**
> **2. CONTRAST-ASSOCIATED ACUTE KIDNEY INJURY HAS BEEN SUBSTANTIALLY OVER-ESTIMATED.**
> **Much of the historical association reflected confounding — the patients receiving contrast were sicker. The attributable risk from modern intravenous contrast is considerably lower than once believed, and N-acetylcysteine and bicarbonate protocols are not supported.**
> **THE CLINICAL CONSEQUENCE: DO NOT WITHHOLD A CLINICALLY INDICATED CONTRAST CT — for a suspected pulmonary embolism, aortic dissection or intra-abdominal catastrophe — out of exaggerated renal concern.** **The missed diagnosis is the greater harm.** Ensure hydration and review nephrotoxic drugs. Cross-refer [[H3]] 0.2.
> **3. METFORMIN — the issue is not the contrast harming the kidney directly but the risk of metformin accumulation if an AKI develops.** **Practice has become far less restrictive and depends on baseline renal function.** `UNVERIFIED — current withholding recommendations.`
> **Genuine considerations: previous CONTRAST reaction (the relevant history), and iodinated contrast precipitating THYROTOXICOSIS or interfering with subsequent radioiodine imaging and treatment.** Cross-refer [[I1]] 0.3.

---

## 0.4 Percutaneous Transhepatic Cholangiography

> [!tip] From above, when the approach from below has failed
> **PTC — percutaneous puncture of an intrahepatic bile duct under ultrasound and fluoroscopic guidance, with contrast injected to opacify the biliary tree, usually followed by PERCUTANEOUS TRANSHEPATIC BILIARY DRAINAGE (an external or internal-external drain) or stenting.**
> **THE ORIENTING DISTINCTION: ERCP approaches the biliary tree RETROGRADE FROM BELOW, endoscopically through the ampulla. PTC approaches it ANTEGRADE FROM ABOVE, percutaneously through the liver.**
> **PTC IS THE ANSWER WHEN ERCP HAS FAILED OR IS IMPOSSIBLE:**
> **· ALTERED ANATOMY — Roux-en-Y reconstruction, gastric bypass, previous gastrectomy — where the ampulla cannot be reached endoscopically.**
> **· HILAR OR PROXIMAL obstruction, where drainage from below may not reach the obstructed segments.**
> **· Duodenal obstruction preventing endoscopic access.**
> **· Failed cannulation at ERCP.**
> **It generally requires DILATED intrahepatic ducts to provide a target.** Cross-refer [[C7]] and [[C3]] 0.2.

> [!danger] The complications, and haemobilia
> **· BLEEDING — the liver is vascular and the needle traverses it. Coagulation must be checked and corrected, and anticoagulants and antiplatelets managed beforehand.**
> **HAEMOBILIA — bleeding into the biliary tree — presents as the classic triad of BILIARY COLIC, JAUNDICE AND UPPER GASTROINTESTINAL BLEEDING (melaena or haematemesis).** **It is worth recognising because a gastrointestinal bleed after a liver or biliary procedure is easily attributed to something else, and the source is not found at gastroscopy unless blood is seen at the ampulla.**
> **· BILIARY SEPSIS AND CHOLANGITIS — instrumenting an OBSTRUCTED, frequently INFECTED biliary system releases organisms into the circulation.** **Antibiotic cover is essential, and post-procedural fever and rigors are cholangitis until proven otherwise.** Cross-refer [[C7]] 0.3.
> **· BILE LEAK and biliary peritonitis.**
> **· PNEUMOTHORAX or haemothorax from a high puncture.**
> **· DRAIN PROBLEMS — dislodgement, blockage, and pericatheter leakage.** **A biliary drain whose output suddenly falls, in a patient who becomes febrile or more jaundiced, is BLOCKED or DISLODGED — that is a clinical deterioration, not a plumbing inconvenience, and it needs urgent review.**
> **· Tumour seeding along the tract in malignant obstruction.**
> **PRACTICAL WARD CARE: record drain output volume and character, secure the drain, know whether it is external or internal-external, and escalate a fall in output, a fever, or increasing pain.**

---

## 0.5 Arthrocentesis
`CF-PAIR` **THREE-WAY, and two of the three now sit in one file. `Investigation-Interpretation §1.15 Joint Aspirate (Synovial Fluid) Analysis` and `Investigation-Interpretation` Part 2 `## 0.6 Joint Aspiration and Synovial Fluid Interpretation` (from `MSK L1`, moved `ac620de`) both cover this. All three kept in full, NOT reconciled — this one is the procedure, the other two are the interpretation.**

> [!danger] You cannot exclude septic arthritis without aspirating the joint
> **THIS IS THE MOST IMPORTANT SINGLE PROCEDURE IN THE ASSESSMENT OF A HOT, SWOLLEN, PAINFUL JOINT.**
> **No combination of history, examination, inflammatory markers or imaging excludes septic arthritis. Untreated, it destroys the joint within days and carries significant mortality.**
> **ASPIRATE BEFORE ANTIBIOTICS where the patient's condition allows — antibiotics reduce culture yield — BUT NEVER DELAY ANTIBIOTICS IN A SEPTIC PATIENT to arrange the tap.** Cross-refer [[L1]] 0.1.
> **WHAT TO SEND, and it must be requested explicitly:**
> **· URGENT GRAM STAIN AND CULTURE.**
> **· CELL COUNT AND DIFFERENTIAL.**
> **· POLARISED LIGHT MICROSCOPY FOR CRYSTALS.**
> **The crystal examination is a separate request and is frequently omitted, and the sample is then unusable for it.**

> [!danger] Crystals do not exclude infection
> **THE CRYSTALS:**
> **· MONOSODIUM URATE (GOUT) — NEEDLE-SHAPED, and NEGATIVELY birefringent (yellow when parallel to the compensator axis).**
> **· CALCIUM PYROPHOSPHATE (pseudogout) — RHOMBOID or rod-shaped, and POSITIVELY birefringent (blue when parallel).**
> **THE CRITICAL POINT: FINDING CRYSTALS DOES NOT EXCLUDE SEPTIC ARTHRITIS.**
> **The two coexist, and a patient with known gout is not protected from infection — indeed a chronically damaged joint is more susceptible.**
> **"IT'S JUST HIS GOUT AGAIN" IN A PATIENT WITH A HOT JOINT AND A FEVER IS A CLASSIC AND DEVASTATING MISSED DIAGNOSIS.** **If the clinical picture is septic, treat as septic while awaiting cultures, regardless of the crystals.** Cross-refer [[L1]] 0.2–0.3.
> **THE APPEARANCE OF THE FLUID also informs: clear straw-coloured (normal or non-inflammatory) · turbid or frankly purulent (inflammatory or septic) · and BLOOD-STAINED (haemarthrosis — trauma, anticoagulation, or a bleeding disorder).**
> **AND FAT GLOBULES IN A BLOODY ASPIRATE (lipohaemarthrosis) INDICATE AN INTRA-ARTICULAR FRACTURE** — marrow fat has entered the joint, and it means imaging for a fracture that may not be obvious on the initial film. **The same finding appears as a fat-fluid level on a horizontal-beam radiograph.** Cross-refer [[L7]] 0.3.

> [!warning] Contraindications and the prosthetic joint
> **· DO NOT PASS A NEEDLE THROUGH OVERLYING CELLULITIS OR INFECTED SKIN — it risks introducing organisms into a joint that may be sterile.** **Use a different approach route through healthy skin, or seek help.**
> **· ANTICOAGULATION AND BLEEDING DISORDERS increase the risk of haemarthrosis — but SUSPECTED SEPTIC ARTHRITIS GENERALLY OVERRIDES this, because the consequence of not diagnosing it is worse. Discuss rather than defer.**
> **· A PROSTHETIC JOINT MUST NOT BE ASPIRATED ON THE WARD.** **Prosthetic joint infection is difficult to diagnose and to treat, contamination of the sample makes interpretation impossible, and introducing organisms into a prosthesis is catastrophic.** **These are aspirated under strict conditions, usually in theatre or radiology, by or in consultation with orthopaedics.**
> **· AND DO NOT INJECT CORTICOSTEROID INTO A JOINT THAT MIGHT BE INFECTED.** Therapeutic aspiration and steroid injection are reasonable in confirmed crystal or inflammatory arthritis — but only once infection is excluded.
> **Technique: strict asepsis, appropriate landmarks, local anaesthetic, avoidance of neurovascular structures — and ULTRASOUND GUIDANCE improves success rates, particularly in small or difficult joints and in obese patients.**

---

## 0.6 Arthroscopy and Joint Procedures

> [!danger] Arthroscopy for degenerative knee disease does not work
> **THIS IS ONE OF THE BEST-DOCUMENTED EXAMPLES IN MEDICINE OF A WIDELY PERFORMED PROCEDURE SHOWN NOT TO WORK, AND IT IS HIGH-YIELD FOR EXAMS AND FOR PRACTICE.**
> **ARTHROSCOPIC PARTIAL MENISCECTOMY, DEBRIDEMENT AND LAVAGE FOR DEGENERATIVE KNEE DISEASE AND FOR ATRAUMATIC DEGENERATIVE MENISCAL TEARS PROVIDE NO MEANINGFUL BENEFIT OVER CONSERVATIVE MANAGEMENT — AND NO BENEFIT OVER SHAM SURGERY IN BLINDED TRIALS.**
> **The sham-controlled trials are the important part: patients improved after the placebo operation as much as after the real one, which established that the apparent benefit was not from the surgery.**
> **It appears on Choosing Wisely lists internationally, and it continues to be performed in significant numbers.**
> **WHY IT MATTERS BEYOND ORTHOPAEDICS: a degenerative meniscal tear is an extremely COMMON incidental MRI finding in middle-aged and older people, including those with no knee pain at all.** **Finding one on a scan does not mean it is the cause of the symptoms — and the sequence "knee pain → MRI → tear found → arthroscopy" is a textbook illustration of how an incidental finding generates an ineffective intervention.**
> **THE EVIDENCE-BASED MANAGEMENT of degenerative knee disease is EXERCISE THERAPY (which has good evidence and is under-prescribed), weight management, analgesia, activity modification — and joint replacement when it is warranted.** Cross-refer [[L5]] 0.4, [[L6]] 0.2 and [[EBM1]] 0.2.

> [!tip] Where arthroscopy IS indicated
> **· TRUE MECHANICAL LOCKING from a displaced bucket-handle meniscal tear — a knee that physically cannot be straightened, which is different from the "giving way" and "catching" that patients often describe.**
> **· ACUTE TRAUMATIC injuries in younger patients.**
> **· LIGAMENT RECONSTRUCTION (anterior cruciate and others).**
> **· Removal of a symptomatic LOOSE BODY.**
> **· SYNOVIAL BIOPSY where tissue diagnosis is needed.**
> **· ARTHROSCOPIC WASHOUT AND DEBRIDEMENT OF SEPTIC ARTHRITIS — a genuine and urgent indication, and quite distinct from washout for degenerative disease.** Cross-refer [[L1]] 0.1.
> **· Shoulder, hip, ankle and wrist arthroscopy for specific structural pathology.**
> **COMPLICATIONS: infection · VENOUS THROMBOEMBOLISM · haemarthrosis · nerve injury · persistent pain and stiffness · and the risks of anaesthesia.**

> [!warning] Joint replacement and prosthetic joint infection
> **JOINT REPLACEMENT is among the most effective operations in medicine for pain and function in end-stage arthritis — the point of the section above is not that surgery does not work, but that the WRONG operation for the WRONG stage of disease does not work.**
> **COMPLICATIONS: VTE (hence thromboprophylaxis) · DISLOCATION · periprosthetic FRACTURE · aseptic LOOSENING · leg length discrepancy · and INFECTION.**
> **PROSTHETIC JOINT INFECTION deserves specific mention because it presents to generalists:**
> **· EARLY infection presents with the expected features of wound infection and systemic illness.**
> **· LATE or CHRONIC infection is INSIDIOUS — persistent or recurrent PAIN in a prosthetic joint, sometimes with no fever, normal or only mildly raised inflammatory markers, and a sinus tract or effusion.**
> **A PERSISTENTLY PAINFUL PROSTHESIS IS INFECTED UNTIL PROVEN OTHERWISE, and attributing it to loosening or to "it just aches" delays a diagnosis that becomes progressively harder to treat.**
> **It requires specialist management — prolonged targeted antibiotics with debridement, and often one- or two-stage revision — and the microbiological diagnosis depends on properly obtained samples, which is why ward aspiration is prohibited.** Cross-refer [[L1]] 0.1 and [[K2]] 0.4.

**Ix:** **A PROCEDURAL TIME-OUT, including site marking, before every procedure** (*why:* wrong-site and wrong-patient events are entirely preventable and occur when the checklist is treated as paperwork; *what:* correct patient, site and procedure). **KNOWING THE MAXIMUM LOCAL ANAESTHETIC DOSE AND THE LOCATION OF THE LIPID EMULSION BEFORE DRAWING UP** (*why:* local anaesthetic systemic toxicity progresses to refractory cardiac arrest and the antidote must be found in seconds; *what:* preparedness). **WATER-SOLUBLE CONTRAST — never barium — where perforation or leak is possible; and a LOW-OSMOLAR agent where aspiration is possible** (*why:* leaked barium causes fatal chemical mediastinitis, and aspirated gastrografin causes fatal pulmonary oedema; *what:* a safe study). **JOINT ASPIRATION with URGENT GRAM STAIN, CULTURE, CELL COUNT AND POLARISED MICROSCOPY, explicitly requested** (*why:* septic arthritis cannot be excluded any other way, and crystal examination is a separate request that is routinely omitted; *what:* organism, cell count, crystals — **remembering that crystals do not exclude infection**). **NOT aspirating a prosthetic joint on the ward** (*why:* contamination makes the result uninterpretable and introduces organisms into a prosthesis; *what:* referral instead). **Coagulation status and antibiotic cover before PTC** (*why:* bleeding and cholangitis are the two major complications; *what:* correctable risk). **Immediate reassessment of any patient with pain, fever or tachycardia after an upper endoscopy** (*why:* oesophageal perforation has high mortality and outcome depends on early recognition; *what:* surgical emphysema, effusion, contrast leak). **Asking what the MRI finding actually explains before referring for arthroscopy** (*why:* degenerative meniscal tears are common incidental findings and the operation does not outperform sham; *what:* whether the finding is the cause of the symptoms).

---

> [!note] Cross-references
> Perioperative assessment and sedation → [[AN1]] 0.1–0.2 · Anticoagulation around procedures → [[A9]] 0.4 · Consent and capacity → [[A10]] 0.2 · Safety culture, checklists and speaking up → [[EBM1]] 0.6 · Guideline use and low-value care → [[EBM1]] 0.2 · Upper GI bleeding and endoscopy → [[C4]] · Dysphagia, reflux and oesophageal disease → [[C6]] 0.1 · Coeliac disease and duodenal biopsy → [[C5]] 0.4 · Small bowel obstruction and the gastrografin challenge → [[C5]] 0.3 · Meconium ileus → [[M5]] 0.1 · Pancreatobiliary disease, ERCP and cholangitis → [[C7]] · Jaundice and biliary obstruction → [[C3]] 0.2 · Contrast nephropathy and AKI → [[H3]] 0.2 · Iodinated contrast and thyroid disease → [[I1]] 0.3 · Septic arthritis, gout and the hot joint → [[L1]] · Lipohaemarthrosis and occult fracture → [[L7]] 0.3 · Degenerative knee disease and exercise therapy → [[L5]] 0.4 and [[L6]] 0.2 · Prosthetic joint infection → [[K2]] 0.4 · Foreign bodies by site → [[A8]] and [[F3]] 0.2

<!-- ===== SOURCE: Examination.md ===== -->
*Moved here from `Examination.md` on 2026-09-01. Verbatim and unrenumbered.*

## 1.8 Pleural Aspiration (Procedure)

**Opening:** wash hands, introduce, confirm identity, explain the procedure (a needle/catheter inserted through the chest wall to sample or drain fluid from around the lung), gain consent, confirm site with imaging/USS guidance beforehand (ultrasound-guided aspiration is now standard practice and reduces complication rates compared to a purely clinical "blind" approach).

**Step-by-step sequence:**
1. Position the patient sitting up, leaning forward slightly over a pillow/table, arms resting forward — this opens up the intercostal spaces posteriorly.
2. Identify the site — typically guided by ultrasound marking, generally in the "triangle of safety" region for the affected side, above the rib (to avoid the neurovascular bundle running along the inferior rib margin) and below the scapula tip.
3. Clean the skin with antiseptic, drape, and infiltrate local anaesthetic down to the pleura, aspirating as you go to confirm you're not in a vessel and to identify the pleural space when fluid/air is first aspirated.
4. Insert the aspiration needle/catheter along the anaesthetised tract, just above the rib, advancing while aspirating until fluid is obtained.
5. Withdraw the required volume for diagnostic testing (or therapeutically, per the clinical indication — see [[02_Respiratory]] Pleural Effusions for the diagnostic tests to send: Light's criteria, pH, glucose, Gram stain/culture, cytology).
6. Withdraw the needle, apply a dressing, and obtain a post-procedure CXR to exclude a pneumothorax (a recognised complication).

**What to say aloud:** narrate the safety checks (confirming site with imaging, checking you're above the rib, confirming no excessive volume being removed too quickly if therapeutic — rapid large-volume drainage risks re-expansion pulmonary oedema).

**Presenting findings back to an examiner:** describe the fluid appearance (straw-coloured, turbid, frankly purulent, blood-stained) and state which diagnostic tests you are sending it for and why.

**Cross-reference:** see [[Investigation-Interpretation]] Pleural Fluid Analysis (Pleural Tap) for how to interpret the results, and [[02_Respiratory]] Empyema and Haemothorax for when drainage (rather than just diagnostic sampling) is indicated.

---

## 1.11 Abdominal Paracentesis (Procedure)

**Opening:** wash hands, introduce, confirm identity, explain the procedure (a needle/catheter inserted through the abdominal wall to sample or drain fluid from the peritoneal cavity), gain consent, confirm site with ultrasound guidance beforehand where available (reduces complication rates, particularly bowel perforation risk).

**Step-by-step sequence:**
1. Position the patient supine, slightly rotated toward the side being tapped if there's a large volume of free fluid (helps pool fluid away from bowel loops).
2. Identify the site — classically the left or right iliac fossa, lateral to the rectus sheath (avoiding the inferior epigastric vessels), at a point of demonstrated fluid on percussion/ultrasound; avoid visible collateral vessels, scars, and organomegaly.
3. Clean the skin with antiseptic, drape, and infiltrate local anaesthetic down to the peritoneum, aspirating as you advance to confirm you're not in a vessel and to identify free fluid return.
4. Insert the paracentesis needle/catheter along the anaesthetised tract using a "Z-track" technique (displacing the skin before insertion, so the tract seals once the needle is withdrawn — reduces persistent leakage afterward), advancing while aspirating until ascitic fluid is obtained.
5. Withdraw the required volume for diagnostic testing (send for the tests outlined in [[Investigation-Interpretation]] Ascitic Fluid Analysis (Paracentesis) — SAAG, neutrophil count, culture, ± cytology/amylase/triglycerides as indicated), or for large-volume therapeutic drainage — see below.
6. Withdraw the needle, apply a dressing, monitor for ongoing leakage or signs of complications (bleeding, peritonitis).

> [!warning] For large-volume therapeutic paracentesis (>5L), IV albumin is required to prevent post-paracentesis circulatory dysfunction — see [[03_Gastrointestinal]] Ascites (in ArLD) for the full Mx context this procedure sits within.

**What to say aloud:** narrate the safety checks (confirming site with ultrasound/percussion, checking you're clear of the inferior epigastric vessels, the Z-track technique rationale, and — for large-volume drainage — the need for albumin cover).

**Presenting findings back to an examiner:** describe the fluid appearance (straw-coloured, turbid, blood-stained, chylous) and state which diagnostic tests you are sending it for and why.

**Cross-reference:** see [[Investigation-Interpretation]] Ascitic Fluid Analysis (Paracentesis) for how to interpret the results, and [[03_Gastrointestinal]] Ascites and Spontaneous Bacterial Peritonitis for the disease-level context and further Mx.

---

<!-- ===== SOURCE: F0-4_Resuscitation_Algorithms_and_Emergency_Procedures.md ===== -->
*Moved here from `Emergency and Crit Care_merged.md` on 2026-09-01. Verbatim and unrenumbered.*

## 0.7 Mechanical Ventilation

**D:** Positive pressure ventilatory support, invasive or non-invasive, replacing or supplementing spontaneous breathing.

**A/P:** Spontaneous breathing generates **negative** intrathoracic pressure, which draws air in and augments venous return. Positive pressure ventilation inverts this → intrathoracic pressure rises → **venous return falls** → in a hypovolaemic patient, blood pressure drops immediately after intubation. This is the mechanism behind post-intubation hypotension and the reason volume status matters before the tube goes in.

> [!info] The intern-level parameters
> **Tidal volume** — set against predicted body weight, not actual weight, since lung size tracks height rather than obesity. **Respiratory rate** — set with minute ventilation in mind. **PEEP** — maintains alveolar recruitment and improves oxygenation. **FiO₂** — titrated down as tolerated. **Plateau pressure** — the marker of alveolar distension and the number that limits tidal volume. `UNVERIFIED — lung-protective tidal volume in mL/kg predicted body weight, plateau pressure limits, PEEP tables, and oxygenation targets are all omitted; obtain from local ICU protocol and current ARDS guidance.`

> [!danger] Auto-PEEP and breath stacking in obstructive disease
> In severe asthma and COPD, expiration is prolonged. If the ventilator delivers the next breath before the last has been exhaled, air trapping accumulates → intrathoracic pressure rises progressively → venous return collapses → **PEA arrest.** The asthmatic who arrests shortly after intubation is the classic scenario.
> **The management is counterintuitive: disconnect the circuit and allow full exhalation**, apply lateral chest compression if needed, then resume with a longer expiratory time, lower rate and accepting a high CO₂ (permissive hypercapnia). Exclude tension pneumothorax at the same time.

> [!warning] Non-invasive ventilation — where it helps and where it delays
> **CPAP** benefits acute cardiogenic pulmonary oedema. **BiPAP** benefits hypercapnic exacerbations of COPD. Both fail in the patient who cannot protect their airway, is vomiting, is haemodynamically unstable, or is agitated and non-compliant. **The harm is using NIV to postpone an intubation that is going to happen anyway** — set a time-limited trial with explicit review criteria rather than an open-ended one.

**Ix:** ABG or VBG after each significant settings change (*why:* the response to a change is the only way to know it was right; *what:* pCO₂, pH, oxygenation). Continuous waveform capnography (*why:* real-time ventilation monitoring and disconnection alarm; *what:* trace and value). Plateau pressure measurement (*why:* distinguishes high airway resistance from stiff lungs and is the number that guides lung protection; *what:* elevated plateau indicating alveolar overdistension). CXR (*why:* tube position, pneumothorax, evolving infiltrates; *what:* findings). Blood pressure with continuous monitoring (*why:* post-intubation hypotension from reduced venous return is expected and must be anticipated; *what:* fall following positive pressure initiation).

### 0.7.1 Mx – Immediate
Adequate sedation and analgesia. Set initial parameters per protocol, confirm with a gas, and reassess. Anticipate and treat post-intubation hypotension.

### 0.7.2 Mx – Definitive
ICU management with lung-protective strategy, daily sedation interruption and weaning assessment where appropriate.

### 0.7.3 Mx – Chronic/long-term
Ventilator-associated pneumonia prevention, early mobilisation, and follow-up for post-intensive-care syndrome.

---

## 0.8 Procedural Sedation

**D:** Administration of sedative or dissociative agents to tolerate an unpleasant procedure while maintaining cardiorespiratory function, on a continuum from minimal sedation to general anaesthesia.

> [!danger] Sedation is a continuum and patients move along it unpredictably
> The depth you intended is not necessarily the depth you get. **Anyone administering procedural sedation must be prepared to manage the next level down**, including airway obstruction and apnoea. This is why a dedicated sedationist — separate from the person performing the procedure — is the standard, not a luxury.

> [!tip] Pre-procedure assessment
> Fasting status, airway assessment (as per LEMON in 0.6), comorbidities and ASA class, allergies, previous anaesthetic problems, current medications including opioids and benzodiazepines, and consent. Extremes of age, obstructive sleep apnoea and significant cardiorespiratory disease all raise the risk substantially.

> [!warning] Monitoring and staffing
> Continuous pulse oximetry, ECG, blood pressure and **capnography**, which detects apnoea well before desaturation — particularly important in a patient on supplemental oxygen, whose saturation stays normal while they stop breathing. Resuscitation equipment and reversal agents immediately available. A second clinician whose only job is the patient.

Agents commonly used in Australian emergency departments include ketamine (which is dissociative rather than sedative and preserves airway reflexes and respiratory drive better than alternatives), propofol, midazolam, fentanyl and nitrous oxide. `UNVERIFIED — all agent doses, titration increments, combinations, fasting guidance and reversal agent dosing are omitted; obtain from ACEM guidance and local policy.`

**Ix:** Pre-procedure assessment as above (*why:* identifies the patient in whom sedation should happen in theatre rather than the emergency department; *what:* difficult airway features, high ASA class). Continuous monitoring throughout (*why:* the complications are respiratory and occur without warning; *what:* apnoea on capnography, desaturation, hypotension). Recovery assessment against discharge criteria (*why:* premature discharge risks re-sedation at home, particularly with longer-acting agents; *what:* return to baseline conscious state, mobility, tolerance of oral intake).

### 0.8.1 Mx – Immediate
Prepare, monitor, pre-oxygenate, titrate to effect, and stop at the depth required. Manage airway obstruction with positioning and adjuncts before reaching for reversal.

### 0.8.2 Mx – Definitive
Recovery with continued monitoring until discharge criteria are met.

### 0.8.3 Mx – Chronic/long-term
Written discharge advice: no driving, no operating machinery, no significant decisions, and a responsible adult for the remainder of the day.

---

## 0.11 Fascia Iliaca Block

**D:** A regional anaesthetic technique depositing local anaesthetic beneath the fascia iliaca to anaesthetise the femoral and lateral femoral cutaneous nerves, used principally for fractured neck of femur.

**A/P:** The femoral nerve, lateral femoral cutaneous nerve and — variably — the obturator nerve run deep to the fascia iliaca in the iliac fossa. A volume of local anaesthetic placed in this potential space spreads along it to reach the nerves without direct needle contact with them. Blocking these provides analgesia to the hip, anterior thigh and femoral shaft.

> [!tip] Why it matters in the elderly hip fracture patient
> This population tolerates opioids poorly — delirium, respiratory depression, constipation, falls. A fascia iliaca block is **opioid-sparing**, and it is associated with reduced delirium and better pain scores. In many Australian hospitals it is part of the hip fracture pathway and is expected within a defined time of presentation. It is a technique interns are frequently taught and asked to perform.

> [!warning] Contraindications and cautions
> Patient refusal or inability to consent, local infection at the site, allergy to local anaesthetic, anticoagulation (relative — check local policy), and previous femoral vascular surgery or graft. Document a neurovascular examination **before** the block, since the block will obscure subsequent assessment.

> [!danger] Local anaesthetic systemic toxicity
> The volumes used are large. LAST presents with perioral tingling, tinnitus, metallic taste, agitation and confusion, progressing to seizures, arrhythmia and cardiac arrest. **Aspirate before injecting, inject incrementally, and have intravenous lipid emulsion immediately available and know where it is kept.** `UNVERIFIED — maximum safe local anaesthetic doses by weight, the block volume and concentration, and the intralipid regimen for LAST are all omitted; obtain from your local protocol, the Australian Medicines Handbook and ANZCA guidance.`

**Ix:** Pre-block neurovascular examination documented (*why:* the block abolishes sensation and motor function in the distribution, so a deficit found afterwards cannot be attributed without a baseline; *what:* sensation, motor function, distal pulses). Weight (*why:* maximum local anaesthetic dose is weight-based and toxicity is dose-dependent; *what:* weight in kilograms). Coagulation profile and medication review where anticoagulated (*why:* bleeding risk into the compartment; *what:* INR, anticoagulant agent and last dose). Ultrasound guidance where available (*why:* improves accuracy of fascial plane identification and reduces vascular puncture compared with landmark technique; *what:* fascia iliaca, femoral artery, needle tip position). Post-block pain score (*why:* confirms success and identifies the need for an alternative; *what:* reduction in score).

### 0.11.1 Mx – Immediate
Consent, position, sterile technique, ultrasound guidance where available, aspirate and inject incrementally with continuous verbal contact with the patient to detect early LAST.

### 0.11.2 Mx – Definitive
Multimodal analgesia continues alongside the block. Repeat or catheter techniques for prolonged analgesia are anaesthetic decisions.

### 0.11.3 Mx – Chronic/long-term
Document the block, agent, volume and time in the notes and on the anaesthetic record, since duration affects the peri-operative plan. Cross-refer [[L5]] Hip Pain and [[11_08a_Ortho_-_Joint_Replacements]].

---

> [!note] Cross-references
> Cardiac arrest and the 4 Hs and 4 Ts → [[A1]] 0.4 · Deteriorating patient recognition → [[A1]] 0.1 · Shock phenotypes and fluid decisions → [[F0.3]] · Opioid-induced respiratory depression → [[F0.1]] 0.5 · Acute asthma and COPD ventilation detail → [[F0.5]]


<!-- ===== SOURCE: 03a_Anaesthetics_Primer.md ===== -->
*Moved here from `Anaes_merged.md` on 2026-09-01. Verbatim and unrenumbered.*

## 0.2 Airway Adjuncts

> [!note] Most airway adjuncts help open the airway to promote air delivery, but only endotracheal intubation and tracheostomies properly protect the airway.

### 0.2.1 Oropharyngeal / Guedel airway (OPA)
- Measure by placing the tube on the patient's cheek — wide part near the front teeth, smaller opening at the angle of the jaw ("hard to hard")
- In adults, insert upside down, then twist 180° when reaching the back of the throat
- Poorly tolerated in conscious/semi-conscious patients (can cause gag reflex)

### 0.2.2 Nasopharyngeal airway (NPA)
- Tube passed through the nostril to the back of the throat; bypasses obstructions in the mouth/base of tongue
- Measure with one end at the tip of the nose, other end at the tragus of the ear ("soft to soft")
- Insert as if inserting an NG tube — aim straight, not downwards

> [!danger] Contraindicated if suspected skull base fracture (risk of intracranial passage).

### 0.2.3 Supraglottic airway
Divided into laryngeal mask airway (LMA) and iGel.
- The end sits at the vocal cords, forming a seal to block the oesophageal opening (lowers aspiration risk)
- Does not enter the trachea completely, so still carries some aspiration risk — cannot be said to fully protect the airway
- Useful for short or low-risk procedures (e.g. incision and drainage of simple abscesses)

**Laryngeal mask airway:** reusable supraglottic device; some versions have inflatable seals (better seal) and gastric ports for drainage/suction of secretions.

**iGel:** single-use supraglottic device; seal activated by body temperature (no inflation required).

### 0.2.4 Bag-valve-mask (BVM)
- Mask placed over nose and mouth (usually with head tilt-chin lift manoeuvre + tight seal)
- Compression of the bag → increased pressure → opens valve → air passes into the mask
- Can be connected to oxygen ± gas supply for pre-oxygenation
- Allows manual ventilation just before intubation

### 0.2.5 Endotracheal tube
- Inserted with the help of a laryngoscope or fibreoptic camera into the trachea
- Usually size 7 for women, size 8 for men — may need resizing based on weight
- Depth needs to be marked (usually 20–24cm at the teeth), then taped to secure
- Inflatable cuff seals the trachea and prevents aspiration

### 0.2.6 Laryngoscope
- Consists of "blades" and a torchlight
- Used to lift soft tissues and the epiglottis, directly visualising the larynx so the tube can be inserted past the vocal folds
- Patient needs to be able to bend their neck backwards for insertion

### 0.2.7 Tracheostomies
Bypass the upper airway, directing ventilation through the trachea into the lungs.
- **Cricothyroidotomy:** done in emergencies — incision through the membrane between cricoid and thyroid cartilage, tube inserted through the incision
- **Surgical tracheostomy:** incision made through the trachea itself, tracheostomy inserted through this incision

---

## 0.3 Regional / Local Anaesthesia

Divided into peripheral nerve blocks and neuraxial anaesthesia (further divided into spinal & epidural).

### 0.3.1 Peripheral nerve blocks

**Local anaesthetics (LA):** lidocaine, bupivacaine, prilocaine
- Long-acting: bupivacaine (also takes longer to work), levobupivacaine, ropivacaine
- Middle-acting: lidocaine (especially good for mucous membranes), prilocaine, mepivacaine
- Short-acting: procaine

Adrenaline can be mixed in — causes vasoconstriction so LA remains at the injection site longer (more effective) and allows higher LA doses (lower risk of systemic entry). Can be used to block specific nerves (e.g. femoral nerve block for neck-of-femur fracture) or injected at incision sites during surgery.

### 0.3.2 Risks of local anaesthetics

> [!danger] Systemic distribution (LA accidentally injected intravenously)
> **S/Smx:** perioral tingling, tongue numbness, lightheadedness, tinnitus; if severe — seizures, apnoea, cardiac depression, coma
> **Mx:** stop LA; 20% lipid emulsion (Intralipid — binds to LA in circulation); resuscitate as necessary (may require intubation, ventilation); seizure management

Other risks: failure, nerve injury, bleeding.

### 0.3.3 Neuraxial blocks
Injection of anaesthetic (e.g. LA, opioids) into the epidural or subarachnoid space.
- Injection level should be around L3/L4. L4/L5 level can be estimated as the line between the iliac crests.
- Not higher — spinal cord ends ~L1; increased risk of transecting spinal cord.
- Needle passes through: skin → subcutaneous fat → supraspinous ligament → interspinous ligament → ligamentum flavum → epidural space (epidural needle stops here) → dura mater → arachnoid mater → subarachnoid space (spinal needle stops here)
- Sterile procedure (requires scrubbing in)
- Local anaesthetic usually given to skin and surrounding soft tissue before the needle is advanced
- Blocks tested using cold spray to determine the dermatomal level at which the block ends

> [!danger] Absolute contraindications to neuraxial anaesthesia
> Anticoagulant states (increased risk of bleeding at the cord — see the Pre-op instructions section above for the specific timing thresholds by anticoagulant class, since "anticoagulated" isn't a single fixed exclusion but depends on which drug and how recently it was stopped); local sepsis (risk of CSF infection); shock or hypovolaemic states; raised ICP (risk of coning); unwilling or uncooperative patient (risk to patient and staff); fixed output states (e.g. mitral and aortic stenosis)

### 0.3.4 Epidural anaesthetic
- Epidural space is larger than the subarachnoid space, requiring a larger volume of anaesthetic
- Can be given as a single dose, or via catheter connected to continuous infusion or patient-controlled analgesia (PCA)
- Usually given in labour for pregnancy, as the catheter can stay in for continuous anaesthesia

**Risks:**
- Dural puncture headache — Mx with caffeine and oral fluids, bed rest, analgesia; if headache >24–48h, blood patch (small amount of patient's own blood introduced into CSF space to patch the puncture)
- Vessel puncture and inadvertent injection — Mx with resuscitation (symptomatic)
- Hypoventilation due to motor block of intercostal muscles — may require ventilation
- Inadvertent spinal anaesthesia (large volume injected into CSF — near-total spinal block) — requires resuscitation
- Epidural haematoma/abscess — requires urgent neuro referral

### 0.3.5 Spinal anaesthetic
- Aims to anaesthetise the spinal roots passing through the space
- Single dose — only suitable for short procedures (may wear out otherwise)

**Risks:**
- Some lightheadedness and ↓BP — conservative Mx
- Total spinal block (↓HR, ↓BP, anxiety, apnoea, loss of consciousness) — requires urgent resuscitation
- Headache (possibly from dural puncture)
- Urinary retention
- Permanent neurological damage (rare)

---

<!-- ===== SOURCE: 14_05d_Psych_-_Electroconvulsive_Therapy.md ===== -->
*Moved here from `Psychiatry_merged.md` on 2026-09-01. Verbatim and unrenumbered.*

## Electroconvulsive therapy (ECT)

- **D:** psychiatric treatment where a generalised seizure is induced in a patient to manage refractory mental disorders.

> [!info] Indications
> - Refractory severe depression (~50% response rate).
> - Life-threatening catatonia.
> - Prolonged or severe manic episode.
> - Prior good response.

> [!info] Alternatives: transcranial magnetic stimulation; vagus nerve stimulation; deep brain stimulation.

- **Other points:**
  - Must be administered under anaesthesia with a muscle relaxant.
  - Cognitive impairment afterwards, including retrograde and anterograde amnesia.
  - Generally regarded as safe in pregnancy.


<!-- ===== SOURCE: H1_Haematuria_and_Proteinuria.md ===== -->
*Moved here from `Investigation-Interpretation.md` on 2026-09-01. Verbatim and unrenumbered.*

## 0.6 Renal Biopsy

> [!tip] When it is indicated
> **· Nephrotic syndrome in an ADULT without an obvious cause.**
> **· Nephritic syndrome and any suspicion of RPGN — urgently.**
> **· Unexplained acute kidney injury**, particularly with an active urinary sediment.
> **· Systemic disease with renal involvement — lupus, vasculitis, myeloma, amyloid — where the histology determines treatment intensity.**
> **· Unexplained progressive chronic kidney disease with normal-sized kidneys.**
> **· Renal transplant dysfunction.**
> **When it is NOT indicated: typical childhood nephrotic syndrome · typical diabetic nephropathy with a compatible history and retinopathy · and SMALL, ECHOGENIC KIDNEYS, where the disease is already irreversible and the biopsy carries risk without benefit.**

> [!warning] Before and after
> **Before: control the BLOOD PRESSURE · check FBC, coagulation and platelets · CEASE antiplatelets and anticoagulants for the appropriate interval · confirm two kidneys and their size on ultrasound · and obtain informed consent covering the bleeding risk.**
> **After: BLEEDING is the main complication** — ranging from microscopic haematuria (common and expected) through visible haematuria to perinephric haematoma requiring transfusion or embolisation, and rarely nephrectomy. **Observation with regular observations and haemoglobin is standard.**
> **Arteriovenous fistula formation is a recognised late complication.**
> **The specimen is examined by LIGHT MICROSCOPY, IMMUNOFLUORESCENCE (which gives the linear/granular/pauci-immune pattern that classifies RPGN) and ELECTRON MICROSCOPY (which shows podocyte and basement membrane detail).** All three are needed, which is why the specimen must be handled correctly at collection.

---

> [!note] Cross-references
> Acute kidney injury, chronic kidney disease and CKD-MBD → [[H3]] · Lower urinary tract symptoms and retention → [[H2]] · Renal colic, scrotal and groin problems → [[H4]] · Vasculitis, ANCA and pulmonary-renal syndrome → [[L2]] 0.5 · Autoantibody interpretation → [[L2]] 0.6 · Lupus nephritis and urinalysis at every visit → [[L2]] 0.4 · Haemoptysis → [[A4]] 0.3 · Myeloma and light chains → [[J4]] · Rhabdomyolysis and myoglobinuria → [[A7]] 0.6 · Diabetic kidney disease → [[I2]] 0.5 · RAS blockade and the expected creatinine rise → [[CV-X]] 0.3 · Post-streptococcal disease and skin infection → [[K2]] 0.6 and [[AU1]] 0.4 · Paediatric nephrotic syndrome → [[M5]] · Hypertension → [[B2]]
