from http import HTTPStatus
from typing import Annotated
from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from depends import get_session
from handlers import batch_upload_shorten_urls_models
from handlers import create_shorten_url_model
from handlers import delete_shorten_url_handler
from handlers import get_original_url
from handlers import get_shorten_url_info
from schemas import BatchUploadResponse
from schemas import CreateShortenUrlRequest
from schemas import DatabaseCheckResponse
from schemas import GetShortenUrlStatusResponse
from schemas import ShortenUrlFull
from services import CheckDbRepository
from utils import ShortenUrlFullRowMapper

router = APIRouter()


@router.get(
    '/ping',
    response_model=DatabaseCheckResponse,
    status_code=HTTPStatus.OK,
    name='Проверка соединения с БД'
)
async def ping(session: Annotated[AsyncSession, Depends(get_session)]):
    return await CheckDbRepository.check_db(db=session)


@router.post('/', response_model=ShortenUrlFull, status_code=HTTPStatus.CREATED, name='Создание сокращённого URL')
async def create_shorten_url(
        create_data: CreateShortenUrlRequest,
        session: Annotated[AsyncSession, Depends(get_session)],
) -> Any:
    shorten_url_model = await create_shorten_url_model(create_data=create_data, session=session)
    return await ShortenUrlFullRowMapper.get_from_shorten_url_model(data=shorten_url_model)


@router.post(
    '/batch_upload',
    response_model=BatchUploadResponse, status_code=HTTPStatus.CREATED, name='Пакетная загрузка ссылок.')
async def batch_upload(
        create_data: List[CreateShortenUrlRequest],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    return await batch_upload_shorten_urls_models(create_data=create_data, session=session)


@router.get(
    '/{shorten_url_id}',
    response_class=RedirectResponse,
    status_code=HTTPStatus.TEMPORARY_REDIRECT,
    name='Возвращает оригинальный URL.'
)
async def get_url(
        shorten_url_id: int,
        session: Annotated[AsyncSession, Depends(get_session)]
):
    return await get_original_url(shorten_url_id=shorten_url_id, session=session)


@router.get(
    '/{shorten_url_id}/status',
    response_model=GetShortenUrlStatusResponse,
    status_code=HTTPStatus.OK,
    name='Возвращает статус использования URL'
)
async def get_shorten_url_status(
        shorten_url_id: int,
        session: Annotated[AsyncSession, Depends(get_session)],
        full_info: bool = True,
        max_result: int = 10,
        offset: int = 0
):
    return await get_shorten_url_info(
        shorten_url_id=shorten_url_id,
        session=session, full_info=full_info,
        max_result=max_result,
        offset=offset
    )


@router.delete(
    '/{shorten_url_id}',
    response_model=ShortenUrlFull,
    status_code=HTTPStatus.OK,
    name='Удаление сокращённой ссылки.'
)
async def delete_shorten_url(
        shorten_url_id: int,
        session: Annotated[AsyncSession, Depends(get_session)]
):
    return await delete_shorten_url_handler(shorten_url_id=shorten_url_id, session=session)
