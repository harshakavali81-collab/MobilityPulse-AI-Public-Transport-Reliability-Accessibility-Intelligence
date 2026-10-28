"""Small evaluation helper; do not interpret demo metrics as live ETA validation."""
import numpy as np
from sklearn.metrics import mean_absolute_error,mean_squared_error
def evaluate_predictions(actual,predicted):
    y=np.asarray(actual,dtype=float)
    p=np.asarray(predicted,dtype=float)
    if not len(y) or len(y)!=len(p):raise ValueError("Require equal nonempty target/prediction arrays")
    if not np.isfinite(y).all() or not np.isfinite(p).all():raise ValueError("Non-finite prediction data")
    return {"mae":round(float(mean_absolute_error(y,p)),3),
            "rmse":round(float(np.sqrt(mean_squared_error(y,p))),3),
            "sample_size":len(y),"operationally_validated":False}
