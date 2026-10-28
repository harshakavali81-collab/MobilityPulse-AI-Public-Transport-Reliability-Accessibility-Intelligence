import sys
from mobilitypulse.ingestion.gtfs_static_loader import load_gtfs_zip
if len(sys.argv)!=2:raise SystemExit("Usage: python scripts/validate_gtfs.py path/to/feed.zip")
frames=load_gtfs_zip(sys.argv[1])
print("GTFS validation succeeded:",", ".join(sorted(frames)))
