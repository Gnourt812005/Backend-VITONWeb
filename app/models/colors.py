from sqlalchemy import Column, Integer, Text, UniqueConstraint, PrimaryKeyConstraint
from app.core.database import Base 

class Colors(Base):
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True)
    color_name = Column(Text, nullable=False)
    hex_code = Column(Text, nullable=False)

    __tablearg__ = (
        PrimaryKeyConstraint("id", name="colors_pkey"),
        UniqueConstraint("color_name", name="colors_color_name_key")
    )