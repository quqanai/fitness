from .schemas import RegisterSchema
from .service import RegisterService


async def register(register_data: RegisterSchema):
    await RegisterService(register_data.email, register_data.password).do()
    return register_data
