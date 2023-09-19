from typing import List, Union, Optional
from datetime import date
from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str
    email: str
    cpf: str
    phone: str
    password: str
    birth: date


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class PersonLogin(BaseModel):
    email: str
    password: str


class PersonDelete(BaseModel):
    param: str
