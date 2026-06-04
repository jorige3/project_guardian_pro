from pathlib import Path
import ast


class ProjectStatsAnalyzer:
    """Analyze Python project statistics."""

    def analyze(self, files: list[Path]) -> dict[str, int]:
        stats = {
            "python_files": len(files),
            "total_lines": 0,
            "classes": 0,
            "functions": 0,
        }

        for file in files:
            try:
                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                stats["total_lines"] += len(content.splitlines())

                tree = ast.parse(content)

                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        stats["classes"] += 1

                    if isinstance(
                        node,
                        (
                            ast.FunctionDef,
                            ast.AsyncFunctionDef,
                        ),
                    ):
                        stats["functions"] += 1

            except Exception:
                continue

        return stats
