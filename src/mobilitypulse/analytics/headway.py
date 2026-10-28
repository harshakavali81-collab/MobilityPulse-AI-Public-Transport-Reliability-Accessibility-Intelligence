"""Observed stop headways: do not subtract arrivals at different stops."""
from collections import defaultdict
from datetime import datetime
from statistics import median

def by_route(rows):
    groups=defaultdict(list)
    for r in rows:
        if r.get("status")=="observed" and r.get("actual_arrival"):
            groups[(r["route_id"],r["stop_id"],r["service_date"])].append(datetime.fromisoformat(r["actual_arrival"].replace("Z","+00:00")))
    gaps=defaultdict(list)
    for (route,stop,date),times in groups.items():
        times=sorted(times)
        gaps[route].extend((b-a).total_seconds()/60 for a,b in zip(times,times[1:]) if 0<(b-a).total_seconds()/60<300)
    return [{"route_id":route,"median_headway_minutes":round(median(values),1) if values else None,
             "observed_intervals":len(values)} for route,values in sorted(gaps.items())]
