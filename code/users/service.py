from fastapi import HTTPException, status
from jose import jwt
from passlib.context import CryptContext
from tortoise.exceptions import IntegrityError

from code.common.service import BaseService
from code.common.settings import settings
from .models import User

pwd_context = CryptContext(schemes=['bcrypt'])


class RegisterService(BaseService):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def _hash_password(self, password: str):
        return pwd_context.hash(password)

    async def _create_user(self, hashed_password: str):
        try:
            return await User.create(email=self.email, hashed_password=hashed_password)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already registered',
            )

    def _create_token(self, user: User):
        payload = {'user_id': str(user.id)}
        return jwt.encode(payload, settings.secret_key)

    async def do(self):
        hashed_password = self._hash_password(self.password)
        user = await self._create_user(hashed_password)
        return self._create_token(user)
