from sqlalchemy.ext.asyncio import AsyncSession

from depends import shorten_url_repository
from models import ShortenUrlModel
from utils import ExceptionFactory


async def get_shorten_url_model(shorten_url_id: int, session: AsyncSession) -> ShortenUrlModel:
    """
    Логика получения модели сокращённой ссылки.

    :param shorten_url_id: ID сокращённой ссылки.
    :param session: Сессия БД.
    :return: Модель сокращённой ссылки.
    :raises HTTPException: Если сокращённой ссылки не существует.
    """
    shorten_url_model = await shorten_url_repository.get(db=session, id=shorten_url_id)
    if not shorten_url_model:
        raise await ExceptionFactory.get_404_exception(message='Shorten URL not found')
    return shorten_url_model
