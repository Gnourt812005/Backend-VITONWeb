from app.models.ProductColor import ProductColor
from app.schemas.ProductColor import ProductColorCreate, ProductColorUpdate
from app.crud.Base import BaseCRUD

class ProductColorCRUD(BaseCRUD[ProductColor, ProductColorCreate, ProductColorUpdate]):
    pass

product_color_crud = ProductColorCRUD(ProductColor)