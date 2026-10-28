# Security and responsible deployment

This repository is for local educational demonstration, not a production transit service. No secrets or credentials belong in source control. Use `.env` ignored by Git, restrict real API credentials to server-side secret stores, and review agency feed licensing before ingestion.

Before hosting publicly: enforce HTTPS and origin restrictions, protect the API with throttling/auth as needed, implement data retention and logging policies, scan dependencies, validate external feed sizes/types, isolate processing, configure health probes and monitor data freshness. The optional RT downloader enforces a 10MB response limit and must only query authorized endpoints.

Report vulnerabilities privately to the project maintainer. Avoid publicly posting exploit details or credentials.
