from fastapi import HTTPException, status
from tortoise.exceptions import IntegrityError

from code.common.service import BaseService
from .models import User


class RegisterService(BaseService):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    async def _create_user(self):
        try:
            return await User.create(email=self.email, hashed_password=self.password)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already registered',
            )

    async def do(self):
        return await self._create_user()
