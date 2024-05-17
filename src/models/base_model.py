from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer

# Импортируем базовый класс для моделей.
from .base import Base


class BaseModel(Base):
    """
    Базовая модель БД.
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, doc='ID')
    created_at = Column(DateTime, index=True, default=datetime.utcnow, doc='Дата создания записи')
