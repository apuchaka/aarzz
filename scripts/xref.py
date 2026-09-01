#!/usr/bin/env python3
"""Vault-wide inbound reference index. BOTH reference forms:
   [[Code]] 0.x  wikilink  AND  `Filename.md` 0.x  backticked filename.
   Built after the wikilink-only sweep produced a false negative on the
   three NEW_* sources in GI (CLAUDE.md rule 9: a false skip is invisible)."""
import re, sys, glob, collections, os

VAULT = '/home/user/aarzz'

def sources_of(path):
    """Source files concatenated into a merged doc, with their line spans."""
    out = []
    lines = open(path, encoding='utf-8').read().split('\n')
    for n, l in enumerate(lines, 1):
        m = re.match(r'^<!-- ===== SOURCE: (.*?) ===== -->', l)
        if m:
            out.append((n, m.group(1)))
    return out, lines

def stems(srcfiles):
    """Reference tokens a source file could be cited by."""
    toks = {}
    for s in srcfiles:
        base = s[:-3] if s.endswith('.md') else s
        toks.setdefault(base, base)          # backticked full filename
        pre = base.split('_')[0]
        # wikilink prefix codes: C1, F0-3, GER8, NEW... (NEW is not a code)
        if re.fullmatch(r'[A-Z]{1,4}[0-9]{0,2}(-[0-9])?', pre) and pre != 'NEW':
            toks.setdefault(pre, base)
            if '-' in pre:                      # F0-2 is written [[F0.2]] in prose
                toks.setdefault(pre.replace('-', '.'), base)
    return toks

def index(target_merged):
    srcs, _ = sources_of(os.path.join(VAULT, target_merged))
    srcfiles = [s for _, s in srcs]
    tok = stems(srcfiles)
    # wikilink form  [[TOK]] optional §/section number
    wl = re.compile(r'\[\[(' + '|'.join(re.escape(k) for k in sorted(tok, key=len, reverse=True)) +
                    r')\]\]\s*(§?\d+\.\d+(?:\.\d+)?)?')
    # backticked filename form  `File.md` 0.x   (also bare File.md)
    bt = re.compile(r'`?(' + '|'.join(re.escape(k) for k in sorted(tok, key=len, reverse=True)) +
                    r')(?:\.md)?`?\s*(§?\d+\.\d+(?:\.\d+)?)?')
    hits = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(VAULT, '*.md'))):
        b = os.path.basename(f)
        if b in ('CLAUDE.md','RUN_STATE.md'):
            continue
        for n, l in enumerate(open(f, encoding='utf-8'), 1):
            if l.startswith('<!-- ===== SOURCE:'):
                continue
            for m in wl.finditer(l):
                hits[(tok[m.group(1)], m.group(2) or '(file-level)')].append((b, n, 'wikilink'))
            for m in bt.finditer(l):
                # only count backtick form when the token is a full filename stem
                if '_' in m.group(1):
                    hits[(tok[m.group(1)], m.group(2) or '(file-level)')].append((b, n, 'backtick'))
    return srcfiles, hits

if __name__ == '__main__':
    t = sys.argv[1]
    srcfiles, hits = index(t)
    seen = set()
    for (src, sec), rows in sorted(hits.items()):
        key = (src, sec, tuple(sorted(set((b, n) for b, n, _ in rows))))
        if key in seen:
            continue
        seen.add(key)
        uniq = sorted(set((b, n) for b, n, _ in rows))
        internal = sum(1 for b, _ in uniq if b == t)
        forms = ','.join(sorted(set(f for _, _, f in rows)))
        origins = collections.Counter(b for b, _ in uniq)
        print(f'{src} {sec}  n={len(uniq)} (internal={internal}) [{forms}]  ' +
              ', '.join(f'{k}x{v}' for k, v in origins.most_common()))
    print('\n--- SOURCES WITH ZERO INBOUND (any form) ---')
    cited = set(s for (s, _) in hits)
    for s in srcfiles:
        b = s[:-3] if s.endswith('.md') else s
        if b not in cited:
            print('  ' + b)
