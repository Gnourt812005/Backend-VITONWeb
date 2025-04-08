from pydantic import BaseModel 
from pydantic import ConfigDict
from typing import Optional
from uuid import UUID
class ProductColorBase(BaseModel):
    product_id: UUID
    color_id: int
    available: bool

class ProductColorCreate(ProductColorBase):
    pass

class ProductColorUpdate(BaseModel):
    product_id: Optional[UUID] = None
    color_id: Optional[int] = None
    available: Optional[bool] = None

class ProductColorOut(ProductColorBase):
    model_config = ConfigDict(from_attributes=True) 