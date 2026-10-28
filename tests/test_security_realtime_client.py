import pytest
from mobilitypulse.ingestion.gtfs_realtime_client import validate_feed_url
def test_allowlisted_https_feed():
    assert validate_feed_url("https://agency.example.org/gtfsrt","agency.example.org").startswith("https://")
@pytest.mark.parametrize("url",[
  "http://agency.example.org/rt",
  "https://127.0.0.1/rt",
  "https://localhost/rt",
  "https://agency.example.org:444/rt",
  "https://user:password@agency.example.org/rt",
  "https://internal.example.org/rt"
])
def test_disallowed_feeds(url):
    with pytest.raises(ValueError):validate_feed_url(url,"agency.example.org")
def test_api_key_when_configured(client,monkeypatch):
    monkeypatch.setenv("MOBILITYPULSE_API_KEY","token-test-secret")
    assert client.get("/api/overview").status_code==401
    assert client.get("/api/overview",headers={"X-API-Key":"token-test-secret"}).status_code==200
    assert client.get("/api/health").status_code==200
def test_security_headers(client):
    r=client.get("/api/health")
    assert r.headers.get("x-content-type-options")=="nosniff"
    assert r.headers.get("x-frame-options")=="DENY"
def test_oversize_payload(client,monkeypatch):
    monkeypatch.setenv("MOBILITYPULSE_MAX_POST_BYTES","15")
    r=client.post("/api/delays/predict",content=b"x"*200,
                  headers={"content-type":"application/json"})
    assert r.status_code==413
def test_missing_rt_state_is_explicit(client,monkeypatch,tmp_path):
    monkeypatch.setenv("GTFS_RT_STATE_PATH",str(tmp_path/"not-present.json"))
    r=client.get("/api/feed/status").json()
    assert r["live_tracking"] is False
    assert r["gtfs_realtime_available"] is False
