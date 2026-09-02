"""Is a CF-PAIR marker still in the same file as the account it names?

A CF-PAIR marker says "a second full account of this topic exists, here".
Cutting a file can put the marker and the account it names in different output
files, leaving a pointer that no longer resolves for someone reading top to
bottom. Chat B refused to split History-Taking.md on exactly this argument; the
argument is about the shape of the marker, not about that file, so it has to be
run everywhere.

What counts as a target, in order of confidence:
  * a quoted heading title in backticks   -> must be a heading in this file
  * a bare or qualified section number    -> must be a heading in this file
  * the literal claim "in this file"      -> at least one named target must be
Anything the marker names by [[wikilink]] is deliberately cross-file and is not
counted; so is a target quoted from a file the marker itself names.

Rule 11: --selftest builds a marker whose answer is known, in both directions.
"""
import re, io, os, sys, collections, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vaultroot

MARK = re.compile(r'`CF-PAIR\b')
SEC = re.compile(r'§\s*(\d+(?:\.\d+)+)')
TICK = re.compile(r'`([^`]+)`')


def norm(s):
    s = s.replace('’', "'").replace('—', '-').replace('–', '-')
    s = re.sub(r'[*`_]', '', s)
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def headings(text):
    """normalised heading text -> present, plus the set of section numbers."""
    titles, nums = set(), set()
    for l in text.split('\n'):
        m = re.match(r'^#{1,6}\s+(.*?)\s*$', l)
        if not m:
            continue
        raw = m.group(1)
        titles.add(norm(raw))
        titles.add(norm(re.sub(r'^\d+(\.\d+)*[a-z]?\s+', '', raw)))
        mn = re.match(r'^(\d+(?:\.\d+)+)', raw)
        if mn:
            nums.add(mn.group(1))
    return titles, nums


def marker_block(lines, i):
    """A marker's text: its own line, plus the rest of its > callout."""
    out = [lines[i]]
    if lines[i].lstrip().startswith('>'):
        j = i + 1
        while j < len(lines) and lines[j].lstrip().startswith('>'):
            out.append(lines[j]); j += 1
    return ' '.join(out)


OTHER_FILES = set()


def load_names():
    """Every file basename, and every unique short prefix of one, so a reference
    written `Exam_01 §1.2` or `NEW_Drugs_10 §0.5.4` counts as naming its file."""
    import collections as _c
    names, pref = set(), _c.Counter()
    for p in vaultroot.md_files():
        b = os.path.basename(p)[:-3]
        names.add(b)
        parts = b.split('_')
        for k in range(1, len(parts)):
            pref['_'.join(parts[:k])] += 1
    for k, v in pref.items():
        if v == 1 and len(k) >= 4:
            names.add(k)
    return names


LOC = re.compile(r'\b(in this file|in this same file|in the same file|earlier in this'
                 r'|later in this|directly below|directly above|just above|just below)\b', re.I)


def scan(path, text):
    """Flag a marker only where it ASSERTS a location the target no longer has.

    Two shapes count, and nothing else does:
      * the marker makes a locational claim - "in this file", "earlier in this
        same file", "directly below" - and a target it names is not in the file;
      * the marker carries a section number that is neither resolvable here nor
        qualified by a file or source-block name, so a reader cannot follow it.
    A marker that simply NAMES another file or block is a normal cross-reference,
    not a separated marker, and is not a defect. That distinction is the whole
    point: naming the file is the fix, so a checker that still flags it would
    report the repair as the fault.
    """
    titles, nums = headings(text)
    lines = text.split('\n')
    out = []
    for i, l in enumerate(lines):
        if not MARK.search(l):
            continue
        blk = marker_block(lines, i)
        missing = []
        for m in SEC.finditer(blk):
            n = m.group(1)
            if n in nums:
                continue
            seg = blk[:m.start()]
            tick = seg.rfind('`')
            seg = seg[tick + 1:] if (tick != -1 and blk.count('`', 0, m.start()) % 2 == 1) \
                else seg[-25:]
            if re.search(r'\[\[[^\]|#]+\]\][^`§]{0,10}?$', seg):
                continue
            if any(nm in seg for nm in OTHER_FILES):
                continue
            missing.append('unqualified §' + n)
        if LOC.search(blk):
            claimed = []
            for tk in TICK.findall(blk):
                if tk.startswith('CF-PAIR') or '[[' in tk:
                    continue
                body = re.sub(r'\s*§\s*\d+(\.\d+)*', '', tk)
                body = re.sub(r'^[A-Za-z0-9_.\-]+\s+##?#?\s*', '', body)
                nt = norm(body)
                if len(nt) >= 12 and ' ' in nt and nt not in titles:
                    claimed.append(repr(tk[:60]))
            if claimed:
                missing.append('locational claim %r, but: %s'
                               % (LOC.search(blk).group(0), ', '.join(claimed)))
        if missing:
            out.append((i + 1, missing, l.strip()[:110]))
    return out


def selftest():
    good = ("## 0.1 Alpha\n\n`CF-PAIR` **See §0.2 and `Beta Heading Here`.**\n\n"
            "## 0.2 Beta Heading Here\ntext\n")
    bad = ("## 0.1 Alpha\n\n`CF-PAIR` **See §0.2 and `Beta Heading Here` in this file.**\n")
    ok = True
    r = scan('x', good)
    print('  [%s] a marker whose targets are in the file is silent: %r'
          % ('ok ' if not r else 'FAIL', r)); ok &= not r
    r = scan('x', bad)
    print('  [%s] a marker whose targets are gone is caught: %r'
          % ('ok ' if r else 'FAIL', [x[1] for x in r])); ok &= bool(r)
    nolo = ("## 0.1 Alpha\n\n`CF-PAIR` **The other account is `Beta Heading Here`, elsewhere.**\n")
    r = scan('x', nolo)
    print('  [%s] a cross-reference with NO locational claim is not a defect: %r'
          % ('ok ' if not r else 'FAIL', r)); ok &= not r
    OTHER_FILES.add('Exam_01')
    named = "## 0.1 Alpha\n\n`CF-PAIR Exam_01 \u00a71.2` **See `Exam_01 \u00a71.2 Vital Signs`.**\n"
    r = scan('x', named)
    print('  [%s] a cross-file reference that NAMES its file is not a defect: %r'
          % ('ok ' if not r else 'FAIL', r)); ok &= not r
    OTHER_FILES.discard('Exam_01')
    return ok


def main():
    if '--selftest' in sys.argv:
        print('=== cfpair.py self-test ===')
        sys.exit(0 if selftest() else 1)
    print('=== cfpair.py ===  (self-test first, per CLAUDE.md rule 11)')
    if not selftest():
        print('SELF-TEST FAILED'); sys.exit(1)
    print()
    root = vaultroot.root()
    OTHER_FILES.update(load_names())
    per = collections.Counter(); tot = 0; markers = 0
    for p in vaultroot.md_files(root):
        rel = os.path.relpath(p, root)
        if os.path.basename(rel) in ('CLAUDE.md', 'RUN_STATE.md', 'STUDY_INDEX.md'):
            continue
        text = io.open(p, encoding='utf-8').read()
        markers += len(MARK.findall(text))
        r = scan(rel, text)
        if r:
            per[rel] = len(r); tot += len(r)
            if '-v' in sys.argv:
                for ln, miss, ctx in r:
                    print('  %s:%d  %s\n      %s' % (rel, ln, ', '.join(miss), ctx))
    print('%d CF-PAIR markers examined' % markers)
    for f, n in per.most_common():
        print('  %-64s %d' % (f, n))
    print('\n%d CF-PAIR marker(s) naming a target that is not in their own file' % tot)
    return tot


if __name__ == '__main__':
    main()
