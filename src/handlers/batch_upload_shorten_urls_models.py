from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from schemas import BatchUploadResponse
from schemas import CreateShortenUrlRequest
from utils import ShortenUrlFullRowMapper
from .create_shorten_url_model import create_shorten_url_model


async def batch_upload_shorten_urls_models(
        create_data: List[CreateShortenUrlRequest],
        session: AsyncSession
) -> BatchUploadResponse:
    """
    Логика пакетной загрузки ссылок.

    :param create_data: Данные для пакетной загрузки ссылок.
    :param session: Сессия БД.
    :return: Модель пакетной загрузки ссылок.
    """
    shorten_url_models = list()
    errors = list()
    for data in create_data:
        try:
            shorten_url_model = await create_shorten_url_model(create_data=data, session=session)
            shorten_url_models.append(await ShortenUrlFullRowMapper.get_from_shorten_url_model(data=shorten_url_model))
        except Exception as e:
            errors.append(f'{type(e).__name__}, args: {e.args}')
    return BatchUploadResponse(shorten_url_models=shorten_url_models, errors=errors)
