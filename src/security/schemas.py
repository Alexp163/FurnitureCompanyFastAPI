from datetime import datetime
from pydantic import BaseModel


class SecurityReadSchema(BaseModel):
    id: int
    name: str
    age: str
    weapon: str
    wallet: float | None
    created_at: datetime
    updated_at: datetime


class SecurityCreateSchema(BaseModel):
    name: str
    age: str
    weapon: str
    wallet: float | None


class SecurityUpdateSchema(BaseModel):
    name: str
    age: str
    weapon: str
    wallet: float | None

