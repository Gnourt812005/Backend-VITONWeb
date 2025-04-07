from app.models.sizes import Sizes
from app.schemas.sizes import SizesCreate, SizesUpdate
from app.crud.base import BaseCRUD

class SizesCRUD(BaseCRUD[Sizes, SizesCreate, SizesUpdate]):
    pass

sizes_crud = SizesCRUD(Sizes)