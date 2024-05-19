from sqlalchemy.ext.asyncio import AsyncSession

from depends import shorten_url_repository
from models import ShortenUrlModel
from schemas import CreateShortenUrlRequest
from utils import ExceptionFactory
from utils import ShortenUrlCreateRowMapper


async def create_shorten_url_model(create_data: CreateShortenUrlRequest, session: AsyncSession) -> ShortenUrlModel:
    """
    Логика создания модели сокращённого URL.

    :param create_data: Данные для создания сокращённого URL.
    :param session: Сессия БД.
    :return: Модель сокращённого URL.
    """
    shorten_url_create = await ShortenUrlCreateRowMapper.get(create_data=create_data)
    try:
        return await shorten_url_repository.create(db=session, obj_in=shorten_url_create)
    except Exception as e:
        raise await ExceptionFactory.get_400_exception(message=f'{type(e).__name__}, args: {e.args}')
