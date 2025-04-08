from pydantic import BaseModel 
from typing import Optional
from pydantic import ConfigDict
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

    model_config = ConfigDict(from_attributes=True) 