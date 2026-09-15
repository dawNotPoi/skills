#!/usr/bin/env python3
"""Check or copy this library's leaf skills; Python 3.9+, standard library only."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import unquote, urlsplit


class LibraryError(ValueError):
    """Invalid library structure or unsafe installation request."""


def metadata(path: Path) -> dict[str, str]:
    """Read the repository's deliberately restricted two-scalar frontmatter."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise LibraryError(f"Missing frontmatter: {path}")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise LibraryError(f"Unclosed frontmatter: {path}") from exc
    fields = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        match = re.fullmatch(r"(name|description): (.+)", line)
        if not match:
            raise LibraryError(f"Use plain one-line name/description fields: {path}")
        key, value = match.groups()
        if key in fields:
            raise LibraryError(f"Duplicate {key}: {path}")
        if value != value.strip() or value[0] in "|>'\"[{!&*#" or ": " in value or " #" in value:
            raise LibraryError(f"Unsupported scalar syntax for {key}: {path}")
        fields[key] = value
    name, description = fields.get("name", ""), fields.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise LibraryError(f"Invalid skill name: {path}")
    if name != path.parent.name:
        raise LibraryError(f"Folder/name mismatch: {path}")
    if not 1 <= len(description) <= 1024:
        raise LibraryError(f"Invalid description length: {path}")
    if not any(line.strip() for line in lines[end + 1:]):
        raise LibraryError(f"Missing instructions: {path}")
    return fields


def discover(root: Path) -> dict[str, Path]:
    root = root.resolve()
    skill_root = root / "skills"
    if not skill_root.is_dir():
        raise LibraryError(f"Missing skills directory: {root}")
    # Canonical source must not hide external content behind symlinks.
    if any(p.is_symlink() for p in skill_root.rglob("*")):
        raise LibraryError("Symlinks are not allowed in canonical skill sources")
    found = {}
    for path in sorted(skill_root.rglob("SKILL.md")):
        if len(path.relative_to(skill_root).parts) != 3:
            raise LibraryError(f"Expected skills/<domain>/<name>/SKILL.md: {path}")
        fields = metadata(path)
        name = fields["name"]
        if name in found:
            raise LibraryError(f"Duplicate skill name: {name}")
        found[name] = path.parent
    if not found:
        raise LibraryError("No skills found")
    return found


def prose(text: str) -> str:
    """Exclude fenced examples from the simple Markdown link check."""
    return re.sub(r"(?ms)^```[^\n]*\n.*?^```[^\n]*$", "", text)


def check(root: Path) -> int:
    root = root.resolve()
    found = discover(root)
    for required in ("README.md", "AGENTS.md", "CLAUDE.md", "skills/INDEX.md"):
        if not (root / required).is_file():
            raise LibraryError(f"Missing entry: {required}")
    entries = re.findall(r"\[([a-z0-9-]+)\]\(([^)]+/SKILL\.md)\)",
                         (root / "skills/INDEX.md").read_text(encoding="utf-8"))
    expected = {(name, (folder / "SKILL.md").relative_to(root / "skills").as_posix())
                for name, folder in found.items()}
    if len(entries) != len(expected) or set(entries) != expected:
        raise LibraryError("skills/INDEX.md is stale, duplicated, or incomplete")
    for folder in found.values():
        if not (folder.parent / "README.md").is_file():
            raise LibraryError(f"Missing domain README: {folder.parent}")
    for path in root.rglob("*.md"):
        if ".git" in path.relative_to(root).parts:
            continue
        for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^)\s]+)\)",
                                 prose(path.read_text(encoding="utf-8"))):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                raise LibraryError(f"Broken or escaping link in {path}: {target}")
    if "@AGENTS.md" not in (root / "CLAUDE.md").read_text(encoding="utf-8"):
        raise LibraryError("CLAUDE.md must refer to the shared AGENTS.md bootstrap")
    return len(found)


def install(root: Path, dest: Path, names: list[str], all_skills: bool = False,
            apply: bool = False) -> list[str]:
    """Preflight all paths; copy complete leaf folders, never overwrite."""
    root, dest = root.resolve(), dest.expanduser().resolve()
    found = discover(root)
    if all_skills and names:
        raise LibraryError("Choose --all or --skill, not both")
    chosen = sorted(found) if all_skills else sorted(set(names))
    if not chosen:
        raise LibraryError("Choose --all or at least one --skill")
    unknown = set(chosen) - set(found)
    if unknown:
        raise LibraryError(f"Unknown skills: {', '.join(sorted(unknown))}")
    if dest == root or dest.is_relative_to(root / "skills"):
        raise LibraryError("Do not install into the canonical library source")
    if dest.exists() and not dest.is_dir():
        raise LibraryError(f"Destination is not a directory: {dest}")
    for name in chosen:
        target = dest / name
        if target.exists() or target.is_symlink():
            raise LibraryError(f"Refusing to overwrite existing installation: {target}")
    actions = [f"{found[name]} -> {dest / name}" for name in chosen]
    if apply:
        dest.mkdir(parents=True, exist_ok=True)
        for name in chosen:
            # copytree rejects a destination created after preflight as well.
            shutil.copytree(found[name], dest / name)
    return actions


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list")
    commands.add_parser("check")
    sub = commands.add_parser("install")
    sub.add_argument("--dest", type=Path, required=True)
    select = sub.add_mutually_exclusive_group(required=True)
    select.add_argument("--all", action="store_true")
    select.add_argument("--skill", action="append", default=[])
    sub.add_argument("--apply", action="store_true", help="write files (default is dry-run)")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    try:
        if args.command == "check":
            print(f"OK: {check(root)} skills; layout, metadata, index and local Markdown links")
        elif args.command == "list":
            for name, folder in discover(root).items():
                print(f"{name}\t{folder.relative_to(root).as_posix()}")
        else:
            actions = install(root, args.dest, args.skill, args.all, args.apply)
            print("Copied:" if args.apply else "Dry-run; add --apply to copy:")
            print("\n".join(actions))
    except (LibraryError, OSError, UnicodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
