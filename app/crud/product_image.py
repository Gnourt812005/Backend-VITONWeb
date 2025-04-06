from app.models.product_image import ProductImage
from app.schemas.product_image import ProductImageCreate, ProductImageUpdate
from app.crud.base import BaseCRUD

class ProductImageCRUD(BaseCRUD[ProductImage, ProductImageCreate, ProductImageUpdate]):
    pass

product_image_crud = ProductImageCRUD(ProductImage)