from guardian.analyzers.health_score import (
    HealthScore,
)


def test_health_score():
    score = HealthScore.calculate(2)

    assert score == 80
