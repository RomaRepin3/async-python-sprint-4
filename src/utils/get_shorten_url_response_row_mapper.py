from typing import List
from typing import Optional

from core.config import app_logger
from models import LinkClickModel
from models import ShortenUrlModel
from schemas import GetShortenUrlStatusResponse
from schemas import LinkClickFull


class GetShortenUrlStatusResponseRowMapper:
    """
    Сборка модели GetShortenUrlStatusResponse.
    """

    @staticmethod
    async def get(
            shorten_url: ShortenUrlModel,
            link_clicks: Optional[List[LinkClickModel]],
            is_full_info: bool = True
    ) -> GetShortenUrlStatusResponse:
        """
        Сборка модели GetShortenUrlStatusResponse.

        :param shorten_url: Модель БД ShortenUrlModel.
        :param link_clicks: Переходы по ссылке.
        :param is_full_info: Полная информация.
        :return: Модель GetShortenUrlStatusResponse.
        """
        app_logger.info(f'Get status response for shorten url: {shorten_url}')
        links_schemas = [
            LinkClickFull(id=link.id, url_id=link.shorten_url_id, created_at=link.created_at) for link in link_clicks
        ]
        return GetShortenUrlStatusResponse(
            shorten_url_id=shorten_url.id,
            requests_count=len(link_clicks),
            deleted=shorten_url.is_deleted,
            link_clicks=links_schemas if is_full_info else list()
        )
