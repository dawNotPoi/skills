"""Copy selected leaf skills into an explicit host directory without overwriting."""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys

from check_library import ROOT, catalog


def install(root: Path, destination: Path, names: list[str] | None,
            dry_run: bool = False) -> list[str]:
    root = root.resolve()
    destination = destination.expanduser().resolve()
    if destination.is_relative_to(root) or root.is_relative_to(destination):
        raise ValueError('destination must not contain or be inside the source library')
    entries = catalog(root)
    selected = sorted(entries if names is None else set(names))
    if not selected:
        raise ValueError('select at least one skill')
    unknown = set(selected) - entries.keys()
    if unknown:
        raise ValueError('unknown skills: ' + ', '.join(sorted(unknown)))
    if destination.exists() and not destination.is_dir():
        raise ValueError('destination is not a directory')
    for name in selected:
        target = destination / name
        if target.exists() or target.is_symlink():
            raise FileExistsError(f'refusing to overwrite {target}')
    index = root / 'skills/INDEX.md'
    if 'skill-router' in selected and not index.is_file():
        raise ValueError('router installation requires the source index')
    if dry_run:
        return selected
    destination.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    try:
        for name in selected:
            target = destination / name
            # Exclusive creation: a concurrent/pre-existing target is never owned.
            target.mkdir()
            created.append(target)
            shutil.copytree(entries[name], target, dirs_exist_ok=True)
            if name == 'skill-router':
                references = target / 'references'
                references.mkdir(exist_ok=True)
                header = ('<!-- Generated routing snapshot; not an installed-skill inventory. '
                          'Paths below are source-library-relative. -->\n\n')
                (references / 'library-index.md').write_text(
                    header + index.read_text(encoding='utf-8'), encoding='utf-8')
    except Exception:
        for path in reversed(created):
            shutil.rmtree(path)
        raise
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', required=True, type=Path)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--all', action='store_true')
    group.add_argument('--skill', action='append', dest='skills')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        names = install(ROOT, args.dest, None if args.all else args.skills, args.dry_run)
    except (ValueError, OSError) as exc:
        print(f'Install failed: {exc}', file=sys.stderr)
        return 1
    action = 'Would install' if args.dry_run else 'Installed'
    print(f'{action} {len(names)} skills: ' + ', '.join(names))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
