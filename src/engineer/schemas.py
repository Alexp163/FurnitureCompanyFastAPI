from pydantic import BaseModel
from datetime import datetime


class EngineerReadSchema(BaseModel):
    id: int
    name: str
    special: str
    experience: str
    created_at: datetime
    updated_at: datetime

class EngineerCreateSchema(BaseModel):
    name: str
    special: str
    experience: str


class EngineerUpdateSchema(BaseModel):
    name: str
    special: str
    experience: str
