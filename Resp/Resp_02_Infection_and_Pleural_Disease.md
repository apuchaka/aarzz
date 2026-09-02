---
aliases:
  - "02_Respiratory"
split_from: "Resp_merged.md"
part: "2 of 6"
---

> [!note] **Continues `02_Respiratory` from `Resp_01_Respiratory_Failure_Asthma_and_COPD`.**
> That source block is split across `Resp_01_Respiratory_Failure_Asthma_and_COPD` · `Resp_02_Infection_and_Pleural_Disease` · `Resp_03_Malignancy_Interstitial_and_Suppurative`.
> The alias `02_Respiratory` resolves to `Resp_02_Infection_and_Pleural_Disease`, which holds its largest part.

<!-- SPLIT-HEADER-END -->
## 0.8 Pneumonia

**D:** inflammation of the lungs with consolidation or interstitial infiltrates, categorised according to causative organism.

> [!note] "Pneumonia is a radiological diagnosis" — technically termed pneumonitis until confirmed by CXR.

### 0.8.1 Community-acquired pneumonia (CAP)

**D:** pneumonia acquired outside hospital or healthcare facilities.

**A:** 50% *Strep. pneumoniae*, 20% *H. influenzae*, *M. catarrhalis* (immunocompromised or chronic lung disease), *Ps. aeruginosa* (CF or bronchiectasis), *S. aureus* (CF)

**S/Smx:** cough + sputum, SOB, pleuritic chest pain, fever/rigors, confusion, night sweats

> [!danger] Signs of sepsis: ↑HR, ↑RR, ↓O2, ↓BP, fever, confusion

> [!info] Verified against Australian Therapeutic Guidelines: Antibiotic / South Australian CAP guidance, Aug 2026 — Australia's Therapeutic Guidelines emphasise clinical "red flag" assessment over CURB-65 as the primary severity tool, though SMART-COP and CURB-65 are both still used/recognised. Know CURB-65 (below) since it's still widely taught/used, but don't assume it's the sole/preferred AU severity tool the way this UK-sourced note implies.
> **CURB-65 (or CRB-65):** Confusion, Urea >7, RR ≥30, BP (SBP <90 or DBP <60), ≥65yo — still clinically useful and widely known in Australia, just not the guideline's primary recommended tool.

**Ix:** observations (*why:* vital signs are core to both diagnosis and severity assessment; *what:* feed into CURB-65/SMART-COP/red-flag assessment). CXR (*why:* required to confirm the diagnosis — pneumonia is technically a radiological diagnosis, termed pneumonitis until confirmed; *what:* consolidation or interstitial infiltrates). ABG (*why:* assesses oxygenation/severity in unwell patients; *what:* may show hypoxia ± hypercapnoea in severe disease). Bloods — U&E (*why:* renal function, part of severity scoring, and baseline before nephrotoxic antibiotics e.g. gentamicin; *what:* elevated urea contributes to severity scores), FBC (*why:* screens for the degree of inflammatory response; *what:* leucocytosis), CRP (*why:* supports the diagnosis and can be trended to monitor response; *what:* elevated), LFTs (*why:* baseline and screens for atypical organism-associated derangement e.g. Legionella; *what:* may be deranged). If sepsis suspected or severe disease: blood cultures (*why:* identifies bacteraemia and the causative organism to guide/narrow antibiotic therapy; *what:* may be positive, especially with *S. pneumoniae*), sputum culture (*why:* identifies the causative organism, particularly important if failing to improve or in severe disease; *what:* may identify the causative pathogen and sensitivities).

**P:** 30-day mortality by CURB-65 score — <5% if 0–1; 15% if 3; >25% if 4–5.

> [!info] Verified against Australian Therapeutic Guidelines: Antibiotic, Aug 2026 — Australian CAP antibiotic choices differ materially from the UK NICE regimen below; use the AU regimen. Symptom-resolution timeline is not specifically UK-jurisdiction-dependent (reflects the natural history of the illness) so is retained as general guidance.
> **Expected symptom resolution (general, not AU-specific but not contradicted by AU sources):** 1 week — fever resolves; 4 weeks — chest pain/sputum reduce markedly; 6 weeks — cough/breathlessness reduce markedly (follow-up CXR); 3 months — most symptoms resolve, fatigue may remain; 6 months — most people back to normal.
>
> **Mx based on severity (Australian Therapeutic Guidelines: Antibiotic):**
> - **Low severity** → oral amoxicillin ± doxycycline (doxycycline or clarithromycin added/substituted for atypical cover, or if penicillin-allergic)
> - **Moderate severity** → IV benzylpenicillin + oral or IV azithromycin (or doxycycline/clarithromycin as the atypical-cover partner)
> - **Severe (± ICU)** → IV benzylpenicillin + gentamicin + azithromycin (IV/PO); if confirmed severe penicillin allergy — IV ceftriaxone + azithromycin, or a respiratory fluoroquinolone as monotherapy
>
> Note the AU regimen is built around benzylpenicillin/amoxicillin + a macrolide or tetracycline for atypical cover, not the UK's co-amoxiclav-based escalation — don't reach for co-amoxiclav as the Australian severe-CAP default.

**Mx:**
- **Immediate/acute:** as per the severity-stratified antibiotic regimen above, started promptly once the diagnosis is suspected/confirmed; O2 and supportive care per severity; sepsis pathway if sepsis criteria met.
- **Definitive:** typical treatment duration 5 days for most CAP (longer if complicated, e.g. empyema, or slow to respond); de-escalate/narrow therapy once culture results available.
- **Chronic/long-term:** address modifiable risk factors (smoking cessation), ensure pneumococcal/influenza vaccination status is current, follow-up CXR at ~6 weeks particularly in smokers/older patients to ensure resolution and exclude an underlying lesion (e.g. malignancy) as the cause.

### 0.8.2 Hospital-acquired pneumonia (HAP)

**D:** acute LRTI acquired ≥48h after hospital admission, not incubating at time of admission.

**A:** early onset (<5 days after admission) — *Strep. pneumoniae*. Late onset — MRSA, *Ps. aeruginosa*, *E. coli*, *Klebsiella pneumoniae*, *Acinetobacter* spp.

> [!warning] Partially verified, with genuine additional progress this session — an Australian Government Communicable Diseases Intelligence report (2022) provides actual national antimicrobial utilisation data for Australian Hospital-Acquired Pneumonia treatment, confirming the agents in real-world Australian use are: **ceftriaxone, piperacillin-tazobactam, metronidazole, gentamicin, amoxicillin-clavulanate, and cefepime** — all consistent with, and further confirming, the severe/escalation options already in the file below (piperacillin-tazobactam, and now also amoxicillin-clavulanate as a genuine AU-relevant option not previously confirmed). **Notably, this AU utilisation data source explicitly covers parenteral (IV) agents only** — no oral agents are listed for HAP in this dataset, in contrast to CAP (where the same report and Australian Prescriber both clearly describe an oral-first approach for low-severity disease, e.g. amoxicillin ± doxycycline). This is a genuinely informative finding in itself: it suggests Australian HAP management may be more consistently parenteral-first in practice than the "non-severe oral" framing below assumes, rather than there being a well-defined, simply-unfound oral HAP regimen equivalent to the CAP one. Still worth checking current eTG directly for the specific non-severe HAP pathway if oral management is genuinely being considered for a specific patient, but this session's search suggests the oral-HAP framing itself may be a lower-yield distinction in Australian practice than in the original UK-sourced note. Local hospital antibiogram/resistance patterns matter more for HAP than CAP regardless of jurisdiction, given HAP pathogens vary significantly by institution.
> UK figures (unverified for AU use): **Non-severe:** co-amoxiclav 500/125mg tds x 5 days (or doxycycline, cefalexin, co-trimoxazole, levofloxacin). **Severe (+sepsis):** review in 48h, consider switch to PO for 5 days total; IV tazocin (piperacillin-tazobactam) 4.5g tds–qds (or ceftazidime, ceftriaxone, cefuroxime, meropenem, levofloxacin). **Suspected/confirmed MRSA:** vancomycin (or teicoplanin, linezolid).

**Mx:**
- **Immediate/acute:** empirical broad-spectrum antibiotics covering the likely organism(s) by onset timing (see above) and local resistance patterns — check local hospital antibiogram, since HAP pathogen/resistance profiles vary significantly by institution; escalate to cover MRSA/*Pseudomonas* if risk factors present or the patient is unwell/septic.
- **Definitive:** review at 48h and de-escalate/narrow based on culture results and clinical response; switch IV to oral once clinically stable and improving.
- **Chronic/long-term:** infection control measures to prevent further nosocomial infection; review need for ongoing invasive devices (lines, catheters) that may be perpetuating risk.

### 0.8.3 Atypical pneumonia
Caused by organisms that cannot be cultured normally or detected by Gram stain.

> [!tip] Mnemonic "Legions of psittaci MCQs"
> - **Legionella:** infected water supplies/air conditioning, can cause hyponatraemia — typical stem: "cheap hotel holiday, hypoNa"
> - **Chlamydia psittaci:** infected birds — typical stem: "parrot owner"
> - **Mycoplasma pneumoniae:** milder pneumonia, erythema multiforme (target lesions), neurological symptoms, cold agglutinin disease
> - **Chlamydophila pneumoniae:** rare — moderate chronic pneumonia + wheeze
> - **Coxiella burnetii (Q fever):** exposure to animals/bodily fluids — typical stem: "farmer with flu-like illness"
>
> Covered by macrolides, fluoroquinolones, or tetracyclines.

### 0.8.4 Pneumonia in immunocompromised patients

**Pneumocystis jirovecii pneumonia (PJP)**
**D:** fungal lung infection typically affecting HIV patients with CD4 <200.
**S/Smx:** may be the first presentation of HIV; fever, dry cough, dyspnoea; may present with other signs of immunocompromise (e.g. oesophageal candidiasis); pneumothorax as a complication. Extrapulmonary: hepatosplenomegaly, lymphadenopathy, choroid lesions ("moles" on the posterior uvea).
**Ix:** CXR (*why:* initial screen; *what:* bilateral interstitial infiltrates, lobar consolidation, or normal — a normal CXR does not exclude PJP). Exercise-induced desaturation (*why:* a sensitive marker even when the resting CXR/sats are near-normal; *what:* SpO2 drop on exertion supports the diagnosis). Bronchoalveolar lavage (*why:* the definitive diagnostic test when the diagnosis is uncertain; *what:* silver stain shows characteristic cysts).
**Mx:**
- **Immediate/acute:** cotrimoxazole IV/PO x 21 days; if severe — IV or aerosolised pentamidine (second-line, e.g. sulfa allergy/intolerance), consider ICU admission; if hypoxic (PaO2 <70mmHg or A-a gradient >35mmHg on room air) — add corticosteroids (reduces risk of respiratory failure and death, most benefit if started early).
- **Chronic/long-term (prophylaxis):** cotrimoxazole for patients with CD4 <200; can stop once CD4 >200 on effective antiretroviral therapy for a sustained period.

**Aspergillosis**
**D:** fungal lung infection typically affecting immunocompromised patients — allogeneic stem cell transplant (25%), haematologic malignancy (28%), solid organ transplant, AIDS.
**A:** *Aspergillus* spp. (~70% *A. fumigatus*)
**P:** inhalation of spores + neutropenia and ↓CD4 (<100) or ↓macrophage function → invasive disease; may disseminate haematogenously or via the parasinus cavity to affect multiple organs.
**S/Smx:** non-productive/mild-moderate cough, headache, fever, congestion or sinus tenderness.

> [!warning] High suspicion for pleuritic chest pain in patients with prolonged neutropenia (>10 days) + risk factors.

**Ix:** CXR (*why:* initial screen; *what:* may show nodules, cavitation, or be normal early), HRCT (*why:* more sensitive, and the characteristic "halo sign" (ground-glass around a nodule, from haemorrhage) is an early diagnostic clue prompting urgent treatment; *what:* halo sign early, "air-crescent sign" later as the lesion evolves), other scans per symptoms (*why:* screens for disseminated disease given the risk of haematogenous/parasinus spread; *what:* identifies extrapulmonary involvement), sputum culture (*why:* may identify the organism though sensitivity is limited; *what:* may grow *Aspergillus*, though a negative culture doesn't exclude invasive disease); consider BAL (*why:* higher yield than sputum for confirming the diagnosis in suspected invasive disease; *what:* galactomannan antigen testing and culture on lavage fluid).
**Mx:**
- **Immediate/acute:** voriconazole first-line (or amphotericin B, or other antifungals per local protocol/sensitivities) for invasive disease — start promptly given high mortality if treatment delayed.
- **Definitive:** reverse underlying immunosuppression where possible (e.g. reduce immunosuppressive drugs if safe to do so); aspergilloma — consider surgical removal, especially if haemoptysis.
- **Chronic/long-term:** secondary antifungal prophylaxis may be considered in patients who will remain immunosuppressed (e.g. ongoing chemotherapy).
**P:** if immunosuppression can be reversed, patients usually recover well.

### 0.8.5 Viral pneumonia/pneumonitis (including COVID-19)

> [!note] Gap-filled from CSV ("Viral Pneumonitis," Medium yield) — genuinely absent as its own entity despite bacterial pneumonia being thoroughly covered above; a striking omission given how commonly this presentation is now encountered. This entry also covers **COVID-19**, which was found to be almost entirely absent from this project during this gap-check — only passing mentions existed elsewhere (as a general URTI/gastroenteritis cause, and a noted but poorly-understood Bell's palsy association) despite it remaining clinically relevant in 2026. Verified against SA Health's COVID-19 antiviral treatment guidelines, Aug 2026.

- **D:** pneumonia caused by a respiratory virus rather than bacteria — influenza (see [[08_05-06_Infectious_Disease_-_Viral_Infections]] Influenza, not repeated here), RSV, adenovirus, parainfluenza, and SARS-CoV-2 (COVID-19) are the most clinically significant causes; genuinely important to distinguish from bacterial pneumonia given the different Ix priorities and the fact **antibiotics provide no benefit for a purely viral pneumonia** — unnecessary antibiotic use in this context is a recognised antimicrobial stewardship concern, not a harmless "just in case" measure.
- **S/Smx:** often a more gradual onset than typical bacterial CAP, though this is a general tendency rather than a reliable discriminator; fever, dry cough (more classically than the productive cough of bacterial pneumonia, though this overlaps considerably), dyspnoea, myalgia/systemic symptoms often prominent. **Secondary bacterial pneumonia is a genuinely important complication to actively consider** — a patient who initially improves then deteriorates again ("biphasic" pattern), or who develops purulent sputum/new focal signs after an initial viral illness, should prompt reassessment for secondary bacterial superinfection, which *does* need antibiotics.
- **Ix:** viral PCR/rapid antigen testing (nasopharyngeal swab, or lower respiratory sample in more severe/hospitalised disease) to confirm the causative virus and inform isolation/infection control precautions; CXR (may show bilateral, more diffuse/interstitial changes than the lobar consolidation more typical of bacterial pneumonia, though this pattern is not fully reliable for distinguishing the two); inflammatory markers and other bloods as clinically indicated, noting **CRP is often less markedly elevated in viral pneumonia than in bacterial pneumonia** (see [[Investigation-Interpretation]] Inflammatory Markers (CRP and ESR) for the general kinetics/interpretation principle this reflects, not repeated here) — a genuinely useful, though imperfect, discriminating clue.

**COVID-19 specifically:**
- **S/Smx:** ranges from asymptomatic/mild upper respiratory illness to severe pneumonia and ARDS — fever, cough, dyspnoea, fatigue, myalgia, anosmia/ageusia (loss of smell/taste, a relatively distinctive early feature though less prominent with more recent variants than earlier in the pandemic).
- **Mx — risk-stratified, time-critical treatment for eligible patients, similar in principle to the influenza antiviral-timing point established elsewhere in this project:**
  - **Oral antivirals (nirmatrelvir/ritonavir — brand name Paxlovid — first-line; molnupiravir where nirmatrelvir/ritonavir is contraindicated):** genuinely time-critical, most effective when started within 5 days of symptom onset, in patients with mild-to-moderate disease who have ≥1 risk factor for progression to severe disease (age, immunosuppression, significant comorbidity). **Nirmatrelvir/ritonavir has clinically significant drug interactions given ritonavir's potent CYP3A4-inhibiting effect** (affecting many statins, anticoagulants, and cardiac medications) — a full medication review is genuinely necessary before prescribing, not an optional check; this is the main reason molnupiravir is sometimes chosen instead despite being generally less preferred.
  - **Remdesivir (IV):** reserved for very-high-risk patients, per current Australian statewide clinical guidelines, including via hospital-in-the-home-type community programs in some jurisdictions.
  - **Supportive care and escalation** (oxygen, and for more severe/hospitalised disease, corticosteroids and other interventions per current inpatient protocols) for patients with more significant illness — not detailed further here, given rapidly evolving practice in this specific area.
  - **Vaccination remains a core prevention strategy**, consistent with the same principle established for influenza above.
- A genuinely important general point: COVID-19 management guidance has evolved substantially and continues to evolve as variants and evidence change — always check current local/state guidance directly for the specific current recommendations, given this is one of the more actively-revised areas of practice.

**Long COVID (post-COVID-19 condition):**
- **D:** persistent or new symptoms continuing beyond the expected acute recovery period — the WHO working definition specifies onset **usually within 3 months of the acute COVID-19 illness, with symptoms lasting at least 2 months**, not explained by an alternative diagnosis, and impacting the person's ability to carry out everyday functions (this exact 3-month/2-month framing is genuinely specific and worth knowing given definitions have varied — some literature instead uses a simpler ">12 weeks of persistent symptoms" cutoff; both are in current use). The WHO has explicitly noted this definition may continue to evolve as more evidence emerges, so treat the exact cutoffs as the current working definition rather than a permanently fixed threshold.
- **S/Smx:** genuinely multi-system and highly variable — over 200 individual symptoms have been reported across different patients. The most consistently reported core symptoms are **fatigue, dyspnoea, and cognitive impairment ("brain fog")**, alongside myalgia, sleep disturbance, and a wide range of other possible respiratory, cardiovascular, neurological, and gastrointestinal symptoms depending on the individual. **Post-exertional malaise** (a worsening of symptoms after physical or cognitive exertion, often delayed) is a recognised and important feature in a subset of patients, given it directly informs the "pacing" approach to activity described below — pushing through fatigue as if it were simple deconditioning can worsen rather than improve the condition in these patients. There is significant symptom and presentation overlap with myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS), and roughly half of long COVID patients meeting long COVID criteria also meet ME/CFS criteria.
- **R:** risk factors are not yet fully settled in the literature, but current data suggests female sex and age 40–50 are more commonly represented; severity of the acute COVID-19 illness does **not** reliably predict long COVID risk — even patients with mild or non-hospitalised acute infection can develop it, a genuinely important point given it means long COVID shouldn't be dismissed as implausible just because the acute illness was mild. Australian data suggests the overall prevalence in Australia is comparatively low, attributed to high vaccination rates and the population's predominant exposure to less severe (Omicron-era) variants.
- **Ix:** primarily a clinical diagnosis of exclusion — directed at ruling out alternative explanations for the specific symptoms present (e.g. new cardiac, respiratory, or neurological pathology) rather than a single confirmatory test, given no specific biomarker for long COVID currently exists.
- **Mx:** **no single specific treatment exists — management is symptom-directed and multidisciplinary**, not a standardised protocol. RACGP provides a structured patient resource (a post-COVID-19 symptoms diary) to help track symptoms and guide management over time. Key general principles: **pacing/energy conservation** (particularly relevant given the post-exertional malaise feature above — graded activity should be individualised and cautious rather than assuming a standard "push through it" rehabilitation approach), symptom-specific referral where indicated (e.g. respiratory, cardiology, neuropsychology), and psychological support given the genuine impact on function and quality of life. Long COVID clinics/multidisciplinary programs exist in some Australian regions for more complex or persistent presentations.
- **P:** most patients show significant symptom reduction by around 1 year post-acute infection, though the trajectory is genuinely variable and some patients experience a relapsing-remitting course rather than steady improvement.

---

## 0.17 Aspiration Pneumonia and Pneumonitis

> [!note] Gap-filled from CSV (under "Pneumonia (including atypical, CAP, HAP, aspiration)" — Medium yield) — not covered as a distinct entity in the source UK notes, which cover CAP/HAP/atypical/immunocompromised pneumonia but not aspiration specifically.

**D:** Two distinct entities that are often conflated: **aspiration pneumonitis** (chemical injury from aspirated gastric contents, sterile inflammation) vs **aspiration pneumonia** (bacterial infection following aspiration of oropharyngeal/gastric contents containing pathogenic bacteria).

**R:** impaired consciousness (sedation, alcohol, seizure, anaesthesia), swallowing dysfunction (stroke, neurodegenerative disease, oesophageal disease), reduced gag reflex, prolonged intubation/tube feeding, poor dentition/oral hygiene (increases bacterial load of aspirate).

**A/P:** aspiration of gastric acid causes direct chemical injury (pneumonitis) — up to 25% of these patients go on to develop a superimposed bacterial infection (aspiration pneumonia) over the following days. Aspiration of oropharyngeal contents containing bacteria causes aspiration pneumonia directly, typically affecting gravity-dependent lung segments (posterior upper lobes/apical lower lobes if aspiration occurred supine; basal segments if upright).

**S/Smx:** witnessed or suspected aspiration event, cough, dyspnoea, fever (may be delayed if evolving from pneumonitis to superimposed infection), signs of consolidation in the affected (typically dependent) segment.

**Ix:** CXR (*why:* confirms and localises consolidation, typically in gravity-dependent segments; *what:* infiltrate in the expected dependent segment based on the aspiration event's positioning). Bloods, sputum/blood cultures where practical, ideally before antibiotics if the patient is stable enough (*why:* culture yield is low but still worth attempting in cases severe enough to warrant hospitalisation; *what:* often unrevealing given polymicrobial/anaerobic flora that's hard to culture).

**Mx:**
- **Immediate/acute:** clear the airway of fluid/particulate matter as soon as possible after a witnessed aspiration event; consider intubation if the patient cannot protect their own airway.
- **Definitive — a key distinction most learners miss:** for **pure chemical pneumonitis** with no evidence of bacterial infection, prophylactic antibiotics are **not** evidence-based and may select for resistant organisms — a reasonable approach is to withhold antibiotics where the picture is clearly chemical, and start empirical treatment if there's no improvement within 48h, or if pneumonitis can't be confidently distinguished from bacterial pneumonia. For **aspiration pneumonia** (established/likely bacterial infection), antibiotics are the key treatment — empirical choice should cover typical CAP/HAP organisms per setting; routine additional anaerobic cover (e.g. metronidazole) is debated and not clearly evidence-based in most cases — reserve specific anti-anaerobic therapy for suspected lung abscess/empyema rather than using it routinely for every aspiration pneumonia.
- **Chronic/long-term:** speech pathology swallow assessment to identify and manage the underlying aspiration risk (thickened fluids, modified diet, positioning); optimise oral hygiene/dental care (reduces the bacterial load of any future aspiration); address the underlying cause where possible (e.g. reflux management, medication review for sedating drugs).

> [!warning] Partially resolved — a Medical Journal of Australia article directly cites Therapeutic Guidelines: Antibiotic as recommending **empirical benzylpenicillin + metronidazole** for aspiration pneumonia specifically (distinct from standard CAP choices, and reflecting the anaerobic-cover debate discussed below). This is a genuine, specific AU-sourced regimen — but the citation is to the 2010 edition of eTG, and antibiotic guidelines are updated periodically, so the exact drug choice should still be checked against the *current* eTG edition rather than assumed unchanged over 15+ years. **The higher-yield teaching point is now even more strongly supported**: the British Thoracic Society's 2023 clinical statement explicitly states routine anti-anaerobic coverage is not required for aspiration pneumonia except in specific circumstances, and a large 2024 multicentre cohort study (18 hospitals, ~4,000 patients) found no mortality benefit from extended anaerobic coverage — if anything, a non-significant trend toward *higher* mortality (adjusted risk difference +1.6%) with broader anaerobic-covering regimens, alongside the added *C. difficile* risk broader-spectrum antibiotics carry. This makes "chemical pneumonitis vs bacterial pneumonia" and "routine anaerobic cover is increasingly not recommended" the genuinely well-evidenced, current teaching points, regardless of the exact drug specifics, which should still be checked against current eTG.

---

## 0.16 Acute Bronchitis

> [!note] Gap-filled from CSV (Respiratory category, Medium yield) — not covered in the source UK notes.

**D:** Self-limiting inflammation of the bronchi, usually viral, causing an acute cough illness without evidence of pneumonia.

**R:** smoking, exposure to irritants, viral URTI preceding it (most cases follow a cold).

**A/P:** most commonly viral (similar viruses to the common cold/influenza); occasionally bacterial (*Mycoplasma*, *Bordetella pertussis*, *Chlamydophila*). Inflammation of the bronchial mucosa → cough, increased mucus production, without alveolar consolidation (distinguishing it from pneumonia).

**S/Smx:** cough (may be productive), lasting up to 3 weeks; may follow a URTI; mild systemic symptoms (low-grade fever, malaise); wheeze may be present; importantly — **no** focal chest signs of consolidation, and the patient is not systemically unwell in the way pneumonia typically presents.

**Ix:** clinical diagnosis (*why:* Ix is generally unnecessary in typical presentations without red flags; *what:* diagnosis rests on history/exam). CXR (*why:* only if pneumonia can't be confidently excluded clinically, or red flags present (e.g. haemoptysis, significant systemic upset, risk factors for TB/malignancy); *what:* used to exclude consolidation, not to confirm bronchitis itself).

**Mx:**
- **Definitive (this is a self-limiting illness — no separate acute/chronic tiers needed):** supportive care — analgesia/antipyretics, adequate hydration, advise about expected duration (cough can persist up to 3 weeks even as the illness resolves).
- **Antibiotics:** not routinely indicated — most cases are viral; consider only if a bacterial cause is suspected (e.g. pertussis in the right clinical context) or in patients at higher risk of complications (frail, significant comorbidity).
- Safety-net: advise re-presentation if symptoms worsen, fail to improve as expected, or red flags for pneumonia develop.

---

## 0.21 Upper Respiratory Tract Infection (URTI)

> [!note] Gap-filled from CSV (Respiratory category, High yield, "unlikely covered") — not covered as a standalone topic in the source UK notes, likely because it's usually considered low-complexity/self-evident, but flagged as high-yield in the CSV so given a brief dedicated entry.

**D:** Infection of the upper respiratory tract — nose, sinuses, pharynx, larynx — most commonly viral, encompassing the "common cold," pharyngitis, sinusitis, and laryngitis.

**A:** overwhelmingly viral (rhinovirus most common; also coronavirus, adenovirus, influenza, parainfluenza, RSV); bacterial causes (e.g. group A strep pharyngitis) are a minority but clinically important given specific antibiotic-responsive Mx and rare but serious complications (rheumatic fever — see [[01_Cardiovascular]] 0.22 — and peritonsillar abscess).

**S/Smx:** nasal congestion/rhinorrhoea, sore throat, cough, low-grade fever, malaise — typically self-limiting over 7–10 days.

> [!danger] Red flags distinguishing a concerning presentation from simple URTI: stridor/drooling (epiglottitis — emergency), unilateral tonsillar swelling with trismus (peritonsillar abscess/quinsy), neck stiffness (meningitis), significant systemic toxicity out of proportion to a simple URTI.

**Ix:** clinical diagnosis in the vast majority of cases (*why:* Ix rarely changes Mx for typical URTI; *what:* diagnosis on history/exam). Throat swab/rapid strep test (*why:* used when bacterial pharyngitis is suspected (e.g. using a validated clinical score such as Centor/McIsaac criteria) to guide antibiotic decisions and reduce unnecessary prescribing; *what:* positive supports group A strep as the cause).

**Mx:**
- **Definitive (self-limiting in the large majority):** supportive care — analgesia/antipyretics, fluids, rest; reassurance about expected duration.
- **Targeted (confirmed/high-probability bacterial pharyngitis):** penicillin V (or amoxicillin) for confirmed/high-probability group A strep pharyngitis, particularly relevant in populations/regions with higher rheumatic fever risk (see [[01_Cardiovascular]] 0.22 and the Australian Context of Health/Aboriginal & TSI Health category for RHD-endemic-region considerations).
- **Chronic/long-term:** not applicable to simple URTI; recurrent tonsillitis may warrant ENT referral for consideration of tonsillectomy if meeting frequency/severity criteria.

---

## 0.9 Tuberculosis

**D:** infectious disease caused by *Mycobacterium tuberculosis*.

**R:** prolonged exposure, birth in an endemic country (Asia, Latin America, Africa), HIV and immunosuppression (reactivation), silicosis, apical fibrosis

**A/P (pathogenesis sequence):**
1. Inhalation of TB
2. Engulfed by alveolar macrophages
3. Survives and multiplies within macrophages
4. Kills macrophages → released
5. Migrates to regional lymph nodes — affected node + lesion = Ghon complex
6. TH1 response → granuloma formation (Type IV hypersensitivity) — central caseous necrotic material, peripheral granulation tissue (macrophages, lymphocytes) → latent infection, non-infectious, normal CXR, tuberculin skin test positive
7. Reactivation due to immunosuppression → disseminated (miliary) TB

**S/Smx:** cough, fatigue, weight loss, night sweats, haemoptysis, clubbing

### 0.9.1 Diagnosis of latent TB — Mantoux test
0.1 mL of 1:1,000 purified protein derivative (PPD) injected intradermally; result read 2–3 days later.
- **<6mm:** negative (no reaction) — give BCG if unvaccinated
- **6–15mm:** previous BCG or TB infection — do not give BCG
- **>15mm:** positive — suggests TB infection

**False negatives:** miliary TB, sarcoidosis, HIV, lymphoma, age <6 months

### 0.9.2 Diagnosis of active TB
- CXR (*why:* screens for characteristic active-disease patterns; *what:* upper lobe cavitation, bilateral hilar lymphadenopathy)
- Sputum smear (*why:* rapid, allows immediate infection-control decisions while awaiting culture; *what:* 3 samples, stained acid-fast; sensitivity 50–80%, reduced in HIV (20–30%))
- Sputum culture (*why:* gold-standard diagnostic test, and the only method allowing drug-sensitivity testing; *what:* 1–3 weeks in liquid media, longer in solid media)
- NAAT (*why:* bridges the gap between the fast-but-less-sensitive smear and the slow-but-definitive culture, useful for early rifampicin-resistance screening; *what:* rapid diagnosis (within 48h); more sensitive than smear, less sensitive than culture)

### 0.9.3 Mx of active TB

> [!info] Verified — the RIPE regimen is WHO-endorsed and used essentially identically in the Australian TB program (state/territory-based, e.g. via specialist TB services); no material dosing/duration difference identified from the international standard below.
> **4 drugs for 2 months, 2 drugs for 4 months:**
> - Rifampicin & isoniazid for 6 months (with pyridoxine/B6)
> - Pyrazinamide & ethambutol for 2 months
>
> **Mx tiering:** this is the **definitive/chronic** treatment course — active TB doesn't have a separate "immediate" pharmacological tier beyond starting this regimen promptly on diagnosis; the immediate priority alongside starting treatment is infection control (isolation/airborne precautions until deemed non-infectious) and mandatory notification to the state/territory public health unit (TB is a notifiable disease in Australia).

### 0.9.4 Mx of latent TB

> [!danger] **Correction, found by the verification-box scope audit in M8 (2026-08-29).** This entry previously gave **"rifampicin + isoniazid for 3 months, OR isoniazid alone for 6 months"** — the first of those is the **UK (3HR) regimen** and is not the standard Australian option.
>
> **The Australian regimens** are **isoniazid daily for 6–9 months (6–9H)** or **rifampicin monotherapy daily for 4 months (4R)** — rifampicin *alone*, not combined, and for **4** months rather than 3. The shorter **3HP** regimen (isoniazid + rifapentine weekly for 12 weeks) is established internationally and has been used in some Australian services, but check local availability before quoting it as standard. See `PENDING_GUIDELINE_CHECKS.md` **B38**.
>
> **How it survived, and it is the second instance of this shape this session.** The verification box above covers the **active-TB RIPE regimen** — it says "no material dosing/duration difference identified" — and that statement is about RIPE. **Latent TB is a different regimen** and was never in the box's scope, but it sits directly beneath it under the same heading structure, so it inherits the box's apparent authority. This is the same failure as the paediatric adrenaline timing in `15_01a`: a box that is accurate about what it names, silent about what it does not, and read as covering the block.

**Mx:** **isoniazid daily for 6–9 months (6–9H)**, or **rifampicin monotherapy daily for 4 months (4R)** — with **pyridoxine (B6)** alongside any isoniazid-containing regimen, as for active TB above.

### 0.9.5 Drug adverse effects
| Drug | Adverse effects |
|---|---|
| Rifampicin | liver enzyme inducer, red urine, hepatotoxicity |
| Isoniazid | peripheral neuropathy (give B6!), agranulocytosis, hepatotoxicity, liver enzyme inhibitor |
| Pyrazinamide | hyperuricaemia causing gout, arthralgia, myalgia, hepatotoxicity |
| Ethambutol | optic neuritis — check visual acuity before and during treatment |

### 0.9.6 Secondary / extra-pulmonary TB
Tuberculous meningitis (CNS), Pott's disease (vertebral bodies), scrofuloderma (cervical lymph nodes), renal, GI, or any other site; disseminated TB (multiple organs, haematogenous spread) — higher mortality than pulmonary TB.

---

## 0.12 Pleural Effusions

> [!warning] FLAG 2026-09-01, CORRECTED 2026-09-02 — **Light's criteria appear in NO file. This flag previously said three.**
> The three it named do not carry them. **This section** has a protein-only table (transudate <30 g/L,
> exudate >30 g/L) — a different rule, not Light's. **`Investigation-Interpretation §1.4 Pleural Fluid
> Analysis`** says *"Apply Light's criteria ... see [[02_Respiratory]] Pleural Effusions for the full
> criteria"* — a forward reference to criteria that are not here. **`GP_merged`'s LDH entry** names two
> of the three in passing (*"pleural:serum LDH ratio and absolute pleural LDH form two of the three"*)
> and states no threshold. **So the protein ratio >0.5, the LDH ratio >0.6 and the LDH above two-thirds
> of the serum upper limit are in the corpus nowhere.** Recorded in `_meta/MY_TASKS.md`; not written
> here, because they need an Australian source rather than my memory.

| Transudate (<30 g/L protein) | Exudate (>30 g/L protein) |
|---|---|
| Heart failure | Infection |
| Hypoalbuminaemia | Connective tissue disease (RA, SLE) |
| Hypothyroidism | Neoplasm |
| Meig's syndrome (benign ovarian tumour + ascites) | Pancreatitis |
| | Pulmonary embolism |
| | Dressler's syndrome |
| | Yellow nail syndrome |

**Ix:** CXR (*why:* screens for and roughly quantifies the effusion; *what:* blunted costophrenic angle, meniscus sign). Pleural USS (*why:* confirms the effusion, guides safe drainage, and can suggest loculation/complexity; *what:* anechoic (simple) vs echogenic/septated (complex/exudative) appearance). Diagnostic pleural aspiration with Light's criteria (*why:* the key test distinguishing transudate from exudate when the cause isn't clinically obvious, directing the differential above; *what:* protein/LDH ratios classify as exudate if any of: pleural:serum protein >0.5, pleural:serum LDH >0.6, or pleural LDH >2/3 upper limit of normal serum LDH).

**Mx:**
- **Immediate/acute:** therapeutic drainage for large/symptomatic effusions, or if empyema/complicated parapneumonic effusion is suspected (pH <7.2, or frank pus — needs drainage, not just antibiotics).
- **Definitive:** treat the underlying cause identified from the transudate/exudate differential (e.g. diuresis for HF, antibiotics ± drainage for infection, oncological management for malignant effusion).
- **Chronic/long-term:** recurrent malignant effusions may need pleurodesis or an indwelling pleural catheter for symptom control.

---

## 0.19 Empyema and Haemothorax

> [!note] Gap-filled from CSV (Respiratory category, Medium yield, "unlikely covered") — not covered as standalone entities in the source UK notes; mentioned only implicitly via CAP complications and the pneumothorax decision pathway (haemothorax as a high-risk feature).

**Empyema**

**D:** Frank pus in the pleural space, typically evolving from an untreated or inadequately treated parapneumonic effusion.

**A/P:** parapneumonic effusion (simple, exudative, sterile) → bacterial invasion of the pleural space → complicated parapneumonic effusion (positive culture/Gram stain, low pH) → frank pus (empyema) if untreated, often with loculation as fibrin deposits organise the collection.

**S/Smx:** persisting/worsening fever and systemic illness despite antibiotics for pneumonia, pleuritic chest pain, dyspnoea — the key clinical clue is a patient with pneumonia not responding to appropriate antibiotics as expected, prompting a search for an undrained collection.

**Ix:** CXR/pleural USS (*why:* identifies the effusion and can suggest complexity/loculation; *what:* effusion, possibly septated/loculated). Diagnostic pleural aspiration (*why:* confirms the diagnosis and distinguishes simple parapneumonic effusion from complicated/empyema, which changes Mx from antibiotics-alone to requiring drainage; *what:* frank pus, or fluid with pH <7.2, low glucose, positive Gram stain/culture — any of these mandate drainage, not antibiotics alone).

**Mx:**
- **Immediate/acute:** chest drain insertion for any complicated parapneumonic effusion or frank empyema (antibiotics alone are inadequate once fluid is infected/complicated) + continue systemic antibiotics.
- **Definitive:** intrapleural fibrinolytics (e.g. alteplase + DNase) for loculated collections not draining adequately; VATS (video-assisted thoracoscopic surgery) for surgical decortication if medical drainage fails.
- **Chronic/long-term:** ensure adequate treatment duration (often longer courses than uncomplicated pneumonia) and follow-up imaging to confirm resolution.

**Haemothorax**

**D:** Blood within the pleural space, most commonly from chest trauma; also iatrogenic (post-procedure) or from an underlying pathology (e.g. malignancy, ruptured aneurysm, anticoagulation-related).

**A/P:** disruption of intrathoracic vessels (intercostal, pulmonary, or great vessels), or bleeding into the pleural space from a pre-existing lesion → blood accumulation → potential for both hypovolaemic shock (from blood loss) and respiratory compromise (from lung compression), i.e. it is both a "shock" and a "respiratory" emergency simultaneously.

**S/Smx:** as per pneumothorax/pleural effusion (dyspnoea, chest pain, reduced breath sounds, dullness to percussion — dullness distinguishes it from the hyper-resonance of pneumothorax) plus signs of hypovolaemic shock if significant blood loss.

**Ix:** CXR (*why:* screens for the collection, though may under-represent volume if the patient is supine (trauma setting); *what:* effusion/opacification, may be difficult to distinguish acutely from pleural fluid on CXR alone). CT chest (*why:* better characterises the volume and source, especially in trauma work-up; *what:* confirms haemothorax and may identify the bleeding source). FBC, group & crossmatch (*why:* assesses the degree of blood loss and prepares for possible transfusion; *what:* falling Hb, baseline for transfusion).

**Mx:**
- **Immediate/acute:** ABCDE resuscitation as for hypovolaemic shock (see `[[Emergency and Crit Care_merged]] 01_Cardiovascular §0.20.2 Hypovolaemic shock`) alongside chest drain insertion (large-bore) to drain the haemothorax and monitor ongoing blood loss via drain output.
- **Definitive:** urgent thoracotomy/surgical exploration if massive haemothorax (e.g. >1500mL immediate drain output, or ongoing output >200mL/hr) or haemodynamic instability despite resuscitation — significant ongoing bleeding needs surgical source control, not just drainage.
- **Chronic/long-term:** monitor for retained haemothorax (undrained clot) which can organise into a fibrothorax if inadequately evacuated — may need VATS for evacuation if this develops.

---

## 0.11 Pneumothorax

**D:** air within the pleural space.
- **Primary:** occurs in people with no known respiratory illness
- **Secondary:** pre-existing respiratory illness
- **Tension:** usually secondary to trauma

**R:** smoking, pre-existing lung disease (COPD, asthma, CF, lung cancer, PJP), Marfan syndrome (M>F, young), RA, ventilation (including non-invasive)

**A/P:** spontaneous, traumatic, iatrogenic, or underlying lung pathology.
> [!note] Catamenial pneumothorax — 3–6% of spontaneous pneumothoraces in menstruating women, secondary to intrathoracic endometriosis.

**S/Smx:** SOB, chest pain (often pleuritic), sweating, ↑HR, ↑RR. In tension pneumothorax: ↓breath sounds, tracheal tug (late/rare sign).

**Ix:** CXR (*why:* confirms the diagnosis and quantifies size; *what:* visible pleural line with absent lung markings peripheral to it). If tension pneumothorax is suspected, proceed to management immediately — don't wait for imaging.

> [!danger] Mx of tension pneumothorax
> Large-bore cannula into the 2nd intercostal space at the mid-clavicular line → once pressure is relieved, insert a chest drain.

### 0.11.1 Mx of spontaneous pneumothorax

**Decision pathway (Immediate/acute → Definitive, tiered by risk features):**
- **Immediate/acute:** tension pneumothorax → needle decompression as above; assess for high-risk features (haemodynamic compromise, significant hypoxia, bilateral pneumothorax, underlying lung disease, ≥50yo + significant smoking history, haemothorax).
- **Definitive:** if no high-risk features and safe to intervene based on imaging size (CXR ≥2cm laterally or apically) — choice of conservative Mx, ambulatory device (e.g. Rocket Pleural Vent), or needle aspiration. If <2cm, get CT for drainage under interventional radiology (IR) if intervention needed.
  - **Aspiration:** insertion of a fine needle (14G) into the 2nd intercostal space at the mid-clavicular line. If unsuccessful, proceed to chest drain.
  - **Chest drain:** insertion of a large drain via incision at the safe triangle; external end placed under water — air exits and bubbles through; swinging should be seen with respiration.
> [!warning] Complications: air leaks (persistent bubbling on coughing), surgical emphysema.
  - **If no resolution:** video-assisted thoracoscopic surgery (VATS), mechanical/chemical pleurodesis ± bullectomy — surgical methods: abrasive pleurodesis (direct physical pleural irritation), chemical pleurodesis (e.g. talc), pleurectomy (removal of the pleura).
- **Chronic/long-term:** review every 2–4 days as outpatient if managed conservatively; if secondary pneumothorax, monitor as inpatient; if stable, follow up in 2–4 weeks. Address recurrence risk — VATS/pleurodesis considered after a first contralateral or second ipsilateral spontaneous pneumothorax given the recurrence risk.

> [!info] Verified — CASA (Australia's civil aviation authority) does not publish its own separate figure for passenger flying after pneumothorax and effectively defers to airline/international guidance; the widely-used international standard (originating from BTS but adopted broadly, including by airlines Australian patients fly with) matches what's below, so this is not meaningfully "UK-specific" content requiring a different AU figure.
> - Stop smoking
> - Only fly 2 weeks after successful drainage, or 1 week post clear CXR (spontaneous); allow longer (~2 weeks) for traumatic pneumothorax
> - Permanently avoid diving unless complete resolution (and, per most sources, unless a definitive procedure — e.g. pleurectomy — has been performed, given the risk of recurrence at depth)

---

