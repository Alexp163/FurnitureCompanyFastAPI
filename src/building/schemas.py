from datetime import datetime

from pydantic import BaseModel


class BuildingReadSchema(BaseModel):
    id: int
    name: str  # название здания
    profile: str  # назначение
    year: int  # год постройки
    floors: int  # этажность
    cleaning_id: int | None  # специалист клининга
    engineer_id: int | None  # инженер
    location_id: int | None  # локация
    created_at: datetime  # дата создания
    updated_at: datetime  # дата обновления


class BuildingCreateSchema(BaseModel):
    name: str
    profile: str
    year: int | None
    floors: int | None
    cleaning_id: int | None  # специалист клининга
    engineer_id: int | None  # инженер
    location_id: int | None  # локация


class BuildingUpdateSchema(BaseModel):
    name: str
    profile: str
    year: int | None
    floors: int | None
    cleaning_id: int | None  # специалист клининга
    engineer_id: int | None  # инженер
    location_id: int | None  # локация
