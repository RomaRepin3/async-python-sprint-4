from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import RedirectResponse

from depends import link_click_repository
from schemas import LinkClick
from utils import ExceptionFactory
from .get_shorten_url_model import get_shorten_url_model


async def get_original_url(shorten_url_id: int, session: AsyncSession) -> RedirectResponse:
    """
    Логика получения оригинального URL.

    :param shorten_url_id: ID сокращённой ссылки.
    :param session: Сессия БД.
    :return: Оригинальный URL.
    """
    shorten_url_model = await get_shorten_url_model(shorten_url_id=shorten_url_id, session=session)
    if shorten_url_model.is_deleted:
        raise await ExceptionFactory.get_410_exception(message='Shorten URL is deleted')
    await link_click_repository.create(db=session, obj_in=LinkClick(shorten_url_id=shorten_url_id))
    return RedirectResponse(url=shorten_url_model.full_url)
