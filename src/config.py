from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = Field(default="LeibnizCal", env="APP_NAME")
    debug: bool = Field(default=False, env="DEBUG")
    database_url: str = Field(default="sqlite:///./leibniz.db", env="DATABASE_URL")
    host: str = Field(default="127.0.0.1", env="HOST")
    port: int = Field(default=8000, env="PORT")

    class Config:
        env_file = ".env"  # Se busca en la raíz del proyecto

settings = Settings()
