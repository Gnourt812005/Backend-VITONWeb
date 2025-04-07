from sqlalchemy import Column, Integer, Text, Numeric, DateTime, CheckConstraint, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.sql import func
from app.core.database import Base 

class Products(Base):
    __tablename__ = "products"
    id = Column(UUID(as_uuid=True), server_default="gen_random_uuid()")
    name = Column(Text, nullable=False)
    brand = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    original_price = Column(Numeric(10, 2))
    fabric = Column(Text)
    care_instructions = Column(ARRAY(Text))
    features = Column(ARRAY(Text))
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
