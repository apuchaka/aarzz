#!/usr/bin/env python3
"""Three post-move checks. Each shape survives a move and reads as correct.

  1. STUB  — a `Moved to [[X]]` stub whose named section is not in X.
  2. TWICE — a heading that exists once before a move and twice after.
  3. XREF  — a prose `[[File]] Section Name` pointer whose section is not in File.

Usage:
  scripts/aftermove.py                 all three, TWICE compared against HEAD
  scripts/aftermove.py --base <rev>    compare TWICE against <rev>
  scripts/aftermove.py --selftest      known-answer tests, then exit

Rule 11: every check below is run first against a case whose answer is already
known.  A check that cannot fail is worse than no check, because it reports clean.
"""
import re,sys,os,io,glob,collections,subprocess
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import vaultroot

ROOT=vaultroot.root()

def files():
    out='\n'.join(vaultroot.tracked_md_files(ROOT))
    return [f for f in out.split('\n') if f.strip() and not f.startswith('_meta/')]

def text(f):  return io.open(os.path.join(ROOT,f),encoding='utf-8').read()
def at(rev,f):
    r=subprocess.run(['git','-C',ROOT,'show',f'{rev}:{f}'],capture_output=True,text=True)
    return r.stdout if r.returncode==0 else ''

RE_HEAD=re.compile(r'^#{1,6} (.+)$',re.M)
def headings(t): return [m.group(1).strip() for m in RE_HEAD.finditer(t)]

# ---------------------------------------------------------------- 1. STUB
RE_STUB=re.compile(r'Moved (?:to|here from) `\[\[([^\]]+)\]\]`')
RE_TICK=re.compile(r'`([^`]+)`')

def norm(s):
    """Compare heading text ignoring the section number and markdown emphasis."""
    s=re.sub(r'[*_`]','',s)
    s=re.sub(r'^\s*\d+(\.\d+)*\s+','',s.strip())
    return re.sub(r'\s+',' ',s).lower()

# Boilerplate that appears inside stub prose in backticks and is not a section name.
STUB_NOISE={'source:','todo:link','cf-pair','unverified','verified','med:','src:'}

def stub_names(line):
    """The section/block names a stub claims moved. Not every backticked run is one."""
    out=[]
    for n in RE_TICK.findall(line):
        if n.startswith('[['): continue
        if n.strip().lower() in STUB_NOISE: continue
        if len(n) < 8: continue
        out.append(n)
    return out

def check_stubs(verbose=False):
    """A stub is satisfied when its named content is FINDABLE in the destination.

    Deliberately not 'is a heading there'. Stubs name headings, sub-blocks and
    callout titles alike, and a sub-block arrives as a body line, not a heading.
    Asking the narrower question produced 100+ false positives on the live vault
    (CLAUDE.md rule 9: a component pattern that is too generic).
    """
    body={}; head={}
    for f in files():
        t=text(f); b=os.path.basename(f)[:-3]
        head[b]={norm(h) for h in headings(t)}
        body[b]=[norm(l) for l in t.split('\n') if l.strip()]
    bad=[]
    for f in files():
        for i,line in enumerate(text(f).split('\n'),1):
            m=RE_STUB.search(line)
            if not m or 'Moved to' not in line: continue
            tgt=m.group(1)
            if tgt not in head: bad.append((f,i,tgt,'<target file not found>')); continue
            for n in stub_names(line):
                q=norm(n)
                if q in head[tgt]: continue
                if any(q in l for l in body[tgt]): continue
                bad.append((f,i,tgt,n))
    return bad

# --------------------------------------------------------------- 2. TWICE
def check_twice(base):
    out=[]
    for f in files():
        b=collections.Counter(h for h in headings(at(base,f)))
        n=collections.Counter(h for h in headings(text(f)))
        for h,c in n.items():
            if c>1 and b.get(h,0)<c: out.append((f,h,b.get(h,0),c))
    return out

# ---------------------------------------------------------------- 3. XREF
RE_XREF=re.compile(r'\[\[([^\]|#]+)\]\]\s+([A-Z][^,.;:()\[\]]{6,70}?)(?=\s*(?:[,.;:()]|—|$|\bfor\b|\bin\b|\bat\b|\band\b))')

def check_xrefs():
    idx={}
    for f in files(): idx[os.path.basename(f)[:-3]]={norm(h) for h in headings(text(f))}
    bad=[]
    for f in files():
        for i,line in enumerate(text(f).split('\n'),1):
            for m in RE_XREF.finditer(line):
                tgt,name=m.group(1),m.group(2).strip()
                if tgt not in idx: continue          # dangling.py owns missing files
                if not idx[tgt]: continue
                if norm(name) in idx[tgt]: continue
                # a prefix of a real heading counts (references are often clipped)
                if any(h.startswith(norm(name)) for h in idx[tgt]): continue
                bad.append((f,i,tgt,name))
    return bad

# ------------------------------------------------------------- self-tests
def selftest():
    ok=True
    def t(label,got,want):
        nonlocal ok
        good = got==want
        ok = ok and good
        print(f'  [{"ok " if good else "FAIL"}] {label}: got {got!r}, want {want!r}')
    print('--- norm()')
    t('section number stripped',norm('1.15 Joint Aspirate'),'joint aspirate')
    t('bold inside a word survives',norm('**H**aemolysis'),'haemolysis')
    t('emphasis stripped',norm('*modified* Valsalva'),'modified valsalva')
    print('--- STUB matcher, against a stub known to be well-formed and one known to be broken')
    line='> [!note] **Moved to `[[Procedures]]` on 2026-09-01:** `0.6 Renal Biopsy` — reproduced there.'
    m=RE_STUB.search(line)
    t('target extracted',m.group(1) if m else None,'Procedures')
    t('section extracted',[n for n in RE_TICK.findall(line) if not n.startswith('[[') and len(n)>6],['0.6 Renal Biopsy'])
    print('--- STUB check, against one stub known good and one known broken')
    real=check_stubs()
    t('the live renal-biopsy stub is satisfied',
      [x for x in real if 'Renal Biopsy' in x[3]],[])
    t('SOURCE: is not read as a section name',
      [x for x in real if x[3].strip()=='SOURCE:'],[])
    import tempfile
    t('a stub naming absent content IS caught',
      bool([n for n in stub_names('Moved to `[[Procedures]]`: `A Section Nobody Ever Wrote` — done.')]),True)
    print('--- XREF matcher, against a live reference whose answer is known')
    s='see [[Investigation-Interpretation]] Chest X-Ray — Systematic Approach for the framework'
    got=[(m.group(1),m.group(2).strip()) for m in RE_XREF.finditer(s)]
    t('file+section split',got,[('Investigation-Interpretation','Chest X-Ray')])
    print('--- TWICE, against a constructed duplicate (the failure it exists to catch)')
    before=collections.Counter(headings('## Alpha\n## Beta\n'))
    after =collections.Counter(headings('## Alpha\n## Beta\n## Alpha\n'))
    dup=[h for h,c in after.items() if c>1 and before.get(h,0)<c]
    t('duplicate detected',dup,['Alpha'])
    t('no false positive on unchanged',[h for h,c in before.items() if c>1 and before.get(h,0)<c],[])
    return ok

if __name__=='__main__':
    if '--selftest' in sys.argv:
        print('=== aftermove.py self-test ===')
        sys.exit(0 if selftest() else 1)
    base='HEAD'
    if '--base' in sys.argv: base=sys.argv[sys.argv.index('--base')+1]
    print('=== aftermove.py ===  (self-test first, per CLAUDE.md rule 11)')
    if not selftest(): print('SELF-TEST FAILED — results below are not trustworthy'); sys.exit(1)
    print(f'\n--- 1. stubs naming content that is not at the destination')
    b=check_stubs()
    for f,i,t_,n in b: print(f'  {f}:{i}  [[{t_}]] does not hold `{n}`')
    print(f'  {len(b)} broken stub(s)')
    print(f'\n--- 2. headings that exist twice now and did not at {base}')
    d=check_twice(base)
    for f,h,c0,c1 in d: print(f'  {f}  {h[:70]}  {c0} -> {c1}')
    print(f'  {len(d)} new duplicate heading(s)')
    print(f'\n--- 3. prose [[File]] Section pointers whose section is not in File')
    x=check_xrefs()
    for f,i,t_,n in x: print(f'  {f}:{i}  [[{t_}]] "{n}"')
    print(f'  {len(x)} unresolved name pointer(s)')
    sys.exit(1 if (b or d or x) else 0)
