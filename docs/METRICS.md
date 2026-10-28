# Analytics definitions

## Arrival delay

`observed_delay_minutes = actual_arrival - scheduled_arrival` for a matching observed stop event. Negative values are early. There is no actual delay when actual arrival is missing.

## On-time performance

A stop event is considered on time if its observed arrival delay is in the inclusive range **[-1, +5] minutes**.

`on_time_pct = 100 * count(-1 <= observed_delay_minutes <= 5) / count(valid observed stop events)`.

When no observed arrivals exist, return `null`; zero is an incorrect value for "unknown." The definition is a portfolio-specific window, not a universal agency SLA.

## Cancellation

`cancelled_stop_events` counts stop-time rows with `status=cancelled`. A trip with six stops can contribute six cancelled stop events. It is **not** a distinct trip cancellation count.

## Headway

Within each `(service_date, route_id, stop_id)` group, sort observed actual arrivals and take successive positive gaps under 300 minutes. Report the median per route, preserving route-stop-date boundaries. No schedule-only headway is mislabeled as an observed result.

## Percentiles

P90 is the nearest-rank-like sample index used by the implementation. For production, document interpolation policy and temporal granularity, excluded outliers, source completeness, and confidence intervals.
