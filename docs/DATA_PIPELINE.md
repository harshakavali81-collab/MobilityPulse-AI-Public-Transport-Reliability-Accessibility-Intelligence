# Data pipeline and lineage

![Pipeline](../assets/03-ingestion-pipeline.svg)

```mermaid
flowchart TD
  A[GET authorized GTFS ZIP] --> B[Read agency, routes, trips, stops, stop_times]
  B --> C{Required columns and references valid?}
  C -- no --> D[Fail with validation error]
  C -- yes --> E[Build route-stop catalogue]
  F[Actual arrival event CSV] --> G[Require source and timestamp columns]
  G --> H[Calculate observed_delay_minutes]
  E --> I[Source-aware API]
  H --> I
  J[Synthetic generator - seed 42] --> I
  I --> K[On-time / Headway / Accessibility]
  K --> L[Dashboard]
  K --> M[Power BI CSV]
  K --> N[ML temporal evaluation]
```

**Data contracts:** Schedule defines planned service. Observed arrivals require genuine actual timestamps and traceable source. Explicit cancellation flags are recorded separately from observed service. On-time windows are defined in [metrics](METRICS.md). Unknown stop accessibility values remain unknown. An actual trip source needs agency approval and independent review before operational use.
