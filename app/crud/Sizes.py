from app.models.Sizes import Sizes
from app.schemas.Sizes import SizesCreate, SizesUpdate
from app.crud.Base import BaseCRUD

class SizesCRUD(BaseCRUD[Sizes, SizesCreate, SizesUpdate]):
    pass

sizes_crud = SizesCRUD(Sizes)