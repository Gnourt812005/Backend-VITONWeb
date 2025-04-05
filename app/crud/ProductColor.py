from app.models.ProductColor import ProductColor
from app.schemas.ProductColor import ProductColorCreate, ProductColorUpdate
from app.crud.BaseComposite import BaseCRUDComposite

class ProductColorCRUD(BaseCRUDComposite[ProductColor, ProductColorCreate, ProductColorUpdate]):
    pass

product_color_crud = ProductColorCRUD(ProductColor)