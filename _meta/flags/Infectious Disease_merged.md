# Infectious Disease_merged.md — grouping and misplacement flags

Status: **ANALYSED. NOTHING MOVED.**
Sources: 12 · lines 3594 · numbering drift: **none**.
Zero inbound: `08_04_Infectious_Disease_-_Antibiogram`, `NEW_Infectious_Diseases`.

## PROPOSED MOVES

### History-taking (standing rule) — the clearest one in the vault so far
| ID | Section | L | → | Why |
|---|---|---|---|---|
| I-1 | `## The STI Check — Sexual History, What to Test, and When` + `### Taking a sexual history` + `### What a standard asymptomatic check consists of` + `### Window periods` + `### After the result` | 870–923 | **History-Taking.md** | a named history-taking framework with its own heading. The disease entries below it (chlamydia, gonorrhoea, syphilis…) stay. **This is an OSCE station in its own right** |

### Investigation interpretation (standing rule, as extended)
`NEW_Investigations_Infectious_Diseases` is **23 investigation entries filed under a system**.
| ID | Section | L | → | Note |
|---|---|---|---|---|
| I-2 | `## 0.19 Autoimmune / Rheumatological Serology (ANA, anti-La/SSB, Scl-70, histone, myositis)` | 3464 | **Investigation-Interpretation.md §1.16** | **§1.16 "Autoimmune Markers — Systematic Reference" already exists** |
| I-3 | `## 0.20 Positive Autoimmune Serology (approach to an unexpected positive)` | 3490 | **Investigation-Interpretation.md §1.16** | pure interpretation — *"approach to an unexpected positive"* |
| I-4 | `## 0.21 Vasculitis Serology (ANCA, PR3, MPO, anti-GBM)` | 3511 | **Investigation-Interpretation.md §1.16** | serves `Renal §0.7 ANCA-Associated GN` and MSK vasculitis |
| I-5 | `## 0.18 Coeliac Serology (anti-tTG IgA, DGP)` | 3444 | **Investigation-Interpretation.md**; serves **GI §0.17 Coeliac Disease** | `Pediatrics:802` already cites *"[[03_Gastrointestinal]] Coeliac Disease — IgA-tTG plus total IgA"* |
| I-6 | `## 0.1 Gram Stain` · `## 0.2 Microbiology Panel (Wound C&S)` · `## 0.3 Viral Culture` | 3104–3158 | **Investigation-Interpretation.md §1.18** | **§1.18 "Blood Cultures and Microbiology Basics" already exists** |
| I-7 | `## 0.9 Stool & Fecal Studies` (culture, multiplex PCR, O/C/P, **faecal calprotectin, FOBT/FIT**) | 3253 | **Investigation-Interpretation.md**; calprotectin and FIT serve **GI** (IBD, bowel screening) | |
| I-8 | `## 0.12 HIV Panel` · `## 0.13 Western Blot` · `## 0.14 Syphilis Panel` · `## 0.15 Monospot` · `## 0.16 Parvovirus Serology` · `## 0.17 ASOT / anti-DNase B` | 3308–3443 | **Investigation-Interpretation.md** | ASOT serves `Cardio §0.22 Rheumatic Fever` |
| I-9 | organism entries `## 0.4 Bacteroides` · `0.5 Fusobacterium` · `0.6 Enterococcus` · `0.7 CPE` · `0.8 Candida` · `0.10 Cryptosporidium` · `0.11 Giardia` · `0.22 Campylobacter` · `0.23 C. perfringens` | 3159–3576 | **flag — axis question** | these are **organisms**, not investigations. They duplicate the disease entries in `08_01-03` and `08_07`. Recommend folding into those, not moving to Investigation-Interpretation |

### Topic in the wrong system
| ID | Section | L | → | Why |
|---|---|---|---|---|
| I-10 | `## Vaccination Schedule (Australia — NIP)` + `### Influenza vaccination` + `## Passive Immunisation — Immunoglobulin After an Exposure` | 332–404 | **preventive health** — `GER3_Preventive_and_Occupational_Health` (per CLAUDE.md §1.10's mapping) or `PH1` | schedule and eligibility, not infection management. Pairs with `NEW_Drugs_20 §0.1 Vaccines` (2957) |
| I-11 | `## Notifiable Diseases (Australia)` **and** `## Notifiable Diseases in Australia — What "Notifiable" Actually Means` | 327, 1313 | **`A10_Ethics__Capacity__Consent_and_Certification` or `PH1`** | **two sections on the same topic in one merged file, from two different sources.** The duty to notify is a legal/public-health obligation |
| I-12 | `## Mastitis and Breast Abscess` | 1133 | **OBGYN** | lactational mastitis. Ties to Heme H-19 (the breast source) |
| I-13 | `## Sepsis` | 1242 | **flag — Emergency owns it** | `Emergency A1 §0.2 SIRS, Sepsis and Septic Shock`, `§0.3 Sepsis Phenotypes by Source`, `F0-3 §0.7`–`§0.10`. Five sepsis sections across two files |
| I-14 | `## Spinal epidural abscess` | 1268 | **flag** | duplicates `Neuro 04_Neurology ### Spinal Epidural Abscess` (596) |
| I-15 | `## Post-splenectomy sepsis` | 1184 | **flag** | with `GI C1 §0.5` post-splenectomy prophylaxis and `Heme 10_09b ## Hyposplenism` |
| I-16 | `### Acute epiglottitis` | 112 | **flag — ENT owns it** | `ENT ## Acute epiglottitis` and `Emergency A2 §0.5 Acute Stridor` |
| I-17 | `### Centor criteria (sore throat)` | 290 | **flag — ENT owns it** | `Cardio §0.22` already routes to `[[13_05a_ENT_-_Sore_Throat_and_Tonsillitis]]`, noting **Centor/FeverPAIN thresholds do not apply the same way in Australia** — that caveat must not be lost |
| I-18 | `## 0.5 Allergic Rhinitis and the Atopic March` (K4) | 2379 | **flag — ENT owns it** | `ENT ## Allergic Rhinitis (Hay Fever)` |
| I-19 | `## 0.6 Urticaria, Angioedema and Mast Cell Disorders` (K4) | 2412 | **flag — Derm** | `Derm:2242` routes *"Urticaria, anaphylaxis and drug reaction labelling → [[K4]] 0.2–0.3"*, i.e. **Derm points back here** — the boundary is genuinely contested. Decide with Derm |
| I-20 | `## Diarrhoea — differential diagnosis` + `## Gastroenteritis — causes by incubation time` | 1331, 1353 | **flag — GI owns it** | `GI C5 §0.3 Acute Diarrhoea and Gastroenteritis`. **`08_10` has only 4 inbound, 2 internal** |

## KEEP + IN-TEXT FLAG
- `K4_Allergy_and_Clinical_Immunology` is **allergy and immunology filed under infectious disease** —
  7 sections, 5 inbound (Derm ×2, Paeds, Resp, internal). Its own referrers are dermatological and
  respiratory. **Candidate for its own home; flag as a set, not section by section.**
- `08_04 Antibiogram` (4 sections, **zero inbound**) is a **drug-selection reference** —
  empirical cover by organism. Overlaps `NEW_Drugs_05 §0.2 Antibacterials` (21 subsections).
- `## Cross-references — other infections covered elsewhere in this project` (1386) is an
  administrative section inside clinical content — same shape as `Resp §0.22`. Candidate for `_meta/`.
- `## Approach to Fever in the Returned Traveller` (1220) and `K1 §0.4 Fever in the Returning
  Traveller` (1541) are **the same topic twice in one file**.

## GROUPINGS
**HIGH**
- **G-I1 Fever workup** — `08_09 ## PUO/FUO` (1192) · `## Approach to Fever in the Returned
  Traveller` (1220) · `K1 §0.1 Mechanism and Approach` (1419) · `§0.2 Acute Undifferentiated Fever`
  (1465) · `§0.3 FUO and Prolonged Fever` (1503) · `§0.4 Returning Traveller` (1541) ·
  `§0.5 Immunocompromised and Febrile Neutropenia` (1587) · `§0.6 Post-Operative and Drug Fever`
  (1627) · `NEW_Infectious_Diseases ## Fever in Immunocompromised Patient` (3033).
  **Nine sections, four sources, one topic.** (+ `Heme 10_10a ## Neutropenic sepsis`, `J5 §0.2`)
- **G-I2 Skin and soft tissue infection** — `08_09 ## Cellulitis` (1110) · `## Necrotising fasciitis`
  (1161) · `## Animal & human bites` (1101) · `K2 §0.1 Cellulitis and Erysipelas` (1682) ·
  `§0.2 Necrotising Soft Tissue Infection` (1733) · `§0.3 Abscess, Boils and Deep Space` (1769) ·
  `§0.4 Lymphangitis, Lymphadenitis` (1813) · `§0.5 Bites, Wounds and Australian Exposures` (1851) ·
  `§0.6 Infestations` (1891) · `NEW_Drugs_05 §0.2.20 Antibacterials (Skin)` (2710)
- **G-I3 HIV** — `08_05-06 ## HIV` +`### drug classes` +`### OI by CD4 count` (631–681) ·
  `K3 §0.4 HIV and Opportunistic Infection` (2086) · `NEW_Drugs_05 §0.5` +`.1`–`.5` (2783–2830) ·
  `NEW_Inv_ID §0.12 HIV Panel` (3308) · `§0.13 Western Blot` (3330).
  (+ `Neuro ## CNS Infections Associated with Immunosuppression`, which ID:676 already defers to)
- **G-I4 Exposure, PEP and PrEP** — `K3 §0.1 Occupational and Bloodborne Virus Exposure` (1948) ·
  `§0.2 Non-Occupational Exposure, PEP and PrEP` (1994) · `08_01-03 ## Passive Immunisation` (369)
- **G-I5 Tuberculosis** — `K3 §0.3` (2031). **Cross-file with `Resp §0.9` +6 subsections and
  `NEW_Inv_Resp §0.7 TB Screening`** — see Resp R-13. **Three homes**
- **G-I6 STIs** — `08_08` ## chlamydia (950) · genital herpes (975) · genital warts (985) ·
  gonorrhoea (995) · LGV (1014) · syphilis +congenital (1023, 1053) · chancroid (944) ·
  donovanosis (1059) · *M. genitalium* (1068) · trichomonas (938) · BV (924) · pubic lice (1077) ·
  `## STI ulcers — summary DDx` (1086) · `NEW_Inv_ID §0.14 Syphilis Panel` (3348)
- **G-I7 Gastrointestinal infection** — `08_01-03 ## Campylobacter` (24) · `## C. difficile` (121) ·
  `## Cholera` (51) · `## E. coli` (70) · `## Enteric fever` (86) · `## Bacillus cereus` (14) ·
  `08_05-06 ## Norovirus` +`### DDx of acute gastroenteritis` (543, 550) · `08_07 §0.1 Amoebiasis`
  (752) · `§0.2 Cryptosporidiosis` (762) · `§0.4 Giardiasis` (774) · `08_10` (1331, 1353) ·
  `NEW_Inv_ID §0.9`, `§0.10`, `§0.11`, `§0.22`, `§0.23`
- **G-I8 Malaria and travel-related parasitic disease** — `08_07 §0.6 Malaria` +`.1 falciparum`
  +`.2 non-falciparum` (789–817) · `§0.5 Leishmaniasis` (781) · `§0.7 Schistosomiasis` (818) ·
  `§0.8 Trypanosomiasis` (829) · `§0.9 Other mosquito-borne` +`.1`–`.3` (839–867) ·
  `§0.3 Cutaneous larva migrans` (768) · `08_05-06 ## Dengue` (486) · `## Yellow fever` (622) ·
  `## Ebola` (497) · `## Rabies` (606) · `K3 §0.6 Vector-Borne and Zoonotic Disease in Australia`
  (2171) · `NEW_Drugs_05 §0.4.1 Antimalarials` (2763)
- **G-I9 Antimicrobial pharmacology** — the whole of `NEW_Drugs_05` §0.1–§0.6 (2524–2888) ·
  `08_04 Antibiogram` (406–474) · `08_09 ## Antimicrobial side effects` (1299)
- **G-I10 Childhood exanthems and vaccine-preventable disease** — `08_05-06 ## Measles` (558) ·
  `## Mumps` (527) · `## Rubella` (606) · `## Parvovirus B19` (696) · `## HFMD` (706) ·
  `## Viral exanthemata` (714) · `08_01-03 ## Diphtheria` (57) · `## Tetanus` (233).
  **Cross-file: `Pediatrics 15_03a Childhood Viral Exanthems`.** ⚠️ `Resp §0.22` explicitly parked
  **diphtheria** *"for whichever of those files comes up next in the rotation"* — **it landed here**
- **G-I11 Allergy and immunology** — `K4 §0.1`–`§0.7` (2229–2508). See the K4 flag above
- **G-I12 Streptococcal disease** — `08_01-03 ## Streptococcus` +`### Scarlet fever`
  +`### Centor criteria` +`### Group B Strep` (265–326) · `NEW_Inv_ID §0.17 ASOT` (3424).
  (+ `Cardio §0.22 Rheumatic Fever`, `§0.23 RHD`)
- **G-I13 Staphylococcal disease** — `08_01-03 ## Staphylococci` +`### Toxic shock` +`### MRSA`
  (205–232)
- **G-I14 Vaccination** — `08_01-03 ## Vaccination Schedule` +`### Influenza` (332–368) ·
  `NEW_Drugs_20 §0.1 Vaccines` (2957) · `§0.2 Immunoglobulins` +`.1 IVIG` (2989–3008)

**MEDIUM**
- **G-I15 Immunodeficiency** — `K3 §0.5 Immunodeficiency and Screening Before Immunosuppression`
  (2130). **Cross-file with `Heme 10_03a Primary Immunodeficiencies` (15 sections) and
  `Pediatrics 15_15b`** — see Heme H-12. **Three homes**
- **G-I16 Atypical and zoonotic bacteria** — `## Anthrax` (6) · `## Cat scratch` (45) ·
  `## Leptospirosis` (197) · `## Lyme disease` (153) · `## Q fever` (191) · `## Leprosy` (145) ·
  `## Botulism` (31) · `## Other Clostridia` (254)
- **G-I17 Respiratory infection** — `## Legionella` (100) · `## Mycoplasma pneumoniae` (175) ·
  `## H. influenzae` +`### epiglottitis` (107, 112) · `## Influenza` (729) · `## COVID-19` (743) ·
  `## Pseudomonas` (170) · `## Klebsiella` (78). **Cross-file with `Resp §0.8` pneumonia set**
- **G-I18 Herpesviruses** — `## CMV` (476) · `## Infectious mononucleosis` +`### EBV-associated`
  (507, 522) · `## HSV` (583) · `NEW_Inv_ID §0.15 Monospot` (3376)
- **G-I19 Lemierre's / deep neck** — `## Lemierre's syndrome` (1151) · `NEW_Inv_ID §0.5
  Fusobacterium` (3177). Cross-file with ENT neck lumps

**UNGROUPED — stays put**: `## Mpox` (682) · `## Nematode infections` (1285) ·
`## Threadworms` (1292) · `NEW_Drugs_05 §0.1 Anthelmintics` (2524) · 4 administrative blocks

## LIMITATIONS
- I-19 (urticaria/angioedema) is a **genuine two-way disagreement** — Derm points here, this file
  holds the content. Not resolvable until the Derm pass.
- I-13 (sepsis), I-16/I-17/I-18 (ENT), I-20 (GI), G-I5 (TB), G-I10 (exanthems), G-I15
  (immunodeficiency) all deliberately undecided pending other files.
