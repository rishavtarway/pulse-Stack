from typing import List, Union, Optional
from pydantic import AnyHttpUrl, EmailStr, validator
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    PROJECT_NAME: str = "PulseStack"
    DOMAIN: str = "pulse-stack.onrender.com"
    SERVER_NAME: str = "PulseStack"
    SERVER_HOST: AnyHttpUrl = "https://pulse-stack.onrender.com"
    
    # Strictly from Environment
    MONGO_DATABASE_URI: Optional[str] = None
    MONGO_DATABASE: str = "pulsestack_db"
    
    SECRET_KEY: str = os.getenv("SECRET_KEY", "temporary_dev_key_change_in_prod")
    TOTP_SECRET_KEY: str = os.getenv("TOTP_SECRET_KEY", "temporary_totp_key_change_in_prod")
    TOTP_ALGO: str = "sha256"
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    USERS_OPEN_REGISTRATION: bool = True
    FIRST_SUPERUSER: EmailStr = "admin@pulsestack.com"
    FIRST_SUPERUSER_PASSWORD: str = "PulseStackAdmin123"
    
    BACKEND_CORS_ORIGINS: List[str] = ["https://pulse-stack.onrender.com", "http://localhost:3000", "https://pulse-stack.vercel.app"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        return v

    EMAILS_ENABLED: bool = False

settings = Settings()
