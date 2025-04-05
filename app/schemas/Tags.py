from pydantic import BaseModel 
from typing import Optional

class TagsBase(BaseModel):
    tag_name: str

class TagsCreate(TagsBase):
    pass

class TagsUpdate(BaseModel):
    tag_name: Optional[str] = None

class TagsOut(TagsBase):
    id: int

    class Config:
        orm_mode = True 