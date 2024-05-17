from typing import List

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from .link_click_full import LinkClickFull


class GetShortenUrlStatusResponse(BaseModel):
    """
    Модель для получения статуса сокращённой ссылки.
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)

    shorten_url_id: int = Field(description='ID сокращённой ссылки')
    requests_count: int = Field(description='Количество запросов к сокращённой ссылке')
    deleted: bool = Field(description='Признак удаления сокращённой ссылки')
    link_clicks: List[LinkClickFull] = Field(description='Переходы по ссылке', default_factory=list)
