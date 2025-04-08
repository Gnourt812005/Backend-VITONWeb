from pydantic import BaseModel 
from pydantic import ConfigDict
from typing import Optional

class SizesBase(BaseModel):
    size_code: str
    display_name: str

class SizesCreate(SizesBase):
    pass

class SizesUpdate(BaseModel):
    size_code: Optional[str] = None
    display_name: Optional[str] = None 

class SizesOut(SizesBase):
    id: int

    model_config = ConfigDict(from_attributes=True) 