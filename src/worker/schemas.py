from pydantic import BaseModel

from datetime import datetime


class WorkerReadSchema(BaseModel):
    id: int
    name: str  # ФИО
    age: str  # возраст
    profession: str  # профессия
    experience: str  # опыт работы
    wallet: float | None
    created_at: datetime
    updated_at: datetime


class WorkerCreateSchema(BaseModel):
    name: str
    age: str
    profession: str
    experience: str
    wallet: float | None


class WorkerUpdateSchema(BaseModel):
    name: str
    age: str
    profession: str
    experience: str
    wallet: float | None
