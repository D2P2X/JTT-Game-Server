from sqlalchemy import create_engine, MetaData
from databases import Database
from app.core.config import settings 

database = Database(settings.DATABASE_URL)
metadata = MetaData()
engine = create_engine(settings.DATABASE_URL)

async def connect():
    await database.connect()

async def disconnect():
    await database.disconnect()
