from datetime import datetime

from pydantic import BaseModel


class OrderReadSchema(BaseModel):
    id: int
    price: float
    date_order: datetime
    customer_id: int
    engineer_id: int
    location_id: int
    crated_at: datetime
    updated_at: datetime


class OrderCreateSchema(BaseModel):
    price: float
    date_order: datetime
    customer_id: int
    engineer_id: int
    location_id: int


class OrderUpdateSchema(BaseModel):
    price: float
    date_order: datetime
    customer_id: int
    engineer_id: int
    location_id: int

