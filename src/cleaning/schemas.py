from datetime import datetime

from pydantic import BaseModel

class CleaningReadSchema(BaseModel):
    id: int
    profile: str # специальность
    experience: str # опыт
    created_at: datetime  # дата создания
    updated_at: datetime  # дата техническая возможность


class CleaningCreateSchema(BaseModel):
    profile: str
    experience: str


class CleaningUpdateSchema(BaseModel):
    profile: str
    experience: str

