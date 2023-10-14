from fastapi import Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader


API_KEY = "s3cr3t"

api_key_header = APIKeyHeader(name="X-API-KEY")


def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key == API_KEY:
        return api_key

    raise HTTPException(status_code=403, detail="Invalid API key")
