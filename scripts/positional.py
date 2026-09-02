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
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import vaultroot

ROOT=vaultroot.root()
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
        # A reference names a section by its acronym far more often than by its
        # full heading.  Missing this let "the PONV section above" through against
        # "0.4 Post-Operative Nausea and Vomiting (PONV)" on a real reorder.
        for al in re.findall(r'\(([^)]{2,40})\)',h):
            a=norm(al)
            if a and a not in byname: byname[a].append(i)
            byname[a+' section'].append(i) if a else None
        base=norm(re.sub(r'\([^)]*\)','',h))
        if base and base not in byname: byname[base].append(i)
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
                if not tgt:
                    # "PONV - see dedicated section above" captures the whole run.
                    # Try word windows at each end, minus the connective words, so a
                    # reference that NAMES a section inside a longer phrase resolves.
                    w=[x for x in q.split() if x not in
                       ('see','the','a','dedicated','section','entry','part','in','at','and')]
                    cand=set()
                    for k in (1,2,3,4):
                        if len(w)>=k: cand.add(' '.join(w[:k])); cand.add(' '.join(w[-k:]))
                    hits={ln for c in cand if len(c)>=4 for ln in byname.get(c,[])}
                    if len(hits)==1: tgt=list(hits)
            if not tgt: continue                  # not a same-file section reference
            if len(tgt)>1: continue               # ambiguous, cannot judge direction
            t=tgt[0]
            okay = (t<i) if dirn=='above' else (t>i)
            if not okay: out.append((path,i,name,dirn,t))
    return out

def constraints(path,text):
    """Every resolvable positional reference, as an ordering constraint.

    Reading these BEFORE reordering is far cheaper than discovering them as
    breakage afterwards: Endocrine's disease block broke 12 references on the
    first attempt and 3 more on the second, all of which are listed here.
    Output is "X must come before Y", deduplicated, using ## section names.
    """
    L=text.split('\n')
    h2=[]                                  # (lineno, name) for ## only
    for i,l in enumerate(L,1):
        m=RE_HEAD.match(l)
        if m and m.group(1)=='##': h2.append((i,m.group(2).strip()))
    def owner(line):
        cur=None
        for i,n in h2:
            if i<=line: cur=n
            else: break
        return cur
    hits=scan(path,text)                   # only the ones pointing the WRONG way
    # rescan for ALL resolvable refs, right or wrong
    out=set()
    byname=collections.defaultdict(list); bynum=collections.defaultdict(list)
    for i,n in h2:
        byname[norm(n)].append((i,n))
        for al in re.findall(r'\(([^)]{2,40})\)',n):
            a=norm(al)
            if a: byname[a].append((i,n))
        base=norm(re.sub(r'\([^)]*\)','',n))
        if base: byname[base].append((i,n))
        sn=secnum(n)
        if sn: bynum[sn].append((i,n))
    for i,l in enumerate(L,1):
        if RE_HEAD.match(l): continue
        src=owner(i)
        if not src: continue
        for m in RE_POS.finditer(l):
            name,dirn=m.group(1).strip(),m.group(2)
            ctx=l[max(0,m.start()-18):m.end()+22]
            if RE_COMPARATIVE.search(ctx): continue
            cands=None
            if re.match(r'^\d+\.\d',name): cands=bynum.get(name)
            else:
                q=norm(name); cands=byname.get(q)
                if not cands:
                    w=[x for x in q.split() if x not in
                       ('see','the','a','dedicated','section','entry','part','in','at','and')]
                    pool=set()
                    for k in (1,2,3,4):
                        if len(w)>=k:
                            for c in (' '.join(w[:k]),' '.join(w[-k:])):
                                if len(c)>=4: pool.update(byname.get(c,[]))
                    cands=list(pool) if len(pool)==1 else None
            if not cands or len(set(n for _,n in cands))!=1: continue
            tgt=cands[0][1]
            if tgt==src: continue           # intra-section, no constraint
            out.add((tgt,src) if dirn=='above' else (src,tgt))
    return sorted(out)

def files():
    o='\n'.join(vaultroot.tracked_md_files(ROOT))
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
    # Found live, 2026-09-01, reordering Anaes_merged: the resolver reported CLEAN
    # while two references in 0.8 said "the PONV section above" and I had just moved
    # 0.8 above 0.4.  The reference names the section by ACRONYM inside a longer
    # phrase, which nothing in the matcher could see.  Both directions pinned here.
    t('acronym-in-phrase, inverted, caught',
      [x[3] for x in scan('t','## 0.8 Postoperative Care\nPONV - see dedicated section above\n## 0.4 Nausea and Vomiting (PONV)\n')],
      ['above'])
    t('acronym-in-phrase, correct, silent',
      scan('t','## 0.4 Nausea and Vomiting (PONV)\n## 0.8 Postoperative Care\nPONV - see dedicated section above\n'),[])
    # NOTE: the first version of this test asserted a hit on
    #   '## 0.1 Alpha / ## 0.2 Beta / see 0.2 above'
    # which is CORRECTLY ordered - 0.2 really is above the reference - so silence
    # was the right answer and the test was wrong, not the code.  Both directions
    # are now pinned.
    t('numbered section, correct order, silent',
      scan('t','## 0.1 Alpha\n## 0.2 Beta\nsee 0.2 above\n'),[])
    t('numbered section, inverted, caught',
      [(x[2],x[3]) for x in scan('t','## 0.1 Alpha\nsee 0.2 above\n## 0.2 Beta\n')],[('0.2','above')])
    print('--- audit filter: real references must survive, comparatives must be dropped')
    def keeps(l):
        for x in RE_ANY.finditer(l):
            if not RE_COMPARATIVE.search(l[max(0,x.start()-18):x.end()+22]): return True
        return False
    KEEP=['via the PONV section above)','- PONV - see dedicated section above',
          'mnemonic in the IPF section above; no dedicated entry',
          'see Polypharmacy and Deprescribing below.',
          'per the COPD-X framework above - not by',
          '**Both criteria above are ADULT criteria**','| CLS | yes | As above. |',
          '(see Abuse of Older People (Elder Abuse) and Carer Stress above']
    DROP=['time spent below 90%, and the obstructive',
          'function far below their baseline, and decisions',
          'on DXA below a defined threshold','fall from standing height or less',
          'target SpO2 92-96% while treating']
    t('every real reference survives the filter',[l[:34] for l in KEEP if not keeps(l)],[])
    t('every comparative is dropped',[l[:34] for l in DROP if keeps(l)],[])
    return ok

RE_ANY=re.compile(r'\b(above|below|earlier in this|further down|further up|preceding section|following section)\b',re.I)
# "below 90%", "far below their baseline", "below a defined threshold" are the
# COMPARATIVE sense and say nothing about order.  Excluding those is safer than
# trying to enumerate the referring sense, which has no closed vocabulary:
# "section above", "framework above", "regimen above", "criteria above", "box above".
RE_COMPARATIVE=re.compile(
    r'(?:\b(?:far|well|just|or|and|to|of|is|are|was|were|fall|falls|fell|drop|drops|dropping|'
    r'stay|stays|remain|remains|spent|anything|nothing|value|values|score|scores)\s+(?:above|below)\b)'
    r'|(?:\b(?:above|below)\s+(?:\d|[<>~]|about\b|around\b|roughly\b|approximately\b|'
    r'a\s+defined\b|the\s+\d|which\b|this\s+age|normal\b|baseline\b|target\b|threshold\b))',re.I)

def order(text):
    out=[]
    for l in text.split('\n'):
        m=RE_HEAD.match(l)
        if m and m.group(1)=='##': out.append(m.group(2).strip())
    return out

def audit(f,base):
    """Every positional word inside a ## section that MOVED, for reading by hand.

    positional.py can only judge a reference it can resolve to a heading.  A
    reference by acronym, by description ("see dedicated section above"), or to a
    sub-part is unresolvable, and on a reorder those are exactly the ones that
    break.  So: no verdict, just the lines, scoped to the sections that moved.
    """
    cur=io.open(os.path.join(ROOT,f),encoding='utf-8').read()
    old=subprocess.run(['git','-C',ROOT,'show',f'{base}:{f}'],capture_output=True,text=True).stdout
    ob,nb=order(old),order(cur)
    if ob==nb: return []
    rank_o={h:i for i,h in enumerate(ob)}; rank_n={h:i for i,h in enumerate(nb)}
    movedset={h for h in nb if h in rank_o and rank_o[h]!=rank_n[h]}
    out=[]; cursec=None
    for i,l in enumerate(cur.split('\n'),1):
        m=RE_HEAD.match(l)
        if m and m.group(1)=='##': cursec=m.group(2).strip()
        if cursec not in movedset or l.startswith('#'): continue
        hits=[m for m in RE_ANY.finditer(l)]
        if not hits: continue
        keep=False
        for m in hits:
            ctx=l[max(0,m.start()-18):m.end()+22]
            if not RE_COMPARATIVE.search(ctx): keep=True; break
        if keep: out.append((f,i,cursec,l.strip()))
    return out

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
    if '--constraints' in sys.argv:
        for f in targets:
            c=constraints(f,io.open(os.path.join(ROOT,f),encoding='utf-8').read())
            print(f'\n--- {f}: {len(c)} ordering constraint(s) from its own prose')
            for x,y in c: print(f'  {x[:52]:54s} MUST PRECEDE  {y[:52]}')
        sys.exit(0)
    if '--audit' in sys.argv:
        assert base, '--audit needs --base'
        n=0
        for f in targets:
            rows=audit(f,base)
            if rows: print(f'\n--- {f}: {len(rows)} positional line(s) inside sections that moved')
            for _,i,sec,l in rows:
                print(f'  {i:6d} [{sec[:40]}] {l[:150]}')
            n+=len(rows)
        print(f'\n{n} line(s) to read by hand. No verdict is offered: these are the references the resolver CANNOT judge.')
        sys.exit(0)
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
