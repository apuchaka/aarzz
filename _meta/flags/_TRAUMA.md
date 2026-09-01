# A6 · Trauma — analysis only. NOTHING MOVED. `M-6` NOT EXECUTED.

Requested because the ledger's four-file count was wrong. **It is five files and 23 sections**, and
the within-MSK duplication is the part that changes the shape of the problem.

## What each file holds

### MSK_merged.md — 16 sections, and it holds trauma **twice**
| Corpus A · `11_09b_Ortho_-_Trauma` | L | Corpus B · `L8_Facial__Head_and_Torso_Trauma` | L |
|---|---:|---|---:|
| `## Major Trauma — Primary Survey` +7 subsections (`<C>`, A, B, C, D, E, after the primary survey) | 1138 | `## 0.1 The Primary Survey and Trauma Principles` | 3774 |
| `## Thoracic trauma` | 1278 | `## 0.3 Chest Trauma` | 3849 |
| `## Splenic trauma` · `## Liver trauma` | 1300, 1306 | `## 0.4 Abdominal Trauma` | 3886 |
| `## Lower genitourinary tract trauma` | 1291 | — | |
| `## Head injuries` — **a pointer, not content**: *"(See [[04_Neurology]] CT Head, Head Injury, and Intracranial Pressure)"* | 1314 | — | |
| `## Ocular trauma` | 1318 | — | |
| `## Burns and Scalds` +3 subsections | 1197 | — | |
| — | | `## 0.2 Facial Trauma` | 3807 |
| — | | `## 0.5 Pelvic Trauma` | 3914 |
| — | | `## 0.6 Trauma in Special Populations` | 3942 |
Plus `NEW_Orthopaedics_and_Trauma ## Acute Joint Trauma` (L5046).

### The other four files
| File | Section | L |
|---|---|---:|
| **GI_merged** | `C1 §0.10 Abdominal Trauma` — *"blunt trauma injures solid organs by deceleration… spleen and liver are the most commonly injured"* | 1805 |
| **Neuro_merged** | `04_Neurology ### Head Injury` — *"primary injuries divided into focal or diffuse"* | 1543 |
| **Emergency** | `F0-5 §0.7 Major Head Injury` · `F0-5 §0.8 Minor Head Injury` · `A7 §0.5 Minor Traumatic Wound` | 3612, 3643, 1753 |
| **Renal and Urology** | `07 §0.19 Urethral and Bladder Trauma` · `H4 §0.6 Urological Trauma` | 703, 1578 |

## Which copies duplicate which

**1 · Primary survey — 2 copies, both in MSK.** Same topic, different emphasis, neither a subset:
- `11_09b` structures it as `<C>`ABCDE with a subsection per letter, and states *"the sequence is the
  same, but the differential within each letter is narrower"*.
- `L8 §0.1` adds three things `11_09b` does not have: **the six immediately life-threatening chest
  injuries as a named primary-survey list**, **"blood on the floor and four more"** (the five bleeding
  sites, each with its adjunct), and **tranexamic acid with the time-dependence warning**.
- `11_09b` adds the C-spine detail (manual in-line stabilisation) that `L8 §0.1` does not.

**2 · Abdominal trauma — 3 copies across 2 files.** `GI C1 §0.10` is the **fullest**: mechanism,
the unstable-patient-does-not-go-to-CT rule, the missed injuries (hollow viscus, pancreatic/duodenal,
diaphragmatic rupture, the seat-belt sign), non-operative management of solid organ injury, and a full
`**Ix:**` panel. `MSK L8 §0.4` leads on **eFAST — what it can and cannot do**. `MSK ## Splenic trauma`
and `## Liver trauma` are two short organ-specific entries.
⚠️ **This is the copy `M-6` was going to move into Emergency, which holds none of it.**

**3 · Head injury — 4 copies across 3 files, and one is already a deferral.**
`Neuro ### Head Injury` sits inside `## CT Head, Head Injury, and Intracranial Pressure` with
`### Who gets a CT head for head injury?` (which carries the live note that Australian pathways use the
**Canadian CT Head Rule**, not NICE). `Emergency F0-5 §0.7`/`§0.8` split it by severity, `§0.8` framed
entirely around *"whether imaging is required"*. **`MSK ## Head injuries` is not a duplicate — it is a
one-line pointer to Neuro, and it is the correct shape.**

**4 · Chest trauma — 2 copies, both in MSK.** `11_09b ## Thoracic trauma` leads on haemothorax and the
>1.5 L thoracotomy threshold; `L8 §0.3` leads on flail chest (*"the problem is the lung underneath,
not the paradox"*).

**5 · Urological trauma — 3 copies across 2 files.** `MSK ## Lower genitourinary tract trauma` ·
`Renal 07 §0.19` (gap-filled, *"completely absent from the source notes despite being a classic exam
topic"*) · `Renal H4 §0.6` (*"blood at the meatus means no catheter"*).

**6 · Burns — 2 copies across 2 files.** `MSK ## Burns and Scalds` +`### First aid` +`### Assessment —
depth and TBSA` +`### Mx` duplicates `Emergency A7 §0.1 Burns — Assessment`, `§0.2 Burns —
Resuscitation and Management`, `§0.3 Chemical Burns`.

**7 · Ocular trauma — 3 copies across 3 files.** `MSK ## Ocular trauma` · `Emergency A7 §0.4 Chemical
Eye Injury` and `A8 §0.4 Corneal and Ocular Foreign Body` · `Opthalm E1 §0.5 Chemical Injury, Trauma
and Foreign Bodies` and `## Corneal Abrasion`.

## The within-MSK duplication is the finding that changes the problem
`M-6` was framed as *move GI's abdominal trauma into Emergency, which has none*. That is true of
Emergency but **MSK already holds trauma twice over**, including the same abdominal content, and
**Emergency's only whole-trauma heading is `A7 §0.5 Minor Traumatic Wound`** — `FAST` appears once in
that entire file. **Executing `M-6` alone would move one of three abdominal-trauma copies into the file
that has the least trauma, leaving the two MSK copies untouched and un-marked.**

## What a single home would look like
**A `Trauma.md` file, on the same axis argument as `Procedures.md`** — trauma is a presentation
sequence that cuts across systems, not a system.

It would take: the primary survey (both MSK copies, side by side, not merged) · chest, abdominal,
pelvic, facial trauma · trauma in special populations · burns (both copies) · the trauma-specific
imaging decisions (eFAST, when the unstable patient does not go to CT).

It would **not** take: `Neuro ### Head Injury` and the CT-head rule, which is a neurological
assessment with its own decision instrument and its own Australian caveat · `Renal 07 §0.19` and
`H4 §0.6`, which are urological management · `Opthalm E1 §0.5`, which is ophthalmic ·
`Emergency A8`, which is the foreign-body source and is flagged separately as one source with eight
destinations. **Each of those keeps a pointer into the trauma file rather than moving.**

**The MSK pointer at `## Head injuries` is the model** for how every one of those deferrals should look.

## Not done
No trauma content has been moved. `M-6` is not executed. This is analysis only.
