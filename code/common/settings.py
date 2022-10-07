from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    database_url: PostgresDsn
    secret_key: str


settings = Settings()

MODELS = [
    'code.users.models',
    'code.trainees.models',
]

TORTOISE_CONFIG = {
    'connections': {'default': settings.database_url},
    'apps': {
        'models': {
            'models': [*MODELS, 'aerich.models'],
            'default_connection': 'default',
        },
    },
}
