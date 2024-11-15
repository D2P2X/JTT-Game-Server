from app.db.database import database
from app.db.models import users

# 사용자 추가 함수
async def add_user(name: str, email: str):
    query = users.insert().values(name=name, email=email)
    return await database.execute(query)

# 사용자 조회 함수
async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)

# 초기 데이터 삽입 함수
async def add_initial_data():
    await database.connect()  # 데이터베이스 연결

    # 초기 데이터 목록
    users_data = [
        {"name": "Naeun", "email": "naeun@example.com"},
        {"name": "Yukyung", "email": "yukyung@example.com"},
        {"name": "Justice", "email": "justice@example.com"},
        {"name": "Geonsu", "email": "geonsu@example.com"},
        {"name": "Youngyoo", "email": "youngyoo@example.com"},
    ]

    # 데이터 삽입
    for user in users_data:
        try:
            await add_user(name=user["name"], email=user["email"])
        except Exception as e:
            print(f"Failed to add user {user['name']}: {e}")

    await database.disconnect()  # 데이터베이스 연결 해제
