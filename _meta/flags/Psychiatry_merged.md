# Psychiatry_merged.md — grouping and misplacement flags

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


Status: **ANALYSED. GROUPINGS PRODUCED. Only the A1 structural move has been executed.**
Sources: **23** · lines **3,036** · sections **175** · numbering drift: **none**.
Zero inbound: `NEW_Psychiatry`.

## A1 EXECUTED — `N1`–`N8` arrived here from `Neuro_merged.md`

Commit `f5e49c9`. Eight whole sources, 1,624 lines, inserted before the
`NEW_Drugs_17_Psychotropic` divider. Verified: block sha256 `b395c26c7c69a568` identical
before and after; Neuro 5,867 → 4,243; this file 1,405 → 3,029 (then 3,036 with A3 flags);
all eight `SOURCE: N#_` dividers present in order here, **zero remaining in Neuro**;
duplicate-header counts unchanged against `git show HEAD:`.

**The pairing that made the folder error visible, now resolved:**

| Corpus A source | L | Corpus B partner, **now in this file** | L |
|---|---|---|---|
| `14_01 Mood Disorders` | 3 | `N4_Mood_Disorders` | 1767 |
| `14_02 Anxiety and Related Disorders` | 172 | `N5_Anxiety__OCD_and_Trauma` | 2009 |
| `14_03 Psychotic Disorders and Antipsychotics` | 290 | `N3_Psychosis_and_Antipsychotics` | 1546 |
| `14_04 Personality Disorders` + `14_05c Unexplained Symptoms` | 443, 692 | `N6_Functional__Dissociative__Personality` | 2199 |
| `14_05a Eating Disorders` | 604 | `N8_Eating_Disorders` | 2559 |
| `14_05b Insomnia` | 673 | `N7_Sleep_Disorders` | 2375 |
| `14_06b Mental Health Act and Sectioning` | 842 | `N1_Mental_State_Examination_and_Risk` | 1121 |
| `14a-1 Substance Misuse` + `14a-2 Overdose` | 931, 1074 | `N2_Acute_Behavioural_Disturbance…` | 1362 |

**Pointer retarget — measured, and it contradicts the premise of the instruction.** 209
`[[N1]]`–`[[N8]]` references exist in the vault. **None broke.** Wikilinks in this corpus name
the **source** file, which A1 did not rename, so no retarget was required or performed. What
changed is reachability, not resolution: **45 references flipped intra-file → cross-file**
(9 `[[N#]]` left behind in Neuro, 36 `[[D#]]` carried into Psychiatry). `dangling` still 1 (the
deliberate `[[B2]] 0.5`), `misaimed` 0, drift map unchanged. **Locator notes were added at
both ends instead of a retarget** — that is the correct repair for a reachability change.

## PROPOSED MOVES
| ID | Section | L | → | Why |
|---|---|---|---|---|
| Y-1 | `14a-2 Overdose and Poisoning Management` — `§0.1 by agent` · `§0.2 Digoxin` · `§0.3 Salicylate` · `§0.4 TCA` | **1079–1120** | **Emergency** | `Emergency A5 §0.1 The Poisoned Patient`, `§0.2 TCA Overdose`, `F0-1 §0.1`–`§0.8`, `NEW_Drugs_04 Antidotes and Antivenoms`. **Salicylate also duplicates `Endocrine F0-2 §0.8`.** 1 inbound (Examination) |
| Y-2 | `## 0.5 Postpartum (Puerperal) Psychosis` | **362** | **OBGYN** | ⚠️ **the other half of OBGYN B-10** (`## Puerperal psychosis`, OBGYN 1481) and `O3 §0.6 Perinatal Mental Health`. **Three homes** |
| Y-3 | `## Perinatal depression` | 158 | **flag — with Y-2** | same cluster |
| Y-4 | `## Guardianship — a related but distinct framework` | **900** | **`A10_Ethics__Capacity__Consent_and_Certification`** | guardianship is a capacity framework, not a psychiatric disorder |
| Y-5 | `14_06b Mental Health Act and Sectioning` (9 sections: involuntary treatment, CTOs, ITOs, SACAT, interstate transfer, safeguards, police, voluntary inpatients) | **855–904** | **flag — `A10` or keep** | **SA-specific mental health law.** Its Corpus B partner `N1 §0.5 Mental Health Legislation in South Australia` **carries a `> [!danger] Verify everything in this section` warning.** Keep the warning with whichever copy survives |
| Y-6 | `14_07 Attention Deficit Hyperactivity Disorder` | **908–930** | **decide with Paediatrics** | **5 inbound, Paediatrics ×3.** `Pediatrics M7 §0.6 ADHD` (4086) is the partner; `NEW_Drugs_17 §0.5` is the drug half |
| Y-7 | `## Gambling disorder (gambling-related harms)` | **1045** | **arguable — GP / PH1** | a behavioural-addiction and public-health topic filed under recreational drug profiles |
| Y-8 | `14_05d Electroconvulsive Therapy` | **738–758** | **flag — procedures** | consent, workup and complications of a procedure. 1 inbound, internal |
| Y-9 | `**Focused Hx:** / **Examination:**` in `NEW_Psychiatry ## Acute Behavioural Disturbance` | **3019–3020** | **History-Taking.md / Examination.md** | L3020 is explicitly about the limits of examining an agitated patient **✅ RESOLVED 2026-09-01 — Option 1: left in place, indexed in `Examination.md` §3 and `History-Taking.md` §2 (`bcf7515`/`fab04f5`)** |

## KEEP + IN-TEXT FLAG
- **Alcohol withdrawal — the split confirmed from this end — and it is five-way, not four.** `## Alcohol use disorder`
  (**934**) carries pointers to `[[03_Gastrointestinal]] Alcohol withdrawal` at **:934 and :938**,
  naming it *"the full AU-verified management (diazepam-based…)"*. The other copies are
  `N2 §0.1` (**now in this file, 1372**), `N2 §0.2` (1411), `NEW_Drugs_17 §0.6` (2926) and
  `04_Neurology ### Alcohol Withdrawal Seizures` (Neuro 804). **That is FIVE, not four** — see G-Y9.
  **GI M-5 (add a pointer from here) is correct and already half-built — the pointers exist; it is
  the content that is elsewhere.**
- `14_06a Drugs Used in Psychiatry` (8 sections, **763–841**) and `NEW_Drugs_17_Psychotropic`
  (24 sections, **2750–2997**) are **two drug references for the same classes in one
  file** — benzodiazepines, lithium, SSRIs, SNRIs, TCAs, MAOIs, Z-drugs all appear in both.
- `## Eponymous syndromes (appendix)` (**278**) is an appendix inside clinical content.

## GROUPINGS — PRODUCED 2026-09-01, after A1 put the file back together

**Superseded the "deferred" note that stood here.** `N1`–`N8` arrived from `Neuro_merged.md`
at commit `f5e49c9`; the file is now **3,036 lines, 23 sources, 116 sections**, and the
groupings below are made against the whole corpus rather than half of it.

**Line numbers are current as of `90dc93f`** (after the A1 move and the A3 flag insertions).
Method per the brief: **first paragraph of each section read, not the heading alone.**

**Grouping is not merging.** Nothing below implies a discard verdict for any section, and
nothing has been moved. Where two sections cover one topic I say what each *uniquely* holds,
because that is the fact a later merge would need and the fact a heading comparison destroys.

### The shape of this file, now that it is whole

Every Corpus A source has exactly one Corpus B partner, and — this is the finding — **the
partners are not duplicates. They are split along a consistent axis:**

> **Corpus A is written as diagnosis-by-diagnosis reference. Corpus B (`N1`–`N8`) is written
> as approach-to-the-presentation.** A covers *what schizophrenia is*; `N3` covers *what to do
> in a first episode*. A lists *the personality disorder clusters*; `N6` covers *borderline
> personality disorder in the general hospital*. A defines *insomnia*; `N7 §0.2` gives *the 3P
> model and names the perpetuating factors as the treatment target*.

Sampled across all eight pairs, **zero are subsets of each other.** That is the same measure
§1.10 records for section-vs-fragment merges (10 sampled, 0 pure subsets), arrived at
independently here. It is the reason none of these groups is a merge recommendation.

---

### G-Y1 · MOOD DISORDERS — **HIGH**

| Source | Sections | L |
|---|---|---|
| `14_01` | `## Depression` · `### Screening` · `### Management` · `### Switching antidepressants` · `### SSRIs` | 6–52 |
| `14_01` | `## Bipolar disorder` · `### Manic episode` · `### Hypomanic episode` · `### Management` | 93–130 |
| `14_01` | `## Cyclothymia` · `## Seasonal affective disorder` · `## Perinatal depression` | 131, 144, 158 |
| `N4` | `§0.1 Depression — Assessment` · `§0.2 Depression — Management` · `§0.4 Bipolar Disorder and Mania` · `§0.6 Special Situations` | 1777, 1822, 1891, 1971 |
| `14_06a` | `§0.2 Lithium` · `§0.3 Mirtazapine` · `§0.4 MAOIs` · `§0.5 SSRIs` · `§0.6 SNRIs` · `§0.7 TCAs` | 779–835 |
| `N4` | `§0.3 Antidepressants` · `§0.5 Mood Stabilisers` | 1854, 1933 |
| `NEW_Drugs_17` | `§0.1 Antidepressants` + `§0.1.1`–`§0.1.5` · `§0.4 Drugs for Bipolar` + `§0.4.1 Lithium` + `§0.4.2 Other Mood Stabilisers` | 2761–2819, 2884–2904 |

**Why same topic:** all describe the unipolar/bipolar spectrum and the drugs used in it.
**What each uniquely holds — the reason this is a grouping and not a fold:**
- `14_01 ### Switching antidepressants` (L35) holds the **discontinuation taper** (4 weeks,
  fluoxetine excepted) — absent from `N4` and from `NEW_Drugs_17`.
- `14_01 ### Management` (L28) carries a **`[!info]` RACGP Red Book verification box** on
  *screening*, which neither B copy has.
- `N4 §0.2` carries the **stepped-care principle that antidepressants are not first-line in
  mild depression** — a management stance, not a fact.
- `N4 §0.6` frames the perinatal period as **treated illness versus untreated illness**, which
  is the decision an intern actually faces and does not appear in `14_01 ## Perinatal
  depression`.
- `14_01 ## Seasonal affective disorder` (L144) carries a **`[!warning]` correction** — the
  entry previously said there was little evidence for light therapy. **That correction is the
  content**, and it exists in one copy only.

> [!warning] **Lithium is in three places and the three are not the same claim.**
> `14_06a §0.2` (L779, mechanism/AE), `N4 §0.5` (L1933, *"narrow therapeutic index, and the
> drugs that cause toxicity"*), `NEW_Drugs_17 §0.4.1` (L2886, *"an anti-suicide effect
> independent of mood stabilisation"*). Three files, three different reasons to read it.
> **Recorded, not consolidated** — same disposition as PERT in GI.

> [!note] **Valproate teratogenicity crosses files.** `NEW_Drugs_17 §0.4.2` (L2897) defers to
> `NEW_Drugs_15_Neurological.md 0.1.1` and then **raises the stakes** — *"this applies with
> even greater force in bipolar disorder, where alternatives exist."* `NEW_Drugs_15` is in
> `Neuro_merged.md`. **This is now a cross-file pointer that was intra-file before A1.**
> It still resolves (wikilinks name source files), but it is one of the 45 references the A1
> report lists as having flipped intra-file → cross-file.

### G-Y2 · SUICIDE, SELF-HARM AND RISK ASSESSMENT — **HIGH**

| Source | Sections | L |
|---|---|---|
| `14_01` | `## Suicide` · `## Self-harm (including non-suicidal self-injury)` | 53, 78 |
| `N1` | `§0.2 Risk Assessment` · `§0.3 Suicide and Self-Harm` | 1159, 1182 |

**Why same topic:** the same clinical assessment from two directions.
**The two B sections carry the two claims that matter most and A does not have either:**
- `N1 §0.2` — *"Risk stratification tools do not predict individual suicide, and must not
  decide who gets care."*
- `N1 §0.3` — *"Asking about suicide does not create the idea."*

`14_01 ## Self-harm` (L78) carries its own `[!note]` recording that **self-harm and suicide
are clinically distinct rather than points on one severity spectrum**, which is the reason
this group has four sections rather than being folded to two.

### G-Y3 · ANXIETY, OCD AND TRAUMA — **HIGH**

| Source | Sections | L |
|---|---|---|
| `14_02` | `## GAD` · `### Management (stepped-care)` · `## Panic disorder` · `## OCD` · `### Management` · `## PTSD` · `### Management` · `## Specific phobia` · `## Acute stress disorder` | 175–277 |
| `N5` | `§0.1 Approach to Anxiety — and the Medical Mimics` · `§0.2 The Anxiety Disorders` · `§0.3 Panic` · `§0.4 OCD and Related` · `§0.5 Trauma and Stressor-Related` · `§0.6 Management` | 2019–2198 |
| `14_06a` | `§0.1 Benzodiazepines` · `§0.8 Z-drugs` | 764, 836 |
| `NEW_Drugs_17` | `§0.3 Drugs for Anxiety and Sleep` + `§0.3.1 Benzodiazepines` + `§0.3.2 Barbiturates` + `§0.3.3 Other` | 2855–2883 |

**Why same topic:** the anxiety spectrum and its pharmacology.
**Uniquely held:**
- `N5 §0.2` gives the **organising principle** — *"what distinguishes them is the FOCUS of the
  fear"* — which turns A's nine parallel entries into one framework.
- `N5 §0.3` separates **the panic attack from panic disorder**; A treats them as one.
- `N5 §0.5` adds **adjustment disorder**, absent from `14_02`.
- `14_02 ### Management` (PTSD, L253) holds the **negative recommendation** — single-session
  debriefing is not recommended — which B does not state.
- `NEW_Drugs_17 §0.3.3` states plainly that **SSRIs/SNRIs and CBT are the actual first-line
  treatments for anxiety, not benzodiazepines**, and adds buspirone and pregabalin.

> [!warning] **`14_06a §0.1 Benzodiazepines` (L764) already carries an A3 flag** reading
> *"two drug references for the same classes in one file"* — written before `N1`–`N8` arrived.
> **It is now three**, counting `NEW_Drugs_17 §0.3.1`. The flag's wording understates the
> count; it does not misstate the finding.

### G-Y4 · PSYCHOSIS AND ANTIPSYCHOTICS — **HIGH**

| Source | Sections | L |
|---|---|---|
| `14_03` | `§0.1 Features that define psychotic disorders` · `§0.2 Schizophrenia` + `§0.2.1`–`§0.2.3` · `§0.3 Schizoaffective` · `§0.4 Psychosis` · `§0.5 Postpartum Psychosis` | 293–379 |
| `14_03` | `§0.6 Antipsychotics` + `§0.6.1`–`§0.6.7` | 380–442 |
| `N3` | `§0.1 The First Episode of Psychosis` · `§0.2 Schizophrenia and Related Disorders` · `§0.3 The Differential Diagnosis of Psychosis` | 1556–1637 |
| `N3` | `§0.4 Antipsychotics` · `§0.5 Antipsychotic Adverse Effects` · `§0.6 Clozapine` · `§0.7 Long-Term Management and Physical Health` | 1638–1766 |
| `NEW_Drugs_17` | `§0.2 Antipsychotics` · `§0.2.1 Clozapine — a separate safety case` | 2820–2854 |

**Why same topic:** one disease group and one drug class.
**Uniquely held:**
- `N3 §0.1` — *"why the negative [symptoms] matter more"*. A lists negative symptoms
  (`§0.2.2`, L328) without ever saying they drive the outcome.
- `N3 §0.5` opens on **acute dystonia — dramatic, frightening, and rapidly reversible**. A's
  `§0.6.3` covers EPSE via the **ADAPT** mnemonic. **Different content under near-identical
  headings** — this is the case the brief's first-paragraph rule exists for.
- `N3 §0.7` — *"if nobody is named, nobody does it"* on physical health monitoring. A's
  `§0.6.6` gives a monitoring **schedule**. Schedule and ownership are different claims.
- **Clozapine three ways:** A `§0.6.5` (L417) leads on **agranulocytosis 1% / neutropaenia 3%**;
  `N3 §0.6` (L1701) leads on **it is used too late**; `NEW_Drugs_17 §0.2.1` (L2843) leads on
  **superiority in treatment resistance and reduced suicidality**. A risk figure, a
  behavioural failure, and an indication. **All three are needed; none is redundant.**

> [!note] **`§0.5 Postpartum Psychosis` (L362) is in this group AND flagged `Y-2` for OBGYN.**
> Both are true: it is a psychotic disorder and it is a puerperal emergency. It has **three
> homes** — here, `OBGYN ## Puerperal psychosis`, and `O3 §0.6 Perinatal Mental Health`.
> The grouping does not resolve the placement question and is not meant to.

### G-Y5 · PERSONALITY DISORDERS — **HIGH**

| Source | Sections | L |
|---|---|---|
| `14_04` | `## Cluster A` + paranoid, schizoid, schizotypal · `## Cluster B` + antisocial, borderline, narcissistic, histrionic · `## Cluster C` + avoidant, dependent, OCPD · `## Management (general)` | 448–603 |
| `N6` | `§0.4 Personality Disorders` · `§0.5 Borderline Personality Disorder in the General Hospital` | 2300, 2318 |

**Why same topic:** the same ten diagnoses plus their management.
**Uniquely held:** `N6 §0.4` gives the **definition of a personality disorder as a class**
(enduring, pervasive, inflexible, deviating from cultural expectation, stable, onset in
adolescence) — **`14_04` has no such section at all**; it opens directly on Cluster A. `N6 §0.5`
is about **the interactions BPD generates in a general ward**, which is an intern-facing topic
`14_04` does not attempt.

### G-Y6 · FUNCTIONAL, SOMATIC AND DISSOCIATIVE DISORDERS — **HIGH**

| Source | Sections | L |
|---|---|---|
| `14_05c` | `## Somatic symptom disorder` · `## Illness anxiety disorder` · `## Conversion disorder (FND)` · `## Dissociative disorders` · `## Factitious disorder` · `## Malingering` | 695–737 |
| `N6` | `§0.1 Functional Neurological Disorder` · `§0.2 Somatic Symptom and Related Disorders` · `§0.3 Dissociation` · `§0.6 Factitious Disorder and Malingering` | 2209, 2253, 2275, 2349 |

**Why same topic:** a one-to-one correspondence, six A sections to four B sections.
**Uniquely held, and clinically weighted:**
- `N6 §0.1` — **FND is a POSITIVE diagnosis made on POSITIVE signs, not a diagnosis of
  exclusion.** `14_05c ## Conversion disorder` (L709) defines it as *"≥1 symptom of altered
  voluntary motor or sensory function"* and stops. **The B section carries the whole
  diagnostic stance.**
- `N6 §0.2` — *"it is about the RESPONSE, not the absence of pathology"*, the modern framing.
  A's `## Somatic symptom disorder` predates it.
- `N6 §0.6` — the distinction from FND is **intentionality**, *"and it must not be applied
  loosely."* A's `## Malingering` (L732) states the definition without the caution.

**This is the pair where the B side carries the most that A lacks.** Noted for weighting if
these ever come up for merge.

### G-Y7 · EATING DISORDERS — **HIGH**

| Source | Sections | L |
|---|---|---|
| `14_05a` | `## Anorexia nervosa` · `## Bulimia nervosa` · `## Binge-eating disorder` | 607, 626, 649 |
| `N8` | `§0.1 Recognising` · `§0.2 Medical Complications and Risk Assessment` · `§0.3 Refeeding Syndrome` · `§0.4 Anorexia — Management` · `§0.5 Bulimia, BED and ARFID` · `§0.6 Treatment Pathways and the Australian Context` | 2571–2747 |

**Why same topic:** the same three diagnoses, plus three sections A has nothing for.
**Uniquely held:** `N8 §0.3 Refeeding Syndrome` — the phosphate/potassium/magnesium mechanism,
**with the trap that serum levels may be normal while the intracellular compartment is drawn
down**. `14_05a` has no refeeding section. `N8 §0.2` — *"bradycardia and hypotension are
markers of severity, not fitness."* `N8 §0.6` — **the Medicare Eating Disorder Plan**, the only
Australian-system content in the group.

> [!note] **`N8` has 17 inbound references and only 2 were from Neuro.** That imbalance is what
> made the A1 folder error visible. All 17 still resolve — they name `N8_Eating_Disorders`,
> the source file, which A1 did not rename.

### G-Y8 · SLEEP — **HIGH**

| Source | Sections | L |
|---|---|---|
| `14_05b` | `## Insomnia` | 676 |
| `N7` | `§0.1 Sleep Assessment` · `§0.2 Insomnia` · `§0.3 Circadian Rhythm Disorders and Shift Work` · `§0.4 Parasomnias` · `§0.5 Excessive Daytime Sleepiness and Narcolepsy` · `§0.6 Sleep in Specific Contexts` | 2385–2558 |
| `14_06a` | `§0.8 Z-drugs` | 836 |
| `NEW_Drugs_17` | `§0.3.3 Other Drugs for Anxiety and Sleep` | 2875 |

**Why same topic:** sleep and its pharmacology.
**The asymmetry is extreme: A has one section, B has six.** `14_05b` is a 17-line source file
holding a definition of insomnia. `N7` adds the assessment framework (*"the framework that
sorts the presentation in one question"*), circadian disorders (*"commonly misread as insomnia
or laziness"*), parasomnias sorted by **timing of the event**, narcolepsy, and — the
intern-facing one — **hospital sleep deprivation contributing to delirium, "and the answer is
not a sedative."**

> [!warning] **Before A1, `N7 §0.6`'s delirium claim and Geriatrics' delirium content were in
> different files, and they still are.** Moving `N7` into Psychiatry did not create that split;
> it is noted here because a reader looking for "delirium" now has to know to look in three
> files. **Recorded, not actioned** — `Delirium` placement is a PART B question.

### G-Y9 · SUBSTANCE USE AND ACUTE BEHAVIOURAL DISTURBANCE — **HIGH**, and the largest group

| Source | Sections | L |
|---|---|---|
| `14a-1` | `## Alcohol use disorder` · `## Cannabis` · `## Cocaine` · `## MDMA` · `## LSD` · `## Nitrous oxide` · `## Opioid misuse` + `### Acute Mx` + `### Long-term Mx` · `## Gambling disorder` | 934–1073 |
| `N2` | `§0.1 Alcohol Withdrawal and Delirium Tremens` · `§0.2 Alcohol Use Disorder` · `§0.3 Stimulants and Methamphetamine` · `§0.4 Other Substances` · `§0.5 Behavioural Disturbance in Special Populations` | 1372–1516 |
| `N1` | `§0.4 Agitation, Aggression and De-escalation` | 1240 |
| `NEW_Psychiatry` | `## Acute Behavioural Disturbance` | 3009 |
| `NEW_Drugs_17` | `§0.6 Drugs for Alcohol Dependence` · `§0.7 Drugs for Nicotine Dependence` · `§0.8 Other Psychotropic Drugs` (opioid dependence) | 2926–2962 |

**Why same topic:** substances, their withdrawal, and the behavioural emergency they produce.
**Uniquely held, and these are the safety claims:**
- `N2 §0.4` — **the withdrawal syndromes that can kill are ALCOHOL and BENZODIAZEPINES, not
  opioids.** Stated nowhere in Corpus A.
- `N2 §0.3` — **benzodiazepines first for stimulant agitation, not antipsychotics.**
- `N2 §0.5` and `NEW_Psychiatry` agree independently that **behavioural disturbance in an older
  person is delirium until proven otherwise**, and that ABD is *"a presentation, not a
  diagnosis."*
- `N1 §0.4` — *"prevention is most of the work"*, the de-escalation content.
- `14a-1 ### Acute management` (L1031) holds the **naloxone escalation ladder** (400mcg → 800mcg
  ×2 at 1-minute intervals → 2mg → 4mg) — the only dosing in the group, and it is in Corpus A.

> [!danger] **Alcohol withdrawal is now in FIVE places, not four.** The existing A3 flag at
> `14a-1 ## Alcohol use disorder` (L934) says *"`M-5` alcohol withdrawal is in four places
> across three files"* — written when `N2` was in `Neuro_merged.md`. The five: `14a-1` (L934),
> `N2 §0.1` (L1372), `N2 §0.2` (L1411), `NEW_Drugs_17 §0.6` (L2926), and **`03_Gastrointestinal
> ## Alcohol withdrawal`** in `GI_merged.md`, which `14a-1` itself points at twice (L934, L938)
> as *"the full AU-verified management (diazepam-based…)"*.
> **The GI copy is the one with the verification.** Any future consolidation has to preserve
> that pointer, not the local text. **Flag wording is understated; the finding stands.**

### G-Y10 · MENTAL STATE EXAMINATION AND THE MEDICAL MIMICS — **HIGH**, and it is cross-cutting

| Source | Sections | L |
|---|---|---|
| `N1` | `§0.1 Psychiatric Assessment and the MSE` | 1133 |
| `N1` | `§0.6 Medical Causes of Psychiatric Presentation` | 1319 |
| `N5` | `§0.1 Approach to Anxiety — and the Medical Mimics` | 2019 |
| `N3` | `§0.3 The Differential Diagnosis of Psychosis` (*"exclude organic causes in every first episode"*) | 1612 |
| `NEW_Psychiatry` | `## Acute Behavioural Disturbance` (*"treating it as a psychiatric problem before excluding a medical one"*) | 3009 |

**Why same topic:** four sections in three sources make the **same** argument — that a
psychiatric presentation is a diagnosis of exclusion at the organic level — each time about a
different presentation. `N1 §0.6` states it as a principle and rejects the phrase *"medical
clearance"* in favour of *"medical ASSESSMENT."*

**This group is listed BECAUSE it is diffuse, not despite it.** It is the one grouping here
that a heading-level pass cannot see at all: four headings, four different topic words, one
claim. **No action proposed** — the claim is correctly repeated, because a reader arriving at
psychosis should not have to have read the anxiety section.

> [!warning] **`N1 §0.1` carries `> [!tip] The MSE is an EXAMINATION, not a history`** — which
> is the standing rule's own boundary, stated by the corpus. Under the standing rule this
> section is a candidate for `Examination.md`. **PART B. Not flagged for move here**, because
> the MSE is also the single most-referenced section in `N1` and moving it is a destination
> decision, not a row decision.

### G-Y11 · ADHD — **MEDIUM** (the drug half is confident; the placement is not)

| Source | Sections | L |
|---|---|---|
| `14_07` | `§0.1 Attention deficit hyperactivity disorder` | 908 |
| `NEW_Drugs_17` | `§0.5 Drugs for ADHD` + `§0.5.1 Psychostimulants` + `§0.5.2 Non-Amphetamine` + `§0.5.3 Other` | 2905–2925 |

**Why same topic:** one condition and its pharmacology. **Confidence MEDIUM only because the
group is incomplete in this file** — `Pediatrics M7 §0.6 ADHD` is the third member and sits in
`Pediatrics_merged.md`. `14_07` has **5 inbound references, 3 of them from Paediatrics.**
See flag `Y-6`; the grouping does not settle it.

### G-Y12 · OVERDOSE AND POISONING — **HIGH as a group, but the group probably does not belong here**

| Source | Sections | L |
|---|---|---|
| `14a-2` | `§0.1 Overdose / poisoning — management by agent` · `§0.2 Digoxin toxicity` · `§0.3 Salicylate toxicity` · `§0.4 TCA toxicity` | 1079–1120 |

Internally coherent — one table plus three worked agents. **Already flagged `Y-1` for Emergency**
(`A5 §0.1 The Poisoned Patient`, `§0.2 TCA Overdose`, `F0-1 §0.1`–`§0.8`, `NEW_Drugs_04
Antidotes`; salicylate also duplicates `Endocrine F0-2 §0.8`). Grouped here for completeness so
that no section in the file is unaccounted for.

---

### NOT CONFIDENTLY GROUPABLE — these stay, and are listed as the brief requires

| Section | L | Why it does not group |
|---|---|---|
| `14_05d ## Electroconvulsive therapy` | 741 | **A singleton.** No Corpus B partner, no drug-file partner, 1 inbound and it is internal. It is a *procedure* — consent, workup, complications — in a file of diagnoses. Flagged `Y-8`; **its group, if it has one, is in the new `Procedures.md`, not in this file.** |
| `14_06b` — 9 sections (involuntary treatment, CTOs, ITOs, SACAT, interstate transfer, safeguards, police, voluntary inpatients, guardianship) | 855–904 | Groups with `N1 §0.5` (L1285) **as a `CF-PAIR`, not as a topic group.** Both are SA mental health law; **both are already marked**, and `N1 §0.5`'s `[!danger] Verify everything in this section` warning was applied to both copies under A5. **A grouping verdict here would look like a merge recommendation and must not.** |
| `14_06b ## Guardianship` | 900 | Flagged `Y-4` for `A10_Ethics__Capacity__Consent_and_Certification`. It is a **capacity** framework, not a mental-health-law one, and the section says so itself. |
| `14_02 ## Eponymous syndromes (appendix)` | 278 | Already carries an A3 flag — *"an appendix inside clinical content."* Contents are eponyms across several topics; **it groups with nothing because it is a container, not a topic.** |
| `N2 §0.6 The System Interface` | 1517 | Police and ambulance interface. Touches `N1 §0.4` (de-escalation), `14_06b ## Police involvement` (L892) and the ED. **Three partial overlaps, no majority** — the same shape as GI's G21 five-way partial overlap, which was ruled *not a fold*. |
| `NEW_Drugs_17 ## Build status` | 2963 | Build metadata. |
| `NEW_Psychiatry # NEW — Psychiatry` · `## Build status of this file` · `## Topics skipped in this category` · `### Near-misses deliberately built-eligible` | 3001, 3038, 3046, 3057 | Build metadata. **`### Near-misses` (L3057) is worth a human read** — it lists topics deliberately kept eligible for a later build, which is a work queue, not content. |
| `14_01 ## Bipolar disorder` (L93) · `14_04 ## Cluster A/B/C` (448, 493, 554) · `NEW_Drugs_17 §0.3`, `§0.4`, `§0.5` (2855, 2884, 2905) | — | **Headings with no body** — pure containers for their subsections. Grouped via their children above; listed here so the section count reconciles. |

---

### COUNT RECONCILIATION — measured, not estimated

```
total sections            175
in at least one group     156
not confidently groupable  19
covered                   175
UNACCOUNTED                 0
phantom (line numbers not matching a real heading)  []
```

| Group | Sections | New at this row |
|---|---:|---:|
| G-Y1 Mood | 33 | 33 |
| G-Y2 Suicide and risk | 4 | 4 |
| G-Y3 Anxiety, OCD, trauma | 21 | 21 |
| G-Y4 Psychosis and antipsychotics | 25 | 25 |
| G-Y5 Personality disorders | 16 | 16 |
| G-Y6 Functional, somatic, dissociative | 10 | 10 |
| G-Y7 Eating disorders | 9 | 9 |
| G-Y8 Sleep | 9 | **7** — `14_06a §0.8 Z-drugs` and `NEW_Drugs_17 §0.3.3` are shared with G-Y3 |
| G-Y9 Substance use and ABD | 20 | 20 |
| G-Y10 MSE and medical mimics | 5 | **2** — `N5 §0.1`, `N3 §0.3` and `NEW_Psychiatry ABD` are shared with G-Y3/G-Y4/G-Y9 |
| G-Y11 ADHD | 5 | 5 |
| G-Y12 Overdose and poisoning | 4 | 4 |

**Three sections belong to two groups each, deliberately** — G-Y8 shares two hypnotic entries
with G-Y3, and G-Y10 shares three medical-mimic sections with G-Y3, G-Y4 and G-Y9. That
overlap is the finding in G-Y10, not an error in it.

> [!warning] **I first wrote "116 sections" here from memory and it was wrong — the file has
> 175.** Corrected by running the count before committing. Recorded because §1.10 lists five
> prior instances of a corpus-wide figure being quoted rather than measured, and rule 11
> requires the check to be run rather than reasoned. The script is
> `scratchpad/recon.py`; the block above is its output verbatim.

## LIMITATIONS

1. **These groupings were produced from first paragraphs, as the brief requires — but a first
   paragraph in this corpus is often a `> [!tip]` or `> [!danger]` callout title**, which is a
   *claim*, not a description of scope. Where a section's callout title is vivid, I have
   quoted it; that biases the "uniquely held" column toward sections with striking openings.
   **A section whose distinguishing content sits in its fourth bullet is under-represented
   here.** This is a known blind spot, not a suspected one.
2. **No grouping implies a discard.** Twelve groups, zero merge recommendations.
3. Line numbers are valid at `90dc93f`. **Any move invalidates them**, including the PART B
   moves already flagged in this file.
