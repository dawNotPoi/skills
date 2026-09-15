"""Structural and installer unit tests; these do not evaluate an LLM."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from library import LibraryError, check, discover, install, metadata


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "library"
        self.root.mkdir()
        self.dest = Path(self.temp.name) / "installed"
        self.add_skill("alpha")
        for name in ("README.md", "AGENTS.md"):
            (self.root / name).write_text("# Entry\n", encoding="utf-8")
        (self.root / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
        self.write_index()

    def add_skill(self, name, domain="development"):
        folder = self.root / "skills" / domain / name
        folder.mkdir(parents=True)
        (folder.parent / "README.md").write_text("# Domain\n", encoding="utf-8")
        (folder / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Use for a bounded task.\n---\n\n# Instructions\n",
            encoding="utf-8")
        return folder

    def write_index(self):
        entries = [f"[{name}]({folder.relative_to(self.root / 'skills')}/SKILL.md)"
                   for name, folder in discover(self.root).items()]
        (self.root / "skills/INDEX.md").write_text("\n".join(entries), encoding="utf-8")

    def test_valid_library(self):
        self.assertEqual(check(self.root), 1)

    def test_duplicate_name_rejected(self):
        self.add_skill("alpha", "writing")
        with self.assertRaises(LibraryError):
            discover(self.root)

    def test_flat_source_rejected(self):
        folder = self.root / "skills/flat"
        folder.mkdir()
        (folder / "SKILL.md").write_text("---\nname: flat\ndescription: Task.\n---\nBody\n")
        with self.assertRaises(LibraryError):
            discover(self.root)

    def test_name_mismatch_rejected(self):
        path = self.root / "skills/development/alpha/SKILL.md"
        path.write_text(path.read_text().replace("name: alpha", "name: beta"))
        with self.assertRaises(LibraryError):
            metadata(path)

    def test_long_description_rejected(self):
        path = self.root / "skills/development/alpha/SKILL.md"
        path.write_text(f"---\nname: alpha\ndescription: {'x' * 1025}\n---\nBody\n")
        with self.assertRaises(LibraryError):
            metadata(path)

    def test_duplicate_metadata_rejected(self):
        path = self.root / "skills/development/alpha/SKILL.md"
        path.write_text(path.read_text().replace("name: alpha", "name: alpha\nname: alpha"))
        with self.assertRaises(LibraryError):
            metadata(path)

    def test_missing_body_rejected(self):
        path = self.root / "skills/development/alpha/SKILL.md"
        path.write_text("---\nname: alpha\ndescription: Task.\n---\n")
        with self.assertRaises(LibraryError):
            metadata(path)

    def test_stale_index_rejected(self):
        self.add_skill("beta")
        with self.assertRaises(LibraryError):
            check(self.root)

    def test_broken_link_rejected(self):
        (self.root / "README.md").write_text("[missing](missing.md)\n")
        with self.assertRaises(LibraryError):
            check(self.root)

    def test_fenced_example_ignored(self):
        (self.root / "README.md").write_text("```md\n[example](not-real.md)\n```\n")
        self.assertEqual(check(self.root), 1)

    def test_dry_run_writes_nothing(self):
        self.assertEqual(len(install(self.root, self.dest, [], all_skills=True)), 1)
        self.assertFalse(self.dest.exists())

    def test_apply_copies_local_resources(self):
        folder = self.root / "skills/development/alpha"
        (folder / "references").mkdir()
        (folder / "references/guide.md").write_text("Local guide\n")
        install(self.root, self.dest, ["alpha"], apply=True)
        self.assertEqual((self.dest / "alpha/references/guide.md").read_text(), "Local guide\n")
        self.assertFalse((self.dest / "development").exists())

    def test_conflict_preflight_prevents_partial_install(self):
        self.add_skill("beta")
        (self.dest / "beta").mkdir(parents=True)
        with self.assertRaises(LibraryError):
            install(self.root, self.dest, [], all_skills=True, apply=True)
        self.assertFalse((self.dest / "alpha").exists())

    def test_unknown_name_rejected(self):
        with self.assertRaises(LibraryError):
            install(self.root, self.dest, ["missing"], apply=True)
        self.assertFalse(self.dest.exists())

    def test_canonical_source_destination_rejected(self):
        with self.assertRaises(LibraryError):
            install(self.root, self.root / "skills", ["alpha"], apply=True)

    def test_source_symlink_rejected(self):
        try:
            (self.root / "skills/development/link").symlink_to(self.dest)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        with self.assertRaises(LibraryError):
            discover(self.root)

    def test_existing_file_not_overwritten(self):
        self.dest.mkdir()
        (self.dest / "alpha").write_text("keep me")
        with self.assertRaises(LibraryError):
            install(self.root, self.dest, ["alpha"], apply=True)
        self.assertEqual((self.dest / "alpha").read_text(), "keep me")


if __name__ == "__main__":
    unittest.main()
