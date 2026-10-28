-- OPTIONAL NORMALIZED REFERENCE SCHEMA, not a database already provisioned.
-- Compatible with SQLite for educational exploration.
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS transit_routes (
    route_id TEXT PRIMARY KEY,
    route_short_name TEXT,
    route_long_name TEXT,
    route_type INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS transit_stops (
    stop_id TEXT PRIMARY KEY,
    stop_name TEXT NOT NULL,
    stop_lat REAL CHECK (stop_lat BETWEEN -90 AND 90),
    stop_lon REAL CHECK (stop_lon BETWEEN -180 AND 180),
    wheelchair_boarding INTEGER DEFAULT 0 CHECK (wheelchair_boarding IN (0,1,2))
);
CREATE TABLE IF NOT EXISTS transit_trips (
    trip_id TEXT PRIMARY KEY,
    route_id TEXT NOT NULL REFERENCES transit_routes(route_id),
    service_id TEXT
);
CREATE TABLE IF NOT EXISTS stop_events (
    event_id INTEGER PRIMARY KEY,
    service_date TEXT NOT NULL,
    trip_id TEXT NOT NULL REFERENCES transit_trips(trip_id),
    route_id TEXT NOT NULL REFERENCES transit_routes(route_id),
    stop_id TEXT NOT NULL REFERENCES transit_stops(stop_id),
    stop_sequence INTEGER NOT NULL CHECK (stop_sequence > 0),
    scheduled_arrival TEXT NOT NULL,
    actual_arrival TEXT,
    observed_delay_minutes REAL,
    status TEXT NOT NULL CHECK(status IN ('scheduled','observed','cancelled')),
    source TEXT NOT NULL,
    UNIQUE(service_date,trip_id,stop_id,stop_sequence)
);
CREATE INDEX IF NOT EXISTS idx_events_route_date ON stop_events(route_id,service_date);
CREATE INDEX IF NOT EXISTS idx_events_stop_date ON stop_events(stop_id,service_date);
