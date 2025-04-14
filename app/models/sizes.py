from sqlalchemy import Column, Integer, Text, CheckConstraint, UniqueConstraint, PrimaryKeyConstraint
from app.core.database import Base 
from sqlalchemy.orm import relationship
from app.models.product_size import ProductSize

class Sizes(Base):
    __tablename__ = "sizes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    size_code = Column(Text, nullable=False)
    display_name = Column(Text, nullable=False)

    rlts_product_size = relationship("ProductSize", foreign_keys=[ProductSize.size_id], back_populates="rlts_sizes")


    __table_args__ = (
        PrimaryKeyConstraint("id", name="sizes_pkey"),
        UniqueConstraint("size_code", name="sizes_size_code_key"), 
        CheckConstraint(
            "size_code = ANY (ARRAY['XS', 'S', 'M', 'L', 'XL', 'XXL'])",
            name="sizes_size_code_check"
        )
    )