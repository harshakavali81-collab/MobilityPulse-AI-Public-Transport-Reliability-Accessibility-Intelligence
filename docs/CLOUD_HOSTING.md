# Optional cloud API deployment

The portfolio and dashboard can be published through GitHub Pages as a standalone **synthetic-only static site**. A real FastAPI server cannot run on GitHub Pages.

`render.yaml` is an **optional configuration template** for a separately hosted FastAPI process. It has NOT been deployed. The project owner must connect an account to a cloud provider, review pricing, set exact CORS origins and authorize production secrets and source-data credentials.

Before exposing the backend:
1. Provision a vetted host with HTTPS, appropriate secrets storage and operational monitoring.
2. Set `CORS_ORIGINS` to the exact frontend HTTPS origin. Never set wildcard for a credentialed service.
3. Configure `MOBILITYPULSE_API_KEY` only for server-to-server clients; never expose it in React `VITE_*` variables.
4. Use a managed API gateway or WAF for authentication and distributed throttling; in-process limit is a demo fallback.
5. Obtain permitted data feeds and verify right-to-use, accuracy, service date/time zones and any privacy requirements.
6. Test with independent historical actual arrival observations before deploying model predictions.

GitHub Actions compilation and offline synthetic ML evaluation **do not** prove public production safety or realtime accuracy. The deployed static dashboard will intentionally continue to use synthetic snapshots even if the backend is later hosted elsewhere.
