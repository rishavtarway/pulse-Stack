from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client: Optional[AsyncIOMotorClient] = None

def get_client() -> AsyncIOMotorClient:
    global client
    if client is None:
        uri = str(settings.MONGO_DATABASE_URI or "mongodb://localhost:27017")
        logger.info("Initializing MongoDB client...")
        client = AsyncIOMotorClient(
            uri,
            tls=True,
            tlsAllowInvalidCertificates=True,
            uuidRepresentation="standard"
        )
    return client

# This is what initial_data.py was looking for
def get_engine() -> AsyncIOMotorClient:
    return get_client()

# Re-adding MongoDatabase for the migration script
mongo_client = get_client()
MongoDatabase = mongo_client[settings.MONGO_DATABASE]

async def ping():
    await get_client().admin.command("ping")
