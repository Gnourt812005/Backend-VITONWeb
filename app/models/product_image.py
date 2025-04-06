from sqlalchemy import Column, Integer, Uuid, PrimaryKeyConstraint, ForeignKeyConstraint ,Boolean, Text, DateTime
from app.core.database import Base 
from sqlalchemy.sql import func
class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Uuid(as_uuid=True))
    image_url = Column(Text, nullable=False)
    alt_text = Column(Text)
    is_primary = Column(Boolean, server_default="false")
    created_at = Column(DateTime, server_default=func.now())

    __table_args__ = (
        PrimaryKeyConstraint("id", name="product_images_pkey"),
        ForeignKeyConstraint(["product_id"], ['products.id'], name="product_images_product_id_fkey")  
    )

    
