"""Publish a clean SharePoint-ready copy of this template.

The Git repository remains the maintainer source of truth. This script creates
a copyable folder for non-technical users without Git metadata, caches, or
other generated files.
"""

from __future__ import annotations

import argparse
import fnmatch
import os
import shutil
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "dist" / "Codex-SharePoint-Template"

EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    "node_modules",
    "dist",
    "tmp",
    "htmlcov",
    ".trash",
    "cache",
}

EXCLUDED_FILES = {
    ".DS_Store",
    "Thumbs.db",
    "desktop.ini",
    ".coverage",
}

EXCLUDED_PATTERNS = [
    ".env",
    ".env.*",
    "*.log",
    "*.tmp",
    "*.temp",
    "*.bak",
    "*.swp",
    "*.pyc",
    "*.pyo",
    "workspace*.json",
]


def relative_parts(path: Path) -> tuple[str, ...]:
    try:
        return path.relative_to(ROOT).parts
    except ValueError:
        return path.parts


def should_exclude(path: Path, is_dir: bool) -> bool:
    name = path.name

    if is_dir and name in EXCLUDED_DIRS:
        return True

    if not is_dir and name in EXCLUDED_FILES:
        return True

    if any(fnmatch.fnmatch(name, pattern) for pattern in EXCLUDED_PATTERNS):
        return True

    parts = relative_parts(path)
    if len(parts) >= 3 and parts[0] == "wiki" and parts[1] == ".obsidian" and parts[2] == "cache":
        return True

    return False


def ignore_names(directory: str, names: list[str]) -> set[str]:
    ignored: set[str] = set()
    directory_path = Path(directory)

    for name in names:
        candidate = directory_path / name
        if should_exclude(candidate, candidate.is_dir()):
            ignored.add(name)

    return ignored


def validate_output_path(output: Path) -> Path:
    resolved = output.resolve()
    if resolved == ROOT:
        raise ValueError("Output path cannot be the repository root.")

    try:
        resolved.relative_to(ROOT)
    except ValueError:
        return resolved

    if not resolved.is_relative_to(ROOT / "dist"):
        raise ValueError("Output paths inside the repository must be under dist/.")

    return resolved


def make_writable(path: Path) -> None:
    try:
        os.chmod(path, stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)
    except OSError:
        pass


def retry_after_chmod(function, path: str, _exc_info) -> None:
    make_writable(Path(path))
    function(path)


def make_tree_writable(path: Path) -> None:
    make_writable(path)
    for child in path.rglob("*"):
        make_writable(child)


def publish(output: Path, replace: bool) -> Path:
    destination = validate_output_path(output)
    default_destination = DEFAULT_OUTPUT.resolve()

    if destination.exists():
        if destination == default_destination or replace:
            make_tree_writable(destination)
            shutil.rmtree(destination, onerror=retry_after_chmod)
        else:
            raise FileExistsError(
                f"{destination} already exists. Choose another output path or pass --replace."
            )

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT, destination, ignore=ignore_names)
    make_tree_writable(destination)
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a clean SharePoint-ready copy of the Codex template."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output folder. Defaults to {DEFAULT_OUTPUT}.",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Replace an existing non-default output folder.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        destination = publish(args.output, args.replace)
    except Exception as exc:
        print(f"Publish failed: {exc}")
        return 1

    print("SharePoint-ready template published")
    print("===================================")
    print(f"Output: {destination}")
    print()
    print("Next steps:")
    print("1. Review the output folder.")
    print("2. Copy or sync that folder into the read-only SharePoint template library.")
    print("3. Have users copy the published folder into their own SharePoint-synced workspace.")
    print("4. In copied projects, ask Codex for: setup wizard")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
