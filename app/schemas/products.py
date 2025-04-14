from pydantic import BaseModel 
from pydantic import ConfigDict
from typing import Optional, List, Dict, Any
from decimal import Decimal
from datetime import datetime
from uuid import UUID

class ProductsBase(BaseModel):
    name: str
    brand: str
    description: Optional[str] = None
    price: Decimal
    original_price: Optional[Decimal] = None
    fabric: Optional[str] = None
    care_instructions: Optional[List[str]] = None
    features: Optional[List[str]] = None
    stock: Optional[int] = None
    average_rating: Optional[Decimal] = None
    review_count: Optional[int] = None
    category: str

class ProductsCreate(ProductsBase):
    pass

class ProductsUpdate(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    original_price: Optional[Decimal] = None
    fabric: Optional[str] = None
    care_instructions: Optional[List[str]] = None
    features: Optional[List[str]] = None
    stock: Optional[int] = None
    average_rating: Optional[Decimal] = None
    review_count: Optional[int] = None
    category: Optional[str] = None

class ProductsOut(ProductsBase):
    id: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    sizes: Optional[List[Dict[str, Any]]] = None
    colors: Optional[List[Dict[str, Any]]] = None
    tags: Optional[List[str]] = None
    imageUrl : Optional[str] = None 
    images : Optional[List[Dict[str, Any]]] = None
    model_config = ConfigDict(from_attributes=True) 