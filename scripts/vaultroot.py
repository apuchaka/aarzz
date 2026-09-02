#!/usr/bin/env python3
"""The vault root, resolved from the script's own location — and a HARD GUARD
that refuses to hand back an empty file list.

WHY THIS EXISTS. Two failure modes were live in `scripts/` until 2026-09-02,
one in each half of it, and both produced a clean verdict rather than an error:

  1. `VAULT='/home/user/aarzz'` hardcoded (dangling, drift, misaimed, sections,
     xref). Run inside any other checkout — a worktree, an extracted baseline,
     a clone on another machine — they silently read the LIVE vault and report
     on the wrong tree. A "before vs after" comparison run that way measures the
     same tree twice and always agrees.

  2. `git -C ROOT ls-files` (positional, internalrefs, internal_misaimed,
     aftermove, bandcheck). Run inside a copy git cannot see, `ls-files` returns
     NOTHING, the loop body never executes, and the script prints
     "0 references pointing the wrong way" — over zero files.

Both are CLAUDE.md rule 11's case: a check that cannot fail is worse than no
check, because it reports clean and the report goes into a commit message.

  root()                 the vault root; $VAULT overrides for a deliberate
                         cross-tree run
  md_files()             every *.md at the root, tracked or not; EXITS 2 if the
                         list is empty, and prints where it looked
  tracked_md_files()     git-tracked *.md, falling back to md_files() when the
                         root is not a git checkout — never to an empty list

  python3 scripts/vaultroot.py --selftest
"""
import os, sys, glob, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def root():
    return os.environ.get('VAULT') or ROOT


def _guard(paths, where, what):
    if not paths:
        sys.stderr.write(
            'FATAL: %s found 0 %s under %r.\n'
            'Refusing to print a verdict over an empty file list — see '
            'scripts/vaultroot.py.\n' % (os.path.basename(sys.argv[0]), what, where))
        sys.exit(2)
    return paths


def md_files(vault=None, pattern='*.md'):
    v = vault or root()
    return _guard(sorted(glob.glob(os.path.join(v, pattern))), v, 'markdown files')


def tracked_md_files(vault=None, pattern='*.md'):
    """git-tracked paths RELATIVE to the root. Falls back to a filesystem glob
    when the root is not the top of a git checkout, so a non-git copy is read
    correctly instead of silently coming back empty."""
    v = vault or root()
    top = subprocess.run(['git', '-C', v, 'rev-parse', '--show-toplevel'],
                         capture_output=True, text=True).stdout.strip()
    if top and os.path.realpath(top) == os.path.realpath(v):
        out = subprocess.run(['git', '-C', v, 'ls-files', pattern],
                             capture_output=True, text=True).stdout
        return _guard([f for f in out.split('\n') if f.strip()], v, 'tracked markdown files')
    return _guard([os.path.relpath(p, v) for p in sorted(glob.glob(os.path.join(v, '**', pattern), recursive=True))],
                  v, 'markdown files (not a git checkout, globbed instead)')


def _selftest():
    bad = 0
    r = root()
    ok = os.path.isdir(os.path.join(r, 'scripts'))
    print(('[ok ] ' if ok else '[FAIL] ') + 'root() resolves from __file__, not a literal: %r' % r); bad += 0 if ok else 1

    n = len(md_files())
    ok = n > 10
    print(('[ok ] ' if ok else '[FAIL] ') + 'md_files() finds the vault: %d files' % n); bad += 0 if ok else 1

    t = len(tracked_md_files())
    ok = t > 10
    print(('[ok ] ' if ok else '[FAIL] ') + 'tracked_md_files() finds the vault: %d files' % t); bad += 0 if ok else 1

    # the guard itself, against a directory whose answer is known: it has no .md
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = subprocess.run([sys.executable, '-c',
                            'import sys;sys.path.insert(0,%r);import vaultroot;'
                            'vaultroot.md_files(%r);print("VERDICT: clean")'
                            % (os.path.dirname(os.path.abspath(__file__)), d)],
                           capture_output=True, text=True)
        ok = p.returncode == 2 and 'VERDICT' not in p.stdout
        print(('[ok ] ' if ok else '[FAIL] ') +
              'empty directory -> exit %d, no verdict printed' % p.returncode)
        if not ok: print('        stdout was: %r' % p.stdout)
        bad += 0 if ok else 1

        p = subprocess.run([sys.executable, '-c',
                            'import sys;sys.path.insert(0,%r);import vaultroot;'
                            'vaultroot.tracked_md_files(%r);print("VERDICT: clean")'
                            % (os.path.dirname(os.path.abspath(__file__)), d)],
                           capture_output=True, text=True)
        ok = p.returncode == 2 and 'VERDICT' not in p.stdout
        print(('[ok ] ' if ok else '[FAIL] ') +
              'empty non-git directory -> exit %d, no verdict printed' % p.returncode)
        bad += 0 if ok else 1

    print('\nself-test failures: %d' % bad)
    return bad


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(1 if _selftest() else 0)
    print(root())
