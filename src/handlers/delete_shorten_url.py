from sqlalchemy.ext.asyncio import AsyncSession

from depends import shorten_url_repository
from schemas import ShortenUrlFull
from utils import ShortenUrlFullRowMapper
from .get_shorten_url_model import get_shorten_url_model


async def delete_shorten_url_handler(shorten_url_id: int, session: AsyncSession) -> ShortenUrlFull:
    """
    Логика удаления сокращённой ссылки.

    :param shorten_url_id: ID сокращённой ссылки.
    :param session: Сессия БД.
    """
    shorten_url_model = await get_shorten_url_model(shorten_url_id=shorten_url_id, session=session)
    await shorten_url_repository.delete(db=session, id=shorten_url_id)
    return await ShortenUrlFullRowMapper.get_from_shorten_url_model(data=shorten_url_model)
