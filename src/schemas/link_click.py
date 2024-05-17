from pydantic import BaseModel
from pydantic import Field


class LinkClick(BaseModel):
    """
    Модель для хранения данных по кликам по ссылкам.
    """
    shorten_url_id: int = Field(description='ID сокращённой ссылки')
