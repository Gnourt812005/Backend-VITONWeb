from sqlalchemy import Column, Integer, Text, UniqueConstraint, PrimaryKeyConstraint
from app.core.database import Base 
from sqlalchemy.orm import relationship
from app.models.product_color import ProductColor

class Colors(Base):
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True)
    color_name = Column(Text, nullable=False)
    hex_code = Column(Text, nullable=False)
    
    rlts_product_color = relationship("ProductColor", foreign_keys=[ProductColor.color_id], back_populates="rlts_colors")

    __table_args__ = (
        PrimaryKeyConstraint("id", name="colors_pkey"),
        UniqueConstraint("color_name", name="colors_color_name_key")
    )