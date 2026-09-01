---
block: Public Health, Epidemiology & Research Literacy
source: built in chat, model knowledge, NOT source-verified
---

> [!warning] Sourcing — and why this file has fewer flags than the others
> Written from model knowledge, not retrieved from source. **Unlike the clinical files, most of this material is MATHEMATICAL OR DEFINITIONAL rather than guideline-dependent — sensitivity does not change between jurisdictions or get revised by a committee.** **The definitions, formulae and concepts here are reliable.**
> **What DOES require verification is flagged: the Australian screening programmes (ages, intervals and tests change), the notifiable disease list, and the immunisation schedule.** Verify against **SA Health**, the **Australian Immunisation Handbook**, and the relevant national screening programme sites.

---

## 0.1 Study Design

`CF-PAIR` **`Clinical-Process-EBM ## Study Design and Bias` arrived in Part 1 and was NOT merged into this section.**

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

`CF-PAIR` **`Clinical-Process-EBM ## Diagnostic Test Characteristics` arrived in Part 1 and was NOT merged into this section.**

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


> [!info] **CO-LOCATED — a second account of this topic is directly below, intact, nothing reconciled.**
> They were elsewhere in this file. A cross-reference means opening a second place to read.

<!-- ===== SOURCE: Clinical-Process-EBM-Consent-Capacity.md ===== -->
*Co-located here from elsewhere in this file, 2026-09-01. Verbatim.*

## Diagnostic Test Characteristics — Sensitivity, Specificity, PPV and NPV
`CF-PAIR §0.3` **Part 0 §0.3 Diagnostic Test Statistics covers the same ground. Both kept in full, NOT reconciled.**

> [!warning] **Correction to this project's own record.** The workflow's N2 entry instructs a future round to "verify Notifiable Diseases and sensitivity/specificity are genuinely already adequate first, don't rebuild what exists." Notifiable diseases *is* adequate (see [[08_01-03_Infectious_Disease_-_Bacterial_Infections]] Notifiable Diseases (Australia)). **Sensitivity and specificity were not.** The terms appear eight times across the corpus, every one of them an *application* to a specific test — D-dimer's high sensitivity, faecal calprotectin, the Ottawa rules — with the concepts themselves never defined and PPV/NPV never mentioned at all. This is the same failure mode that produced the false "SNAP is covered" claim: **applied in context is not the same as built as a topic.**

> [!note] Gap-filled from CSV ("Sensitivity, specificity, PPV/NPV interpretation," High yield, Public Health/Epidemiology category). Verified against the RACGP practical guide to statistics for general practice and Australian Prescriber's *Evidence, risk and the patient*, Aug 2026.

**The four measures, and the distinction that carries all the clinical weight:**

| | Question it answers | Fixed or variable? |
|---|---|---|
| **Sensitivity** | Of people **with** the disease, what proportion test positive? | A property of the **test** — does not change with population |
| **Specificity** | Of people **without** the disease, what proportion test negative? | A property of the **test** |
| **PPV** | Of people who test **positive**, what proportion actually have the disease? | Depends on **prevalence** — changes with the population |
| **NPV** | Of people who test **negative**, what proportion are genuinely disease-free? | Depends on **prevalence** |

> [!danger] **The single most important consequence, and the reason this belongs in a clinical file rather than a statistics one: PPV falls as prevalence falls, even though the test has not changed.** Order a test in a population where the disease is rare and most of your positives will be false positives — not because the test is bad, but because there were so few true cases available to find. This is the mechanism behind three things already stated elsewhere in this project without their underlying reason:
> - Why **screening programmes are restricted by age and risk band** rather than offered to everyone (see [[19_General_Practice_and_Preventive_Medicine]] Preventive Medicine and Screening in Australian General Practice).
> - Why **general practice investigates differently from an emergency department** — the same symptom carries a far lower pre-test probability there (see [[19_General_Practice_and_Preventive_Medicine]] Continuity of Care, and What Makes General Practice Different).
> - Why **a positive allergy test is sensitisation rather than disease** unless it fits the history (see [[13_04_ENT_-_Nose__Rhinosinusitis__Fractures__CSF_Rhinorrhoea__Epistaxis__Nasal_Cancers_]] Allergic Rhinitis (Hay Fever)).

**The two mnemonics, and what they actually mean:**
- **SnNout** — a highly **Sen**sitive test, when **N**egative, rules **out**. High sensitivity means few false negatives, so a negative result is trustworthy.
- **SpPin** — a highly **Sp**ecific test, when **P**ositive, rules **in**. High specificity means few false positives, so a positive result is trustworthy.

**Worked example already in this project:** **D-dimer** is highly sensitive and poorly specific, which is exactly why it functions as a **rule-out** test in a patient with low pre-test probability of VTE and is useless as a rule-in test — see [[Heme Onc_merged]] Coagulation Screen and D-dimer Interpretation, which states the practical rule; this entry is the reasoning underneath it.

> [!danger] **A test or risk tool validated in one population does not automatically perform the same way in another, and this is a recurring Australian equity problem rather than a theoretical one.** Sensitivity and specificity are properties of a test *in the population it was validated in*; move to a population with different disease prevalence, different age structure, or a different spectrum of disease, and both the predictive values and sometimes the test characteristics themselves shift.
> The worked example is already in this project: **AUSDRISK is not recommended for Aboriginal and Torres Strait Islander people**, because it was derived in a population with a different baseline prevalence and age of onset, and applying it unadjusted under-identifies risk in exactly the group at greatest risk (see [[06_Metabolic_Medicine_and_Endocrinology]]). The same reasoning underlies why **MMSE and MoCA over-diagnose cognitive impairment** where formal schooling, literacy or cultural content differ, and why a separately validated instrument exists (see [[04_Neurology]] Mild Cognitive Impairment (MCI)).
> **The generalisable question to ask of any test or score: who was it validated in, and is my patient like them?** This is the formal version of the recurring Step 10 pattern in this project — a standard tool being inappropriate or under-inclusive for a specific population.

> [!tip] **Pre-test probability is not optional context — it is half the calculation.** A test result does not tell you whether the patient has the disease; it *moves* your estimate from where it already was. This is why clinical decision rules (Wells, Ottawa, Centor) exist: they establish the pre-test probability *before* the test is ordered, so the result can be interpreted rather than merely read. An intern who orders a test without having formed a pre-test probability cannot interpret the answer either way.

---

<!-- ===== SOURCE: PH1_Population_Health_and_Research_Literacy.md ===== -->

## 0.4 Measures of Effect

`CF-PAIR` **`Clinical-Process-EBM ## Interpreting Treatment Effects` arrived in Part 1 and was NOT merged into this section.**

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

> [!note] **Moved to `[[Preventive-Health]]` on 2026-09-01:** `0.5 Screening` — reproduced there verbatim under a `SOURCE:` divider naming this file.

> [!note] **Moved to `[[Preventive-Health]]` on 2026-09-01:** `0.6 Public Health Practice` — reproduced there verbatim under a `SOURCE:` divider naming this file.

---


> [!info] **CO-LOCATED — a second account of this topic is directly below, intact, nothing reconciled.**
> They were elsewhere in this file. A cross-reference means opening a second place to read.

<!-- ===== SOURCE: Clinical-Process-EBM-Consent-Capacity.md ===== -->
*Co-located here from elsewhere in this file, 2026-09-01. Verbatim.*

## Interpreting Treatment Effects — Absolute vs Relative Risk, and NNT
`CF-PAIR §0.4` **Part 0 §0.4 Measures of Effect covers the same ground. Both kept in full.**

> [!note] Gap-filled from CSV ("Absolute vs relative risk reduction, NNT," High yield, Public Health/Epidemiology category). Genuinely absent: corpus-wide search returned **zero hits** for NNT, number needed to treat, absolute risk reduction, or confidence interval — despite the project quoting relative risk figures in several entries (HRT's breast cancer risk, endometrial cancer RR) where the absolute/relative distinction is exactly what a patient will ask about. Verified against Australian Prescriber's *Evidence, risk and the patient* and the NHMRC levels of evidence framework, Aug 2026.

**The three numbers, using one worked example throughout.** Suppose an event occurs in **0.2%** of a control group and **0.1%** of a treated group:

- **Absolute risk reduction (ARR)** = control rate − treated rate = **0.1 percentage points**.
- **Relative risk reduction (RRR)** = ARR ÷ control rate = **50%**.
- **Number needed to treat (NNT)** = 1 ÷ ARR = 1 ÷ 0.001 = **1,000** patients treated to prevent one event.

> [!danger] **Those three numbers describe the same result, and they do not feel the same.** "Halves your risk" and "one in a thousand benefit" are both true here. **Relative figures are larger and more persuasive precisely because they conceal the baseline**, which is why they dominate drug advertising, media reporting and abstracts — and why an intern quoting an RRR to a patient without the ARR is misleading them while saying something technically correct.
>
> The rule that follows: **whenever you are given a relative figure, ask what the baseline risk is.** A 50% reduction in a common event is transformative; the same 50% in a rare one may be worth almost nothing to that individual, while carrying the same side effects and the same cost.

**NNT in practice:**
- **Lower is better.** An NNT of 10 means treating 10 people to prevent one event; an NNT of 1,000 means treating 1,000.
- **NNT is meaningless without its time frame and its outcome.** "NNT 20" is uninterpretable; "NNT 20 over 5 years to prevent one non-fatal MI" can be discussed with a patient. Always ask *over what period* and *to prevent what*.
- **Its counterpart is NNH — number needed to harm.** The decision is the comparison of the two, not the NNT alone: an NNT of 50 against an NNH of 500 is a very different proposition from an NNT of 50 against an NNH of 60.
- **NNT is not transferable between populations** with different baseline risks. The same treatment has a much lower NNT in a high-risk patient, which is the arithmetic behind **absolute cardiovascular risk assessment** — treating on calculated absolute risk rather than on individual risk factors is a way of directing treatment to the people with the lowest NNT (see [[01_Cardiovascular]] 0.40 Dyslipidaemia and [[19_General_Practice_and_Preventive_Medicine]] Preventive Medicine and Screening in Australian General Practice).

> [!info] **Why this matters for the time-to-benefit reasoning already used elsewhere in this project.** The deprescribing entry says a preventive medicine whose benefit accrues over 5–10 years offers little to a patient whose life expectancy is shorter (see [[18_Geriatrics_and_Older_Persons_Health]] Polypharmacy and Deprescribing). NNT is the formal version of that argument: the NNT is quoted *over a period*, and if the patient will not live through that period, the benefit does not accrue while the harms are immediate. The two entries are the same reasoning at different levels of formality.

> [!info] **The equity consequence of NNT depending on baseline risk, which is not obvious and runs opposite to intuition.** Because NNT falls as baseline risk rises, **the same treatment delivers more absolute benefit to a higher-risk patient**. Aboriginal and Torres Strait Islander Australians carry higher baseline risk for several of the conditions this project covers — cardiovascular disease, chronic kidney disease, rheumatic heart disease. It follows arithmetically that **under-treatment in a higher-risk population forgoes *more* absolute benefit than the same under-treatment elsewhere** — the gap in outcomes is widened not only by the difference in baseline risk but by any difference in treatment rates on top of it. The practical reading: a treatment-access gap is not a separate issue from an incidence gap; it compounds it, which is why this project's equity entries repeatedly check for both (see [[19_General_Practice_and_Preventive_Medicine]] Preventive Medicine and Screening in Australian General Practice).

**Confidence intervals, briefly:** a result is reported with a range of values consistent with the data. Two intern-level uses — **a 95% CI for a risk ratio that crosses 1 means no statistically significant difference was demonstrated**, and **a wide CI signals an imprecise estimate**, usually from a small study, even when the point estimate looks impressive.

---

<!-- ===== SOURCE: PH1_Population_Health_and_Research_Literacy.md ===== -->

# 1 Research literacy merged in from `Clinical-Process-EBM` (C5, 2026-09-01)

> [!info] **C5 executed.** The second half of `Clinical-Process-EBM` — everything after the
> consent sections, which went to `[[A10_Ethics__Capacity__Consent_and_Certification]]` under C4.
>
> **`[[EBM1_Evidence_and_Clinical_Process]]` stays separate as the APPLICATION file** — critical
> appraisal in practice, using guidelines, clinical reasoning and diagnostic error, documentation,
> handover, open disclosure. This file is the statistics and study-design half.
>
> **`## Screening` did NOT come here.** It went to `[[Preventive-Health]]` with this file's own
> `§0.5 Screening` and `§0.6 Public Health Practice`, under C7 — screening is a preventive-health
> topic, not a research-literacy one, even though its *biases* are.

<!-- ===== SOURCE: Clinical-Process-EBM-Consent-Capacity.md ===== -->
*Moved here from `Clinical-Process-EBM-Consent-Capacity.md` on 2026-09-01. Verbatim and unrenumbered.*

## Choosing a Medicine — Quality Use of Medicines

> [!note] Gap-filled from CSV ("Key factors to consider when selecting the most appropriate medication," Medium yield). Verified absent with the teach-vs-mention check: the corpus contains **hundreds of specific drug choices** across every disease entry, and **no entry teaching how such a choice is made**. Zero hits for drug selection, rational prescribing or comparable phrasing.
>
> **Placement overrides the queue's allocation** (which said `19_General_Practice_and_Preventive_Medicine`): prescribing is clinical process, not general-practice discipline or preventive care, and this entry is the therapeutic counterpart to Diagnostic Test Characteristics and Interpreting Treatment Effects below — the same file, the same reasoning applied to treatment rather than diagnosis. Verified against Australia's **National Medicines Policy** Quality Use of Medicines objective and the **National Prescribing Competencies Framework**, Aug 2026.

**Quality Use of Medicines (QUM)** is the Australian framework, and its four words are the actual test: medicines should be used **judiciously, appropriately, safely and effectively**.

### The question sequence

Asking these in order prevents most prescribing errors, because each one can stop the process:

1. **Is a medicine needed at all?** Non-drug options first where they exist — and the honest version of this question is whether the *problem* needs treating, not whether a drug exists for it.
2. **What am I trying to achieve, and how will I know?** A prescription without a defined endpoint cannot be reviewed, and becomes permanent by default (see [[18_Geriatrics_and_Older_Persons_Health]] Polypharmacy and Deprescribing, not repeated here).
3. **Which medicine?** — see the factors below.
4. **What dose, route, frequency and duration?** Duration is the one most often left blank.
5. **How will I monitor it, and when will I stop?** **Decide the stopping or review point at the time of starting**, not later.

### Choosing between medicines

**Patient factors:**
- **Age and physiology** — renal and hepatic function, which change dose rather than only drug choice; frailty (see [[18_Geriatrics_and_Older_Persons_Health]] Frailty).
- **Pregnancy and breastfeeding.**
- **Comorbidity and drug–disease interaction** — the drug that suits the condition may be wrong for the patient.
- **Allergies and previous adverse reactions**, distinguishing true allergy from intolerance, because recording an intolerance as an allergy removes a whole class unnecessarily.
- **Current medicines and interactions** — and the cumulative burden, not only pairwise interactions.
- **What the patient can actually manage** — dose frequency, formulation, dexterity, vision, cognition, and whether they can open the packaging.

**Medicine factors:** efficacy for *this* indication, safety and adverse-effect profile, suitability of formulation and frequency, and **cost**.

> [!info] **Cost is a clinical factor, not an administrative one — and the mechanism is worth stating.** A medicine the patient does not fill or takes intermittently because of cost has a real-world efficacy of approximately zero, however good the trial data. So cost affects outcome through adherence, which makes it part of the drug-choice decision rather than something to consider afterwards. Practically: know whether the medicine is **PBS-listed**, whether it requires an **authority**, and what the patient will actually pay.

**Evidence:** what is the **absolute** benefit for a patient like this one, over what period? A drug with an impressive relative risk reduction may offer very little to a low-risk patient (see Interpreting Treatment Effects — Absolute vs Relative Risk, and NNT below, not repeated here).

> [!danger] **Aboriginal and Torres Strait Islander patients — a specific, funded, under-used measure that directly addresses the cost mechanism above.** The **Closing the Gap (CTG) PBS Co-payment Program** reduces or removes the PBS co-payment for eligible Aboriginal and Torres Strait Islander people. Eligibility is broad — **any age, any location, registered with Medicare, self-identifying**, where in the prescriber's opinion the person has or is at risk of chronic disease and would be unlikely to adhere to their regimen without the assistance. Patients who would normally pay the full PBS amount pay the **concessional rate**; concession-card holders pay **nothing**.
> **The actionable point is that registration is the prescriber's job**, done through Health Professional Online Services, and the programme is under-used because clinicians do not think of it. Given that cost drives non-adherence and non-adherence drives the outcome gap, **failing to register an eligible patient is a clinical omission, not a paperwork one.** Verified against the PBS Closing the Gap Co-payment Program factsheet and Services Australia prescriber guidance, Aug 2026.

> [!tip] The single most useful habit: **write the indication and the intended duration or review date on every prescription you start.** It answers questions 2, 4 and 5 at once, and it is what makes the medicine reviewable by the next person rather than something they inherit and dare not stop.

---

## Study Design and Bias — Reading the Evidence Behind a Recommendation
`CF-PAIR §0.1 §0.2` **Part 0 §0.1 Study Design and §0.2 Bias, Confounding and Validity cover the same ground. All kept in full.**

> [!note] Gap-filled from CSV ("Study design types and sources of bias," Public Health/Epidemiology category). Genuinely absent, and confirmed with the teach-vs-mention lens rather than a presence hit: corpus-wide search returned **zero hits** for *case-control*, *cohort study* as a study design, *selection bias*, *recall bias* or *confounding* — the only matches were "cohort" in the sense of a patient group and "confirms" partial-matching *confound*. The file's previous "Evidence-based medicine — a brief note" placeholder explicitly recorded this as an unbuilt topic; this entry replaces it. Verified against the **NHMRC Designation of Levels of Evidence** (the Australian hierarchy in use since 1999, extended in 2009 to cover diagnostic, prognostic, aetiological and screening questions as well as treatment), Aug 2026.

**Why an intern needs this at all.** You will not design a study. You will constantly be handed a claim — by a drug rep, a consultant, a patient with a printout, a guideline — and have to judge how much weight it carries. The whole skill reduces to two questions: **what kind of study is this**, and **what could have produced this result other than the effect being claimed?**

### The designs, ordered by how well they control for the alternatives

| Design | What it does | The alternative explanation it cannot rule out |
|---|---|---|
| **Case report / case series** | Describes one or several patients. | Everything. No comparison group, so there is nothing to attribute the outcome *against*. Generates hypotheses; settles nothing. |
| **Cross-sectional** (a survey/prevalence study) | Measures exposure and outcome **at the same moment**. | **Which came first.** Finding that people with back pain are less active cannot tell you whether inactivity caused the pain or the pain stopped the activity. |
| **Case-control** | Starts with people who **have** the outcome, finds similar people who don't, looks **backwards** at exposure. | **Recall bias** — people with a disease search their memory harder for exposures than healthy controls do. Efficient for rare diseases and long latencies; cannot give you incidence. |
| **Cohort** | Starts with **exposure**, follows people **forwards** to see who develops the outcome. | **Confounding**, and **loss to follow-up** — if the people who drop out differ from those who stay, the remaining group is no longer the group you recruited. |
| **Randomised controlled trial (RCT)** | Allocates the intervention **by chance**. | Less than the above — but see blinding below. Chance allocation is the only method that balances the confounders you *didn't think of*, which is the entire reason it sits at the top. |
| **Systematic review / meta-analysis** | Pools all studies meeting pre-set criteria. | **The quality of what went in.** Pooling biased trials produces a precise, confident, biased answer. |

> [!info] **The NHMRC levels, which is the hierarchy Australian guidelines cite.** **Level I** — systematic review of RCTs · **Level II** — at least one properly designed RCT · **Level III** — comparative studies without randomised allocation (cohort, case-control, interrupted time series with control) · **Level IV** — case series. Guidelines you will actually read (RACGP, eTG, RANZCOG) grade recommendations against this, so "Level III evidence" in a guideline is telling you *the design*, not the strength of the effect.

### The biases, and the mechanism of each

The word *bias* here does not mean prejudice. It means **a systematic error in how the result was produced** — one that does not shrink by studying more people. That distinction is the single most useful thing in this entry: a larger study fixes imprecision, never bias.

- **Selection bias** — the people studied differ systematically from the people the result will be applied to. *Mechanism:* the comparison groups were assembled by something related to the outcome. A trial recruiting only under-65s with no comorbidity tells you little about the 82-year-old in front of you.
- **Confounding** — a third factor causes both the exposure and the outcome, manufacturing an association between them. *Mechanism:* the classic worked example is coffee and lung cancer — coffee drinkers smoked more, and smoking causes both the coffee habit's company and the cancer. Handled by randomisation (prospectively) or by statistical adjustment (retrospectively, and only for confounders you measured).
- **Recall bias** — differential accuracy of memory between groups. *Mechanism:* having the disease changes how hard you search your memory. Specific to retrospective designs.
- **Observer and performance bias** — knowing who got what changes how outcomes are assessed and how patients are treated. *Mechanism:* this is what **blinding** exists to prevent. *Single-blind* = the participant doesn't know; *double-blind* = neither participant nor assessor knows. Blinding matters most for subjective outcomes (pain scores) and least for hard ones (death).
- **Attrition bias** — differential dropout. *Mechanism:* if the people for whom the drug wasn't working left the trial, the survivors flatter the drug. Countered by **intention-to-treat analysis** — analysing every participant in the group they were *allocated* to, regardless of what they actually received. **Per-protocol** analysis (only those who completed as assigned) systematically favours the intervention, so when a paper reports both and they disagree, believe the intention-to-treat one.
- **Publication bias** — positive results get published; negative ones sit in drawers. *Mechanism:* a meta-analysis can therefore be a faithful synthesis of a distorted sample of reality. This is what trial registration exists to counter.

> [!danger] **Association is not causation, and the specific reason matters more than the slogan.** Any observed association has four possible explanations before causation is one of them: **chance**, **bias**, **confounding**, and **reverse causation** (the outcome caused the exposure). Work through those four before concluding anything. It is also the honest answer to the patient who has read that something "causes" something else.

> [!info] **Selection bias with a name and a consequence, already established elsewhere in this project (Step 10).** This is the one place the equity point here is concrete rather than general. **AUSDRISK — the Australian type 2 diabetes risk tool — is not validated for Aboriginal and Torres Strait Islander people**, and a different, earlier screening approach applies (see [[06_Metabolic_Medicine_and_Endocrinology]] and [[19_General_Practice_and_Preventive_Medicine]] Preventive Medicine and Screening in Australian General Practice). The mechanism is exactly the selection bias above: a tool derived in a population that under-represented the group it is later applied to will mis-estimate risk in that group, and the direction of the error is not predictable from first principles. The general lesson an intern can carry: **before applying a risk score or a trial result, ask who was in the derivation population.** Where that answer is "not this patient", the score is a prompt for clinical judgement, not a substitute for it.

> [!tip] **What this looks like at intern level, practically.** You are not appraising papers on the ward. You are being asked, on a round, "why do we do it this way?" — and the useful answer distinguishes *this is Level I evidence* from *this is how the unit has always done it*. The second is not illegitimate, but it should be said out loud as what it is.

---

## Statistical Significance — p-values and Confidence Intervals

> [!note] Gap-filled from CSV ("Interpretation of p-values," Public Health/Epidemiology category). Genuinely absent — corpus-wide search returned **zero hits** for *p-value*, *p value* or *statistical significance*; the only related content was the two-line "confidence intervals, briefly" note in the entry above, which stated the two intern-level uses of a CI without defining what either a CI or a p-value actually is. Verified against **Australian Prescriber**'s statistics-for-clinicians material and the NHMRC evidence framework, Aug 2026.

**What a p-value actually is.** It is the probability of seeing a difference **at least as large as the one observed, if there were truly no difference** between the groups. Nothing more. The conventional threshold of **p < 0.05** is a social convention, not a law of nature — it means "this result would arise by chance less than 1 time in 20 if the treatment did nothing."

> [!danger] **The three misreadings, each of which will be said out loud on a ward round.**
> - **"p = 0.04 means there is a 96% chance the treatment works."** No. The p-value assumes there is no effect and asks how surprising the data are under that assumption. It is not the probability that the hypothesis is true.
> - **"p = 0.06 means the treatment doesn't work."** No. It means the study did not demonstrate an effect at the conventional threshold — which is also what you would see with a real effect and too few patients. **Absence of evidence is not evidence of absence.**
> - **"p < 0.001 means the treatment works really well."** No. p measures how *confident* you can be that a difference exists, not **how big it is**. A trivial difference becomes highly significant in a large enough study. The clinically relevant question is the effect size — which is the ARR/NNT reasoning in the entry above.

**Why the confidence interval is the more useful number.** A 95% CI gives the range of effect sizes compatible with the data, so it answers "is it big enough to matter?" and "was it demonstrated?" at once:
- **A CI for a ratio (risk ratio, odds ratio, hazard ratio) that crosses 1** — or **a CI for a difference that crosses 0** — means no statistically significant effect was demonstrated. The two null values differ because a ratio of 1 and a difference of 0 both mean "no effect"; using the wrong one is a common slip.
- **The width tells you the precision.** RR 0.60 (95% CI 0.58–0.62) and RR 0.60 (95% CI 0.20–1.80) have the identical point estimate; the first is an answer and the second is barely more than a guess.
- **Read the whole interval clinically, not just whether it crosses the null.** If the entire interval lies within a range you would consider trivial, the result is significant *and* unimportant. If a wide interval includes both trivial and major benefit, the honest conclusion is that the size of the effect is still unknown.

> [!info] **Multiple testing, because it explains a specific pattern you will see in papers.** Test twenty outcomes at p < 0.05 and one will come up "significant" by chance alone. *Mechanism:* the 1-in-20 threshold applies to each test independently. This is why a **pre-specified primary outcome** carries so much more weight than a subgroup finding announced after the fact, and why a trial that missed its primary outcome but reports an impressive secondary one deserves scepticism rather than enthusiasm.

**Cross-reference:** the effect-size half of this — absolute vs relative risk, NNT — is the entry immediately above; a p-value tells you whether a difference was demonstrated, and the ARR/NNT tell you whether it is worth anything to the patient. Neither is interpretable without the other.

---

> [!note] **C5 / C7 executed 2026-09-01. This file kept its identity and gained the research-literacy half of `Clinical-Process-EBM`.**
> `§0.5 Screening` and `§0.6 Public Health Practice` **left** for `[[Preventive-Health]]` — screening
> is a preventive-health topic even though its biases are a research-literacy one, and both halves are
> now adjacent there. **15 wikilinks point at this file**, all still resolving.
