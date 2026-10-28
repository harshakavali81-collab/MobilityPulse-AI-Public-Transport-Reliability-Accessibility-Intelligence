# Repository tree and module responsibilities

```text
.
├── assets/                 10 original SVG project illustrations
├── backend/
│   ├── app/main.py         FastAPI application, CORS, router registration
│   ├── app/db/store.py     Source-aware catalogue and synthetic demo
│   └── app/routes/         Stops, routes, analytics, accessibility and ML
├── frontend/
│   ├── src/pages/          Six dashboard and explorer pages
│   ├── src/components/     SVG route diagram and Recharts charts
│   ├── src/api/            Central HTTP fetch wrapper
│   └── src/styles.css      Responsive visual language
├── src/mobilitypulse/
│   ├── ingestion/          Static GTFS / realtime / observations
│   ├── processing/         Validation and key integrity
│   ├── analytics/          OTP, delay and observed headways
│   ├── models/             Offline training and inference
│   └── monitoring/         Freshness and anomaly signals
├── data/                   Locally generated demo and input folders
├── scripts/                Generation, exports and diagnostics
├── powerbi/                DAX starter measures and CSV exports
├── notebooks/              Three exploratory Jupyter notebooks
├── tests/                  FastAPI, metric, GTFS, ML and realtime tests
├── docs/                   Architecture, ethics, metrics, deployment
├── portfolio/              Standalone case study and recruiter content
├── .github/workflows/      Tests and frontend build CI
├── Dockerfile(s)           Backend and frontend container definitions
└── README.md               End-to-end instructions and visual preview
```

Every directory with a Python role is importable as a package. Generated exports, model artifacts and agency data are intentionally not used as an authoritative source in the default demonstration.
