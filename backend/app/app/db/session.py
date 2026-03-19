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
def get_engine() -> AsyncIOMotorClient:
    return get_client()
# Re-creating the objects needed for migrations
# We initialize them only on the first import of this module
mongo_client = get_client()
MongoDatabase = mongo_client[settings.MONGO_DATABASE]
# This alias helps during the pre-start checks
mongo_db = MongoDatabase
