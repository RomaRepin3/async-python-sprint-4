from logging import config as logging_config
from logging import getLogger

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from .logger import LOGGING

logging_config.dictConfig(LOGGING)
app_logger = getLogger('app')


class AppSettings(BaseSettings):
    """
    Настройки приложения.
    """
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    PROJECT_NAME: str
    DATABASE_DSN: str
    PROJECT_HOST: str
    PROJECT_PORT: int


app_settings = AppSettings()
