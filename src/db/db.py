from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from src.core import app_settings

# Создаём движок
# Настройки подключения к БД передаём из переменных окружения, которые заранее загружены в файл настроек
engine = create_async_engine(app_settings.DATABASE_DSN, echo=True, future=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
