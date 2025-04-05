from sqlalchemy import Column, Integer, Uuid, ForeignKey, Boolean, Text, DateTime
from app.core.database import Base 

class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True)
    product_id = Column(Uuid, ForeignKey("products.id"))
    image_url = Column(Text, nullable=False)
    alt_text = Column(Text)
    is_primary = Column(Boolean)
    created_at = Column(DateTime)

    
