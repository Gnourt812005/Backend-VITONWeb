from app.models.colors import Colors
from app.schemas.colors import ColorsCreate, ColorsUpdate
from app.crud.base import BaseCRUD

class ColorsCRUD(BaseCRUD[Colors, ColorsCreate, ColorsUpdate]):
    pass

colors_crud = ColorsCRUD(Colors)