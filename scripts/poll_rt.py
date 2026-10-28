import argparse,json,urllib.request
from mobilitypulse.ingestion.gtfs_realtime_loader import parse_feed
parser=argparse.ArgumentParser()
parser.add_argument("--url",required=True,help="Permitted operator realtime protobuf URL")
parser.add_argument("--auth-header",default=None,help="Optional header NAME:VALUE, never print secrets")
args=parser.parse_args()
req=urllib.request.Request(args.url,headers={"User-Agent":"MobilityPulse-demo/1.1"})
if args.auth_header:
    name,value=args.auth_header.split(":",1);req.add_header(name.strip(),value.strip())
with urllib.request.urlopen(req,timeout=10) as response:body=response.read(10_000_001)
if len(body)>10_000_000:raise ValueError("Feed exceeds 10MB size limit")
print(json.dumps(parse_feed(body),indent=2))
