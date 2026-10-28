def validate_snapshot(snapshot):
    problems=[]
    if snapshot.get("age_seconds") is None:problems.append("missing timestamp")
    elif snapshot["age_seconds"]>90:problems.append("stale feed")
    if snapshot.get("age_seconds") is not None and snapshot["age_seconds"]<0:problems.append("future timestamp")
    if not any(snapshot.get(k,0) for k in ("trip_updates","vehicle_positions","alerts")):
        problems.append("no entities")
    return problems
