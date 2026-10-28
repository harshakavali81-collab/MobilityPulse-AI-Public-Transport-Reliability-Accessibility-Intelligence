"""Optional offline protobuf GTFS-RT feed reader. No live feed is configured by default."""
from datetime import datetime,timezone
def parse_feed(body:bytes):
    try:from google.transit import gtfs_realtime_pb2
    except ImportError as exc:raise RuntimeError("Install gtfs-realtime-bindings") from exc
    feed=gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(body)
    stamp=int(feed.header.timestamp) if feed.header.HasField("timestamp") else None
    counts={"trip_updates":0,"vehicle_positions":0,"alerts":0}
    for e in feed.entity:
        if e.HasField("trip_update"):counts["trip_updates"]+=1
        if e.HasField("vehicle"):counts["vehicle_positions"]+=1
        if e.HasField("alert"):counts["alerts"]+=1
    now=datetime.now(timezone.utc).timestamp()
    age=round(now-stamp,1) if stamp is not None else None
    return {"feed_timestamp":stamp,"age_seconds":age,"fresh":age is not None and 0<=age<=90,**counts}
