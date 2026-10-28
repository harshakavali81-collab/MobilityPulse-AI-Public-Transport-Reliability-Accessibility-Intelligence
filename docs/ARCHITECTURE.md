# Architecture and source-of-truth boundaries

![Architecture diagram](../assets/02-system-architecture.svg)

## Responsibilities

```mermaid
flowchart LR
  subgraph ingest[Ingestion]
    A[Authorized GTFS Schedule] --> V[Schema + FK Validation]
    B[Permitted Actual Events] --> Q[Observed-event Verification]
  end
  D[Deterministic Demo] --> C[Source-Aware Catalog]
  V --> C
  Q --> C
  C --> R[Route, Stop and Accessibility API]
  C --> S[Observed-event Metric Service]
  S --> M[Time-Split ML Evaluation]
  R --> F[React Interface]
  S --> F
  S --> P[CSV / Power BI]
  M --> L[Optional Offline Artifact]
  L --> R
```

The data mode field identifies `synthetic`, `schedule_only`, or `externally_supplied_observations`. The externally supplied category is **not a certification of correctness**. The application does not mix GTFS schedules into the set of actually observed arrivals. A configured ZIP with no observation CSV returns null delay/OTP values. No persistent hosted database is included: the backend in this portfolio holds a per-process cached catalogue. Adding production storage requires migration, credentials, retention design, authentication and data licensing.
