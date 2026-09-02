---
block: Study index — the only navigation file
source: written 2026-09-02 for reading, not for building. Everything here is measured against the live corpus on that date.
---

# Study index

**You are reading a system file. You hit a marker. Should you stop?**

Almost always **no**. Four markers mean stop. Everything else is provenance —
a record of where a block came from or where it went — and you read past it.

> [!danger] **The five-second rule**
> **STOP** for `UNVERIFIED` on a **dose, rate, threshold or time window** ·
> a **`FLAG 2026-`** box · a **banded table** · a **figure with no marker at all
> in a file that carries markers elsewhere.**
> **READ PAST** `SOURCE:` dividers · `CF-PAIR` · `CO-LOCATED` · `Moved to` ·
> `[!info] Verified against …` · every `> [!note]` beginning *"Gap-filled"*.

---

# 1 The files you open while studying

Five. Nothing else at the root is for reading.

The notes are no longer 40 files at the root. They are **178 files in folders by
system**, same content, cut at the seams the merge left behind. The folder is the
old file; the number is reading order inside it.

```
Cardio/   13    OBGYN/    12    MSK/      12    Endo/     12
Emergency/11    Paeds/    10    HemeOnc/  10    GI/       10
Psych/     9    Neuro/     9    ID/        9    Ophth/     7
Derm/      7    Resp/      6    Renal/     6    ENT/       6
Geri/      3    GP/        1    Anaes/     1
Clinical/ 18    Examination (5), History-Taking, Communication, Procedures,
                Investigation-Interpretation, the GER6 drug-class crosswalk,
                and eight merged-away stubs
Practice/  6    Ethics, Population Health, Preventive Health, Safeguarding,
                Australian Health Context, EBM
```

| File | What it is | When to open it | What you do with it |
|---|---|---|---|
| **the study files**, in the folders above — `Cardio/Cardio_01_…`, `Neuro/Neuro_01_…` and the rest | the notes. **178 files, 67,526 lines.** Not one line of content changed in the split; every line of the old 40 is in exactly one of these, in the same order | always | read a folder top to bottom, in file-number order |
| **`checklist.csv`** | 872 topics, 24 categories, each rated High / Medium / Low yield (308 / 394 / 170). Read it with `encoding='utf-8-sig'` or the first column header breaks | when choosing what to read next, and to record what you have read | the `Studied? (Y/N)` and `Confidence (1-3)` columns are **blank for all 872 rows** — it is a topic list you have not yet used as a tracker |
| **`MY_TASKS.md`** | 71 lines. Every known clinical defect, contradiction and boundary problem, one line each: file, line, what is wrong, what to change | when a marker makes you stop, and once before each exam | check whether the thing in front of you is already on it. If it is, the line tells you what is wrong without you re-deriving it |
| **`PENDING_GUIDELINE_CHECKS.md`** | 65 rows, **64 still open**, IDs B1–B67 | when you hit a figure you intend to rely on | search the file, line or drug. A row means the figure is known to need a source check |
| **`CLAUDE.md` §1.7 and §1.12** | the marker definitions, if you want them first-hand | rarely — section 3 below is the short version | — |

**`KNOWN_ABSENCES.md` does not exist.** It is named in the working briefs as a
destination for topics found to be genuinely missing, and no round ever needed
it. Nothing points at it. Do not go looking.

**`MASTER_VERIFICATION_WORKFLOW.md` does not exist at the root either**, though
`CLAUDE.md` and `PENDING_GUIDELINE_CHECKS.md` both cite it. It is a build
document. Its absence costs you nothing.

---

# 2 The ignore list

**Everything below records how the corpus was built. None of it is study.**
Reading it is what cost you three days. It is written to be exhaustive so that
a future you, at 11pm, wondering whether there is context in `_meta/`, can see
the answer here and not open a single one of them.

## The whole of `_meta/` — 48 files, none of them for reading

```
_meta/RUN_STATE.md                      what each session did, in order. 1,078 lines.
_meta/PENDING_ROWS_TO_ADD.md            rows drafted for the tracker, not yet added by hand
_meta/flags/_INVENTORY.md               an index of duplicated topics
_meta/flags/_CONSOLIDATED.md            the same, consolidated
_meta/flags/_BY_DESTINATION.md          the same, sorted by destination file
_meta/flags/_PAIRED_BLOCKS.md           which blocks were placed side by side
_meta/flags/_RULE5_FIGURES.md           an audit of paediatric figures, by span
_meta/flags/_TRAUMA.md                  a trauma-content audit
_meta/flags/_Clinical_Process_set.md    a ruling about four files
_meta/flags/THE_161.md                  161 flagged items, with dispositions
_meta/split_manifest.json               which output file each line range became
_meta/split_baseline/<18 files>.body    the pre-split text of each file that was cut,
                                        kept so the split can be re-verified byte for byte
_meta/flags/<19 system files>.md        per-file move proposals: Anaes, Cardio, Derm,
                                        ENT, Emergency, Endocrine, GI, GP, Geriatrics,
                                        Heme Onc, Infectious Disease, MSK, Neuro,
                                        OBGYN, Opthalm, Pediatrics, Psychiatry,
                                        Renal and Urology, Resp
```

Every one of those is a **decision record about moving text between files**. The
decisions were executed. The files are the receipt. There is no clinical content
in any of them that is not already in a system file, and the flag files' line
numbers went stale the moment the moves happened.

## The build documents

```
CLAUDE.md                   the rules the sessions worked under. Not study, except
                            §1.7 and §1.12 if you want the marker definitions first-hand.
scripts/                    20 Python checkers. They verify the corpus; they teach nothing.
```

## Inside the system files themselves

These *look* like content and are not. Read past every one:

```
the SOURCE divider comment          422 of them. Provenance.
*Moved here from … Verbatim.*       the line under a divider. Provenance.
> [!note] **Moved to <destination>**  114 tombstones. A signpost, not a gap.
> [!info] **CO-LOCATED …**          26 notices. Means: the second account is
                                    directly below. Keep reading.
`CF-PAIR` …                         133. Means: another account exists. Named, not merged.
> [!note] Gap-filled from CSV …     234. Says why an entry was written. Not clinical.
"Build status" / "Topics skipped"   36 remain. Tier counts. Skip.
```

**If a paragraph is about the corpus rather than about a patient, it is not
study.** That single test disposes of all of the above.

---

# 3 The markers, and what to do mid-read

## Read past — no action

| Marker | What it tells you | What you do |
|---|---|---|
| **the `SOURCE:` divider comment** (an HTML comment naming the origin file) | a new source block starts here, and **its section numbers restart at 0.1** | note which block you are in, only if you meet a bare `§0.x` — see section 4 |
| **tombstones** — a `> [!note]` beginning **"Moved to"** and naming a destination file | this section's content is now in file X, verbatim, with a divider naming this file. 114 of them | if you want that content, open X. Otherwise keep reading. **Nothing was lost** |
| **`CF-PAIR`** | a second full account of this topic exists, named on the marker. Deliberately not merged. 133 of them | read the one in front of you. Open the other only if the figures matter and you want to compare |
| **`CO-LOCATED`** | the second account is **directly below**, intact | keep reading. You will meet it in a moment |
| **`[!info] Verified against <source>, Aug 2026`** | somebody checked this against a named Australian source. 189 boxes | **read past — but see the warning below** |
| **`> [!note] Gap-filled from CSV …`** | 234 of them. Says why an entry was written to fill a checklist row | not clinical. Skip |

> [!warning] **A verification box does not tell you what it did NOT cover.**
> `CLAUDE.md` §1.9 requires every verification box to carry a **`NOT checked:`**
> line naming what falls outside it. **There are zero such lines in the notes.**
> 189 boxes, none scoped. So "Verified against ANZCOR" means *some* of what is
> under that box was checked, and you cannot tell which. This has already
> produced one live defect — a verification box endorsing a drug-timing table
> that had since been corrected underneath it.

## Stop and check

| Marker | What it tells you | What you do |
|---|---|---|
| **`UNVERIFIED — <what to check>, per <source>`** | 919 of them. The marker names both the thing and the source that would settle it | **If it is on a dose, rate, threshold or time window: do not commit it to memory.** If it names a login-only source — Therapeutic Guidelines, AMH, AIDH, eviQ — it will never be resolved; look it up at the point of use, which is correct practice anyway. Everything else: read the claim, distrust the number |
| **`> [!warning] FLAG 2026-…`** | 79 of them. A known structural problem at that spot — usually the same topic in several files, sometimes with the safety rule in only one of them | read the flag. It names the other places. If it says a safety rule lives elsewhere, go and read that one |
| **a banded table** — severity grades, weight bands, staging | not a marker; a shape. See section 4 | check the boundaries meet before you use it |
| **a figure with no marker at all** | in a file that carries markers elsewhere, silence is not endorsement | see section 4, first paragraph |

## Markers you will never meet

`CLAUDE.md` defines these. **Every one has zero instances in the 40 files you
read.** Do not go looking for them and do not treat their absence as meaningful:

```
CONFLICT CF-###          0 in the notes  (defined in CLAUDE.md §1.12; the corpus
                                          uses CF-PAIR and FLAG instead)
NO-BASELINE              0
TODO:link                0
### Added from unverified layer   0
`SRC:` tokens            0
`→MED:` mirrors          0
`[paed]` / `[adult]`     0
[!check] callouts        0   (verification uses [!info] Verified against …)
NOT checked: lines       0   (see the warning above — this is the one that matters)
```

---

# 4 Four things about this corpus that would bite you

**Most of it is unverified, and the absence of a marker is not evidence.**
919 `UNVERIFIED` markers sit across 102 of the 178 files; 76 carry none at
all, and that means nobody checked those files, not that they are clean. The
markers were added by people reading for particular defects, so they cluster
where somebody happened to look. The sharpest case: an ASCIA adrenaline table
carried a marker on one wrong band while **two other bands in the same table
were also wrong and unmarked**. Treat a figure as unverified by default and let
the marker tell you what is *specifically* known to be wrong, not what is
specifically fine.

**A bare `§0.x` reference is ambiguous.** Every system file is several source
files concatenated under `SOURCE:` dividers, and **each block restarts its
numbering at 0.1**. **The split made this much better and did not cure it.** Measured the same way
either side: **1,809 repeated section numbers across 24 files before, 396 across
39 files after** — down 78%, because most files now hold fewer blocks. A pointer
that says `see 0.20` still means 0.20 *of the block it is written in*, which is
not the 0.20 you will find by searching. If a reference names a file or a block
prefix — `` `C4 §0.2` ``, `` `03_Gastrointestinal §0.31` `` — trust it. If it is
bare, scroll up to the nearest `SOURCE:` divider first and count from there.

**Banded tables fail in four distinct ways here, and three of them look fine.**
*Gaps* — 39–40 kg has no needle size. *Overlaps* — a potassium of 3.0 is both
mild and moderate. *Point boundaries* — `<3 months` beside `>3 months` leaves a
child of exactly 3 months with no antibiotic regimen, and the arithmetic gap is
zero, so nothing flags it. *Two-axis coupling* — the ASCIA rows require a weight
**and** an age, so a 20 kg six-year-old matches no row at all. Twelve were found
by reading; seven more appeared the moment the checker could see overlaps and
point boundaries. All are listed in `MY_TASKS.md`. **Before you rely on
any banded table, read the boundaries against each other, not down the column.**

**Searching this corpus is not like searching a textbook.** Acronym expansions
are bolded letter by letter — the text is `**H**aemolysis`, so searching
`Haemolysis` returns nothing; search a run from the middle of the word instead.
Dashes come in five characters and digits in unicode variants (`×10⁹`), so a
pattern that looks right can match nothing. Topics live under headings that do
not use the name you would search: a pulled elbow sat under `### Pulled elbow`
while searches for `nursemaid` and `pronation` both came back clean. And **a high
hit count means nothing** — `ANA` returns 2,111 hits of which about 30 are the
antibody; the rest are *management*, *anaemia*, *anaesthetics*. If you searched
and found nothing, search the plain English name of the thing before believing
it is absent.

---

# 5 The size of what is outstanding

Counts and where they live. Not the items.

**`MY_TASKS.md` — 71 lines.** Every citation in it was retargeted to the split
files on 2026-09-02 — 112 of them, across 62 rows — and **what that verification
covers is this: each one points at a line byte-identical to the line it cited
before the split.** They were resolved by matching the text, never by shifting
the number, so none can have drifted onto whatever now sits at an arithmetically
adjusted line. Nineteen rows were then read by hand against the content they
describe; eighteen land on it exactly.

**What it does not cover:** whether the original citation was well-aimed in the
first place. One is not — **row 45** cites the melanoma metastatic-disease line
where it describes the Breslow survival table, which sits about eight lines
below. That was true before the split and was carried across unchanged, because
the retarget was allowed to alter only the file name and the number.

Five rows (1-5) cite a block deleted at commit `2495aba` and still point into git
history, which is immutable and correct as written:

```
20   banded-table boundary defects — gaps, overlaps, point boundaries, two-axis
28   clinical errors and pairs of accounts that disagree
 6   build-time judgement calls to confirm or overrule
 5   cross-file partners located, neither account declaring the other
 3   ordering decisions still open
 2   ordering decisions you have already declined
 2   large duplication sets, reported as sets not pair by pair
 3   questions asked and answered — a finding, no action needed
 1   corpus-wide: 189 verification boxes, none carrying a NOT checked: line
 1   findability: a 28 KB reference file nothing in the corpus points at
```

**`PENDING_GUIDELINE_CHECKS.md` — 65 rows, 64 open**, IDs B1–B67. Each names a
figure or guideline needing a source check. A meaningful share can never be
closed: they cite Therapeutic Guidelines, AMH, AIDH or eviQ, which require an
institutional login. Those stay open permanently and that is correct — the
marker is an instruction to look it up at the point of use.

**In the notes themselves:**

```
   919  UNVERIFIED markers, across 32 of 40 files
    79  FLAG 2026- boxes, across 22 files
   133  CF-PAIR declarations
   189  verification boxes — none carrying a NOT checked: line
   114  tombstones and 26 CO-LOCATED notices (navigation, not gaps)
```

**Reference integrity, as it stands:**

```
     7  numeric section pointers aiming at a section that does not exist
        (6 into A10, 1 into B2)
    36  wikilinks resolving to nothing, across 9 targets — P1, P3, P4, P6,
        COM1, Medications_Reference, Shock_Phenotypes, 13_ENT, 15_Paeds.
        Those targets have no file and no source block anywhere; the adjacent
        prose names the topic, so nothing is unreachable, only unclickable
    57  bare internal pointers that do not resolve in their own block
        (48 resolve in a different block of the same file, 9 nowhere)
     2  references whose stated title disagrees with the section number
    32  CF-PAIR markers naming an account that is in a different file
```

**The last three used to read 0, and the 0 was an artefact.** Those two checkers
selected files by the name `*_merged.md`, so they never looked at Communication,
Procedures, History-Taking, Investigation-Interpretation, A10, PH1, EBM1,
Preventive-Health or Safeguarding — which is where all of them live. Re-run over
the whole corpus, the pre-split tree scores **76, 2 and 36** on the same three
lines, so the split improved every one of them. None is a reason to stop reading:
each is a pointer you may have to resolve by scrolling rather than by clicking.

**`checklist.csv` — 872 topics**, 308 High yield, 394 Medium, 170 Low.
`Studied?` and `Confidence` are blank for all 872.

That is the whole of what is known to be outstanding. It is 71 lines in one
file and 64 rows in another. You are not carrying anything else.
