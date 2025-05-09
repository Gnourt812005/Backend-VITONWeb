from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import Optional
class Settings(BaseSettings):
    PROJECT_NAME: str = "viton-backend"
    API_V1_STR : str = "../api/v1"
    DATABASE_URL : str
    REDIS_HOST : Optional[str] = ""
    REDIS_PORT : Optional[str] = ""
    REDIS_USERNAME : Optional[str] = ""
    REDIS_PASSWORD : Optional[str] = ""

    def getDatabaseUrl (self) -> str:
        return self.DATABASE_URL
    #redis://<username>:<password>@<host>:<port>
    def getRedisUrl (self) -> str:
        return f"redis://{self.REDIS_USERNAME}:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = ConfigDict(env_file="../../.env", case_sensitive=True)

settings = Settings()