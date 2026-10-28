from fastapi import APIRouter,HTTPException
from backend.app.db.store import catalog
router=APIRouter()
@router.get("/routes")
def routes():
    c=catalog()
    return {"items":c["routes"],"metadata":c["metadata"]}
@router.get("/routes/{route_id}")
def route_detail(route_id:str):
    c=catalog()
    route=next((r for r in c["routes"] if r["route_id"]==route_id),None)
    if route is None: raise HTTPException(404,"Route not found")
    stopmap={s["stop_id"]:s for s in c["stops"]}
    return {"route":route,"stops":[stopmap[s] for s in route.get("stop_ids",[]) if s in stopmap],"metadata":c["metadata"]}
