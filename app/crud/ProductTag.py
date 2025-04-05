from app.models.ProductTag import ProductTag
from app.schemas.ProductTag import ProductTagCreate, ProductTagUpdate
from app.crud.Base import BaseCRUD

class ProductTagCRUD(BaseCRUD[ProductTag, ProductTagCreate, ProductTagUpdate]):
    pass

product_tag_crud = ProductTagCRUD(ProductTag)