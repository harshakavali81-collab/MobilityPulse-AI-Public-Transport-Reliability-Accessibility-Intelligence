"""Explicitly refresh the local GTFS-RT diagnostics snapshot, when authorized.

Requires GTFS_RT_URL and GTFS_RT_ALLOWED_HOSTS to be set. Network I/O is never
performed just because the React dashboard or API is opened.
"""
import json,os,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from mobilitypulse.ingestion.gtfs_realtime_client import download_diagnostics

def main():
    snapshot=download_diagnostics()
    snapshot["checked_at"]=datetime.now(timezone.utc).isoformat()
    target=Path(os.getenv("GTFS_RT_STATE_PATH",str(ROOT/"data/interim/feed_state.json")))
    target.parent.mkdir(parents=True,exist_ok=True)
    temp=target.with_suffix(".tmp")
    temp.write_text(json.dumps(snapshot,indent=2),encoding="utf-8")
    temp.replace(target)
    print(json.dumps({"source":snapshot["source"],"fresh":snapshot["fresh"],
                      "age_seconds":snapshot["age_seconds"],
                      "trip_updates":snapshot["trip_updates"],
                      "vehicle_positions":snapshot["vehicle_positions"],
                      "alerts":snapshot["alerts"],"state_path":str(target)},indent=2))
if __name__=="__main__":
    main()
