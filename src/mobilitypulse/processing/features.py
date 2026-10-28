"""Create only temporal and sequence features. No sensitive passenger features."""
import pandas as pd
FEATURES=["hour","day_of_week","stop_sequence"]
def build_temporal_features(frame:pd.DataFrame)->pd.DataFrame:
    result=frame.copy()
    stamp=pd.to_datetime(result["scheduled_arrival"],utc=True,errors="coerce")
    if stamp.isna().any():raise ValueError("Cannot extract features from invalid scheduled_arrival")
    result["hour"]=stamp.dt.hour
    result["day_of_week"]=stamp.dt.dayofweek
    if "stop_sequence" in result:
        result["stop_sequence"]=pd.to_numeric(result["stop_sequence"],errors="coerce")
    return result
