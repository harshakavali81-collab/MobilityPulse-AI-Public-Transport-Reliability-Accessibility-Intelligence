"""Save the deterministic fictional fixture for notebooks, teaching and reports."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import json,csv
from backend.app.db.store import make_demo
d=make_demo()
out=ROOT/"data"/"synthetic"
out.mkdir(parents=True,exist_ok=True)
(out/"demo_transit.json").write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding="utf-8")
with (out/"historical_observations.csv").open("w",newline="",encoding="utf-8") as fp:
    wr=csv.DictWriter(fp,fieldnames=list(d["observations"][0]))
    wr.writeheader();wr.writerows(d["observations"])
print("Generated",len(d["observations"]),"synthetic stop observations.")
