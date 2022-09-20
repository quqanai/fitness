from code.common.service import BaseService
from .models import Trainee


class CreateTraineeService(BaseService):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    async def _create_trainee(self):
        return await Trainee.create(first_name=self.first_name, last_name=self.last_name)

    async def do(self):
        return await self._create_trainee()
