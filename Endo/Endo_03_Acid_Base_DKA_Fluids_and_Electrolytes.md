---
aliases:
  - "F0.2"
  - "F0-2_Acid-Base__DKA_and_Fluid_States"
  - "NEW_Acid-Base_Fluids_and_Electrolytes"
split_from: "Endocrine and metabolics_merged.md"
part: "3 of 12"
---

<!-- SPLIT-HEADER-END -->
<!-- ===== SOURCE: F0-2_Acid-Base__DKA_and_Fluid_States.md ===== -->


> [!warning] Sourcing
> Written from model knowledge, not retrieved from guidelines. Mechanism, interpretive method and discriminators are reliable at intern level. **Every dose, threshold, reference range and timing figure carries an `UNVERIFIED` marker naming what to check, or has been omitted with the omission stated in place.** For this file specifically: **all fluid rates, insulin infusion rates, potassium replacement figures and correction targets are omitted, not flagged.** A DKA fluid rate error was previously found in this corpus. Obtain these from your health network's DKA protocol, the ADS/ADEA guidance, and for children the RCH and APEG guidelines — the adult and paediatric regimens are not interchangeable and the difference is the point.

---

## 0.1 Acid-Base Interpretation — Framework

**D:** A structured method for converting a blood gas plus electrolytes into a named disorder, or disorders, and a differential.

**A/P:** A primary process shifts pH → the body compensates through the opposite system (respiratory compensation is fast, renal compensation takes days) → compensation never fully corrects pH and never overshoots → therefore a pH that has corrected fully, or overshot, means a second primary process is present rather than vigorous compensation.

> [!tip] The interpretation sequence
> **1. pH** — acidaemic or alkalaemic? This names the *primary* disorder even when a second process is hidden underneath.
> **2. pCO₂ and bicarbonate** — which one moves in the direction that explains the pH? That system is primary; the other is compensating.
> **3. Anion gap**, on every metabolic acidosis, and arguably on every gas — a raised gap can be present with a normal pH and normal bicarbonate when a second alkalotic process masks it.
> **4. Delta ratio**, if the gap is raised — does the rise in gap account for the fall in bicarbonate, or is there a second metabolic process?
> **5. Is compensation appropriate?** If not, there is a second primary disorder.

> [!info] The calculations
> **Anion gap** = Na⁺ − (Cl⁻ + HCO₃⁻). Some formulations include potassium; be consistent about which you use, because the normal range differs between them. The gap must be **corrected for albumin** — a hypoalbuminaemic ICU or cirrhotic patient can have a significant unmeasured-anion load with an apparently normal gap. `UNVERIFIED — normal anion gap range, the albumin correction factor, Winter's formula constants for expected pCO₂, and the delta ratio cut-offs all require verification against the Oxford Handbook of Clinical and Laboratory Investigation or a current source. No numeric values are stated here.`

> [!warning] Three interpretive traps
> **A normal bicarbonate does not exclude a metabolic acidosis** — a coexisting metabolic alkalosis (vomiting, diuretics) can normalise it while the anion gap stays wide. Always calculate the gap.
> **A "normal" pCO₂ in a tiring asthmatic is a pre-arrest finding**, not reassurance — it means the patient can no longer sustain the hyperventilation that was keeping them alive.
> **Venous gases are adequate for pH, bicarbonate, potassium and lactate**, which covers most ward decisions. They are unreliable for pO₂ and only approximate for pCO₂. Do not delay a decision waiting for arterial access.

> [!tip] Causes by category
> **HAGMA — GOLD MARK:** Glycols (ethylene glycol, propylene glycol) · Oxoproline (chronic paracetamol, malnourished women) · L-lactate · D-lactate (short bowel) · Methanol · Aspirin · Renal failure · Ketoacidosis.
> **NAGMA:** GI bicarbonate loss (diarrhoea, high-output stoma, ureteric diversion) · renal tubular acidosis · carbonic anhydrase inhibitors · large-volume saline resuscitation.
> **Metabolic alkalosis:** vomiting and NG loss · diuretics · hyperaldosteronism · profound hypokalaemia.
> **Respiratory acidosis:** anything reducing minute ventilation — sedation, neuromuscular weakness, severe airflow obstruction, chest wall disease.
> **Respiratory alkalosis:** pain, anxiety, hypoxia, sepsis, PE, salicylate, pregnancy, hepatic failure.

**Ix:** VBG or ABG with electrolytes (*why:* gives pH, pCO₂, bicarbonate, potassium and lactate in minutes and is the substrate for the whole sequence above; *what:* the primary disorder and its compensation). Full UEC including chloride (*why:* the anion gap cannot be calculated without chloride, and chloride is frequently omitted from the ordered panel — this is the commonest practical reason an acid-base assessment cannot be completed; *what:* sodium, chloride, bicarbonate for the gap). Albumin (*why:* corrects the anion gap, without which unmeasured anions are missed in the sick and malnourished; *what:* hypoalbuminaemia requiring correction). Lactate (*why:* separates the largest single HAGMA category and tracks resuscitation response; *what:* elevation, and clearance on repeat). Serum ketones, preferably beta-hydroxybutyrate (*why:* urine ketone dipsticks detect acetoacetate and can read falsely low early in DKA and falsely high during recovery, so they mislead in both directions; *what:* elevated beta-hydroxybutyrate). Serum osmolality with calculated gap where a toxic alcohol is possible (*why:* detects the parent alcohol before the acid metabolite forms; *what:* raised osmolar gap — cross-refer [[F0.1]] 0.8). Salicylate and paracetamol levels where the pattern is mixed or unexplained (*why:* salicylate produces a distinctive mixed picture and is easily missed; *what:* level).

### 0.1.1 Mx – Immediate
Treat the patient, not the number. The pH itself is rarely the therapeutic target; the underlying process is. Restore perfusion and ventilation.

### 0.1.2 Mx – Definitive
Directed at the identified cause. Bicarbonate therapy is contentious in most metabolic acidoses and is not a routine intern decision. `UNVERIFIED — indications and thresholds for bicarbonate therapy require verification and vary by cause.`

### 0.1.3 Mx – Chronic/long-term
Recurrent unexplained acidosis warrants investigation for renal tubular acidosis, malabsorption or occult toxin exposure.

---


<!-- ===== SOURCE: Investigation-Interpretation.md ===== -->
*Co-located here from `Investigation-Interpretation.md` on 2026-09-01. Verbatim and unrenumbered.*

> [!info] **CO-LOCATED, NOT CROSS-REFERENCED. Two accounts of blood-gas interpretation, side by side, both intact.**
> They were in two files. A cross-reference means opening a second file, which under time pressure does not happen.
> The framework above and the step-by-step reading below were written separately and overlap heavily. A third account, `### 0.20.6 Arterial Blood Gas Reference Values`, is also in this file.

## 1.5 ABG / VBG Interpretation

**What it measures:** oxygenation, ventilation (CO2), and acid-base status — one of the highest-yield "read the result" skills across both MCQ and OSCE, since it's tested via numbers rather than an image and rewards a consistent stepwise approach.

**Systematic approach:**

1. **Assess oxygenation first (independent of acid-base status):** PaO2 <80mmHg (~10.6kPa) on room air suggests hypoxaemia — check the FiO2/O2 delivery the patient was on at the time, since a "normal" PaO2 on high-flow O2 may still represent significant underlying lung disease. See [[02_Respiratory]] Respiratory Failure for the Type I (hypoxaemic) vs Type II (hypoxaemic + hypercapnoeic) classification this feeds into.

2. **Check the pH:** <7.35 = acidaemia; >7.45 = alkalaemia. This tells you the net direction but not yet the cause.

3. **Check PaCO2 (the respiratory component):**
   - PaCO2 >45mmHg (~6kPa) with acidaemia → respiratory acidosis (hypoventilation — e.g. COPD exacerbation, opioid overdose, exhaustion in severe asthma — see [[02_Respiratory]] Asthma acute exacerbation, where a rising/normalising CO2 in a tachypnoeic patient is a red flag for exhaustion, not reassurance)
   - PaCO2 <35mmHg (~4.7kPa) with alkalaemia → respiratory alkalosis (hyperventilation — anxiety, PE, early asthma/sepsis before exhaustion sets in, pain)

4. **Check HCO3⁻ (the metabolic component):**
   - HCO3⁻ <22mmol/L with acidaemia → metabolic acidosis
   - HCO3⁻ >26mmol/L with alkalaemia → metabolic alkalosis

5. **Match the direction of pH change to which component (respiratory or metabolic) moved the "wrong way" to explain it** — the disturbance that matches the direction of the pH change is the primary one; the other value has either not yet responded (acute) or is compensating (chronic/compensated).
   - **Compensation logic:** the body always compensates in the *same direction* as the primary disturbance (i.e. it doesn't overcorrect past normal) — a metabolic acidosis triggers respiratory compensation (hyperventilation, ↓CO2) via the same pH-lowering-opposing direction, and a chronic respiratory acidosis (e.g. COPD) triggers renal compensation (↑HCO3⁻ reabsorption) over days. **Fully compensated** = pH has returned to (near-)normal despite the underlying primary disturbance still being present — this is the "compensated respiratory acidosis" pattern expected in a stable COPD patient (see [[02_Respiratory]] COPD Exacerbation), and its *absence* (an uncompensated/partially-compensated picture in a known chronic retainer) suggests a more acute superimposed process.

6. **If metabolic acidosis — calculate the anion gap** (Na⁺ − [Cl⁻ + HCO3⁻], normal ~8–16mmol/L) to narrow the cause:
   - **Raised anion gap:** mnemonic "MUDPILES" — Methanol, Uraemia, DKA, Propylene glycol/Paraldehyde, Iron/Isoniazid, Lactic acidosis (e.g. sepsis, tissue hypoperfusion, seizure), Ethylene glycol, Salicylates
   - **Normal anion gap (hyperchloraemic):** GI bicarbonate loss (diarrhoea), renal tubular acidosis, early renal failure

7. **Check lactate specifically if raised/unwell:** elevated lactate is a marker of tissue hypoperfusion/anaerobic metabolism — relevant to sepsis severity (see [[01_Cardiovascular]] Shock, Septic shock) and can itself widen the anion gap.

**Where this feeds into disease-specific content already documented (not repeated here):** [[02_Respiratory]] Asthma (acute exacerbation — hypercapnoea as a marker of exhaustion), COPD (chronic compensated respiratory acidosis and controlled O2 targets in known CO2 retainers), ARDS (severe hypoxaemia, PaO2/FiO2 ratio as a diagnostic/severity criterion), and Respiratory Failure (Type I vs Type II classification table). See [[01_Cardiovascular]] Shock for lactate's role in septic/hypovolaemic shock assessment.

**Pitfalls:**
- VBG is a reasonable substitute for ABG for pH/HCO3⁻/lactate in most acute settings (avoiding a painful arterial stab), but venous PaO2/PaCO2 do **not** reliably reflect arterial values — an ABG is still needed when oxygenation/ventilation status specifically must be known precisely (e.g. confirming hypercapnoea in a COPD exacerbation).
- A "normal" pH does not mean no acid-base disturbance is present — mixed disturbances (e.g. a metabolic acidosis and a respiratory alkalosis occurring together) can partially cancel out and normalise the pH while both underlying processes remain clinically significant.

---

<!-- ===== SOURCE: F0-2_Acid-Base__DKA_and_Fluid_States.md ===== -->

## 0.2 HAGMA — Diabetic Ketoacidosis (the acid-base picture)

**D:** High anion gap metabolic acidosis produced by accumulation of ketoacids in absolute or relative insulin deficiency.

**A/P:** Insulin deficiency with counter-regulatory excess (glucagon, cortisol, catecholamines, growth hormone) → unrestrained lipolysis → free fatty acids delivered to the liver → hepatic beta-oxidation to acetoacetate and beta-hydroxybutyrate → these are the unmeasured anions that widen the gap. Simultaneously, absent insulin plus gluconeogenesis and glycogenolysis → hyperglycaemia exceeding renal threshold → osmotic diuresis → profound water, sodium and **total body potassium** depletion, all of which is masked at presentation.

> [!danger] The potassium trap
> Acidosis and insulin deficiency drive potassium **out of cells**, so the measured serum potassium is normal or high while total body potassium is severely depleted. Insulin drives it straight back in. **A normal potassium at presentation will fall dangerously once insulin starts.** A low potassium at presentation means the deficit is extreme, and insulin must not be started until it is being replaced. `UNVERIFIED — the potassium threshold below which insulin is withheld, and all replacement rates, come from your local DKA protocol and are not stated here.`

> [!warning] Euglycaemic DKA
> SGLT2 inhibitors (dapagliflozin, empagliflozin) produce ketoacidosis with a glucose that is normal or only mildly raised, because glucose is being excreted rather than accumulating. Pregnancy, prolonged fasting, alcohol and vomiting also predispose. **A normal glucose does not exclude DKA.** Check ketones in any acidotic diabetic patient regardless of glucose — this is an increasingly common Australian presentation and a well-recognised source of delayed diagnosis.

**S/Smx:** Polyuria, polydipsia, weight loss, vomiting, abdominal pain (which can mimic a surgical abdomen), Kussmaul respiration, ketotic breath, dehydration, drowsiness. Look for the precipitant: infection, missed insulin, first presentation of type 1 diabetes, myocardial infarction, pancreatitis, steroids.

**Ix:** Beta-hydroxybutyrate, ideally bedside (*why:* it is the dominant ketone in DKA and the one urine dipsticks miss, and it is the marker used to determine resolution; *what:* elevation at diagnosis, falling with treatment). VBG (*why:* gives pH, bicarbonate and potassium within minutes, and venous is sufficient — arterial sampling adds little and delays treatment; *what:* HAGMA with the severity grading that determines disposition). UEC with chloride (*why:* anion gap, potassium for the trap above, and sodium requiring correction for hyperglycaemia; *what:* raised gap, potassium, corrected sodium). Glucose, serial (*why:* guides when dextrose is added to the infusion — insulin continues to clear ketones after glucose normalises, so the infusion is not simply stopped; *what:* falling glucose). FBC (*why:* leucocytosis occurs in DKA itself and does not confirm infection, but a left shift or very high count prompts a search; *what:* white cell count with the caveat). Septic screen — cultures, urinalysis, CXR (*why:* infection is the commonest precipitant and treating DKA without treating the trigger fails; *what:* source). ECG (*why:* silent myocardial infarction precipitates DKA in older diabetics, and hyper/hypokalaemia shows here first; *what:* ischaemia, peaked or flattened T waves). Serum osmolality (*why:* distinguishes and identifies overlap with hyperosmolar hyperglycaemic state; *what:* marked elevation).

### 0.2.1 Mx – Immediate
See 0.3 — management is protocol-driven and is set out there rather than duplicated.

### 0.2.2 Mx – Definitive
Resolution is defined by **closure of the anion gap and clearance of ketones**, not by normalisation of glucose. Stopping insulin when the glucose normalises is a recognised error that re-precipitates the acidosis.

### 0.2.3 Mx – Chronic/long-term
Diabetes educator and endocrinology review, sick-day management plan, and for a first presentation, structured type 1 education before discharge.

---

## 0.3 Adult Diabetic Ketoacidosis — Management

**D:** The management pathway for DKA in an adult, which is protocolised in every Australian health network.

**R:**
*Unmodifiable:* Type 1 diabetes, previous DKA episodes, adolescence and young adulthood.
*Modifiable:* Missed or omitted insulin, pump failure, undiagnosed intercurrent infection, SGLT2 inhibitor use, alcohol, corticosteroid therapy, limited health literacy or access, insulin cost and supply issues.

**A/P:** As per 0.2. The three simultaneous deficits requiring correction are **fluid, insulin and potassium**, and the order and rate of each is what the protocol exists to specify.

> [!danger] Fluid and insulin figures are omitted
> `UNVERIFIED — initial fluid bolus volume, subsequent replacement rate, choice of crystalloid, fixed-rate insulin infusion rate in units/kg/hr, the glucose threshold at which dextrose is added, potassium replacement rates by measured level, and bicarbonate indications are ALL omitted from this file. A DKA fluid rate error has already been found in this corpus. Obtain every one of these figures from your health network's DKA protocol before use — do not reconstruct them from memory or from a UK or US source, as replacement rates and fluid choices differ between jurisdictions.`

**S/Smx:** As per 0.2.

**Ix:** As per 0.2, with hourly bedside glucose and ketones, and serial VBG and potassium during the infusion (*why:* the whole treatment is titrated against these three and the potassium can fall precipitously; *what:* falling ketones, closing gap, potassium trend).

### 0.3.1 Mx – Immediate
A–E and resuscitation. Two large-bore cannulae. Fluid resuscitation begins first; insulin follows once potassium is known and is being replaced if low. Fixed-rate intravenous insulin infusion. Hourly monitoring. **Continue the patient's long-acting basal insulin** if they take one — stopping it is a common error that causes rebound ketosis when the infusion ends. Identify and treat the precipitant. Escalate to HDU/ICU per local severity criteria.

### 0.3.2 Mx – Definitive
Continue the infusion until the anion gap has closed and ketones have cleared, adding dextrose to permit this once glucose falls. Transition to subcutaneous insulin with an **overlap** before the infusion stops — stopping the infusion at the moment the subcutaneous dose is given leaves an uncovered gap. Diabetes team involvement.

### 0.3.3 Mx – Chronic/long-term
Sick-day plan, ketone meter provision, insulin technique review, psychosocial assessment where episodes recur — recurrent DKA in a young person is frequently a marker of distress, insulin omission or an eating disorder, and warrants a conversation rather than only a protocol.

---

## 0.4 Paediatric Diabetic Ketoacidosis

**D:** DKA in a child or adolescent, managed differently from the adult because of the risk of cerebral oedema.

**A/P:** The metabolic derangement is identical to the adult. What differs is that children are at meaningfully higher risk of **cerebral oedema**, a complication that carries high mortality and morbidity and that appears to relate to osmotic shifts during correction. The paediatric protocol is therefore built around slower, more cautious correction of fluid and glucose than the adult protocol.

> [!danger] Cerebral oedema — the reason the paediatric protocol exists
> Typically occurs some hours *into* treatment, when the child appeared to be improving. Warning signs: **headache, irritability, a falling conscious state, bradycardia with rising blood pressure** (the Cushing response — not a late finding to wait for), and abnormal posturing. Any deterioration in conscious state during DKA treatment in a child is cerebral oedema until proven otherwise and requires immediate senior involvement and treatment before imaging. `UNVERIFIED — treatment agent, dose and route for suspected cerebral oedema require verification against the RCH clinical practice guideline.`

> [!warning] Do not apply the adult protocol to a child
> Fluid deficit estimation, rehydration rate, insulin infusion rate and the timing of insulin initiation all differ. `UNVERIFIED — every paediatric figure is omitted here. Use the RCH Clinical Practice Guideline on DKA and your local paediatric protocol. Weight-based calculation is mandatory and must not be estimated from adult figures.`

**S/Smx:** Polyuria and polydipsia, which in a young child may present as new bedwetting after being dry. Weight loss, lethargy, abdominal pain, vomiting, Kussmaul breathing. **New-onset type 1 diabetes in a child is frequently misdiagnosed as gastroenteritis or a viral illness** — the child who is dehydrated but still passing large volumes of urine is the discriminator, because a child with gastroenteritis and that degree of dehydration should be oliguric.

**Ix:** Bedside glucose and beta-hydroxybutyrate (*why:* immediate diagnosis at the front door in a child who may otherwise be triaged as gastroenteritis; *what:* hyperglycaemia with ketosis). VBG (*why:* severity grading determines fluid regimen and whether the child needs a paediatric ICU; *what:* pH and bicarbonate). UEC with sodium and chloride (*why:* corrected sodium trend is monitored specifically because a falling corrected sodium during treatment is associated with cerebral oedema risk; *what:* corrected sodium trajectory, potassium). Accurate weight (*why:* every paediatric figure is weight-based and an estimate propagates into every subsequent calculation; *what:* measured weight in kilograms). Neurological observations hourly (*why:* this is the surveillance that detects cerebral oedema; *what:* GCS, pupils, heart rate and blood pressure trend). Septic screen where a precipitant is suspected (*why:* infection is a common trigger; *what:* source).

### 0.4.1 Mx – Immediate
Senior paediatric involvement from the outset — this is not a junior-managed condition. Weigh the child. Cautious fluid resuscitation only for shock, then protocolised rehydration. Insulin is started after fluids, not simultaneously, in most paediatric protocols. Hourly neurological observations. `UNVERIFIED — all rates, volumes, the delay before insulin, and the shock-bolus criteria are omitted; obtain from RCH and local guidance.`

### 0.4.2 Mx – Definitive
Continued protocolised correction with transition to subcutaneous insulin. Paediatric endocrinology involvement for a new diagnosis, with structured family education.

### 0.4.3 Mx – Chronic/long-term
Diabetes education for child and family, school management plan, and psychosocial support. In adolescents, recurrent DKA warrants exploration of insulin omission and disordered eating — cross-refer [[M7]] Adolescent & behavioural.

---

## 0.5 HAGMA — Lactic Acidosis

**D:** High anion gap metabolic acidosis from lactate accumulation, either from tissue hypoperfusion or from impaired lactate handling.

> [!info] Type A vs Type B
> **Type A — hypoperfusion.** Shock of any cause, hypoxia, severe anaemia, regional ischaemia (mesenteric ischaemia, ischaemic limb, necrotising infection). This is the common and dangerous category.
> **Type B — no hypoperfusion.** Metformin accumulation, particularly in renal impairment; liver failure impairing clearance; thiamine deficiency; malignancy; seizures; salbutamol; alcohol; D-lactate from short bowel syndrome. `UNVERIFIED — the metformin eGFR thresholds for dose reduction and cessation require verification against the Australian Medicines Handbook.`

**A/P:** Oxygen delivery falls below cellular demand → pyruvate cannot enter the mitochondrion for oxidative phosphorylation → anaerobic glycolysis → pyruvate reduced to lactate with regeneration of NAD⁺ → lactate accumulates as an unmeasured anion. In type B, production is normal but hepatic and renal clearance is impaired, or a drug uncouples oxidative metabolism.

**S/Smx:** Those of the underlying cause. Kussmaul respiration, altered conscious state, hypotension. **The magnitude of lactate elevation correlates with mortality, and failure to clear on serial measurement is more prognostically important than the initial value.**

> [!danger] The lactate with no obvious source
> A markedly raised lactate in a patient who does not look shocked should prompt a specific search for **regional** ischaemia: mesenteric ischaemia (abdominal pain out of proportion to examination findings, atrial fibrillation), a compartment syndrome, or necrotising soft tissue infection. A normal blood pressure does not exclude a dead segment of bowel.

**Ix:** Serial lactate (*why:* clearance over hours is the prognostic and therapeutic marker, far more informative than a single value; *what:* trend). VBG with anion gap (*why:* confirms the lactate accounts for the gap, and a delta ratio suggesting otherwise means a second process; *what:* gap, delta ratio). UEC and eGFR (*why:* renal impairment both causes type B metformin accumulation and results from hypoperfusion; *what:* creatinine, eGFR). LFT (*why:* hepatic impairment reduces lactate clearance; *what:* synthetic function). Blood cultures and septic screen (*why:* sepsis is the commonest cause; *what:* source). CT mesenteric angiography where mesenteric ischaemia is plausible (*why:* the diagnosis is time-critical, missed on plain films, and the lactate may be the only abnormality; *what:* arterial occlusion, bowel wall changes, portal venous gas). Thiamine level or empirical replacement in the malnourished or alcohol-dependent (*why:* thiamine-deficient lactic acidosis responds dramatically and the level takes days; *what:* treat empirically rather than wait).

### 0.5.1 Mx – Immediate
Restore perfusion — this is the treatment for type A. Oxygen, fluid resuscitation, source control, vasopressors as indicated. Cross-refer [[F0.3]] Shock phenotypes.

### 0.5.2 Mx – Definitive
Cease the offending agent in type B. Metformin-associated lactic acidosis may require haemodialysis, which removes both metformin and lactate. `UNVERIFIED — dialysis indications require verification with the Poisons Information Centre and nephrology.` Empirical thiamine where deficiency is plausible.

### 0.5.3 Mx – Chronic/long-term
Metformin dose review against renal function, with sick-day rules that include withholding it during acute illness and before contrast — cross-refer [[H3]] Contrast-Induced Nephropathy.

---

## 0.6 NAGMA — Severe Diarrhoea

**D:** Normal anion gap (hyperchloraemic) metabolic acidosis from gastrointestinal bicarbonate loss.

**A/P:** Small bowel and pancreatic secretions are bicarbonate-rich → high-volume diarrhoea or a high-output stoma loses bicarbonate directly → the kidney retains chloride to maintain electroneutrality → **hyperchloraemia with a normal anion gap.** Potassium is lost simultaneously in stool, so hypokalaemia accompanies it.

> [!tip] Distinguishing GI loss from renal tubular acidosis
> Both give a NAGMA. The **urinary anion gap** separates them: with GI loss the kidney is appropriately excreting ammonium, so the urinary anion gap is negative; in distal RTA the kidney cannot, and the gap is positive or inappropriately non-negative. The memory hook is **"neGUTive"** — a negative urinary anion gap points at the gut. `UNVERIFIED — the urinary anion gap formula and interpretation thresholds require verification.`

> [!warning] Large-volume saline is itself a cause
> Resuscitation with large volumes of 0.9% sodium chloride produces a hyperchloraemic NAGMA. A patient resuscitated for diarrhoeal illness may have an acidosis that is partly iatrogenic — recognise it rather than escalating investigation for it.

**S/Smx:** Dehydration, hypotension, weakness from hypokalaemia, Kussmaul respiration in severe cases. History of high-volume diarrhoea, ileostomy output, or laxative use.

**Ix:** UEC with chloride (*why:* hyperchloraemia with a normal gap is the diagnosis, and chloride is often not on the default panel; *what:* raised chloride, normal gap, low potassium and bicarbonate). VBG (*why:* severity and confirmation; *what:* metabolic acidosis with normal gap). Urinary anion gap or urinary pH (*why:* separates GI from renal cause, which changes management entirely; *what:* negative gap in GI loss). Stool studies including culture, PCR and *C. difficile* toxin where relevant (*why:* identifies a treatable infective cause; *what:* pathogen — cross-refer [[K3]] C. difficile). Magnesium (*why:* co-depleted with potassium and its correction is required before potassium will replete; *what:* hypomagnesaemia). Stool output charting (*why:* quantifies ongoing losses so replacement can match them; *what:* volume per 24 hours).

### 0.6.1 Mx – Immediate
Fluid and electrolyte replacement matched to measured ongoing losses, with potassium and magnesium replacement. Balanced crystalloid rather than large-volume saline where the acidosis is already hyperchloraemic. `UNVERIFIED — replacement rates and potassium infusion limits come from local policy and are not stated here.`

### 0.6.2 Mx – Definitive
Treat the cause of the diarrhoea. Bicarbonate replacement is occasionally indicated in severe or chronic loss. `UNVERIFIED — indications and dosing require verification.`

### 0.6.3 Mx – Chronic/long-term
High-output stoma management with stoma nursing input, and monitoring for chronic acidosis and renal stones in long-standing cases.

---

## 0.7 Metabolic Alkalosis — Profuse Vomiting and Diuretic Use

**D:** Primary rise in bicarbonate with alkalaemia, most often from loss of gastric acid or from diuretic-induced chloride and volume depletion.

**A/P:**
*Vomiting:* Loss of H⁺ and Cl⁻ in gastric fluid → bicarbonate is retained → volume depletion triggers secondary hyperaldosteronism → the distal tubule reabsorbs sodium in exchange for H⁺ and K⁺ → **hypokalaemia and, characteristically, paradoxical aciduria** — acidic urine in an alkalotic patient, which seems wrong until you see the mechanism. Chloride depletion prevents the kidney from excreting the bicarbonate load, so the alkalosis is sustained until chloride is replaced.
*Diuretics:* Loop and thiazide diuretics increase distal sodium delivery and volume contraction → the same aldosterone-driven H⁺ and K⁺ loss, plus contraction alkalosis.

> [!tip] Chloride-responsive vs chloride-resistant
> **Urinary chloride is the discriminating test.**
> *Chloride-responsive (low urinary chloride):* vomiting, NG suction, prior diuretic use, post-hypercapnia. Corrects with sodium chloride and volume replacement.
> *Chloride-resistant (high urinary chloride):* primary hyperaldosteronism, Cushing syndrome, current diuretic use, Bartter and Gitelman syndromes, severe potassium depletion. Does not correct with saline; treat the endocrine cause.
> `UNVERIFIED — urinary chloride cut-off values require verification.`

> [!warning] Look for it in the surgical patient
> Prolonged nasogastric drainage, gastric outlet obstruction and pyloric stenosis all produce this picture. In an infant, hypochloraemic hypokalaemic metabolic alkalosis with projectile non-bilious vomiting is **infantile hypertrophic pyloric stenosis** until proven otherwise — and the metabolic derangement must be corrected before theatre, because it is an anaesthetic risk, not a surgical emergency. Cross-refer [[M3]] Non-bilious vomiting.

**S/Smx:** Often asymptomatic. Weakness, cramps, paraesthesia and arrhythmia from hypokalaemia. Tetany from reduced ionised calcium. Compensatory hypoventilation. Volume depletion signs.

**Ix:** UEC with chloride and potassium (*why:* hypochloraemia and hypokalaemia define the common form and both require correction; *what:* low chloride, low potassium, raised bicarbonate). VBG (*why:* confirms alkalaemia and quantifies compensation; *what:* raised pH and bicarbonate). Urinary chloride (*why:* the single test that separates the responsive from resistant categories and therefore determines treatment; *what:* low versus high). Magnesium (*why:* hypokalaemia refractory to replacement is usually hypomagnesaemia; *what:* low magnesium). Ionised calcium (*why:* alkalosis increases albumin binding and reduces the ionised fraction, causing tetany with a normal total calcium; *what:* low ionised fraction). Aldosterone and renin where chloride-resistant and unexplained (*why:* identifies primary hyperaldosteronism, an under-diagnosed and treatable cause of resistant hypertension; *what:* raised aldosterone-to-renin ratio).

### 0.7.1 Mx – Immediate
Volume and chloride replacement with sodium chloride in the chloride-responsive form, with potassium and magnesium replacement. Antiemetics and treatment of the cause of vomiting. `UNVERIFIED — fluid and potassium replacement rates from local policy.`

### 0.7.2 Mx – Definitive
Review and adjust diuretic therapy. Investigate and treat hyperaldosteronism in the chloride-resistant form. Relieve gastric outlet obstruction after metabolic correction.

### 0.7.3 Mx – Chronic/long-term
Electrolyte monitoring on long-term diuretics, and consideration of a potassium-sparing agent where hypokalaemia recurs.

---

## 0.8 Mixed Acid-Base Disorder — Salicylate Toxicity

**D:** Aspirin poisoning producing a simultaneous primary respiratory alkalosis and primary high anion gap metabolic acidosis — the classic mixed disorder.

**A/P:** Salicylate directly stimulates the medullary respiratory centre → hyperventilation → **primary respiratory alkalosis**, which appears first. Salicylate also uncouples oxidative phosphorylation → impaired ATP generation, heat production, and a shift to anaerobic metabolism → lactate accumulation, plus ketoacid and salicylate anion accumulation → **primary high anion gap metabolic acidosis**. Both are primary. As toxicity progresses and the patient tires, the respiratory component fails and the pH falls.

> [!danger] A falling pH in salicylate toxicity is a terminal sign
> Acidaemia increases the proportion of salicylate in its non-ionised form, which crosses into the CNS. **Deterioration of pH means more drug entering the brain**, and it accelerates. Never allow a salicylate-toxic patient to become acidotic, and be extremely cautious about intubation — a paralysed patient loses the compensatory hyperventilation and the pH crashes. If intubation is unavoidable, ventilation must match the pre-intubation minute volume, which is far higher than default settings.

> [!info] Age changes the picture
> Adults typically present with the mixed picture and a near-normal or alkalotic pH. **Children more often present with a frank metabolic acidosis**, having less respiratory reserve, so the classic mixed pattern may be absent.

**S/Smx:** Tinnitus and deafness (early and characteristic), nausea and vomiting, hyperventilation, sweating, hyperthermia, agitation then confusion, and in severe cases seizures, cerebral and pulmonary oedema. Chronic salicylate toxicity in the elderly is frequently misdiagnosed as sepsis or delirium.

**Ix:** Serial salicylate levels (*why:* a single level can be falsely reassuring because absorption continues, particularly with enteric-coated preparations, so a rising level on repeat changes management; *what:* level and trajectory). VBG or ABG with anion gap (*why:* identifies the mixed disorder and — critically — tracks the pH, whose fall signals CNS penetration; *what:* respiratory alkalosis plus HAGMA, then falling pH). UEC with potassium (*why:* hypokalaemia both results from the alkalosis and prevents effective urinary alkalinisation, which will fail until potassium is replete; *what:* low potassium). Glucose including bedside (*why:* CNS hypoglycaemia occurs with a normal serum glucose, and hypoglycaemia is a treatable cause of the altered mentation; *what:* glucose). Paracetamol level (*why:* co-ingestion is common; *what:* level). Coagulation profile (*why:* salicylate affects platelet function and hypoprothrombinaemia occurs; *what:* deranged INR). CXR (*why:* non-cardiogenic pulmonary oedema is a recognised severe complication; *what:* diffuse infiltrates).

### 0.8.1 Mx – Immediate
Resuscitation, glucose, and IV fluids. Correct potassium. **Urinary alkalinisation** with sodium bicarbonate traps ionised salicylate in the urine and enhances elimination — it will not work while the patient is hypokalaemic. `UNVERIFIED — bicarbonate dosing, target urinary pH, and potassium replacement targets require verification with the Poisons Information Centre and eTG.` Call 13 11 26.

### 0.8.2 Mx – Definitive
**Haemodialysis** for severe toxicity — high level, altered mental state, acidaemia, renal failure, pulmonary oedema, or clinical deterioration. `UNVERIFIED — dialysis threshold criteria require verification.` Avoid intubation where possible for the reason given above.

### 0.8.3 Mx – Chronic/long-term
Mental health assessment where deliberate. Medication review in chronic toxicity, which is usually an accumulation problem in an elderly patient with renal impairment.

---

## 0.9 Isotonic Dehydration

**D:** Volume depletion in which water and solute are lost in roughly equal proportion, leaving serum sodium and osmolality normal.

**A/P:** Loss of isotonic fluid — gastroenteritis, haemorrhage, burns exudate, third-space sequestration — → intravascular volume falls → sodium concentration is unchanged because both water and sodium left together → **the deficit is entirely extracellular**, so cells do not shrink and the neurological features of hypernatraemic dehydration are absent, but circulatory compromise develops earlier for the same volume lost.

> [!tip] Three dehydration patterns
> | | Serum Na | Fluid shift | Clinical emphasis |
> |---|---|---|---|
> | **Isotonic** | Normal | Extracellular only | Circulatory signs appear early |
> | **Hypotonic** | Low | Water moves *into* cells | Cerebral oedema risk; circulatory signs earliest |
> | **Hypertonic** | High | Water moves *out of* cells | Doughy skin, irritability, seizures; circulatory signs appear late and deceptively |

> [!warning] A normal sodium does not mean mild dehydration
> Isotonic dehydration is the commonest pattern in gastroenteritis and is easy to underestimate precisely because the biochemistry looks normal. Assess it clinically — capillary refill, heart rate, mucous membranes, urine output and, in a child, weight change against a recent recorded weight.

**S/Smx:** Tachycardia, prolonged capillary refill, dry mucous membranes, reduced skin turgor, sunken eyes and fontanelle in an infant, oliguria, postural hypotension, then hypotension and altered conscious state.

**Ix:** UEC (*why:* confirms the isotonic pattern and identifies the renal impairment that accompanies significant depletion; *what:* normal sodium, raised urea disproportionate to creatinine). VBG with lactate (*why:* quantifies the perfusion deficit when clinical signs are equivocal; *what:* raised lactate, metabolic acidosis). Weight compared against a recent documented weight, particularly in children (*why:* the most accurate available measure of deficit and superior to any clinical scoring; *what:* percentage weight loss). Urine output measurement (*why:* the most useful ongoing marker of resuscitation adequacy; *what:* output per hour). FBC (*why:* haemoconcentration, and to identify anaemia in haemorrhagic loss; *what:* raised haematocrit). Bedside glucose (*why:* hypoglycaemia in the unwell child who has not been feeding; *what:* low glucose).

### 0.9.1 Mx – Immediate
Isotonic crystalloid replacement, given as boluses with reassessment after each in shock, or as calculated replacement plus maintenance plus ongoing losses where not shocked. Oral or nasogastric rehydration is preferred in children with mild to moderate gastroenteritis and is at least as effective as IV with fewer complications. `UNVERIFIED — bolus volumes, maintenance calculations and deficit replacement rates for adults and children are omitted; use local and RCH guidance.`

### 0.9.2 Mx – Definitive
Treat the cause of the losses and match replacement to their ongoing volume.

### 0.9.3 Mx – Chronic/long-term
Oral rehydration education, and a plan for recurrence in patients with chronic high-output losses.

---

## 0.10 Third-Spacing

**D:** Sequestration of fluid into a compartment where it is not available to the circulation — bowel lumen, peritoneum, pleural space, or interstitium — producing intravascular depletion despite normal or increased total body water.

**R/Causes:** Sepsis, pancreatitis, bowel obstruction, major surgery, burns, hepatic failure with ascites, hypoalbuminaemia, anaphylaxis, trauma.

**A/P:** Inflammatory mediators injure the endothelial glycocalyx → capillary permeability rises → protein and fluid leak into the interstitium → oncotic pressure falls intravascularly and rises interstitially → further fluid follows → **the patient is simultaneously intravascularly dry and grossly oedematous.** This is the paradox that makes it a management trap: the patient looks fluid-overloaded and is in fact under-perfused.

> [!danger] The management paradox
> The oedematous, weeping, positively-balanced post-operative or septic patient may still need fluid — or may not. **Static measures (a fluid balance chart, visible oedema, a CVP number) are poor guides.** Reassess dynamically: response to a small bolus, lactate clearance, urine output, and bedside echocardiography. Getting this wrong in either direction causes harm — under-resuscitation causes acute kidney injury, over-resuscitation causes pulmonary oedema and abdominal compartment syndrome.

> [!warning] Bowel obstruction
> Litres can sit in dilated obstructed bowel with no external loss recorded anywhere on the fluid balance chart. A patient with obstruction and a "normal" fluid balance may be profoundly depleted.

**S/Smx:** Peripheral and dependent oedema, ascites, pleural effusions, weight gain, with concurrent tachycardia, oliguria, hypotension and raised lactate. Abdominal distension and rising intra-abdominal pressure in severe cases.

**Ix:** Serial lactate (*why:* distinguishes an oedematous but adequately perfused patient from one who is genuinely hypoperfused, which the clinical appearance cannot; *what:* elevation, clearance). UEC and creatinine (*why:* acute kidney injury from under-perfusion is the commonest consequence; *what:* rising creatinine, urea:creatinine ratio). Albumin (*why:* hypoalbuminaemia both causes and results from the process and confounds the anion gap; *what:* low albumin). Bedside echocardiography and dynamic assessment such as passive leg raise (*why:* dynamic measures predict fluid responsiveness where static ones do not; *what:* response in stroke volume or clinical parameters). Urine output with hourly measurement (*why:* the practical ongoing marker; *what:* output per hour). Intra-abdominal pressure measurement where distension is marked (*why:* abdominal compartment syndrome causes renal and respiratory failure and is reversible if recognised; *what:* raised pressure — `UNVERIFIED — thresholds require verification`). CXR (*why:* pulmonary oedema from over-resuscitation; *what:* interstitial oedema, effusions).

### 0.10.1 Mx – Immediate
Small fluid boluses with reassessment after each rather than large prescribed volumes. Treat the underlying inflammatory process — source control in sepsis, decompression in obstruction. Early ICU involvement where vasopressor support is needed instead of further fluid.

### 0.10.2 Mx – Definitive
Source control. Once the inflammatory insult resolves, the sequestered fluid mobilises back into the circulation over the following days, and the patient who needed fluid on day one may need diuresis on day four. Anticipating this transition is the skill.

### 0.10.3 Mx – Chronic/long-term
Deliberate de-resuscitation once stable, nutritional support, and monitoring for the pressure areas and wound healing problems that prolonged oedema causes.

---

> [!note] Cross-references
> Toxic alcohols and salicylate as poisonings → [[F0.1]] · Shock, sepsis and the distributive phenotypes → [[F0.3]] · Deteriorating patient recognition → [[A1]] 0.1 · Electrolyte-specific entries (hypercalcaemia, phosphate, magnesium) → [[I3]] · Contrast nephropathy and metformin → [[H3]]


<!-- ===== SOURCE: NEW_Acid-Base_Fluids_and_Electrolytes.md ===== -->


# NEW — Acid-Base, Fluids & Electrolytes

> [!warning] **Built standalone; merged into this file on 2026-09-01.** Every entry below was built against the header-only existence check described in `data/new_build_topics.md`. No cross-references into existing corpus files were written at build time, deliberately — these were for review first. Where an entry overlaps existing corpus content, that is for the reviewer to reconcile, not assumed absent.

> [!danger] **Sourcing limitation applying to this whole file.** Primary Australian guideline domains (`rch.org.au`, `racgp.org.au`, `tg.org.au`, `health.gov.au`, the state health services) are **blocked by this environment's egress proxy** — verified by direct test on 2026-08-30, both `curl` and `WebFetch`, 38 domains, all refused with 403 at the gateway. Only search snippets are reachable. Every entry here is therefore **snippet-sourced**: guideline names and substance are accurate as far as the snippets go, but no primary document was read. Numeric thresholds are included **only** where three independent sources agreed in retrievable snippets; where they disagreed, the figure is **omitted and the disagreement stated**, per the build rule. Do not tighten any omitted figure to a single number without a primary source.

## Dehydration

- **DDx:** the presentation is a *volume state*, not a diagnosis — the differential is the **cause**, and an intern's job is to name it rather than treat the dehydration alone.
  - **Increased losses, GI:** gastroenteritis (much the commonest in children), vomiting of any cause, high-output stoma, diarrhoea including *C. difficile*, bowel obstruction with third-space loss.
  - **Increased losses, renal:** osmotic diuresis (**hyperglycaemia — check a glucose in every unexplained dehydration**, this is the miss that matters), diuretics, diabetes insipidus, salt-wasting nephropathy, post-obstructive diuresis, adrenal insufficiency.
  - **Increased losses, skin/other:** fever, burns, heat exposure, exertional sweating, sepsis with capillary leak.
  - **Reduced intake:** frail older person with poor oral intake or dependence on carers for fluids; dysphagia post-stroke; dementia; painful oral conditions (stomatitis, tonsillitis) in children; anorexia in any acute illness; a patient deliberately restricting intake.
  - **Redistribution rather than true deficit:** sepsis, anaphylaxis, hypoalbuminaemia, cirrhosis, nephrotic syndrome, heart failure — the patient may be **intravascularly depleted while total body water is high**. This distinction changes management completely and is the single most useful conceptual point in the entry.
- **Focused Hx:** duration and volume of losses (number of vomits, stool frequency and character, stoma output); **oral intake — what and how much, actually quantified**, not "not much"; urine output (nappies in infants: number, heaviness, hours since last wet one); thirst; weight change if a recent weight is known; fever; abdominal pain; drug history with attention to **diuretics, ACE inhibitors/ARBs, NSAIDs, SGLT2 inhibitors, laxatives, metformin** (the "sick day" drugs an intern should be thinking about withholding); comorbidity — diabetes, CKD, adrenal disease, heart failure; in older people, mobility, continence, and **who normally provides drinks**; in children, feeding history and whether oral rehydration has already been tried; travel and contacts for infective causes.
- **Examination:**
  - **Haemodynamics first:** heart rate, blood pressure including **postural drop**, capillary refill, peripheral temperature and mottling, respiratory rate. **Deep sighing (acidotic) breathing points to significant acidosis** — think DKA or severe hypovolaemic shock, and escalate rather than continue a routine assessment.
  - **Volume signs:** mucous membranes, skin turgor (unreliable in older people, whose skin loses elasticity independently of hydration — a genuine pitfall), sunken eyes, **sunken anterior fontanelle in infants**, JVP, axillary sweat.
  - **Conscious state:** alert → lethargic/irritable → reduced consciousness tracks increasing severity and is one of the more reliable discriminators.
  - **Weigh the patient.** In children, **comparison against a recent pre-illness weight is the best single measure of deficit** there is; record current weight with minimal clothing.
  - **Look for the cause while examining:** abdomen for obstruction/peritonism, skin for burns or rash, evidence of sepsis.
  - **Fluid balance chart and urine output** — an intern is usually the person who ensures this is actually being recorded.

> [!warning] **Severity banding: the percentage figures did not meet the sourcing bar and are deliberately omitted.**
> Sources genuinely disagree on the percentage-weight-loss cut-offs for mild/moderate/severe paediatric dehydration. NSW Health ECAT material gives one banding; other widely used sources give different infant-versus-child cut-offs again, and the RCH percentages could not be confirmed. **Assess by the combination of clinical signs and by weight change against a known recent weight, not by a remembered percentage.**
> Two points *were* consistent across every source checked and are the ones to carry:
> - **Mild dehydration has no clinical signs.** Signs appearing at all implies at least moderate depletion — so the absence of signs does not mean the absence of a deficit.
> - **A combination of signs is more accurate than any single sign.** No individual sign, skin turgor included, is good enough alone.

- **First-line Ix:** in a well child with mild gastroenteritis and a clear history, **no blood tests are needed** — investigation is driven by severity, diagnostic doubt, or a suspected non-GI cause. Otherwise:
  - **Glucose** — immediate, in every patient, and the highest-yield single test here.
  - **UEC** for urea, creatinine and sodium (a urea rising out of proportion to creatinine supports hypovolaemia), and **potassium**, which drives immediate management.
  - **Venous blood gas** for pH, bicarbonate, base excess and lactate where the patient is unwell or acidotic breathing is present.
  - **FBC** (haemoconcentration; leucocytosis if infective), **CRP** if sepsis suspected.
  - **Urinalysis** — ketones, glucose, specific gravity, and infection.
  - **Weight**, recorded as an observation, not just noted.
  - Cause-directed: stool culture/PCR if bloody or prolonged diarrhoea, blood cultures if febrile and unwell, β-hCG in any female of reproductive age, **paired serum and urine osmolality plus urine sodium** if the sodium is deranged and the cause is unclear, **short Synacthen/cortisol** if adrenal insufficiency is genuinely suspected.

> [!info] **Sodium is the trap.** Dehydration is not one electrolyte picture. **Hypernatraemic** dehydration (free water loss exceeding sodium loss — classically the breastfed infant with poor intake, or the older person with no access to water) presents with *less* obvious volume depletion than the deficit warrants, because water shifts out of cells to defend the circulation. It carries a specific hazard: **correcting it too fast risks cerebral oedema**, so the rate of correction is a senior decision, not an intern's. The safe intern-level action is to recognise a deranged sodium, flag it early, and not run fast fluids on autopilot. **Numeric correction rates are deliberately not given here** — they were not confirmable to the three-source standard under the egress limitation above.

---

## Topics skipped in this category

None — the single topic in this category had no header match.

| Topic | Verdict |
|---|---|
| Dehydration | **BUILT** — no `##`/`###` header anywhere in the corpus matched "Dehydration" |


