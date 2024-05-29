from pydantic import BaseModel
from typing import Optional


class purchase_order(BaseModel):
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

