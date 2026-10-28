"""MobilityPulse API: clear separation of scheduled, observed, and synthetic data."""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routes import routes, stops, analytics, accessibility, delays

app = FastAPI(title="MobilityPulse AI", version="1.1.0",
              description="Transport analytics portfolio demonstration. No live arrival guarantees.")
origins = [s.strip() for s in os.getenv("CORS_ORIGINS","http://localhost:5173,http://localhost:8080").split(",") if s.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=False,
                   allow_methods=["GET", "POST"], allow_headers=["Content-Type"])
for module in (routes, stops, analytics, accessibility, delays):
    app.include_router(module.router, prefix="/api")

@app.get("/api/health")
def health():
    return {"status":"ok","service":"mobilitypulse-ai","version":"1.1.0"}
