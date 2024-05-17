from pydantic import BaseModel
from pydantic import Field


class DatabaseCheckResponse(BaseModel):
    """
    Модель для проверки соединения с базой данных.
    """
    success: bool = Field(description='Статус соединения с базой данных')
    message: str = Field(description='Сообщение', default_factory=str)
