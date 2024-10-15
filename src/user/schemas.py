from pydantic import BaseModel
from datetime import datetime


class UserReadSchema(BaseModel):
    id: int
    name: str
    age: str
    email: str
    created_at: datetime
    updated_at: datetime


class UserCreateSchema(BaseModel):
    name: str
    age: str
    email: str
    address: str
    password: str

class UserUpdateSchema(BaseModel):
    name: str
    age: str
    email: str
    address: str
    password: str


