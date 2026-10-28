"""Common structural and reference checks for permitted GTFS Schedule ZIPs."""
REQUIRED={"agency.txt":["agency_name","agency_url","agency_timezone"],
"routes.txt":["route_id","route_type"],"stops.txt":["stop_id","stop_name","stop_lat","stop_lon"],
"trips.txt":["route_id","service_id","trip_id"],
"stop_times.txt":["trip_id","arrival_time","departure_time","stop_id","stop_sequence"]}
def validate(frames):
    errors=[]
    for name,columns in REQUIRED.items():
        if name not in frames:
            errors.append(f"missing {name}");continue
        df=frames[name]
        for c in columns:
            if c not in df.columns:errors.append(f"{name}: missing {c}")
        if df.empty:errors.append(f"{name}: empty")
    if errors:return errors
    stops=frames["stops.txt"]
    for col,low,high in [("stop_lat",-90,90),("stop_lon",-180,180)]:
        vals=__import__("pandas").to_numeric(stops[col],errors="coerce")
        if vals.isna().any() or not vals.between(low,high).all():errors.append(f"stops.txt: invalid {col}")
    for src,key,ref,target in [("trips.txt","route_id","routes.txt","route_id"),
                               ("stop_times.txt","trip_id","trips.txt","trip_id"),
                               ("stop_times.txt","stop_id","stops.txt","stop_id")]:
        if not set(frames[src][key].dropna()).issubset(set(frames[ref][target].dropna())):errors.append(f"{src}: dangling {key}")
    return errors
