from sqlalchemy import Column, Integer, Uuid, ForeignKey, Boolean, PrimaryKeyConstraint
from app.core.database import Base 

class ProductColor(Base):
    __tablename__ = "product_color_availability"
    product_id = Column(Uuid, ForeignKey("products.id"))
    color_id = Column(Integer, ForeignKey("colors.id"))
    available = Column(Boolean)

    __table_args__= (
        PrimaryKeyConstraint("product_id", "color_id")
    )