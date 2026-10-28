from fastapi import APIRouter
from backend.app.db.store import catalog
router=APIRouter()
@router.get("/accessibility")
def accessibility():
    c=catalog()
    items=[]
    for stop in c["stops"]:
        val=int(stop.get("wheelchair_boarding") or 0)
        items.append({**stop,"wheelchair_status":{0:"unknown",1:"publisher_reported_accessible",2:"publisher_reported_inaccessible"}.get(val,"unknown")})
    return {"items":items,"metadata":c["metadata"],
            "disclaimer":"Static publisher metadata is not independently verified and does not guarantee step-free boarding."}
