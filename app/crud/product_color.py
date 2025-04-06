from app.models.product_color import ProductColor
from app.schemas.product_color import ProductColorCreate, ProductColorUpdate
from app.crud.basecomposite import BaseCRUDComposite

class ProductColorCRUD(BaseCRUDComposite[ProductColor, ProductColorCreate, ProductColorUpdate]):
    pass

product_color_crud = ProductColorCRUD(ProductColor)