from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Lazy initialization: don't connect until actually asked
_client_instance: Optional[AsyncIOMotorClient] = None
def get_client() -> AsyncIOMotorClient:
    global _client_instance
    if _client_instance is None:
        uri = str(settings.MONGO_DATABASE_URI or "mongodb://localhost:27017")
        logger.info("Connecting to MongoDB Atlas...")
        _client_instance = AsyncIOMotorClient(
            uri,
            serverSelectionTimeoutMS=10000,
            tls=True,
            tlsAllowInvalidCertificates=True,
            uuidRepresentation="standard"
        )
    return _client_instance
def get_engine() -> AsyncIOMotorClient:
    return get_client()
# Re-creating the objects needed for migration as proxy objects
class MongoProxy:
    def __getattr__(self, name):
        client = get_client()
        db = client[settings.MONGO_DATABASE]
        return getattr(db, name)
    def __getitem__(self, name):
        client = get_client()
        return client[settings.MONGO_DATABASE][name]
# These now will NOT crash on import, only when the script tries to use them
mongo_client = None # Will be initialized inside get_client
MongoDatabase = MongoProxy()
mongo_db = MongoDatabase
