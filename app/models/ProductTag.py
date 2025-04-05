from sqlalchemy import Column, Integer, Uuid, ForeignKey, Boolean, PrimaryKeyConstraint
from app.core.database import Base 

class ProductTag(Base):
    __tablename__ = "product_tag_availability"
    product_id = Column(Uuid, ForeignKey("products.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))

    __table_args__= (
        PrimaryKeyConstraint("product_id", "tag_id")
    )