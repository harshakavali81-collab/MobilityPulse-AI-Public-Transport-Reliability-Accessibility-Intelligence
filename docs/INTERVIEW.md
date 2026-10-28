# Recruiter and interview walkthrough

**Problem:** Public transit passengers and operators need trustworthy visibility into service reliability and accessibility. GTFS schedules alone do not tell whether service was punctual.

**Solution:** Created source-aware ingestion and validation, calculated metrics only from actual event fields, built API endpoints, implemented interactive React visualizations, added a separate offline ML evaluation, and created testable deployment workflows.

**Data:** Default demonstration consists of 4 fictional routes, 12 fictional stops and 21 synthetic days. Dates, events and coordinates are not live operational data.

**Difficult engineering choices:** Reject invalid GTFS foreign keys; don't mistake scheduled times for actual arrivals; preserve unknown accessibility; calculate headways at the same stop/date; chronological rather than random model split; don't claim synthetic ML accuracy transfers to reality.

**Tradeoffs:** Cached per-process storage simplifies demos but lacks persistence and multiuser handling. A real deployment would use PostgreSQL/PostGIS, scheduled feed polling, auth, observability, consent/license reviews and appropriate transit domain validation.

**Tech stack:** Python, Pandas, FastAPI, React, Vite, Recharts, scikit-learn, pytest, Docker, GitHub Actions.

**Resume line:** Built MobilityPulse AI, a source-aware transit reliability analytics portfolio platform using GTFS ingestion, Python/FastAPI, React dashboards, accessibility metadata, chronological ML evaluation and automated tests on synthetic data.
