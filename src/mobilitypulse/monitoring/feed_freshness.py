from datetime import datetime,timezone
def freshness(timestamp,max_age_seconds=90):
    if timestamp is None:return {"status":"missing","age_seconds":None}
    age=(datetime.now(timezone.utc).timestamp()-float(timestamp))
    return {"status":"fresh" if 0<=age<=max_age_seconds else "stale","age_seconds":round(age,1)}
