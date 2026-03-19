from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client: Optional[AsyncIOMotorClient] = None

def get_client() -> AsyncIOMotorClient:
    global client
    if client is None:
        client = AsyncIOMotorClient(
            str(settings.MONGO_DATABASE_URI),
            uuidRepresentation="standard"
        )
    return client

async def ping():
    await get_client().admin.command("ping")

mongo_client = get_client()
