from datetime import datetime

from pydantic import BaseModel


class OrderReadSchema(BaseModel):
    id: int
    price: float
    date_order: datetime
    customer_id: int | None
    engineer_id: int | None
    location_id: int | None
    created_at: datetime
    updated_at: datetime


class OrderCreateSchema(BaseModel):
    price: float
    date_order: datetime
    customer_id: int | None
    engineer_id: int | None
    location_id: int | None


class OrderUpdateSchema(BaseModel):
    price: float
    date_order: datetime
    customer_id: int | None
    engineer_id: int | None
    location_id: int | None
