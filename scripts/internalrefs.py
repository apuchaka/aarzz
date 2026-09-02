#!/usr/bin/env python3
"""Bare internal §0.x pointers in a merged file: are they actually ambiguous?

A merged file concatenates many source files, each numbered from 0.1, so `## 0.1`
appears once per block and a bare `§0.1` looks ambiguous. It is not ambiguous in
the general case: the SOURCE divider governing the line says which block the
writer was in, and a bare number almost always means "this block's 0.1".

This resolves every bare §0.x against the block it is WRITTEN IN and reports the
ones that do not resolve there - the genuinely misaimed pointers. Renumbering is
not needed to answer the question, and would break the 2,953 cross-file
`[[File]] 0.x` pointers that resolve by (source file, section number).

  scripts/internalrefs.py [FILE ...]
  scripts/internalrefs.py --selftest
"""
import re,sys,os,io,subprocess,collections

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RE_DIV=re.compile(r'^<!-- ===== SOURCE: (\S+\.md) ===== -->')
RE_H  =re.compile(r'^(#{2,6}) (\d+\.\d+(?:\.\d+)*)')
RE_WL =re.compile(r'\[\[[^\]|#]+\]\]\s*§?\d+\.\d+(?:\.\d+)?')
RE_BT =re.compile(r'`[A-Za-z0-9_\-. ]+\.md`\s*§?\d+\.\d+(?:\.\d+)?')
RE_BARE=re.compile(r'§(\d+\.\d+(?:\.\d+)?)')

def scan(path,text):
    L=text.split('\n')
    # section numbers present per block, in order of block appearance
    blocks=[]; cur=None
    for l in L:
        m=RE_DIV.match(l)
        if m: cur={'src':m.group(1),'nums':set()}; blocks.append(cur); continue
        h=RE_H.match(l)
        if h:
            if cur is None: cur={'src':None,'nums':set()}; blocks.append(cur)
            cur['nums'].add(h.group(2))
    # walk again, tracking which block each line is in
    out=[]; bi=-1
    allnums=set()
    for b in blocks: allnums|=b['nums']
    for i,l in enumerate(L,1):
        if RE_DIV.match(l): bi+=1; continue
        if bi<0: continue
        stripped=RE_BT.sub(' ',RE_WL.sub(' ',l))     # drop qualified pointers
        for n in RE_BARE.findall(stripped):
            if n in blocks[bi]['nums']: continue      # resolves in its own block
            where=[b['src'] for b in blocks if n in b['nums']]
            out.append((path,i,n,blocks[bi]['src'],where))
    return out

def selftest():
    ok=True
    def t(label,got,want):
        nonlocal ok; good=got==want; ok=ok and good
        print(f'  [{"ok " if good else "FAIL"}] {label}: got {got!r}, want {want!r}')
    same=('<!-- ===== SOURCE: A.md ===== -->\n## 0.1 Alpha\n## 0.2 Beta\nsee §0.2 for more\n'
          '<!-- ===== SOURCE: B.md ===== -->\n## 0.1 Gamma\n')
    t('a bare ref resolving in its own block is silent',scan('t',same),[])
    other=('<!-- ===== SOURCE: A.md ===== -->\n## 0.1 Alpha\nsee §0.7 for more\n'
           '<!-- ===== SOURCE: B.md ===== -->\n## 0.7 Gamma\n')
    r=scan('t',other)
    t('a bare ref resolving only in ANOTHER block is reported',[(x[2],x[3],x[4]) for x in r],[('0.7','A.md',['B.md'])])
    none=('<!-- ===== SOURCE: A.md ===== -->\n## 0.1 Alpha\nsee §0.9 for more\n')
    t('a bare ref resolving nowhere is reported',[(x[2],x[4]) for x in scan('t',none)],[('0.9',[])])
    qual=('<!-- ===== SOURCE: A.md ===== -->\n## 0.1 Alpha\nsee [[B]] 0.7 and `B.md` 0.8\n'
          '<!-- ===== SOURCE: B.md ===== -->\n## 0.7 G\n## 0.8 H\n')
    t('qualified pointers are not treated as bare',scan('t',qual),[])
    return ok

def files():
    o=subprocess.run(['git','-C',ROOT,'ls-files','*_merged.md'],capture_output=True,text=True).stdout
    return [f for f in o.split('\n') if f.strip()]

if __name__=='__main__':
    if '--selftest' in sys.argv:
        print('=== internalrefs.py self-test ==='); sys.exit(0 if selftest() else 1)
    print('=== internalrefs.py ===  (self-test first, per CLAUDE.md rule 11)')
    if not selftest(): print('SELF-TEST FAILED'); sys.exit(1)
    targets=[a for a in sys.argv[1:] if not a.startswith('--')] or files()
    tot=0; elsewhere=0; nowhere=0
    print()
    for f in targets:
        r=scan(f,io.open(os.path.join(ROOT,f),encoding='utf-8').read())
        if not r: continue
        print(f'--- {f}: {len(r)} bare §0.x not resolving in their own block')
        for _,i,n,src,where in r:
            if where: elsewhere+=1
            else: nowhere+=1
            print(f'  {i:6d}  §{n:8s} written in [{src}] -> exists in: {where or "NOWHERE in this file"}')
        tot+=len(r)
    print(f'\n{tot} bare internal pointer(s) that do not resolve in their own block '
          f'({elsewhere} resolve in a different block, {nowhere} resolve nowhere)')
    sys.exit(1 if tot else 0)
