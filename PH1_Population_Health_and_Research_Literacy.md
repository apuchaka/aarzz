---
block: Public Health, Epidemiology & Research Literacy
source: built in chat, model knowledge, NOT source-verified
---

> [!warning] Sourcing — and why this file has fewer flags than the others
> Written from model knowledge, not retrieved from source. **Unlike the clinical files, most of this material is MATHEMATICAL OR DEFINITIONAL rather than guideline-dependent — sensitivity does not change between jurisdictions or get revised by a committee.** **The definitions, formulae and concepts here are reliable.**
> **What DOES require verification is flagged: the Australian screening programmes (ages, intervals and tests change), the notifiable disease list, and the immunisation schedule.** Verify against **SA Health**, the **Australian Immunisation Handbook**, and the relevant national screening programme sites.

---

## 0.1 Study Design

> [!tip] The hierarchy — with the caveat that matters
> **Systematic review and meta-analysis of RCTs > randomised controlled trial > cohort study > case-control study > cross-sectional study > case series and case report > expert opinion.**
> **THE CAVEAT: a well-conducted cohort study is better evidence than a poorly conducted RCT.** **Design determines the CEILING of evidence quality; CONDUCT determines whether it gets there.** The hierarchy is about study type, not about any individual study.
> **And the best design depends on the QUESTION**: RCTs answer questions about treatment effect; cohorts answer questions about prognosis and harm; qualitative research answers questions about experience and acceptability; and no RCT will ever be done on whether parachutes work.

> [!info] The observational designs — and the direction each one runs
> **· CROSS-SECTIONAL — a snapshot at one point in time.**
> **Measures PREVALENCE. Quick, cheap, useful for health service planning.**
> **CANNOT ESTABLISH TEMPORALITY — you cannot tell whether the exposure preceded the outcome — so it is weak for causation.**
> **· CASE-CONTROL — starts with the OUTCOME and looks BACKWARD at exposure.**
> **STRENGTHS: efficient for RARE OUTCOMES and for diseases with LONG LATENCY; cheap; quick; can examine multiple exposures.**
> **WEAKNESSES: cannot measure incidence or absolute risk · highly vulnerable to RECALL BIAS and SELECTION BIAS (choosing appropriate controls is the central difficulty) · measures the ODDS RATIO.**
> **· COHORT — starts with the EXPOSURE and follows FORWARD in time.**
> **STRENGTHS: establishes TEMPORALITY · measures INCIDENCE and RELATIVE RISK · good for RARE EXPOSURES · can examine multiple outcomes from one exposure.**
> **WEAKNESSES: expensive and slow (if prospective) · LOSS TO FOLLOW-UP is the principal threat to validity · inefficient for rare outcomes · still subject to confounding.**
> **THE MEMORY AID: CASE-CONTROL looks BACK from the disease. COHORT follows FORWARD from the exposure.**

> [!warning] The randomised controlled trial — and its one unique property
> **RANDOMISATION IS THE ONLY METHOD THAT CONTROLS FOR UNKNOWN AND UNMEASURED CONFOUNDERS.**
> **Statistical adjustment can only control for confounders you have thought of and measured. Randomisation controls for the ones you have not.** **That single property is why the RCT sits where it does in the hierarchy.**
> **The features that determine whether an RCT is any good:**
> **· ALLOCATION CONCEALMENT — the person recruiting cannot know what the next allocation will be. Distinct from blinding, and arguably more important, because it prevents selective recruitment.**
> **· BLINDING — of participants, clinicians, assessors and analysts. Outcome assessor blinding matters most for subjective outcomes.**
> **· INTENTION-TO-TREAT ANALYSIS — see 0.4.**
> **· Adequate power, appropriate outcomes, and complete follow-up.**
> **Limitations: cost · limited EXTERNAL VALIDITY (trial populations are younger, healthier and less comorbid than real patients) · ethical constraints · and poor suitability for rare or very long-term outcomes.**
> **Variants: CROSSOVER (each participant is their own control — only for stable chronic conditions) · CLUSTER randomised (randomising groups, e.g. general practices) · FACTORIAL (testing two interventions at once) · STEPPED WEDGE · and NON-INFERIORITY trials, which ask whether a new treatment is not meaningfully worse (usually because it is cheaper, safer or easier).**
> **PRAGMATIC trials test effectiveness in real-world conditions; EXPLANATORY trials test efficacy under ideal conditions.**

> [!tip] Systematic reviews, and reading a forest plot
> **A SYSTEMATIC REVIEW uses a pre-specified protocol to find and appraise all relevant studies. A META-ANALYSIS statistically pools them. A review can be systematic without a meta-analysis, and pooling heterogeneous studies is worse than not pooling them.**
> **HETEROGENEITY — how much the studies disagree, quantified by I². High heterogeneity means the pooled estimate may be meaningless, and the reason for the variation is often more interesting than the average.**
> **PUBLICATION BIAS — positive studies are more likely to be published, so a review of published literature over-estimates effect. Assessed with a FUNNEL PLOT, where asymmetry suggests missing negative studies.**
> **READING A FOREST PLOT: each horizontal line is one study's confidence interval, the box size reflects its weight, the vertical line is the line of no effect (1 for ratios, 0 for differences), and the DIAMOND at the bottom is the pooled estimate. If the diamond crosses the line, the pooled result is not statistically significant.**

> [!danger] The ecological fallacy
> **ECOLOGICAL STUDIES compare populations rather than individuals — for example, correlating national fat consumption with national heart disease rates.**
> **THE ECOLOGICAL FALLACY is inferring something about INDIVIDUALS from GROUP-level data.** A country with high average fat intake and high heart disease does not tell you that the individuals eating the fat are the ones having the heart attacks.
> **Ecological studies are useful for generating hypotheses and for evaluating population-level interventions, and they are not evidence about individual risk.**

---

## 0.2 Bias, Confounding and Validity

> [!danger] Bias is systematic error — and a bigger sample does not fix it
> **RANDOM ERROR (chance) — reduced by increasing the sample size. It affects PRECISION.**
> **BIAS (systematic error) — NOT reduced by increasing the sample size. It affects VALIDITY.**
> **A large biased study is a precisely wrong answer.** This distinction is the single most useful thing in critical appraisal.

> [!warning] Selection bias — how people got into the study
> **· SAMPLING and NON-RESPONSE bias — those who participate differ from those who do not.**
> **· VOLUNTEER (healthy volunteer) bias.**
> **· LOSS TO FOLLOW-UP (attrition) bias — and it matters most when the reason for dropping out is related to the outcome.**
> **· THE HEALTHY WORKER EFFECT — employed populations are healthier than the general population, so occupational cohorts under-estimate the harm of exposures.**
> **· BERKSON BIAS — using hospital controls in a case-control study, where the controls are hospitalised for reasons that may themselves relate to the exposure.**
> **· NEYMAN (prevalence-incidence) BIAS — studying prevalent rather than incident cases misses those who died quickly or recovered quickly, so the survivors are unrepresentative.**

> [!warning] Information bias — how the data were collected
> **· RECALL BIAS — people with a disease remember and report exposures differently from those without.** **The classic weakness of case-control studies**, and particularly severe for exposures with a perceived causal link (mothers of children with a congenital anomaly recall pregnancy exposures far more thoroughly).
> **· OBSERVER and INTERVIEWER bias — mitigated by blinding.**
> **· MISCLASSIFICATION — and the direction matters:**
> **NON-DIFFERENTIAL misclassification (errors equally distributed between groups) BIASES TOWARD THE NULL — it dilutes a real effect.**
> **DIFFERENTIAL misclassification (errors distributed unevenly) can bias in EITHER direction and is far more dangerous.**
> **This is why "the measurement was crude, so the true effect is probably larger" is a legitimate argument for non-differential error — and why it is not legitimate when the error is differential.**
> **· THE HAWTHORNE EFFECT — people change behaviour because they are being observed.**
> **· IMMORTAL TIME BIAS — a period during which the outcome cannot occur is misallocated to the treated group, making the treatment look protective. A recurring problem in observational studies of medications.**
> **· LEAD TIME and LENGTH TIME bias — see 0.5, where they matter most.**

> [!danger] Confounding — the definition has three parts, and all three are required
> **A confounder is a variable that:**
> **1. IS ASSOCIATED WITH THE EXPOSURE, and**
> **2. IS INDEPENDENTLY ASSOCIATED WITH THE OUTCOME, and**
> **3. IS NOT ON THE CAUSAL PATHWAY between them.**
> **The third clause is the one that gets forgotten.** **A variable that MEDIATES the effect is not a confounder, and adjusting for it wrongly removes the very effect you are measuring.**
> **The classic example: coffee drinking appears associated with lung cancer — because coffee drinkers smoke more. Smoking is associated with coffee, independently causes lung cancer, and is not on the causal pathway from coffee to cancer.**
> **CONTROLLING FOR CONFOUNDING:**
> **· AT DESIGN: RANDOMISATION (the only method covering unknown confounders) · RESTRICTION · MATCHING.**
> **· AT ANALYSIS: STRATIFICATION · MULTIVARIABLE REGRESSION · propensity scoring.**
> **RESIDUAL CONFOUNDING always remains in observational studies, because measurement of confounders is imperfect and unknown confounders cannot be adjusted for.** **This is why an observational association is not causation, however large.**

> [!tip] Effect modification is not confounding
> **EFFECT MODIFICATION (interaction) means the effect of the exposure GENUINELY DIFFERS between subgroups** — for example, a drug that works in men and not in women.
> **A confounder is a NUISANCE to be adjusted away. An effect modifier is a FINDING to be reported.**
> **Adjusting away an effect modifier destroys real information.** **The correct response is to report the effect SEPARATELY in each stratum.**

> [!warning] Causation — and the one criterion that is essential
> **The Bradford Hill considerations: STRENGTH of association · CONSISTENCY across studies and populations · SPECIFICITY · TEMPORALITY · BIOLOGICAL GRADIENT (dose-response) · PLAUSIBILITY · COHERENCE with existing knowledge · EXPERIMENTAL evidence · and ANALOGY.**
> **THEY ARE CONSIDERATIONS, NOT A CHECKLIST — and only TEMPORALITY IS ABSOLUTELY REQUIRED. The cause must precede the effect.**
> **Also consider REVERSE CAUSALITY** — the outcome caused the exposure. Early disease reduces physical activity, making inactivity look like a cause of the disease.
> **INTERNAL VALIDITY — is the result true for the people in the study? EXTERNAL VALIDITY (generalisability) — does it apply to your patient?** **A trial can have perfect internal validity and be irrelevant to the 85-year-old in front of you.**

---

## 0.3 Diagnostic Test Statistics

> [!tip] Draw the 2×2 table every single time
> |  | **Disease PRESENT** | **Disease ABSENT** |
> |---|---|---|
> | **Test POSITIVE** | **True positive (TP)** | **False positive (FP)** |
> | **Test NEGATIVE** | **False negative (FN)** | **True negative (TN)** |
> **SENSITIVITY = TP / (TP + FN)** — of those WITH the disease, the proportion the test identifies. **Read ACROSS the disease-present column.**
> **SPECIFICITY = TN / (TN + FP)** — of those WITHOUT the disease, the proportion correctly excluded.
> **POSITIVE PREDICTIVE VALUE = TP / (TP + FP)** — of those who test positive, the proportion who have the disease. **Read ACROSS the test-positive row.**
> **NEGATIVE PREDICTIVE VALUE = TN / (TN + FN)**.
> **The columns give you sensitivity and specificity. The rows give you the predictive values.** Getting this the wrong way round is the commonest error, and drawing the table prevents it.

> [!danger] SnNout and SpPin
> **· A HIGHLY SENSITIVE TEST, WHEN NEGATIVE, RULES THE DISEASE OUT. — "SnNout"**
> Because a sensitive test has few false negatives, so a negative result is trustworthy.
> **· A HIGHLY SPECIFIC TEST, WHEN POSITIVE, RULES THE DISEASE IN. — "SpPin"**
> Because a specific test has few false positives, so a positive result is trustworthy.
> **This is why SCREENING tests are chosen for SENSITIVITY (you must not miss cases) and CONFIRMATORY tests for SPECIFICITY (you must not wrongly label people).**

> [!danger] Sensitivity and specificity do not change with prevalence — predictive values do
> **SENSITIVITY AND SPECIFICITY ARE PROPERTIES OF THE TEST.** They are stable across populations (with some caveats about spectrum effects).
> **PREDICTIVE VALUES DEPEND ENTIRELY ON PREVALENCE — that is, on the pre-test probability.**
> **THE CONSEQUENCE, WHICH IS THE MOST IMPORTANT IDEA IN DIAGNOSTIC TESTING:**
> **IN A LOW-PREVALENCE POPULATION, EVEN AN EXCELLENT TEST HAS A POOR POSITIVE PREDICTIVE VALUE — MOST POSITIVES ARE FALSE POSITIVES.**
> **Work it through: a test with 99% sensitivity and 99% specificity, applied to a population where the disease prevalence is 1 in 10,000. Of 10,000 people tested, roughly 1 true case tests positive, and about 100 healthy people also test positive. The PPV is about 1%.** **Ninety-nine out of a hundred positives are wrong, with a test that is 99% accurate on both axes.**
> **This is the mathematical basis of: why screening asymptomatic populations generates false positives · why testing without a clinical indication is harmful · and why "the test was positive" means very different things in different patients.**
> **It also explains why a test performs worse in general practice than in the hospital where it was validated.**

> [!tip] Likelihood ratios — prevalence-independent, and usable at the bedside
> **LR+ = sensitivity / (1 − specificity)** — how much a positive result increases the odds of disease.
> **LR− = (1 − sensitivity) / specificity** — how much a negative result decreases them.
> **They are independent of prevalence, and they combine with the pre-test probability (using a Fagan nomogram or odds arithmetic) to give a post-test probability.**
> **Rough interpretation: LR+ above 10 or LR− below 0.1 produce large, often conclusive changes in probability. Values near 1 change almost nothing** — which is a useful way of identifying tests not worth doing.
> **ROC CURVE — plots sensitivity against (1 − specificity) across all possible cut-offs. The AREA UNDER THE CURVE summarises overall discrimination: 0.5 is no better than chance, 1.0 is perfect.**
> **MOVING A CUT-OFF TRADES SENSITIVITY AGAINST SPECIFICITY — you cannot increase both.** Where you set it depends on the relative cost of a missed case versus a false alarm.

> [!info] Prevalence and incidence
> **PREVALENCE — the proportion of a population WITH the disease at a point in time (existing cases). Useful for planning services.**
> **INCIDENCE — the rate of NEW cases over a period. Useful for studying causation.**
> **PREVALENCE ≈ INCIDENCE × DURATION.**
> **The consequence that catches people out: a treatment that prolongs life without curing INCREASES prevalence while incidence is unchanged.** **Rising prevalence can mean better survival rather than more disease.**

---

## 0.4 Measures of Effect

> [!info] The measures, and where each comes from
> **· RELATIVE RISK (risk ratio) = risk in exposed / risk in unexposed.** From cohort studies and RCTs.
> **· ODDS RATIO = odds in exposed / odds in unexposed.** From case-control studies (where risk cannot be calculated), and from logistic regression. **It APPROXIMATES the relative risk when the outcome is RARE, and OVER-ESTIMATES it when the outcome is common** — which is why odds ratios for common outcomes are frequently misreported as if they were risk ratios.
> **· HAZARD RATIO — from survival (time-to-event) analysis, describing the instantaneous relative rate over time.**
> **· ABSOLUTE RISK REDUCTION (ARR) = risk in control group − risk in treated group.**
> **· RELATIVE RISK REDUCTION (RRR) = ARR / risk in control group.**
> **· NUMBER NEEDED TO TREAT (NNT) = 1 / ARR** — **always rounded UP.** How many patients must be treated for one to benefit.
> **· NUMBER NEEDED TO HARM (NNH) = 1 / absolute risk increase.**

> [!danger] Relative measures exaggerate; absolute measures inform
> **This is the single most important statistical literacy point in clinical practice.**
> **WORKED EXAMPLE: a drug reduces the risk of an event from 2% to 1%.**
> **· RELATIVE RISK REDUCTION = 50%. "Halves your risk!"**
> **· ABSOLUTE RISK REDUCTION = 1%.**
> **· NNT = 100. One hundred people take the drug for one to benefit; ninety-nine take it for nothing.**
> **All three describe the same result. The first is what appears in the press release, the abstract and the pharmaceutical representative's slide. The third is what the patient needs to decide.**
> **Relative measures are also identical whether the baseline risk is 2% or 0.02% — which is why they conceal how much a treatment actually matters to an individual.**
> **ALWAYS ASK FOR THE ABSOLUTE NUMBERS, and communicate them to patients in natural frequencies ("about 1 in 100 people like you will avoid a heart attack") rather than percentages, which are poorly understood by patients and by clinicians.**

> [!warning] Confidence intervals and p values — what they actually mean
> **A 95% CONFIDENCE INTERVAL is the range within which the true value plausibly lies.**
> **· FOR A RATIO (RR, OR, HR): if the interval CROSSES 1, the result is not statistically significant.**
> **· FOR A DIFFERENCE (ARR, mean difference): if it CROSSES 0, the result is not statistically significant.**
> **· THE WIDTH indicates PRECISION — a wide interval means an imprecise estimate, usually from a small study. A statistically significant result with an interval from 1.01 to 8.9 is compatible with almost no effect and with an enormous one.**
> **THE P VALUE is the probability of obtaining a result AT LEAST AS EXTREME as the one observed, IF THE NULL HYPOTHESIS WERE TRUE.**
> **WHAT IT IS NOT:**
> **· It is NOT the probability that the null hypothesis is true.**
> **· It is NOT the probability that the result occurred by chance.**
> **· It is NOT a measure of effect size — a tiny, clinically irrelevant difference will be highly significant in a large enough study.**
> **· p = 0.049 and p = 0.051 are not meaningfully different, despite the conventional threshold.**
> **CONFIDENCE INTERVALS ARE MORE INFORMATIVE THAN P VALUES, because they convey both significance and magnitude.**

> [!danger] Statistical significance is not clinical significance
> **A large trial can demonstrate a statistically significant reduction in blood pressure of 1 mmHg, or a significant improvement on a symptom scale that no patient would notice.**
> **Always ask: is the effect BIG ENOUGH TO MATTER to a patient? Is it larger than the minimum clinically important difference?**
> **And the reverse: a non-significant result in an underpowered study is NOT evidence of no effect. "Absence of evidence is not evidence of absence" — look at the confidence interval, which will usually be wide enough to include a clinically important benefit.**
> **TYPE I ERROR (alpha) — concluding there is an effect when there is not. Conventionally set at 0.05.**
> **TYPE II ERROR (beta) — missing a real effect. POWER = 1 − beta, conventionally 80% or 90%.**
> **MULTIPLE COMPARISONS — testing twenty outcomes at p < 0.05 produces roughly one false positive by chance. This is why pre-specified primary outcomes matter and why subgroup analyses are hypothesis-generating rather than conclusive.**

> [!warning] Three things to be suspicious of when reading a trial
> **1. INTENTION-TO-TREAT versus PER-PROTOCOL analysis.**
> **ITT analyses participants in the group they were RANDOMISED to, regardless of what they actually received. It PRESERVES RANDOMISATION and reflects real-world effectiveness, and it is CONSERVATIVE for superiority trials.**
> **PER-PROTOCOL analyses only those who completed the protocol — which breaks randomisation and can exaggerate benefit.**
> **THE EXCEPTION WORTH KNOWING: in NON-INFERIORITY trials, ITT is ANTI-CONSERVATIVE — because dropout and non-adherence blur the difference between groups and make treatments look more similar, i.e. more "non-inferior".** **Non-inferiority trials should report both.**
> **2. COMPOSITE ENDPOINTS — combining outcomes of very different importance ("death, myocardial infarction, or hospitalisation for angina").** **The effect is frequently driven entirely by the least important component. Look at the individual components.**
> **3. SURROGATE ENDPOINTS — a laboratory or imaging measure standing in for a clinical outcome (HbA1c for diabetic complications, bone density for fracture, tumour response for survival).** **Surrogates have repeatedly failed to predict clinical benefit, and drugs improving a surrogate have been shown to increase mortality.** **Ask whether the outcome is one a patient would care about.**

---

## 0.5 Screening

> [!info] The Wilson and Jungner criteria — grouped by what they concern
> **THE CONDITION: an important health problem · a recognisable LATENT or early symptomatic stage · a natural history that is adequately understood.**
> **THE TEST: suitable, ACCEPTABLE to the population, sufficiently sensitive and specific, safe.**
> **THE TREATMENT: an ACCEPTED and EFFECTIVE treatment must exist, and treating early must produce BETTER OUTCOMES than treating at the usual time of presentation.**
> **THE PROGRAMME: facilities for diagnosis and treatment available · an agreed policy on whom to treat · cost balanced against benefit · and case-finding must be a CONTINUING process, not a one-off project.**
> **The criterion most often failed in practice is the third group: EARLY TREATMENT MUST IMPROVE OUTCOMES.** Detecting something early is worthless if treating it early does not help.

> [!danger] Lead time, length time, and overdiagnosis — the three reasons screening looks better than it is
> **1. LEAD TIME BIAS.** **Screening moves the DATE OF DIAGNOSIS earlier without changing the DATE OF DEATH — so measured "survival from diagnosis" lengthens while the person dies at exactly the same moment.**
> **A patient diagnosed at 60 and dying at 65 has "5-year survival". Screen them at 55 and they have "10-year survival" and die on the same day.**
> **2. LENGTH TIME BIAS.** **Screening at intervals preferentially detects SLOW-GROWING disease, because fast-growing disease appears and becomes symptomatic between screening rounds.**
> **So the screen-detected cases are systematically the ones with a better prognosis — making the screened group look better regardless of any treatment effect.**
> **3. OVERDIAGNOSIS — the most important and least understood harm.**
> **Detection of disease that meets the pathological definition but WOULD NEVER HAVE CAUSED SYMPTOMS OR DEATH IN THAT PERSON'S LIFETIME.**
> **The overdiagnosed patient CANNOT BENEFIT, because there was nothing to prevent — but they receive all the harms: the diagnosis, the anxiety, the label, the surgery, the radiotherapy, the complications, and the insurance and employment consequences.**
> **Overdiagnosis also makes screening look effective, because each overdiagnosed "case" is counted as a survivor.**
> **Demonstrated examples include neuroblastoma screening in infants, thyroid cancer screening, and — to a contested degree — prostate and some breast cancer screening.**
> **THE CONSEQUENCE FOR APPRAISAL: A SCREENING PROGRAMME MUST BE JUDGED ON DISEASE-SPECIFIC AND IDEALLY ALL-CAUSE MORTALITY IN RANDOMISED TRIALS — NOT on survival from diagnosis, not on stage shift, and not on the number of cancers detected.** **All three of those improve with a useless screening test.**

> [!warning] The Australian programmes
> **· BreastScreen Australia — mammography for asymptomatic women in a defined age range.** **REMEMBER: SCREENING IS FOR ASYMPTOMATIC PEOPLE. A symptomatic woman needs diagnostic assessment.** Cross-refer [[O7]] 0.5.
> **· National Cervical Screening Program — now HPV-BASED rather than cytology-based, at longer intervals, with SELF-COLLECTION available**, which has substantially improved participation among under-screened groups. Cross-refer [[O6]] 0.2.
> **· National Bowel Cancer Screening Program — immunochemical faecal occult blood testing mailed to eligible ages.** **Participation is the main limitation, and a GP endorsement measurably improves it.** **A POSITIVE iFOBT REQUIRES COLONOSCOPY, and delays in that pathway are a recognised problem.** Cross-refer [[C5]] 0.5.
> **· Newborn bloodspot screening, newborn hearing screening, and pulse oximetry screening.** Cross-refer [[M3]] 0.6.
> **· A national LUNG CANCER SCREENING programme for high-risk smokers has been introduced.**
> **· PSA testing for prostate cancer is NOT a national screening programme — it remains a shared decision-making conversation because of the overdiagnosis and overtreatment problem.** Cross-refer [[GER3]] and [[H2]] 0.2.
> `UNVERIFIED — all ages, intervals, tests and eligibility. These change and must be checked.`
> **INFORMED CHOICE, NOT COERCION: people have a right to decline screening, and the conversation should present benefits AND harms — including false positives, overdiagnosis and the consequences of further investigation — in absolute numbers.**

---

## 0.6 Public Health Practice

> [!danger] Notify on suspicion — do not wait for confirmation
> **Notification of specified diseases is a LEGAL OBLIGATION on medical practitioners and laboratories, discharged to the state health department (in South Australia, through SA Health's communicable disease control).**
> **FOR SOME CONDITIONS, NOTIFICATION IS REQUIRED IMMEDIATELY AND ON CLINICAL SUSPICION — before laboratory confirmation.** **MEASLES and MENINGOCOCCAL DISEASE are the paradigm examples**, because contact tracing and prophylaxis are time-critical and waiting for confirmation wastes the window.
> **Notification enables: contact tracing and post-exposure prophylaxis · outbreak detection · source identification · and surveillance.**
> **It is not optional, it is not a breach of confidentiality, and it is not somebody else's job.**
> `UNVERIFIED — the SA notifiable disease list, the urgency categories, and the notification mechanism. Know where to find it before you need it.`

> [!tip] Outbreak investigation — the ordered steps
> **1. CONFIRM THE OUTBREAK (is this more than expected?) and CONFIRM THE DIAGNOSIS.**
> **2. DEFINE A CASE — an explicit case definition by person, place and time, usually with confirmed, probable and possible categories.**
> **3. FIND CASES — active case finding.**
> **4. DESCRIPTIVE EPIDEMIOLOGY — describe by TIME (the epidemic curve), PLACE (mapping) and PERSON (who is affected).**
> **5. GENERATE HYPOTHESES about source and transmission.**
> **6. TEST THE HYPOTHESES with an analytical study — usually a RETROSPECTIVE COHORT (if the exposed population is defined, e.g. a wedding) or a CASE-CONTROL study (if it is not).**
> **7. IMPLEMENT CONTROL MEASURES.**
> **8. COMMUNICATE — to clinicians, the public and stakeholders.**
> **9. EVALUATE and report.**
> **THE CRITICAL PRACTICAL POINT: CONTROL MEASURES DO NOT WAIT FOR STEP 7.** **Implement what you can as soon as you have a plausible hypothesis — steps run in parallel, and an outbreak investigation that withholds action pending analysis costs cases.**

> [!info] Epidemic curves and the numbers that matter
> **THE SHAPE OF THE EPIDEMIC CURVE SUGGESTS THE TRANSMISSION MODE:**
> **· POINT SOURCE — a single sharp peak, with all cases occurring within one incubation period. Everyone exposed at one time (a contaminated meal).**
> **· CONTINUOUS COMMON SOURCE — a plateau, as exposure continues over time (a contaminated water supply).**
> **· PROPAGATED (person-to-person) — successive peaks separated by roughly one incubation period, each larger than the last.**
> **The time from exposure to the peak approximates the median INCUBATION PERIOD, which helps identify the pathogen.**
> **ATTACK RATE = number of cases / number of people at risk — calculated for each exposure to identify the source.**
> **R₀ (basic reproduction number) — the average number of secondary cases from one case in a fully susceptible population.**
> **HERD IMMUNITY THRESHOLD = 1 − 1/R₀.** **So a disease with R₀ of 4 requires 75% immunity to interrupt transmission; measles, with a very high R₀, requires very high coverage — which is why measles is the first disease to return when vaccination rates slip.**

> [!warning] Immunisation, and how to talk about it
> **HERD IMMUNITY protects those who cannot be vaccinated — infants too young, the immunosuppressed, and those in whom vaccines fail.** **This makes vaccination a collective as well as an individual act.**
> **The Australian Immunisation Register records vaccinations across the lifespan, and the National Immunisation Program provides funded vaccines on a schedule.** `UNVERIFIED — the current schedule.`
> **VACCINE HESITANCY — the evidence on communication:**
> **· Most hesitant parents are NOT ideologically opposed; they are anxious and seeking reassurance. Treating them as anti-vaccine is counterproductive.**
> **· BLUNTLY REFUTING MYTHS CAN BACKFIRE — repeating a myth in order to deny it increases its familiarity and, in some studies, its perceived truth.** **Lead with the accurate positive message rather than with the correction.**
> **· A PRESUMPTIVE approach ("today we're doing three vaccinations") produces higher uptake than a participatory one ("what would you like to do about vaccines?"), while still allowing questions.**
> **· The clinician's own clear recommendation is one of the strongest determinants of uptake.**
> **· Address the specific concern, acknowledge it as reasonable to ask about, and do not rush.**

> [!tip] The levels of prevention — including the one nobody knows
> **· PRIMORDIAL — preventing the emergence of risk factors at all (urban design that makes walking normal, tobacco advertising bans).**
> **· PRIMARY — preventing disease in those with risk factors (immunisation, smoking cessation, statins in high-risk patients).**
> **· SECONDARY — detecting disease early to improve outcome (screening).**
> **· TERTIARY — reducing the impact of established disease (rehabilitation, secondary prevention after myocardial infarction).**
> **· QUATERNARY — PROTECTING PATIENTS FROM OVER-MEDICALISATION AND FROM THE HARMS OF UNNECESSARY INTERVENTION.**
> **Quaternary prevention is the least known and arguably the most relevant to daily practice: not ordering the test that will generate an incidentaloma, not prescribing the drug whose NNT is 300, deprescribing, and declining to screen someone who will not benefit.** **"First, do no harm" expressed as a public health concept.** Cross-refer [[GER1]] 0.4 and [[GER3]].
> **And the social determinants of health — the conditions in which people are born, grow, work and age — account for more variation in health outcomes than healthcare does.** Cross-refer [[AU1]] 0.2.

**Ix:** Not applicable — but the analogous discipline is: **before ordering any test, ask what the PRE-TEST PROBABILITY is, and what you will do with a positive and with a negative result** (*why:* a test that will not change management should not be ordered, and in low pre-test probability a positive result is more likely false than true; *what:* a genuinely useful answer). **Before accepting a reported treatment benefit, ask for the ABSOLUTE risk reduction and the NNT** (*why:* relative measures conceal magnitude; *what:* the number that lets a patient decide). **Before accepting a screening claim, ask whether it reduces MORTALITY in randomised trials** (*why:* survival, stage shift and detection rates all improve with a useless test; *what:* mortality benefit or its absence).

---

> [!note] Cross-references
> Preventive health, screening and immunisation in practice → [[GER3]] · Evidence appraisal, guidelines and clinical reasoning → [[EBM1]] · Deprescribing and polypharmacy → [[GER1]] 0.4 · Australian health system, Closing the Gap and social determinants → [[AU1]] · Cervical and breast screening → [[O6]] 0.2 and [[O7]] 0.5 · Bowel cancer screening and iFOBT → [[C5]] 0.5 · PSA and prostate screening → [[H2]] 0.2 · Newborn screening → [[M3]] 0.6 · Notifiable infections and contact tracing → [[F0.3]] 0.9 and [[M2]] 0.6 · Occupational disease notification → [[RESP-X]] 0.2 · Communication of risk and shared decision-making → [[GER5]] · Consent and information disclosure → [[A10]] 0.2
