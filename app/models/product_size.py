from sqlalchemy import Column, Integer, Uuid, Boolean, PrimaryKeyConstraint, ForeignKeyConstraint
from app.core.database import Base 
from sqlalchemy.orm import relationship

class ProductSize(Base):
    __tablename__ = "product_size_availability"
    product_id = Column(Uuid(as_uuid=True))
    size_id = Column(Integer)
    available = Column(Boolean, nullable=False, server_default="true")

    rlts_products = relationship("Products", foreign_keys=[product_id], back_populates="rlts_product_size")
    rlts_sizes = relationship("Sizes", foreign_keys=[size_id], back_populates="rlts_product_size")


    __table_args__ = (
        PrimaryKeyConstraint("product_id", "size_id", name="product_size_availability_pkey"),  # Composite primary key
        ForeignKeyConstraint(["product_id"], ["products.id"], ondelete="CASCADE", name="product_size_availability_product_id_fkey"),  # Foreign key for product_id
        ForeignKeyConstraint(["size_id"], ["sizes.id"], ondelete="CASCADE", name="product_size_availability_size_id_fkey"),  # Foreign key for size_id
    )