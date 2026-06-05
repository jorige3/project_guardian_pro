from pathlib import Path

IGNORE_DIRS = {
    ".git",
    "venv",
    ".venv",
    "__pycache__",
}


def scan_project(project_path: str) -> list[Path]:
    """
    Recursively scan project files.
    """

    files = []

    for path in Path(project_path).rglob("*.py"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        files.append(path)

    return files
