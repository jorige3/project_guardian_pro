import click

from src.utils.scanner import scan_project
from src.analyzers.security_analyzer import SecurityAnalyzer
from src.analyzers.project_stats import ProjectStatsAnalyzer
from src.analyzers.health_score import HealthScore
from src.reports.markdown_report import generate_report
from src.utils.logger import setup_logger

logger = setup_logger()


@click.command()
@click.argument("project_path")
def run(project_path: str) -> None:
    """
    Analyze a project and generate a report.
    """
    logger.info(
        f"Starting scan for {project_path}"
    )

    click.echo("Project Guardian Pro")
    click.echo("=" * 40)

    click.echo(f"Scanning: {project_path}")

    files = scan_project(project_path)
    
    logger.info(
        f"Files scanned: {len(files)}"
    )

    security_analyzer = SecurityAnalyzer()
    security_findings = security_analyzer.analyze(files)

    stats_analyzer = ProjectStatsAnalyzer()
    stats = stats_analyzer.analyze(files)

    health_score = HealthScore.calculate(
        len(security_findings)
    )

    report_path = generate_report(
        project_path,
        security_findings,
    )
 
    logger.info(
        f"Report generated: {report_path}"
    )
 
    click.echo("")
    click.echo("Project Statistics")
    click.echo("-" * 20)
    click.echo(f"Python Files : {stats['python_files']}")
    click.echo(f"Total Lines  : {stats['total_lines']}")
    click.echo(f"Classes      : {stats['classes']}")
    click.echo(f"Functions    : {stats['functions']}")

    click.echo("")
    click.echo(f"Security Issues : {len(security_findings)}")
    click.echo(f"Health Score    : {health_score}/100")

    click.echo("")
    click.echo(f"Report generated: {report_path}")