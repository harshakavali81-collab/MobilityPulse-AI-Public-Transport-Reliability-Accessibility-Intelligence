"""Conservative input cleaning; preserve missing actual observations."""
import pandas as pd
def clean_observations(df:pd.DataFrame)->pd.DataFrame:
    required={"route_id","stop_id","trip_id","service_date","scheduled_arrival","actual_arrival","status"}
    missing=required-set(df.columns)
    if missing:raise ValueError(f"Missing observations columns: {sorted(missing)}")
    result=df.copy()
    for name in ["route_id","stop_id","trip_id","status"]:
        result[name]=result[name].astype("string").str.strip()
    if result[list(required-{"actual_arrival"})].isna().any().any():
        raise ValueError("Required observation identifiers are missing")
    # Do not invent actual_arrival or fill absent delay with zero.
    result["scheduled_arrival"]=pd.to_datetime(result["scheduled_arrival"],utc=True,errors="coerce")
    result["actual_arrival"]=pd.to_datetime(result["actual_arrival"],utc=True,errors="coerce")
    if result["scheduled_arrival"].isna().any():raise ValueError("Scheduled arrival timestamp invalid")
    result["observed_delay_minutes"]=(result["actual_arrival"]-result["scheduled_arrival"]).dt.total_seconds()/60
    return result
