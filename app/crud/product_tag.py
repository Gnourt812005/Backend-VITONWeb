from app.models.product_tag import ProductTag
from app.schemas.product_tag import ProductTagCreate, ProductTagUpdate
from app.crud.basecomposite import BaseCRUDComposite

class ProductTagCRUD(BaseCRUDComposite[ProductTag, ProductTagCreate, ProductTagUpdate]):
    pass

product_tag_crud = ProductTagCRUD(ProductTag)