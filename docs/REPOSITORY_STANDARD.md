# Repository standard

## Layout

This repository keeps its working source paths. A shared portfolio structure does not require moving a React application, Python package, BI workbook or Verilog project into identical runtime directories.

| Area | Convention |
| --- | --- |
| Landing page | `README.md`: purpose, visuals, demo, features, stack, architecture, setup, tradeoffs and roadmap |
| Detailed reference | `PROJECT_GUIDE.md`: retained project-specific explanation and historical release notes |
| Documentation | `docs/`: design, inventory, reproduction and evidence |
| Work intake | `.github/ISSUE_TEMPLATE/`: bug and feature forms |
| Review | `.github/PULL_REQUEST_TEMPLATE.md`: linked issue, behavior and validation |
| Automation | `.github/workflows/portfolio-docs.yml`: README section and local-link checks |
| Source and tests | Existing project-specific paths listed below; no empty source/test placeholders |

## Workflow

1. Open an issue describing the user problem and measurable acceptance criteria.
2. Add it to a GitHub Project with Todo, In progress, Review and Done states when a board is configured.
3. Use a focused branch and meaningful commits, such as `docs: correct local setup paths` or `fix(api): reject malformed input`.
4. Run the project's documented checks and `python scripts/check_portfolio_docs.py`.
5. Open a pull request with actual validation results and `Closes #<issue-number>`.
6. Merge after review; record release evidence and update the issue/board.

Board creation, profile pins, repository social previews and milestone settings require account-level configuration. This file does not claim those settings have been applied.

## Validation scope

The documentation check validates the landing-page headings and local link targets only. It does not execute models, certify test coverage, inspect Git history for secrets, verify external websites, or prove production readiness. Existing application workflows remain the source of runtime CI evidence.

Keep credentials in local environment variables. A gitignore rule does not remove secrets already tracked or committed. Use only permitted sample data in public demos.

## Inventory at standardization

The following are the pre-existing public project files. New standardization files are described above. Historical guides may mention external bundles that are not part of this list.

- [`LICENSE`](<../LICENSE>)
- [`Makefile`](<../Makefile>)
- [`README.md`](<../README.md>)
- [`SECURITY.md`](<../SECURITY.md>)
- [`assets`](<../assets>)
- [`assets/01-hero.svg`](<../assets/01-hero.svg>)
- [`assets/02-system-architecture.svg`](<../assets/02-system-architecture.svg>)
- [`assets/03-ingestion-pipeline.svg`](<../assets/03-ingestion-pipeline.svg>)
- [`assets/04-gtfs-entity-model.svg`](<../assets/04-gtfs-entity-model.svg>)
- [`assets/05-route-network-map.svg`](<../assets/05-route-network-map.svg>)
- [`assets/06-route-reliability-bars.svg`](<../assets/06-route-reliability-bars.svg>)
- [`assets/07-delay-distribution.svg`](<../assets/07-delay-distribution.svg>)
- [`assets/08-headway-trend.svg`](<../assets/08-headway-trend.svg>)
- [`assets/09-accessibility-coverage.svg`](<../assets/09-accessibility-coverage.svg>)
- [`assets/10-feed-quality-status.svg`](<../assets/10-feed-quality-status.svg>)
- [`assets/README.md`](<../assets/README.md>)
- [`backend`](<../backend>)
- [`backend/Dockerfile`](<../backend/Dockerfile>)
- [`backend/app`](<../backend/app>)
- [`backend/app/__init__.py`](<../backend/app/__init__.py>)
- [`backend/app/db`](<../backend/app/db>)
- [`backend/app/db/__init__.py`](<../backend/app/db/__init__.py>)
- [`backend/app/db/schema.sql`](<../backend/app/db/schema.sql>)
- [`backend/app/db/store.py`](<../backend/app/db/store.py>)
- [`backend/app/main.py`](<../backend/app/main.py>)
- [`backend/app/routes`](<../backend/app/routes>)
- [`backend/app/routes/__init__.py`](<../backend/app/routes/__init__.py>)
- [`backend/app/routes/accessibility.py`](<../backend/app/routes/accessibility.py>)
- [`backend/app/routes/analytics.py`](<../backend/app/routes/analytics.py>)
- [`backend/app/routes/delays.py`](<../backend/app/routes/delays.py>)
- [`backend/app/routes/routes.py`](<../backend/app/routes/routes.py>)
- [`backend/app/routes/stops.py`](<../backend/app/routes/stops.py>)
- [`backend/app/security.py`](<../backend/app/security.py>)
- [`data`](<../data>)
- [`data/interim`](<../data/interim>)
- [`data/interim/.gitkeep`](<../data/interim/.gitkeep>)
- [`data/processed`](<../data/processed>)
- [`data/processed/.gitkeep`](<../data/processed/.gitkeep>)
- [`data/raw`](<../data/raw>)
- [`data/raw/.gitkeep`](<../data/raw/.gitkeep>)
- [`data/synthetic`](<../data/synthetic>)
- [`data/synthetic/README.md`](<../data/synthetic/README.md>)
- [`docker-compose.yml`](<../docker-compose.yml>)
- [`docs`](<../docs>)
- [`docs/API.md`](<../docs/API.md>)
- [`docs/ARCHITECTURE.md`](<../docs/ARCHITECTURE.md>)
- [`docs/CLOUD_HOSTING.md`](<../docs/CLOUD_HOSTING.md>)
- [`docs/DATA_ETHICS.md`](<../docs/DATA_ETHICS.md>)
- [`docs/DATA_PIPELINE.md`](<../docs/DATA_PIPELINE.md>)
- [`docs/DEPLOYMENT.md`](<../docs/DEPLOYMENT.md>)
- [`docs/HYDERABAD_FEED.md`](<../docs/HYDERABAD_FEED.md>)
- [`docs/INTERVIEW.md`](<../docs/INTERVIEW.md>)
- [`docs/LIVE_DATA_INTEGRATION.md`](<../docs/LIVE_DATA_INTEGRATION.md>)
- [`docs/METRICS.md`](<../docs/METRICS.md>)
- [`docs/MODEL_CARD.md`](<../docs/MODEL_CARD.md>)
- [`docs/PROJECT_TREE.md`](<../docs/PROJECT_TREE.md>)
- [`docs/PROJECT_WORKFLOW.md`](<../docs/PROJECT_WORKFLOW.md>)
- [`docs/ROADMAP.md`](<../docs/ROADMAP.md>)
- [`docs/SECURITY_HARDENING.md`](<../docs/SECURITY_HARDENING.md>)
- [`docs/STATIC_DEPLOYMENT.md`](<../docs/STATIC_DEPLOYMENT.md>)
- [`docs/TROUBLESHOOTING.md`](<../docs/TROUBLESHOOTING.md>)
- [`frontend`](<../frontend>)
- [`frontend/.gitignore`](<../frontend/.gitignore>)
- [`frontend/Dockerfile`](<../frontend/Dockerfile>)
- [`frontend/index.html`](<../frontend/index.html>)
- [`frontend/nginx.conf`](<../frontend/nginx.conf>)
- [`frontend/package.json`](<../frontend/package.json>)
- [`frontend/public`](<../frontend/public>)
- [`frontend/public/logo.svg`](<../frontend/public/logo.svg>)
- [`frontend/src`](<../frontend/src>)
- [`frontend/src/App.jsx`](<../frontend/src/App.jsx>)
- [`frontend/src/api`](<../frontend/src/api>)
- [`frontend/src/api/client.js`](<../frontend/src/api/client.js>)
- [`frontend/src/components`](<../frontend/src/components>)
- [`frontend/src/components/Charts.jsx`](<../frontend/src/components/Charts.jsx>)
- [`frontend/src/components/RouteMap.jsx`](<../frontend/src/components/RouteMap.jsx>)
- [`frontend/src/main.jsx`](<../frontend/src/main.jsx>)
- [`frontend/src/pages`](<../frontend/src/pages>)
- [`frontend/src/pages/Accessibility.jsx`](<../frontend/src/pages/Accessibility.jsx>)
- [`frontend/src/pages/Dashboard.jsx`](<../frontend/src/pages/Dashboard.jsx>)
- [`frontend/src/pages/FeedStatus.jsx`](<../frontend/src/pages/FeedStatus.jsx>)
- [`frontend/src/pages/Reliability.jsx`](<../frontend/src/pages/Reliability.jsx>)
- [`frontend/src/pages/RouteExplorer.jsx`](<../frontend/src/pages/RouteExplorer.jsx>)
- [`frontend/src/pages/StopDetails.jsx`](<../frontend/src/pages/StopDetails.jsx>)
- [`frontend/src/styles.css`](<../frontend/src/styles.css>)
- [`frontend/vite.config.js`](<../frontend/vite.config.js>)
- [`notebooks`](<../notebooks>)
- [`notebooks/01_gtfs_exploration.ipynb`](<../notebooks/01_gtfs_exploration.ipynb>)
- [`notebooks/02_reliability_analytics.ipynb`](<../notebooks/02_reliability_analytics.ipynb>)
- [`notebooks/03_delay_model.ipynb`](<../notebooks/03_delay_model.ipynb>)
- [`portfolio`](<../portfolio>)
- [`portfolio/CASE_STUDY.md`](<../portfolio/CASE_STUDY.md>)
- [`portfolio/index.html`](<../portfolio/index.html>)
- [`powerbi`](<../powerbi>)
- [`powerbi/README.md`](<../powerbi/README.md>)
- [`powerbi/queries.sql`](<../powerbi/queries.sql>)
- [`pyproject.toml`](<../pyproject.toml>)
- [`render.yaml`](<../render.yaml>)
- [`requirements.txt`](<../requirements.txt>)
- [`scripts`](<../scripts>)
- [`scripts/download_hyderabad_schedule.py`](<../scripts/download_hyderabad_schedule.py>)
- [`scripts/export_powerbi.py`](<../scripts/export_powerbi.py>)
- [`scripts/export_static_api.py`](<../scripts/export_static_api.py>)
- [`scripts/generate_demo.py`](<../scripts/generate_demo.py>)
- [`scripts/poll_rt.py`](<../scripts/poll_rt.py>)
- [`scripts/refresh_realtime.py`](<../scripts/refresh_realtime.py>)
- [`scripts/validate_gtfs.py`](<../scripts/validate_gtfs.py>)
- [`src`](<../src>)
- [`src/mobilitypulse`](<../src/mobilitypulse>)
- [`src/mobilitypulse/__init__.py`](<../src/mobilitypulse/__init__.py>)
- [`src/mobilitypulse/analytics`](<../src/mobilitypulse/analytics>)
- [`src/mobilitypulse/analytics/__init__.py`](<../src/mobilitypulse/analytics/__init__.py>)
- [`src/mobilitypulse/analytics/headway.py`](<../src/mobilitypulse/analytics/headway.py>)
- [`src/mobilitypulse/analytics/on_time_performance.py`](<../src/mobilitypulse/analytics/on_time_performance.py>)
- [`src/mobilitypulse/analytics/route_reliability.py`](<../src/mobilitypulse/analytics/route_reliability.py>)
- [`src/mobilitypulse/ingestion`](<../src/mobilitypulse/ingestion>)
- [`src/mobilitypulse/ingestion/__init__.py`](<../src/mobilitypulse/ingestion/__init__.py>)
- [`src/mobilitypulse/ingestion/gtfs_realtime_client.py`](<../src/mobilitypulse/ingestion/gtfs_realtime_client.py>)
- [`src/mobilitypulse/ingestion/gtfs_realtime_loader.py`](<../src/mobilitypulse/ingestion/gtfs_realtime_loader.py>)
- [`src/mobilitypulse/ingestion/gtfs_static_loader.py`](<../src/mobilitypulse/ingestion/gtfs_static_loader.py>)
- [`src/mobilitypulse/ingestion/ogd_loader.py`](<../src/mobilitypulse/ingestion/ogd_loader.py>)
- [`src/mobilitypulse/ingestion/realtime_predictions.py`](<../src/mobilitypulse/ingestion/realtime_predictions.py>)
- [`src/mobilitypulse/models`](<../src/mobilitypulse/models>)
- [`src/mobilitypulse/models/__init__.py`](<../src/mobilitypulse/models/__init__.py>)
- [`src/mobilitypulse/models/evaluate.py`](<../src/mobilitypulse/models/evaluate.py>)
- [`src/mobilitypulse/models/predict_delay.py`](<../src/mobilitypulse/models/predict_delay.py>)
- [`src/mobilitypulse/models/train_delay_model.py`](<../src/mobilitypulse/models/train_delay_model.py>)
- [`src/mobilitypulse/monitoring`](<../src/mobilitypulse/monitoring>)
- [`src/mobilitypulse/monitoring/__init__.py`](<../src/mobilitypulse/monitoring/__init__.py>)
- [`src/mobilitypulse/monitoring/feed_anomalies.py`](<../src/mobilitypulse/monitoring/feed_anomalies.py>)
- [`src/mobilitypulse/monitoring/feed_freshness.py`](<../src/mobilitypulse/monitoring/feed_freshness.py>)
- [`src/mobilitypulse/processing`](<../src/mobilitypulse/processing>)
- [`src/mobilitypulse/processing/__init__.py`](<../src/mobilitypulse/processing/__init__.py>)
- [`src/mobilitypulse/processing/clean.py`](<../src/mobilitypulse/processing/clean.py>)
- [`src/mobilitypulse/processing/features.py`](<../src/mobilitypulse/processing/features.py>)
- [`src/mobilitypulse/processing/validate_gtfs.py`](<../src/mobilitypulse/processing/validate_gtfs.py>)
- [`tests`](<../tests>)
- [`tests/conftest.py`](<../tests/conftest.py>)
- [`tests/test_api.py`](<../tests/test_api.py>)
- [`tests/test_gtfs.py`](<../tests/test_gtfs.py>)
- [`tests/test_metrics.py`](<../tests/test_metrics.py>)
- [`tests/test_ml.py`](<../tests/test_ml.py>)
- [`tests/test_processing.py`](<../tests/test_processing.py>)
- [`tests/test_realtime.py`](<../tests/test_realtime.py>)
- [`tests/test_realtime_predictions.py`](<../tests/test_realtime_predictions.py>)
- [`tests/test_security_realtime_client.py`](<../tests/test_security_realtime_client.py>)
- [`tests/test_static_export.py`](<../tests/test_static_export.py>)
- [`vercel.json`](<../vercel.json>)
