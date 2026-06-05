class HealthScore:
    """Calculate project health score."""

    @staticmethod
    def calculate(
        security_findings: int,
    ) -> int:
        score = 100

        score -= security_findings * 10

        return max(score, 0)
