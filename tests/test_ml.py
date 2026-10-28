import math
from backend.app.db.store import make_demo
def test_demo_features():
    d=make_demo()
    row=next(x for x in d["observations"] if x["status"]=="observed")
    assert "preceding_delay_minutes" in row and "hour" in row
def test_synthetic_training_opt_in():
    from mobilitypulse.models.train_delay_model import train
    try:
        train(allow_synthetic=False)
    except ValueError as e:
        assert "Synthetic" in str(e)
    else:
        raise AssertionError("Training must require explicit opt-in")
def test_model_train_and_evaluate():
    from mobilitypulse.models.train_delay_model import train
    metrics=train(allow_synthetic=True)
    assert metrics["train_rows"]>100
    assert metrics["test_rows"]>10
    assert math.isfinite(metrics["model_mae"])
    assert metrics["operationally_validated"] is False

def test_no_future_delay_leakage_in_lag_feature():
    from collections import defaultdict
    grouped=defaultdict(list)
    for record in make_demo()["observations"]:
        grouped[record["trip_id"]].append(record)
    for events in grouped.values():
        rows=sorted(events,key=lambda x:x["stop_sequence"])
        assert rows[0]["preceding_delay_minutes"]==0
        for prev,current in zip(rows,rows[1:]):
            expected=max(0,prev["observed_delay_minutes"] or 0)
            assert abs(current["preceding_delay_minutes"]-round(expected,2))<1e-6
