from app.models.Products import Products
from app.schemas.Products import ProductsCreate, ProductsUpdate
from app.crud.Base import BaseCRUD

class ProductsCRUD(BaseCRUD[Products, ProductsCreate, ProductsUpdate]):
    pass

products_crud = ProductsCRUD(Products)