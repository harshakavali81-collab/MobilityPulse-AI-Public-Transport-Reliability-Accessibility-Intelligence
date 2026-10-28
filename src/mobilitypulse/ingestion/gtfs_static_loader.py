from pathlib import Path
from zipfile import ZipFile
import pandas as pd
from mobilitypulse.processing.validate_gtfs import REQUIRED, validate
def load_gtfs_zip(path):
    path=Path(path)
    if not path.is_file():raise FileNotFoundError(path)
    with ZipFile(path) as z:
        names={n.split("/")[-1]:n for n in z.namelist()}
        frames={}
        for name in set(REQUIRED)|{"calendar.txt","calendar_dates.txt"}:
            if name in names:
                with z.open(names[name]) as fp:frames[name]=pd.read_csv(fp,dtype=str)
    errors=validate(frames)
    if errors:raise ValueError("; ".join(errors))
    return frames
def to_catalog(frames):
    routes=frames["routes.txt"].fillna("").to_dict("records")
    stops=frames["stops.txt"].fillna("").to_dict("records")
    trips=frames["trips.txt"][["route_id","trip_id"]].drop_duplicates()
    stop_times=frames["stop_times.txt"][["trip_id","stop_id","stop_sequence"]].merge(trips,on="trip_id")
    for r in routes:
        rows=stop_times[stop_times["route_id"]==r["route_id"]]
        r["stop_ids"]=rows.sort_values("stop_sequence")["stop_id"].drop_duplicates().tolist()
    return {"metadata":{"dataset":"Supplied GTFS Schedule","data_mode":"schedule_only",
       "source":"externally supplied static feed; not independently verified",
       "observations_are_real":False,"live_tracking":False},
       "routes":routes,"stops":stops,"observations":[],"alerts":[]}
