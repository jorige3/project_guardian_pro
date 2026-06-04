from pathlib import Path


class SecurityAnalyzer:
    """
    Detect basic security issues.
    """

    DANGEROUS_PATTERNS = [
        "eval(",
        "exec(",
    ]

    def analyze(self, files: list[Path]) -> list[dict]:
        findings = []

        for file in files:
            try:
                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                for pattern in self.DANGEROUS_PATTERNS:
                    if pattern in content:
                        findings.append(
                            {
                                "file": str(file),
                                "issue": f"Found {pattern}",
                            }
                        )

            except Exception:
                continue

        return findings
