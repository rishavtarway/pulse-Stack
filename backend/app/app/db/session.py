from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class _MongoClientSingleton:
    mongo_client: Optional[AsyncIOMotorClient] = None

    @classmethod
    def get_client(cls) -> AsyncIOMotorClient:
        if cls.mongo_client is None:
            cls.mongo_client = AsyncIOMotorClient(
                str(settings.MONGO_DATABASE_URI),
                uuidRepresentation="standard"
            )
        return cls.mongo_client

mongo_client = _MongoClientSingleton.get_client()
