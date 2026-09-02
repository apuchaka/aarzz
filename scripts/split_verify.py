"""Reconstruct each split source from its output files and require byte equality.

Everything at or above `<!-- SPLIT-HEADER-END -->` in an output file is split
machinery (frontmatter, split pointer). Everything below it must be the source,
verbatim, in order. This script concatenates the below-sentinel text of a
source's output files in spec order and compares it byte-for-byte with the
source's body as recorded in _meta/split_baseline/.

Rule 11: `--selftest` builds a case whose answer is already known — a dropped
line, a reordered pair, a changed character — and requires the check to fail on
each. A check that cannot fail is worse than no check.
"""
import io, os, sys, json, hashlib, tempfile, shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vaultroot

SENTINEL = '<!-- SPLIT-HEADER-END -->'


def below_sentinel(path):
    t = io.open(path, encoding='utf-8').read()
    i = t.find(SENTINEL)
    if i == -1:
        raise ValueError('no sentinel in %s' % path)
    return t[i + len(SENTINEL) + 1:]          # skip the sentinel's own newline


def check(root, src, outs, baseline_dir):
    got = ''.join(below_sentinel(os.path.join(root, o['file'])) for o in outs)
    want = io.open(os.path.join(baseline_dir, src.replace('/', '_') + '.body'),
                   encoding='utf-8').read()
    return got == want, hashlib.sha256(got.encode()).hexdigest()[:12], \
        hashlib.sha256(want.encode()).hexdigest()[:12], len(got), len(want)


def selftest():
    d = tempfile.mkdtemp()
    try:
        base = os.path.join(d, 'base'); os.makedirs(base)
        io.open(os.path.join(base, 'S.md.body'), 'w', encoding='utf-8').write('a\nb\nc\nd\n')
        def mk(name, text):
            p = os.path.join(d, name)
            io.open(p, 'w', encoding='utf-8').write('---\nx: 1\n---\n\n' + SENTINEL + '\n' + text)
        cases = {
            'identical':      [('1.md', 'a\nb\n'), ('2.md', 'c\nd\n')],
            'dropped line':   [('1.md', 'a\n'),    ('2.md', 'c\nd\n')],
            'reordered':      [('1.md', 'b\na\n'), ('2.md', 'c\nd\n')],
            'changed char':   [('1.md', 'a\nb\n'), ('2.md', 'c\nD\n')],
            'duplicated':     [('1.md', 'a\nb\n'), ('2.md', 'b\nc\nd\n')],
        }
        ok = True
        for label, files in cases.items():
            for n, t in files:
                mk(n, t)
            outs = [{'file': n} for n, _ in files]
            same, g, w, lg, lw = check(d, 'S.md', outs, base)
            want_same = (label == 'identical')
            good = (same == want_same)
            ok &= good
            print('  selftest %-14s expected %-5s got %-5s  %s'
                  % (label, want_same, same, 'PASS' if good else '*** FAIL ***'))
        return ok
    finally:
        shutil.rmtree(d)


def main():
    if '--selftest' in sys.argv:
        print('split_verify selftest (rule 11 — run it where the answer is known):')
        sys.exit(0 if selftest() else 1)
    root = vaultroot.root()
    manifest = json.load(io.open(os.path.join(root, '_meta', 'split_manifest.json'), encoding='utf-8'))
    baseline = os.path.join(root, '_meta', 'split_baseline')
    if not manifest:
        sys.stderr.write('FATAL: empty manifest, refusing to print a verdict.\n'); sys.exit(2)
    bad = 0
    for src, outs in sorted(manifest.items()):
        same, g, w, lg, lw = check(root, src, outs, baseline)
        print('%-38s %-8s got %s (%d B)  want %s (%d B)'
              % (src, 'IDENTICAL' if same else '*** DIFFERS ***', g, lg, w, lw))
        bad += 0 if same else 1
    print('\n%d of %d sources reconstruct byte-identically.' % (len(manifest) - bad, len(manifest)))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
