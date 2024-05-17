from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String

from .base_model import BaseModel


class ShortenUrlModel(BaseModel):
    """
    Модель для хранения ссылок.
    """
    __tablename__ = 'shorten_url'

    full_url = Column(String(100), unique=True, nullable=False, doc='Полный URL')
    short_url = Column(String(100), unique=True, nullable=False, doc='Сокращённый URL')
    is_deleted = Column(Boolean, default=False, nullable=False, doc='Признак удаления записи')
