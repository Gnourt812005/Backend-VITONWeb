from sqlalchemy import Column, Integer, Text
from app.core.database import Base 

class Sizes(Base):
    __tablename__ = "sizes"
    id = Column(Integer, primary_key=True)
    size_code = Column(Text, nullable=False, unique=True)
    display_name = Column(Text, nullable=False)