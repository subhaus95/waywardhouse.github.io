#!/usr/bin/env python3
"""
qa-posts.py — Post-build QA for waywardhouse Jekyll posts.

Checks every .md file in _posts/ for known rendering gotchas:

  1. MATH_DOLLAR   — math: true post has bare $digit in prose (KaTeX renders it as math)
  2. INVALID_JSON  — data-options='...' attribute contains invalid JSON
  3. NO_HEIGHT     — <div data-viz="echarts"> missing style="height:..."
  4. VIZ_NO_TAG    — post has data-viz elements but no tag-hash-viz / viz: true
  5. APOS_IN_ATTR  — data-options='...' contains an apostrophe (breaks HTML attribute)
  6. DATE_URL      — link contains date-format path /YYYY/MM/DD/slug/ (site uses /:title/)
  7. STORY_NO_TAG  — post has .story-section but no tag-hash-story in tags
  8. LEAFLET_MARKER_APOS — data-markers='...' contains apostrophe (breaks HTML attribute)

Usage:
  python3 scripts/qa-posts.py            # check all posts, exit 1 if any issues
  python3 scripts/qa-posts.py --fix      # auto-fix safe issues (MATH_DOLLAR only)
  python3 scripts/qa-posts.py --changed  # only check files changed in git (CI mode)

Exit code: 0 = clean, 1 = issues found (fails CI).
"""

import sys, os, re, json, html, argparse, subprocess

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')

# ── Helpers ───────────────────────────────────────────────────────────────────

def extract_data_options(content):
    """Yield (char_offset, raw_json_string) for each data-options='...' attribute."""
    for m in re.finditer(r"data-options='", content):
        start = m.end()
        raw = []
        j = start
        while j < len(content):
            if content[j] == "'":
                break
            raw.append(content[j])
            j += 1
        yield m.start(), ''.join(raw)


def extract_data_markers(content):
    """Yield (char_offset, raw_json_string) for each data-markers='...' attribute."""
    for m in re.finditer(r"data-markers='", content):
        start = m.end()
        raw = []
        j = start
        while j < len(content):
            if content[j] == "'":
                break
            raw.append(content[j])
            j += 1
        yield m.start(), ''.join(raw)


def is_prose_line(line):
    """True if a line is prose text (not a raw HTML data-options line)."""
    stripped = line.strip()
    return not (
        stripped.startswith('<div data-viz=') or
        stripped.startswith('<p class="viz-caption') or
        stripped.startswith('<div data-leaflet') or
        stripped.startswith('<div class="story-step"') or
        stripped.startswith('data-update=')
    )


def get_changed_files():
    """Return list of _posts/*.md files changed in the last commit or unstaged."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'],
            capture_output=True, text=True, cwd=os.path.dirname(POSTS_DIR)
        )
        changed = result.stdout.strip().split('\n')
        # Also include unstaged changes
        result2 = subprocess.run(
            ['git', 'diff', '--name-only'],
            capture_output=True, text=True, cwd=os.path.dirname(POSTS_DIR)
        )
        changed += result2.stdout.strip().split('\n')
        return [f for f in set(changed) if f.startswith('_posts/') and f.endswith('.md')]
    except Exception:
        return []


# ── Checks ────────────────────────────────────────────────────────────────────

def check_math_dollar(fname, content):
    """MATH_DOLLAR: math-enabled post has bare $digit in prose."""
    has_math = 'tag-hash-math' in content or re.search(r'^math:\s*true', content, re.MULTILINE)
    if not has_math:
        return []
    issues = []
    for lineno, line in enumerate(content.split('\n'), 1):
        if not is_prose_line(line):
            continue
        matches = list(re.finditer(r'\$(\d)', line))
        for m in matches:
            issues.append({
                'check': 'MATH_DOLLAR',
                'file': fname,
                'line': lineno,
                'detail': f'Bare ${m.group(1)}... in math-enabled post prose — KaTeX will treat as math delimiter. Fix: replace $N with &#36;N',
                'fixable': True,
            })
    return issues


def check_invalid_json(fname, content):
    """INVALID_JSON: data-options='...' contains invalid JSON."""
    issues = []
    for offset, raw in extract_data_options(content):
        try:
            json.loads(html.unescape(raw))
        except json.JSONDecodeError as e:
            lineno = content[:offset].count('\n') + 1
            issues.append({
                'check': 'INVALID_JSON',
                'file': fname,
                'line': lineno,
                'detail': f'data-options JSON parse error: {e}',
                'fixable': False,
            })
    return issues


def check_no_height(fname, content):
    """NO_HEIGHT: ECharts div missing explicit height."""
    issues = []
    for m in re.finditer(r'<div\s+data-viz="echarts"', content):
        # Check if the same opening tag has a style with height
        tag_end = content.find('>', m.start())
        tag_text = content[m.start():tag_end+1]
        if 'height' not in tag_text:
            lineno = content[:m.start()].count('\n') + 1
            issues.append({
                'check': 'NO_HEIGHT',
                'file': fname,
                'line': lineno,
                'detail': 'ECharts div missing style="height:Xpx" — renders as 0-height canvas (invisible)',
                'fixable': False,
            })
    return issues


def check_viz_no_tag(fname, content):
    """VIZ_NO_TAG: post has data-viz but no tag-hash-viz or viz: true."""
    has_viz_el = bool(re.search(r'data-viz=', content) or re.search(r'data-leaflet', content))
    if not has_viz_el:
        return []
    has_tag = 'tag-hash-viz' in content or re.search(r'^viz:\s*true', content, re.MULTILINE)
    if not has_tag:
        return [{
            'check': 'VIZ_NO_TAG',
            'file': fname,
            'line': 1,
            'detail': 'Post has data-viz/data-leaflet elements but no tag-hash-viz or viz: true in front matter — ECharts/Leaflet will not load',
            'fixable': False,
        }]
    return []


def check_apos_in_attr(fname, content):
    """APOS_IN_ATTR: apostrophe inside single-quoted data-options attribute."""
    issues = []
    for offset, raw in extract_data_options(content):
        if "'" in raw:
            lineno = content[:offset].count('\n') + 1
            # Find first apostrophe context
            idx = raw.index("'")
            snippet = raw[max(0, idx-20):idx+20]
            issues.append({
                'check': 'APOS_IN_ATTR',
                'file': fname,
                'line': lineno,
                'detail': f"Apostrophe in data-options='...' breaks HTML attribute parsing. Near: ...{snippet}...",
                'fixable': False,
            })
    return issues


def check_date_url(fname, content):
    """DATE_URL: link uses /YYYY/MM/DD/slug/ format (site uses /:title/)."""
    issues = []
    for m in re.finditer(r'\(/\d{4}/\d{2}/\d{2}/[\w-]+/?', content):
        lineno = content[:m.start()].count('\n') + 1
        issues.append({
            'check': 'DATE_URL',
            'file': fname,
            'line': lineno,
            'detail': f'Date-format URL {m.group()} — site uses permalink: /:title/ so this will 404',
            'fixable': False,
        })
    return issues


def check_story_no_tag(fname, content):
    """STORY_NO_TAG: scrollytelling section present but no tag-hash-story."""
    has_story = 'story-section' in content or 'story-step' in content
    if not has_story:
        return []
    has_tag = 'tag-hash-story' in content
    if not has_tag:
        return [{
            'check': 'STORY_NO_TAG',
            'file': fname,
            'line': 1,
            'detail': 'Post has .story-section elements but no tag-hash-story in tags — Scrollama will not load, steps will not animate',
            'fixable': False,
        }]
    return []


def check_leaflet_marker_apos(fname, content):
    """LEAFLET_MARKER_APOS: apostrophe inside data-markers='...' attribute."""
    issues = []
    for offset, raw in extract_data_markers(content):
        if "'" in raw:
            lineno = content[:offset].count('\n') + 1
            idx = raw.index("'")
            snippet = raw[max(0, idx-20):idx+20]
            issues.append({
                'check': 'LEAFLET_MARKER_APOS',
                'file': fname,
                'line': lineno,
                'detail': f"Apostrophe in data-markers='...' breaks HTML attribute. Near: ...{snippet}...",
                'fixable': False,
            })
    return issues


CHECKS = [
    check_math_dollar,
    check_invalid_json,
    check_no_height,
    check_viz_no_tag,
    check_apos_in_attr,
    check_date_url,
    check_story_no_tag,
    check_leaflet_marker_apos,
]

# ── Auto-fix ──────────────────────────────────────────────────────────────────

def fix_math_dollar(filepath, content):
    """Replace bare $digit in prose with &#36;digit."""
    lines = content.split('\n')
    fixed = []
    for line in lines:
        if is_prose_line(line):
            fixed.append(re.sub(r'\$(\d)', r'&#36;\1', line))
        else:
            fixed.append(line)
    return '\n'.join(fixed)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='QA checker for Jekyll posts')
    parser.add_argument('--fix', action='store_true', help='Auto-fix safe issues')
    parser.add_argument('--changed', action='store_true', help='Only check git-changed files')
    parser.add_argument('--check', nargs='+', help='Only run specific checks (e.g. MATH_DOLLAR INVALID_JSON)')
    args = parser.parse_args()

    posts_dir = os.path.abspath(POSTS_DIR)
    if not os.path.isdir(posts_dir):
        print(f"ERROR: _posts/ not found at {posts_dir}", file=sys.stderr)
        sys.exit(2)

    # Determine which files to check
    if args.changed:
        rel_files = get_changed_files()
        files = [os.path.join(os.path.dirname(posts_dir), f) for f in rel_files
                 if os.path.exists(os.path.join(os.path.dirname(posts_dir), f))]
        if not files:
            print("No changed post files detected.")
            sys.exit(0)
    else:
        files = sorted(
            os.path.join(posts_dir, f)
            for f in os.listdir(posts_dir)
            if f.endswith('.md')
        )

    active_checks = [c for c in CHECKS
                     if not args.check or c.__name__.replace('check_', '').upper() in [x.upper() for x in args.check]]

    all_issues = []
    fixed_files = 0

    for filepath in files:
        fname = os.path.basename(filepath)
        try:
            content = open(filepath).read()
        except Exception as e:
            print(f"ERROR reading {fname}: {e}")
            continue

        file_issues = []
        for check in active_checks:
            file_issues.extend(check(fname, content))

        if args.fix:
            # Apply safe auto-fixes
            has_math_dollar = any(i['check'] == 'MATH_DOLLAR' for i in file_issues)
            if has_math_dollar:
                content = fix_math_dollar(filepath, content)
                open(filepath, 'w').write(content)
                fixed_files += 1
            # Re-run checks after fix to remove resolved issues from report
            file_issues = []
            for check in active_checks:
                file_issues.extend(check(fname, content))

        all_issues.extend(file_issues)

    # ── Report ────────────────────────────────────────────────────────────────
    if args.fix and fixed_files:
        print(f"Auto-fixed MATH_DOLLAR in {fixed_files} file(s).")

    if not all_issues:
        print(f"✓ QA passed — {len(files)} post(s) checked, 0 issues.")
        sys.exit(0)

    # Group by check type for summary
    by_check = {}
    for issue in all_issues:
        by_check.setdefault(issue['check'], []).append(issue)

    print(f"\n{'='*60}")
    print(f"QA FAILED — {len(all_issues)} issue(s) in {len(files)} post(s) checked")
    print(f"{'='*60}\n")

    for check_name, issues in sorted(by_check.items()):
        print(f"[{check_name}] — {len(issues)} occurrence(s)")
        for issue in issues[:10]:  # cap at 10 per check type
            print(f"  {issue['file']}:{issue['line']}  {issue['detail'][:120]}")
        if len(issues) > 10:
            print(f"  ... and {len(issues)-10} more")
        print()

    fixable = [i for i in all_issues if i['fixable']]
    if fixable:
        print(f"Run with --fix to auto-correct {len(fixable)} safe issue(s) (MATH_DOLLAR).")

    sys.exit(1)


if __name__ == '__main__':
    main()
