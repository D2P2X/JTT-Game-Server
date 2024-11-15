from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.database import connect, disconnect

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect()
    yield
    await disconnect()
