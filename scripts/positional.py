#!/usr/bin/env python3
"""Positional cross-references — the shape a REORDER breaks silently.

A section number does not change when a section moves, so `[[X]] 0.4` keeps
resolving.  `see General Anaesthesia above` does not: it is a claim about
ORDER, and reordering is exactly what invalidates it.

This resolves every `<Name> above|below` and `§0.x above|below` that names a
section in the SAME file, and checks the direction against the current order.

  scripts/positional.py                 whole vault
  scripts/positional.py FILE ...        named files
  scripts/positional.py --base REV ...  only report what REV did not already have
  scripts/positional.py --selftest
"""
import re,sys,os,io,subprocess,collections

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RE_HEAD=re.compile(r'^(#{2,6}) (.+)$')
# "<Name> above" / "<Name> below".  Name must start capitalised or with a section number.
RE_POS=re.compile(r'(?:§|\bsee\s+|\bin\s+|\bat\s+)?((?:\d+\.\d+(?:\.\d+)*)|(?:[A-Z][A-Za-z0-9/\'’\- ]{3,60}?))\s+(above|below)\b')

def norm(s):
    s=re.sub(r'[*_`]','',s)
    s=re.sub(r'^\s*\d+(\.\d+)*\s+','',s.strip())
    return re.sub(r'\s+',' ',s).strip().lower()

def secnum(h):
    m=re.match(r'^\s*(\d+(?:\.\d+)*)\s',h)
    return m.group(1) if m else None

def scan(path,text):
    heads=[]                       # (lineno, raw heading text)
    for i,l in enumerate(text.split('\n'),1):
        m=RE_HEAD.match(l)
        if m: heads.append((i,m.group(2).strip()))
    byname=collections.defaultdict(list); bynum=collections.defaultdict(list)
    for i,h in heads:
        byname[norm(h)].append(i)
        n=secnum(h)
        if n: bynum[n].append(i)
    out=[]
    for i,l in enumerate(text.split('\n'),1):
        if RE_HEAD.match(l): continue
        for m in RE_POS.finditer(l):
            name,dirn=m.group(1).strip(),m.group(2)
            tgt=None
            if re.match(r'^\d+\.\d',name): tgt=bynum.get(name)
            else:
                q=norm(name)
                tgt=byname.get(q)
                if not tgt:                       # a clipped reference to a longer heading
                    hit=[ln for k,v in byname.items() if k.startswith(q) and len(q)>=8 for ln in v]
                    tgt=hit or None
            if not tgt: continue                  # not a same-file section reference
            if len(tgt)>1: continue               # ambiguous, cannot judge direction
            t=tgt[0]
            okay = (t<i) if dirn=='above' else (t>i)
            if not okay: out.append((path,i,name,dirn,t))
    return out

def files():
    o=subprocess.run(['git','-C',ROOT,'ls-files','*.md'],capture_output=True,text=True).stdout
    return [f for f in o.split('\n') if f.strip() and not f.startswith('_meta/')]

def selftest():
    ok=True
    def t(label,got,want):
        nonlocal ok; good=got==want; ok=ok and good
        print(f'  [{"ok " if good else "FAIL"}] {label}: got {got!r}, want {want!r}')
    good='## Alpha\ntext\n## Beta\nsee Alpha above for the rest\n'
    bad ='## Alpha\nsee Beta above for the rest\ntext\n## Beta\n'
    t('correct "above" is silent',scan('t',good),[])
    t('inverted "above" is caught',[(x[2],x[3]) for x in scan('t',bad)],[('Beta','above')])
    good2='## Alpha\nsee Beta below for the rest\n## Beta\n'
    bad2 ='## Alpha\ntext\n## Beta\nsee Alpha below\n'
    t('correct "below" is silent',scan('t',good2),[])
    t('inverted "below" is caught',[(x[2],x[3]) for x in scan('t',bad2)],[('Alpha','below')])
    t('unknown name ignored',scan('t','## Alpha\nsee Gamma above\n'),[])
    # NOTE: the first version of this test asserted a hit on
    #   '## 0.1 Alpha / ## 0.2 Beta / see 0.2 above'
    # which is CORRECTLY ordered - 0.2 really is above the reference - so silence
    # was the right answer and the test was wrong, not the code.  Both directions
    # are now pinned.
    t('numbered section, correct order, silent',
      scan('t','## 0.1 Alpha\n## 0.2 Beta\nsee 0.2 above\n'),[])
    t('numbered section, inverted, caught',
      [(x[2],x[3]) for x in scan('t','## 0.1 Alpha\nsee 0.2 above\n## 0.2 Beta\n')],[('0.2','above')])
    return ok

if __name__=='__main__':
    argv=sys.argv[1:]
    a=[]; i=0
    while i<len(argv):
        if argv[i]=='--base': i+=2; continue
        if argv[i].startswith('--'): i+=1; continue
        a.append(argv[i]); i+=1
    if '--selftest' in sys.argv:
        print('=== positional.py self-test ==='); sys.exit(0 if selftest() else 1)
    print('=== positional.py ===  (self-test first, per CLAUDE.md rule 11)')
    if not selftest(): print('SELF-TEST FAILED'); sys.exit(1)
    base=None
    if '--base' in sys.argv: base=sys.argv[sys.argv.index('--base')+1]
    targets=a or files()
    tot=0
    for f in targets:
        cur=scan(f,io.open(os.path.join(ROOT,f),encoding='utf-8').read())
        if base:
            old=subprocess.run(['git','-C',ROOT,'show',f'{base}:{f}'],capture_output=True,text=True).stdout
            prev={(x[2],x[3]) for x in scan(f,old)}
            cur=[x for x in cur if (x[2],x[3]) not in prev]
        for p,i,n,d,t_ in cur:
            print(f'  {p}:{i}  "{n} {d}" but that section is at line {t_}')
        tot+=len(cur)
    print(f'\n{tot} positional reference(s) pointing the wrong way' + (f' that {base} did not already have' if base else ''))
    sys.exit(1 if tot else 0)
