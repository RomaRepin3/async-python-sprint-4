from random import choices
from string import ascii_lowercase

from core.config import app_logger


class CommonUtils:
    """
    Класс для общих утилит.
    """

    @staticmethod
    def get_short_url() -> str:
        """
        Генерация случайного сокращённого URL.

        :return: Сокращённый URL.
        """
        app_logger.info('Generating random short url...')
        return f'https://www.short_url.ru/{"".join(list(choices(ascii_lowercase, k=5)))}'
