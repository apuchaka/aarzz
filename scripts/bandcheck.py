#!/usr/bin/env python3
"""Band-tiling check: find sets of numeric bands over one axis where consecutive
bands do not meet, so a value in between falls into no band.

Three instances made this a class (CLAUDE.md-adjacent, PENDING_GUIDELINE_CHECKS
B66/B67): the ASCIA adrenaline `<7.5 kg` boundary, the EZ-IO `<39 kg` / `>40 kg`
needle bands, and hypercalcaemia "mild 2.6-2.9; moderate 3.0-3.4".

WHAT IT CANNOT SEE, stated so nobody reads a clean run as proof:
  * band sets spread across several lines of a table with the unit only in a
    header cell;
  * TWO-AXIS band sets — the ASCIA table bands on weight AND age at once, and a
    4-year-old over 20 kg matches no row. That is B67 and this script misses it;
  * band sets split across two files.
It reports candidates. Every hit must be read: roughly two thirds are two
different quantities sharing a line (sensitivity vs specificity, a dose volume
vs a diluent volume, risk factors at both extremes of age).

  python3 scripts/bandcheck.py            # sweep the vault
  python3 scripts/bandcheck.py --selftest # run against cases whose answer is known
"""
import io,re,subprocess,sys,os
from decimal import Decimal
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import vaultroot

ROOT=vaultroot.root()
U=(r'(kg|g|mg|mcg|mm|cm|mL|L|mmol/L|mmol|umol/L|U/L|IU/L|IU|years?|yrs?|months?|'
   r'weeks?|days?|hours?|min|%|°C|mmHg|bpm|×10⁹/L|g/L|fL)')
TOK=re.compile(r'(?<![\w.])(?:(\d+(?:\.\d+)?)\s*[-–—−]\s*(\d+(?:\.\d+)?)'
               r'|([<≤>≥])\s*(\d+(?:\.\d+)?))\s*'+U+r'?')

def _step(s):
    return Decimal(1).scaleb(-len(s.split('.')[1])) if '.' in s else Decimal(1)

def gaps(line):
    """Return [(hi, lo)] for consecutive bands on `line` that do not meet."""
    toks=[]
    for m in TOK.finditer(line):
        u=m.group(5)
        if m.group(1):
            a,b=Decimal(m.group(1)),Decimal(m.group(2))
            if a<b: toks.append((a,b,_step(m.group(2)),u))
        else:
            v=Decimal(m.group(4)); s=_step(m.group(4))
            toks.append((None,v,s,u) if m.group(3) in '<≤' else (v,None,s,u))
    if len(toks)<2: return []
    units={t[3] for t in toks}
    if len(toks)<3 and not (len(units)==1 and None not in units): return []
    if not any(t[3] for t in toks): return []
    prev=None                       # bands must read left to right, non-overlapping
    for a,b,s,u in toks:
        lo=a if a is not None else Decimal(-10**9)
        hi=b if b is not None else Decimal(10**9)
        if prev is not None and lo<prev: return []
        prev=hi
    out=[]
    for t1,t2 in zip(toks,toks[1:]):
        if t1[1] is None or t2[0] is None: continue
        if t2[0]-t1[1]>0: out.append((t1[1],t2[0]))
    return out

def selftest():
    cases=[
      ("EZ-IO (reusable drill — 15mm needle for <39kg, 25mm needle for >40kg)",[('39','40')]),
      ("mild 5.5–5.9; moderate 6–6.4; severe ≥6.5 mmol/L",[('5.9','6'),('6.4','6.5')]),
      ("Mild 2.6–2.9; moderate 3.0–3.4; severe >3.4 mmol/L",[('2.9','3.0')]),
      ("40mg if 50–90kg; 60mg if 91–130kg; 80mg if 131–170kg",[('90','91'),('130','131')]),
      ("sensitivity of 42–53%, specificity of 80–93%",[('53','80')]),   # known FALSE POSITIVE
      ("bands 1–5 mg, 5–10 mg and 10–20 mg",[]),                        # tiles: no hit
      ("give 250 mg",[]),
    ]
    bad=0
    for text,exp in cases:
        got=[(str(a),str(b)) for a,b in gaps(text)]
        ok = got==[(str(Decimal(a)),str(Decimal(b))) for a,b in exp]
        print(('PASS ' if ok else 'FAIL ')+repr(text[:60])+'  -> '+repr(got))
        bad+= 0 if ok else 1
    print('selftest failures:',bad); return bad

def sweep():
    files=[f for f in '\n'.join(vaultroot.tracked_md_files(ROOT)).split('\n')
           if f.strip() and not f.startswith('_meta/')
           and f not in ('RUN_STATE.md','CLAUDE.md','PENDING_GUIDELINE_CHECKS.md')]
    n=0
    for f in files:
        for ln,l in enumerate(io.open(os.path.join(ROOT,f),encoding='utf-8').read().split('\n'),1):
            for hi,lo in gaps(l):
                print(f'{f}:{ln}  {hi} .. {lo} uncovered\n    {l.strip()[:190]}'); n+=1
    print('candidates:',n,'— read every one; two thirds are two quantities sharing a line.')

if __name__=='__main__':
    sys.exit(1 if ('--selftest' in sys.argv and selftest()) else (sweep() or 0))
