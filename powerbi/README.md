# Power BI / Excel reporting starter

Run from the repository root:

```bash
python scripts/export_powerbi.py
```

This creates `powerbi/exports/routes.csv`, `stops.csv`, `route_reliability.csv`, `route_headways.csv`, and `observations.csv`. The data is synthetic unless a properly configured external import is used.

Recommended report pages: Executive summary, route scorecards, weekday and hour delay patterns, headway distribution, and accessibility metadata coverage.

Example DAX (import the observations table and verify data types):

```dax
Observed Stop Events = CALCULATE(COUNTROWS(observations), observations[status] = "observed")
Cancelled Stop Events = CALCULATE(COUNTROWS(observations), observations[status] = "cancelled")
On Time Stop Events = CALCULATE(COUNTROWS(observations), observations[status] = "observed", observations[observed_delay_minutes] >= -1, observations[observed_delay_minutes] <= 5)
On Time % = DIVIDE([On Time Stop Events], [Observed Stop Events])
Average Observed Delay = CALCULATE(AVERAGE(observations[observed_delay_minutes]), observations[status] = "observed")
```

This repository provides CSV exports and measure examples, **not** a native `.pbix` file.
