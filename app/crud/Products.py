from app.models.products import Products
from app.schemas.products import ProductsCreate, ProductsUpdate
from app.crud.base import BaseCRUD

class ProductsCRUD(BaseCRUD[Products, ProductsCreate, ProductsUpdate]):
    pass

products_crud = ProductsCRUD(Products)