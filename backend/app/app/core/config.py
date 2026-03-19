from typing import List, Union
from pydantic import AnyHttpUrl, EmailStr, validator, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
import json
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    PROJECT_NAME: str = "PulseStack"
    DOMAIN: str = "localhost"
    SERVER_NAME: str = "PulseStack"
    SERVER_HOST: AnyHttpUrl = "http://localhost"
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    SECRET_KEY: str = "b47fefafd0ec5d1c9faf3571832023f4"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    EMAILS_ENABLED: bool = False
    
    MONGO_DATABASE_URI: str = "mongodb://localhost:27017"
    MONGO_DATABASE: str = "pulsestack_db"
    
    FIRST_SUPERUSER: EmailStr = "admin@pulsestack.com"
    FIRST_SUPERUSER_PASSWORD: str = "PulseStackAdmin123"
settings = Settings()
