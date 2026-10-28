"""Produce synthetic reporting CSVs for Power BI / Excel exploration."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import pandas as pd
from backend.app.db.store import catalog
from mobilitypulse.analytics.route_reliability import by_route
from mobilitypulse.analytics.headway import by_route as headways
out=ROOT/"powerbi"/"exports"
out.mkdir(parents=True,exist_ok=True)
c=catalog()
for name,items in {"routes":c["routes"],"stops":c["stops"],
                    "route_reliability":by_route(c["observations"],c["routes"]),
                    "route_headways":headways(c["observations"]),
                    "observations":c["observations"]}.items():
    pd.DataFrame(items).to_csv(out/(name+".csv"),index=False)
print("CSV exports written to",out)
