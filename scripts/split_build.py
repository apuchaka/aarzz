"""Cut the 18 merged system files into their proposed output files.

NOTHING MOVES. Every body line of every source lands in exactly one output file,
in its original order, byte-identical.

Each output file is:

    ---
    <frontmatter>            <- rewritten: aliases redistributed by the larger-part rule
    ---
    <optional split pointer> <- only where a SOURCE block spans >1 output file
    <!-- SPLIT-HEADER-END -->
    <verbatim source lines>

Everything at or above the sentinel is split machinery. Everything below it is
the source, unaltered. `scripts/split_verify.py` reconstructs each source from
the text below the sentinels and requires byte equality, so the sentinel is what
makes "line-for-line identical" checkable rather than asserted.
"""
import re, io, os, sys, collections, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vaultroot

ROOT = vaultroot.root()
SPEC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'split_spec.tsv')
SENTINEL = '<!-- SPLIT-HEADER-END -->'
DIV = re.compile(r'^<!-- ===== SOURCE: (.+?) ===== -->')

FOLDER = {'GI':'GI','Cardio':'Cardio','MSK':'MSK','Endo':'Endo','Paeds':'Paeds',
          'Psych':'Psych','Ophth':'Ophth','Resp':'Resp','OBGYN':'OBGYN','Emerg':'Emergency',
          'Neuro':'Neuro','HemeOnc':'HemeOnc','ID':'ID','Derm':'Derm','Renal':'Renal',
          'ENT':'ENT','Geri':'Geri','Exam':'Clinical'}


def read_lines(path):
    return io.open(path, encoding='utf-8').read().split('\n')


def frontmatter_span(lines):
    """Return (end_index_exclusive, non-alias key lines, alias list). 0 if none."""
    if not lines or lines[0] != '---':
        return 0, [], []
    for i in range(1, len(lines)):
        if lines[i] == '---':
            body = lines[1:i]
            keys, aliases, in_al = [], [], False
            for l in body:
                if re.match(r'^aliases:', l):
                    in_al = True
                    inline = l.split(':', 1)[1].strip()
                    if inline.startswith('['):
                        aliases += [x.strip().strip('"\'') for x in inline[1:-1].split(',') if x.strip()]
                    elif inline:
                        aliases.append(inline.strip('"\''))
                    continue
                if in_al:
                    if re.match(r'^\s*-\s+', l):
                        aliases.append(re.sub(r'^\s*-\s+', '', l).strip().strip('"\''))
                        continue
                    if l.strip() == '':
                        continue
                    in_al = False
                keys.append(l)
            return i + 1, keys, [a for a in aliases if a]
    return 0, [], []


def blocks_of(lines, nlines):
    """[(name, start, end)] 1-based inclusive, from SOURCE dividers."""
    divs = [(i + 1, DIV.match(l).group(1)[:-3]) for i, l in enumerate(lines) if DIV.match(l)]
    out = []
    for k, (ln, name) in enumerate(divs):
        end = divs[k + 1][0] - 1 if k + 1 < len(divs) else nlines
        out.append((name, ln, end))
    return out


def main():
    rows = [l.rstrip('\n').split('\t') for l in io.open(SPEC, encoding='utf-8') if l.strip()]
    bysrc = collections.OrderedDict()
    for s, a, b, n in rows:
        bysrc.setdefault(s, []).append([int(a), int(b), n])

    only = sys.argv[1] if len(sys.argv) > 1 else None
    manifest = {}

    for src, rs in bysrc.items():
        if only and src != only:
            continue
        path = os.path.join(ROOT, src)
        lines = read_lines(path)
        nlines = sum(1 for _ in io.open(path, encoding='utf-8'))
        rs.sort()
        # FORCED CORRECTION, reported not silent: the proposals were computed against an
        # older tree, so the final range can stop short of (or one past) real EOF.
        # The last output file runs to real EOF; no other range is touched.
        rs[-1][1] = nlines

        fm_end, keys, aliases = frontmatter_span(lines)
        blocks = blocks_of(lines, nlines)

        # --- which output files hold part of which block, and how much
        share = {}          # block name -> Counter(outfile -> lines)
        for name, bs, be in blocks:
            c = share.setdefault(name, collections.Counter())
            for a, b, n in rs:
                ov = max(0, min(be, b) - max(bs, a) + 1)
                if ov:
                    c[n] += ov

        # --- alias -> output file (larger part). Exact block-name match wins.
        alias_to = {}
        for al in aliases:
            cands = [b for b in share if b == al]
            if not cands:
                cands = [b for b in share
                         if re.match(re.escape(al) + r'[_.]', b)
                         or re.match(re.escape(al.replace('.', '-')) + r'[_-]', b)]
            if len(cands) != 1:
                raise SystemExit('FATAL: alias %r in %s matched %d blocks: %r'
                                 % (al, src, len(cands), cands))
            alias_to.setdefault(share[cands[0]].most_common(1)[0][0], []).append(al)

        # --- write
        total = len(rs)
        outs = []
        for idx, (a, b, name) in enumerate(rs):
            prefix = name.split('_', 1)[0]
            folder = FOLDER[prefix]
            os.makedirs(os.path.join(ROOT, folder), exist_ok=True)
            rel = '%s/%s.md' % (folder, name)

            body_start = max(a, fm_end + 1) if idx == 0 else a
            last = (idx == total - 1)
            # `lines` has nlines+1 elements: the final '' is the source's trailing
            # newline. The last chunk must carry it; earlier chunks must not, and
            # instead get an explicit '\n' so a chunk ending on a BLANK line does
            # not silently lose that line's newline. That is the defect the
            # byte-equality check caught on the first build: 1 byte per chunk.
            body = lines[body_start - 1:] if last else lines[body_start - 1:b]

            head = ['---']
            head += keys
            mine = alias_to.get(name, [])
            if mine:
                head.append('aliases:')
                head += ['  - "%s"' % x for x in mine]
            head.append('split_from: "%s"' % src)
            head.append('part: "%s of %s"' % (idx + 1, total))
            head.append('---')
            head.append('')

            # split pointers for every block this file shares with another file
            for bname, bs, be in blocks:
                if not (bs <= b and be >= a):
                    continue
                c = share[bname]
                if len(c) < 2:
                    continue
                order = [n for _, _, n in rs if n in c]
                pos = order.index(name)
                sibs = ' · '.join('`%s`' % o for o in order)
                owner = c.most_common(1)[0][0]
                if pos == 0:
                    lead = ('**`%s` continues below this file, into `%s`.**'
                            % (bname, order[1]))
                else:
                    lead = ('**Continues `%s` from `%s`.**' % (bname, order[pos - 1]))
                head.append('> [!note] %s' % lead)
                head.append('> That source block is split across %s.' % sibs)
                head.append('> The alias `%s` resolves to `%s`, which holds its largest part.'
                            % (bname, owner))
                head.append('')

            head.append(SENTINEL)
            io.open(os.path.join(ROOT, rel), 'w', encoding='utf-8').write(
                '\n'.join(head + body) + ('' if last else '\n'))
            outs.append({'file': rel, 'lines': [a, b], 'aliases': mine})

        manifest[src] = outs
        print('%-38s -> %2d files, %d body lines, %d aliases placed'
              % (src, len(rs), nlines - fm_end, sum(len(v) for v in alias_to.values())))

    mf = os.path.join(ROOT, '_meta', 'split_manifest.json')
    old = json.load(io.open(mf, encoding='utf-8')) if os.path.exists(mf) else {}
    old.update(manifest)
    json.dump(old, io.open(mf, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()
