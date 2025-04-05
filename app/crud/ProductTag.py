from app.models.ProductTag import ProductTag
from app.schemas.ProductTag import ProductTagCreate, ProductTagUpdate
from app.crud.BaseComposite import BaseCRUDComposite

class ProductTagCRUD(BaseCRUDComposite[ProductTag, ProductTagCreate, ProductTagUpdate]):
    pass

product_tag_crud = ProductTagCRUD(ProductTag)