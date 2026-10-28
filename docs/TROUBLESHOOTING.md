# Runbook and troubleshooting

## FastAPI gives ModuleNotFoundError
Run commands from repository root, install editable package with `python -m pip install -e .`, and set `PYTHONPATH=.:src` when working with standalone scripts in shells that do not detect the root.

## Frontend says API unavailable
Start `uvicorn backend.app.main:app --reload --port 8000`. Check `http://localhost:8000/api/health`. Vite proxies `/api` in dev; production needs a reachable separately deployed backend and correct `VITE_API_URL` and `CORS_ORIGINS`.

## Dataset is synthetic
This is expected by design. The fictional network does not represent a real operator. Provide a permitted `GTFS_ZIP_PATH` and, separately, a historical `OBSERVATIONS_CSV_PATH` if you have permission. Do not claim externally supplied records are verified without independent checks.

## API returns 503 for ML
No trained offline model is stored. Run `python -m mobilitypulse.models.train_delay_model --allow-synthetic`. A 503 is intentional and safer than pretending a model exists.

## Missing real-time status
There is no configured GTFS-RT polling service. Offline protobuf inspection is optional with `scripts/poll_rt.py`; it does not automatically update the dashboard.

## Docker build needs network
Docker installs Python/npm dependencies at build time. Ensure network and package registry access. Default ports are bound only to `127.0.0.1`.

## Accessibility metadata is incomplete
GTFS code 0 means unknown. Contact the agency for audited accessibility information and current lift/ramp status before using it for travel decisions.
