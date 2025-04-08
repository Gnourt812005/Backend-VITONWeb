from pydantic import BaseModel 
from pydantic import ConfigDict
from typing import Optional
from uuid import UUID
class ProductTagBase(BaseModel):
    product_id: UUID
    tag_id: int

class ProductTagCreate(ProductTagBase):
    pass

class ProductTagUpdate(BaseModel):
    product_id: Optional[UUID] = None
    tag_id: Optional[int] = None

class ProductTagOut(ProductTagBase):
    model_config = ConfigDict(from_attributes=True) 