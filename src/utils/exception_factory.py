from http import HTTPStatus

from fastapi import HTTPException

from core.config import app_logger


class ExceptionFactory:
    """
    Фабрика исключений.
    """

    @staticmethod
    async def get_400_exception(message: str) -> Exception:
        """
        Фабрика исключений 400.

        :param message: Сообщение об ошибке.
        :return: Исключение 400.
        """
        app_logger.exception(f'Bad request: {message}')
        return HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=message)

    @staticmethod
    async def get_404_exception(message: str) -> Exception:
        """
        Фабрика исключений 404.

        :param message: Сообщение об ошибке.
        :return: Исключение 404.
        """
        app_logger.exception(f'Not found: {message}')
        return HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=message)

    @staticmethod
    async def get_410_exception(message: str) -> Exception:
        """
        Фабрика исключений 410.

        :param message: Сообщение об ошибке.
        :return: Исключение 410.
        """
        app_logger.exception(f'Gone: {message}')
        return HTTPException(status_code=HTTPStatus.GONE, detail=message)
