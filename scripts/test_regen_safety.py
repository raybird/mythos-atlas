#!/usr/bin/env python3
"""Regression tests for safe catalogue regeneration."""
import contextlib, importlib.util, io, json, os, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location('regen', ROOT / 'regenerate_all.py')
regen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(regen)


def sample_catalog():
    return {
        'cultures': [{
            'id': 'testculture',
            'name': '測試文化',
            'name_en': 'Test Culture',
            'region': '測試區',
            'era': '測試時期',
            'sources': ['原始文獻'],
            'creation': '創世',
            'flood': '洪水',
            'pantheon': '神系',
            'motifs': ['母題'],
            'parallels': [['本地', '對應']],
            'stories': ['故事'],
        }],
        'themes': [],
    }


class TestRegenSafety(unittest.TestCase):
    def test_merge_preserves_manual_lines_and_adds_catalog_lines(self):
        generated = '# T\n\n## A\n\n- a\n\n## B\n\n- b\n'
        current = '# T\n\n## A\n\n- a (manual)\n\n## B\n\n- c\n'
        merged = regen.merge_lines(generated.splitlines(True), current.splitlines(True))
        self.assertTrue(all(line in merged for line in current.splitlines(True)))
        self.assertIn('- a\n', merged)
        self.assertIn('- b\n', merged)

    def test_check_flags_unlogged_manual_line_then_passes_with_baseline(self):
        catalog = sample_catalog()
        generated = regen.generate_culture_md(catalog['cultures'][0]).splitlines(True)
        manual = '- 手寫補充\n'
        with tempfile.TemporaryDirectory() as td:
            old_repo = regen.REPO
            old_base = regen.MANUAL_BASELINE
            try:
                regen.REPO = td
                regen.MANUAL_BASELINE = os.path.join(td, 'baseline.json')
                target = Path(td) / 'cultures' / 'testculture'
                target.mkdir(parents=True)
                (target / 'index.md').write_text(''.join(generated + [manual]), encoding='utf-8')
                with open(regen.MANUAL_BASELINE, 'w', encoding='utf-8') as f:
                    json.dump({}, f)
                with contextlib.redirect_stdout(io.StringIO()) as out:
                    result = regen.mode_check(catalog)
                self.assertEqual(result, 1)
                self.assertIn('UNSAFE', out.getvalue())
                with open(regen.MANUAL_BASELINE, 'w', encoding='utf-8') as f:
                    json.dump({'cultures/testculture/index.md': [manual.strip()]}, f)
                with contextlib.redirect_stdout(io.StringIO()) as out:
                    result = regen.mode_check(catalog)
                self.assertEqual(result, 0)
                self.assertIn('SAFE', out.getvalue())
            finally:
                regen.REPO = old_repo
                regen.MANUAL_BASELINE = old_base


if __name__ == '__main__':
    unittest.main(verbosity=2)
