"""Decode publisher-supplied GTFS-RT *predictions*, never actual arrivals.

Predictions are unverified agency estimates; they must not enter historical
observed-arrival performance or model validation datasets.
"""
from datetime import datetime, timezone

def _iso(epoch):
    return datetime.fromtimestamp(int(epoch),tz=timezone.utc).isoformat() if epoch else None

def parse_trip_predictions(body: bytes, max_items: int=150) -> list[dict]:
    from google.transit import gtfs_realtime_pb2
    if not 0 <= max_items <= 1000:
        raise ValueError("max_items must be between 0 and 1000")
    if max_items==0:
        return []
    feed=gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(body)
    rows=[]
    for entity in feed.entity:
        if not entity.HasField("trip_update"):
            continue
        update=entity.trip_update
        trip=update.trip
        for stop in update.stop_time_update:
            arrival=stop.arrival if stop.HasField("arrival") else None
            departure=stop.departure if stop.HasField("departure") else None
            event=arrival if arrival is not None else departure
            if event is None:
                continue
            predicted=int(event.time) if event.HasField("time") else None
            delay=int(event.delay) if event.HasField("delay") else None
            if predicted is None and delay is None:
                continue
            rows.append({
                "trip_id": trip.trip_id or None,
                "route_id": trip.route_id or None,
                "stop_id": stop.stop_id or None,
                "stop_sequence": int(stop.stop_sequence) if stop.HasField("stop_sequence") else None,
                "predicted_event_time": _iso(predicted),
                "publisher_estimated_delay_seconds": delay,
                "event_type": "arrival" if arrival is not None else "departure",
                "provenance": "publisher_gtfs_realtime_prediction",
                "observed_actual_arrival": False,
            })
            if len(rows) >= max_items:
                return rows
    return rows
