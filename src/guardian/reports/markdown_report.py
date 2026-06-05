from pathlib import Path
from datetime import datetime


def generate_report(
    project_name: str,
    findings: list[dict],
) -> str:
    """
    Generate markdown report.
    """

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / "report.md"

    with open(report_file, "w", encoding="utf-8") as f:
        f.write("# Project Guardian Pro Report\n\n")
        f.write(
            f"Generated: {datetime.now()}\n\n"
        )

        f.write(
            f"Total Issues: {len(findings)}\n\n"
        )

        for finding in findings:
            f.write(
                f"- {finding['file']} : "
                f"{finding['issue']}\n"
            )

    return str(report_file)
