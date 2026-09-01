# Consolidated report — corpus reorganisation

**Navigable version:** https://claude.ai/code/artifact/47915732-d749-41d4-beee-6c21b2ee4e26
**Per-file detail:** `_meta/flags/<file>.md` — 20 files.
**Moves by destination:** `_meta/flags/_BY_DESTINATION.md` — 248 rows, 15 blocks.
**Rule 5 figure inventory:** `_meta/flags/_RULE5_FIGURES.md` · **Trauma:** `_meta/flags/_TRAUMA.md`
**Status: PART A EXECUTED (A1–A7). PART B untouched.** `N1`–`N8` → Psychiatry (`f5e49c9`),
`GER3`/`GER4` out of Geriatrics + four new files (`16a9386`), 80 in-text flags (`90dc93f`),
A6/A7 reports and Psychiatry groupings (`cfba800`). **No other content has moved.**

| | |
|---|---:|
| outputs written | 20 |
| moves and flags | 280 |
| groupings | 291 (214 high · 77 medium) |
| approved by user, **not yet executed** | 11 |
| cross-references repaired | 23 |
| structural findings | 4 |

## THE FOUR STRUCTURAL FINDINGS — settle these before section-level moves
1. ~~`Neuro_merged.md:3829–5452` holds `N1`–`N8`~~ **RESOLVED `f5e49c9`.** All eight sources are
   now in `Psychiatry_merged.md` (1,405 → 3,036 lines, 15 → 23 sources). Block sha256 identical
   before and after. **209 `[[N#]]` references, none broken** — wikilinks name the source file;
   45 flipped intra-file → cross-file and locator notes were added at both ends.
   **Psychiatry's section groupings are now produced** — 12 groups over 175 sections.
2. ~~`GER4` and `GER3` are not geriatrics~~ **RESOLVED `16a9386`.** `GER3` → `Preventive-Health.md`,
   `GER4` → `Safeguarding.md`. Geriatrics 1,347 → 928, remainder byte-matching. 84 `[[GER3]]`/
   `[[GER4]]` references, all still resolving.
3. **Investigation interpretation has no home.** 60+ sections across 12 files; 9 duplicate a section
   `Investigation-Interpretation.md` already has. **ECG interpretation is absent from the entire
   Clinical Process set** — its only two section-level homes in the vault are inside `Cardio_merged`.
4. **Safeguarding is a four-way split whose pieces do not overlap**, and the largest piece is in
   Geriatrics.

## DESTINATIONS RANKED BY WHAT THEY GAIN — measured, 248 move rows in 15 blocks

Full detail, with the evidence class of every row: **`_meta/flags/_BY_DESTINATION.md`**.

| Destination | Rows | of which lean on inbound counts | Note |
|---|---:|---:|---|
| `Investigation-Interpretation.md` | **59** | 1 | grows several-fold; **9 known duplicate pairs**; ECG interpretation is its first general entry |
| **No destination proposed — flag only** | **39** | 1 | 20 `X owns it` · 12 `arguable` · 7 `keep, flag` |
| `Examination.md` | **24** | 1 | + ~60 embedded blocks |
| `Examination.md` **and** `History-Taking.md` (paired) | **12** | 0 | one `Focused Hx` + one `Examination` block splitting two ways |
| Paediatrics | **11** | 2 | **all duplications, no gaps** — and the two inbound arguments point opposite ways |
| Emergency and Crit Care | **8** | 0 | 3 previously approved, 1 (`M-6`) withdrawn |
| `History-Taking.md` | **7** | 0 | sexual history from **three** files |
| **New: `Procedures.md`** | **5** | 0 | `GER8`'s real parent |
| A10 Ethics, Capacity, Consent | **4** | 0 | led by guardianship out of mental-health law |
| PH1 / AU1 population health | **4** | 0 | decided by Preventive-Health's scope |
| `Communication.md` | **3** | 0 | 2 of 3 only `arguable` |
| Psychiatry | **3** | 0 | on top of A1's eight whole sources |
| **New: `Safeguarding.md`** | **2** | 0 | `GER4` already moved; NAI and FGM would join it |
| **New: `Preventive-Health.md`** | **2** | 0 | `GER3` already moved; settles a **six-source** topic |
| **System file → system file** (19 destinations) | **65** | 7 | foreign bodies fan out by anatomy; `F0-5` returns to systems; `Cardio B6 §0.4–§0.8` |
| **New: `Palliative-and-End-of-Life-Care.md`** | **0** | — | **no move rows** — its case comes from the Clinical Process output, not a system file |

## CONFLICTS WITH ALREADY-APPROVED DECISIONS — need a ruling
- **`M-1` CSF Studies → Neuro.** Neuro already has `### CSF Interpretation`;
  `Investigation-Interpretation §1.13` also exists; ENT has CSF rhinorrhoea with β-transferrin.
  Moving it makes CSF **four-way**. **Recommend redirecting to Investigation-Interpretation.**
- **`M-2` Coombs/DAT → Heme Onc.** The fuller entry it points at should itself go to
  Investigation-Interpretation. **Recommend both land there.**
- **`M-6` Abdominal trauma → Emergency.** **MSK already holds two copies**; Neuro holds head injury;
  Emergency holds `F0-5 §0.7/§0.8`. **Recommend deciding trauma as one question across four files.**

## TWO-WAY DISAGREEMENTS — each file points at the other
urticaria/angioedema (Derm ↔ ID) · carcinoid (GI / Derm / Endocrine) ·
genetic cancer predisposition (Heme ↔ GP)

## COUNTING NOTE
The brief says 20 system files. There are **19** merged system files plus 16 Clinical Process files.
After GI there were **18** remaining, not 19.

## LIMITATIONS THAT TRAVEL WITH THIS REPORT
- HIGH confidence = "same topic", **not** "one is a subset of the other". No claim-level testing;
  **no discard verdicts implied** (CLAUDE.md rule 12 not applied).
- **Absence of inbound references is weak evidence** — only 0.9% of numeric pointers can be validated.
- **Rule 5 territory — now inventoried** in `_RULE5_FIGURES.md`: 11 spans, 48 figure-bearing
  lines, **five spans that deliberately state no figures at all**. Five items ranked as most at
  risk from a merge, led by the `<7.5 kg` adrenaline row and the undefined paediatric
  hypoglycaemia threshold. **No merge without checking these survive.**
- ~~Psychiatry's section groupings were deliberately not produced~~ **now produced** — and the
  finding is that the eight A/B pairs split along a consistent axis (A = diagnosis reference,
  B = approach to the presentation), **zero of eight being subsets**. No grouping is a merge.
- **Only 31 of 248 move rows cite inbound-reference evidence at all, and 12 lean on it.** The
  0.9%-validatable weakness is concentrated, not diffused; every one of the twelve is marked
  per row in `_BY_DESTINATION.md`.
- Clean against everything currently known to check for — not complete.
