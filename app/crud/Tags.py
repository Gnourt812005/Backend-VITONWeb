from app.models.Tags import Tags
from app.schemas.Tags import TagsCreate, TagsUpdate
from app.crud.Base import BaseCRUD

class TagsCRUD(BaseCRUD[Tags, TagsCreate, TagsUpdate]):
    pass

tags_crud = TagsCRUD(Tags)