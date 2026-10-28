import pandas as pd
import pytest
from mobilitypulse.processing.clean import clean_observations
from mobilitypulse.processing.features import build_temporal_features
from mobilitypulse.models.evaluate import evaluate_predictions

def row(actual):
    return pd.DataFrame([{"route_id":"R1","stop_id":"S1","trip_id":"T1","service_date":"2026-10-01",
       "scheduled_arrival":"2026-10-01T10:00:00Z","actual_arrival":actual,"status":"observed","stop_sequence":1}])
def test_missing_actual_stays_missing():
    out=clean_observations(row(None))
    assert pd.isna(out.iloc[0]["actual_arrival"])
    assert pd.isna(out.iloc[0]["observed_delay_minutes"])
def test_delay_sign():
    out=clean_observations(row("2026-10-01T10:03:00Z"))
    assert out.iloc[0]["observed_delay_minutes"]==3
def test_temporal_features():
    f=build_temporal_features(row(None))
    assert f.iloc[0]["hour"]==10
    assert f.iloc[0]["stop_sequence"]==1
def test_model_eval():
    assert evaluate_predictions([1,2],[2,2])["mae"]==0.5
def test_eval_rejects_empty():
    with pytest.raises(ValueError):evaluate_predictions([],[])
