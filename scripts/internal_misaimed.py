#!/usr/bin/env python3
"""The Resp-shape class: an internal number that RESOLVES in its own block but
lands on something unrelated to what the sentence says.

internalrefs.py cannot see these - a number that resolves in its own block looks
correct to it. But most such references carry their own title:
    `§0.5 Mesothelioma`      own-block 0.5 = "Sleep-Disordered Breathing"
So: find every internal reference of the form `<number> <Title>` and compare the
Title against the heading that number actually resolves to in the SAME block.

This does not judge references that carry no title - those need the sentence read
against the target, and no tool can do it.

  scripts/internal_misaimed.py [--selftest]
"""
import re,sys,os,io,subprocess,difflib
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RE_DIV=re.compile(r'^<!-- ===== SOURCE: (\S+\.md) ===== -->')
RE_H  =re.compile(r'^(#{2,6}) (\d+\.\d+(?:\.\d+)*)\s+(.*)$')
# a reference that carries a title: §0.5 Mesothelioma  /  `0.18 OSA`
RE_REF=re.compile(r'§?(\d+\.\d+(?:\.\d+)?)\s+([A-Z][A-Za-z0-9/\'’(),\- ]{3,60})')
# "~0.1 U/kg/h" is a DOSE, not a reference. A unit right after the number is the tell.
RE_UNIT=re.compile(r'^(?:U|IU|mg|mcg|g|mL|L|mmol|kg|units?)\b|^[A-Z]/')
RE_QUALIFIED=re.compile(
    r'(?:\[\[[^\]|#]+\]\]'
    r'|`[A-Za-z0-9_\-. ]+\.md`'
    r'|[A-Za-z0-9][A-Za-z0-9_\-.]{5,}'
    r'|\b(?:[A-Z]{1,4}[0-9]{1,2}[a-z]?|F[0-9]-[0-9]|CV-X|RESP-X)\b)'    # a source CODE: AN1, J5, B2, F0-4
    r'[^`§]{0,12}$')
STOP=set('the a an of and in for to with on at by from is are as its it this that or'.split())
def toks(s):
    s=re.sub(r'[*_`]','',s.lower()); s=re.sub(r'\([^)]*\)',' ',s)
    return {w for w in re.findall(r'[a-z]+',s) if w not in STOP and len(w)>2}

def scan(path,text):
    L=text.split('\n'); blocks=[]; cur=None
    for l in L:
        m=RE_DIV.match(l)
        if m: cur={'src':m.group(1),'h':{}}; blocks.append(cur); continue
        h=RE_H.match(l)
        if h:
            if cur is None: cur={'src':None,'h':{}}; blocks.append(cur)
            cur['h'].setdefault(h.group(2),h.group(3).strip())
    out=[]; bi=-1
    for i,l in enumerate(L,1):
        if RE_DIV.match(l): bi+=1; continue
        if bi<0 or RE_H.match(l): continue
        for m in RE_REF.finditer(l):
            num,title=m.group(1),m.group(2).strip()
            if RE_UNIT.match(title): continue                    # a dose, not a reference
            if RE_QUALIFIED.search(l[:m.start()]): continue      # names a file: not internal
            tgt=blocks[bi]['h'].get(num)
            if tgt is None: continue                             # internalrefs.py owns these
            a,b=toks(title),toks(tgt)
            if not a or not b: continue
            if a&b: continue                                     # shares a word: consistent
            if difflib.SequenceMatcher(None,title.lower(),tgt.lower()).ratio()>0.55: continue
            out.append((path,i,num,title,tgt,blocks[bi]['src'],l.strip()))
    return out

def selftest():
    ok=True
    def t(lbl,got,want):
        nonlocal ok; g=got==want; ok=ok and g
        print(f'  [{"ok " if g else "FAIL"}] {lbl}: got {got!r}, want {want!r}')
    resp=('<!-- ===== SOURCE: RESP-X.md ===== -->\n## 0.5 Sleep-Disordered Breathing\n'
          'pairs with `§0.5 Mesothelioma` in the other file\n')
    t('the Resp case is caught',[(x[2],x[3],x[4]) for x in scan('t',resp)],
      [('0.5','Mesothelioma','Sleep-Disordered Breathing')])
    good=('<!-- ===== SOURCE: A.md ===== -->\n## 0.5 Mesothelioma\nsee §0.5 Mesothelioma above\n')
    t('a consistent reference is silent',scan('t',good),[])
    qual=('<!-- ===== SOURCE: A.md ===== -->\n## 0.5 Sleep-Disordered Breathing\n'
          'see `02_Respiratory §0.5 Mesothelioma`\n')
    t('a reference naming another file is not internal',scan('t',qual),[])
    near=('<!-- ===== SOURCE: A.md ===== -->\n## 0.5 Mesothelioma and Asbestos\nsee §0.5 Mesothelioma\n')
    t('a near-title match is silent',scan('t',near),[])
    return ok

def files():
    o=subprocess.run(['git','-C',ROOT,'ls-files','*_merged.md'],capture_output=True,text=True).stdout
    return [f for f in o.split('\n') if f.strip() and '/' not in f]

if __name__=='__main__':
    if '--selftest' in sys.argv:
        print('=== internal_misaimed.py self-test ==='); sys.exit(0 if selftest() else 1)
    print('=== internal_misaimed.py ===  (self-test first, per CLAUDE.md rule 11)')
    if not selftest(): print('SELF-TEST FAILED'); sys.exit(1)
    tot=0
    for f in [a for a in sys.argv[1:] if not a.startswith('--')] or files():
        r=scan(f,io.open(os.path.join(ROOT,f),encoding='utf-8').read())
        if not r: continue
        print(f'\n--- {f}: {len(r)}')
        for _,i,n,title,tgt,src,line in r:
            print(f'  L{i}  reference says "{n} {title}"')
            print(f'        own block [{src}] {n} is "{tgt}"')
            print(f'        {line[:150]}')
        tot+=len(r)
    print(f'\n{tot} internal reference(s) whose title disagrees with the section that number resolves to')
    sys.exit(1 if tot else 0)
