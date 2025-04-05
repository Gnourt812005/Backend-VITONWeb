from sqlalchemy import Column, Integer, Uuid, ForeignKey, Boolean, PrimaryKeyConstraint
from app.core.database import Base 

class ProductSize(Base):
    __tablename__ = "product_size_availability"
    product_id = Column(Uuid, ForeignKey("products.id"))
    size_id = Column(Integer, ForeignKey("sizes.id"))
    available = Column(Boolean)

    __table_args__= (
        PrimaryKeyConstraint("product_id", "size_id")
    )