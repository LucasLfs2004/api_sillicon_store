from pydantic import BaseModel
from typing import Optional
from datetime import date


class effect_login(BaseModel):
    email: str
    password: str


class new_account(BaseModel):
    name: str
    cpf: str
    email: str
    birth: date
    phone: str
    password: str


class UserToken(BaseModel):
    user_id: str


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


class new_comment(BaseModel):
    id_product: str
    title: str
    comment: Optional[str] = None
    rating: float


class new_description(BaseModel):
    id_product: str
    description: str


class new_cart(BaseModel):
    id_person: str
    id_product: str
    amount: int


class update_cart(BaseModel):
    id: str
    amount: int


class apply_discount(BaseModel):
    id_person: str
    code: str


class ship_cart(BaseModel):
    region: str
    cep: str
    street: str
