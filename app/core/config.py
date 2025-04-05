from pydantic_settings import BaseSettings
import os 
# from typing import Optional, Any, Dict, Any 
class Settings(BaseSettings):
    PROJECT_NAME: str = "viton-backend"
    API_V1_STR : str = "../api/v1"
    DATABASE_URL : str

    def getDatabaseUrl (self) -> str:
        return self.DATABASE_URL

    class Config:
        env_file = "../../.env"
        case_sensitive = True

settings = Settings()