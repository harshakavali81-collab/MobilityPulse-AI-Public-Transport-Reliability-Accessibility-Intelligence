# MobilityPulse AI

**MobilityPulse AI** is an end-to-end **portfolio demonstration** for exploring route reliability, arrival delay patterns, stop accessibility metadata, and data-feed diagnostics. It combines GTFS Schedule ingestion, data quality checks, historical observed-event analytics, offline machine-learning evaluation, an API, a responsive React dashboard, and Power BI export tooling.

[Setup](#local-installation--setup-guide) · [Architecture](#architecture--system-design-diagram) · [Detailed guide](PROJECT_GUIDE.md) · [Repository standard](docs/REPOSITORY_STANDARD.md)

## Visuals

![System architecture](<assets/02-system-architecture.svg>)

Existing project visual; diagrams and illustrative graphics are not evidence of a deployed application.

## Live Link / Demo

[Explore MobilityPulse AI in the browser](https://harshakavali81-collab.github.io/harshavardhan-portfolio/mobilitypulse-explorer.html). This self-contained portfolio companion provides six interactive views, fictional route maps, sample charts, and GTFS wheelchair-boarding metadata. Its default figures are **illustrative synthetic samples**, not live operator data, measured route punctuality or real ETAs.

## Key Features

| Area | Features |
|---|---|
| React UI | Overview, route explorer, stop details, reliability, accessibility, feed health |
| Python API | FastAPI endpoints with explicit provenance metadata |
| GTFS Schedule | Read ZIPs, validate required tables/columns, coordinate range and key references |
| Historical analytics | On-time windows, average delay, P90 delay, observed stop headways |
| Accessibility | Preserve GTFS wheelchair_boarding 0 as unknown, 1 reported accessible, 2 reported inaccessible |
| ML demo | RandomForest delay regression with chronological service-date split and baseline comparison |
| GTFS-Realtime | Offline parser diagnostics for TripUpdates, VehiclePositions and Alerts |
| Operations | Docker Compose, CI, optional import paths, monitoring helper modules |
| Reporting | Reproducible Power BI/Excel CSV exports and sample DAX |
| Portfolio | Standalone HTML case study, docs and ten custom SVG graphics |

<a id="visual-gallery"></a>

## Tech Stack

![Python](https://img.shields.io/badge/Python-334155?style=flat-square) ![FastAPI](https://img.shields.io/badge/FastAPI-334155?style=flat-square) ![scikit-learn](https://img.shields.io/badge/scikit--learn-334155?style=flat-square) ![Pandas](https://img.shields.io/badge/Pandas-334155?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-334155?style=flat-square) ![React](https://img.shields.io/badge/React-334155?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-334155?style=flat-square)

Dependency versions and optional packages are defined in the repository manifests.

## Architecture / System Design Diagram

[Architecture documentation / diagram](<docs/ARCHITECTURE.md>)

## Local Installation & Setup Guide

**Requirements:** Python 3.10+, Node.js 20.19+ or 22+, and internet access for dependency installation.

```bash
git clone https://github.com/harshakavali81-collab/MobilityPulse-AI-Public-Transport-Reliability-Accessibility-Intelligence.git
cd MobilityPulse-AI-Public-Transport-Reliability-Accessibility-Intelligence
python -m pip install -r requirements.txt
python -m pip install -e .
python scripts/generate_demo.py
uvicorn backend.app.main:app --reload --port 8000
```

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

- **Dashboard:** http://localhost:5173
- **API:** http://localhost:8000/api/health
- **Swagger API documentation:** http://localhost:8000/docs
- **Docker alternative:** `docker compose up --build` → http://localhost:8080

### Test and export

```bash
pytest -q
python scripts/export_powerbi.py
python -m mobilitypulse.models.train_delay_model --allow-synthetic
```

The model command writes local `data/processed/delay_model.joblib` and metadata with an evaluation vs. median baseline. Outputs are **experimental and synthetic**, not certified operational forecasts. They are gitignored.

### Integrating an authorized feed

Set `GTFS_ZIP_PATH` to a permitted static GTFS archive and optionally `OBSERVATIONS_CSV_PATH` to a separate file containing actual arrival observations. Use `uvicorn --env-file .env` after installing `python-dotenv` (or export variables in the shell). Never label Schedule-derived times as live observations. If a GTFS Schedule ZIP has no actual observations, the API reports `on_time_pct: null`, not fabricated punctuality.

See [API guide](docs/API.md), [data provenance](docs/DATA_ETHICS.md), and [deployment](docs/DEPLOYMENT.md) for caveats.

## Challenges & Solutions

**Repository organization:** this project uses `src/`, `backend/`, `frontend/`. Keeping those paths stable avoids breaking imports, asset links and deployment commands while the documentation follows a shared format. Project-specific technical limitations and prior release evidence are retained in [Project guide](PROJECT_GUIDE.md).

## Future Improvements

- Capture a reproducible end-to-end demo with runtime versions and sample inputs.
- Expand regression checks for invalid inputs and documented edge cases.
- Record measured results, data provenance and deployment limitations alongside each release.

## Scope and supporting evidence

<div align="center">
  <img src="assets/01-hero.svg" alt="MobilityPulse AI — public transport reliability and accessibility intelligence" width="100%"/>
  
  <h3>Public Transport Reliability & Accessibility Intelligence</h3>
  <p>React · FastAPI · Python · Pandas · GTFS · Scikit-learn · Docker · GitHub Actions</p>
  <p>
    <a href="#quick-start">Quick start</a> · <a href="#visual-gallery">10 Visuals</a> · <a href="#project-tree">Source tree</a> · <a href="docs/ARCHITECTURE.md">Architecture</a> · <a href="portfolio/index.html">Portfolio</a>
  </p>
  <img src="https://img.shields.io/badge/Source-SYNTHETIC%20DEMO-19a8a0" alt="Synthetic demonstration"/>
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="MIT License"/>
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Frontend-React-61DAFB" alt="React"/>
</div>

## Repository Structure

| Location | Purpose |
| --- | --- |
| `src/` | Source modules |
| `backend/` | Backend services |
| `frontend/` | Frontend interface |
| `tests/` | Tests |
| `docs/` | Documentation |
| `data/` | Data and samples |
| `powerbi/` | Power BI build assets |
| `assets/` | Visual assets |
| `scripts/` | Automation scripts |
| `.github/` | Issue forms, PR template and automated checks |

[Complete file inventory and workflow](docs/REPOSITORY_STANDARD.md). Runtime entry points retain their existing paths.

## Workflow & Tracking

Use the [bug and feature forms](https://github.com/harshakavali81-collab/MobilityPulse-AI-Public-Transport-Reliability-Accessibility-Intelligence/issues/new/choose) to define work with acceptance criteria. Keep tasks in Todo → In progress → Review → Done, and link a pull request with `Closes #<number>`. See [the maintenance workflow](docs/REPOSITORY_STANDARD.md#workflow).

## License

See [LICENSE](LICENSE) for the existing terms.
