from core.config import app_logger
from schemas import CreateShortenUrlRequest
from schemas import ShortenUrlCreate
from .common_utils import CommonUtils


class ShortenUrlCreateRowMapper:
    """
    Сборка модели ShortenUrlCreate.
    """

    @staticmethod
    async def get(create_data: CreateShortenUrlRequest) -> ShortenUrlCreate:
        """
        Сборка модели ShortenUrlCreate.

        :param create_data: Модель CreateShortenUrlRequest.
        :return: Модель ShortenUrlCreate.
        """
        app_logger.info(f'Create shorten url: {create_data}')
        return ShortenUrlCreate(
            full_url=create_data.full_url,
            short_url=CommonUtils.get_short_url()
        )
