from pydantic import BaseModel 
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
    class Config:
        from_attributes = True 