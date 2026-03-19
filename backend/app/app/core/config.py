from typing import List, Union, Optional
from pydantic import AnyHttpUrl, EmailStr, validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    PROJECT_NAME: str = "PulseStack"
    DOMAIN: str = "pulse-stack.onrender.com"
    SERVER_NAME: str = "PulseStack"
    SERVER_HOST: AnyHttpUrl = "https://pulse-stack.onrender.com"
    
    # These must be set in Render environment variables
    # MONGO_DATABASE_URI, MONGO_DATABASE, etc.
    MONGO_DATABASE_URI: str = "mongodb://localhost:27017" # Default for local
    MONGO_DATABASE: str = "pulsestack_db"
    
    SECRET_KEY: str = "b47fefafd0ec5d1c9faf3571832023f4"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    TOTP_SECRET_KEY: str = "87eb2e3130c0c66048d087b21e8e5d1c"
    TOTP_ALGO: str = "sha256"
    
    USERS_OPEN_REGISTRATION: bool = True
    FIRST_SUPERUSER: EmailStr = "admin@pulsestack.com"
    FIRST_SUPERUSER_PASSWORD: str = "PulseStackAdmin123"
    
    BACKEND_CORS_ORIGINS: List[str] = [
        "https://pulse-stack.onrender.com",
        "http://localhost:3000",
        "https://pulse-stack.vercel.app"
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        return v

    EMAILS_ENABLED: bool = False
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

settings = Settings()
