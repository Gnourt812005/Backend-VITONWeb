from sqlalchemy import Column, Integer, Uuid, ForeignKeyConstraint, PrimaryKeyConstraint
from app.core.database import Base 
from sqlalchemy.orm import relationship

class ProductTag(Base):
    __tablename__ = "product_tags"
    product_id = Column(Uuid(as_uuid=True))
    tag_id = Column(Integer)


    rlts_products = relationship("Products", foreign_keys=[product_id], back_populates="rlts_product_tag")
    rlts_tags = relationship("Tags", foreign_keys=[tag_id], back_populates="rlts_product_tag")
   
    __table_args__ = (
        PrimaryKeyConstraint("product_id", "tag_id", name="product_tags_pkey"),  # Composite primary key
        ForeignKeyConstraint(["product_id"], ["products.id"], ondelete="CASCADE", name="product_tags_product_id_fkey"),  # Foreign key for product_id
        ForeignKeyConstraint(["tag_id"], ["tags.id"], ondelete="CASCADE", name="product_tags_tag_id_fkey"),  # Foreign key for size_id
    )