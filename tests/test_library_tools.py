"""Tool tests use temporary fixtures, not the user's installed skill directories."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_library import catalog, validate
from install_skills import install


class LibraryToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'source'
        self.dest = Path(self.temp.name) / 'installed'
        self.write('README.md', '[Entry](AGENTS.md)\n')
        self.write('AGENTS.md', '[Index](skills/INDEX.md)\n')
        self.write('CLAUDE.md', '[Entry](AGENTS.md)\n')
        self.write('docs/usage.md', 'Fixture usage.\n')
        self.write('tests/behavior-cases.md', 'Manual scenarios, not executed.\n')
        self.add_skill('skill-router', 'core')
        self.add_skill('development-discovery', 'development')
        self.write('skills/development/development-discovery/templates/spec.md', 'Template\n')
        self.write('skills/INDEX.md',
                   '| `skill-router` | [SKILL.md](core/skill-router/SKILL.md) |\n'
                   '| `development-discovery` | [SKILL.md](development/development-discovery/SKILL.md) |\n')

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding='utf-8')

    def add_skill(self, name, domain):
        self.write(f'skills/{domain}/{name}/SKILL.md',
                   f'---\nname: {name}\ndescription: A fixture skill.\n---\n\n# Fixture\n')

    def test_valid_catalog_and_links(self):
        self.assertEqual(validate(self.root), [])
        self.assertEqual(len(catalog(self.root)), 2)

    def test_missing_index_entry(self):
        self.write('skills/INDEX.md', '# Empty\n')
        self.assertTrue(any('exactly once' in error for error in validate(self.root)))

    def test_duplicate_index_entry(self):
        index = self.root / 'skills/INDEX.md'
        self.write('skills/INDEX.md', index.read_text() +
                   '| `skill-router` | [SKILL.md](core/skill-router/SKILL.md) |\n')
        self.assertTrue(any('exactly once' in error for error in validate(self.root)))

    def test_broken_link(self):
        self.write('README.md', '[Missing](not-here.md)\n')
        self.assertTrue(any('broken local link' in error for error in validate(self.root)))

    def test_duplicate_name(self):
        self.add_skill('skill-router', 'other')
        self.assertTrue(any('duplicate skill name' in error for error in validate(self.root)))

    def test_flat_layout_rejected(self):
        self.write('skills/flat/SKILL.md', '---\nname: flat\ndescription: Fixture.\n---\n')
        self.assertTrue(any('expected skills/' in error for error in validate(self.root)))

    def test_dry_run_writes_nothing(self):
        self.assertEqual(len(install(self.root, self.dest, None, True)), 2)
        self.assertFalse(self.dest.exists())

    def test_install_flattens_and_preserves_resources(self):
        install(self.root, self.dest, None)
        self.assertTrue((self.dest / 'development-discovery/templates/spec.md').is_file())
        self.assertTrue((self.dest / 'skill-router/references/library-index.md').is_file())
        self.assertFalse((self.dest / 'development').exists())

    def test_collision_leaves_existing_files_untouched(self):
        existing = self.dest / 'skill-router'
        existing.mkdir(parents=True)
        (existing / 'keep.txt').write_text('user content')
        with self.assertRaises(FileExistsError):
            install(self.root, self.dest, None)
        self.assertEqual((existing / 'keep.txt').read_text(), 'user content')
        self.assertFalse((self.dest / 'development-discovery').exists())

    def test_unknown_name_and_source_overlap_rejected(self):
        with self.assertRaises(ValueError):
            install(self.root, self.dest, ['missing'])
        with self.assertRaises(ValueError):
            install(self.root, self.root / 'output', None)
        self.assertFalse(self.dest.exists())

    def test_copy_failure_rolls_back_created_skills(self):
        with patch('install_skills.shutil.copytree', side_effect=OSError('fixture failure')):
            with self.assertRaises(OSError):
                install(self.root, self.dest, None)
        self.assertEqual(list(self.dest.iterdir()), [])

    def test_source_symlink_is_rejected(self):
        link = self.root / 'skills/core/skill-router/external.md'
        try:
            link.symlink_to(self.root / 'README.md')
        except (NotImplementedError, OSError):
            self.skipTest('symlinks unavailable')
        with self.assertRaises(ValueError):
            install(self.root, self.dest, None)


if __name__ == '__main__':
    unittest.main()
