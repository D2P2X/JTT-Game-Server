from app.db.database import database
from app.db.models import metadata

# 데이터베이스 초기화
async def initialize_database():
    await database.connect()
    metadata.create_all()
    await database.disconnect()

# 데이터베이스 상태 확인
async def check_database_status():
    try:
        await database.connect()
        await database.disconnect()
        return "connected"
    except Exception:
        return "disconnected"

