# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Workout Tracker API"
    DEBUG: bool = True
    DATABASE_URL: str
    SECRET_KEY: str = "super-secret-change-this-in-production"

    # JWT algorithm used to sign and verify tokens
    ALGORITHM: str = "HS256"

    # Token expiry time in minutes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()