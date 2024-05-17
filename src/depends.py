from sqlalchemy.ext.asyncio import AsyncSession

from db import async_session
from models import LinkClickModel
from models import ShortenUrlModel
from services import LinkClickRepository
from services import ShortenUrlRepository

shorten_url_repository = ShortenUrlRepository(ShortenUrlModel)
link_click_repository = LinkClickRepository(LinkClickModel)


async def get_session() -> AsyncSession:
    """
    Функция при внедрении зависимостей с БД.
    """
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
