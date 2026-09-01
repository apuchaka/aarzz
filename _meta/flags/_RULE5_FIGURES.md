---
type: analysis
scope: A7 — rule 5 pre-check
status: REPORT ONLY — nothing merged, nothing moved
---

# A7 · Rule 5 pre-check — every weight-, age- and BSA-anchored figure in the three
# topics that carry duplicate copies

**Ruling this answers:** *"Anaphylaxis, paediatric life support and paediatric DKA carry
weight-based figures. List every per-kg figure and injector band in each, with its location,
so I can check they survive before anything moves. The ASCIA table already had a live
paediatric over-dose in this corpus — that is exactly the shape. Do not merge any of the
three."*

**Nothing in this file has been merged, moved or edited.** This is the inventory to check
against after any future move.

## How this was built

`scripts`-side extraction over the 11 spans that hold the three topics, matching every line
carrying a quantity (`mg`, `mcg`, `mL`, `g`, `U`, `J`, `mmol`, `cmH2O`, `%`, a weight in
`kg`, an age in years/months, or a `/kg`, `/m²`, `/24h`, `/h` denominator) inside the span,
then read in full — no truncation, per rule 10's hard prohibition. Line numbers re-verified
against the working tree **after** the A1 moves and the A3 flag insertions, so they are
current as of commit `90dc93f`.

**Total: 11 spans · 48 figure-bearing lines.** Five of the eleven spans state **no figures at
all** and carry `UNVERIFIED` markers instead — those are listed too, because "this copy is
deliberately empty" is exactly the fact a merge can destroy silently.

---

## 1 · ANAPHYLAXIS — four copies, and they do not agree on granularity

### 1a · `Derm_merged.md` §`09_01 ## Anaphylaxis` (lines 6–37) — **the owner. 7 figures.**

This is the fullest copy and the one the other three point at.

| Line | Figure |
|---:|---|
| 18 | `> [!danger]` **IM adrenaline (ASCIA) — 1:1000, outer mid-thigh, `0.01 mg/kg` up to a maximum of `0.5 mg`** |
| 22 | **`0.1–0.15 mg` (0.1–0.15 mL)** — **`<7.5 kg` / `<6 months`** |
| 23 | **`0.15 mg` (0.15 mL)** — `7.5–20 kg` **and** `≤5 years` |
| 24 | **`0.3 mg` (0.3 mL)** — `>20 kg` **and** `≥5 years` |
| 25 | **`0.5 mg` (0.5 mL)** — `>50 kg` **and** `≥12 years` — the adult dose |
| 29 | the provenance note on the `<7.5 kg` row (below) |
| 34 | injector prescribing at discharge: `150mcg` 7.5–20kg · `300mcg` ≥20kg · `300mcg or 500mcg` from ~12y/>50kg |

> [!danger] **Line 22 is the row that was added because the corpus had a live defect.**
> Line 29 records it in the file's own words: *"the table stopped at 7.5 kg, so a reader
> following the pointer here for an infant reached a table that did not cover them."*
> It further records that the figure **sits above** what the box's own `0.01 mg/kg` rule
> would give for a `<7.5 kg` infant (`<75 mcg`), because a minimum practical volume is drawn
> rather than a strictly weight-calculated one — and that **the exact Australian figure for
> this band is unverified against ASCIA** (`PENDING_GUIDELINE_CHECKS.md` **B50**).
>
> **What this means for any move:** the `<7.5 kg` row is not redundant with the `0.01 mg/kg`
> rule above it and **cannot be derived from it**. A reconciliation that treats the per-kg
> rule as the general case and the table as its expansion will delete this row as
> inconsistent. It is inconsistent *on purpose*. It is also the only row in the corpus that
> covers an infant.

### 1b · `Pediatrics_merged.md` §`15_01b Anaphylaxis` (lines 153–188) — **3 figures, and it defers**

| Line | Figure |
|---:|---|
| 160 | `~80%` skin changes (epidemiological, not dosing) |
| 163 | `> [!info]` ASCIA verification box: `150mcg` ~7.5–20kg · `300mcg` ≥20kg · `300mcg or 500mcg` from ~12y/>50kg · **`0.01 mg/kg` to a max of `0.5 mg`** — and states *"the full ASCIA dose table (weight **and** age criteria) is set out in `[[09_01_Dermatology_-_Dermatological_Emergencies]]`"* |
| 180 | **observation `at least 4 hours` after the last adrenaline dose**; biphasic `~3–20%` within 48h — explicitly *"not the 6h/12h figures previously in this note"* |

**Note the shape:** 1b holds the weight bands but **not the `<7.5 kg` row**, and points at 1a
for the full table. It stops where the defect was. A merge that keeps 1b's bands and drops
1a's table reintroduces the exact gap that was fixed.

### 1c · `Emergency and Crit Care_merged.md` §`NEW_Drugs_01 §0.5 Adrenaline` (lines 3854–3892) — **2 figures**

| Line | Figure |
|---:|---|
| 3874 | **Ampoule (1:1000), all ages: `0.01 mL/kg` to a maximum of `0.5 mL` (`0.5 mg`) per dose, IM** |
| 3875 | Injector devices by band: `150 microgram` **7.5 kg to 20 kg** · `300 microgram` **≥20 kg** · from ~**12 years and >50 kg**, `300` or `500 microgram` |

> [!warning] **1a says `0.01 mg/kg`. 1c says `0.01 mL/kg`.** Both are correct — 1:1000 is
> 1 mg/mL, so they are the same quantity in different units — but they are **not textually
> reconcilable**, and a consistency check keyed on the string will read them as a conflict.
> They are the same figure. Do not "fix" either.
>
> 1c also carries **no `<7.5 kg` row**, and no age criteria at all — its bands are
> weight-only. That is a third granularity for one drug.

### 1d · `Emergency and Crit Care_merged.md` §`F0-1 §0.9 Anaphylaxis` (lines 2564–2598) — **0 figures**

**Deliberately figure-free.** States no dose. This is a correct copy, not an incomplete one —
it is a Corpus B section written to abstain. **A merge must not "complete" it from 1a.**

---

## 2 · PAEDIATRIC LIFE SUPPORT — three copies, one full and two abstaining

### 2a · `Pediatrics_merged.md` §`15_01a Paediatric and Newborn Life Support` (lines 3–152) — **11 figures. The owner.**

| Line | Figure |
|---:|---|
| 16 | `> [!info]` ANZCOR 12.2 verification box naming **adrenaline `10mcg/kg` (max `1mg`) IV/IO**, **amiodarone `5mg/kg` (max `300mg`) IV/IO**, **`4J/kg`** initial defibrillation — recorded as *already correct*, ILCOR-based, not UK-specific |
| 41 | Shockable: 1 shock **`4J/kg`**, resume CPR 2 min |
| 42 | **Adrenaline `10mcg/kg` IV/IO after the 2nd shock**, repeat alternate cycles (~4 min) |
| 43 | **Amiodarone `5mg/kg` IV/IO after the 3rd shock**, repeat once after the 5th |
| 45 | `> [!danger]` **live correction record** — the table previously said adrenaline after the **3rd** shock, which is **UK/ERC, not ANZCOR** (`PENDING_GUIDELINE_CHECKS.md` **B37**) |
| 73 | newborn: **5 inflation breaths**, **`20–30 cmH2O`** for **2–3 seconds** |
| 76 | then **`30–40 breaths/min`**, **`5–6 cmH2O`** PEEP |
| 105 | **EZ-IO needle by weight: `15mm` for `<39kg`, `25mm` for `>40kg`, `45mm` larger** |
| 109 | lidocaine **1% 5mL** if conscious |
| 113 | proximal tibia **1–2cm** medial and **1–2cm** distal to the tuberosity |
| 11 | the file's own header note: *"in this corpus has already produced one live paediatric dosing defect (a band stopping at 7.5 kg)"* |

> [!warning] **Line 105 has a gap between its bands: `<39kg` and `>40kg`.** A child of
> 39–40 kg falls between them. This is a needle length, not a drug dose, so the clinical
> consequence is bounded — but it is the same *shape* as the 7.5 kg defect (a band set that
> does not tile the weight axis) and it is the only other instance of that shape found in
> these eleven spans. **Flagged, not corrected** — the correct figure is not verifiable from
> a session.

### 2b · `Emergency and Crit Care_merged.md` §`F0-4 §0.4 Paediatric Resuscitation` (lines 3167–3194) — **0 dosing figures, 1 marker**

Line 3177 states the *principle* — every dose, volume and energy is weight-based; use a
**length-based resuscitation tape** or measured weight, because age-based formulae are
estimates that differ between sources — then abstains:

> `UNVERIFIED — compression-to-ventilation ratios (which differ for one versus two rescuers), compression depth as a proportion of chest diameter, defibrillation energy in J/kg, and adrenaline dosing are all omitted. Obtain from ANZCOR Guideline 12 series and the RCH resuscitation guideline.`

**This copy's value is entirely in what it refuses to state.** 2a has the numbers; 2b has the
length-based-tape instruction, which 2a does not. Neither is a subset of the other.

### 2c · `Emergency and Crit Care_merged.md` §`F0-4 §0.5 Neonatal Resuscitation` (lines 3195–3222) — **0 figures, 1 marker**

Line 3208: term newborn commences **in air**, oxygen titrated to rising saturation targets;
hypothermia an independent mortality predictor in the preterm.
`UNVERIFIED — starting oxygen concentration by gestation and the minute-by-minute saturation targets require verification against ANZCOR Guideline 13.4.`

### 2d · `Emergency and Crit Care_merged.md` §`F0-4 §0.10 Paediatric Analgesia` (lines 3351–3379) — **0 figures**

Listed for completeness: an analgesia section in a paediatric span stating no doses.

### 2e · `Emergency and Crit Care_merged.md` §`F0-3 §0.8 Paediatric Sepsis` (lines 2917–2944) — **0 figures, 1 marker**

Line 2935 states the principle — weight-based boluses **with reassessment after each for
hepatomegaly, crackles and worsening respiratory status**, because fluid overload is a real
hazard — then abstains:
`UNVERIFIED — bolus volume in mL/kg, the number of boluses before inotropes, and all antibiotic doses are omitted; use RCH guidelines and local protocol.`

---

## 3 · PAEDIATRIC DKA — two copies, and the figure-bearing one carries two live danger boxes

### 3a · `Pediatrics_merged.md` §`15_16b Diabetes Mellitus, MODY, DKA` (lines 1747–1864) — **22 figures**

**Diagnosis and background**

| Line | Figure |
|---:|---|
| 1753 | risk `5%` with one affected family member |
| 1754 | hyperglycaemia when `80–90%` of β-cells destroyed |
| 1759 | WHO: random `≥11.1 mmol/L` · fasting `≥7 mmol/L` |
| 1809 | DKA: glucose `>11`; pH `<7.3`; bicarbonate `<15 mmol/L`; ketones `>3` or urine ketones `++` |
| 1852 | resolution: pH `>7.3` + ketones `<0.6` + bicarbonate `>15 mmol/L` |

**Insulin and hypoglycaemia**

| Line | Figure |
|---:|---|
| 1770 | maintenance insulin **`0.5–0.75 U/kg/24h`** total daily dose |
| 1781 | **`10–20 g`** fast-acting glucose PO; 1 tsp sugar under the tongue every 10–12 min |
| 1782 | **`5 mL/kg` IV 10% glucose** |
| 1783 | **glucagon `1 mg` IM — `500 mcg` if `<8 years` or `<25 kg`** |
| 1825 | insulin infusion **`0.1 U/kg/h`**, started only after 1–2h of fluids, **no bolus** |

> [!warning] **Line 1777 is a `> [!warning]` box, not a figure — and it must survive.**
> It records that this entry *treats hypoglycaemia without ever defining it*, that the corpus
> holds **`<3.3 mmol/L`** for adults and **`<2.6 mmol/L`** for newborns, and that
> **neither is the figure for a child with diabetes** — *"Reading the adult number across is
> the error this box exists to prevent."* The paediatric threshold is deliberately absent
> pending `PENDING_GUIDELINE_CHECKS.md` **B55**.
>
> **A merge that fills this gap from an adjacent adult entry commits precisely the error the
> box names.** This is the highest-risk single line in the three topics.

**Fluids — the two live danger boxes**

| Line | Figure |
|---:|---|
| 1819 | resuscitation **only if shocked: `10 mL/kg` 0.9% NaCl bolus**, isotonic only |
| 1823 | K: `>5.5` none · `3.5–5.5` **`40 mmol/L`** · `<3.5` senior review |
| 1837 | **maintenance (reduced DKA rates): `<10kg` — `2 mL/kg/h` · `10–40kg` — `1 mL/kg/h` · `>40kg` — `40 mL/h` as a FIXED rate, not per kilogram** |
| 1844 | deficit from pH: `>7.1` = 5% dehydration · `<7.1` = 10% |
| 1845 | hourly rate = (48h maintenance + deficit − boluses in excess of `20 mL/kg`) ÷ 48 |
| 1846 | `40 mmol` K per `1 L` NaCl |
| 1848 | worked example: 20kg boy, deficit `100 mL/kg × 20kg = 2000 mL` |

> [!danger] **Line 1828 — an UNCORRECTED absolute figure, left in place deliberately.**
> The entry previously stated *"10% dextrose infusion at `125 mL/h`"* — an adult-sized fixed
> rate in a paediatric protocol — and it has **not** been corrected, because the right figure
> is not verified. Line 1830 gives the reasoning: `125 mL/h` is roughly maintenance for a 50kg
> adolescent and **several times maintenance for a 10kg toddler**, *"in the condition where
> fluid overload is the mechanism of the complication that kills, cerebral oedema."*
>
> **This is a rule 5 defect that is known, documented and still live.** It is exactly the
> `10kg / 50kg` test the rule prescribes, already applied and already failed. Any move of
> this content must carry lines 1828–1830 with it, unchanged.

> [!danger] **Lines 1839–1841 — a CORRECTED unit error, and the correction is the content.**
> The `>40kg` band previously read `4 mL/kg/h`, which for a 50kg adolescent gives
> **`200 mL/h` instead of `40 mL/h` — five times the correct maintenance rate**, again in
> the condition whose lethal complication is cerebral oedema.
>
> Line 1841 records **how it was caught without any source**: the three bands read
> `2 → 1 → 4` mL/kg/h as weight *increases*, inverting the normal relationship — per-kilogram
> maintenance always falls as weight rises. *"A rate that goes down, down, then up by fourfold
> is not a clinical threshold, it is a unit change: the third band is mL/hour, not
> mL/kg/hour."* Re-verified against the **SA Health Paediatric DKA guideline**
> (`PENDING_GUIDELINE_CHECKS.md` **B49**).
>
> **The reasoning is more valuable than the corrected number** and is the thing a merge is
> most likely to drop as commentary.

### 3b · `Endocrine and metabolics_merged.md` §`F0-2 §0.4 Paediatric DKA` (lines 1193–1219) — **0 figures**

Deliberately figure-free. Same status as 1d: a correct abstaining copy, not an incomplete one.

---

## Summary table — where the figures are

| Topic | Copy | Location | Figures | Status |
|---|---|---|---:|---|
| Anaphylaxis | Derm `09_01` | `Derm_merged.md:6–37` | **7** | **owner** — the only copy with the `<7.5 kg` row |
| Anaphylaxis | Paeds `15_01b` | `Pediatrics_merged.md:153–188` | 3 | bands only, defers to Derm for the table |
| Anaphylaxis | Emerg `NEW_Drugs_01 §0.5` | `Emergency…:3854–3892` | 2 | `mL/kg` not `mg/kg`; weight-only bands |
| Anaphylaxis | Emerg `F0-1 §0.9` | `Emergency…:2564–2598` | **0** | deliberately abstains |
| Life support | Paeds `15_01a` | `Pediatrics_merged.md:3–152` | **11** | **owner**; ANZCOR-verified; one live timing correction |
| Life support | Emerg `F0-4 §0.4` | `Emergency…:3167–3194` | **0** | abstains; owns the length-based-tape instruction |
| Life support | Emerg `F0-4 §0.5` | `Emergency…:3195–3222` | **0** | abstains (neonatal) |
| Life support | Emerg `F0-4 §0.10` | `Emergency…:3351–3379` | **0** | abstains (analgesia) |
| Life support | Emerg `F0-3 §0.8` | `Emergency…:2917–2944` | **0** | abstains (sepsis) |
| Paed DKA | Paeds `15_16b` | `Pediatrics_merged.md:1747–1864` | **22** | **owner**; 2 live danger boxes, 1 undefined-threshold warning |
| Paed DKA | Endo `F0-2 §0.4` | `Endocrine…:1193–1219` | **0** | deliberately abstains |

---

## The five things a merge would most plausibly destroy

Ranked by clinical weight, per rule 12's requirement to say which kind of finding this is.

1. **`Derm_merged.md:22` — the `<7.5 kg` / `<6 months` adrenaline row.** The only infant
   coverage in the corpus, added *because* a reader following a pointer reached a table that
   did not cover them. It is deliberately inconsistent with the `0.01 mg/kg` rule two lines
   above it, so any reconciliation pass deletes it as an error. **Lethal misattribution risk.**
2. **`Pediatrics_merged.md:1777` — the "hypoglycaemia is never defined here" warning.** Names
   two thresholds in the corpus and says neither applies to this patient. Filling the gap from
   an adult entry is the error. **Lethal misattribution risk.**
3. **`Pediatrics_merged.md:1828–1830` — the uncorrected `125 mL/h` dextrose rate.** Live,
   known, deliberately left with its reasoning attached. If the box travels without the
   figure, or the figure without the box, the defect becomes invisible again. **Live defect.**
4. **`Pediatrics_merged.md:1839–1841` — the `4 mL/kg/h` → `40 mL/h` unit correction.** The
   corrected number will survive a merge; the *reasoning that caught it* reads as commentary
   and will not. **Method loss.**
5. **`Pediatrics_merged.md:105` — the EZ-IO `<39kg` / `>40kg` gap.** A band set that does not
   tile the weight axis, same shape as the 7.5 kg defect. Bounded consequence (needle length),
   but it is the only other instance found. **Flagged, uncorrected.**

## Limitation of this check

The extraction is keyed on lines *containing a quantity*. It therefore cannot see a
weight-based rule stated in words with no number — *"dose by body surface area"*, *"use the
length-based tape"* — except where such a line happened to sit inside a span I read in full.
Both `F0-4 §0.4` and `F0-3 §0.8` above were caught that way and are in the table, but I
cannot claim the class is complete. Per rule 8: **clean against everything currently known to
check for.**
