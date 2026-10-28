"""Save the deterministic synthetic fixture to disk for teaching and export."""
from pathlib import Path
import json,csv
from backend.app.db.store import make_demo
d=make_demo()
root=Path(__file__).resolve().parents[1]/"data"/"synthetic"
root.mkdir(parents=True,exist_ok=True)
(root/"demo_transit.json").write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding="utf-8")
with (root/"historical_observations.csv").open("w",newline="",encoding="utf-8") as fp:
    wr=csv.DictWriter(fp,fieldnames=list(d["observations"][0]))
    wr.writeheader();wr.writerows(d["observations"])
print("Generated",len(d["observations"]),"synthetic stop observations.")
