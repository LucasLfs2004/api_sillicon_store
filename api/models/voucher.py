from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class new_voucher(BaseModel):
    code: str
    discount: float
    expiration: int
    min_value: float
