from http import HTTPStatus
from typing import Annotated
from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from depends import get_session
from depends import link_click_repository
from depends import shorten_url_repository
from schemas import BatchUploadResponse
from schemas import CreateShortenUrlRequest
from schemas import DatabaseCheckResponse
from schemas import GetShortenUrlStatusResponse
from schemas import LinkClick
from schemas import ShortenUrlFull
from services import CheckDbRepository
from utils import ExceptionFactory
from utils import GetShortenUrlStatusResponseRowMapper
from utils import ShortenUrlCreateRowMapper
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
    shorten_url_create = await ShortenUrlCreateRowMapper.get(create_data=create_data)
    try:
        shorten_url_model = await shorten_url_repository.create(db=session, obj_in=shorten_url_create)
    except Exception as e:
        raise await ExceptionFactory.get_400_exception(message=f'{type(e).__name__}, args: {e.args}')
    return await ShortenUrlFullRowMapper.get_from_shorten_url_model(data=shorten_url_model)


@router.post(
    '/batch_upload',
    response_model=BatchUploadResponse, status_code=HTTPStatus.CREATED, name='Пакетная загрузка ссылок.')
async def batch_upload(
        create_data: List[CreateShortenUrlRequest],
        session: Annotated[AsyncSession, Depends(get_session)]
):
    shorten_url_models = list()
    errors = list()
    for data in create_data:
        try:
            shorten_url_create = await ShortenUrlCreateRowMapper.get(create_data=data)
            shorten_url_model = await shorten_url_repository.create(db=session, obj_in=shorten_url_create)
            shorten_url_models.append(
                await ShortenUrlFullRowMapper.get_from_shorten_url_model(data=shorten_url_model)
            )
        except Exception as e:
            errors.append({'full_url': data.full_url, 'error': str(e)})
    return BatchUploadResponse(shorten_url_models=shorten_url_models, errors=errors)


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
    shorten_url_model = await shorten_url_repository.get(db=session, id=shorten_url_id)
    if not shorten_url_model:
        raise await ExceptionFactory.get_404_exception(message='Shorten URL not found')
    elif shorten_url_model.is_deleted:
        raise await ExceptionFactory.get_410_exception(message='Shorten URL is deleted')
    await link_click_repository.create(db=session, obj_in=LinkClick(shorten_url_id=shorten_url_id))
    return RedirectResponse(url=shorten_url_model.full_url)


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
    shorten_url_model = await shorten_url_repository.get(db=session, id=shorten_url_id)
    if not shorten_url_model:
        raise await ExceptionFactory.get_404_exception(message='Shorten URL not found')
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
    shorten_url_model = await shorten_url_repository.get(db=session, id=shorten_url_id)
    if not shorten_url_model:
        raise await ExceptionFactory.get_404_exception(message='Shorten URL not found')
    await shorten_url_repository.delete(db=session, id=shorten_url_id)
    return await ShortenUrlFullRowMapper.get_from_shorten_url_model(data=shorten_url_model)
