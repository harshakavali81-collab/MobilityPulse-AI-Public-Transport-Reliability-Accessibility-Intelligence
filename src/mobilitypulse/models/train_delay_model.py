"""Offline demonstration model; uses chronological holdout and median baseline."""
import argparse,json
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,root_mean_squared_error
from backend.app.db.store import catalog
ROOT=Path(__file__).resolve().parents[3]
FEATURES=["hour","day_of_week","preceding_delay_minutes","stop_sequence"]
def train(allow_synthetic=False):
    c=catalog()
    if c["metadata"]["data_mode"]=="synthetic" and not allow_synthetic:
        raise ValueError("Synthetic model evaluation requires --allow-synthetic")
    df=pd.DataFrame(c["observations"])
    df=df[(df["status"]=="observed") & df["observed_delay_minutes"].notna()].copy()
    df=df.dropna(subset=FEATURES).sort_values(["service_date","trip_id","stop_sequence"])
    dates=sorted(df["service_date"].unique())
    if len(dates)<5:raise ValueError("At least five observed service dates required")
    split=dates[max(1,int(len(dates)*0.8))]
    train_df=df[df["service_date"]<split]
    test_df=df[df["service_date"]>=split]
    model=RandomForestRegressor(n_estimators=80,min_samples_leaf=4,random_state=42,n_jobs=1)
    model.fit(train_df[FEATURES],train_df["observed_delay_minutes"])
    actual=test_df["observed_delay_minutes"].to_numpy()
    predicted=model.predict(test_df[FEATURES])
    baseline=np.full(len(test_df),float(train_df["observed_delay_minutes"].median()))
    metrics={"mode":c["metadata"]["data_mode"],"test_start":str(split),
             "train_rows":len(train_df),"test_rows":len(test_df),
             "model_mae":round(float(mean_absolute_error(actual,predicted)),3),
             "model_rmse":round(float(root_mean_squared_error(actual,predicted)),3),
             "median_baseline_mae":round(float(mean_absolute_error(actual,baseline)),3),
             "operationally_validated":False}
    out=ROOT/"data"/"processed";out.mkdir(parents=True,exist_ok=True)
    joblib.dump(model,out/"delay_model.joblib")
    (out/"delay_model.metrics.json").write_text(json.dumps(metrics,indent=2))
    return metrics
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--allow-synthetic",action="store_true")
    args=parser.parse_args()
    print(json.dumps(train(args.allow_synthetic),indent=2))
