from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import app_logger
from schemas import DatabaseCheckResponse


class CheckDbRepository:
    """
    Репозиторий для проверки подключения к БД.
    """

    @staticmethod
    async def check_db(db: AsyncSession) -> DatabaseCheckResponse:
        """
        Проверка подключения к БД.
        """
        app_logger.info('Checking database connection...')

        try:
            await db.execute(select(1))
            app_logger.info('Database connection is OK!')
            return DatabaseCheckResponse(success=True)
        except Exception as e:
            app_logger.exception(e)
            return DatabaseCheckResponse(success=False, message=f'{type(e).__name__}, args: {e.args}')
