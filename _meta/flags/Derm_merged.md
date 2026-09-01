# Derm_merged.md — grouping and misplacement flags

Status: **ANALYSED. NOTHING MOVED.**
Sources: 12 · lines 2609 · numbering drift: **none**. Zero inbound: `NEW_Dermatology`.
**The tidiest Corpus-A-to-Corpus-B mapping in the vault so far** — G1–G6 map cleanly onto 09_01–09_08.

## PROPOSED MOVES

### Topic in the wrong system
| ID | Section | L | → | Why |
|---|---|---|---|---|
| D-1 | `## Anaphylaxis` | 6 | **Emergency / ID(K4)** | `Emergency F0-1 §0.9 Anaphylaxis and Acute Allergic Reaction`, `NEW_Drugs_01_Allergy_and_Anaphylaxis` (a whole source in Emergency), `Pediatrics 15_01b Anaphylaxis`. **Four homes.** `ENT:1252` routes *"anaphylaxis and angioedema in [[K4]] 0.2"* — i.e. to ID |
| D-2 | `## Acute urticaria and angioedema` | 38 | **decide with ID** | ⚠️ **the two-way disagreement flagged as ID I-19.** ID holds `K4 §0.6 Urticaria, Angioedema and Mast Cell Disorders`; **Derm:2242 points AT ID for it**, while Derm also holds this section. **Both files defer to the other.** Needs a ruling |
| D-3 | `## Necrotising fasciitis` | 135 | **flag** | `ID 08_09 ## Necrotising fasciitis` and `ID K2 §0.2` — **three homes** |
| D-4 | `## Cellulitis & erysipelas` | 575 | **flag** | `ID 08_09 ## Cellulitis`, `ID K2 §0.1`, `Derm G1 §0.6 Cellulitis and Its Mimics` — **four homes**. See ID G-I2 |
| D-5 | `## Varicella zoster virus / chickenpox` + `### PEP` + `### VZV in pregnancy` + `## Herpes zoster / shingles` | 729–792 | **flag — ID/OBGYN** | `ID 08_05-06` defers here explicitly; **VZV in pregnancy** belongs with OBGYN, and `Cardio NEW_Inv §0.35 Rubella/Varicella Serology` (approved GI M-4 destination is ID) is the serology half |
| D-6 | `## Head lice` · `## Scabies` | 579, 599 | **flag** | `ID K2 §0.6 Infestations`; `NEW_Drugs_08 §0.5 Scabicides and Pediculicides` (2528) is the drug half |
| D-7 | `## 0.2 The Endocrine and Neoplastic Causes` (G6) — the **carcinoid syndrome** block | 2082–2119 | **decide with GI/Endocrine** | ⚠️ **the mechanism half of approved GI M-13.** `Derm:2084–2100` carries *"why the liver explains everything about it"*, carcinoid crisis, and the octreotide-before-anaesthesia warning. **GI §0.15 has the disease entry; Derm has the mechanism** |
| D-8 | `## 0.4 The Systemic Vasculitides` (G3) | 1540 | **flag — MSK owns it** | `MSK 12_04` (10 sections) and `L2 §0.5`. **G3 §0.3 Cutaneous Small Vessel Vasculitis (1501) legitimately stays** — that is the skin-limited disease |
| D-9 | `## 0.6 Cyanosis and Abnormal Skin Colour` (G6) | 2204 | **arguable — Resp/Cardio** | central vs peripheral cyanosis is a respiratory/cardiac sign. Includes methaemoglobin — see Heme H-14 |
| D-10 | `## Pyoderma gangrenosum` | 248 | **keep, flag** | strongly associated with IBD (`GI §0.16.3 Extra-intestinal features`). Skin lesion, so it stays; flag the link |
| D-11 | `## 0.6 Wounds, Pressure Injury and Leg Ulcers` (G2) | 1385 | **flag** | `Examination.md §1.27 Leg and Skin Ulcers` and `§1.28 Wound Management` **already exist**; `Cardio §0.36.8 Lower Leg Ulcers` is a third. **Pressure injury** ties to Geriatrics |

### Examination / investigation interpretation (standing rule)
| ID | Section | L | → | Note |
|---|---|---|---|---|
| D-12 | `## Skin lesion morphology — reference terms` | 942 | **Examination.md §1.15** | **§1.15 "Dermatological Examination" already exists.** This is the vocabulary that examination uses |
| D-13 | `## 0.1 Describing a Rash` (G1) | 1048 | **Examination.md §1.15** | *how to describe*, not what it is. Same shape as MSK K-15 (`Describing a Fracture`) |
| D-14 | `## 0.1 Assessing a Pigmented Lesion` (G5) | 1873 | **Examination.md §1.15** | ABCDE / dermatoscopy assessment method. **`09_02` has 10 inbound: Examination ×4, Communication ×2, History-Taking** — the referrer profile is the Clinical Process set |
| D-15 | 6 × `**Focused Hx:**` + 6 × `**Examination:**` in `NEW_Dermatology` | 2264–2318 | **History-Taking.md / Examination.md** | L2274 *"full skin examination with the patient undressed"*; L2304 *"Nikolsky's sign"* |
| D-16 | `## 0.5 Nails` (G5) | 1985 | **flag — Examination** | nail signs are read in every system examination (`Examination.md §1.9` already lists clubbing, leuconychia, koilonychia) |

## KEEP + IN-TEXT FLAG
- **`## Non-blanching rashes — approach and differential` (920) and `G3 §0.1 Approach to the
  Non-Blanching Rash` (1441) and `NEW_Dermatology ## Non-Blanching Rash and Purpuric Rash` (2307)**
  are the same topic three times **within this one file**.
- `## Pruritus (Itch)` (975) · `G4 §0.4 Pruritus` (1764) — twice. Plus `GI C6 §0.6 Pruritus Ani`
  and the cholestatic pruritus in `GI §0.1/§0.2` — **the itch differential is split by body site
  across two files**.
- `## Alopecia (Hair Loss)` (1001) · `G5 §0.6 Hair Loss` (2007) — twice.
- `Derm:2242` is a **cross-reference index block** listing 20 outbound pointers. It is the densest
  routing table in the vault and **several of its targets are contested** (K4, C3, I2, I4, AN1).
  Worth preserving as a routing artefact when anything moves.

## GROUPINGS
**HIGH** — Corpus A (09_*) and the G-files map almost one-to-one.
- **G-D1 Acute rash / the unwell patient with a rash** — `09_01 ## Cutaneous Drug Eruptions` (53) ·
  `## SJS/TEN` (77) · `G1 §0.2 The Acutely Unwell Patient with a Rash` (1075) ·
  `§0.3 Severe Cutaneous Adverse Reactions` (1108) · `§0.4 Drug Eruptions` (1146) ·
  `NEW_Derm ## Acute Rash` (2256) · `## Acute Inflammatory Dermatosis` (2277) ·
  `## Maculopapular Rash` (2290). (+ `Emergency A5 §0.6 Severe Cutaneous Adverse Reactions`)
- **G-D2 Blistering disease** — `09_08 ## Pemphigus` (822) · `## Bullous pemphigoid` (837) ·
  `## Erythema multiforme` (852) · `G2 §0.1 Approach to the Blistering Patient` (1247) ·
  `§0.2 Autoimmune Blistering Diseases` (1276) · `§0.3 Other Causes of Blistering` (1308) ·
  `NEW_Derm ## Blistering Rash` (2297) · `09_01 ## SSSS` (116) · `## Eczema herpeticum` (101)
- **G-D3 Purpura and vasculitis** — `09_08 ## Non-blanching rashes` (920) · `09_01 ## Cutaneous
  vasculitis` (139) · `G3 §0.1`–`§0.6` (1441–1636) · `NEW_Derm ## Non-Blanching Rash` (2307)
- **G-D4 Eczema and contact dermatitis** — `09_04 ## Contact Dermatitis` (386) · `## Eczema` +`###
  phases` +`### Mx` +`### Steroid creams` (405–466) · `G4 §0.1` (1638) · `NEW_Drugs_08 §0.2` +`.1`–`.4`
  (2415–2463)
- **G-D5 Psoriasis** — `09_04 ## Psoriasis` +`### classification` +`### Mx` (467–520) ·
  `G4 §0.2` (1683) · `NEW_Drugs_08 §0.3` +`.1`–`.5` (2464–2512). (+ `MSK 12_01 ## Psoriatic arthritis`)
- **G-D6 Melanoma and pigmented lesions** — `09_02 ## Melanoma` +`### DDx` (154, 205) ·
  `## Benign naevi` +`### subtypes` (219, 224) · `## Seborrhoeic keratosis` (232) ·
  `## Dermatofibroma` (241) · `G5 §0.1 Assessing a Pigmented Lesion` (1873) · `§0.2 Melanoma` (1905) ·
  `§0.4 Premalignant and Benign Lesions` (1968)
- **G-D7 Non-melanoma skin cancer** — `09_03a ## BCC` (265) · `## SCC` +`### stages` +`### Mx`
  (281–320) · `G5 §0.3` (1943)
- **G-D8 Acne and rosacea** — `09_03b ## Acne vulgaris` +4 subsections (322–384) ·
  `09_04 ## Rosacea` +`### Mx` (521, 536) · `G4 §0.3 The Other Chronic Dermatoses` (1723) ·
  `NEW_Drugs_08 §0.1` +`.1`–`.4` (2369–2414)
- **G-D9 Fungal skin infection** — `09_06 ## Tinea` +`### onychomycosis` +`### capitis`
  +`### corporis` +`### pedis` +`### versicolor` (621–676) · `## Candida` (677) ·
  `## Seborrhoeic dermatitis` (699) · `NEW_Drugs_08 §0.4.1` (2515) ·
  (+ `MSK NEW_Inv_Ortho §0.14 KOH Preparation` — see MSK K-7)
- **G-D10 Viral skin infection** — `09_06 ## Viral warts` (690) · `## Molluscum` (714) ·
  `09_07 ## VZV/chickenpox` (729) · `## Herpes zoster` (761) · `## Pityriasis rosea` (779) ·
  `NEW_Drugs_08 §0.6 Drugs for Warts` (2547) · `G1 §0.5 Infectious Exanthems in Adults` (1171)
- **G-D11 Bacterial skin infection** — `09_05 ## Impetigo` (548) · `## Folliculitis` (566) ·
  `## Cellulitis & erysipelas` (575) · `09_01 ## SSSS` (116) · `## Necrotising fasciitis` (135) ·
  `G1 §0.6 Cellulitis and Its Mimics` (1199). **Cross-file with `ID K2` — see ID G-I2**
- **G-D12 Pruritus** — `09_08 ## Pruritus (Itch)` (975) · `G4 §0.4 Pruritus` (1764)
- **G-D13 Hair and nails** — `09_08 ## Alopecia` (1001) · `G5 §0.5 Nails` (1985) ·
  `§0.6 Hair Loss` (2007)
- **G-D14 Flushing and sweating** — `G6 §0.1 Approach to Flushing` (2051) · `§0.2 Endocrine and
  Neoplastic Causes` (2082) · `§0.3 Menopause, Drugs and Common Causes` (2120) ·
  `§0.4 Hyperhidrosis` (2141) · `§0.5 Anhidrosis` (2178). **No Corpus A partner** — G6 is C-only
- **G-D15 Erythroderma and skin failure** — `G2 §0.4 Erythroderma` (1336) · `§0.5 Skin Failure` (1362)

**MEDIUM**
- **G-D16 Chronic dermatoses** — `09_08 ## Lichen planus` (882) · `## Erythema nodosum` (868) ·
  `09_07 ## Hidradenitis suppurativa` (793) · `G4 §0.3` (1723)
- **G-D17 Pigmentation and photosensitivity** — `G4 §0.5 Pigmentation` (1801) ·
  `§0.6 Photosensitivity and Sun Protection` (1824). Sun protection ties to preventive health
- **G-D18 Bites and stings** — `09_08 ## Insect bites` (897). Cross-file with `ID K2 §0.5 Bites,
  Wounds and Australian Exposures` and `Emergency F0-1 §0.10/§0.11` (snakebite, spiders)
- **G-D19 Cysts and lumps** — `09_08 ## Epidermoid (Sebaceous) Cyst` (1023).
  **Cross-file with `Cardio B6 §0.8 Undifferentiated Lump`** — which Cardio C-10 already flags as
  having 19 inbound and none from cardiology

## LIMITATIONS
- **D-2 (urticaria/angioedema) and D-7 (carcinoid) are both two-way**: another file points here for
  content this file also holds, or vice versa. Neither is resolvable from one side.
- D-1, D-3, D-4, D-5, D-6 all await the ID pass conclusion; D-8 awaits MSK; D-9 awaits Resp/Cardio.
