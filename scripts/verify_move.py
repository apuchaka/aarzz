#!/usr/bin/env python3
"""Verify that a moved block arrived intact, against the pre-move revision.

WHY THIS EXISTS. On 2026-09-01 the first verifier for the 104-section
Investigation-Interpretation move reported 4 mismatches. All four were the
verifier's own bug: it rebuilt each block by reading forward until the NEXT
HEADING OF ANY LEVEL, so any section containing subheadings (the ECG section and
its twelve, plus three others) came back truncated and compared unequal.

Loss rate was 0%. Verifier false-negative rate was 4 in 104.

That is the dangerous direction, and CLAUDE.md rule 11 already names it: "a false
MISSING during a merge verification says content was destroyed - which invites a
'restore' that re-adds a block already present, or a revert of a good merge."

THE FIX: a block ends at the next heading of the SAME OR HIGHER level, or at a
SOURCE divider. Subheadings belong to the block.

Usage:  verify_move.py <old-rev> <manifest.json>
manifest: [{"src_file","start","end","dest_file","head"}, ...] with 1-indexed
inclusive line numbers in the OLD revision.
"""
import re, sys, json, subprocess, os

def block_span(lines, start_idx, level):
    """From a heading at start_idx, return the end index (exclusive)."""
    j = start_idx + 1
    while j < len(lines):
        if lines[j].startswith('<!-- ===== SOURCE'):
            break
        m = re.match(r'^(#{1,6}) ', lines[j])
        if m and len(m.group(1)) <= level:      # SAME OR HIGHER, not any
            break
        j += 1
    return j

def extract(lines, head):
    """Every copy of `head` in `lines`, as a list of blocks (blank lines dropped)."""
    lvl_m = re.match(r'^(#{1,6}) ', head)
    out = []
    for i, l in enumerate(lines):
        if l != head:
            continue
        if lvl_m:
            j = block_span(lines, i, len(lvl_m.group(1)))
        else:                                    # a callout block
            j = i + 1
            while j < len(lines) and lines[j].lstrip().startswith('>') \
                  and not re.match(r'^\s*>\s*\[!', lines[j]):
                j += 1
        out.append([x for x in lines[i:j] if x.strip() and not x.startswith('`CF-PAIR')])
    return out

def selftest():
    """Rule 11: construct the failure this tool exists to catch, and confirm it catches it."""
    doc = ['## 0.12 ECG Interpretation', 'lead I', '### 0.12.1 P wave', 'p detail',
           '### 0.12.2 PR interval', 'pr detail', '## 0.13 Next Section', 'other']
    got = extract(doc, '## 0.12 ECG Interpretation')[0]
    want = doc[0:6]
    ok1 = got == want
    print(f"  [{'ok ' if ok1 else 'FAIL'}] a section with subheadings keeps them "
          f"({len(got)} lines, expected {len(want)})")
    # the OLD buggy rule, reproduced, to show it fails the same case
    j = 1
    while j < len(doc) and not re.match(r'^#{1,6} ', doc[j]):
        j += 1
    ok2 = doc[0:j] != want
    print(f"  [{'ok ' if ok2 else 'FAIL'}] the old stop-at-any-heading rule DOES truncate it "
          f"({j} lines) - this is the bug being guarded against")
    doc2 = ['> [!info] First callout', '> body one', '', '> [!info] Second callout', '> body two']
    got2 = extract(doc2, '> [!info] First callout')[0]
    ok3 = got2 == ['> [!info] First callout', '> body one']
    print(f"  [{'ok ' if ok3 else 'FAIL'}] a callout does not swallow the next callout")
    fails = sum(1 for x in (ok1, ok2, ok3) if not x)
    print(f"\n  self-test: {3-fails}/3 known answers correct")
    return fails

def main(oldrev, manifest_path, repo):
    man = json.load(open(manifest_path, encoding='utf-8'))
    ok = bad = 0
    for it in man:
        old = subprocess.run(['git', '-C', repo, 'show', f"{oldrev}:{it['src_file']}"],
                             capture_output=True, text=True).stdout.split('\n')
        want = [l for l in old[it['start']-1:it['end']] if l.strip()]
        now = open(os.path.join(repo, it['dest_file']), encoding='utf-8').read().split('\n')
        if any(b == want for b in extract(now, it['head'])):
            ok += 1
        else:
            bad += 1
            print(f"  !! {it['head'][:60]}  ({it['src_file']} -> {it['dest_file']})")
    print(f'blocks identical: {ok}   MISMATCH: {bad}')
    return 1 if bad else 0

if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(1 if selftest() else 0)
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main(sys.argv[1], sys.argv[2], repo))
