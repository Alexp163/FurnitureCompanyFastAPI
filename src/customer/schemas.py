from pydantic import BaseModel
from datetime import datetime


class CustomerReadSchema(BaseModel):
    id: int
    name: str
    age: str
    rating: str
    wallet: float | None
    created_at: datetime
    updated_at: datetime


class CustomerCreateSchema(BaseModel):
    name: str
    age: str
    rating: str
    wallet: float | None


class CustomerUpdateSchema(BaseModel):
    name: str
    age: str
    rating: str
    wallet: float | None


