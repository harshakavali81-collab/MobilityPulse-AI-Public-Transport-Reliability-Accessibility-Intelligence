# REST API reference

Base: `http://localhost:8000/api`. Interactive OpenAPI: `http://localhost:8000/docs`.

| Method | Path | Meaning |
|---|---|---|
| GET | /health | API liveness |
| GET | /overview | Demo or externally supplied summary + provenance |
| GET | /routes | Route directory |
| GET | /routes/{route_id} | Route details and ordered stops |
| GET | /stops | Stop directory |
| GET | /stops/{stop_id} | Stop detail and reliability |
| GET | /analytics/reliability | Observed route scorecards |
| GET | /analytics/trends | Observed metrics by service date |
| GET | /analytics/headways | Median observed same-stop headways |
| GET | /accessibility | Wheelchair code interpretation |
| GET | /alerts | Demonstration notices, not official live alerts |
| GET | /feed/status | Live feed connection status |
| POST | /delays/predict | Experimental model estimate; 503 if model missing |

Prediction sample body:

```json
{"hour":9,"day_of_week":1,"preceding_delay_minutes":4,"stop_sequence":2}
```

The model is trained locally by running `python -m mobilitypulse.models.train_delay_model --allow-synthetic`. It does not constitute a live arrival estimate.

## Schema caveats

All primary read endpoints return `metadata` with `data_mode` and `observations_are_real`. The latter is always false for the default demo and cannot be independently certified for an externally supplied CSV. An imported GTFS schedule without historical observation CSV has `on_time_pct=null`.
