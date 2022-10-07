from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from tortoise.exceptions import DoesNotExist

from code.users.models import User
from .settings import settings

security = HTTPBearer()


async def current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, settings.secret_key)
        user = await User.get(id=payload['user_id'])
    except (JWTError, DoesNotExist):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return user
