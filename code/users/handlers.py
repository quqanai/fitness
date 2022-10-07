from .schemas import RegisterSchema
from .service import RegisterService


async def register(register_data: RegisterSchema):
    token = await RegisterService(register_data.email, register_data.password).do()
    return {'token': token}
