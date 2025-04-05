from sqlalchemy import Column, Integer, Text, CheckConstraint, UniqueConstraint, PrimaryKeyConstraint
from app.core.database import Base 

class Sizes(Base):
    __tablename__ = "sizes"
    id = Column(Integer, autoincrement=True)
    size_code = Column(Text, nullable=False)
    display_name = Column(Text, nullable=False)

    __tablearg__ = (
        PrimaryKeyConstraint("id", name="sizes_pkey"),
        UniqueConstraint("size_code", name="sizes_size_code_key"), 
        CheckConstraint(
            "size_code = ANY (ARRAY['XS', 'S', 'M', 'L', 'XL', 'XXL'])",
            name="sizes_size_code_check"
        )
    )