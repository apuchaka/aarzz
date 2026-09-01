# Psychiatry_merged.md — grouping and misplacement flags

Status: **ANALYSED. NOTHING MOVED.**
Sources: 15 · lines 1405 · numbering drift: **none**. Zero inbound: `NEW_Psychiatry`.

## READ WITH `_meta/flags/Neuro_merged.md` FIRST
**This file holds only half of psychiatry.** The Corpus B set (`N1`–`N8`, 1,624 lines) is in
`Neuro_merged.md:3829–5452`. Every grouping below has a Corpus B partner **in another file**:

| This file (Corpus A) | L | Partner, in **Neuro_merged** | L |
|---|---|---|---|
| `14_01 Mood Disorders` | 5 | `N4_Mood_Disorders` | 4472 |
| `14_02 Anxiety and Related Disorders` | 174 | `N5_Anxiety__OCD_and_Trauma` | 4714 |
| `14_03 Psychotic Disorders and Antipsychotics` | 288 | `N3_Psychosis_and_Antipsychotics` | 4251 |
| `14_04 Personality Disorders` + `14_05c Unexplained Symptoms` | 443, 690 | `N6_Functional__Dissociative__Personality` | 4904 |
| `14_05a Eating Disorders` | 602 | `N8_Eating_Disorders` | 5264 |
| `14_05b Insomnia` | 671 | `N7_Sleep_Disorders` | 5080 |
| `14_06b Mental Health Act and Sectioning` | 837 | `N1_Mental_State_Examination_and_Risk` | 3829 |
| `14a-1 Substance Misuse` + `14a-2 Overdose` | 914, 1050 | `N2_Acute_Behavioural_Disturbance_and_Substance_Use` | 4067 |

**No section-level grouping is worth doing until the eight sources are in one file.**
Detailed groupings are therefore **deliberately deferred**, not omitted.

## PROPOSED MOVES
| ID | Section | L | → | Why |
|---|---|---|---|---|
| Y-1 | `14a-2 Overdose and Poisoning Management` — `§0.1 by agent` · `§0.2 Digoxin` · `§0.3 Salicylate` · `§0.4 TCA` | 1054–1090 | **Emergency** | `Emergency A5 §0.1 The Poisoned Patient`, `§0.2 TCA Overdose`, `F0-1 §0.1`–`§0.8`, `NEW_Drugs_04 Antidotes and Antivenoms`. **Salicylate also duplicates `Endocrine F0-2 §0.8`.** 1 inbound (Examination) |
| Y-2 | `## 0.5 Postpartum (Puerperal) Psychosis` | 358 | **OBGYN** | ⚠️ **the other half of OBGYN B-10** (`## Puerperal psychosis`, OBGYN 1481) and `O3 §0.6 Perinatal Mental Health`. **Three homes** |
| Y-3 | `## Perinatal depression` | 158 | **flag — with Y-2** | same cluster |
| Y-4 | `## Guardianship — a related but distinct framework` | 883 | **`A10_Ethics__Capacity__Consent_and_Certification`** | guardianship is a capacity framework, not a psychiatric disorder |
| Y-5 | `14_06b Mental Health Act and Sectioning` (9 sections: involuntary treatment, CTOs, ITOs, SACAT, interstate transfer, safeguards, police, voluntary inpatients) | 837–889 | **flag — `A10` or keep** | **SA-specific mental health law.** Its Corpus B partner `N1 §0.5 Mental Health Legislation in South Australia` **carries a `> [!danger] Verify everything in this section` warning.** Keep the warning with whichever copy survives |
| Y-6 | `14_07 Attention Deficit Hyperactivity Disorder` | 890–913 | **decide with Paediatrics** | **5 inbound, Paediatrics ×3.** `Pediatrics M7 §0.6 ADHD` (4086) is the partner; `NEW_Drugs_17 §0.5` is the drug half |
| Y-7 | `## Gambling disorder (gambling-related harms)` | 1021 | **arguable — GP / PH1** | a behavioural-addiction and public-health topic filed under recreational drug profiles |
| Y-8 | `14_05d Electroconvulsive Therapy` | 736–758 | **flag — procedures** | consent, workup and complications of a procedure. 1 inbound, internal |
| Y-9 | `**Focused Hx:** / **Examination:**` in `NEW_Psychiatry ## Acute Behavioural Disturbance` | 1361–1362 | **History-Taking.md / Examination.md** | L1362 is explicitly about the limits of examining an agitated patient |

## KEEP + IN-TEXT FLAG
- **Alcohol withdrawal — the four-way split confirmed from this end.** `## Alcohol use disorder`
  (917) carries pointers to `[[03_Gastrointestinal]] Alcohol withdrawal` at **:934 and :938**,
  naming it *"the full AU-verified management (diazepam-based…)"*. The other copies are
  `N2 §0.1` (Neuro 4077) and `04_Neurology ### Alcohol Withdrawal Seizures` (Neuro 804).
  **GI M-5 (add a pointer from here) is correct and already half-built — the pointers exist; it is
  the content that is elsewhere.**
- `14_06a Drugs Used in Psychiatry` (8 sections, 759–836) and `NEW_Drugs_17_Psychotropic`
  (8 sections + 15 subsections, 1092–1304) are **two drug references for the same classes in one
  file** — benzodiazepines, lithium, SSRIs, SNRIs, TCAs, MAOIs, Z-drugs all appear in both.
- `## Eponymous syndromes (appendix)` (278) is an appendix inside clinical content.

## GROUPINGS — deferred
Corpus A groupings that stand **within this file** regardless of the Neuro question:
- **G-Y1 Mood** — `14_01 ## Depression` +`### screening` +`### Mx` +`### switching` +`### SSRIs`
  (6–52) · `## Bipolar` +`### manic` +`### hypomanic` +`### Mx` (93–130) · `## Cyclothymia` (131) ·
  `## Seasonal affective disorder` (144) · `## Perinatal depression` (158) ·
  `NEW_Drugs_17 §0.1` +`.1`–`.5` (1103–1161) · `§0.4 Drugs for Bipolar` +`.1 Lithium`+`.2` (1226–1246) ·
  `14_06a §0.2 Lithium` `§0.3 Mirtazapine` `§0.4 MAOIs` `§0.5 SSRIs` `§0.6 SNRIs` `§0.7 TCAs`
- **G-Y2 Suicide and self-harm** — `14_01 ## Suicide` (53) · `## Self-harm` (78).
  (+ `N1 §0.2 Risk Assessment`, `§0.3 Suicide and Self-Harm` — **in Neuro**)
- **G-Y3 Anxiety spectrum** — `14_02` all 9 sections (175–287) · `NEW_Drugs_17 §0.3` +`.1`–`.3`
  (1197–1225) · `14_06a §0.1 Benzodiazepines` `§0.8 Z-drugs`
- **G-Y4 Psychosis and antipsychotics** — `14_03 §0.1`–`§0.6.7` (289–442) ·
  `NEW_Drugs_17 §0.2` +`.1 Clozapine` (1162–1196)
- **G-Y5 Personality and functional disorders** — `14_04` all 14 sections (444–601) ·
  `14_05c` all 6 sections (691–735)
- **G-Y6 Eating disorders** — `14_05a ## Anorexia` (603) · `## Bulimia` (622) · `## Binge-eating`
  (645). **N8 has 17 inbound from across the vault — see Neuro**
- **G-Y7 Sleep** — `14_05b ## Insomnia` (672) · `NEW_Drugs_17 §0.3.3` · `14_06a §0.8 Z-drugs` (827)
- **G-Y8 Substance use** — `14a-1` all 10 sections (917–1053) · `NEW_Drugs_17 §0.6 Alcohol
  Dependence` (1268) · `§0.7 Nicotine Dependence` (1282)
- **G-Y9 ADHD** — `14_07 §0.1` (891) · `NEW_Drugs_17 §0.5` +`.1`–`.3` (1247–1267). See Y-6

## LIMITATIONS
**The main deliverable for this file cannot be produced until the N1–N8 question is settled.**
Producing section groupings now would mean grouping half a corpus against itself and would have to
be redone. This is stated as an incomplete output, not a clean one.
