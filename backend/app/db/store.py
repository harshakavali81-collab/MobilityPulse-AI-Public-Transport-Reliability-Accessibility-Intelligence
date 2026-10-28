"""Validated catalogue store, backed by explicitly synthetic default records."""
import os
import random
from functools import lru_cache
from datetime import datetime, timedelta, timezone, date
from mobilitypulse.ingestion.gtfs_static_loader import load_gtfs_zip, to_catalog
from mobilitypulse.ingestion.ogd_loader import load_observations

STOPS = [
 ("S01","Central Square",17.424,78.467,1),("S02","River Walk",17.429,78.477,1),
 ("S03","North Gardens",17.438,78.488,0),("S04","University Gate",17.447,78.498,1),
 ("S05","West Market",17.433,78.447,2),("S06","Old Library",17.438,78.458,1),
 ("S07","Tech Park",17.453,78.480,1),("S08","Airport Link",17.462,78.494,0),
 ("S09","South Plaza",17.410,78.474,1),("S10","Lakeside",17.413,78.489,2),
 ("S11","Medical District",17.422,78.502,1),("S12","East Terminal",17.428,78.513,1)
]
ROUTES = [
 ("R1","M1","Central — University","#17bca9",["S01","S02","S03","S04","S07","S08"]),
 ("R2","B2","West Market — East Terminal","#718ff4",["S05","S06","S01","S09","S10","S11","S12"]),
 ("R3","C3","South Plaza — Tech Park","#f7a968",["S09","S01","S02","S07","S04"]),
 ("R4","E4","Lakeside — Airport Link","#bc9af5",["S10","S11","S03","S07","S08"])
]

def make_demo():
    rng=random.Random(42)
    stops=[dict(stop_id=k,stop_name=n,stop_lat=lat,stop_lon=lon,wheelchair_boarding=w) for k,n,lat,lon,w in STOPS]
    routes=[dict(route_id=i,route_short_name=sn,route_long_name=name,route_color=c,route_type=3,stop_ids=s) for i,sn,name,c,s in ROUTES]
    obs=[]
    for d in range(21):
        day=date(2026,10,1)+timedelta(days=d)
        for route in routes:
            for trip in range(7):
                hr=7+trip*2
                scheduled=datetime(day.year,day.month,day.day,hr,(trip*7+d*3)%60,tzinfo=timezone.utc)
                cancelled=rng.random() < (0.065 if route["route_id"]=="R4" else 0.045)
                base={"R1":2.2,"R2":4.3,"R3":6.1,"R4":3.7}[route["route_id"]]
                delay=max(-3,rng.gauss(base+(2 if trip in [0,1,5] else 0),3.5))
                previous_observed_delay=0.0
                for idx,sid in enumerate(route["stop_ids"]):
                    sched=scheduled+timedelta(minutes=idx*6)
                    observed_delay=round(max(-3,delay+idx*0.25+rng.gauss(0,0.6)),2)
                    actual=None if cancelled else (sched+timedelta(minutes=observed_delay)).isoformat()
                    obs.append(dict(service_date=str(day),trip_id=f'{route["route_id"]}-{d}-{trip}',route_id=route["route_id"],
                        stop_id=sid,stop_sequence=idx+1,scheduled_arrival=sched.isoformat(),
                        actual_arrival=actual,observed_delay_minutes=None if cancelled else observed_delay,
                        status="cancelled" if cancelled else "observed",source="synthetic",
                        preceding_delay_minutes=round(max(0,previous_observed_delay),2),
                        hour=hr,day_of_week=day.weekday()))
                    previous_observed_delay=observed_delay if not cancelled else 0.0
    return dict(metadata=dict(dataset="Fictional Sample City",data_mode="synthetic",observations_are_real=False,
        live_tracking=False,timezone="UTC",source="generated deterministic demo",updated_at="2026-10-21T23:59:00Z"),
        stops=stops,routes=routes,observations=obs,
        alerts=[dict(id="DEMO-01",severity="info",route_id="R3",
        title="Illustrative peak-hour scenario",description="Synthetic demonstration, not an actual advisory.",source="synthetic")])

@lru_cache(maxsize=1)
def catalog():
    gtfs=os.getenv("GTFS_ZIP_PATH","").strip()
    if not gtfs: return make_demo()
    c=to_catalog(load_gtfs_zip(gtfs))
    observed=os.getenv("OBSERVATIONS_CSV_PATH","").strip()
    if observed:
        c["observations"]=load_observations(observed)
        c["metadata"]["data_mode"]="externally_supplied_observations"
        c["metadata"]["observations_are_real"]=False
        c["metadata"]["source"]="externally supplied; provenance not independently verified"
    return c
