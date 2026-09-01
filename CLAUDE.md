# 1 Project Rules — Grind Time Intern Exam Notes

## 1.1 What this project is
Intern-level medical exam notes for Australian AMC-standard exams (MCQ 27 Sept 2026, OSCE 1 Nov, second MCQ 8 Nov). 148 content .md files, checklist.csv (872-row master topic checklist, 24 categories), and MASTER_VERIFICATION_WORKFLOW.md (the 26-step method and work queue).

Read MASTER_VERIFICATION_WORKFLOW.md before any work. Read checklist.csv with `encoding='utf-8-sig'` — plain utf-8 breaks the first column header.

## 1.2 Target standard
Intern/RMO level. The test for any content: would a newly-graduated intern need this to recognise, explain, or act on something clinically? Not subspecialist depth. The workflow document's "Target standard" section has the full definition — follow it.

## 1.3 Non-negotiable working rules

1. **Verify before writing any cross-reference.** Check the target file's exact header text first. Never write a plausible-sounding section name and assume it exists.

2. **Zero grep hits is not proof of absence.** Check case-sensitivity, Unicode characters (α, β, ₂ subscripts), hyphenation variants, **markdown emphasis inside a word**, and alternate medical terminology before concluding content is missing. Historically most "missing" results have been search artifacts.
   - **The markdown case specifically:** this corpus bolds acronym expansions letter by letter — `**H**aemolysis, **E**levated **L**iver enzymes, **L**ow **P**latelets`. A search for `Haemolysis` finds nothing, because the literal text is `**H**aemolysis`. **Whenever a search for an acronym expansion returns zero hits, search again for a distinctive letter-run from the middle of the word** (`aemolysis`) before concluding the expansion is absent. The construction most likely to be searched for is the one least likely to be found.
   - Also never conclude absence from **truncated** output: a hit that was returned and cut off by a `cut`/`head` limit looks identical to no hit at all. View the full line.
   - **DASH VARIANTS ARE FOLDED BY `gapcheck.py`, the way digit folding works** — hyphen,
     en-dash, em-dash, figure dash and minus all match each other, in both directions, in
     the pattern and in the text. Added 2026-08-31 after **three en-dash false-ABSENTs in
     one run** made it a class rather than an incident: `warm-cold` (0 hits, the block was
     written `wet–dry / warm–cold`), `pulmonary-renal` (**0 hits, and the syndrome is
     PRESENT TWICE** as `pulmonary–renal` in two same-day-referral callouts), and one in
     the week 2 merge verification. **The trap is removed mechanically rather than
     remembered** — an invisible character variant is exactly the failure a person cannot
     be asked to notice.
   - **THE SINGLE-WORD RETRY IS A STANDING STEP, NOT A FALLBACK — and `gapcheck.py` RUNS
     IT FOR YOU.** Promoted 2026-08-31 after the rarer-word retry caught a duplicate for
     the **third** time: **Glasgow-Imrie** (C7 — the retry on `Glasgow` found the Glasgow
     score with its PANCREAS mnemonic), **West Haven** (C3 — the complete four-grade scale
     sat under a heading reading only `Grading`), and **`lipohaemarthrosis`** (L1 — 0 hits,
     and the retry on `haemarthrosis` found *"fat globules suggest an intra-articular
     fracture"* already stated at `NEW_Investigations_Rheumatology:173`).
     **In all three the original search looked clean.** That is why "retry when something
     looks suspicious" is not a rule: a clean-looking zero is exactly the case it exists
     for. **Every ABSENT verdict gets the retry before it counts.**
     `gapcheck.py` now derives the terms and runs them itself on any zero result, printing
     every hit in full — a multi-word pattern retries each meaningful word bare, and a
     single long word retries its internal substrings, which covers `haemarthrosis` inside
     `lipohaemarthrosis` and `aemolysis` inside `**H**aemolysis` by the same mechanism.
     **What the tool cannot derive, and you still do by hand: spelling and naming variants,
     and the concept expressed in different words.**
   - **SEARCH THE PLAIN ENGLISH NAME OF THE TOPIC, NOT ONLY THE EPONYM, THE ACRONYM OR
     THE MECHANISM.** The eponym clause above says: when the *name* of a named instrument
     returns nothing, search its components. **This is the converse, and it is not implied
     by it** — when you search an alternate name, a mechanism word or an acronym, you must
     still search **what the corpus would plainly call the thing.**
     - Found 2026-08-31 auditing the week-3 merge. **A pulled elbow block was merged and
       marked `NO-BASELINE` while `Corpus A/11_02:149` already carried a section headed
       `### Pulled elbow`.** The gap check had run `nursemaid` (0 hits) and `pronation`
       (3 hits, all adult fracture mechanisms) — **an American eponym and a mechanism word,
       neither of which the existing section uses.** Both searches were correctly built,
       correctly scoped and correctly read. **Neither searched the two words in the heading.**
     - **This is the failure mode rules 9 and 10 cannot see.** The pattern was right for
       what it asked, the scope was right, the count was right, the reading was complete.
       The *question* was wrong. A search for a name the corpus does not use returns an
       honest zero about a topic the corpus covers under another heading.
     - Three further instances in the same audit: `allopurinol hypersensitivity` was called
       absent while **three** files carried it, one of them the destination file itself, at
       a line saying *"not repeated here"*; the RA *treat-to-target* principle was reported
       absent while sitting **34 lines above the merge point**; `weight stigma` likewise.
     - **The cheap form of this check: before merging a block, grep the destination file for
       the words in your own block's TITLE.** It costs one command and it is the only
       search guaranteed to be phrased the way a reader would phrase it.

   - **Rule 9 is this rule's inverse** — it covers the search that finds the *wrong* thing
     rather than nothing, and the file silently skipped before any search ran. A zero
     result can mean the term was absent, the spelling differed (this rule), or the file
     was never examined (rule 9).

3. **Every automated scan produces false positives.** Verify each hit manually against actual file content before treating it as a gap. Report dismissed artifacts alongside confirmed gaps — the ratio is the main signal of whether the run was careful.

4. **Scans also produce false negatives.** A template-completeness scan keyed on the presence of an S/Smx line cannot detect entries that lack one entirely. Build scans defensively and assume blind spots exist. If you find one, fix the scan and re-run affected items before continuing.

5. **In any paediatric entry, treat every absolute quantity as suspect.** Confirmed four times (2026-08-29): DKA maintenance fluid, DKA dextrose rate, paediatric nephrotic proteinuria, and the adrenaline band that stopped at 7.5kg. For any `g`, `mg`, `mL`, `mL/h` or `g/24h` figure in a paediatric file, **ask what it does at 10kg and at 50kg.** The correct paediatric forms are per-kg, per-m², per-age-band, or per-kg with an absolute cap — the corpus does this well where it does it at all (`40mg/kg (≤2g)`, `60mg/m²/day (max 80mg)`, the ASCIA and ANZCOR bands). **The defect is always an absolute figure standing alone**, because a number that is right for an adult survives being copied — nothing about it looks wrong in isolation. This applies to every round, not only paediatric ones: adult files carry paediatric content too.

6. **One fix at a time, one commit each.** After each fix: confirm no duplicate headers introduced, confirm all cross-references resolve. Commit with a descriptive message before moving on. Never batch unverified edits.

7. **Stop and report if you discover a limitation in your own method mid-run.** Do not continue applying a scan you've realised is flawed. This is more important than completing the phase.

8. **Report honestly.** "Clean against everything currently known to check for" — never "verified complete." This project's history is that every completeness claim was later disproven by a new technique.

9. **Substring matches create both false hits and silent false skips.** `child` matches
   `Child-Pugh`; `ALL` matches the English word "all" under a case-insensitive search;
   `paed` matches ortho**paed**ics; `ASCIA` matches f**ascia**; `epinephrine` matches
   nor**epinephrine**. **Rule 2 covers searches that find nothing; this covers searches
   that find the wrong thing** — and skip logic that excludes files with no error at all.
   Anchor on word boundaries or full paths.
   - **The two failure directions are not equally visible.** A false hit lands in a report
     and gets dismissed. A false skip produces nothing, and **a file missing from a scan
     looks identical to a file that came back clean.** Never write skip logic on a
     substring.
   - **Not every unanchored match is a defect.** `child`, `infant`, `gestation` and
     `pubert` fire inside *children*, *infants*, *gestational* and *puberty* — the same
     concept, and anchoring them would break them. The test is whether the longer word is
     a **different** concept.
   - **A COMPONENT pattern that is too generic makes a real gap read as FILLED.** This is
     the inverse of the eponym check and is equally silent. That check says: before
     concluding a named instrument is absent, search its *components* rather than its name.
     But a component must be **specific to the instrument**, or it matches everything.
     - Found 2026-08-31 on D4. `normal CK` was used as the component pattern for
       *steroid myopathy has a normal CK*. It matched **9 files**, of which the relevant
       one was **polymyalgia rheumatica** at `12_02` — *"↑ESR (>40). Normal CK and EMG"* —
       a different condition entirely. The gap was real and the pattern reported it filled.
       Two more the same day: `over-interpret` matched a urine-dipstick warning and CRP/ESR
       kinetics, not spinal imaging; `tibialis posterior` matched **Achilles rupture and
       the Thompson test**, not the foot-drop inversion discriminator.
     - **The direction of failure matters.** A too-narrow component pattern produces a
       false ABSENT, which the eponym check then catches. A too-generic one produces a
       false PRESENT, which **nothing catches** — the item is silently dropped from the
       merge and no report ever mentions it. Prefer a distinctive phrase from the
       instrument itself (`metabolic atrophy`, `imaging must match the clinical level`)
       over a common clinical word pair, and **read every component hit before trusting
       it**.
   - Found three times in one week (2026-08-30). Treat it as a class: when one turns up,
     audit every containment test and unanchored alternative in the same tool, against the
     real corpus rather than by eye. That audit found two further instances nobody had
     noticed — `ASCIA` inside `fascia` on 33 lines, mis-routing verification items into
     the actionable queue, and `epinephrine` inside `norepinephrine`.

   - **A HIGH HIT COUNT IS THE LEAST RELIABLE SIGNAL IN THIS CORPUS, and a collision list
     will always be behind the corpus.** Eight new instances in a single run (2026-08-31,
     week 2 merge), **none of them on the known-collisions list that run started from**:

     | Pattern | Hits | What it actually matched | Real |
     |---|---:|---|---:|
     | `felon` | 62 | **`li`FELON`g`** — every hit, in prophylaxis-duration prose | **0** |
     | `Conn` | 123 | `connective` ×39, `connects` ×22, `connected` ×18 | **0** |
     | `Gell` | 9 | `Shi`GELL`a`, `Salmon`ELL`a`, `fla`GELL`in` | **0** |
     | `LADA` | 6 | `ma`LADA`ptive` ×5, `ma`LADA`ptation` | **0** |
     | `IGRA` | 125 | `m`IGRA`ine` ×57, `m`IGRA`tion` ×13, `m`IGRA`ns` ×8 | 7 |
     | `PrEP` | 113 | PREP`aration(s)` ×68, `pre`PUCE ×3 | ~15 |
     | `TRAb` | 32 | TRAB`ecular` ×11, `s`TRAB`ismus` ×11 | 4 |
     | `IRIS` | 22 | the eye | 4 |
     | `orf` | 7 | Peterd`ORF`, n`ORF`loxacin, burgd`ORF`eri | **0** |
     | `PPPD` | 3 | **pylorus-preserving pancreaticoduodenectomy**, not the dizziness syndrome | **0** |
     | `HLH` | 3 | **hypoplastic left heart**, not haemophagocytic lymphohistiocytosis | **0** |
     | `RED-S` | 1 | `Red-stained nappy` | **0** |
     | **`ANA`** | **2111** | `management` ×465, `anaemia` ×316, `Anaemia` ×168, `Anaesthetics` ×162, `Management` ×128, `analgesia` ×124 | **~30** |

     - **`ANA` at 2111 hits is the ceiling case, and it settles the question: if 2111 can
       be ~99% noise, NO HIT COUNT IS EVIDENCE OF ANYTHING.** Not four figures, not three,
       not two. The count tells you how common the letters are, not whether the concept is
       in the corpus. Read the matches or do not use the number.

     - **`PPPD` and `HLH` are the more dangerous shape than pure noise.** Each is a *real*
       medical acronym that already means **something else** in this corpus — pylorus-preserving
       pancreaticoduodenectomy and hypoplastic left heart. Noise like `orf` looks like noise on
       sight; **a hit that is itself a legitimate clinical term reads as a genuine find**, and is
       dismissed only by reading the sentence around it.
     - **`IGRA` at 125 hits with 7 real is WORSE than a zero result, because nobody
       scrutinises 125.** A zero triggers rule 2's component re-search by reflex and, in
       `gapcheck.py`, by refusal to issue a verdict. A three-figure count reads as
       overwhelming coverage and is waved through. **The failure is invisible in exact
       proportion to how confident the number looks.**
     - `felon`, `Conn`, `Gell` and `LADA` each returned a non-zero count for a term
       **completely absent from the corpus**. Four false PRESENTs in one run — the
       direction rule 9 already flags as the one nothing downstream catches.
     - **So: do not maintain a list of known-bad patterns and check against it. KNOWING A
       TERM COLLIDES DOES NOT HELP IF THE CHECK IS NOT RE-RUN EACH TIME.** `PERC` **was
       already on the collision list** for that run and still returned **253 hits**
       (`hypercalcaemia` ×73, `percentage` ×23, `hypercholesterolaemia` ×17,
       `percussion` ×16); `HIT` returned 206. **The list does not stop the count being
       produced, and the count is what gets read.** A list tells you a pattern is bad
       *once*; the check has to establish it *every time*, because the next reader is a
       different session with a different working memory. The list
       was five entries long at the start of that run and eight instances were found that
       it did not contain. **Treat any pattern under about six characters as suspect by
       default**, and settle it the cheap way — pipe the hits through
       `grep -oiE "[a-z]*PATTERN[a-z]*" | sort | uniq -c` and read what the matches
       actually are, before reading any of them as a verdict.

10. **A search that excludes its own destination cannot detect the duplicate it is about
   to create.** Distinct from rules 2 and 9: there the *pattern* was wrong — a spelling
   missed, a substring over-matched. Here **the pattern is correct and the scope is
   wrong**, so the search returns a clean, confident, useless answer.
   - Found 2026-08-31. A gap check ran `grep … "Corpus A" | grep -v "14_05a"` before
     merging three signs of self-induced vomiting into `14_05a`. **Two of the three were
     already in that file, 36 lines above the insertion point** — *"recurrent vomiting may
     lead to erosion of teeth and calluses on the knuckles (Russell's sign)"*. The
     exclusion was deliberate and reasonable-seeming: the question being asked was "does
     this exist *elsewhere*". The question that mattered was "does this exist **at all**".
   - **The gap search must always include the destination file**, and must run against
     **every corpus**, not the one the destination happens to live in. Four further
     duplicates that day came from a check that searched Corpus A alone while the content
     sat in Corpus C.
   - **The same rule applies to auditing a merge.** An audit run against the *current*
     tree finds the merge's own additions and reports everything present. **Audit against
     the tree the merge started from.**
   - **A multi-hit grep must be read to the LAST hit before any `ABSENT` verdict, and a
     hit count is not a verdict.** This is a third failure direction, and rules 9 and 10
     do not cover it: there the *pattern* was wrong, or the *scope* was wrong. **Here the
     pattern was right, the scope was right, the count was right, and the reading stopped
     early.**
     - Found 2026-08-31 merging B1. `grep shear` returned **14 hits**. The first was
       *diffuse axonal injury* in `04_Neurology`, obviously unrelated, and on that basis
       the claim was called absent. **`01_Cardiovascular` §0.36.5 already carried it** —
       *"(rate control first, then vasodilator if BP remains high, to avoid reflex
       tachycardia worsening shear stress)"* — the identical claim, identically reasoned,
       further down the same result set. The same run also called *oxygen only if
       hypoxaemic* absent while §0.1.2 said `O2 if sats <94%`, which is rule 2's spelling
       clause in its most ordinary form.
     - **Everything a scan can report was correct.** Nothing in the tool's output was
       wrong and no better pattern existed. **A reader who stops at the first hit produces
       exactly the same conclusion as a scan that found nothing**, and the two are
       indistinguishable in any report.
     - **So: `n` hits means `n` lines to read.** Where a result set is genuinely too large
       to read, that is a signal the pattern needs narrowing — **not** licence to sample
       it. Quote the hit that settled the question, so the reading is visible in the
       report and not merely asserted.

   - **HARD PROHIBITION — no `cut`, `head`, `-m`, `fold`, or any column or line limit on a
     grep whose output feeds an `ABSENT` verdict.** Not a caution. Not "prefer to avoid".
     **If the output is too long to read, narrow the pattern — never truncate the result.**
     - Rule 2 has prohibited concluding absence from truncated output since the beginning,
       and it was **violated twice in a single block** (B3 and B4, 2026-08-31) by someone
       who had just written the clause above. A prohibition that is only stated gets
       violated; this one is phrased so that the *command being typed* is the violation,
       which is checkable while typing it rather than afterwards.
     - **B3:** `cut -c1-150` ended a line **four words before** `because of atrial
       stunning`. **B4:** `cut -c1-160` ended a line at `tongue-biting (lat`, cutting
       `(lateral suggests seizure)` — **on a line already quoted in the same session for a
       different claim.**
     - **The two clauses guard different axes.** The one above governs *which* hits are
       read; this governs *how much of each*. **Reading every hit at `cut -c1-150` is still
       reading none of them properly**, and satisfying either says nothing about the other.
     - Truncation is fine for **previewing** a result set, for counting, and for anything
       that is not a verdict. `scripts/gapcheck.py` exists so the verdict path has a tool
       that cannot truncate.

   - **ADJACENCY — never require two terms to be near each other. Search the rarer term
     alone.** A pattern like `situational syncope`, `micturition syncope`, or
     `X.{0,40}Y` asserts that the corpus places the two words together. It frequently does
     not.
     - Found 2026-08-31 on B4. Situational syncope was called absent on
       `situational syncope|micturition syncope|cough syncope` — **every alternative
       required the word *syncope* adjacent.** The corpus writes
       *"situational (micturition, defaecation, cough, swallow)"* under a heading. Searching
       **`micturition` alone returned it immediately.**
     - This is the Step 29 word-order check, and it is now a rule: **pick the term that is
       rarest in general English, search it bare, and read the hits.** A proximity operator
       is a guess about someone else's sentence structure.

   - **PARAPHRASE — a failed phrase search must be retried on its least-common single word
     before `ABSENT`.** The corpus rewords. A phrase is the author's; the concept is not.
     - Found 2026-08-31 on B4. *Hypotension is relative to the patient's own baseline* was
       called absent on `own baseline|relative hypotension|usual blood pressure`. The corpus
       writes *"a blood pressure low **for that patient**"* and then gives a worked example.
       **A paraphrase is not a pattern.**
     - The retry is mechanical: take the phrase, drop every word that is common in medical
       prose, and search what remains — bare, unanchored, untruncated.

   - **RULE 2 IS THE BACKSTOP WHEN 9 AND 10 BOTH PASS.** This is the reason to keep running
     it even when the search looks clean.
     - Of six `ABSENT` verdicts overturned at placement across B3 and B4, **rule 10's
       clauses would have passed four of them**: the scope was right, the corpus was right,
       the pattern was right, the count was right. They failed on truncation, adjacency and
       paraphrase — all three of which are **rule 2's territory: the search that finds
       nothing because the corpus said it differently.**
     - **Rule 2's component re-search caught all four.** So: run it on *every* zero result,
       including — especially — the ones where the pattern looks obviously correct.

11. **A claim about tool behaviour is TESTED, never reasoned.** Run it, print the output,
   quote the output. Reading the source and explaining what it must do is not evidence, and
   this project has now been wrong twice in one day doing exactly that.
   - **Both explanations were confident, plausible, and false.** Asked why one `→MED:`
     marker registered in the dose-mirror report and another did not, I read the regexes and
     answered from them: the first "registered because the filename in its wikilink contains
     digits", the second "failed because its line carried no digit". A four-line script
     settled it:
     ```
     GTN                    MED match: ['GTN']      DOSE match: []
     sodium nitroprusside   MED match: []           DOSE match: []
     ```
     **Neither explanation survived.** `RE_DOSE` requires a *unit*, so no filename ever
     matched it; the report simply listed every parsed mirror regardless of figures. And the
     second failed because the drug pattern `[A-Za-z0-9_\-]+` **excludes spaces**, so no
     multi-word drug name ever matched — nothing to do with digits.
   - **The second was a live defect, and only running it could have found it.** Every
     multi-word drug — `sodium nitroprusside`, `magnesium sulfate`, `calcium gluconate`,
     `tranexamic acid` — was **silently dropped** by the mirror machinery. No match, no
     entry, no error: the voided-marker shape. It was found the only way it can be, **by
     writing one and noticing the report did not change.**
   - **Reasoning about code shares the defect of the code.** The same misreading that puts a
     bug in a regex puts it in the explanation of that regex, so an explanation derived from
     the source cannot detect a bug in the source. Only execution is independent of it.
   - **This applies to every claim about the tooling**: what a scan counts, why a marker did
     or did not register, what a lint rule catches, whether a skip fired. If it is going into
     a commit message, a report, or a PR body — **run it first and paste what it printed.**
   - **VERIFYING YOUR OWN WORK USES `gapcheck.py`, NOT PLAIN GREP. A check that can produce a
     false negative is not a check.** The gap search and the verification search are the same
     search pointed in opposite directions, and both fail the same way.
     - Found 2026-08-31, verifying the 16-PR merge to `main`. A hand-written `grep -F` pass
       over the 29 headline additions reported **four MISSING**. Three were bad patterns of
       mine — unescaped `**`, a literal `(`, an em-dash I had transcribed wrong. **The
       fourth was real rule 2**: the block is titled `**modified** Valsalva`, with the bold
       markers *inside* the phrase, so `grep -F "modified Valsalva"` cannot match it. The
       content was present at lines 619–628 the whole time.
     - **Re-run through `gapcheck.py`, all 29 came back PRESENT.** Nothing had been lost in
       nine rebases. **The verification had a 14% false-negative rate and the merge had a 0%
       loss rate.**
     - **This is the more dangerous direction than it looks.** A false ABSENT during a *gap
       check* costs a duplicate. A false MISSING during a *merge verification* says content
       was destroyed — which invites a "restore" that re-adds a block already present, or a
       revert of a good merge. **The remedy is the same tool, because it cannot truncate,
       refuses proximity and phrase patterns, and never reports zero as a verdict.**
     - So: **any claim that content is present or absent goes through `gapcheck.py`** —
       including, and especially, when the thing being checked is your own merge.

   - **A CHECK THAT CANNOT FAIL IS WORSE THAN NO CHECK, BECAUSE IT REPORTS CLEAN.** No
     check at all leaves a known hole. A broken one closes the hole in the report while
     leaving it open in the work, and every run it survives adds a false assurance to the
     record.
     - Found 2026-08-31, mid-run, after eleven merges had each ended with this
       duplicate-header check:
       ```
       grep -n "^#\+ " FILE | awk -F: '{print $3}' | sort | uniq -d     # VACUOUS
       ```
       `grep -n` prefixes the line number, so `$1` is the number, `$2` is the header text
       **up to its first colon**, and `$3` is whatever follows a second one. **For a
       colon-free header `$3` is empty**, so every such header collapses to the empty
       string, `uniq -d` prints one blank line, and the blank reads as "no duplicates".
     - **The two-line proof, which is what makes this stick:**
       ```
       $ printf '10:## Alpha\n20:## Alpha\n' | awk -F: '{print $3}' | sort | uniq -d | cat -A
       $
       ```
       **Two identical headers. One empty line.** The check could not detect the error it
       existed to detect, and had never been able to.
     - It surfaced only by accident: `01_Cardiovascular` has `## 0.8 Bradycardia:
       Peri-arrest` and `## 0.9 Tachycardia: Peri-arrest` — two *different* headers sharing
       a colon-suffix — so on the twelfth file the broken check finally emitted a visible
       false positive. **Without that coincidence it would still be running.** The correct
       form is `grep -h "^#\+ " FILE | sort | uniq -d`; re-run, all eleven files were clean.
     - **The generalisation: run every check once against a case whose answer you already
       know, before trusting it on a case whose answer you do not.** A check is a claim
       about tool behaviour, so the rest of rule 11 applies to it — construct the failure
       it is supposed to catch, confirm it catches it, and paste what it printed.
     - Three defects of this family surfaced in that one run: this, a `NO-BASELINE`
       baseline test whose scope wrongly included **Corpus B, the merge source** (fixed by
       restricting to `Corpus A` + `Corpus C`), and a merge-verification pattern that
       returned a false MISSING because the block was written with **en-dashes** and the
       pattern used a hyphen. **Loss rate 0%; verification false-negative rate 1 in 27.**
       Each was found only by running the check where the answer was already known.

   - **AN AUDIT SCOPED BY COMMIT-MESSAGE TEXT IS SCOPED BY WHAT A SESSION CHOSE TO
     WRITE, NOT BY WHAT HAPPENED. Scope by what the commit DID.** Third check in this
     project unable to find the thing it existed to find.
     - Found 2026-09-01 at the fourteen-file gate. An audit for `UNVERIFIED` markers
       destroyed by a supersede ran `git log -i --grep="supersede"` and reported
       **seven**. That grep matches **66 of 93** section-merge commits — a commit
       supersedes a fragment or it does not, and whether its *message* says so is a
       drafting choice. Re-scoped to `--grep="^Section merge"` and then to *every
       commit whose diff removes lines*, the real number was **ten**, and the four
       extra included a **login-required Therapeutic Guidelines marker** (§1.14: never
       delete one) and an **R1 tranexamic-acid dose-and-window marker** whose
       replacement block carried no marker at all.
     - **The seven were reported as complete.** That is the damage: not the miss itself
       but a completeness claim built on a scope nobody had checked.
     - **The test for any audit's scope: could a commit that did the thing fail to
       match?** `--grep` over prose always can. Select on the diff — files touched,
       lines removed, a token appearing or disappearing — because that is the record of
       what happened rather than of what was said about it.
     - Same family as the vacuous duplicate-header check and the `Stemmer`-at-1.0
       duplicate scorer: **the check ran, reported a number, and the number was a
       property of the check rather than of the corpus.**

12. **A DISCARD VERDICT MUST BE MADE AT CLAIM LEVEL. Naming a destination file or
   section is not evidence that the destination carries the content.** Rules 2, 9 and 10
   all govern the search that *looks for* something. This governs the verdict that decides
   **not to look any further**, and it is the only verdict in this project that leaves no
   artefact behind.
   - **THE COROLLARY IS WHY THIS RULE IS EXPENSIVE ON PURPOSE: A WRONG DISCARD IS
     UNDETECTABLE DOWNSTREAM.** A wrong *merge* produces a duplicate, carrying a `SRC:`
     token, which a later gap check finds — the four caught on 2026-08-31 were all found
     that way. A wrong *discard* produces **nothing**: no marker, no block, no diff, no
     entry in any report. It is therefore the more expensive error and warrants the more
     expensive check. Nothing else in this method has that property.
   - **Two failure depths, both found by hand in one file (C6) in one morning. Neither was
     a search error — both searches were correct, and the verdicts were made at the wrong
     granularity.**
     - **AREA-LEVEL (the achalasia shape).** C6 §0.3 "oesophageal disease" was discarded to
       `13_06b` and §0.30 because **those files own the area**. They do. **The topic is not
       in them:** achalasia appears twice in `13_06b`, both times as **one word in a list** —
       no definition, no failure of the lower oesophageal sphincter to relax, no bird's beak,
       no manometry, no management. **A file owning an area is not evidence it carries a
       topic.**
     - **CLAIM-LEVEL (the dyspepsia shape).** C6 §0.1 was discarded to §0.28 GORD and §0.29
       gastritis. **Both exist and are good.** B's section still carried at least six claims
       absent from both — among them the **inferior-MI cardiac exclusion**, with the point
       that relief from an antacid or from GTN **does not distinguish** the two. **A topic
       being present is not evidence that its claims are.**
   - **So the test is: extract every distinct clinical claim from the discarded section and
     test each one separately.** A section on dyspepsia is not one claim — it is a mechanism
     claim, a red-flag list, a drug-cause list, an investigation set and a management
     approach, each separately present or absent. Test the **named destination first**, then
     the whole vault before concluding, because content sitting elsewhere is a *reachability*
     problem and not the same finding.
   - **Classify, never collapse:** `CONFIRMED` · `DISPLACED` (present, but not where the
     table said) · `AREA-LEVEL` · `CLAIM-GAPS` (list every missing claim) · `WRONG` (absent
     from the vault entirely).
   - **When a claim is missing, the claim merges — the section does not.** One missing claim
     is not licence to re-merge a section that was correctly discarded in the rest.
   - **Weight the finding.** A missed red flag, a lethal misattribution and a management step
     are not the same as a footnote. Say which it is.

## 1.4 Reporting format
For each queue item: what was checked · scan hits produced · genuine gaps vs dismissed artifacts (with reasons) · fixes made with commit hashes · any limitation noticed in the method itself.

## 1.5 Content builds (Phase 2 of the queue) work differently
One topic per unit of work, not one category. Require a cited Australian source per topic (RACGP, Therapeutic Guidelines, state health guidelines, relevant college). Depth should match the existing notes, not be uniformly shallow.

---

## 1.6 Corpus merge — scope of the added material

Rules 1.1–1.5 above are unchanged and take precedence. **Rule numbering in §1.3 is
load-bearing** — Corpus C files cite "CLAUDE.md rule 8" by number. Never renumber them.

The project now holds three corpora, not one:

| Corpus | Files | Frontmatter `trust:` | What it is |
|---|---|---|---|
| **A** | ~148 | `inherited` | The original notes. Plausible, in use, never systematically checked. |
| **B** | 37 | `unverified` | Built from model knowledge. Every figure marked or omitted. |
| **C** | 53 | `snippet` | AMH/guideline-derived via snippets. **Inconsistent on figures — see below.** |

`verified` is reserved for content checked against a named Australian source, with its scope
recorded (§1.9).

> [!danger] **Corpus C is NOT reliably figure-free. Never assume it.**
> This table previously read "States no doses or reference ranges", generalised from five
> sample files. **It is wrong.** Checking all 22 Corpus C drug files, **8 state a dose or
> a dose-adjacent quantity** — among them the full ASCIA adrenaline table in
> `NEW_Drugs_01` (`0.01 mL/kg`, max `0.5 mg`, injector bands from **7.5 kg**),
> `hydrocortisone 100 mg IV` in `NEW_Drugs_10`, loperamide maxima, anti-D `500 IU`,
> pyridoxine thresholds, Hb transfusion triggers and vancomycin `AUC/MIC 400–600 mg·h/L`.
>
> **Most of C abstains; some of it does not.** `figures: none` is therefore a **per-file
> finding, established by reading that file** — never a corpus-wide assumption, and never
> inferred from C's provenance. Only 3 of the 22 drug files currently carry the key.
>
> **Where a C file states a dose, the fix is the `NEW_Drugs_10` pattern, not deletion:**
> ```
> > - **SURGERY:** hydrocortisone 100 mg IV at induction, then 200 mg per 24 hours…
> >   - **THESE TWO FIGURES ARE ADULT DOSES. DO NOT USE THEM IN A CHILD.** Paediatric
> >     cover is dosed by body weight or body surface area, not as a fixed adult quantity.
> ```
> That is rule 5 in its correct form, and it is the model for every dose already sitting
> in C.

**Corpus A is `inherited`, not `verified`.** Step 17's re-run found seven UK leftovers in
files an earlier sweep had already flagged, and `co-amoxiclav` still sits in
`03_Gastrointestinal` appendicectomy prophylaxis. Labelling A as verified would make that
content indistinguishable from checked content, which is the failure this whole exercise
exists to prevent.

Also set per file: `population: adult | paed | mixed`, `figures: none` where the file states
no numbers, and the script-maintained `conflicts_open` / `conflicts_r1` counters.

---

## 1.7 Inline markers

Backtick-delimited so they survive editing, work inside table cells, and grep cleanly:

```
`UNVERIFIED — what needs checking, and the source that would settle it.`
`VERIFIED <source> <YYYY-MM> — what was checked.`
`CF-032`                  conflict reference (a real one — `CF-012` is only ever an example)
`[paed]` `[adult]`        population scope
`→MED:adrenaline`         mirrors a figure owned elsewhere
`TODO:link — topic`       stripped placeholder link
`SRC:C1_Acute_Abdomen §0.6`  origin of an additive-merge block (§1.10)
```

Write a marker only where the claim differs from the file's frontmatter default.

**Every `UNVERIFIED` marker must name the source that would settle it.**
`` `UNVERIFIED — the dose.` `` cannot be triaged; `` `UNVERIFIED — dose, per ANZCOR 12.2.` ``
can be actioned immediately. Unsourced markers accumulate into a triage backlog.

---

## 1.8 Login-required sources — permanently noted, never queued

**Therapeutic Guidelines, AMH, AIDH and eviQ require an institutional login and will not be
consulted by anyone — agent or human.** Items only those sources could settle are
**permanently noted**. The marker stays in the file as a standing instruction to look it up
at the point of use, which is correct behaviour for dosing regardless.

Never delete a login-required marker. Never resolve one from memory, from a non-Australian
source, or on the grounds that two corpora agree.

**Open Australian sources remain usable and should be named:** ANZCOR, ASCIA, RCH,
Queensland Children's Health, NSW ACI, SA Health, the Australian Immunisation Handbook and
NIP schedule, PBS, TGA, RACGP, RANZCOG, Kidney Health Australia, APEG, CDNA, NBA, AIHW.

**No guideline is fetched from a web session** — those run network-proxied. Wanting to look
something up is a stop, not a search.

Step 11 (AU dosing and product names) and Step 17 (UK-localisation) already govern the
Australian-context sweeps. These rules do not replace them.

---

## 1.9 Verification scope — the `NOT checked:` line

Step 14 tracks whether a guideline is *current*. This tracks whether a verification box
covered *everything beneath it* — a different failure, and one this project has hit twice:
`15_01a`'s ANZCOR box confirmed the doses while the adrenaline timing beneath it was UK/ERC
and wrong, and `PENDING_GUIDELINE_CHECKS.md` **B65** is a box claiming paediatric validity
above absolute adult figures.

```markdown
> [!check] VERIFIED — ANZCOR Guideline 12.2, Aug 2026
> **Checked:** adrenaline dose, amiodarone dose, defibrillation energy.
> **NOT checked:** drug timing relative to shock number, sequencing, 4Hs/4Ts wording.
```

**`NOT checked:` is mandatory.** "nil" is permitted only when true. A box without it is a
lint failure. Rule 8 applies here directly: report honestly, never "verified complete".

---

## 1.10 Merge rules

**Supersession is on provenance, never on content.** Judging which claim is more clinically
accurate requires a source that cannot be reached from a session.

| A's claim | B's claim | Action |
|---|---|---|
| `verified` | `unverified` | A wins, B discarded |
| `inherited` | `unverified` | `CONFLICT` block, both retained |
| absent | present | additive merge, keeps `unverified` label |
| figures differ | figures | `CONFLICT`, never auto-resolved |

**Corpus B can never win automatically** — it carries no sources. Where B proves right, a
guideline established it, not B.

**Two corpora agreeing is not corroboration.** They share ancestry. A model asked about
appendicectomy prophylaxis would likely reproduce A's `co-amoxiclav + metronidazole` and
agree perfectly. Concordance never closes an item.

**BEFORE MERGING A SECTION, GREP THE DESTINATION FOR ITS `SRC:` TOKEN.**

```
grep -n "SRC:<bfile> §<section>" <destination>
```

**This is the one search in this project that cannot fail.** Every other check in §1.3 exists
because a search can miss — wrong spelling, wrong scope, wrong alphabet, a name the corpus does
not use. The `SRC:` token is **exact, machine-written and unique**, so a zero means zero.
Use it in preference to any content search when the question is "has part of this section
already been merged here".

**Measured 2026-08-31: 138 of the 970 sections in Corpus B and B-new already hold a merged
fragment — 14%.** 58 B files are affected. **7 sections have fragments in more than one
destination**, and those are the awkward ones: one section, two fragments, two places.

**WHERE A FRAGMENT EXISTS, THE SECTION SUPERSEDES IT — AND INHERITS ITS CROSS-REFERENCES.**

The fragment's clinical claims are reproduced by the section merge. **Its connective tissue is
not, because the connective tissue was written by the merge and exists nowhere in Corpus B.**
Ten blocks were sampled against their own B source sections: **zero were pure subsets, and
five of ten were assembly** — built from two B files, or from B plus destination content, or
narrowed deliberately with a scope note.

What must be carried across, not discarded:

| Merge-authored element | Worked example |
|---|---|
| internal `§x.y.z` cross-references | C1 §0.6's block **replaced B's Alvarado sentence** with a pointer to `§0.41.3` |
| `[[file]]` pointers placing a claim against existing content | *"the anatomy is already tabulated in [[11_07a_Ortho_-_Dermatomes_and_Myotomes]]"* |
| delta-framing against destination content | *"the **acute** precipitants **SMITH** does not cover"* — SMITH is Corpus A's mnemonic, absent from B3 |
| verbatim quotation of another file | `01_Cardiovascular:48` quotes `NEW_Drugs_06` then says *"what that entry does not give is **how you know**"* |
| ownership assignment | *"[[04_Neurology]] and the rhabdomyolysis entries own those"* |
| a deliberate scope note | the ATSI block: *"deliberately narrow — what an intern does, not the history, the policy or the epidemiology"*, then a map of where the rest lives |

**Delete the fragment's prose; keep its pointers, re-aimed at the merged section.** A section
merged without them is content a reader cannot reach from where they are, which is the
reachability failure §1.3 rule 12 already names.

**The two worked examples of correct placement**, for the case where the destination already
covers part of what is being merged:
- `03_Gastrointestinal` §0.33.4 — *"**AIMS65** is a further pre-endoscopy risk score alongside
  the Glasgow-Blatchford and Rockall scores **already at §0.33.2**."*
- `01_Cardiovascular:48` — quotes the owning entry, then states only the delta.

Both name what they add, point at what exists, and reproduce nothing. **Reach for that shape
wherever the overlap is obvious, rather than defaulting to duplication.**

**Additive merge format** — under a marked subheading, never woven into existing prose,
which produces unreviewable diffs and blurs provenance at every sentence boundary. **Every
block carries a `SRC:` token naming the origin file and section**, so `grep -rn "SRC:C1_" .`
reconstructs everything that B file contributed and where each piece landed:

```markdown
### Added from unverified layer — <topic>
`SRC:C1_Acute_Abdomen §0.6` `UNVERIFIED — model knowledge, not source-checked.`
```

**The destination table for each B file is committed to `_meta/merges/<bfile>.md`** — every
section, its destination, and its disposition **including discarded ones**. Supersession
otherwise leaves no trace at all: a superseded section simply never appears, so a wrong
supersede is invisible and nothing can audit it. The discard rows are the point.

**Before creating any file, grep the whole vault.** Corpus A is not purely
disease-organised — it holds investigation, history and examination files, and
presentation-type sections inside disease files (`03_Gastrointestinal` §0.41 is "Abdominal
Pain — Regional Anatomy and DDx"). A duplicate file is the one error nothing downstream
detects. Rule 2 applies: zero grep hits is not proof of absence.

**Corpus B's wikilinks are FILENAME PREFIXES, not placeholder codes. Do not strip them —
expand them.** This said "167 wikilinks point at placeholder codes that resolve to nothing".
Measured across all 39 files: **798 wikilinks, 764 unresolved**, and the characterisation was
wrong as well as the number. `[[C4]]` is `C4_Gastrointestinal_Bleeding`, `[[GER1]]` is
`GER1_Comprehensive_Geriatric_Assessment`, `[[A9]]` is `A9_Transfusion__Coagulopathy…`.
**They dangle only because the prefix is not the full filename.**

**The mapping is not a pure prefix match** — `[[F0.2]]` uses a dot where the filename uses a
hyphen (`F0-2_Acid-Base__DKA_and_Fluid_States`). Build it by measurement: normalise `.`→`-`,
require the code to be followed by `_`, and require **exactly one** matching file. Report any
prefix that does not resolve to exactly one.

| | n | Rule |
|---|---|---|
| **Expandable** | **573** | Expand to the full filename. Verified: 87 distinct codes, **0 ambiguous**. This is not guessing — the mapping is deterministic against the filesystem. |
| **Unbuilt targets** | **191** (50 codes) *as measured against `Corpus B/` alone* | `E1`, `H4`, `J4`, `L3`, `L4`, `M5`, `N6`, `O6` … codes B's scheme reserved. Used identically in prose (`Acute angle-closure glaucoma → [[E1]]`, `Myeloma → [[J4]]`), so the adjacent text names the topic. These became `` `TODO:link — topic (unbuilt)` ``. **THE `(unbuilt)` HALF OF THAT LABEL IS NOW FALSE FOR ALL OF THEM — see below.** |

> [!danger] **`Corpus B-new/` BUILT EVERY ONE OF THEM. Re-measured 2026-09-01, during the D3 merge.**
> `Corpus B-new/` holds **112 files**, not the 39 of `Corpus B/`. Counting every `TODO:link` marker still sitting in either directory, and asking the filesystem whether a file with that prefix now exists:
>
> ```
> distinct TODO:link codes still in B/B-new: 47   total markers: 188
> codes that NOW have a file: 47   markers pointing at them: 188
> still genuinely unbuilt: []
> ```
>
> **47 of 47. 188 of 188. Zero genuinely unbuilt.** `L4` → `L4_Back_and_Neck_Pain.md` (×9), `N6` → `N6_Functional__Dissociative_and_Personality_Disorders.md` (×9), `O6` → `O6_Sexual_and_Reproductive_Health.md` (×11), `GER3` → `GER3_Preventive_and_Occupational_Health.md` (×14). Only `P1` and `P3` from the list above have no file — and **no marker references either**, so they cost nothing.
>
> **This is the fifth sampled-not-counted figure in this project**, after "C states no doses", "65 backticked references", "42 wikilinks in C" and "167 placeholder links". It has the same cause every time: the number was correct for the corpus it was measured against and was then quoted as a fact about the project. `Corpus B-new/` did not exist when 191/50 was counted.
>
> **What to do with a `(unbuilt)` marker you meet in a merged block:** the *topic* is not unbuilt, so do not repeat the claim. Point at the **Corpus A owner** if one exists — `L4` → `[[11_06_Ortho_-_Spinal_Orthopaedics]]`, `N6` → `[[14_05c_Psych_-_Unexplained_Symptoms__Somatoform__Dissociative__Factitious_Disorders_]]`. Where Corpus A owns nothing, leave the marker but **drop the word `(unbuilt)`**: the B-new file is in this run's own queue and the pointer becomes writable once it merges. Never guess a target — that part of the original rule stands.

**This is the fourth sampled count, and they share one cause.** "Corpus C states no doses"
(8 of 22 drug files do), "65 backticked references" (276), "42 wikilinks in C" (195), and
"167 placeholder links in B" (798/764) were each generalised from the same five-file sample
rather than counted. **Nobody ran the count.** Before quoting any corpus-wide figure in this
project, measure it — the habit, not the individual numbers, is the defect.

---

## 1.11 Content ownership

| Content | Owner |
|---|---|
| Dose, route, frequency, maximum | the file where it already lives — recorded in `_meta/OWNERS.md` |
| Drug mechanism, adverse effects, monitoring, class traps | `NEW_Drugs_NN_*.md` |
| Therapeutic-class pharmacology | `Medications_Reference.md` |
| Which drug in this disease, and why | condition file |
| Which test in this disease, and why | condition file, inline `(*why:*; *what:*)` |
| What a test is and how to read it | `NEW_Investigations_*.md` |
| Reference intervals | nobody — deliberately absent |

**Dual naming is correct and must never be rewritten.** `furosemide (frusemide)`,
`adrenaline (epinephrine)`, `lidocaine (lignocaine)` — Australian name leading, superseded
or international name in brackets. Corpus C does this deliberately, so a reader who learnt
the old name can find the entry. If the AU term already appears on the line, the line is
already correct; rewriting it produces `furosemide (furosemide)`.

**A rename map is a list of substance identities, not spellings.** `DRUG_NAMING` carried
`amphetamine sulfate → dexamfetamine` — **two different substances** — until the
source-per-entry audit of 2026-08-30 removed it. **The digit check cannot catch this**: no
digit moves when a substance name is swapped, so the dose survives intact attached to the
wrong drug. Every entry names a source; an entry without one is not applied.

**`Medications_Reference.md` is not the dose owner.** Its own scope note forbids the role
("Nothing was moved here"), it holds two entries, and it states no doses. Do not relocate
dosing into it — that would break cross-references it was designed to preserve.

**Owner tables must record the range they cover.** B50 is the case where two files pointed at
an ASCIA adrenaline table that stopped at 7.5 kg, so a reader following the pointer for an
infant reached a table that did not cover them. A pointer to an incomplete owner is worse
than a local figure, because nothing signals the failure.

**Do not add NEW doses or reference ranges to Corpus C, and do not backfill its empty
`Normal:`/`Abnormal:` fields.** The only available filling material is model knowledge.

**But do not treat C as figure-free** (§1.6): 8 of its 22 drug files already state doses,
so "C states no doses" must never be used as a premise — not to skip a check, not to grant
`figures: none`, and not to assume a C dose came from somewhere else. Existing figures are
**scoped in place using the `NEW_Drugs_10` pattern**, never deleted.

Step 12 already covers same-fact-in-3+-files consistency. `→MED:` mirrors exist to make that
check mechanical, not to replace it.

---

## 1.12 Conflicts

Weight by risk. **R1** — dose, route, frequency, resuscitation timing, weight-based
paediatric figures, anything legal or notifiable — expanded `> [!fail]` block above the
claim. **R2** — thresholds and scores driving disposition — collapsed `> [!fail]-`.
**R3** — inline `` `CF-###` `` only.

```markdown
> [!fail]- CONFLICT CF-012 — imaging pathway **R2**   ← EXAMPLE ID. No file has ever contained a `CF-012`; the real appendicitis-imaging conflict is `CF-032`.
> **A (`inherited`):** <claim>
> **B (`unverified`):** <claim>
> **Why it matters:** <clinical consequence>
> **Resolve against:** <named open AU sources>
```

Both claims stay in the text. **Never adjudicate** — resolution is done by the human during
study, when the clinical context is already loaded. IDs are `CF-###`, sequential, never
reused, kept distinct from the tracker's `B##` sequence.

**No agent edits a `CONFLICT` block or a resolution stamp.** Those are written by hand in
Obsidian, and a session editing them causes exactly the silent loss described in §1.13.

---

## 1.13 Obsidian and git both write these files

Resolution stamps are made by hand in Obsidian during study. Sessions edit on branches.
**Two independent sync systems over one folder, neither aware of the other.** A merge
conflict in clinical markdown is the worst failure available, because taking one side
silently discards either a stamp or a merge and nothing detects the loss.

- Pull `main` into Obsidian **before** every study session.
- Push Obsidian edits **before** starting a session — a session clones `main`, so anything
  unpushed is invisible to it.
- Never leave a PR open on files being revised from.
- Resolve any conflict on a computer, never on a phone, and check the `NOT checked:` lines
  survived.

**One step = one session = one branch = one PR.** Web sessions can only push to their own
working branch, and session context does not carry over — `_meta/RUN_STATE.md` and the Queue
markers are the only memory.

---

## 1.14 Never

- Resolve a clinical conflict, or mark anything `verified`, without a named Australian source.
- Treat agreement between two corpora as corroboration.
- Write a `[!check]` without a `NOT checked:` line.
- Add a figure to a file declaring `figures: none`.
- Delete a login-required marker, or resolve one from a non-AU source.
- Edit `PENDING_GUIDELINE_CHECKS.md` from a script — it has a manual ID sequence and an
  append-never-delete history.
- Create a file without grepping the whole vault first.
- Delete a Corpus B file before every section is merged or explicitly rejected in a commit
  message — **and, even then, not until its block is complete and the intra-B links have
  been retargeted.** "Fully merged" is not sufficient on its own: other, still-unmerged B
  files link to it, and deleting on the merged test alone dangles every one of those
  links. C1, C2 and C3 passed the merged test on 2026-08-31 and were deliberately kept.
- Renumber §1.3's rules, or renumber file sections, or repair Corpus B's placeholder links.
- Claim a phase is "complete" in the sense of verified. Rule 8: "clean against everything
  currently known to check for."

