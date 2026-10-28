# Optional API hardening and deployment limits

Added `backend/app/security.py`:
- Env-based `MOBILITYPULSE_API_KEY` and constant-time header check for protected API endpoints.
- `MOBILITYPULSE_MAX_POST_BYTES` content-length limit (default 8192 bytes).
- Optional in-process `MOBILITYPULSE_RATE_LIMIT_PER_MINUTE`.
- CORS explicit origin allowlist and X-Content-Type-Options, frame and referrer safeguards.
- No default secrets embedded in source or React bundles.

These are developer guardrails, **not production security certification**. If the API is consumed by public browser clients, a shared API key embedded in JavaScript is not secret. Prefer an authenticated server-side proxy or public read-only endpoints protected by infrastructure rate limits. Multiple API replicas require centralized distributed rate limiting. Validate trusted proxy headers at the ingress, use HTTPS, request/log limits, dependency scanning, managed secrets, incident monitoring, and independent pen-testing. No PII should be collected by the demo.

For dedicated hosting, the backend has a health endpoint `GET /api/health`. Cloud hosting accounts and credentials must be configured by the owner, separately from this repository.
