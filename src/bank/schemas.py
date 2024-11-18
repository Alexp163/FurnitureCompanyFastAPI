from datetime import datetime

from pydantic import BaseModel


class BankReadSchema(BaseModel):
    id: int
    payment: int
    wallet: float | None
    created_at: datetime
    updated_at: datetime


class BankCreateSchema(BaseModel):
    payment: int
    wallet: float | None


class BankUpdateSchema(BaseModel):
    payment: int
    wallet: float | None
