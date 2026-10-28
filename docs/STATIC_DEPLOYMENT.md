# Portfolio + offline dashboard on GitHub Pages

This repository includes a repeatable GitHub Pages workflow in `.github/workflows/pages.yml`.

## Deployed public content
- `/` redirects to `/portfolio/`.
- `/portfolio/` is the static recruiter-facing case study.
- `/demo/` is the React dashboard built with frozen, generated **synthetic** JSON snapshots.
- `/assets/` exposes ten original SVG visuals.

**Important:** GitHub Pages only serves static files; it does not run the Python API, connect to live vehicles, or train ML models. The dashboard is intentionally marked demo and its data may represent fictional dates.

## One-time setting (only if Pages has not been enabled)

Repository → **Settings → Pages → Build and deployment → Source → GitHub Actions**.

Then use **Actions → Publish MobilityPulse Portfolio and Offline Demo → Run workflow**, or push a commit to main.

If the GitHub Pages workflow reports a Pages configuration error, enable Pages in repository Settings; the linked GitHub connector cannot change administration settings.

Pages website (only after a successful workflow deploy):
`https://harshakavali81-collab.github.io/MobilityPulse-AI-Public-Transport-Reliability-Accessibility-Intelligence/`

Offline dashboard:
`https://harshakavali81-collab.github.io/MobilityPulse-AI-Public-Transport-Reliability-Accessibility-Intelligence/demo/`

Never describe this static site as a live transit or backend production deployment.

## Build locally

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
python scripts/export_static_api.py
cd frontend
VITE_STATIC_DEMO=true VITE_BASE_PATH=/demo/ npm run build
```

For Windows PowerShell, set environment variables with `$env:VITE_STATIC_DEMO = 'true'` and `$env:VITE_BASE_PATH = '/demo/'` before `npm run build`.
