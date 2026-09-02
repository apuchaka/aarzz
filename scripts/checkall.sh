#!/bin/sh
# Run every tool's self-test, then every check against the live vault.
# A check that cannot fail is worse than no check, because it reports clean
# (CLAUDE.md rule 11). So each tool proves it catches the defect it exists for,
# against a case whose answer is already known, BEFORE it is trusted on the corpus.
#
# vaultroot goes FIRST because every other check depends on it. Until 2026-09-02
# half of `scripts/` hardcoded `/home/user/aarzz` (reads the wrong tree from any
# other checkout) and the other half used `git -C ROOT ls-files` (returns nothing
# in a copy git cannot see, so the script prints a clean verdict over zero files).
set -e
cd "$(dirname "$0")/.."
fail=0
echo "=== SELF-TESTS (known answers) ==="
for t in vaultroot check_dividers verify_move reanchor bandcheck; do
  echo "--- $t"
  python3 "scripts/$t.py" --selftest || fail=1
done
echo
echo "=== LIVE VAULT ==="
echo "--- vault root in use";       python3 scripts/vaultroot.py
echo "--- SOURCE divider convention"; python3 scripts/check_dividers.py || fail=1
echo "--- dangling numeric pointers"; python3 scripts/dangling.py | head -9
echo "--- misaimed pointers";        python3 scripts/misaimed.py | tail -3
echo "--- bare internal pointers";   python3 scripts/internalrefs.py | tail -2
echo "--- internal misaimed";        python3 scripts/internal_misaimed.py | tail -2
echo "--- numbering drift";          python3 scripts/drift.py | tail -2
echo "--- band tiling";              python3 scripts/bandcheck.py | tail -1
echo "--- duplicate headers"
for f in *.md; do
  d=$(grep -h '^#\+ ' "$f" 2>/dev/null | sort | uniq -d | wc -l)
  [ "$d" -gt 0 ] && printf '    %-38s %s duplicate heading texts\n' "$f" "$d"
done
exit $fail
