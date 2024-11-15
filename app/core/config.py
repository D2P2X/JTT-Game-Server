from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(default='', env="DATABASE_URL")  # 필수 환경 변수
    APP_NAME: str = Field(default="App_NAME", env="APP_NAME")
    DEBUG_MODE: bool = Field(default=False, env="DEBUG_MODE")

    class Config:
        env_file = ".env"  # .env 파일에서 환경 변수를 로드
        env_file_encoding = "utf-8"  # .env 파일의 인코딩을 utf-8로 설정

# 설정 인스턴스 생성
settings = Settings()
