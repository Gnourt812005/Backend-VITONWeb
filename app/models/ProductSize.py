from sqlalchemy import Column, Integer, Uuid, Boolean, PrimaryKeyConstraint, ForeignKeyConstraint
from app.core.database import Base 

class ProductSize(Base):
    __tablename__ = "product_size_availability"
    product_id = Column(Uuid(as_uuid=True))
    size_id = Column(Integer)
    available = Column(Boolean, nullable=False, server_default="true")

    __table_args__ = (
        PrimaryKeyConstraint("product_id", "size_id", name="product_size_availability_pkey"),  # Composite primary key
        ForeignKeyConstraint(["product_id"], ["products.id"], ondelete="CASCADE", name="product_size_availability_product_id_fkey"),  # Foreign key for product_id
        ForeignKeyConstraint(["size_id"], ["sizes.id"], ondelete="CASCADE", name="product_size_availability_size_id_fkey"),  # Foreign key for size_id
    )