"""OPT-IN Hyderabad TGSRTC static GTFS import (schedules, NOT live arrivals).

Download requires explicit operator terms review. We do not redistribute
operator data, commit it, or claim independent validation of its accuracy.

Reference: https://tgsrtc.telangana.gov.in/open-data
"""
from __future__ import annotations
import argparse
import urllib.request
from pathlib import Path
from zipfile import ZipFile

PUBLIC_STATIC_FEED="https://data.opencity.in/dataset/88e2d145-7ec6-4666-88dd-6cf18b18312e/resource/1b0d18bb-b2fb-4a79-8ed0-1e071da5790c/download/telangana_opendata_gtfs_tgsrtc_08_february_2026.zip"
MAX_BYTES=40_000_000
def download(output: Path):
    from mobilitypulse.ingestion.gtfs_static_loader import load_gtfs_zip
    request=urllib.request.Request(PUBLIC_STATIC_FEED,headers={"User-Agent":"MobilityPulseAI/1.3 schedule-data-research"})
    with urllib.request.urlopen(request,timeout=35) as response:
        body=response.read(MAX_BYTES+1)
    if len(body)>MAX_BYTES:
        raise ValueError("ZIP larger than configured safe download limit")
    output.parent.mkdir(parents=True,exist_ok=True)
    temp=output.with_suffix(".tmp")
    try:
        temp.write_bytes(body)
        with ZipFile(temp) as z:
            if len(z.namelist())>200 or sum(x.file_size for x in z.infolist())>200_000_000:
                raise ValueError("Archive exceeds expanded size or entry count limits")
            if not all(x.filename.endswith(".txt") for x in z.infolist() if not x.is_dir()):
                raise ValueError("Unexpected GTFS archive entry")
        tables=load_gtfs_zip(temp)
        temp.replace(output)
        return {name:len(df) for name,df in tables.items()}
    finally:
        temp.unlink(missing_ok=True)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--accept-provider-terms",action="store_true",help="Confirm you reviewed official TGSRTC open-data terms.")
    p.add_argument("--output",type=Path,default=Path("data/raw/hyderabad_tgsrtc_gtfs.zip"))
    a=p.parse_args()
    if not a.accept_provider_terms:
        p.error("Review https://tgsrtc.telangana.gov.in/open-data first; then use --accept-provider-terms.")
    print("Schedule-only GTFS download:",download(a.output))
    print("No live arrivals are available from this schedule ZIP.")
if __name__=="__main__":main()
