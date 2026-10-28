# Deployment guide

## Local Docker

```bash
docker compose up --build
```

Frontend: `http://localhost:8080`; API docs: `http://localhost:8000/docs`. Development bindings use localhost only.

## Local source development

Run `pip install -r requirements.txt && pip install -e .` and `uvicorn backend.app.main:app --reload --port 8000`. For React run `cd frontend && npm install && npm run dev`. Vite proxies `/api` to localhost:8000.

## Public hosting (not deployed by this repository)

The frontend's production build comes from `frontend/`: `npm run build` outputs `dist/`. Host the FastAPI server separately with HTTPS. Set `VITE_API_URL=https://your-api.example` at frontend build time; set `CORS_ORIGINS` on the API to the actual site origin. Health endpoint: `/api/health`. This demo includes no multi-user authentication, managed database, rate limiting, WAF, monitoring stack or uptime SLA; add them before production usage. HTTPS, data licensing, server limits, and an independently verified source are required for public service.

## GitHub Actions

`.github/workflows/ci.yml` runs API data tests, reproducible synthetic fixture generation, CSV exports, offline model checks and a React production build. A passing workflow verifies build integrity only; it is not a claim about actual transit prediction performance.
