from pydantic import BaseModel
from typing import Optional
from datetime import date


class new_voucher(BaseModel):
    code: str
    discount: float
    expiration: date
    min_value: float
