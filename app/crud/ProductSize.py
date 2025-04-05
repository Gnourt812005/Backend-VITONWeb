from app.models.ProductSize import ProductSize
from app.schemas.ProductSize import ProductSizeCreate, ProductSizeUpdate
from app.crud.Base import BaseCRUD

class ProductSizeCRUD(BaseCRUD[ProductSize, ProductSizeCreate, ProductSizeUpdate]):
    pass

product_size_crud = ProductSizeCRUD(ProductSize)