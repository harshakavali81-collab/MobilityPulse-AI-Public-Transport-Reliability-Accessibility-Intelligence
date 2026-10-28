from collections import defaultdict
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
    return {"mode":c["metadata"]["data_mode"],"live_tracking":False,
       "gtfs_realtime_available":False,"last_realtime_update":None,
       "message":"No verified live GTFS-Realtime connection is configured.","metadata":c["metadata"]}
