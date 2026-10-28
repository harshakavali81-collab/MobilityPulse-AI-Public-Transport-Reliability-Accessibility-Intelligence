import pytest
from mobilitypulse.ingestion.gtfs_realtime_loader import parse_feed
def test_valid_empty_protobuf():
    pb=pytest.importorskip("google.transit.gtfs_realtime_pb2")
    msg=pb.FeedMessage()
    msg.header.gtfs_realtime_version="2.0"
    result=parse_feed(msg.SerializeToString())
    assert result["trip_updates"]==0
    assert result["feed_timestamp"] is None
def test_feed_timestamp_unknown():
    from mobilitypulse.monitoring.feed_freshness import freshness
    assert freshness(None)["status"]=="missing"
