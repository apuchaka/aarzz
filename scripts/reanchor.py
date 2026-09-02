#!/usr/bin/env python3
"""Re-anchor a flag row on heading TEXT, because its recorded line number is stale.

WHY THIS EXISTS. Measured on a 219-row sample: the line numbers recorded in the
flag files landed on a heading in 97% of rows at 73aebe0 (the last commit before
any content moved), and in 16% at HEAD. The 80 in-text flags (90dc93f) alone took
it from 212/219 to 53/219 - insertions are far more destructive than moves,
because an insertion near the top shifts everything below it.

They will keep degrading with every executed block, so NEVER execute a row from
its recorded line number.

Two things make an exact text match fail as well, so this matches on tokens:
  - the section names in the flag rows are PARAPHRASES, not verbatim headings
    ("0.1 Thyroid Panel (TSH, fT4, fT3, antibodies)" against an actual
     "0.1 Thyroid Panel (TSH, Free T4, Free T3, Thyroid Antibodies)")
  - filenames go stale too: A1 moved N1-N8 out of Neuro, so a row naming Neuro
    now sends you to a file that does not hold the content.

Prints every candidate with its score. READ THEM. A score is not a verdict -
CLAUDE.md rule 9: a high hit count is the least reliable signal in this corpus.

Usage:  reanchor.py "## 0.1 Thyroid Panel (TSH, fT4, fT3, antibodies)"
"""
import re, sys, glob, os
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import vaultroot

STOP = {'and','the','of','a','in','for','to','its','with','on'}
SKIP = {'CLAUDE.md','RUN_STATE.md','PENDING_GUIDELINE_CHECKS.md'}

def toks(t):
    t = re.sub(r'[*`]', '', t)
    t = re.sub(r'^#{1,6}\s*', '', t)
    t = t.replace('–', '-').replace('—', '-')
    return set(w for w in re.findall(r'[a-z0-9]+', t.lower()) if w not in STOP and len(w) > 2)

def num(t):
    m = re.match(r'^#{1,6}\s+([0-9]+\.[0-9.]*[0-9])\s', t.replace('*', ''))
    return m.group(1) if m else None

def find(query, vault):
    qt, qn = toks(query), num(query)
    out = []
    for p in vaultroot.md_files(vault):
        b = os.path.basename(p)
        if b in SKIP:
            continue
        for i, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
            if not re.match(r'^#{1,6} ', l):
                continue
            ht = toks(l)
            if not qt or not ht:
                continue
            sc = len(qt & ht) / max(1, min(len(qt), len(ht)))
            hn = num(l)
            if qn and hn and qn == hn:
                sc += 0.45
            elif qn and hn and qn != hn:
                sc -= 0.35
            if sc >= 0.55:
                out.append((round(sc, 2), b, i, l))
    out.sort(reverse=True)
    return out

def selftest(vault):
    """Rule 11: a case whose answer is already known - the paraphrase that broke exact matching."""
    q = '## 0.1 Thyroid Panel (TSH, fT4, fT3, antibodies)'
    hits = find(q, vault)
    exact = any('Thyroid Panel' in h[3] for h in hits[:1])
    print(f"  [{'ok ' if exact else 'FAIL'}] paraphrased query resolves to the real heading")
    if hits:
        print(f"        top hit: {hits[0][1]}:{hits[0][2]}  {hits[0][3][:72]}")
    print(f"\n  self-test: {'1/1' if exact else '0/1'} known answers correct")
    return 0 if exact else 1

if __name__ == '__main__':
    vault = vaultroot.root()
    if '--selftest' in sys.argv:
        sys.exit(selftest(vault))
    for sc, f, i, l in find(sys.argv[1], vault):
        print(f'{sc:<5} {f}:{i}  {l[:100]}')
