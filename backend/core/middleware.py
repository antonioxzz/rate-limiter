import time
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

RATE_LIMIT_DURATION = 60
RATE_LIMIT_REQUESTS = 10

class RateLimitingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if not request.url.path.startswith("/api"):
            return await call_next(request)
        
        redis_client = request.app.state.redis
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"

        p = redis_client.pipeline()
        p.incr(key)
        p.expire(key, RATE_LIMIT_DURATION, nx=True)
        results = await p.execute()
        
        request_count = results[0]
        ttl = await redis_client.ttl(key)
        
        headers = {
            "X-RateLimit-Limit": str(RATE_LIMIT_REQUESTS),
            "X-RateLimit-Remaining": str(RATE_LIMIT_REQUESTS - request_count),
            "X-RateLimit-Reset": str(ttl)
        }

        if request_count > RATE_LIMIT_REQUESTS:
            return Response(status_code=429, content="Too Many Requests", headers=headers)

        response = await call_next(request)
        response.headers.update(headers)
        return response
