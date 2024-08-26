from datetime import datetime

from pydantic import BaseModel

class LocationReadSchema(BaseModel):
    id: int
    name: str
    city: str
    distance: str
    created_at: datetime
    updated_at: datetime


class LocationCreateSchema(BaseModel):
    name: str
    city: str
    distance: str


class LocationUpdateSchema(BaseModel):
    name: str
    city: str
    distance: str
