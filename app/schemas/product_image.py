from pydantic import BaseModel 
from pydantic import ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class ProductImageBase(BaseModel):
    product_id: UUID
    image_url: str
    alt_text: Optional[str] = None
    is_primary: Optional[bool] = None
    

class ProductImageCreate(ProductImageBase):
    pass

class ProductImageUpdate(BaseModel):
    product_id: Optional[UUID] = None
    image_url: Optional[str] = None
    alt_text: Optional[str] = None
    is_primary: Optional[bool] = None

class ProductImageOut(ProductImageBase):
    id: int
    created_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True) 