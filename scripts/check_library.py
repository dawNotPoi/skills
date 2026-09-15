"""Validate this library's layout, simple frontmatter, index and local links."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'\[[^\]\n]*\]\(([^)\n]+)\)')


def metadata(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding='utf-8').splitlines()
    if not lines or lines[0] != '---':
        raise ValueError(f'{path}: missing frontmatter')
    try:
        end = lines.index('---', 1)
    except ValueError as exc:
        raise ValueError(f'{path}: unclosed frontmatter') from exc
    result = {}
    for key in ('name', 'description'):
        values = [line[len(key) + 1:].strip() for line in lines[1:end]
                  if line.startswith(key + ':')]
        if len(values) != 1 or not values[0] or values[0] in ('>', '|', '>-', '|-'):
            raise ValueError(f'{path}: {key} must be a nonempty single-line value')
        result[key] = values[0].strip('\"\'')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', result['name']):
        raise ValueError(f'{path}: invalid skill name')
    if len(result['name']) > 64 or len(result['description']) > 1024:
        raise ValueError(f'{path}: metadata exceeds size limit')
    return result


def catalog(root: Path) -> dict[str, Path]:
    root = root.resolve()
    skills = root / 'skills'
    result: dict[str, Path] = {}
    for path in skills.rglob('*'):
        if path.is_symlink():
            raise ValueError(f'{path}: source symlinks are not supported by this installer')
    for path in sorted(skills.rglob('SKILL.md')):
        relative = path.relative_to(root)
        if len(relative.parts) != 4:
            raise ValueError(f'{relative}: expected skills/<domain>/<name>/SKILL.md')
        name = metadata(path)['name']
        if path.parent.name != name:
            raise ValueError(f'{relative}: name differs from leaf directory')
        if name in result:
            raise ValueError(f'{relative}: duplicate skill name {name}')
        result[name] = path.parent
    if not result:
        raise ValueError('no leaf skills found')
    return result


def local_links(path: Path) -> list[str]:
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'(?ms)^```[^\n]*\n.*?^```[^\n]*(?:\n|$)', '', text)
    return LINK.findall(text)


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    try:
        entries = catalog(root)
    except (ValueError, OSError) as exc:
        return [str(exc)]
    for required in ('README.md', 'AGENTS.md', 'CLAUDE.md', 'skills/INDEX.md',
                     'docs/usage.md', 'tests/behavior-cases.md'):
        if not (root / required).is_file():
            errors.append(f'missing entry/resource: {required}')
    index = root / 'skills/INDEX.md'
    if index.is_file():
        paths = [unquote(urlsplit(link).path) for link in local_links(index)
                 if urlsplit(link).path.endswith('/SKILL.md')]
        actual = Counter((index.parent / path).resolve() for path in paths)
        expected = {(folder / 'SKILL.md').resolve() for folder in entries.values()}
        if set(actual) != expected or any(count != 1 for count in actual.values()):
            errors.append('index must list every leaf SKILL.md exactly once')
        for line in index.read_text(encoding='utf-8').splitlines():
            links = LINK.findall(line)
            for link in links:
                if not urlsplit(link).path.endswith('/SKILL.md'):
                    continue
                target = (index.parent / unquote(urlsplit(link).path)).resolve()
                if target.is_file():
                    name = metadata(target)['name']
                    if f'`{name}`' not in line:
                        errors.append(f'index row does not identify {name}')
    for path in root.rglob('*.md'):
        if any(part in ('.git', '__pycache__', '.venv') for part in path.relative_to(root).parts):
            continue
        for link in local_links(path):
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f'{path.relative_to(root)}: broken local link {link}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: {len(catalog(args.root))} skills; layout, metadata, index and local links')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
