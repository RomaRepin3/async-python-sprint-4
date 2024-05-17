from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from .base_model import BaseModel


class LinkClickModel(BaseModel):
    """
    Модель для хранения данных по кликам по ссылкам.
    """
    __tablename__ = 'link_click'

    shorten_url_id = Column(Integer, ForeignKey('shorten_url.id'), nullable=False, doc='ID сокращённой ссылки')
