
import sys, os
sys.path.append(os.path.abspath(".."))

from fastapi import FastAPI
from app.core.startup import lifespan
from app.routers import test_api, database_api, user_api
from app.core.config import settings 

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

# 라우터 등록
app.include_router(test_api.router) # FastAPI에서 라우터를 애플리케이션에 등록하는 메서드입니다.
app.include_router(database_api.router)
app.include_router(user_api.router)

# 애플리케이션 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
