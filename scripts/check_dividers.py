#!/usr/bin/env python3
"""Enforce the SOURCE-divider convention.

WHY THIS EXISTS. On 2026-09-01 the Investigation-Interpretation merge wrote its
dividers as

    <!-- ===== SOURCE: J3_Bleeding_and_Thrombosis.md  (moved from Heme Onc_merged.md, 2026-09-01) ===== -->

which *looks* like the convention. `dangling.py` parses `SOURCE: (.*?) =====` and
took the whole string as the filename, so every section under that divider was
registered under a key nothing points at: **60 pointers reported broken. None was.**

A format that merely resembles the convention is enough to make a checker report
catastrophe. So the convention is now checked mechanically instead of remembered.

THE CONVENTION: the divider line is exactly

    <!-- ===== SOURCE: <filename>.md ===== -->

Nothing else on the line. Provenance notes go on the FOLLOWING line, as italics.

Exit 1 if any divider in the vault deviates.
"""
import re, sys, glob, os
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import vaultroot

GOOD = re.compile(r'^<!-- ===== SOURCE: [^\s<>|]+\.md ===== -->$')
ANY  = re.compile(r'<!-- =+ SOURCE:')

def check(paths):
    bad = []
    total = 0
    for p in paths:
        for n, l in enumerate(open(p, encoding='utf-8').read().split('\n'), 1):
            if not ANY.search(l):
                continue
            total += 1
            if not GOOD.match(l):
                bad.append((os.path.basename(p), n, l))
    return total, bad

def selftest():
    """Rule 11: run the check against cases whose answer is already known."""
    import tempfile
    cases = [
        ("<!-- ===== SOURCE: N4_Mood_Disorders.md ===== -->", True),
        ("<!-- ===== SOURCE: F0-2_Acid-Base__DKA_and_Fluid_States.md ===== -->", True),
        # the exact string that caused the 60 false positives:
        ("<!-- ===== SOURCE: J3_Bleeding.md  (moved from Heme Onc_merged.md, 2026-09-01) ===== -->", False),
        ("<!-- ===== SOURCE: NoExtension ===== -->", False),
        ("<!-- ===== SOURCE:N4_Mood_Disorders.md ===== -->", False),
        ("<!-- ===== SOURCE: N4_Mood_Disorders.md ===== --> trailing", False),
    ]
    fails = 0
    for text, should_pass in cases:
        got = bool(GOOD.match(text))
        mark = "ok " if got == should_pass else "FAIL"
        if got != should_pass:
            fails += 1
        print(f"  [{mark}] expect {'PASS' if should_pass else 'REJECT'}: {text[:78]}")
    print(f"\n  self-test: {len(cases)-fails}/{len(cases)} known answers correct")
    return fails

if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(1 if selftest() else 0)
    vault = sys.argv[1] if len(sys.argv) > 1 else vaultroot.root()
    total, bad = check(vaultroot.md_files(vault))
    print(f'SOURCE dividers checked: {total}')
    if bad:
        print(f'DEVIATING FROM THE CONVENTION: {len(bad)}')
        for f, n, l in bad:
            print(f'  {f}:{n}  {l[:110]}')
        sys.exit(1)
    print('all match the convention')
