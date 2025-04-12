from sqlalchemy import Column, Integer, Uuid, ForeignKey, Boolean, PrimaryKeyConstraint, ForeignKeyConstraint
from app.core.database import Base 
from sqlalchemy.orm import relationship

class ProductColor(Base):
    __tablename__ = "product_color_availability"
    product_id = Column(Uuid(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"))
    color_id = Column(Integer, ForeignKey("colors.id", ondelete="CASCADE"))
    available = Column(Boolean, nullable=False, server_default="true")
    
    rlts_products = relationship("Products", foreign_keys=[product_id], back_populates="rlts_product_color")
    rlts_colors = relationship("Colors", foreign_keys=[color_id], back_populates="rlts_product_color")
    
    __table_args__= (
        PrimaryKeyConstraint("product_id", "color_id", name="product_color_availability_pkey"),
        ForeignKeyConstraint(["product_id"], ["products.id"], ondelete="CASCADE", name="product_color_availability_product_id_fkey"),  # Foreign key for product_id
        ForeignKeyConstraint(["color_id"], ["colors.id"], ondelete="CASCADE", name="product_color_availability_color_id_fkey"),  # Foreign key for size_id
    )
