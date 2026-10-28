"""Observed events must be independently obtained and provenance-reviewed."""
import pandas as pd
REQUIRED={"service_date","trip_id","route_id","stop_id","scheduled_arrival","actual_arrival","status","source"}
def load_observations(path):
    df=pd.read_csv(path,dtype=str)
    missing=REQUIRED-set(df)
    if missing:raise ValueError(f"Missing observed columns: {sorted(missing)}")
    if df["source"].isna().any() or (df["source"].str.strip()=="").any():
        raise ValueError("All imported observations require a source")
    a=pd.to_datetime(df["actual_arrival"],utc=True,errors="coerce")
    b=pd.to_datetime(df["scheduled_arrival"],utc=True,errors="coerce")
    df["observed_delay_minutes"]=(a-b).dt.total_seconds()/60
    return df.where(df.notna(),None).to_dict("records")
