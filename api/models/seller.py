from pydantic import BaseModel
from typing import Optional

class offer_product(BaseModel):
    id_product: str
    new_price: Optional[float] = None


class description_product(BaseModel):
    id_product: str
    description: str
