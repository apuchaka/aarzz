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
# A reference is QUALIFIED if a file is named before the number, in any of the
# forms this corpus actually uses - not only the two the first draft recognised.
# Found 2026-09-02: the first draft reported 125, and most were notes reading
# `AN1 §0.5 Postoperative Complications` or `GI_merged §0.42 ...`, where the file
# IS named but inside the SAME backtick span, so `File.md` never matched.
# CLAUDE.md rule 3: every automated scan produces false positives.
_NAMES=None
def known_names():
    """Every name that can qualify a pointer: file basenames, SOURCE-divider
    names, and the Corpus B prefix codes that resolve to exactly one of them.

    Enumerating these EXACTLY replaced a regex that tried to guess their shape.
    That regex missed `NEW_Investigations_Haematology_Part2 §0.11 ...` and
    `GP_merged NEW_Investigations_General_and_Preventive §0.14 ...`, both of
    which name the file plainly, and so reported a qualified pointer as bare.
    """
    global _NAMES
    if _NAMES is not None: return _NAMES
    n=set()
    allmd=[f for f in subprocess.run(['git','-C',ROOT,'ls-files','*.md'],
           capture_output=True,text=True).stdout.split('\n') if f.strip()]
    for f in allmd:                       # every .md, not just the merged files:
        n.add(os.path.basename(f)[:-3])   # `Examination.md 1.27` must qualify too
        for m in re.finditer(r'^<!-- ===== SOURCE: (\S+)\.md ===== -->',
                             io.open(os.path.join(ROOT,f),encoding='utf-8').read(),re.M):
            n.add(m.group(1))
    n={x for x in n if len(x)>2}
    codes=set()
    for x in n:
        head=x.split('_')[0]
        if len(head)<=5 and any(c.isdigit() for c in head) and len([y for y in n if y.startswith(head+'_')])==1:
            codes.add(head)
    _NAMES=sorted(n|codes,key=len,reverse=True)
    return _NAMES

def qualified(line,pos):
    """Is the section number at `pos` preceded, close by, by a named file?

    Scoped to the enclosing backtick span when there is one - this corpus writes
    such notes as a single span, `AN1 §0.5 Postoperative Complications` - and
    otherwise to the 25 characters before, so a file named in a NEIGHBOURING
    reference on the same line does not qualify this one.

    Found 2026-09-02: the first draft recognised only [[File]] 0.x and
    `File.md` 0.x, and reported 125 bare pointers. 69 of those name the file
    inside the same span in a form it could not see. CLAUDE.md rule 3.
    """
    seg=line[:pos]
    tick=seg.rfind('`')
    if tick!=-1 and line.count('`',0,pos)%2==1:
        seg=seg[tick+1:]
    else:
        seg=seg[-25:]
    if re.search(r'\[\[[^\]|#]+\]\][^`§]{0,10}?$',seg): return True
    if any(nm in seg for nm in known_names()): return True
    # The corpus also abbreviates: `NEW_Drugs_10 §0.5.4` for NEW_Drugs_10_Endocrine.
    # A token that is a prefix of EXACTLY ONE known name, and long enough not to
    # collide, qualifies too.
    for tok in re.findall(r'[A-Za-z0-9][A-Za-z0-9_\-.]{7,}',seg):
        if len([n for n in known_names() if n.startswith(tok)])==1: return True
    return False

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
        for m in RE_BARE.finditer(stripped):
            n=m.group(1)
            if qualified(stripped,m.start()): continue
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
    print('--- qualified(): the nine cases the 125-to-56 correction turned on')
    C=[("> `AN1 §0.5 Postoperative Complications` is the Corpus B version.",True,'source code in span'),
       ("> `GI_merged §0.42 Faecal Incontinence (Adult)`.",True,'X_merged in span'),
       ("> `NEW_Investigations_Haematology_Part2 §0.11 Coagulation Profile`",True,'long source name'),
       ("> `GP_merged NEW_Investigations_General_and_Preventive §0.14 Genetic Risk`",True,'two names in span'),
       ("> `Examination.md §1.27 Leg and Skin Ulcers`",True,'File.md in span'),
       ("see §0.4 for the full management",False,'genuinely bare'),
       ("cross-refer [[F0.3]] 0.7 and then §0.9",False,'neighbouring link must not qualify'),
       ("> `§0.1 ILD` ↔ `§0.7 IPF`",False,'span starts with the number'),
       ("`CF-PAIR` **`J3 §0.1 Interpreting` and `§1.17 Coagulation Screen`",False,'second span is bare')]
    wrong=[]
    for line,want,label in C:
        i=line.rfind('§') if 'second span' in label else line.find('§')
        if qualified(line,i)!=want: wrong.append(label)
    t('all nine qualified() cases',wrong,[])
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
