from pydantic import BaseModel
from pydantic import Field


class ShortenUrlUpdate(BaseModel):
    """
    Полная модель сокращённой ссылки.
    """
    full_url: str = Field(description='Полный URL')
    short_url: str = Field(description='Сокращённый URL')
    is_deleted: bool = Field(description='Признак удаления ссылки')
