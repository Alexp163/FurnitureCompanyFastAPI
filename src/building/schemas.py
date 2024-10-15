from datetime import datetime

from pydantic import BaseModel


class BuildingReadSchema(BaseModel):
    id: int
    name: str  # название здания
    profile: str  # назначение
    year: str  # год постройки
    floors: str  # этажность
    cleaning_id: int  # специалист клининга
    engineer_id: int  # инженер
    location_id: int  # локация
    created_at: datetime  # дата создания
    updated_at: datetime  # дата обновления


class BuildingCreateSchema(BaseModel):
    name: str
    profile: str
    year: str
    floors: str
    cleaning_id: int  # специалист клининга
    engineer_id: int  # инженер
    location_id: int  # локация

class BuildingUpdateSchema(BaseModel):
    name: str
    profile: str
    year: str
    floors: str
    cleaning_id: int  # специалист клининга
    engineer_id: int  # инженер
    location_id: int  # локация