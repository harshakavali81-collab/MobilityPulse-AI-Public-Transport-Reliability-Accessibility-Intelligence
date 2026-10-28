from datetime import datetime, timezone
from google.transit import gtfs_realtime_pb2 as pb
from mobilitypulse.ingestion.realtime_predictions import parse_trip_predictions
def test_publisher_trip_updates_are_not_actual_arrivals():
    feed=pb.FeedMessage()
    feed.header.gtfs_realtime_version="2.0"
    feed.header.timestamp=int(datetime.now(timezone.utc).timestamp())
    e=feed.entity.add()
    e.id="id-1"
    e.trip_update.trip.trip_id="T42"
    e.trip_update.trip.route_id="B1"
    u=e.trip_update.stop_time_update.add()
    u.stop_id="STOP1"
    u.stop_sequence=2
    u.arrival.time=1790000000
    u.arrival.delay=120
    values=parse_trip_predictions(feed.SerializeToString())
    assert len(values)==1
    assert values[0]["trip_id"]=="T42"
    assert values[0]["publisher_estimated_delay_seconds"]==120
    assert values[0]["observed_actual_arrival"] is False
def test_missing_prediction_is_not_fabricated():
    feed=pb.FeedMessage()
    feed.header.gtfs_realtime_version="2.0"
    e=feed.entity.add()
    e.id="id-2"
    e.trip_update.trip.trip_id="T3"
    e.trip_update.stop_time_update.add().stop_id="S1"
    assert parse_trip_predictions(feed.SerializeToString())==[]
def test_empty_prediction_endpoint_in_demo(client,monkeypatch,tmp_path):
    monkeypatch.setenv("GTFS_RT_STATE_PATH",str(tmp_path/"missing.json"))
    response=client.get("/api/feed/predictions")
    assert response.status_code==200
    x=response.json()
    assert x["items"]==[]
    assert x["not_actual_arrivals"] is True
    assert x["feed_fresh"] is False
