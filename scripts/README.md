# `scripts/` — the checks, with their known-answer tests

**Committed 2026-09-01. Before this, no tool in this project was committed at all** — the
whole toolchain lived in a session scratchpad that is destroyed when the session ends, so every
defect found in a run was fixed only inside that run and the next session started from nothing.
`gapcheck.py`, which CLAUDE.md §1.3 cites throughout as mandatory for any `ABSENT` verdict, **is
still not in this repository.**

## Run everything

```sh
scripts/checkall.sh
```

Self-tests run first. **A check that cannot fail is worse than no check, because it reports
clean** — CLAUDE.md rule 11 — so each tool constructs the defect it exists to catch and proves
it catches it before being trusted on the corpus.

## What each one is, and the incident behind it

| Tool | Guards against | The incident |
|---|---|---|
| `check_dividers.py` | a `SOURCE:` divider that only *looks* like the convention | The Investigation-Interpretation merge wrote `SOURCE: file.md  (moved from X, date)`. `dangling.py` parses `SOURCE: (.*?) =====` and took the whole string as the filename, registering every moved section under a key nothing points at. **60 pointers reported broken; none was.** |
| `verify_move.py` | a false MISSING after a move | The first verifier stopped at the next heading *of any level*, so any section with subheadings compared unequal. **4 mismatches reported out of 104; loss rate 0%.** Rule 11 names this as the dangerous direction: a false MISSING invites a "restore" that re-adds content already present. |
| `reanchor.py` | executing a row from a stale line number or filename | Line numbers landed on a heading in **97%** of a 219-row sample at `73aebe0` and **16%** at HEAD. Section names in the flag rows are paraphrases, so exact text matching fails too. Filenames go stale as well — A1 moved `N1`–`N8` out of Neuro. |
| `dangling.py` | a numeric pointer at a section that does not exist | Found the 23 off-by-one pointers into `01_Cardiovascular`. |
| `misaimed.py` | a pointer whose number exists but names a different section | `dangling.py` called 7 of these clean. **35% error rate among the 21 checkable pointers.** |
| `drift.py` | section-numbering drift per source | Its output is compared before/after every move; it has been byte-identical across all of them. |
| `xref.py` | inbound-reference counting | v1 counted wikilinks only and missed backticked-filename references; it also missed `[[F0.2]]`, where prose uses a dot and the filename a hyphen. |

## The one rule that is not automated

**No tool enforces that a flag row's line number is re-checked before execution.** `reanchor.py`
makes it cheap; nothing makes it mandatory. The staleness banner at the top of every file in
`_meta/flags/` is the only thing standing between a future session and executing from a number
that is wrong 84% of the time.
