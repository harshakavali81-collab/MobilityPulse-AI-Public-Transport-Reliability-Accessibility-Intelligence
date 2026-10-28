-- Illustrative PostgreSQL queries. Assumes tables normalized according to the optional schema.
-- Schedule-derived rows are not counted as observed punctuality.
-- 1: Route-wise observed event on-time performance
SELECT route_id,
  COUNT(*) FILTER (WHERE status='observed' AND actual_arrival IS NOT NULL) AS observed_stop_events,
  COUNT(*) FILTER (WHERE status='cancelled') AS cancelled_stop_events,
  ROUND(100.0 * COUNT(*) FILTER (
    WHERE status='observed' AND actual_arrival IS NOT NULL
    AND observed_delay_minutes BETWEEN -1 AND 5
  ) / NULLIF(COUNT(*) FILTER (
    WHERE status='observed' AND actual_arrival IS NOT NULL),0), 2) AS on_time_pct,
  ROUND(AVG(observed_delay_minutes) FILTER(
    WHERE status='observed' AND actual_arrival IS NOT NULL)::numeric,2) AS mean_delay_minutes
FROM stop_events
GROUP BY route_id
ORDER BY route_id;

-- 2: Stop accessibility status with unknown preserved
SELECT stop_id, stop_name,
  CASE wheelchair_boarding
    WHEN 1 THEN 'publisher_reported_accessible'
    WHEN 2 THEN 'publisher_reported_inaccessible'
    ELSE 'unknown' END AS reported_status
FROM transit_stops;

-- 3: Observed route headways, comparing actual arrivals at same stop and date
WITH t AS (
 SELECT route_id,stop_id,service_date,actual_arrival,
        LAG(actual_arrival) OVER (
          PARTITION BY route_id,stop_id,service_date ORDER BY actual_arrival
        ) AS prior_actual
 FROM stop_events
 WHERE status='observed' AND actual_arrival IS NOT NULL
), gaps AS (
 SELECT route_id, EXTRACT(EPOCH FROM (actual_arrival::timestamptz-prior_actual::timestamptz))/60 AS headway_m
 FROM t WHERE prior_actual IS NOT NULL
)
SELECT route_id,ROUND((PERCENTILE_CONT(.5) WITHIN GROUP(ORDER BY headway_m))::numeric,1) AS median_observed_headway
FROM gaps WHERE headway_m>0 AND headway_m<300 GROUP BY route_id ORDER BY route_id;
