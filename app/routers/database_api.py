from fastapi import APIRouter
from app.services.database_service import initialize_database, check_database_status

router = APIRouter()

# 데이터베이스 상태 확인
@router.get("/database/status")
async def get_database_status():
    status = await check_database_status()
    return {"status": status}

# 데이터베이스 초기화
@router.post("/database/initialize")
async def initialize_db():
    await initialize_database()
    return {"message": "Database initialized successfully"}
