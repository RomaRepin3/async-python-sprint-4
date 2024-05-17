from pydantic import BaseModel
from pydantic import Field


class CreateShortenUrlRequest(BaseModel):
    """
    Модель для создания сокращённой ссылки.
    """
    full_url: str = Field(
        description='URL для сокращённой ссылки',
        max_length=100,
        pattern=r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$',
        example='https://www.test.ru'
    )
