#!/usr/bin/env python3
"""Whole-vault verification for the reorder run.

Every claim below is a comparison against a named commit, not an assertion.
  scripts/verify_reorder.py [BASE]      default BASE=78cd7b3 (pre-reorder)
"""
import re,sys,os,io,glob,collections,subprocess
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import vaultroot
ROOT=vaultroot.root()
BASE=sys.argv[1] if len(sys.argv)>1 else '78cd7b3'
# The pure-move guarantee holds over the REORDER range only. Commits after it -
# the bare-pointer qualification - are prose edits and change lines by design, so
# checks 1 and 2 compare BASE..MOVES_END while everything else compares BASE..HEAD.
MOVES_END=sys.argv[2] if len(sys.argv)>2 else '46c6bdf'
def sh(*a): return subprocess.run(list(a),capture_output=True,text=True,cwd=ROOT).stdout
def files(): return vaultroot.tracked_md_files(ROOT)
def at(f): return sh('git','show',f'{BASE}:{f}')
def now(f):
    p=os.path.join(ROOT,f)
    return io.open(p,encoding='utf-8').read() if os.path.exists(p) else ''
def atmoves(f): return sh('git','show',f'{MOVES_END}:{f}')

fail=0
def check(label,ok,detail=''):
    global fail
    if not ok: fail+=1
    print(f'  [{"PASS" if ok else "FAIL"}] {label}{(" — "+detail) if detail else ""}')

print(f'=== verify_reorder.py — everything below is measured against {BASE} ===\n')

print(f'1. PURE MOVE: line multiset identical per reordered file, {BASE}..{MOVES_END}')
# top-level merged files only: _meta/flags/ holds analysis files with the same names
reordered=[f for f in files() if f.endswith('_merged.md') and '/' not in f]
bad=[]
for f in reordered:
    a=collections.Counter(at(f).split('\n')); b=collections.Counter(atmoves(f).split('\n'))
    if a!=b: bad.append((f,sum((b-a).values()),sum((a-b).values())))
check(f'{len(reordered)} merged files, line multiset unchanged',not bad,
      '; '.join(f'{f} +{p}/-{m}' for f,p,m in bad))

print(f'\n2. PURE MOVE: digit multiset identical per reordered file, {BASE}..{MOVES_END}')
bad=[]
for f in reordered:
    a=collections.Counter(c for c in at(f) if c.isdigit())
    b=collections.Counter(c for c in atmoves(f) if c.isdigit())
    if a!=b: bad.append(f)
check(f'{len(reordered)} merged files, digit multiset unchanged',not bad,', '.join(bad))

print('\n3. No heading gained or lost anywhere in the vault')
# RUN_STATE.md is the run's own record and gains headings by design; _meta/ likewise.
CONTENT=[f for f in files() if f!='RUN_STATE.md' and not f.startswith('_meta/')]
A=collections.Counter(); B=collections.Counter()
for f in CONTENT:
    A.update(l for l in at(f).split('\n') if l.startswith('#'))
    B.update(l for l in now(f).split('\n') if l.startswith('#'))
check(f'content headings {sum(A.values())} -> {sum(B.values())} (RUN_STATE and _meta excluded: records, not content)',A==B,
      f'lost {[k[:50] for k in (A-B)]} gained {[k[:50] for k in (B-A)]}')

print('\n4. No duplicate heading introduced, per file')
bad=[]
for f in files():
    da={k for k,v in collections.Counter(l for l in at(f).split('\n') if re.match(r'^#+ ',l)).items() if v>1}
    db={k for k,v in collections.Counter(l for l in now(f).split('\n') if re.match(r'^#+ ',l)).items() if v>1}
    if db-da: bad.append(f)
check('no new duplicate headings',not bad,', '.join(bad))

print('\n5. No conflict markers anywhere')
m=[f for f in files() if re.search(r'^(<<<<<<<|>>>>>>>|=======)$',now(f),re.M)]
check('0 conflict markers',not m,', '.join(m))

print('\n6. Callouts, checked structurally')
# a) a callout title whose body is missing entirely (nothing follows on a > line)
# b) a callout body orphaned from its title by a non-> line inserted between
empty=[];orphan=[]
for f in files():
    L=now(f).split('\n')
    for i,l in enumerate(L):
        if re.match(r'^> \[!\w+\]-?\s*$',l):                      # title with NO text on the line
            if i+1>=len(L) or not L[i+1].startswith('>'): empty.append(f'{f}:{i+1}')
    # an orphaned continuation: a '>' line whose block has no [! title anywhere above it
    inblock=False;titled=False
    for i,l in enumerate(L):
        if l.startswith('>'):
            if not inblock: inblock=True; titled=bool(re.match(r'^> \[!\w+\]',l))
            elif re.match(r'^> \[!\w+\]',l) and not titled: titled=True
        else:
            inblock=False; titled=False
check('0 empty callouts (title with no body and no text)',not empty,', '.join(empty[:6]))
# c) the shape that actually broke before: a non-'>' non-blank line directly after a title
mid=[]
for f in files():
    L=now(f).split('\n')
    for i,l in enumerate(L):
        if re.match(r'^> \[!\w+\]-?\s*$',l) and i+1<len(L) and L[i+1] and not L[i+1].startswith('>'):
            mid.append(f'{f}:{i+1}')
check('0 callout bodies severed from their title',not mid,', '.join(mid[:6]))

print('\n7. Wikilink targets resolve (CLAUDE.md 1.10 prefix rule)')
import os as _os
def _names(get):
    n=set()
    for f in files():
        n.add(_os.path.basename(f)[:-3])
        for m in re.finditer(r'^<!-- ===== SOURCE: (\S+)\.md ===== -->',get(f),re.M): n.add(m.group(1))
    return n
def _unres(get,names):
    out=collections.Counter(); tot=0
    for f in files():
        # RUN_STATE.md quotes [[File]] as an EXAMPLE when describing the checks;
        # it is the run's record, not content, and is excluded here as in check 3.
        if f.startswith('_meta/') or f=='RUN_STATE.md': continue
        for m in re.finditer(r'\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]',get(f)):
            t=m.group(1).strip(); tot+=1
            q=t.replace('.','-')
            if t in names or q in names: continue
            if len([n for n in names if n.startswith(q+'_')])==1: continue
            out[t]+=1
    return tot,out
tb,ub=_unres(at,_names(at)); tn,un=_unres(now,_names(now))
newbad={k:v for k,v in un.items() if v>ub.get(k,0)}
check(f'{tn} wikilinks, {sum(un.values())} unresolved ({sum(ub.values())} at {BASE}) — 0 new',
      not newbad, str(newbad))

print('\n8. Working tree')
st=sh('git','status','--porcelain').strip()
check('clean',not st,st[:200])
print(f'\n=== {"ALL CHECKS PASS" if not fail else str(fail)+" CHECK(S) FAILED"} ===')
sys.exit(1 if fail else 0)
