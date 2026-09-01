#!/usr/bin/env python3
"""Per-source-file numbering-trust report.

   Four independent signals that a file's section numbers have drifted:
     FINGERPRINT  a heading carrying TWO numbers ('## 0.23 0.22a RHD') - the
                  direct trace of an insert-and-renumber
     GAP          a break in the top-level 0.N sequence
     DUP          the same section number twice in one source
     DANGLING     inbound pointers to a number that does not exist
     MISNAMED     inbound pointers whose number exists but names another section

   A file with none of these is not proven clean - only 0.9% of numeric pointers
   carry a name, so MISNAMED can only ever see a sliver. Absence of signal is
   weak evidence; presence of signal is strong."""
import re, glob, os, collections, sys
V='/home/user/aarzz'
heads=collections.defaultdict(dict); order=collections.defaultdict(list)
fingerprint=collections.defaultdict(list); c2s={}; owner={}
for f in sorted(glob.glob(os.path.join(V,'*.md'))):
    b=os.path.basename(f)
    if b in ('CLAUDE.md','RUN_STATE.md'): continue
    cur=b[:-3]; owner[cur]=b
    for n,l in enumerate(open(f,encoding='utf-8'),1):
        m=re.match(r'^<!-- ===== SOURCE: (.*?) ===== -->',l)
        if m:
            cur=m.group(1)[:-3]; owner[cur]=b
            pre=cur.split('_')[0]
            if re.fullmatch(r'[A-Z]{1,4}[0-9]{0,2}(-[0-9])?',pre) and pre!='NEW': c2s[pre]=cur
            c2s[cur]=cur; continue
        h=re.match(r'^#{1,6} (\d+\.\d+(?:\.\d+)?)\s+(.*)',l)
        if h:
            # NEW_Drugs_07 is concatenated into TWO merged docs; without this guard
            # its headings are counted twice and read as duplicate section numbers.
            if h.group(1) in heads[cur] and heads[cur][h.group(1)]==h.group(2).strip():
                continue
            heads[cur][h.group(1)]=h.group(2).strip(); order[cur].append(h.group(1))
            if re.match(r'^\d+\.\d+[a-z]?\b', h.group(2)):      # a second number in the title
                fingerprint[cur].append((n,l.strip()[:80]))
    pre=b[:-3].split('_')[0]
    if re.fullmatch(r'[A-Z]{1,4}[0-9]{0,2}(-[0-9])?',pre) and pre!='NEW': c2s.setdefault(pre,b[:-3])
    c2s.setdefault(b[:-3],b[:-3]); owner.setdefault(b[:-3],b)
alt='|'.join(re.escape(t) for t in sorted(c2s,key=len,reverse=True))
PTR=re.compile(r'(?:\[\[|`)('+alt+r')(?:\.md)?(?:\]\]|`)\s*(?:§|section|sections|part|chapter|item)?\s*(\d+\.\d+(?:\.\d+)?)(\s+[A-Z][A-Za-z\'()\-]*(?:\s+[A-Za-z\'()\-/]+){0,4})?')
STOP={'for','the','and','see','not','a','of','in','to','with'}
W=lambda s:{w.lower().strip("'()/-") for w in re.findall(r"[A-Za-z']+",s or '')}-STOP
dang=collections.Counter(); mis=collections.Counter()
for f in sorted(glob.glob(os.path.join(V,'*.md'))):
    b=os.path.basename(f)
    if b in ('CLAUDE.md','RUN_STATE.md'): continue
    for l in open(f,encoding='utf-8'):
        if l.startswith('<!-- ===== SOURCE:'): continue
        for m in PTR.finditer(l):
            s=c2s[m.group(1)]; sec=m.group(2)
            if s not in heads: continue
            if sec not in heads[s]: dang[s]+=1; continue
            nw=W(m.group(3))
            if nw and not (nw & W(heads[s][sec])): mis[s]+=1
rows=[]
for s in sorted(heads):
    tops=[x for x in order[s] if x.count('.')==1]
    seq=[]
    for x in tops:
        try: seq.append(int(x.split('.')[1]))
        except ValueError: pass
    gaps=[]; dups=[]
    seen=set()
    for i,v in enumerate(seq):
        if v in seen: dups.append(v)
        seen.add(v)
        if i and v not in (seq[i-1], seq[i-1]+1): gaps.append(f'{seq[i-1]}->{v}')
    fp=len(fingerprint[s])
    score=fp*3+len(dups)*2+len(gaps)+dang[s]*2+mis[s]*3
    if score: rows.append((score,s,owner[s],fp,gaps,dups,dang[s],mis[s]))
rows.sort(reverse=True)
print(f'{"source":<52}{"fp":>3}{"dup":>4}{"gap":>4}{"dang":>5}{"misnm":>6}')
print('-'*76)
for sc,s,o,fp,gaps,dups,d,m in rows:
    print(f'{s[:51]:<52}{fp:>3}{len(dups):>4}{len(gaps):>4}{d:>5}{m:>6}')
    if fp:   print(f'      FINGERPRINT: ' + ' | '.join(x[1] for x in fingerprint[s][:3]))
    if gaps: print(f'      GAPS: ' + ', '.join(gaps[:8]))
    if dups: print(f'      DUPS: ' + ', '.join(str(x) for x in dups[:8]))
print(f'\n{len(heads)-len(rows)} of {len(heads)} sources show NO drift signal.')
