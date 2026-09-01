---
type: action-item-for-the-human
status: NOT the tracker. Two rows drafted for you to paste in by hand.
---

# Rows to add to `PENDING_GUIDELINE_CHECKS.md`

> [!danger] **`PENDING_GUIDELINE_CHECKS.md` IS NOT IN THIS REPOSITORY AND NEVER HAS BEEN.**
> Verified three ways before writing this file:
> ```
> 18 .md files cite it by name
> find . -type f | grep -iE "pend|guideline|check"     →  only checklist.csv
> git log --all --pretty=format: --name-only | grep -i guideline  →  nothing, on any branch
> ```
> It lives in your Obsidian vault, unpushed. That is exactly the situation CLAUDE.md §1.13
> describes: *"a session clones `main`, so anything unpushed is invisible to it."*
>
> **I have not created it here, deliberately.** Creating a second copy would start a second ID
> sequence against a file whose whole value is a single manual append-never-delete history, and
> the next Obsidian sync would produce a merge conflict in it — *"the worst failure available,
> because taking one side silently discards either a stamp or a merge and nothing detects the
> loss."* CLAUDE.md §1.14 also forbids editing that file from a script.
>
> **So the two rows below are drafted, not filed. Paste them in by hand, in Obsidian.**

## The IDs

**Highest `B##` referenced anywhere in this repository: `B65`.** 56 distinct IDs are cited
across the corpus. **That is a floor, not the sequence maximum** — the tracker may well have
rows above B65 that no corpus file happens to cite, so **read the last row of the real file and
number from there.** The IDs below are written as `B<next>` and `B<next+1>` rather than guessed,
because a guessed ID that collides is worse than a blank one.

## The rows

Match the column layout of the real file — I cannot see it, so this is the content, not the
formatting.

---

### Row 1 — `B<next>`

**Item:** EZ-IO intraosseous needle length by weight — the bands do not cover 39–40 kg.

**Where:** `Pediatrics_merged.md:105` (`15_01a Paediatric and Newborn Life Support`, §Equipment).

**What it says now:** *"EZ-IO (reusable drill — 15mm needle for <39kg, 25mm needle for >40kg,
45mm needle for larger patients)."*

**The defect:** `<39 kg` and `>40 kg` do not meet. A child weighing 39.5 kg is in neither band
and this line gives no needle length for them. The 25 mm / 45 mm boundary is also stated only as
*"larger patients"*, with no figure at all.

**Resolve against:** the Teleflex EZ-IO directions for use (the manufacturer owns the needle-length
selection criteria), cross-checked against ANZCOR Guideline 12 series and the RCH intraosseous
access guideline.

**Weight:** low-moderate. A needle length, not a drug dose — a wrong choice risks a failed or
extravasating insertion, not an overdose. **Filed because of the class it belongs to, not its
own severity.**

---

### Row 2 — `B<next+1>` — **the class row, and the reason Row 1 is being filed at all**

**Item:** **Weight- and age-band sets that do not tile the axis they claim to cover.** Two
confirmed instances; tracked as a class.

| # | Where | The bands | The gap |
|---|---|---|---|
| 1 | `Derm_merged.md:22` — ASCIA IM adrenaline table | began at `7.5–20 kg` | **everyone under 7.5 kg had no row at all** — an infant following a pointer to this table reached nothing. Fixed 2026-08-29 by adding a `<7.5 kg / <6 months` row; **that row's figure is itself still unverified — `B50`** |
| 2 | `Pediatrics_merged.md:105` — EZ-IO needle length | `<39 kg` then `>40 kg` | **39–40 kg falls between them.** Row 1 above |

**Why it is a class and not two incidents:**

- **It is distinct from CLAUDE.md rule 5.** Rule 5 catches *an absolute figure standing alone* —
  a number that is right for an adult and survives being copied into a paediatric entry. It asks
  *"what does this do at 10 kg and at 50 kg?"* **That question passes here**, because every band
  in both sets is individually correct at the weights it names.
- **The defect is in the join, and no per-figure check inspects a join.** Every check this
  project runs examines figures one at a time. A gap between two correct figures is invisible to
  all of them — which is why instance 1 survived until a reader happened to follow a pointer for
  an infant, and instance 2 survived every sweep including the rule 5 extraction that found it
  only because that extraction printed the bands adjacent to each other.
- **It fails silently and in the dangerous direction.** A patient in the gap produces no wrong
  number to notice; they produce *no number*, in a table that still looks complete and
  self-consistent. Rule 9 already names this asymmetry for searches — *"a file missing from a
  scan looks identical to a file that came back clean"* — and this is the same asymmetry in a
  dose table.

**The mechanical test, which is cheap enough to be standing:** for any band set, read the
boundaries in order and confirm each upper limit meets the next lower limit.
`<39` then `>40` **fails**. `7.5–20` then `>20 kg` **passes**. Also confirm the set is closed at
**both** ends — instance 1 was an open bottom end, and *"larger patients"* in instance 2 is an
unquantified top end.

**Resolve against:** nothing external. **This row is a method item, not a guideline item** — it
closes when a band-tiling check exists and has been run across every dose table in the corpus,
not when a guideline is consulted. Filed here because that is where the two instances that
prompted it are already tracked.

**Weight:** the class is high. Instance 1 was a live paediatric under-dose with no coverage for
infants, in the most time-critical drug in the corpus.

---

## Already done in the corpus, so these rows are the record and not the fix

- `Derm_merged.md` — a `> [!danger]` callout now sits directly beneath the ASCIA table stating
  that the `<7.5 kg` row **deliberately exceeds** the box's own `0.01 mg/kg` rule, why (a minimum
  practical volume rather than a strictly weight-calculated one), that it is the corpus's only
  infant coverage, that **the two other copies of this table do not carry it** so a merge taking
  either as canonical loses it silently, and that its being unverified is a reason to check it
  and never a reason to delete it.
- `Pediatrics_merged.md:106` — a `> [!warning]` callout on the EZ-IO line stating the gap, naming
  it as the second instance of the class, and carrying the `UNVERIFIED` marker with its source.
