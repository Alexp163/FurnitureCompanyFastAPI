from pydantic import BaseModel
from datetime import datetime


class EngineerReadSchema(BaseModel):
    id: int
    name: str
    special: str
    experience: str
    wallet: float | None
    created_at: datetime
    updated_at: datetime


class EngineerCreateSchema(BaseModel):
    name: str
    special: str
    experience: str
    wallet: float | None

class EngineerUpdateSchema(BaseModel):
    name: str
    special: str
    experience: str
    wallet: float | None
