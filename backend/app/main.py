"""MobilityPulse API: transparent data provenance, optional access controls."""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routes import routes, stops, analytics, accessibility, delays
from backend.app.security import protect_requests

app = FastAPI(title="MobilityPulse AI", version="1.2.0",
              description="Transit analytics portfolio demonstration. Not an operational arrival service.")
app.middleware("http")(protect_requests)
origins=[s.strip() for s in os.getenv("CORS_ORIGINS","http://localhost:5173,http://localhost:8080").split(",") if s.strip()]
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=False,
                   allow_methods=["GET","POST"],allow_headers=["Content-Type","X-API-Key"])
for module in (routes,stops,analytics,accessibility,delays):
    app.include_router(module.router,prefix="/api")

@app.get("/api/health")
def health():
    return {"status":"ok","service":"mobilitypulse-ai","version":"1.2.0","live_tracking":False}
