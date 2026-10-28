"""Optional API-key and in-process limiting for demonstration deployments.

A real internet-facing service needs upstream throttling, observability,
authentication design, proxy trust policy and multi-instance controls.
"""
import hmac
import os
import time
from collections import defaultdict
from threading import Lock
from fastapi import Request
from fastapi.responses import JSONResponse

_hits=defaultdict(list)
_lock=Lock()
def _limit():
    try:return min(10000,max(0,int(os.getenv("MOBILITYPULSE_RATE_LIMIT_PER_MINUTE","0"))))
    except ValueError:return 0

async def protect_requests(request:Request,call_next):
    path=request.url.path
    if path.startswith("/api/"):
        expected=os.getenv("MOBILITYPULSE_API_KEY","")
        if expected and path!="/api/health":
            given=request.headers.get("x-api-key","")
            if not hmac.compare_digest(given,expected):
                return JSONResponse({"detail":"API key required"},status_code=401,headers={"Cache-Control":"no-store"})
        max_body=int(os.getenv("MOBILITYPULSE_MAX_POST_BYTES","8192"))
        if request.method in {"POST","PUT","PATCH"}:
            size=request.headers.get("content-length")
            if size and size.isdecimal() and int(size)>max_body:
                return JSONResponse({"detail":"Request body too large"},status_code=413)
        limit=_limit()
        if limit:
            client=request.client.host if request.client else "unknown"
            now=time.monotonic()
            with _lock:
                history=_hits[(client,path)]
                history[:]=[t for t in history if now-t<60]
                if len(history)>=limit:
                    return JSONResponse({"detail":"Rate limit exceeded"},status_code=429,headers={"Retry-After":"60"})
                history.append(now)
                if len(_hits)>5000:
                    for key in list(_hits)[:1000]:
                        if not _hits[key] or now-_hits[key][-1]>60:
                            del _hits[key]
    response=await call_next(request)
    response.headers["X-Content-Type-Options"]="nosniff"
    response.headers["X-Frame-Options"]="DENY"
    response.headers["Referrer-Policy"]="no-referrer"
    response.headers["Cache-Control"]="no-store"
    return response
