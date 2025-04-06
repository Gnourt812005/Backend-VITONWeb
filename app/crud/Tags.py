from app.models.tags import Tags
from app.schemas.tags import TagsCreate, TagsUpdate
from app.crud.base import BaseCRUD

class TagsCRUD(BaseCRUD[Tags, TagsCreate, TagsUpdate]):
    pass

tags_crud = TagsCRUD(Tags)