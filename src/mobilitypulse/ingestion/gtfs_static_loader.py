"""GTFS Schedule ZIP loader and simplified representative-pattern route catalog.

The catalog keeps one representative trip per route for an explainable map.
It is not a full service-calendar-aware trip planner or a GTFS shape renderer.
"""
from pathlib import Path
from zipfile import ZipFile
import pandas as pd
from mobilitypulse.processing.validate_gtfs import REQUIRED, validate

def load_gtfs_zip(path):
    path=Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    with ZipFile(path) as z:
        names={n.split("/")[-1]:n for n in z.namelist()}
        frames={}
        for name in set(REQUIRED)|{"calendar.txt","calendar_dates.txt"}:
            if name in names:
                with z.open(names[name]) as fp:
                    frames[name]=pd.read_csv(fp,dtype=str)
    errors=validate(frames)
    if errors:
        raise ValueError("; ".join(errors))
    return frames

def to_catalog(frames):
    routes=frames["routes.txt"].fillna("").to_dict("records")
    stops=frames["stops.txt"].fillna("").to_dict("records")
    # A route can have thousands of trips and several different patterns.
    # Choose a deterministic representative trip to avoid merging every
    # stop-time into every route and sorting stop sequences lexicographically.
    representative=(
        frames["trips.txt"][["route_id","trip_id"]]
        .drop_duplicates()
        .sort_values(["route_id","trip_id"])
        .drop_duplicates("route_id")
    )
    times=frames["stop_times.txt"][["trip_id","stop_id","stop_sequence"]]
    selected=times.merge(representative,on="trip_id",how="inner")
    selected["numeric_sequence"]=pd.to_numeric(selected["stop_sequence"],errors="coerce")
    if selected["numeric_sequence"].isna().any():
        raise ValueError("stop_times.txt: invalid stop_sequence")
    selected=selected.sort_values(["route_id","numeric_sequence","stop_id"],kind="stable")
    patterns={
        route_id: group["stop_id"].drop_duplicates().tolist()
        for route_id,group in selected.groupby("route_id",sort=False)
    }
    for route in routes:
        route["stop_ids"]=patterns.get(route["route_id"],[])
    return {
        "metadata":{
            "dataset":"Supplied GTFS Schedule",
            "data_mode":"schedule_only",
            "source":"externally supplied static feed; not independently verified",
            "route_pattern":"one representative scheduled trip per route",
            "observations_are_real":False,
            "live_tracking":False
        },
        "routes":routes,
        "stops":stops,
        "observations":[],
        "alerts":[]
    }
