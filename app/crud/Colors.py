from app.models.Colors import Colors
from app.schemas.Colors import ColorsCreate, ColorsUpdate
from app.crud.Base import BaseCRUD

class ColorsCRUD(BaseCRUD[Colors, ColorsCreate, ColorsUpdate]):
    pass

colors_crud = ColorsCRUD(Colors)