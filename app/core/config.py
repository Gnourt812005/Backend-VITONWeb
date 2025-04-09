from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "viton-backend"
    API_V1_STR : str = "../api/v1"
    DATABASE_URL : str
    REDIS_HOST : str
    REDIS_PORT : str
    REDIS_USERNAME : str
    REDIS_PASSWORD : str

    def getDatabaseUrl (self) -> str:
        return self.DATABASE_URL
    #redis://<username>:<password>@<host>:<port>
    def getRedisUrl (self) -> str:
        return f"redis://{self.REDIS_USERNAME}:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = ConfigDict(env_file="../../.env", case_sensitive=True)

settings = Settings()