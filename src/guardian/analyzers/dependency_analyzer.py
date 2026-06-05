from pathlib import Path
import tomllib


class DependencyAnalyzer:
    """Analyze project dependencies."""

    def analyze(self, project_root: str) -> dict:
        pyproject = Path(project_root) / "pyproject.toml"

        if not pyproject.exists():
            return {"dependencies": []}

        with open(pyproject, "rb") as f:
            data = tomllib.load(f)

        deps = data.get("project", {}).get(
            "dependencies",
            [],
        )

        return {
            "dependencies": deps,
            "count": len(deps),
        }