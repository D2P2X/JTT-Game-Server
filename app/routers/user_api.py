from fastapi import APIRouter, HTTPException
from app.models.user import User, UserInDB
from app.services.user_service import add_user, get_user, add_initial_data

router = APIRouter()

# 사용자 생성 API
@router.post("/users/", response_model=UserInDB)
async def create_user(user: User):
    try:
        last_record_id = await add_user(name=user.name, email=user.email)
        return {**user.dict(), "id": last_record_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# 사용자 조회 API
@router.get("/users/{user_id}", response_model=UserInDB)
async def read_user(user_id: int):
    user = await get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# 초기 데이터 삽입 API
@router.post("/users/initialize")
async def initialize_users():
    try:
        await add_initial_data()
        return {"message": "Initial data added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add initial data: {e}")