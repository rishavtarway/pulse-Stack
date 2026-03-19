from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
import urllib.parse

client: Optional[AsyncIOMotorClient] = None

def get_client() -> AsyncIOMotorClient:
    global client
    if client is None:
        raw_uri = str(settings.MONGO_DATABASE_URI).strip()
        
        # We handle the 'mongodb+srv' scheme manually to avoid mis-parsing
        if raw_uri.startswith("mongodb+srv://") and "@" in raw_uri:
            try:
                # 1. Strip the prefix
                content = raw_uri[len("mongodb+srv://"):]
                # 2. Split at the LAST '@' to find the Host
                # This ensures any '@' in the password stay in the credentials part
                creds, host_part = content.rsplit("@", 1)
                
                # 3. Handle User:Password
                if ":" in creds:
                    user, password = creds.split(":", 1)
                    # Quote EVERYTHING using quote (not quote_plus) as required by RFC 3986
                    safe_user = urllib.parse.quote(user)
                    safe_password = urllib.parse.quote(password)
                    uri = f"mongodb+srv://{safe_user}:{safe_password}@{host_part}"
                else:
                    uri = raw_uri
            except Exception:
                uri = raw_uri
        else:
            uri = raw_uri
            
        client = AsyncIOMotorClient(
            uri,
            uuidRepresentation="standard"
        )
    return client

async def ping():
    await get_client().admin.command("ping")

mongo_client = get_client()
