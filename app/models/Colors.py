from sqlalchemy import Column, Integer, Text
from app.core.database import Base 

class Colors(Base):
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True)
    color_name = Column(Text, nullable=False, unique=True)
    hex_code = Column(Text, nullable=False)