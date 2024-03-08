from pydantic import BaseModel
from typing import Optional


class ship_info_post(BaseModel):
    name: str
    phone_number: str
    district: str
    city: str
    state: str
    receiver: str
    street: str
    cep: str
    complement: str
    number: int
    principal_ship: Optional[bool] = False


class ship_info_patch(BaseModel):
    name: str
    phone_number: str
    district: str
    city: str
    state: str
    receiver: str
    street: str
    cep: str
    complement: str
    number: int
    principal_ship: Optional[bool] = False
    id: Optional[str] = ''
