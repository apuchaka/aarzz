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
    """Return [(kind, a, b)] for consecutive bands on `line` that do not meet.
    kind is 'gap' (nothing covers a..b), 'point' (exactly a is in no band, from
    `<a` beside `>a`), or 'overlap' (a..b is in TWO bands)."""
    toks=[]
    for m in TOK.finditer(line):
        u=m.group(5)
        if m.group(1):
            a,b=Decimal(m.group(1)),Decimal(m.group(2))
            if a<b: toks.append((a,b,_step(m.group(2)),u,True))
        else:
            v=Decimal(m.group(4)); s=_step(m.group(4)); op=m.group(3)
            # STRICTNESS MATTERS: `<3` excludes 3 and `<=3` includes it, which is
            # the whole difference between the Listeria point-gap and a clean
            # boundary. incl says whether the named value is inside the band.
            toks.append((None,v,s,u,op in '\u2264') if op in '<\u2264'
                        else (v,None,s,u,op in '\u2265'))
    if len(toks)<2: return []
    units={tk[3] for tk in toks}
    if len(toks)<3 and not (len(units)==1 and None not in units): return []
    if not any(t[3] for t in toks): return []

    def ordered(seq):
        prev=None
        for a,b,s,u,_inc in seq:
            lo=a if a is not None else Decimal(-10**9)
            hi=b if b is not None else Decimal(10**9)
            if prev is not None and lo<prev: return False
            prev=hi
        return True
    # a band set may be written low-to-high or high-to-low (GOLD staging is
    # descending); accept either, reject anything that is neither.
    seq=toks if ordered(toks) else (toks[::-1] if ordered(toks[::-1]) else None)
    out=[]
    if seq is None:
        # not a monotone sequence — the one shape still worth reporting is an
        # OVERLAP between adjacent bands, which is how the hypokalaemia and
        # hypercalcaemia sets fail.
        seq=toks
        for t1,t2 in zip(seq,seq[1:]):
            if t1[0] is None or t2[1] is None: continue
            if None not in (t1[0],t1[1],t2[0],t2[1]):
                lo,hi=max(t1[0],t2[0]),min(t1[1],t2[1])
                if lo<hi: out.append(('overlap',lo,hi))
        return out
    for t1,t2 in zip(seq,seq[1:]):
        if t1[1] is None or t2[0] is None: continue
        d=t2[0]-t1[1]
        if d>0: out.append(('gap',t1[1],t2[0]))
    # a point boundary: `<x` beside `>x`, with nothing covering x itself
    def covers(tk,v):
        a,b,s,u,inc=tk
        if a is None: return v<b or (inc and v==b)
        if b is None: return v>a or (inc and v==a)
        return a<=v<=b
    cand={t[1] for t in toks if t[0] is None}|{t[0] for t in toks if t[1] is None}
    for v in sorted(cand):
        if any(covers(tk,v) for tk in toks): continue
        # a point already inside a reported gap adds nothing
        if any(k=='gap' and a<=v<=b for k,a,b in out): continue
        out.append(('point',v,v))
    # overlaps between adjacent bands. `lo<=hi` matters: the hypokalaemia set
    # overlaps at a single POINT (3.0 is both mild and moderate), which a
    # strict `<` misses entirely.
    # An OVERLAP is a value genuinely claimed by two bands. A shared endpoint
    # between two adjacent CLOSED ranges (`1-5 mg, 5-10 mg`) is how this corpus
    # writes abutting ranges everywhere, so it is reported as 'touch' and left
    # out of the default sweep; pass --touch to see them.
    for t1,t2 in zip(toks,toks[1:]):
        pts=[v for v in {t1[0],t1[1],t2[0],t2[1]} if v is not None]
        for v in sorted(set(pts)):
            if covers(t1,v) and covers(t2,v):
                closed=t1[0] is not None and t1[1] is not None and t2[0] is not None and t2[1] is not None
                out.append(('touch' if closed else 'overlap',v,v))
    return out


def selftest():
    cases=[
      ("EZ-IO (reusable drill — 15mm needle for <39kg, 25mm needle for >40kg)",[('gap','39','40')]),
      ("mild 5.5–5.9; moderate 6–6.4; severe ≥6.5 mmol/L",[('gap','5.9','6'),('gap','6.4','6.5')]),
      ("mild 3–3.5 mmol/L; moderate 2.5–3 mmol/L; severe ≤2.5 mmol/L",[('touch','3','3'),('overlap','2.5','2.5')]),
      ("<3 months amoxicillin, >3 months cefotaxime",[('point','3','3')]),
      (">80% Stage 1 | 50–79% Stage 2 | 30–49% Stage 3 | <30% Stage 4",[('gap','79','80'),('gap','49','50')]),
      ("Mild 2.6–2.9 mmol/L; moderate 3.0–3.4 mmol/L; severe >3.4 mmol/L",[('gap','2.9','3.0')]),
      ("40mg if 50–90kg; 60mg if 91–130kg; 80mg if 131–170kg",[('gap','90','91'),('gap','130','131')]),
      ("sensitivity of 42–53%, specificity of 80–93%",[('gap','53','80')]),   # known FALSE POSITIVE
      ("bands 1–5 mg, 5–10 mg and 10–20 mg",[('touch','5','5'),('touch','10','10')]),                        # tiles: no hit
      ("give 250 mg",[]),
    ]
    bad=0
    for text,exp in cases:
        got=[(k,str(a),str(b)) for k,a,b in gaps(text)]
        ok = sorted(got)==sorted((k,str(Decimal(a)),str(Decimal(b))) for k,a,b in exp)
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
            for kind,a,b in gaps(l):
                if kind=='touch' and '--touch' not in sys.argv: continue
                what={'gap':'uncovered','point':'in NO band (a point boundary)',
                      'overlap':'in TWO bands (an overlap)'}[kind]
                span=f'{a}' if kind=='point' else f'{a} .. {b}'
                print(f'{f}:{ln}  {span} {what}\n    {l.strip()[:190]}'); n+=1
    print('candidates:',n,'— read every one; two thirds are two quantities sharing a line.')

if __name__=='__main__':
    sys.exit(1 if ('--selftest' in sys.argv and selftest()) else (sweep() or 0))
