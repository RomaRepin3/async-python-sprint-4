from models import ShortenUrlModel
from schemas import ShortenUrlCreate
from schemas import ShortenUrlUpdate
from .repository_db import RepositoryDB


class ShortenUrlRepository(RepositoryDB[ShortenUrlModel, ShortenUrlCreate, ShortenUrlUpdate]):
    """
    Репозиторий для работы с сокращёнными URL.
    """
    pass
