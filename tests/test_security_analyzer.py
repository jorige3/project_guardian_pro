from src.analyzers.security_analyzer import (
    SecurityAnalyzer,
)


def test_analyzer_creation():
    analyzer = SecurityAnalyzer()

    assert analyzer is not None
