#!/usr/bin/env python3
"""Catch the SILENT direction: a cross-reference whose section number EXISTS in
   the target file but names a DIFFERENT section than the words beside it.

   dangling.py cannot see these - 0.28/0.29/0.30 all exist, so it reports clean.
   The check is possible only because many pointers name the topic as well as the
   number: '[[01_Cardiovascular]] 0.30 Infective Endocarditis'. Where the number
   and the name disagree, one of them is wrong."""
import re, glob, os, collections
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import vaultroot
VAULT=vaultroot.root()
head=collections.defaultdict(dict); code2stem={}
for f in vaultroot.md_files(VAULT):
    b=os.path.basename(f)
    if b in ('CLAUDE.md','RUN_STATE.md'): continue
    cur=b[:-3]
    for l in open(f,encoding='utf-8'):
        m=re.match(r'^<!-- ===== SOURCE: (.*?) ===== -->',l)
        if m:
            cur=m.group(1)[:-3] if m.group(1).endswith('.md') else m.group(1)
            pre=cur.split('_')[0]
            if re.fullmatch(r'[A-Z]{1,4}[0-9]{0,2}(-[0-9])?',pre) and pre!='NEW': code2stem[pre]=cur
            code2stem[cur]=cur; continue
        h=re.match(r'^#{1,6} (\d+\.\d+(?:\.\d+)?)\s+(.*)',l)
        if h: head[cur][h.group(1)]=h.group(2).strip()
    pre=b[:-3].split('_')[0]
    if re.fullmatch(r'[A-Z]{1,4}[0-9]{0,2}(-[0-9])?',pre) and pre!='NEW': code2stem.setdefault(pre,b[:-3])
    code2stem.setdefault(b[:-3],b[:-3])
alt='|'.join(re.escape(t) for t in sorted(code2stem,key=len,reverse=True))
# pointer that carries a number AND at least two capitalised/topic words after it
RX=re.compile(r'\[\[('+alt+r')\]\]\s*(?:§|section|sections|part|chapter|item)?\s*(\d+\.\d+(?:\.\d+)?)\s+([A-Z][A-Za-z\'()\-]*(?:\s+[A-Za-z\'()\-/]+){0,4})')
STOP={'for','the','and','see','not','a','of','in','to','with'}
def words(s): return {w.lower().strip("'()/-") for w in re.findall(r"[A-Za-z']+",s)} - STOP
checked=0; bad=[]
for f in vaultroot.md_files(VAULT):
    b=os.path.basename(f)
    if b in ('CLAUDE.md','RUN_STATE.md'): continue
    for n,l in enumerate(open(f,encoding='utf-8'),1):
        if l.startswith('<!-- ===== SOURCE:'): continue
        for m in RX.finditer(l):
            stem=code2stem[m.group(1)]; sec=m.group(2); named=m.group(3)
            if stem not in head or sec not in head[stem]: continue
            checked+=1
            actual=head[stem][sec]
            nw, aw = words(named), words(actual)
            if not nw: continue
            if nw & aw: continue                      # number and name agree
            # does the named topic match a DIFFERENT section of the same file?
            cand=[s for s,t in head[stem].items() if nw & words(t)]
            bad.append((b,n,stem,sec,actual,named,cand))
print(f'pointers carrying BOTH a number and a topic name : {checked}')
print(f'  number and name DISAGREE : {len(bad)}\n')
for b,n,stem,sec,actual,named,cand in bad:
    fix=('  ACTUAL HOME -> '+', '.join(cand)) if cand else '  (no section of that file matches the name)'
    print(f'{b}:{n}\n   says  {stem} {sec} "{named}"\n   but   {sec} is "{actual}"{fix}')
