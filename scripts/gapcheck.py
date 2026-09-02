#!/usr/bin/env python3
"""The verdict path. Use this, never plain grep, for any PRESENT/ABSENT claim.

CLAUDE.md 1.3 has cited `scripts/gapcheck.py` as mandatory since 2026-08-31 and
described its behaviour in detail. **It has never existed in this repository** -
confirmed against all 33 commits: before 2026-09-01 the repo held 69 .md files,
one .csv, and no scripts at all. So every ABSENT verdict in this project's history
was made either by a per-session reconstruction from that prose, or by plain grep.
Either way, no two sessions ran the same code, and CLAUDE.md rule 11 is explicit
that reasoning about behaviour is not evidence of behaviour.

This is a reconstruction too - but it is committed, self-tested, and the same code
next time.

What CLAUDE.md requires of it, implemented here:
  * NEVER TRUNCATES. No cut/head/-m anywhere on the verdict path.
  * REFUSES TO REPORT ZERO AS A VERDICT. A zero triggers the retry automatically.
  * FOLDS DASH VARIANTS both ways - hyphen, en, em, figure dash, minus.
  * SINGLE-WORD RETRY AS A STANDING STEP, not a fallback: a multi-word pattern
    retries each meaningful word bare; a single long word retries its internal
    substrings (finds `haemarthrosis` inside `lipohaemarthrosis`, and `aemolysis`
    inside `**H**aemolysis` where markdown bolding splits the word).
  * NO PROXIMITY, NO PHRASE-ONLY VERDICTS. A pattern asserting two terms are
    adjacent is a guess about someone else's sentence structure.
  * REPORTS THE COLLISION PROFILE. A count is not evidence: `ANA` matched 2111
    times in this corpus and ~99% was `management`/`anaemia`/`Anaesthetics`.

What it CANNOT do, and you still must: spelling and naming variants, and the
concept expressed in different words. Rule 2's territory.
"""
import re, sys, glob, os, collections
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import vaultroot

DASH = '[-‐‑‒–—−]'
SKIP = {'CLAUDE.md', 'RUN_STATE.md'}
COMMON = {'the','a','an','and','or','of','in','for','to','with','on','is','are','be',
          'patient','patients','disease','syndrome','acute','chronic','management',
          'treatment','risk','use','used','not','no'}

def fold(p):
    """Make every dash variant match every other, in the pattern and in the text."""
    return re.sub(DASH, DASH, p)

def files(vault):
    return [p for p in vaultroot.md_files(vault)
            if os.path.basename(p) not in SKIP]

def search(pattern, vault):
    rx = re.compile(fold(pattern), re.I)
    hits = []
    for p in files(vault):
        for n, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
            if rx.search(l):
                hits.append((os.path.basename(p), n, l))   # FULL line. Never truncated.
    return hits

def terms(pattern):
    """Derive the retry terms, exactly as CLAUDE.md describes."""
    words = [w for w in re.findall(r"[A-Za-z]{3,}", pattern) if w.lower() not in COMMON]
    if len(words) > 1:
        return sorted(set(words), key=len, reverse=True)      # multi-word -> each word bare
    if words and len(words[0]) >= 9:                          # one long word -> its substrings
        w = words[0]
        return [w[i:] for i in range(1, 4)] + [w[:-i] for i in range(1, 4)]
    return []

def collisions(pattern, hits):
    core = re.sub(r'[^A-Za-z]', '', pattern)
    if not core or len(core) > 8:
        return None
    c = collections.Counter()
    for _, _, l in hits:
        for m in re.findall(r'[A-Za-z]*' + re.escape(core) + r'[A-Za-z]*', l, re.I):
            c[m.lower()] += 1
    return c

def run(pattern, vault):
    hits = search(pattern, vault)
    print(f'PATTERN: {pattern!r}')
    print(f'hits: {len(hits)}')
    prof = collisions(pattern, hits)
    if prof and len(prof) > 1:
        print('\n  COLLISION PROFILE - a count is not a verdict, read what it matched:')
        for w, n in prof.most_common(12):
            print(f'    {n:>5}  {w}')
    for f, n, l in hits:
        print(f'  {f}:{n}: {l}')                              # full line, always
    if hits:
        print(f'\nVERDICT: PRESENT ({len(hits)} hits). Read them before relying on the count.')
        return 0
    print('\nZERO HITS. This is NOT a verdict. Running the standing retry:')
    t = terms(pattern)
    if not t:
        print('  no retry terms derivable - narrow or rephrase the pattern by hand.')
        print('VERDICT: WITHHELD.')
        return 2
    found = False
    for w in t:
        h = search(w, vault)
        print(f'\n  retry {w!r}: {len(h)} hits')
        for f, n, l in h:
            print(f'    {f}:{n}: {l}')
        if h:
            found = True
    if found:
        print('\nVERDICT: WITHHELD - the retry found something. Read it: the concept may be '
              'present under a different spelling or wording.')
        return 2
    print('\nVERDICT: ABSENT against this pattern and its retries.')
    print('  STILL YOURS TO DO (the tool cannot derive these): spelling and naming variants, '
          'the eponym vs the plain English name, and the concept expressed in different words.')
    return 1

def selftest(vault):
    """Rule 11: known answers, including the three incidents CLAUDE.md records."""
    ok = 0; tot = 0
    def t(desc, cond):
        nonlocal ok, tot
        tot += 1; ok += bool(cond)
        print(f"  [{'ok ' if cond else 'FAIL'}] {desc}")
    t('dash folding: a hyphen pattern matches an en-dash text',
      re.search(fold('pulmonary-renal'), 'the pulmonary–renal syndrome', re.I) is not None)
    t('dash folding works in the other direction too',
      re.search(fold('warm–cold'), 'wet-dry / warm-cold', re.I) is not None)
    t('substring retry finds haemarthrosis inside lipohaemarthrosis',
      any('haemarthrosis' in x for x in terms('lipohaemarthrosis')))
    t('multi-word pattern retries each word bare',
      set(terms('Glasgow-Imrie score')) >= {'Glasgow', 'Imrie'})
    t('common words are not used as retry terms',
      'management' not in [x.lower() for x in terms('acute management protocol')])
    t('a markdown-bolded acronym expansion is reachable by substring retry',
      any(re.search(x, '**H**aemolysis, **E**levated', re.I) for x in terms('Haemolysis')))
    print(f'\n  self-test: {ok}/{tot} known answers correct')
    return tot - ok

if __name__ == '__main__':
    vault = vaultroot.root()
    if '--selftest' in sys.argv:
        sys.exit(1 if selftest(vault) else 0)
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    sys.exit(run(sys.argv[1], vault))
