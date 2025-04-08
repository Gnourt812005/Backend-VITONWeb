from pydantic import BaseModel 
from pydantic import ConfigDict
from typing import Optional

class TagsBase(BaseModel):
    tag_name: str

class TagsCreate(TagsBase):
    pass

class TagsUpdate(BaseModel):
    tag_name: Optional[str] = None

class TagsOut(TagsBase):
    id: int

    model_config = ConfigDict(from_attributes=True) 