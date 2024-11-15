from fastapi import APIRouter
from app.models.response import ResponseData
import asyncio

router = APIRouter()

@router.get("/test", response_model=ResponseData)
async def handle():
    await asyncio.sleep(1)  # 비동기 대기 (예: 데이터베이스 호출 시뮬레이션)
    response_data = ResponseData(
        message="Hello, Async World!" * 100,
        author="Naeun Song"
    )
    return response_data
