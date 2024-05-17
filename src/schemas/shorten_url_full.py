from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class ShortenUrlFull(BaseModel):
    """
    Модель для передачи данных о ссылке.
    """
    id: int = Field(description='ID')
    full_url: str = Field(description='Полный URL')
    short_url: str = Field(description='Сокращённый URL')
    is_deleted: bool = Field(description='Признак удаления ссылки')
    created_at: datetime = Field(description='Дата создания записи')
