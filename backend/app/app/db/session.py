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
        
        # Robust URI escaping: find the last '@' as the separator
        try:
            if "://" in uri and "@" in uri:
                scheme, rest = uri.split("://", 1)
                auth, host = rest.rsplit("@", 1)
                if ":" in auth:
                    user, password = auth.split(":", 1)
                    # Use quote_plus for password instead of raw password to handle special chars like '@'
                    safe_user = urllib.parse.quote_plus(user)
                    safe_password = urllib.parse.quote_plus(password)
                    uri = f"{scheme}://{safe_user}:{safe_password}@{host}"
        except Exception:
            pass # Fallback to original URI if something goes wrong
            
        client = AsyncIOMotorClient(
            uri,
            uuidRepresentation="standard"
        )
    return client

async def ping():
    await get_client().admin.command("ping")

mongo_client = get_client()
