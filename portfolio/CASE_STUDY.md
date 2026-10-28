# MobilityPulse AI — End-to-End Portfolio Case Study

**Category:** Data Analytics · AI/ML · Python Engineering · React Full Stack · Open Data · Public Impact

**Project objective:** Explore public transit route and stop data, observed historical reliability, delays, route frequency and accessibility metadata through a transparent interface.

## Business question

Published route schedules are not evidence of observed punctuality. Operators and citizens need performance metrics tied to genuine arrival observations, along with visible uncertainty and source provenance. Accessibility fields also require care: unknown metadata cannot be interpreted as accessible.

## Solution architecture

Designed a source-aware GTFS ingestion layer, data checks and foreign-key validation, deterministic fictional demonstration fixtures, FastAPI analytics endpoints, React dashboard, SVG route explorer, accessibility register, separate GTFS-Realtime diagnostics, and a chronological delay ML baseline evaluation.

## Workflow

1. Select an authorized dataset (or default synthetic demo).
2. Validate GTFS tables and keys.
3. Distinguish planned service, externally supplied observations and synthetic records.
4. Calculate observed stop-event OTP, headway, mean and P90 delay.
5. Offer JSON APIs, CSV exports and React charts.
6. Optionally train/evaluate a model on held-out dates.
7. Run pytest and React builds through GitHub Actions.

## Portfolio visuals

![Original project banner](../assets/01-hero.svg)
![ETL pipeline](../assets/03-ingestion-pipeline.svg)
![Route map](../assets/05-route-network-map.svg)
![Reliability illustration](../assets/06-route-reliability-bars.svg)

All artwork is original; all default data and illustrative values are synthetic. No agency affiliation or public deployment is claimed.

## Technologies

Python · Pandas · FastAPI · GTFS · GTFS-RT parser · scikit-learn · React · Recharts · Docker Compose · pytest · GitHub Actions · CSV/Power BI.

## Evaluation philosophy

Use a chronological holdout rather than randomly shuffling time-series observations, compare against a simple baseline, and keep synthetic experiment results separate from operational performance claims. The UI never fabricates actual arrivals from scheduled times.

## Recruiter-ready summary

**MobilityPulse AI:** Developed a portfolio transit-intelligence platform integrating GTFS schedule ingestion and validation, Python/FastAPI services, React reliability and accessibility dashboards, historical stop-event metrics, offline RandomForest evaluation, Docker setup, and automated test workflows using clearly labeled synthetic data.

## Outstanding for real deployment

Agency feed permission; validated observed arrival feed; production auth and persistence; monitoring, rate limiting, secure hosting; legally reviewed privacy controls; and independent forecasting validation.
