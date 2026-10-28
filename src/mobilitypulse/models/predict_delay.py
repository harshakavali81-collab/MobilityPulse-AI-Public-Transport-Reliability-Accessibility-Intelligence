from pathlib import Path
import joblib
ROOT=Path(__file__).resolve().parents[3]
def predict(features):
    path=ROOT/"data"/"processed"/"delay_model.joblib"
    if not path.exists():return None
    model=joblib.load(path)
    return max(-3,round(float(model.predict([[features["hour"],features["day_of_week"],features["preceding_delay_minutes"],features["stop_sequence"]]])[0]),2))
