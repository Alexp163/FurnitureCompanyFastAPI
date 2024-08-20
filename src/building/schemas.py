from datetime import datetime

from pydantic import BaseModel


class BuildingReadSchema(BaseModel):
    id: int
    name: str # название здания
    profile: str # назначение
    year: str # год постройки
    floors: str # этажность
    created_at: datetime # дата создания
    updated_at: datetime # дата обновления


class BuildingCreateSchema(BaseModel):
    name: str
    profile: str
    year: str
    floors: str


class BuildingUpdateSchema(BaseModel):
    name: str
    profile: str
    year: str
    floors: str
