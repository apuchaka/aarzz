# GI_merged.md — grouping and misplacement flags

Status: **ANALYSED. Decisions received from user. NOTHING MOVED.**
Sources: 11 · headings 352 (132 are `Mx – Immediate/Definitive/Chronic` boilerplate) · lines 4271

## Calibration cases — both confirmed independently
- `Glasgow-Imrie` named at C7 §0.1 (L3179) with no components; components sit at 03_GI §0.11 (L1529)
  under `> [!info] Glasgow score — mnemonic "PANCREAS"`. Neither file has both halves.
- `West Haven` appears **0 times in the whole vault**. The complete four-grade scale is at
  03_GI §0.6.3 (L225) under a callout reading only `> [!info] Grading`.

## MOVES — approved by user, not yet executed
| ID | Section | L | From → To | Notes |
|---|---|---|---|---|
| M-1 | `## 0.32 CSF Studies (β-transferrin)` | 4180 | GI → **Neuro** | self-declared misfile |
| M-2 | `## 0.33 Coombs / DAT-IAT` | 4197 | GI → **Heme Onc** | self-declared misfile |
| M-3 | `## 0.34 G-CSF` | 4211 | GI → **NEW_Drugs_07** | a drug, not a test; carries live `UNRESOLVED` marker |
| M-4 | `## 0.35 Rubella / Varicella Serology` | 4217 | GI → **Infectious Disease** | self-declared misfile |
| M-R1 | `## 0.3 Barrett's oesophagus`, `## 0.4 Oesophageal carcinoma` | ENT 653, 666 | **ENT → GI** | Dysphagia approach, pharyngeal pouch, globus **STAY in ENT** |
| M-6 | `## 0.10 Abdominal Trauma` | 1789 | GI → **Emergency** | user accepts it stays orphaned there; `FAST` appears 1× in Emergency |
| M-7 | examination half of `## 0.2 Assessment, Peritonism…` | 1532–1557 | GI → **Examination.md §1.9** | **`**Ix — the core panel**` para at L1558 STAYS in GI** |
| M-8 | `## 0.10 Paracetamol Overdose` + `### 0.10.1 King's College` | 459 | GI → **Emergency** | **deliberate duplicate — do NOT merge with Emergency §0.6** |
| M-9 | `## 0.4 Ascending Cholangitis` | 96 | GI → **Emergency** | **deliberate duplicate — do NOT merge with Emergency §0.11** |
| M-16 | `**Focused Hx:**` + `**Examination:**` blocks of `## Acute Abdominal Pain` and `## Upper GI Bleeding` | 3684–3688, 3715–3717 | GI → **History-Taking.md / Examination.md** | leave pointers |

### Carry with M-8 / M-9
- GI's paracetamol entry holds the **2020 ANZ guideline verification box WITH figures**;
  Emergency §0.6 holds **no figures** and an `UNVERIFIED — the nomogram treatment line …
  the highest-consequence category of number in this file`. **Keep both markers intact and
  adjacent so the contradiction is visible.**
- **Retarget inbound pointers or they break silently:**
  - `Psychiatry_merged.md:1069` → GI's paracetamol copy
  - `Infectious Disease_merged.md:1388` → GI's cholangitis copy
  - `GI_merged.md:1505` (C1 §0.1 must-not-miss list) → Emergency's copy, via `[[F0.3]] 0.11`
  - `ENT_merged.md:662` carries a stale numeric pointer `*(See also 03.08 for GORD)*` —
    **03.08 is not GORD**; GORD is 03_Gastrointestinal §0.28.

## KEEP + ADD IN-TEXT FLAG
- **M-10** `## 0.3 Bilious versus Non-Bilious Vomiting` (L1948) — flag that the neonatal/infant
  two-thirds duplicate Paediatrics, which owns `## Mid-gut malrotation` (P972),
  `## Pyloric stenosis` (P894), `## Hirschsprung disease` (P910), `## 0.4 Neonatal Vomiting` (P3168).
- **M-17** `## 0.31 Pale Stools` (L4168) — a symptom filed as an investigation. Belongs with C3 §0.3.
- **M-18** `## 0.36 Gastrografin` (L4234) — flag, **and REWRITE the heading**. The
  `**OUT OF SCOPE, built in error**` statement is about the build list it came from, **not the file**,
  and reads as a move instruction. Content is correct and belongs with G14.
- **M-13** `## 0.15 Neuroendocrine Tumours / Carcinoid` (L600) — flag all three locations for
  manual consolidation: **GI §0.15**, **Derm_merged L2084–2100** (holds the mechanism — the
  portal-circulation explanation and carcinoid crisis), **Endocrine** as third candidate.

## KEEP + ADD POINTER
- **M-5** `### 0.6.1 Alcohol withdrawal` (L191) stays in GI. **Add a pointer from
  Psychiatry_merged `## Alcohol use disorder` (L917)** so a reader arrives.
  5 inbound: Psychiatry:934, :938, GP:113, Neuro:805, :806.

## KEEP, NO FLAG
M-11 (`## 0.8 Suprapubic Pain`) · M-12 (`## 0.11 Special Groups`) · M-14 (`## 0.5 Occult/Obscure
Bleeding + IDA`) · M-15 (`## 0.5 Intra-abdominal Abscess` — 8 inbound, **none from GI**:
ID×3, MSK×3, Anaes×2) · M-19 (`## 0.22 Pilonidal Disease`)

## RECORDED, NOT ACTIONED
- **Constipation is a load-bearing orphan.** `## 0.2 Constipation` (C5, L2687) has **no Corpus A
  partner** — searched all of lines 1–1473; constipation appears there only as a symptom inside
  11 other entries. 5 inbound from 3 files (Geriatrics×2, Neuro×2, Paediatrics×1).
- **PERT / exocrine pancreatic insufficiency stated in 8 places across 4 sources:**
  03_GI L545, L549, L550, L594, L618, L1415 · C7 L3277, L3392 · NEW_Drugs_12 L3600 · NEW_Inv L3921.
  **Record, do not consolidate.**
- **`## 0.9` and `## 0.10` of NEW_Inv_Gastro are a duplicate pair inside one source** (H. pylori
  testing, then urea breath test again as its own entry).
- `Resp_merged.md:933` → `NEW_Drugs_12 0.8.2` for PERT: **pointer is correct**, heading
  (`### 0.8.2 Other Agents in This Group`) is misleading. PERT is the second bullet.

## GROUPINGS
HIGH: G1 acute abdomen approach (03_GI §0.41 + C1 §0.1 + C1 §0.2 + NEW_Gastro `## Acute Abdominal
Pain` — **three copies**) · G2 complications of cirrhosis (03_GI §0.6.2/.3/.4/.6 + §0.32 + C3 §0.6 +
C4 §0.3 + NEW_Inv §0.30) · G3 upper GI bleeding (**three Glasgow-Blatchford treatments**) ·
G4 PUD/H. pylori · G5 dyspepsia/GORD · G6 oesophageal disease · G7 acute pancreatitis ·
G8 chronic pancreatitis · G9 pancreatic malignancy · G10 cirrhosis/CLD · G11 jaundice (**C-only, no
A partner**) · G12 acute liver failure + paracetamol · G13 lower GI bleeding · G14 bowel obstruction ·
G15 anorectal pain/fissure/fistula/abscess · G16 haemorrhoids · G17 antiemetic selection ·
G18 colorectal cancer · G19 nausea and vomiting (**C-only**) · G20 IBD (**A-only**)

MEDIUM: G21 regional-pain vs disease entry ×5 — **user: NOT folds, leave side by side** ·
G22 cholestatic liver disease · G23 chronic diarrhoea/malabsorption cluster · G24 pancreatic
collections · G25 faecal incontinence (partial — sub-block of C5 §0.6 only) · G26 IBS/functional ·
G27 hernias (**§0.30.4 hiatus hernia is a different concept — do not fold**) · G28 endoscopic/biliary
procedures

**G17 and G28 carry an unresolved AXIS question** (drug-axis, procedure-axis). User: group them,
mark the axis, decide after the Clinical Process pass.

UNGROUPED — stays put, listed for visibility: 03_GI §0.5 Liver Cancers(+.1/.2/.3), §0.7 Wilson's,
§0.8 Haemochromatosis, §0.9 Hepatitis(+.1–.4), §0.9.5 NAFLD, §0.9.6 Autoimmune hepatitis, §0.13
SBBOS, §0.15 NETs, §0.16.4 Toxic megacolon, §0.37 Ischaemic bowel, §0.39 Ileus · C1 §0.5 LUQ,
§0.8 Suprapubic, §0.10 Trauma, §0.11 Special groups · C2 §0.3 Bilious · C3 §0.7 Hepatomegaly ·
C4 §0.5 Occult bleeding · C5 §0.2 Constipation, §0.3 Acute diarrhoea · C6 §0.6 Pruritus ani ·
C7 §0.5 Intra-abdominal abscess · NEW_Drugs_12 §0.9 decontaminants · NEW_Inv §0.8 Gastrin,
§0.19/0.20 enterography · 4 administrative `Build status` / `Topics skipped` blocks

## LIMITATIONS
- Grouping is first-paragraph reading + ~25 full section reads. HIGH = "same topic", **not**
  "one is a subset of the other". No claim-level testing done; no discard verdicts implied.
- Anaphoric cross-references cannot be indexed mechanically. `Renal and Urology_merged.md:2000`
  reads *"see 0.22–0.23 of the same file"* — no filename, so no tool finds it. Hand-caught here.
