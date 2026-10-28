"""Opt-in, allowlisted GTFS-RT download and bounded, provenance-aware diagnostics.

The network request is only performed by the explicitly run refresh script.
It does not supply passenger ETAs, vehicle-location history or verified
arrival observations to the application's analytics.
"""
import ipaddress
import os
import urllib.request
from urllib.parse import urlsplit
from mobilitypulse.ingestion.gtfs_realtime_loader import parse_feed
from mobilitypulse.ingestion.realtime_predictions import parse_trip_predictions

MAX_BYTES=10_000_000

def validate_feed_url(url,allow_hosts):
    parts=urlsplit(url)
    if parts.scheme!="https" or not parts.hostname or parts.username or parts.password or parts.fragment:
        raise ValueError("GTFS-RT URL must be a valid HTTPS URL without credentials or fragments")
    if parts.port not in (None,443):
        raise ValueError("Nonstandard HTTPS port is not allowed")
    host=parts.hostname.lower().rstrip(".")
    allowed={x.strip().lower().rstrip(".") for x in allow_hosts.split(",") if x.strip()}
    if host not in allowed:
        raise ValueError("Feed hostname not in explicit GTFS_RT_ALLOWED_HOSTS allowlist")
    try:
        ipaddress.ip_address(host)
    except ValueError:
        if host=="localhost" or host.endswith((".local",".internal",".localhost")):
            raise ValueError("Private or local feed hosts are disallowed")
    else:raise ValueError("IP-literal targets are disallowed")
    return url

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):
        raise ValueError("Feed redirects disabled; use the approved final HTTPS URL")

def download_diagnostics(url=None,allow_hosts=None):
    url=url or os.environ["GTFS_RT_URL"]
    allow_hosts=allow_hosts if allow_hosts is not None else os.getenv("GTFS_RT_ALLOWED_HOSTS","")
    validate_feed_url(url,allow_hosts)
    request=urllib.request.Request(url,headers={"Accept":"application/x-protobuf,application/octet-stream",
                                               "User-Agent":"MobilityPulseAI/1.2"})
    opener=urllib.request.build_opener(NoRedirect)
    with opener.open(request,timeout=10) as response:
        body=response.read(MAX_BYTES+1)
    if len(body)>MAX_BYTES:
        raise ValueError("GTFS-RT response exceeds 10 MB limit")
    snapshot=parse_feed(body)
    snapshot["publisher_predictions"]=parse_trip_predictions(body)
    snapshot["publisher_predictions_are_observed_arrivals"]=False
    snapshot["source"]="authorized operator GTFS-Realtime"
    snapshot["verified_service_quality"]=False
    snapshot["used_for_arrival_predictions"]=False
    return snapshot
