from decimal import Decimal
from typing import Optional, Set
from pydantic import BaseModel, Field

class ItemModel(BaseModel):
    name: str = Field(...)
    price: Decimal = Field(...)
    quantity: int = Field(...)
    tags: Set[str] = Field(...)

