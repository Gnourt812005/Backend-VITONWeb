from app.models.ProductSize import ProductSize
from app.schemas.ProductSize import ProductSizeCreate, ProductSizeUpdate
from app.crud.BaseComposite import BaseCRUDComposite

class ProductSizeCRUD(BaseCRUDComposite[ProductSize, ProductSizeCreate, ProductSizeUpdate]):
    pass

product_size_crud = ProductSizeCRUD(ProductSize)