import click

from src.utils.scanner import scan_project
from src.analyzers.security_analyzer import SecurityAnalyzer
from src.reports.markdown_report import generate_report


@click.command()
@click.argument("project_path")
def run(project_path: str) -> None:
    """
    Analyze a project and generate a report.
    """

    print(f"Scanning: {project_path}")

    files = scan_project(project_path)

    analyzer = SecurityAnalyzer()

    findings = analyzer.analyze(files)

    report_path = generate_report(project_path, findings)

    print(f"Files scanned: {len(files)}")
    print(f"Issues found: {len(findings)}")
    print(f"Report generated: {report_path}")
