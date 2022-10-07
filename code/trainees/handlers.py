from fastapi import Depends

from code.common.dependencies import current_user
from code.users.models import User
from .models import Trainee
from .schemas import TraineeCreateSchema
from .service import CreateTraineeService


async def create(trainee_data: TraineeCreateSchema):
    return await CreateTraineeService(trainee_data.first_name, trainee_data.last_name).do()


async def get_all(user: User = Depends(current_user)):
    return await Trainee.all()
