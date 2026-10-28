"""Export explicitly synthetic GET snapshots for the GitHub Pages *offline* demo.

The output contains no secrets, real observations or externally fetched data.
This does not launch or deploy FastAPI to a public host.
"""
import argparse,json,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
os.environ.pop("GTFS_ZIP_PATH",None)
os.environ.pop("OBSERVATIONS_CSV_PATH",None)
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.db.store import catalog
EXPORTS={
    "overview":"/api/overview",
    "routes":"/api/routes",
    "stops":"/api/stops",
    "analytics/reliability":"/api/analytics/reliability",
    "analytics/headways":"/api/analytics/headways",
    "analytics/trends":"/api/analytics/trends",
    "accessibility":"/api/accessibility",
    "feed/status":"/api/feed/status",
}
def build(out):
    catalog.cache_clear()
    out=Path(out)
    with TestClient(app) as client:
        for name,endpoint in EXPORTS.items():
            response=client.get(endpoint)
            response.raise_for_status()
            data=response.json()
            assert data.get("metadata",{}).get("data_mode")=="synthetic",endpoint
            assert data["metadata"]["live_tracking"] is False,endpoint
            target=out/(name+".json")
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(json.dumps(data,ensure_ascii=False,separators=(",",":")),encoding="utf-8")
    print(f"Exported {len(EXPORTS)} clearly synthetic read-only endpoint snapshots into {out}.")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",default=str(ROOT/"frontend"/"public"/"sample-api"))
    args=p.parse_args()
    build(args.out)
