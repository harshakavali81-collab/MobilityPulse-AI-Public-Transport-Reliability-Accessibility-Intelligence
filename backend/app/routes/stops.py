from fastapi import APIRouter,HTTPException
from backend.app.db.store import catalog
from mobilitypulse.analytics.on_time_performance import summary
router=APIRouter()
@router.get("/stops")
def stops():
    c=catalog()
    return {"items":c["stops"],"metadata":c["metadata"]}
@router.get("/stops/{stop_id}")
def stop_details(stop_id:str):
    c=catalog()
    stop=next((s for s in c["stops"] if s["stop_id"]==stop_id),None)
    if not stop:raise HTTPException(404,"Stop not found")
    return {"stop":stop,"reliability":summary([o for o in c["observations"] if o["stop_id"]==stop_id]),
            "metadata":c["metadata"]}
