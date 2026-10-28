"""Arrival metrics strictly require actual arrival observations."""
from datetime import datetime

def valid_events(rows):
    return [r for r in rows if r.get("status")=="observed" and r.get("actual_arrival") and r.get("scheduled_arrival")]

def minutes_late(row):
    if row.get("observed_delay_minutes") is not None:
        return float(row["observed_delay_minutes"])
    scheduled=datetime.fromisoformat(row["scheduled_arrival"].replace("Z","+00:00"))
    actual=datetime.fromisoformat(row["actual_arrival"].replace("Z","+00:00"))
    return (actual-scheduled).total_seconds()/60

def summary(rows):
    observations=valid_events(rows)
    delays=[minutes_late(row) for row in observations]
    cancellations=sum(r.get("status")=="cancelled" for r in rows)
    return {
        "scheduled_stop_events":len(rows),
        "observed_stop_events":len(delays),
        "cancelled_stop_events":cancellations,
        "on_time_pct":round(100*sum(-1<=d<=5 for d in delays)/len(delays),1) if delays else None,
        "mean_delay_minutes":round(sum(delays)/len(delays),2) if delays else None,
        "p90_delay_minutes":round(sorted(delays)[min(len(delays)-1,int(.9*len(delays)))],2) if delays else None
    }
