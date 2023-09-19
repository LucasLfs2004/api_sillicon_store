from pydantic import BaseModel
from typing import Optional
from datetime import date


class effect_login(BaseModel):
    email: str
    senha: str


# class Person(BaseModel):
#     name: str
#     id: Optional[int] = None
#     cpf: str
#     email: str
#     birth: date
#     phone: str
#     password: str
#     created_at: Optional[int] = None
#     updated_at: Optional[int] = None


class PersonBase(BaseModel):
    name: str
    email: str
    cpf: str
    phone: str
    birth: str
    password: str


class PersonCreate(PersonBase):
    pass


class PersonInDB(PersonBase):
    id: int
    created_at: int
    updated_at: int


class Person(PersonInDB):
    pass


class new_product(BaseModel):
    owner: int
    name: str
    description: str
    brand: str
    price: float
    stock: int
    featured: Optional[bool] = True
    category: str
    active: Optional[bool] = True
    color: Optional[str] = "null"
    created_at: Optional[int] = 0
    updated_at: Optional[int] = 0
    rating: Optional[int] = 0
    id: Optional[str] = None


class new_category(BaseModel):
    id: Optional[str] = None
    name: str
