"""Produce reproducible CSV exports for Power BI and Excel."""
from pathlib import Path
import pandas as pd
from backend.app.db.store import catalog
from mobilitypulse.analytics.route_reliability import by_route
from mobilitypulse.analytics.headway import by_route as headways
out=Path(__file__).resolve().parents[1]/"powerbi"/"exports"
out.mkdir(parents=True,exist_ok=True)
c=catalog()
for name,items in {"routes":c["routes"],"stops":c["stops"],"route_reliability":by_route(c["observations"],c["routes"]),
                    "route_headways":headways(c["observations"]),"observations":c["observations"]}.items():
    pd.DataFrame(items).to_csv(out/(name+".csv"),index=False)
print("CSV exports written to",out)
