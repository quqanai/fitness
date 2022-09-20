from tortoise.contrib.pydantic import pydantic_model_creator

from .models import Trainee

TraineeCreateSchema = pydantic_model_creator(Trainee, include=('first_name', 'last_name'))
