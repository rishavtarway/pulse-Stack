from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client: Optional[AsyncIOMotorClient] = None

def get_client() -> AsyncIOMotorClient:
    global client
    if client is None:
        # We connect using components to avoid the URI parsing bug on Render
        client = AsyncIOMotorClient(
            host="cluster0.f6tseh9.mongodb.net",
            username="Rishav",
            password="Rishav2005", # Using your updated clean password
            tls=True,
            appName="Cluster0",
            uuidRepresentation="standard"
        )
    return client

async def ping():
    await get_client().admin.command("ping")

mongo_client = get_client()
