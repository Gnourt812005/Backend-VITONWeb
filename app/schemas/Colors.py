from pydantic import BaseModel 
from typing import Optional

class ColorsBase(BaseModel):
    color_name: str
    hex_code: str

class ColorsCreate(ColorsBase):
    pass

class ColorsUpdate(BaseModel):
    color_name: Optional[str] = None
    hex_code: Optional[str] = None

class ColorsOut(ColorsBase):
    id: int

    class Config:
        from_attributes = True 