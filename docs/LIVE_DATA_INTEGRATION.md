# Real GTFS-Realtime integration path (opt-in, diagnostics only)

The repository includes a bounded, allowlisted HTTPS client for GTFS-Realtime protobuf in `src/mobilitypulse/ingestion/gtfs_realtime_client.py` and a manual refresh command in `scripts/refresh_realtime.py`.

It **does not** silently fetch data, start a live feed polling service, capture passenger information, or imply a real ETA.

## What you need

1. Explicitly authorized, published operator GTFS-Realtime protobuf endpoint and its terms/license.
2. Configured `GTFS_RT_URL=https://agency.example.org/gtfs-rt` (replace fictional example with actual authorized URL).
3. Configured `GTFS_RT_ALLOWED_HOSTS=agency.example.org` with exact hostname.
4. Keep any operator API key on the server side, in a credential manager. The included client targets public authorized endpoints without embedded credentials.
5. Run `python scripts/refresh_realtime.py` on a controlled server and place periodic polling behind an authorized scheduler if provider terms permit.

The refresh script saves a local JSON summary with feed timestamp, staleness, entity counts, and whether it is used for predictions (false). The API `GET /api/feed/status` can report a fresh feed if this file exists, but keeps `live_tracking=false` because no vehicle/ETA UI has been validated. In GitHub Pages the feed-health output is a frozen demo snapshot, not live information.

Security: only HTTPS and exact allowlisted hosts; deny redirects, credential-containing URLs, IP-literal targets, and responses over 10 MB. This is **not** a hardened multi-tenant SSRF boundary; only operators who control trusted server configuration should provide feed URLs.

## For true live passenger ETA

Actual operational integration still requires matching trip IDs and service dates against current GTFS schedules, operator timezone rules, verified vehicle update timestamps, stale-feed fallback, service alerts, continuous polling with retries, authorized data processing, privacy review, QA with agency historical observations, and independent model validation before public rider use.

Spec references:
- https://gtfs.org/documentation/realtime/reference/
- https://gtfs.org/documentation/realtime/realtime-best-practices/
