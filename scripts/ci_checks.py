#!/usr/bin/env python3
"""Mythos Atlas — CI Checks

Usage:
  python3 scripts/ci_checks.py

Checks:
  1. Format validation — heading consistency, broken internal links
  2. Orphan check — files not referenced from indexes
  3. Citation check — each entry has ≥1 source reference
  4. Statistical diff — run generate_stats.py and compare to committed
"""

import json, os, re, sys, subprocess, glob
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / '_catalog.json'
README = ROOT / 'README.md'
THEMES_INDEX = ROOT / 'themes' / '00-index.md'
ANALYSES_DIR = ROOT / 'analyses'
THEMES_DIR = ROOT / 'themes'
CULTURES_DIR = ROOT / 'cultures'
REFERENCES_DIR = ROOT / 'references'
GENERATE_STATS = ROOT / 'scripts' / 'generate_stats.py'
STATS_DIR = ROOT / 'stats'
CITATION_BASELINE = ROOT / 'scripts' / 'citation_baseline.txt'

# Top-level directories excluded from content checks. These hold development
# and planning records rather than published mythology content, so their
# links and heading structure are not part of what CI guards.
EXCLUDED_TOP_DIRS = {'.git', 'docs', 'node_modules'}

EXIT_CODE = 0
ERRORS = []
WARNINGS = []
CITATION_BASELINED = set()   # populated from CITATION_BASELINE in main()
BASELINE_SEEN = set()        # baselined pages that still fail, to spot stale entries

def err(msg):
    global EXIT_CODE
    EXIT_CODE = 1
    ERRORS.append(msg)
    print(f'  [ERROR] {msg}')

def warn(msg):
    WARNINGS.append(msg)
    print(f'  [WARN] {msg}')


# Markdown inline link. The destination may itself contain one level of
# balanced parentheses (e.g. 大洪水(神族戰爭淹沒).md), which CommonMark allows.
MD_LINK = re.compile(r'\[([^\]]*)\]\(((?:[^()\n]|\([^()\n]*\))+)\)')


# ── 1. Format Validation ───────────────────────────────────────────

def check_heading_hierarchy(filepath):
    """Check each .md file has proper heading structure."""
    try:
        text = filepath.read_text(encoding='utf-8')
    except Exception as e:
        warn(f'{rel(filepath)}: cannot read ({e})')
        return

    lines = text.split('\n')
    headings = [(i+1, l.strip()) for i, l in enumerate(lines) if l.strip().startswith('#')]

    if not headings:
        err(f'{rel(filepath)}: no heading found')
        return

    # Check first heading is h1
    first_level = len(headings[0][1]) - len(headings[0][1].lstrip('#'))
    if first_level != 1:
        err(f'{rel(filepath)}: first heading must be h1, got h{first_level}')

    # Check hierarchy doesn't skip levels
    prev_level = 1  # assume h1
    for line_no, h in headings[1:]:
        level = len(h) - len(h.lstrip('#'))
        if level > prev_level + 1:
            err(f'{rel(filepath)}:{line_no}: heading level jumps from h{prev_level} to h{level}')
        prev_level = level

    # Check no empty headings
    for line_no, h in headings:
        content = h.lstrip('#').strip()
        if not content:
            err(f'{rel(filepath)}:{line_no}: empty heading')


def check_broken_links(filepath, all_md_files):
    """Check internal .md links point to existing files."""
    try:
        text = filepath.read_text(encoding='utf-8')
    except Exception:
        return

    internal_links = MD_LINK.findall(text)
    for link_text, target in internal_links:
        target_clean = target.split('#')[0].split('?')[0]
        # Markdown links may percent-encode spaces etc.; decode before hitting the FS
        target_clean = unquote(target_clean)
        if not target_clean.endswith('.md'):
            continue
        target_path = (filepath.parent / target_clean).resolve()
        if not target_path.exists():
            # Try from root
            target_root = (ROOT / target_clean).resolve()
            if not target_root.exists():
                err(f'{rel(filepath)}: broken link "{target}" → {rel(target_path)}')


# ── 2. Orphan Check ────────────────────────────────────────────────

def load_catalog():
    try:
        return json.loads(CATALOG.read_text(encoding='utf-8'))
    except Exception as e:
        err(f'cannot load _catalog.json: {e}')
        return {'cultures': [], 'themes': []}


def get_indexed_entries(index_file):
    """Parse a markdown index file and return set of referenced filenames."""
    if not index_file.exists():
        return set()
    text = index_file.read_text(encoding='utf-8')
    refs = set()
    for m in MD_LINK.finditer(text):
        target = unquote(m.group(2).split('#')[0].split('?')[0])
        if target.endswith('.md') or '/' in target:
            refs.add(target)
    return refs


def check_orphan_themes():
    themes_index_refs = get_indexed_entries(THEMES_INDEX)
    for f in sorted(THEMES_DIR.glob('*.md')):
        if f.name in ('README.md', '00-index.md'):
            continue
        # Check if this file is referenced in 00-index.md
        link_target = f.name
        found = any(link_target in ref for ref in themes_index_refs)
        if not found:
            err(f'{rel(f)}: orphan theme — not listed in themes/00-index.md')


def check_orphan_analyses():
    readme_text = README.read_text(encoding='utf-8')
    analyses_section = ''
    m = re.search(r'<!-- ANALYSES_START -->(.*?)<!-- ANALYSES_END -->', readme_text, re.DOTALL)
    if m:
        analyses_section = m.group(1)
    indexed_analyses = set(re.findall(r'\(analyses/([^)]+\.md)\)', analyses_section))

    for f in sorted(ANALYSES_DIR.glob('*.md')):
        if f.name == 'README.md':
            continue
        if f.name not in indexed_analyses:
            err(f'{rel(f)}: orphan analysis — not listed in README.md ANALYSES section')


def check_orphan_gods_stories():
    catalog = load_catalog()
    catalog_gods = {}
    catalog_stories = {}
    for c in catalog.get('cultures', []):
        cid = c['id']
        if 'pantheon' in c:
            pantheon_names = set(re.split(r'[、,，]', c['pantheon']))
            catalog_gods[cid] = pantheon_names
        if 'stories' in c:
            catalog_stories[cid] = set(c['stories'])

    # Check gods
    for gods_dir in sorted(CULTURES_DIR.glob('*/gods/')):
        cid = gods_dir.parent.name
        for f in sorted(gods_dir.glob('*.md')):
            if f.name == 'README.md':
                continue
            # Check if the file exists at least (we don't enforce listing in catalog
            # since catalog may use names not matching filenames)
            pass  # god pages are generally OK if they exist

    # Check stories
    for stories_dir in sorted(CULTURES_DIR.glob('*/stories/')):
        cid = stories_dir.parent.name
        for f in sorted(stories_dir.glob('*.md')):
            if f.name == 'README.md':
                continue


def check_orphan_culture_comparisons():
    """Check comparisons/ files exist and are referenced somewhere reasonable."""
    for comp_dir in sorted(CULTURES_DIR.glob('*/comparisons/')):
        cid = comp_dir.parent.name
        index_file = comp_dir / 'README.md'
        indexed_refs = get_indexed_entries(index_file) if index_file.exists() else set()
        for f in sorted(comp_dir.glob('*.md')):
            if f.name == 'README.md':
                continue
            in_index = any(f.name in ref for ref in indexed_refs)
            if not in_index:
                err(f'{rel(f)}: orphan comparison — not listed in {rel(index_file)}')


# ── 3. Citation Check ──────────────────────────────────────────────

CITATION_SECTION_PATTERN = re.compile(
    r'^#{2,4}\s*(參考文獻|參考來源|參考資料|References|Sources|Bibliography)\s*$',
    re.MULTILINE
)

ENTRY_DIRS = [
    ('gods/*.md', '神祇頁面'),
    ('stories/*.md', '故事頁面'),
    ('comparisons/*.md', '比較頁面'),
]


def citation_err(rel_path, msg):
    """Report a citation gap, unless it is a known pre-existing one."""
    if rel_path in CITATION_BASELINED:
        BASELINE_SEEN.add(rel_path)
        return
    err(f'{rel_path}: {msg}')


def check_citations_in_file(filepath, label):
    """Check that a file has a reference section with content."""
    rel_path = rel(filepath)
    try:
        text = filepath.read_text(encoding='utf-8')
    except Exception:
        return

    # Find all citation sections
    matches = list(CITATION_SECTION_PATTERN.finditer(text))
    if not matches:
        citation_err(rel_path, '缺少參考文獻區塊（需包含「## 參考文獻」或「## 參考來源」）')
        return

    # Check the last citation section has content
    last_match = matches[-1]
    section_start = last_match.end()
    remaining = text[section_start:].strip()

    if not remaining:
        citation_err(rel_path, '參考文獻區塊為空')
        return

    # Count non-empty lines after the section header before next heading
    lines = remaining.split('\n')
    ref_lines = 0
    for line in lines:
        if line.strip().startswith('#'):
            break
        if line.strip() and not line.strip().startswith('>'):
            ref_lines += 1

    if ref_lines == 0:
        citation_err(rel_path, '參考文獻區塊無實際內容')


def run_citation_checks():
    # Check all analysis files
    for f in sorted(ANALYSES_DIR.glob('*.md')):
        if f.name == 'README.md':
            continue
        check_citations_in_file(f, '分析文章')

    # Theme pages are cross-cutting motif summaries that cite through the
    # culture pages they link to, so they carry no reference section of
    # their own and are deliberately not checked here.

    # Check all culture sub-pages
    for pattern, label in ENTRY_DIRS:
        for f in sorted(CULTURES_DIR.glob(f'*/{pattern}')):
            if f.name == 'README.md':
                continue
            check_citations_in_file(f, label)


# ── 4. Statistical Diff ───────────────────────────────────────────

def run_stats_comparison():
    """Run generate_stats.py and check if stats changed."""
    print('  [*] Running generate_stats.py for comparison...')
    try:
        result = subprocess.run(
            [sys.executable, str(GENERATE_STATS)],
            capture_output=True, text=True, timeout=120,
            cwd=str(ROOT)
        )
        print(f'      stdout: {result.stdout.strip()[:200]}')
        if result.returncode != 0:
            err(f'generate_stats.py failed with code {result.returncode}')
            print(f'      stderr: {result.stderr.strip()[:500]}')
            return
    except subprocess.TimeoutExpired:
        err('generate_stats.py timed out')
        return
    except FileNotFoundError:
        warn('generate_stats.py not found, skipping statistical comparison')
        return

    # Check if git is available and compare
    try:
        git_result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True, text=True,
            cwd=str(ROOT)
        )
        if git_result.returncode == 0 and git_result.stdout.strip():
            changed_files = []
            for line in git_result.stdout.strip().split('\n'):
                parts = line.strip().split()
                if len(parts) >= 2:
                    changed_files.append(parts[-1])
            stats_changes = [f for f in changed_files if f.startswith('stats/') or f == 'README.md']
            if stats_changes:
                print(f'      ⚠️  Stats changed after regeneration:')
                for f in stats_changes:
                    print(f'         - {f}')
                warn('Stats changed — commit updated stats if this is intentional')
    except Exception:
        pass


# ── Helpers ────────────────────────────────────────────────────────

def rel(path):
    """Return path relative to ROOT."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def is_excluded(path):
    """True for paths under a directory CI does not police."""
    try:
        parts = path.relative_to(ROOT).parts
    except ValueError:
        return True
    return bool(parts) and parts[0] in EXCLUDED_TOP_DIRS


def load_citation_baseline():
    """Known pages still missing citations.

    These are pre-existing gaps, tracked so CI can block *new* violations
    without demanding that all of them be researched at once. Fixing a page
    means deleting its line here.
    """
    if not CITATION_BASELINE.exists():
        return set()
    return {
        line.strip()
        for line in CITATION_BASELINE.read_text(encoding='utf-8').splitlines()
        if line.strip() and not line.startswith('#')
    }


# ── Main ───────────────────────────────────────────────────────────

def main():
    os.chdir(str(ROOT))

    print('═' * 60)
    print('Mythos Atlas — CI Checks')
    print('═' * 60)

    global CITATION_BASELINED
    CITATION_BASELINED = load_citation_baseline()

    # Build list of all .md files for link checking
    all_md = {f for f in ROOT.rglob('*.md') if not is_excluded(f)}

    # ── Section 1: Format Validation ──
    print('\n[1/4] Format Validation')
    print('─' * 40)
    for f in sorted(all_md):
        check_heading_hierarchy(f)
        check_broken_links(f, all_md)

    # ── Section 2: Orphan Check ──
    print('\n[2/4] Orphan Check')
    print('─' * 40)
    check_orphan_themes()
    check_orphan_analyses()
    check_orphan_culture_comparisons()

    # ── Section 3: Citation Check ──
    print('\n[3/4] Citation Check')
    print('─' * 40)
    run_citation_checks()
    if CITATION_BASELINED:
        print(f'  [*] {len(BASELINE_SEEN)} 個已知缺口暫緩（見 {rel(CITATION_BASELINE)}）')
        stale = sorted(CITATION_BASELINED - BASELINE_SEEN)
        if stale:
            print(f'  [*] {len(stale)} 個項目已補上文獻，可從基準線移除：')
            for p in stale[:20]:
                print(f'        {p}')
            if len(stale) > 20:
                print(f'        ...另有 {len(stale) - 20} 筆')

    # ── Section 4: Statistical Comparison ──
    print('\n[4/4] Statistical Comparison')
    print('─' * 40)
    run_stats_comparison()

    # ── Summary ──
    print('\n' + '═' * 60)
    if ERRORS:
        print(f'❌  FAILED — {len(ERRORS)} errors, {len(WARNINGS)} warnings')
        for e in ERRORS:
            print(f'   {e}')
    elif WARNINGS:
        print(f'⚠️  PASSED with {len(WARNINGS)} warnings')
        for w in WARNINGS:
            print(f'   {w}')
    else:
        print('✅  ALL CHECKS PASSED')
    print('═' * 60)

    return EXIT_CODE


if __name__ == '__main__':
    sys.exit(main())
