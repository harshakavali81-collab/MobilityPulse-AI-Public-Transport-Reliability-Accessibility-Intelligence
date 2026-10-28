from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from backend.app.db.store import catalog
from mobilitypulse.models.predict_delay import predict
router=APIRouter()
class Features(BaseModel):
    hour:int=Field(ge=0,le=23)
    day_of_week:int=Field(ge=0,le=6)
    preceding_delay_minutes:float=Field(ge=0,le=300)
    stop_sequence:int=Field(ge=1,le=200)
@router.post("/delays/predict")
def delay(features:Features):
    result=predict(features.model_dump())
    if result is None:raise HTTPException(503,"No local trained model. Run python -m mobilitypulse.models.train_delay_model --allow-synthetic.")
    c=catalog()
    return {"estimated_delay_minutes":result,"data_mode":c["metadata"]["data_mode"],
       "experimental":True,"operationally_validated":False,
       "disclaimer":"Offline synthetic demonstration, not a live ETA."}
