from app.models.ProductImage import ProductImage
from app.schemas.ProductImage import ProductImageCreate, ProductImageUpdate
from app.crud.Base import BaseCRUD

class ProductImageCRUD(BaseCRUD[ProductImage, ProductImageCreate, ProductImageUpdate]):
    pass

product_image_crud = ProductImageCRUD(ProductImage)