from pydantic import BaseModel


class EngineerReadSchema(BaseModel):
    id: int
    name: str
    special: str
    experience: str


class EngineerCreateSchema(BaseModel):
    name: str
    special: str
    experience: str


class EngineerUpdateSchema(BaseModel):
    name: str
    special: str
    experience: str
