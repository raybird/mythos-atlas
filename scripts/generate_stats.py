#!/usr/bin/env python3
"""Mythos Atlas — Stats Dashboard & Radar Chart Generator

Scans _catalog.json, _state.json, cultures/*, and analyses/* to produce:
  - stats/index.md       — Main dashboard with progress tables & embedded SVGs
  - stats/radar/*.svg    — Per-culture radar charts (5 dimensions)
  - stats/overview/*.svg — Aggregate bar chart, enrichment progress, analysis coverage

Usage:
  python3 scripts/generate_stats.py [--serve]
"""

import json, os, re, sys, glob
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / '_catalog.json'
STATE = ROOT / '_state.json'
CULTURES = ROOT / 'cultures'
ANALYSES = ROOT / 'analyses'
THEMES = ROOT / 'themes'
STATS_DIR = ROOT / 'stats'
RADAR_DIR = STATS_DIR / 'radar'
OVERVIEW_DIR = STATS_DIR / 'overview'

# ── colour palette (Earthy / Mythological) ──────────────────────────
COLOURS = {
    'gods':       '#C44E52',   # deep red
    'stories':    '#4C72B0',   # deep blue
    'comparisons':'#DD8452',   # amber
    'enriched':   '#55A868',   # green
    'analyses':   '#8172B2',   # purple
    'bg':         '#F9F9F9',
    'grid':       '#CCCCCC',
}

# ── helpers ────────────────────────────────────────────────────────
def load_json(path):
    with open(path) as f:
        return json.load(f)

def culture_files(culture_id, subdir):
    d = CULTURES / culture_id / subdir
    if not d.exists():
        return []
    return sorted([p for p in d.iterdir() if p.suffix == '.md' and p.name != 'README.md'])

def detect_cultures_in_md(text, culture_names_en):
    found = set()
    text_lower = text.lower()
    for cid, cname, cname_en in culture_names_en:
        if cname_en.lower() in text_lower or cname in text:
            found.add(cid)
    return found

# ── metrics computation ────────────────────────────────────────────
def compute_metrics():
    catalog = load_json(CATALOG)
    state = load_json(STATE)
    enriched = set(state.get('enrich_log', []))
    analyses_done = set(state.get('analysis_log', []))

    # culture info: id, name, name_en, region
    cultures_info = []
    for c in catalog['cultures']:
        cultures_info.append({
            'id': c['id'],
            'name': c['name'],
            'name_en': c['name_en'],
            'region': c.get('region', ''),
            'era': c.get('era', ''),
            'pantheon_raw': c.get('pantheon', ''),
            'stories_list': c.get('stories', []),
            'parallels_list': c.get('parallels', []),
        })
    # derived
    for ci in cultures_info:
        ci['pantheon_expected'] = len([x for x in re.split(r'[、,，]', ci['pantheon_raw']) if x.strip()]) if ci['pantheon_raw'] else 0
        ci['stories_expected'] = len(ci['stories_list'])
        ci['parallels_expected'] = len(ci['parallels_list'])

    # crawl filesystem
    for ci in cultures_info:
        g = culture_files(ci['id'], 'gods')
        s = culture_files(ci['id'], 'stories')
        c = culture_files(ci['id'], 'comparisons')
        ci['gods_actual'] = len(g)
        ci['stories_actual'] = len(s)
        ci['comparisons_actual'] = len(c)
        ci['total_pages'] = ci['gods_actual'] + ci['stories_actual'] + ci['comparisons_actual']
        # line counts as rough "depth" proxy
        depth = 0
        for p in list(g) + list(s) + list(c):
            try:
                depth += sum(1 for _ in open(p))
            except:
                pass
        ci['content_depth'] = depth
        ci['is_enriched'] = ci['id'] in enriched

    # analyses — count per culture
    culture_names_en = [(ci['id'], ci['name'], ci['name_en']) for ci in cultures_info]
    analysis_refs = defaultdict(int)
    analysis_total = 0
    for af in sorted(ANALYSES.glob('*.md')):
        if af.name in ('README.md',):
            continue
        text = af.read_text(encoding='utf-8')
        found = detect_cultures_in_md(text, culture_names_en)
        for cid in found:
            analysis_refs[cid] += 1
        analysis_total += 1

    for ci in cultures_info:
        ci['analysis_refs'] = analysis_refs.get(ci['id'], 0)

    # theme info
    themes_list = []
    for t in catalog['themes']:
        themes_list.append({
            'id': t['id'],
            'name': t['name'],
            'name_en': t['name_en'],
            'cultures_covered': t.get('cultures_covered', []),
        })

    return {
        'cultures': cultures_info,
        'themes': themes_list,
        'enriched': enriched,
        'analyses_done': analyses_done,
        'analysis_total': analysis_total,
        'runs': state.get('runs', 0),
        'updated': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
    }

# ── radar chart ────────────────────────────────────────────────────
def make_radar_chart(ci, all_metrics, path):
    """5-dimension radar: gods, stories, comparisons, enriched, analysis_refs"""
    # compute global max for normalisation
    max_gods = max(m['gods_actual'] for m in all_metrics) or 1
    max_stories = max(m['stories_actual'] for m in all_metrics) or 1
    max_comps = max(m['comparisons_actual'] for m in all_metrics) or 1
    max_analyses = max(m['analysis_refs'] for m in all_metrics) or 1

    categories = ['Gods', 'Stories', 'Comparisons', 'Enrichment', 'Analyses']
    values = [
        ci['gods_actual'] / max_gods * 100,
        ci['stories_actual'] / max_stories * 100,
        ci['comparisons_actual'] / max_comps * 100,
        100 if ci['is_enriched'] else 20,
        ci['analysis_refs'] / max_analyses * 100,
    ]
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor(COLOURS['bg'])
    ax.set_facecolor(COLOURS['bg'])
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(0)

    ax.fill(angles, values, alpha=0.25, color='#4C72B0')
    ax.plot(angles, values, color='#4C72B0', linewidth=2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=7)
    ax.set_ylim(0, 110)
    ax.set_yticks([25, 50, 75, 100])
    ax.set_yticklabels(['25', '50', '75', '100'], fontsize=6, color='#888888')
    ax.grid(True, color=COLOURS['grid'], alpha=0.5)

    ax.set_title(ci['name_en'], fontsize=10, pad=20, fontweight='bold')
    plt.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)

# ── bar chart: total pages per culture ────────────────────────────
def make_pages_bar(cultures, path):
    cultures_sorted = sorted(cultures, key=lambda c: c['total_pages'], reverse=True)
    names = [c['name_en'] for c in cultures_sorted]
    gods = [c['gods_actual'] for c in cultures_sorted]
    stories = [c['stories_actual'] for c in cultures_sorted]
    comps = [c['comparisons_actual'] for c in cultures_sorted]

    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor(COLOURS['bg'])
    ax.set_facecolor(COLOURS['bg'])

    x = np.arange(len(names))
    w = 0.25
    ax.bar(x - w, gods, w, label='Gods', color=COLOURS['gods'])
    ax.bar(x, stories, w, label='Stories', color=COLOURS['stories'])
    ax.bar(x + w, comps, w, label='Comparisons', color=COLOURS['comparisons'])

    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=75, ha='right', fontsize=6)
    ax.set_ylabel('Pages')
    ax.legend(fontsize=8)
    ax.grid(axis='y', alpha=0.3, color=COLOURS['grid'])
    ax.set_title('Total Pages per Culture', fontsize=13, fontweight='bold')
    plt.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)

# ── enrichment progress pie ────────────────────────────────────────
def make_enrichment_pie(enriched_count, total, path):
    fig, ax = plt.subplots(figsize=(5, 5))
    fig.patch.set_facecolor(COLOURS['bg'])
    ax.set_facecolor(COLOURS['bg'])
    labels = [f'Enriched\n{enriched_count}', f'Pending\n{total - enriched_count}']
    sizes = [enriched_count, total - enriched_count]
    colors = [COLOURS['enriched'], '#CCCCCC']
    explode = (0.05, 0)
    ax.pie(sizes, explode=explode, labels=labels, colors=colors,
           autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
    ax.set_title('Culture Enrichment Progress', fontsize=12, fontweight='bold')
    plt.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)

# ── analysis coverage bar ──────────────────────────────────────────
def make_analysis_coverage(cultures, path):
    c_sorted = sorted(cultures, key=lambda c: c['analysis_refs'], reverse=True)[:20]
    names = [c['name_en'] for c in c_sorted]
    refs = [c['analysis_refs'] for c in c_sorted]

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(COLOURS['bg'])
    ax.set_facecolor(COLOURS['bg'])

    bars = ax.barh(names, refs, color=COLOURS['analyses'])
    ax.bar_label(bars, fontsize=8)
    ax.set_xlabel('Analysis mentions')
    ax.set_title('Top-20 Cultures by Analysis Coverage', fontsize=12, fontweight='bold')
    ax.invert_yaxis()
    ax.grid(axis='x', alpha=0.3, color=COLOURS['grid'])
    plt.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)

# ── generate dashboard markdown ────────────────────────────────────
def generate_dashboard(metrics):
    cultures = metrics['cultures']
    total = len(cultures)
    enriched_count = sum(1 for c in cultures if c['is_enriched'])
    total_pages = sum(c['total_pages'] for c in cultures)
    total_depth = sum(c['content_depth'] for c in cultures)
    avg_pages = total_pages / total if total else 0

    # enrichment rank
    enriched_sorted = sorted(cultures, key=lambda c: c['total_pages'], reverse=True)

    # markdown
    lines = []
    lines.append('# Mythos Atlas — Stats Dashboard')
    lines.append('')
    lines.append('> 自動更新於 ' + metrics['updated'])
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 專案概覽 / Project Overview')
    lines.append('')
    lines.append('| Metric | Value |')
    lines.append('|--------|-------|')
    lines.append(f'| 文化體系 / Cultures | {total} |')
    lines.append(f'| 已充實 / Enriched | {enriched_count} ({enriched_count/total*100:.1f}%) |')
    lines.append(f'| 待充實 / To Enrich | {total - enriched_count} |')
    lines.append(f'| 分析文章 / Analyses | {metrics["analysis_total"]} |')
    lines.append(f'| 神祇頁面 / God Pages | {sum(c["gods_actual"] for c in cultures)} |')
    lines.append(f'| 故事頁面 / Story Pages | {sum(c["stories_actual"] for c in cultures)} |')
    lines.append(f'| 比較頁面 / Comparison Pages | {sum(c["comparisons_actual"] for c in cultures)} |')
    lines.append(f'| 總頁面 / Total Pages | {total_pages} |')
    lines.append(f'| 平均每文化頁面 / Avg Pages/Culture | {avg_pages:.1f} |')
    lines.append(f'| 內容總深度 / Total Lines | {total_depth:,} |')
    lines.append(f'| 執行次數 / Runs | {metrics["runs"]} |')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 🎯 文化充實進度 / Enrichment Progress')
    lines.append('')
    lines.append('![Enrichment Pie](overview/enrichment-pie.svg)')
    lines.append('')
    lines.append('![Pages per Culture](overview/pages-bar.svg)')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 📈 分析覆蓋 / Analysis Coverage')
    lines.append('')
    lines.append('![Analysis Coverage](overview/analysis-coverage.svg)')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 📡 各文化雷達圖 / Per-Culture Radar')
    lines.append('')
    lines.append('五維度雷達圖：神祇頁面、故事頁面、比較頁面、充實狀態、分析提及次數。')
    lines.append('')
    lines.append('| 文化 | 雷達圖 | 頁面總數 | 已充實 | 分析提及 |')
    lines.append('|------|--------|---------|--------|---------|')

    for c in enriched_sorted:
        radar_svg = f'radar/{c["id"]}.svg'
        enriched_mark = '✅' if c['is_enriched'] else '⬜'
        lines.append(f'| **{c["name"]}**<br>{c["name_en"]} | ![radar]({radar_svg}) | {c["total_pages"]} | {enriched_mark} | {c["analysis_refs"]} |')

    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 📊 各文化詳細指標 / Detailed Metrics')
    lines.append('')
    lines.append('| Culture | Gods | Stories | Comps | Total | Enriched | Analyses | Depth |')
    lines.append('|---------|------|---------|-------|-------|----------|----------|-------|')

    for c in enriched_sorted:
        lines.append(f'| {c["name"]} ({c["name_en"]}) | {c["gods_actual"]} | {c["stories_actual"]} | {c["comparisons_actual"]} | {c["total_pages"]} | {"Y" if c["is_enriched"] else "N"} | {c["analysis_refs"]} | {c["content_depth"]} |')

    lines.append('')
    lines.append('---')
    lines.append(f'*Generated by `scripts/generate_stats.py` on {metrics["updated"]}*')
    lines.append('')

    return '\n'.join(lines)

# ── update README stats section ────────────────────────────────────
def update_readme(metrics):
    readme_path = ROOT / 'README.md'
    text = readme_path.read_text(encoding='utf-8')
    cultures = metrics['cultures']
    enriched_count = sum(1 for c in cultures if c['is_enriched'])
    total_pages = sum(c['total_pages'] for c in cultures)

    # rebuild STATS block
    stats_block = f"""<!-- STATS_START -->

## 📊 當前狀態

> 自動更新於 {metrics['updated']}

| 類別 | 進度 |
|------|------|
| 文化體系 | {len(cultures)}/{len(cultures)} |
| 跨文化主題 | {len(metrics['themes'])}/{len(metrics['themes'])} |
| 分析文章 | {metrics['analysis_total']} |
| 已充實文化 | {enriched_count}/{len(cultures)} |
| 總頁面數 | {total_pages} |
| 總執行次數 | {metrics['runs']} |

<!-- STATS_END -->"""

    new_text = re.sub(
        r'<!-- STATS_START -->.*?<!-- STATS_END -->',
        stats_block,
        text,
        flags=re.DOTALL
    )
    readme_path.write_text(new_text, encoding='utf-8')
    return True

# ── main ───────────────────────────────────────────────────────────
def main():
    print('[*] Computing metrics...')
    metrics = compute_metrics()
    cultures = metrics['cultures']
    print(f'    Cultures: {len(cultures)}')
    print(f'    Enriched: {sum(1 for c in cultures if c["is_enriched"])}/{len(cultures)}')
    print(f'    Analyses: {metrics["analysis_total"]}')
    print(f'    Total pages: {sum(c["total_pages"] for c in cultures)}')

    # ensure output dirs
    RADAR_DIR.mkdir(parents=True, exist_ok=True)
    OVERVIEW_DIR.mkdir(parents=True, exist_ok=True)

    # generate per-culture radar charts
    print('[*] Generating radar charts...')
    for ci in cultures:
        path = RADAR_DIR / f'{ci["id"]}.svg'
        try:
            make_radar_chart(ci, cultures, path)
        except Exception as e:
            print(f'    [!] {ci["id"]}: {e}')
    print(f'    Done — {len(cultures)} charts')

    # overview charts
    print('[*] Generating overview charts...')
    make_pages_bar(cultures, OVERVIEW_DIR / 'pages-bar.svg')
    print('    pages-bar.svg')
    make_enrichment_pie(sum(1 for c in cultures if c['is_enriched']), len(cultures), OVERVIEW_DIR / 'enrichment-pie.svg')
    print('    enrichment-pie.svg')
    make_analysis_coverage(cultures, OVERVIEW_DIR / 'analysis-coverage.svg')
    print('    analysis-coverage.svg')

    # dashboard
    print('[*] Generating dashboard...')
    dashboard = generate_dashboard(metrics)
    (STATS_DIR / 'index.md').write_text(dashboard, encoding='utf-8')
    print('    stats/index.md')

    # update README
    print('[*] Updating README.md...')
    update_readme(metrics)
    print('    README.md updated')

    print('[√] Done. Open stats/index.md to view the dashboard.')

if __name__ == '__main__':
    main()
