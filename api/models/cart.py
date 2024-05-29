from pydantic import BaseModel

class ship_cart(BaseModel):
    region: str
    cep: str
    street: str

class ship_cart_id(BaseModel):
    region: str
    id: str