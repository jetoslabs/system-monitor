from pydantic import BaseSettings


class Settings(BaseSettings):
    LOG_SERIALIZE = False
    LOG_LEVEL = "DEBUG"
    HOST = "localhost"
    PORT = 8765
    APP_RELOAD = True
    APP_WORKERS = 2
    API_V1_STR = "v1"

    NATS_URI = "nats://127.0.0.1:4222"
    NATS_TOPIC_VITALS = "vitals"


settings = Settings()
