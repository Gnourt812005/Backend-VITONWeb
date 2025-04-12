from sqlalchemy import Column, Integer, Text, UniqueConstraint
from app.core.database import Base 
from sqlalchemy.orm import relationship
from app.models.product_tag import ProductTag

class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(Text, nullable=False)

    rlts_product_tag = relationship("ProductTag", foreign_keys=[ProductTag.tag_id], back_populates="rlts_tags")


    __table_args__ = (
        UniqueConstraint("tag_name", name="tags_tag_name_key"),
    )