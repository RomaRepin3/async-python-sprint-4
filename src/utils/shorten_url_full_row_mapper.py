from core.config import app_logger
from models import ShortenUrlModel
from schemas import ShortenUrlFull


class ShortenUrlFullRowMapper:
    """
    Сборка модели ShortenUrlFull.
    """

    @staticmethod
    async def get_from_shorten_url_model(data: ShortenUrlModel) -> ShortenUrlFull:
        """
        Сборка модели ShortenUrlFull.

        :param data: Модель БД ShortenUrlModel.
        :return: Модель ShortenUrlFull.
        """
        app_logger.info(f'Get full info for shorten url: {data}')
        return ShortenUrlFull(
            id=data.id,
            full_url=data.full_url,
            short_url=data.short_url,
            is_deleted=data.is_deleted,
            created_at=data.created_at
        )
