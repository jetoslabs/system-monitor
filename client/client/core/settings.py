from pydantic import BaseSettings


class Settings(BaseSettings):
    LOG_SERIALIZE = False
    LOG_LEVEL = "DEBUG"
    HOST = "localhost"
    PORT = 8765
    APP_RELOAD = True
    APP_WORKERS = 2
    API_V1_STR = "v1"


settings = Settings()
