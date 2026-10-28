# Project workflow and request lifecycle

![Workflow visualization](../assets/03-ingestion-pipeline.svg)

```mermaid
sequenceDiagram
  participant User
  participant React
  participant API as FastAPI
  participant Store as Catalogue
  participant Metrics as Analytics
  User->>React: Open reliability page
  React->>API: GET /api/analytics/reliability
  API->>Store: Load source-aware data
  Store-->>API: Routes + observed events + metadata
  API->>Metrics: Aggregate only valid observations
  Metrics-->>API: OTP, delay and cancellations
  API-->>React: JSON + source mode
  React-->>User: Charts and synthetic disclaimer
```

```mermaid
flowchart LR
  E[Push / PR] --> A[GitHub CI]
  A --> B[Python package install]
  B --> C[Pytest]
  C --> D[Fixture generation]
  D --> F[Power BI export]
  F --> M[Offline ML check]
  A --> N[Node 22 install]
  N --> O[React production build]
  M --> Q[Build checks]
  O --> Q
```

## Dependencies

- Python 3.10+, Node 22 recommended.
- Inputs: GTFS Schedule ZIP plus, optionally, an independently sourced observed arrival CSV.
- No GTFS-RT feed, account credentials, or operational data is preconfigured.
- Real public hosting requires an external HTTPS API and separately hosted React static files.
