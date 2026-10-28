# Hyderabad TGSRTC: optional real GTFS Schedule source

**Official terms and open-data context:** https://tgsrtc.telangana.gov.in/open-data

**Discovered static GTFS resource:** https://data.opencity.in/dataset/88e2d145-7ec6-4666-88dd-6cf18b18312e/resource/1b0d18bb-b2fb-4a79-8ed0-1e071da5790c/download/telangana_opendata_gtfs_tgsrtc_08_february_2026.zip

**Third-party feed index and quality notices:** https://mobilitydatabase.org/feeds/gtfs/mdb-3361

This is a public GTFS *schedule* dataset for Hyderabad buses, not independently confirmed realtime positions or historical arrival observations. It may be revised or unavailable. GTFS access is governed by source terms; do not download it until you have reviewed the provider's use conditions. No agency logos, proprietary materials, feeds or API credentials are redistributed in this repository.

## Opt-in

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
python scripts/download_hyderabad_schedule.py --accept-provider-terms
```

Set `GTFS_ZIP_PATH=data/raw/hyderabad_tgsrtc_gtfs.zip` in the backend process environment, then start the API. The existing loader validates GTFS structural requirements and reference keys.

**Important limits:** GTFS schedules are not evidence of on-time performance. No observations CSV means `on_time_pct=null`. The frontend's portfolio-only GitHub Pages build always uses synthetic snapshots, not the downloaded feed. Large GTFS files can exceed memory limits of the demo backend, and route shapes are simplified. Production-scale spatial indexing, service-calendar decoding, independent feed integrity review and a licensed realtime service are not yet provided. Do not use this module for travel advice.
