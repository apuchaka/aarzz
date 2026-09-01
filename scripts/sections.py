#!/usr/bin/env python3
"""Heading + first paragraph for every section of a merged file.
   Skips the Corpus-B 'Mx - Immediate/Definitive/Chronic' boilerplate triads."""
import re, sys, os
VAULT='/home/user/aarzz'
BOILER=re.compile(r'^#{2,6} \d+\.\d+\.\d+ Mx\b')
p=os.path.join(VAULT,sys.argv[1])
lines=open(p,encoding='utf-8').read().split('\n')
src=''; heads=[]
for i,l in enumerate(lines):
    m=re.match(r'^<!-- ===== SOURCE: (.*?) ===== -->',l)
    if m: src=m.group(1)
    if re.match(r'^#{1,6} ',l): heads.append((i,l,src))
cur=None
for n,(i,h,s) in enumerate(heads):
    if s!=cur: print(f'\n>>>>>>>>>> SOURCE {s}  (from L{i})'); cur=s
    if BOILER.match(h): continue
    end=heads[n+1][0] if n+1<len(heads) else len(lines)
    body=[x for x in lines[i+1:end] if x.strip() and not x.startswith('<!--')]
    first=body[0] if body else '(no body)'
    if len(first)>260: first=first[:260]+' …[preview-only]'
    print(f'L{i+1} {h}\n     {first}')
