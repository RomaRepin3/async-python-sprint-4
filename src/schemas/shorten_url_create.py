from pydantic import BaseModel
from pydantic import Field


class ShortenUrlCreate(BaseModel):
    """
    Модель для создания сокрашённой ссылки.
    """
    full_url: str = Field(description='URL для сокращённой ссылки', max_length=100)
    short_url: str = Field(description='Сокращённый URL', max_length=100)
