
from pydantic import BaseModel
from sqlalchemy import UUID


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID
    is_active: bool

    class Config:
        orm_mode = True
