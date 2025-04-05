from sqlalchemy import Column, Integer, Text, Numeric, DateTime, Uuid
from app.core.database import Base 

class Products(Base):
    __tablename__ = "products"
    id = Column(Uuid, primary_key=True)
    name = Column(Text, nullable=False)
    brand = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(Numeric, nullable=False)
    original_price = Column(Numeric)
    fabric = Column(Text)
    care_instructions = Column(Text)
    features = Column(Text)
    stock = Column(Integer)
    average_rating = Column(Numeric)
    review_count = Column(Integer)
    category = Column(Text, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
