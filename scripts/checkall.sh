#!/bin/sh
# Run every tool's self-test, then every check against the live vault.
# A check that cannot fail is worse than no check, because it reports clean
# (CLAUDE.md rule 11). So each tool proves it catches the defect it exists for,
# against a case whose answer is already known, BEFORE it is trusted on the corpus.
set -e
cd "$(dirname "$0")/.."
fail=0
echo "=== SELF-TESTS (known answers) ==="
for t in check_dividers verify_move reanchor; do
  echo "--- $t"
  python3 "scripts/$t.py" --selftest || fail=1
done
echo
echo "=== LIVE VAULT ==="
echo "--- SOURCE divider convention"; python3 scripts/check_dividers.py || fail=1
echo "--- dangling numeric pointers"; python3 scripts/dangling.py | head -6
echo "--- misaimed pointers";        python3 scripts/misaimed.py | tail -3
echo "--- duplicate headers"
for f in *.md; do
  d=$(grep -h '^#\+ ' "$f" 2>/dev/null | sort | uniq -d | wc -l)
  [ "$d" -gt 0 ] && printf '    %-38s %s duplicate heading texts\n' "$f" "$d"
done
exit $fail
