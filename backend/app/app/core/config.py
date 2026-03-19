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
    
    # Mongo Settings
    MONGO_DATABASE_URI: str = "mongodb+srv://Rishav:Rishav21@@cluster0.f6tseh9.mongodb.net/?appName=Cluster0"
    MONGO_DATABASE: str = "pulsestack_db"
    
    # Security
    SECRET_KEY: str = "b47fefafd0ec5d1c9faf3571832023f4"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    
    # Registration & Auth
    USERS_OPEN_REGISTRATION: bool = True
    FIRST_SUPERUSER: EmailStr = "admin@pulsestack.com"
    FIRST_SUPERUSER_PASSWORD: str = "PulseStackAdmin123"
    
    # CORS
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

    # SMTP Settings (Optional for now to prevent crashes)
    EMAILS_ENABLED: bool = False
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

settings = Settings()
