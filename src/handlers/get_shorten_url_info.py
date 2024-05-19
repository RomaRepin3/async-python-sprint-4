from sqlalchemy.ext.asyncio import AsyncSession

from depends import link_click_repository
from schemas import GetShortenUrlStatusResponse
from utils import GetShortenUrlStatusResponseRowMapper
from .get_shorten_url_model import get_shorten_url_model


async def get_shorten_url_info(
        shorten_url_id: int,
        session: AsyncSession,
        full_info: bool = True,
        max_result: int = 10,
        offset: int = 0
) -> GetShortenUrlStatusResponse:
    """
    Логика получения информации о сокращённой ссылке.

    :param shorten_url_id: ID сокращённой ссылки.
    :param session: Сессия БД.
    :param full_info: Флаг для получения полной информации о сокращённой ссылке.
    :param max_result: Максимальное количество результатов для получения.
    :param offset: Смещение для получения результатов.
    :return: Информация о сокращённой ссылке.
    """
    shorten_url_model = await get_shorten_url_model(shorten_url_id=shorten_url_id, session=session)
    link_clicks = await link_click_repository.get_multi_by_shorten_url_id(
        db=session,
        url_id=shorten_url_id,
        skip=offset,
        limit=max_result
    )
    return await GetShortenUrlStatusResponseRowMapper.get(
        shorten_url=shorten_url_model,
        link_clicks=link_clicks,
        is_full_info=full_info
    )
