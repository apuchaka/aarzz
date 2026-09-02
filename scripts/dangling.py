#!/usr/bin/env python3
"""Resolve every NUMERIC section cross-reference in the vault against the
   headings that actually exist in the target source file's span.
   Found because Cardio carries pointers to 01_Cardiovascular 0.34.5 / 0.35.8,
   neither of which exists - each off by one at the second level."""
import re, glob, os, collections
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import vaultroot
VAULT=vaultroot.root()
# map: source-file stem -> set of section numbers it actually contains
have=collections.defaultdict(set); code2stem={}
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
            code2stem[cur]=cur
            continue
        h=re.match(r'^#{1,6} (\d+\.\d+(?:\.\d+)?)\s',l)
        if h: have[cur].add(h.group(1))
    # also register non-merged files under their own name
    pre=b[:-3].split('_')[0]
    if re.fullmatch(r'[A-Z]{1,4}[0-9]{0,2}(-[0-9])?',pre) and pre!='NEW': code2stem.setdefault(pre,b[:-3])
    code2stem.setdefault(b[:-3],b[:-3])

toks=sorted(code2stem,key=len,reverse=True)
alt='|'.join(re.escape(t) for t in toks)
WL=re.compile(r'\[\[('+alt+r')\]\]\s*(?:§|section|sections|part|chapter|item)?\s*(\d+\.\d+(?:\.\d+)?)')
BT=re.compile(r'`('+alt+r')(?:\.md)?`\s*(?:§|section|sections|part|chapter|item)?\s*(\d+\.\d+(?:\.\d+)?)')
bad=[]; total=0
for f in vaultroot.md_files(VAULT):
    b=os.path.basename(f)
    if b in ('CLAUDE.md','RUN_STATE.md'): continue
    for n,l in enumerate(open(f,encoding='utf-8'),1):
        if l.startswith('<!-- ===== SOURCE:'): continue
        for rx in (WL,BT):
            for m in rx.finditer(l):
                stem=code2stem[m.group(1)]; sec=m.group(2); total+=1
                if stem in have and sec not in have[stem]:
                    bad.append((b,n,m.group(1),stem,sec))
print(f'numeric section pointers resolved : {total}')
print(f'pointing at a section that DOES NOT EXIST in the target : {len(bad)}')
print(f'rate : {100*len(bad)/total:.1f}%\n')
byt=collections.Counter(x[3] for x in bad)
print('--- by target file ---')
for k,v in byt.most_common(25): print(f'{v:>4}  {k}')
