from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "viton-backend"
    API_V1_STR : str = "../api/v1"
    DATABASE_URL : str

    def getDatabaseUrl (self) -> str:
        return self.DATABASE_URL
    
    model_config = ConfigDict(env_file="../../.env", case_sensitive=True)

settings = Settings()