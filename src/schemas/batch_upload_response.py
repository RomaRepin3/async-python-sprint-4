from typing import Dict
from typing import List

from pydantic import BaseModel
from pydantic import Field

from .shorten_url_full import ShortenUrlFull


class BatchUploadResponse(BaseModel):
    """
    Модель ответа для пакетной загрузки ссылок.
    """

    shorten_url_models: List[ShortenUrlFull] = Field(description='Сокращённые ссылки')
    errors: List[Dict[str, str]] = Field(description='Ошибки', default_factory=list)
