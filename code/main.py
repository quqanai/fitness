from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from code import trainees, users
from code.common.settings import MODELS, settings

app = FastAPI()
app.include_router(users.router, prefix='/users')
app.include_router(trainees.router, prefix='/trainees')

register_tortoise(
    app,
    db_url=settings.database_url,
    modules={'models': MODELS},
)
