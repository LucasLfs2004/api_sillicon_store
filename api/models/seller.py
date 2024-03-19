from pydantic import BaseModel
from typing import Optional
from datetime import date


class offer_product(BaseModel):
    id_product: str
    id_seller: str
    new_price: Optional[float] = None
