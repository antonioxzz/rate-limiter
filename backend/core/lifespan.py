from contextlib import asynccontextmanager
from fastapi import FastAPI
import redis.asyncio as redis

@asynccontextmanager
async def lifespan_manager(app: FastAPI):
    app.state.redis = redis.from_url("redis://redis:6379/0", decode_responses=True)
    try:
        yield
    finally:
        await app.state.redis.close()
