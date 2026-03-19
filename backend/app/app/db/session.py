from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import urllib.parse
import re

client: Optional[AsyncIOMotorClient] = None

def get_client() -> AsyncIOMotorClient:
    global client
    if client is None:
        uri = str(settings.MONGO_DATABASE_URI)
        
        # Aggressive Regex to catch and escape password
        # This handles passwords with @, :, or / seamlessly
        match = re.search(r'^(mongodb(?:\+srv)?://)([^:]+):(.+)(@.+)$', uri)
        if match:
            prefix, user, password, suffix = match.groups()
            safe_user = urllib.parse.quote_plus(user)
            safe_password = urllib.parse.quote_plus(password)
            uri = f"{prefix}{safe_user}:{safe_password}{suffix}"
            
        client = AsyncIOMotorClient(
            uri,
            uuidRepresentation="standard"
        )
    return client

async def ping():
    await get_client().admin.command("ping")

mongo_client = get_client()
