from pydantic import BaseModel 
from pydantic import ConfigDict
from typing import Optional
from uuid import UUID
class ProductSizeBase(BaseModel):
    product_id: UUID
    size_id: int
    available: bool

class ProductSizeCreate(ProductSizeBase):
    pass

class ProductSizeUpdate(BaseModel):
    product_id: Optional[UUID] = None
    size_id: Optional[int] = None
    available: Optional[bool] = None

class ProductSizeOut(ProductSizeBase):
    model_config = ConfigDict(from_attributes=True) 