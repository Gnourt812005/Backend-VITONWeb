from sqlalchemy import Column, Integer, Text, Numeric, DateTime, CheckConstraint, PrimaryKeyConstraint, JSON
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.sql import func
from app.core.database import Base 
from sqlalchemy import text
from sqlalchemy.orm import relationship
from app.models.product_image import ProductImage
from app.models.product_color import ProductColor
from app.models.product_size import ProductSize
from app.models.product_tag import ProductTag

class Products(Base):
    __tablename__ = "products"
    id = Column(UUID(as_uuid=True), server_default=text('gen_random_uuid()'))
    name = Column(Text, nullable=False)
    brand = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    original_price = Column(Numeric(10, 2))
    fabric = Column(Text)
    care_instructions = Column(JSON(Text))
    features = Column(JSON(Text))
    stock = Column(Integer, server_default="0")
    average_rating = Column(Numeric(10, 1), server_default="0.0")
    review_count = Column(Integer, server_default="0")
    category = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())  # Default and auto-update


    __table_args__ = (
        PrimaryKeyConstraint("id", name="products_pkey"),
        CheckConstraint("review_count >= 0", name="products_review_count_check"),  # Check constraint
    )

    rlts_product_color = relationship("ProductColor", foreign_keys=[ProductColor.product_id], back_populates="rlts_products")
    rlts_product_size = relationship("ProductSize", foreign_keys=[ProductSize.product_id], back_populates="rlts_products")
    rlts_product_tag = relationship("ProductTag", foreign_keys=[ProductTag.product_id], back_populates="rlts_products")
    rlts_product_image = relationship("ProductImage", foreign_keys=[ProductImage.product_id], back_populates="rlts_products")