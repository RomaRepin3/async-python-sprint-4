from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import app_logger
from models import LinkClickModel
from schemas import LinkClick
from .repository_db import RepositoryDB


class LinkClickRepository(RepositoryDB[LinkClickModel, LinkClick, LinkClick]):
    """
    Репозиторий для работы с кликами по ссылкам.
    """

    async def get_multi_by_shorten_url_id(
            self,
            db: AsyncSession,
            url_id: int,
            *,
            skip=0,
            limit=100
    ) -> List[LinkClickModel]:
        """
        Поиск кликов по ID сокращённой ссылки.
        
        :param db: Сессия БД.
        :param url_id: ID сокращённой ссылки.
        :param skip: Смещение.
        :param limit: Ограничение.
        :return: Список кликов по ID сокращённой ссылки.
        """
        app_logger.info(f'Getting clicks by shorten url id: {url_id}, skip={skip}, limit={limit}')
        statement = select(LinkClickModel).where(LinkClickModel.shorten_url_id == url_id).offset(skip).limit(limit)
        results = await db.execute(statement=statement)
        app_logger.info('Get clicks by shorten url id is OK!')
        return list(results.scalars().all())
