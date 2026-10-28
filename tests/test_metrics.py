from mobilitypulse.analytics.on_time_performance import summary
from mobilitypulse.analytics.headway import by_route
from backend.app.db.store import make_demo
def test_empty_observations_unknown():
    r=summary([])
    assert r["on_time_pct"] is None
    assert r["mean_delay_minutes"] is None
def test_scheduled_only_not_observed():
    rows=[{"status":"scheduled","scheduled_arrival":"2026-01-01T09:00:00Z","actual_arrival":None}]
    assert summary(rows)["observed_stop_events"]==0
    assert summary(rows)["on_time_pct"] is None
def test_on_time_window_and_cancellations():
    rows=[{"status":"observed","actual_arrival":"2026-01-01T09:02:00Z","scheduled_arrival":"2026-01-01T09:00:00Z"},
          {"status":"observed","actual_arrival":"2026-01-01T09:07:00Z","scheduled_arrival":"2026-01-01T09:00:00Z"},
          {"status":"cancelled","actual_arrival":None,"scheduled_arrival":"2026-01-01T09:00:00Z"}]
    result=summary(rows)
    assert result["on_time_pct"]==50
    assert result["cancelled_stop_events"]==1
def test_headways_same_stop_not_cross_stop():
    rows=[
      {"status":"observed","service_date":"2026-01-01","route_id":"R1","stop_id":"S1","actual_arrival":"2026-01-01T08:00:00Z"},
      {"status":"observed","service_date":"2026-01-01","route_id":"R1","stop_id":"S1","actual_arrival":"2026-01-01T08:20:00Z"},
      {"status":"observed","service_date":"2026-01-01","route_id":"R1","stop_id":"S2","actual_arrival":"2026-01-01T08:05:00Z"}]
    result=by_route(rows)
    assert result[0]["median_headway_minutes"]==20
def test_deterministic_demo():
    a,b=make_demo(),make_demo()
    assert a["observations"]==b["observations"]
    assert len(a["routes"])==4 and len(a["stops"])==12
