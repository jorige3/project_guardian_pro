from src.analyzers.project_stats import (
    ProjectStatsAnalyzer,
)


def test_project_stats_creation():
    analyzer = ProjectStatsAnalyzer()

    assert analyzer is not None
