def test_health(client):
    r=client.get("/api/health");assert r.status_code==200
    assert r.json()["status"]=="ok"
def test_overview_source(client):
    o=client.get("/api/overview").json()
    assert o["routes"]==4 and o["stops"]==12
    assert o["metadata"]["data_mode"]=="synthetic"
    assert o["metadata"]["live_tracking"] is False
    assert o["reliability"]["observed_stop_events"]>0
def test_routes(client):
    r=client.get("/api/routes")
    assert r.status_code==200 and len(r.json()["items"])==4
    assert len(client.get("/api/routes/R1").json()["stops"])==6
    assert client.get("/api/routes/NOT_A_ROUTE").status_code==404
def test_stops(client):
    r=client.get("/api/stops")
    assert len(r.json()["items"])==12
    assert client.get("/api/stops/S01").status_code==200
    assert client.get("/api/stops/NOT_A_STOP").status_code==404
def test_reliability(client):
    r=client.get("/api/analytics/reliability")
    assert r.status_code==200
    assert len(r.json()["items"])==4
    assert all(0<=x["on_time_pct"]<=100 for x in r.json()["items"])
def test_trends_and_headways(client):
    assert len(client.get("/api/analytics/trends").json()["items"])==21
    assert client.get("/api/analytics/headways").status_code==200
def test_accessibility(client):
    rows=client.get("/api/accessibility").json()["items"]
    assert len(rows)==12
    assert any(x["wheelchair_status"]=="unknown" for x in rows)
def test_feed_not_live(client):
    r=client.get("/api/feed/status").json()
    assert r["live_tracking"] is False
    assert r["last_realtime_update"] is None
def test_prediction_unavailable_before_training(client,monkeypatch):
    from backend.app.routes import delays
    monkeypatch.setattr(delays,"predict",lambda f:None)
    r=client.post("/api/delays/predict",json={"hour":9,"day_of_week":1,"preceding_delay_minutes":4,"stop_sequence":2})
    assert r.status_code==503
def test_prediction_validation(client):
    r=client.post("/api/delays/predict",json={"hour":99,"day_of_week":1,"preceding_delay_minutes":1,"stop_sequence":2})
    assert r.status_code==422
