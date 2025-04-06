from app.models.product_size import ProductSize
from app.schemas.product_size import ProductSizeCreate, ProductSizeUpdate
from app.crud.basecomposite import BaseCRUDComposite

class ProductSizeCRUD(BaseCRUDComposite[ProductSize, ProductSizeCreate, ProductSizeUpdate]):
    pass

product_size_crud = ProductSizeCRUD(ProductSize)