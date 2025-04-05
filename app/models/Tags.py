from sqlalchemy import Column, Integer, Text
from app.core.database import Base 

class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    tag_name = Column(Text, nullable=False, unique=True)