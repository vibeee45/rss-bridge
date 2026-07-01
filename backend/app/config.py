from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME = "RSS Bridge"
    VERSION = "1.0.0"


settings = Settings()