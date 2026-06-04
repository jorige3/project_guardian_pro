# Project Guardian Pro

## Overview

Project Guardian Pro is a Python-based project analysis tool that helps developers evaluate project health through automated security scanning, project statistics, health scoring, reporting, and logging.

The goal is to provide a lightweight command-line utility that quickly analyzes a Python project and generates actionable insights.

---

## Features

### Security Analysis

* Detects potentially dangerous code patterns
* Identifies usage of functions such as `eval()` and `exec()`
* Generates security findings for review

### Project Statistics

* Counts Python files
* Counts total lines of code
* Counts classes and functions
* Provides project metrics at a glance

### Health Scoring

* Calculates a simple project health score
* Reduces score based on detected security findings

### Reporting

* Generates Markdown reports
* Summarizes findings and project metrics

### Logging

* Records analysis activity
* Creates audit logs for troubleshooting and review

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/jorige3/project_guardian_pro.git
cd project_guardian_pro
```

### Install Dependencies

```bash
uv sync
```

---

## Usage

Analyze the current project:

```bash
uv run main.py .
```

Analyze another project:

```bash
uv run main.py /path/to/project
```

---

## Example Output

```text
Project Guardian Pro
========================================
Scanning: .

Project Statistics
--------------------
Python Files : 17
Total Lines  : 293
Classes      : 3
Functions    : 12

Security Issues : 2
Health Score    : 80/100

Report generated: reports/report.md
```

---

## Project Structure

```text
project_guardian_pro/

├── src/
│   ├── analyzers/
│   ├── reports/
│   ├── utils/
│   └── cli.py
│
├── tests/
├── reports/
├── logs/
├── main.py
├── pyproject.toml
└── README.md
```

---

## Development

Run tests:

```bash
uv run pytest
```

Run linting:

```bash
uv run ruff check .
```

Run type checking:

```bash
uv run mypy src
```

Format code:

```bash
uv run black .
```

---

## Current Features

* Security Analyzer
* Project Statistics Analyzer
* Health Score Calculator
* Markdown Reporting
* Application Logging
* Unit Testing
* Ruff Linting
* Black Formatting
* Mypy Type Checking

---

## Roadmap

### Version 0.2.0

* Dependency Analyzer
* Enhanced Markdown Reports
* Configuration File Support
* HTML Reports

### Version 0.3.0

* Severity Levels
* JSON Reports
* GitHub Actions CI/CD
* Risk Scoring

---

## License

MIT License
