from datetime import datetime

from pydantic import BaseModel
from pydantic import Field


class LinkClickFull(BaseModel):
    """
    Модель для хранения данных по кликам по ссылкам.
    """
    id: int = Field(description='ID')
    url_id: int = Field(description='ID сокращённой ссылки')
    created_at: datetime = Field(description='Дата создания записи')
