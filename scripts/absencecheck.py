"""Absence-claim sweep — REPORTS CANDIDATES, SETTLES NOTHING.

WHAT IT CANNOT DO, first, because a clean run here means very little. A
gap-fill note usually claims a topic was never TAUGHT, not that a word never
appeared, and the notes say so ("the teach-vs-mention check"). This script can
only test whether the words appear. Presence is therefore weak evidence and
absence of a hit is weaker: run over the whole vault it returns 63 candidates
of which almost all are a common word ("symptom", "presenting") pulled out of
an emphasised phrase.

THE PREVIOUS SWEEP WAS WORSE AND LOOKED BETTER. It matched a gap-fill note
against a same-file section with an overlapping TITLE, reported 12 candidates
and 7 genuine ones, and MISSED ALL FOUR that the second review found by
reading — PH1's NNT and p-value notes (twin titled "Measures of Effect") and
ID's pubic-lice note (twin titled "Infestations"). No shared words, no pair.

THE ONE FORM THAT IS DECISIVE, and the way to use this: a note claiming ZERO
HITS for a named term where that term now heads a SECTION somewhere else. Only
twelve notes in the corpus claim zero hits; that set is small enough to check
by hand, and doing so on 2026-09-02 found two — Communication's handover note
against `EBM1 §0.5` and its open-disclosure note against `EBM1 §0.6`.

Absence-claim sweep that TESTS THE CLAIM. Terms come from the note's own
words after 'zero hits for' / 'no mention of' / 'absent ... for', plus any
emphasised or quoted term, and are then looked for elsewhere in the vault.

Usage: python3 abssweep4.py [REV]     REV: read the tree at that git revision
"""
import io,re,os,sys,subprocess,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import vaultroot
R=vaultroot.root()+'/'
REV=sys.argv[1] if len(sys.argv)>1 else None
files=[f for f in vaultroot.tracked_md_files(R)
       if not f.startswith('_meta/') and f not in ('RUN_STATE.md','CLAUDE.md','PENDING_GUIDELINE_CHECKS.md')]
def read(f):
    if REV: return subprocess.run(['git','-C',R,'show',f'{REV}:{f}'],capture_output=True,text=True).stdout
    return io.open(R+f,encoding='utf-8').read()
text={f:read(f) for f in files}; low={f:t.lower() for f,t in text.items()}
GAP=re.compile(r'Gap-filled',re.I)
CLAIM=re.compile(r'genuinely absent|absent from|nowhere|no mention|never appear|zero hits|not covered|appeared only|completely absent',re.I)
LIST=re.compile(r'(?:zero hits|no mention|no hits|searched)\s*(?:for|of)\s+(.{5,220}?)(?:\s+[—–]|;|\.\s|$)',re.I)
EMPH=re.compile(r'\*\*?([^*]{4,40})\*\*?|"([^"]{4,40})"')
JUNK=re.compile(r'^(zero hits|genuinely absent|high|medium|low)\b',re.I)
rows=[]
for f in files:
    L=text[f].split('\n'); heads=[(i,l) for i,l in enumerate(L) if l.startswith('## ')]
    for n,l in enumerate(L):
        if not (GAP.search(l) and CLAIM.search(l)): continue
        sec=max([h for h in heads if h[0]<n], default=(0,'(file top)'))
        s_end=min([h[0] for h in heads if h[0]>n], default=len(L))
        own=('\n'.join(L[sec[0]:s_end])).lower()
        terms=set()
        flat=re.sub(r'[*_`]','',l)   # rule 2: the corpus bolds inside phrases — **zero hits** for
        for m in LIST.finditer(flat):
            for t in re.split(r',| or | and ',m.group(1)):
                t=t.strip(' .,;:*"'); 
                if 3<len(t)<45 and re.search(r'[a-z]{3}',t): terms.add(t)
        for m in EMPH.finditer(l):
            t=(m.group(1) or m.group(2)).strip(' .,;:')
            if 3<len(t)<45 and not JUNK.match(t) and re.search(r'[a-z]{3}',t): terms.add(t)
        found=[]
        for t in sorted(terms):
            tl=t.lower()   # the note's own section contains the term by construction; look OUTSIDE it
            hits=[(g,low[g].count(tl)) for g in files if g!=f and tl in low[g]]
            ext=low[f].count(tl)-own.count(tl)
            if ext>0: hits.append((f,ext))
            if hits: found.append((t,sorted(hits,key=lambda x:-x[1])[:3]))
        if found: rows.append((f,n+1,sec[1][:55],found))
print(('REV '+REV if REV else 'WORKING TREE')+' — notes asserting absence whose own named terms are present elsewhere: %d'%len(rows))
for f,n,sec,found in rows:
    print(f'--- {f}:{n}   in {sec}')
    for t,h in found: print(f'      "{t}" -> '+', '.join(f'{os.path.basename(g)}x{c}' for g,c in h))
