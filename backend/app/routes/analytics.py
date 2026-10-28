from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path
import json,os
from fastapi import APIRouter
from backend.app.db.store import catalog
from mobilitypulse.analytics.on_time_performance import summary
from mobilitypulse.analytics.route_reliability import by_route
from mobilitypulse.analytics.headway import by_route as headways
router=APIRouter()
@router.get("/overview")
def overview():
    c=catalog()
    return {"routes":len(c["routes"]),"stops":len(c["stops"]),
            "reliability":summary(c["observations"]),"metadata":c["metadata"]}
@router.get("/analytics/reliability")
def reliability():
    c=catalog()
    return {"items":by_route(c["observations"],c["routes"]),"metadata":c["metadata"]}
@router.get("/analytics/headways")
def observed_headways():
    c=catalog()
    return {"items":headways(c["observations"]),"metadata":c["metadata"]}
@router.get("/analytics/trends")
def trends():
    c=catalog()
    by_date=defaultdict(list)
    for r in c["observations"]:by_date[r["service_date"]].append(r)
    return {"items":[{"date":key,**summary(rows)} for key,rows in sorted(by_date.items())],"metadata":c["metadata"]}
@router.get("/alerts")
def alerts():
    c=catalog()
    return {"items":c.get("alerts",[]),"metadata":c["metadata"]}
@router.get("/feed/status")
def feed_status():
    c=catalog()
    path=Path(os.getenv("GTFS_RT_STATE_PATH","data/interim/feed_state.json"))
    snapshot=None
    if path.is_file():
        try:
            snapshot=json.loads(path.read_text(encoding="utf-8"))
            if snapshot.get("source")!="authorized operator GTFS-Realtime":snapshot=None
        except (OSError,ValueError,TypeError):snapshot=None
    timestamp=snapshot.get("feed_timestamp") if snapshot else None
    age=(datetime.now(timezone.utc).timestamp()-timestamp) if isinstance(timestamp,(int,float)) else None
    fresh=age is not None and 0<=age<=90
    return {"mode":c["metadata"]["data_mode"],
            "live_tracking":False,
            "gtfs_realtime_available":bool(snapshot and fresh),
            "last_realtime_update":datetime.fromtimestamp(timestamp,timezone.utc).isoformat() if timestamp else None,
            "realtime_feed_fresh":fresh,
            "realtime_age_seconds":round(age,1) if age is not None else None,
            "diagnostics_only":True,
            "message":("Fresh authorized protobuf feed diagnostics detected; not connected to arrivals or vehicle tracking."
                       if fresh else "No verified fresh GTFS-Realtime connection is configured."),
            "metadata":c["metadata"]}

@router.get("/feed/predictions")
def feed_predictions():
    """Publisher trip-update estimates with staleness gate and explicit provenance."""
    c=catalog()
    path=Path(os.getenv("GTFS_RT_STATE_PATH","data/interim/feed_state.json"))
    try:
        snapshot=json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None
    except (OSError,ValueError,TypeError):
        snapshot=None
    verified_source=isinstance(snapshot,dict) and snapshot.get("source")=="authorized operator GTFS-Realtime"
    timestamp=snapshot.get("feed_timestamp") if verified_source else None
    age=(datetime.now(timezone.utc).timestamp()-timestamp) if isinstance(timestamp,(int,float)) else None
    fresh=age is not None and 0<=age<=90
    values=snapshot.get("publisher_predictions",[]) if fresh else []
    return {
        "items":values if isinstance(values,list) else [],
        "feed_fresh":fresh,
        "data_mode":"publisher_gtfs_realtime_predictions" if fresh else "unavailable",
        "not_actual_arrivals":True,
        "not_verified_operational_eta":True,
        "not_used_in_reliability_metrics":True,
        "message":"GTFS-RT estimates are not actual arrival observations." if fresh else "No fresh authorized prediction feed available.",
        "metadata":c["metadata"],
    }
