from black import datetime
from pydantic import BaseModel


class SecurityReadSchema(BaseModel):
    id: int
    name: str
    age: str
    weapon: str
    created_at: datetime
    updated_at: datetime


class SecurityCreateSchema(BaseModel):
    name: str
    age: str
    weapon: str


class SecurityUpdateSchema(BaseModel):
    name: str
    age: str
    weapon: str
