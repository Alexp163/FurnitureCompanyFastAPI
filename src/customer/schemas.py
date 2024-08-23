from pydantic import BaseModel

from datetime import datetime

class CustomerReadSchema(BaseModel):
    id: int
    name: str
    age: str
    rating: str


class CustomerCreateSchema(BaseModel):
    name: str
    age: str
    rating: str


class CustomerUpdateSchema(BaseModel):
    name: str
    age: str
    rating: str
