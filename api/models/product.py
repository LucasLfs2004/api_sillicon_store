from pydantic import BaseModel
from typing import Optional


class update_product_model(BaseModel):
    id: str
    name: str
    model: Optional[str] = None
    category: str
    brand: str
    stock: int
    warranty: int
    price: float
    portions: int
    fees_monthly: float
    fees_credit: float
    active: Optional[bool] = True
    featured: Optional[bool] = False


class new_description(BaseModel):
    id_product: str
    description: str
